#!/usr/bin/env python3
"""Dispatch a staged triage draft to bugzilla.mozilla.org.

Reads ``{OUTPUT_ROOT}/triage-bug-{id}/pending.json``, re-fetches the bug,
verifies the draft isn't stale (preferring the saved bug.json snapshot
when present), prompts the user, then issues the REST calls in the
order:

    1. set_fields (priority, severity, status, resolution, ...)
    2. post_comment
    3. set_needinfo (one POST per requestee)

On full success the pending file is removed and a record is appended to
``{OUTPUT_ROOT}/triage-log.json``. On any failure the pending file is
kept so the user can retry; retries are idempotent because already-set
fields are detected via a fresh fetch and skipped.

All HTTP work goes through ``../../shared/bmo_client.py``, which keeps
the API key inside that module's process and never returns it. This
script never sees, prints, or logs the key value.

Exit codes:
    0 success
    1 generic failure
    2 pending file missing
    3 missing API key
    4 partial success (pending preserved)
    5 user aborted at confirmation
    6 stale draft (bug changed since the draft was staged)
"""

import argparse
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _add_shared_to_path():
    """Put the media-skills shared/ dir on sys.path.

    realpath resolves this script's true location, so it works whether the
    skill runs from the source repo, is installed as a symlink, or is
    materialized (the script file is itself a symlink back to source). Walking
    upward finds the sibling shared/ holding bmo_client.py regardless of how
    deep the script sits, and is robust to lexical path normalization.
    """
    d = os.path.dirname(os.path.realpath(__file__))
    while True:
        cand = os.path.join(d, "shared")
        if os.path.isfile(os.path.join(cand, "bmo_client.py")):
            sys.path.insert(0, cand)
            return
        parent = os.path.dirname(d)
        if parent == d:
            return
        d = parent


_add_shared_to_path()
try:
    import bmo_client
except ImportError as e:
    print(f"error: cannot locate shared/bmo_client.py near this script: {e}",
          file=sys.stderr)
    print("hint: install the full media-skills bundle, not just this skill",
          file=sys.stderr)
    sys.exit(2)
import pending_store
import triage_paths


# ---------------------------------------------------------------------------
# BMO REST wrappers — translate bmo_client's sys.exit() failures into
# exceptions so we can preserve partial-success semantics.
# ---------------------------------------------------------------------------


class TriageApplyError(Exception):
    """A BMO REST call failed. bmo_client already wrote details to stderr."""


def _api(method, path, data=None):
    try:
        return bmo_client.api(method, path, data)
    except SystemExit as e:
        raise TriageApplyError(
            "{} /rest/{} failed (exit {})".format(method, path, e.code)
        ) from e


def _get_bug(bug_id):
    result = _api("GET", "bug/{}".format(int(bug_id)))
    bugs = result.get("bugs") or []
    if not bugs:
        raise TriageApplyError("bug {} not found or inaccessible".format(bug_id))
    return bugs[0]


def _post_comment(bug_id, comment):
    return _api(
        "POST",
        "bug/{}/comment".format(int(bug_id)),
        {"comment": comment, "is_private": False},
    )


def _set_fields(bug_id, fields):
    if not fields:
        raise ValueError("_set_fields: refusing to PUT an empty payload")
    return _api("PUT", "bug/{}".format(int(bug_id)), fields)


def _set_needinfo(bug_id, requestee):
    return _api(
        "PUT",
        "bug/{}".format(int(bug_id)),
        {
            "flags": [
                {"name": "needinfo", "status": "?", "requestee": requestee}
            ]
        },
    )


# ---------------------------------------------------------------------------
# Field reconciliation
# ---------------------------------------------------------------------------

# Top-level scalar fields we forward verbatim if present in the pending payload.
SCALAR_FIELDS = (
    "priority",
    "severity",
    "status",
    "resolution",
    "dupe_of",
    "product",
    "component",
)

# Pending-payload keys that map to BMO {add: [...]} field shapes.
ADD_LIST_FIELDS = {
    "cc_add": "cc",
    "blocks_add": "blocks",
    "keywords_add": "keywords",
    "see_also_add": "see_also",
}


