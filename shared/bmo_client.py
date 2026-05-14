"""Shared Bugzilla REST client used by the sec-approval and uplift-request skills.

Exposes an HTTP wrapper plus helpers for working with Phabricator-request
and raw-patch attachments. Plain module functions; no class. Designed for
import via a `sys.path.insert(..., "../shared")` shim in sibling skill
scripts -- no package install required.

API key resolution (first match wins):
    1. $BMO_API_KEY environment variable
    2. api_key in ~/.config/bugzilla/config.toml
    3. api_key in ~/.config/bmo-to-md/config.toml

## Security model

The Bugzilla API key gives full BMO write access under the user's
identity. It must never enter Claude's conversation context, where
prompt-injection content from bugs Claude later reads could exfiltrate
it. This module is the only place in the repo that touches the key
value, and it enforces a strict no-exposure contract:

- The key is read from disk/env and used as an HTTP header inside this
  module only. No public function in this module returns the key.
- `check_auth()` and `ensure_auth()` are the only public auth probes;
  they report presence and the source path, never the value.
- `api()` resolves the key internally on every call. Callers (CLI
  scripts, future helpers) never see or pass a key value.
- The module-private helpers `_resolve_api_key()` and
  `_require_api_key()` exist so `api()` can obtain the key in-process.
  Nothing outside this module may import them, print them, or invoke
  them ad hoc (e.g., a `python3 -c "from bmo_client import
  _resolve_api_key; print(_resolve_api_key())"` one-liner is a
  contract violation).
"""

import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request


BMO = "https://bugzilla.mozilla.org"
PHAB = "https://phabricator.services.mozilla.com"
BMO_CONFIG = os.path.expanduser("~/.config/bugzilla/config.toml")
BMO_TO_MD_CONFIG = os.path.expanduser("~/.config/bmo-to-md/config.toml")


def _read_toml_api_key(path):
    """Read api_key from a TOML file. Returns the value or None."""
    if not os.path.isfile(path):
        return None
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("api_key"):
                    _, _, val = line.partition("=")
                    val = val.strip().strip('"').strip("'")
                    if val:
                        return val
    except OSError:
        pass
    return None


def _resolve_api_key():
    """Module-private. Resolve the BMO API key.

    Returns (key, source) on success or (None, None) on miss. Must not be
    imported or invoked from outside this module -- see Security model.
    """
    env = os.environ.get("BMO_API_KEY", "").strip()
    if env:
        return env, "$BMO_API_KEY"
    for path in (BMO_CONFIG, BMO_TO_MD_CONFIG):
        val = _read_toml_api_key(path)
        if val:
            return val, path
    return None, None


def _require_api_key():
    """Module-private. Resolve the API key or exit(1) with a hint.

    Used only by `api()` so the key never leaves this module. Must not be
    imported or invoked from outside this module -- see Security model.
    """
    key, _ = _resolve_api_key()
    if not key:
        print("error: no Bugzilla API key found", file=sys.stderr)
        print("Store your key in " + BMO_CONFIG
              + " or set $BMO_API_KEY", file=sys.stderr)
        sys.exit(1)
    return key


def check_auth():
    """Print whether an API key is available (never prints the key)."""
    key, source = _resolve_api_key()
    if key:
        print(f"OK: API key found via {source}")
    else:
        print("No API key found")
        print(f"Store your key in {BMO_CONFIG} or set $BMO_API_KEY")
        sys.exit(1)


def ensure_auth():
    """Exit(1) if no API key is available. Silent on success.

    Use at the top of a CLI run to fail fast before doing local work.
    Unlike `check_auth`, prints nothing on success.
    """
    _require_api_key()


def api(method, path, data=None):
    """Issue an authenticated request to /rest/<path>. Returns parsed JSON.

    The API key is resolved internally; callers never see it. Prints the
    response body and exits 1 on HTTP errors (response body only -- never
    request headers, which is where the key lives).
    """
    url = f"{BMO}/rest/{path}"
    body = json.dumps(data).encode() if data else None
    headers = {
        "Content-Type": "application/json",
        "X-BUGZILLA-API-KEY": _require_api_key(),
    }
    req = urllib.request.Request(url, data=body, headers=headers,
                                 method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        err_body = e.read().decode(errors="replace")
        print(f"error: {method} /rest/{path} -> HTTP {e.code}\n{err_body}",
              file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def extract_phab_revision(attachment):
    """Extract a Phabricator revision ID (e.g. D290715) from an attachment.

    Tries the base64-encoded `data` field first (for
    text/x-phabricator-request attachments this is just the Phabricator URL),
    then falls back to the `summary` field. Returns None if neither matches.
    """
    data = attachment.get("data", "")
    if data:
        try:
            decoded = base64.b64decode(data).decode(errors="replace")
            m = re.search(r'(D\d+)', decoded)
            if m:
                return m.group(1)
        except Exception:
            pass
    summary = attachment.get("summary", "")
    m = re.search(r'(D\d+)', summary)
    if m:
        return m.group(1)
    return None


def format_flags(attachment):
    """Render an attachment's flags as `name1status1, name2status2`."""
    flags = attachment.get("flags", [])
    if not flags:
        return ""
    return ", ".join(f"{f['name']}{f['status']}" for f in flags)


def get_attachments(bug_id, *, phab_only=False, include_data=False):
    """Return active (non-obsolete) patch attachments for a bug.

    phab_only=True   keeps only text/x-phabricator-request attachments.
    phab_only=False  keeps text/x-phabricator-request AND text/plain.

    include_data=False uses include_fields to skip the multi-MB base64 `data`
    payload -- cheap, suitable for listing and flag-setting.
    include_data=True requests the full response (callers that need the
    base64 `data` field for extract_phab_revision must opt in).
    """
    if include_data:
        result = api("GET", f"bug/{bug_id}/attachment")
    else:
        fields = "id,summary,flags,content_type,is_obsolete,file_name"
        result = api("GET",
                     f"bug/{bug_id}/attachment?include_fields={fields}")
    attachments = result.get("bugs", {}).get(str(bug_id), [])
    if phab_only:
        keep_ct = ("text/x-phabricator-request",)
    else:
        keep_ct = ("text/x-phabricator-request", "text/plain")
    return [
        a for a in attachments
        if a.get("content_type") in keep_ct
        and not a.get("is_obsolete")
    ]


def find_single_phab_attachment(bug_id, *, include_data=False):
    """Return the bug's sole active Phabricator-request attachment.

    Exits 1 with a hint if 0 or >1 are found. Always filters by content type
    `text/x-phabricator-request` regardless of `phab_only` -- raw patches
    can't be auto-detected unambiguously.
    """
    atts = get_attachments(bug_id, phab_only=True, include_data=include_data)
    if not atts:
        print(f"error: no active Phabricator attachments found on bug "
              f"{bug_id}", file=sys.stderr)
        print("hint: specify --attachment <id> manually, or use --list",
              file=sys.stderr)
        sys.exit(1)
    if len(atts) > 1:
        print(f"Multiple active Phabricator attachments on bug {bug_id}:",
              file=sys.stderr)
        for a in atts:
            rev = extract_phab_revision(a) or "?"
            flags = format_flags(a)
            print(f"  {a['id']}: {rev}  {a.get('summary', '')}  [{flags}]",
                  file=sys.stderr)
        print("\nhint: specify --attachment <id> or use --list",
              file=sys.stderr)
        sys.exit(1)
    return atts[0]