def build_field_payload(pending, current):
    """Return the dict for set_fields(...), with already-set values skipped.

    ``pending`` is the staged JSON. ``current`` is the freshly fetched bug.
    For scalar fields we compare against the bug's current value; for list
    fields we compute the missing additions.
    """
    payload = {}
    for key in SCALAR_FIELDS:
        if key not in pending or pending[key] in (None, ""):
            continue
        new = pending[key]
        if str(current.get(key, "")) == str(new):
            continue  # already set; idempotent skip
        payload[key] = new

    for src, dst in ADD_LIST_FIELDS.items():
        additions = pending.get(src) or []
        if not additions:
            continue
        current_vals = current.get(dst) or []
        # Normalise to comparable strings for set arithmetic on mixed types.
        current_set = {str(v) for v in current_vals}
        missing = [v for v in additions if str(v) not in current_set]
        if missing:
            payload[dst] = {"add": missing}
    return payload


# ---------------------------------------------------------------------------
# Confirmation prompt
# ---------------------------------------------------------------------------


def render_plan(bug_id, fields, pending):
    """Human-readable diff of intended REST calls."""
    lines = ["", "Plan for bug {}:".format(bug_id)]
    if fields:
        lines.append("  PUT  /bug/{}".format(bug_id))
        for k, v in sorted(fields.items()):
            lines.append("    {} = {}".format(k, v))
    else:
        lines.append("  (no field changes)")
    if pending.get("comment"):
        snippet = pending["comment"].splitlines()[0][:80]
        lines.append("  POST /bug/{}/comment".format(bug_id))
        lines.append("    {}…".format(snippet))
    for target in pending.get("ni_targets") or []:
        lines.append("  PUT  /bug/{} (needinfo? {})".format(bug_id, target))
    lines.append("")
    return "\n".join(lines)


def prompt_confirm(stream=None):
    """Return True iff the user typed 'y' or 'yes' (case-insensitive)."""
    stream = stream or sys.stdin
    sys.stdout.write("Proceed? [y/N] ")
    sys.stdout.flush()
    try:
        answer = stream.readline()
    except (KeyboardInterrupt, EOFError):
        return False
    if not answer:
        return False
    return answer.strip().lower() in ("y", "yes")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def _today():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


def _now():
    return pending_store.now_iso_utc()


def _decision_from_branch(pending):
    branch = pending.get("branch", "")
    if branch == "1a":
        return "ni_sent"
    if branch == "1b":
        return "triaged"
    if branch == "1c":
        resolution = (pending.get("resolution") or "").lower()
        return resolution or "closed"
    return "applied"


def _ensure_api_key():
    """Require a BMO API key before doing any REST work.

    bmo_client.ensure_auth() exits 1 on missing key. We catch that so we
    can return our own exit code with a triage-flavoured message.
    """
    try:
        bmo_client.ensure_auth()
    except SystemExit:
        return False
    return True


def run(bug_id, dry_run=False, assume_yes=False, stdin=None):
    pending = pending_store.load_pending(bug_id)
    if pending is None:
        sys.stderr.write(
            "apply_pending: no pending file at {}\n".format(
                pending_store.pending_path(bug_id)
            )
        )
        return 2

    # Apply implies writes, so the key must be present even for a dry run
    # (the dry run still fetches the bug to validate the staleness check).
    if not _ensure_api_key():
        sys.stderr.write(
            "apply_pending: no BMO API key found. Configure "
            "~/.config/bugzilla/config.toml or set $BMO_API_KEY. Pending "
            "draft preserved at {}.\n".format(pending_store.pending_path(bug_id))
        )
        return 3

    try:
        bug = _get_bug(bug_id)
    except TriageApplyError as e:
        sys.stderr.write("apply_pending: fetch failed: {}\n".format(e))
        return 1

    fresh_lct = bug.get("last_change_time", "")
    snapshot = pending_store.load_bug_snapshot(bug_id)
    if snapshot is not None:
        stale = pending_store.is_stale_against_snapshot(bug_id, fresh_lct)
        snapshot_lct = snapshot.get("last_change_time")
    else:
        stale = pending_store.is_stale(pending, fresh_lct)
        snapshot_lct = pending.get("created_at")
    if stale:
        sys.stderr.write(
            "apply_pending: stale draft — bug {} changed at {} (snapshot "
            "at {}). Re-run the triage skill to refresh.\n".format(
                bug_id, fresh_lct, snapshot_lct
            )
        )
        return 6

    fields = build_field_payload(pending, bug)
    sys.stdout.write(render_plan(bug_id, fields, pending))

    if dry_run:
        sys.stdout.write("(dry run — no REST calls issued)\n")
        return 0

    if not assume_yes and not prompt_confirm(stdin):
        sys.stdout.write("Aborted.\n")
        return 5

    succeeded = []
    failed = []

    # 1. Fields
    if fields:
        try:
            _set_fields(bug_id, fields)
            succeeded.append("set_fields")
        except TriageApplyError as e:
            failed.append(("set_fields", str(e)))
            sys.stderr.write("apply_pending: set_fields failed: {}\n".format(e))

    # 2. Comment
    comment = pending.get("comment") or ""
    if comment.strip():
        try:
            _post_comment(bug_id, comment)
            succeeded.append("post_comment")
        except TriageApplyError as e:
            failed.append(("post_comment", str(e)))
            sys.stderr.write("apply_pending: post_comment failed: {}\n".format(e))

    # 3. Needinfo flags (one PUT per requestee — keeps reporting clean).
    for target in pending.get("ni_targets") or []:
        try:
            _set_needinfo(bug_id, target)
            succeeded.append("set_needinfo:{}".format(target))
        except TriageApplyError as e:
            failed.append(("set_needinfo:{}".format(target), str(e)))
            sys.stderr.write(
                "apply_pending: set_needinfo({}) failed: {}\n".format(target, e)
            )

    # Audit log entry.
    log_entry = {
        "bug_id": int(bug_id),
        "date": _today(),
        "applied_at": _now(),
        "scope": pending.get("scope"),
        "branch": pending.get("branch"),
        "priority_set": pending.get("priority"),
        "severity_set": pending.get("severity"),
        "comment_posted": "post_comment" in succeeded,
        "ni_targets": pending.get("ni_targets") or [],
        "succeeded": succeeded,
        "failed": [f[0] for f in failed],
    }
    if failed:
        log_entry["decision"] = "apply_partial"
        log_entry["failures"] = [{"step": step, "error": msg} for (step, msg) in failed]
        pending_store.append_log_entry(log_entry)
        sys.stderr.write(
            "apply_pending: partial success ({} ok, {} failed). "
            "Pending draft preserved for retry.\n".format(len(succeeded), len(failed))
        )
        return 4

    log_entry["decision"] = _decision_from_branch(pending)
    pending_store.append_log_entry(log_entry)
    pending_store.delete_pending(bug_id)
    sys.stdout.write(
        "apply_pending: success ({}). Pending draft removed.\n".format(
            ", ".join(succeeded) or "no-op"
        )
    )
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Apply a staged triage draft to bugzilla.mozilla.org."
    )
    parser.add_argument("bug_id", type=int, help="Bugzilla bug id")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned REST calls without issuing them.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip the interactive confirmation prompt.",
    )
    parser.add_argument(
        "--output-dir",
        metavar="PATH",
        default=None,
        help="Override output_dir from the TOML config for this run.",
    )
    args = parser.parse_args(argv)
    if args.output_dir:
        triage_paths.set_override(args.output_dir)
    try:
        return run(args.bug_id, dry_run=args.dry_run, assume_yes=args.yes)
    except triage_paths.OutputRootUnset as e:
        sys.stderr.write("apply_pending: {}\n".format(e))
        return 1
    except KeyboardInterrupt:
        sys.stderr.write("\napply_pending: interrupted\n")
        return 1
    except Exception as e:  # pragma: no cover - last-ditch
        sys.stderr.write("apply_pending: unexpected error: {}\n".format(e))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
