# Firefox Bug Triage skill

Single-bug interactive triage for bugzilla.mozilla.org. Fetches a bug,
classifies signals, scopes Bugzilla searches to a profile
(`media` / `web-conferencing` / `media-and-web-conferencing` /
`graphics` / `android`), drafts a response, optionally generates a
test page, and stages a pending draft that can be applied to BMO via
REST after explicit user approval.

See `SKILL.md` for the full prompt; this file is the operator-facing
README.

## Invocation

- `/triage` — prompt for a bug number.
- `/triage 1234567` — analyse bug 1234567 (scope inferred).
- `/triage Bug 1234567`
- `/triage https://bugzilla.mozilla.org/show_bug.cgi?id=1234567`
- `/triage 1234567 scope:graphics` — override scope.
- `/triage 1234567 out:/path/to/dir` — one-shot output-root override.

## Outputs

Every artifact for one bug lives in one folder under `{OUTPUT_ROOT}`:

```
{OUTPUT_ROOT}/
├── triage-log.json                  # append-only audit array
└── bug-{ID}/
    ├── triage.md                    # the report
    ├── pending.json                 # staged draft (consumed by apply_pending.py)
    ├── test.html                    # optional test page
    ├── bug.json                     # snapshot used for the stale check
    ├── findings.json                # optional — codebase findings
    └── usage.json                   # optional — Bugzilla usage stats
```

## Configuration

`OUTPUT_ROOT` resolution order (first match wins):

1. `out:<path>` token on the `/triage` command (per-invocation).
2. `output_dir` in `~/.config/firefox-triage/config.toml`.
3. Interactive prompt — the skill asks where the folder should live
   and offers to persist the answer to the TOML.

There is **no built-in default**. If no source is set and the skill is
invoked non-interactively (e.g. running `apply_pending.py` directly),
the call exits with a clear error rather than guessing a location.

### TOML config — `~/.config/firefox-triage/config.toml`

This file controls **output behaviour only**. Do not store an `api_key`
here — see the API-key section below.

```toml
output_dir    = "/home/cm/triage"
default_scope = "media"             # optional — fallback when neither
                                    #   inference nor scope: matches
```

The TOML reader is a minimal stdlib parser that understands top-level
scalars only (no sections, no arrays).

## Security: API-key handling

The Bugzilla API key gives full BMO write access under the user's
identity. The skill must **never** load it into the Claude session.

- **All REST work routes through `../../shared/bmo_client.py`.** The
  key is read inside that module's subprocess, used as an HTTP header,
  and never returned. `apply_pending.py` calls `bmo_client.ensure_auth()`
  to fail-fast on a missing key and `bmo_client.api()` for each
  request; neither returns a key.
- **Authentication probing** goes through
  `../../shared/bmo-check-auth` — silent on success, prints
  remediation on failure, never echoes the value.
- **The skill does not Read or cat** `~/.config/bugzilla/config.toml`,
  `~/.config/bmo-to-md/config.toml`, any `~/.config/bmo*` file, or any
  other path the user identifies as credentialled. SKILL.md restates
  this as a hard rule for Claude.

Key resolution order (handled inside `bmo_client.py`):

1. `$BMO_API_KEY` environment variable.
2. `api_key` in `~/.config/bugzilla/config.toml`.
3. `api_key` in `~/.config/bmo-to-md/config.toml`.

Generate a key at <https://bugzilla.mozilla.org/userprefs.cgi?tab=apikey>.
Reads of public bugs work anonymously, but `apply` requires writes and
will exit 3 if no key is found.

## scripts/

| File | Role |
|---|---|
| `triage_paths.py` | Library + CLI — output-root resolution, per-bug path helpers, TOML reader/writer. CLI used by the prompt-and-persist flow (`--get-output-dir`, `--set-output-dir PATH`, `--get-default-scope`, `--config-path`). Does **not** read or write `api_key`. |
| `pending_store.py` | Library — atomic JSON I/O for pending drafts, bug snapshots, and the audit log. |
| `scope_profiles.py` | Library — five profile tables + `infer_profile()`. |
| `apply_pending.py` | CLI — invoked on `apply {id}`. Imports `../../shared/bmo_client.py` for all BMO REST. Accepts `--output-dir PATH`. Exit codes 0/1/2/3/4/5/6. |
| `render_report.py` | CLI — renders `{root}/bug-{id}/triage.md`. Accepts `--output-dir PATH`. |
| `test_triage_scripts.py` | stdlib unittest, 54 tests. |

### Tests

```sh
cd media-bug-triage-v2/scripts
python3 -m unittest test_triage_scripts
```

All tests are stdlib-only; no network is touched (`bmo_client.api` is
mocked).

### Dry-run an apply

```sh
python3 media-bug-triage-v2/scripts/apply_pending.py 1234567 --dry-run
```

Prints the planned `PUT /bug/{id}` and `POST /bug/{id}/comment` calls,
issues none. Still requires an API key (the dry run fetches the bug
through `bmo_client` for the stale check).

## Required external tools

| Tool | Path | Required? | Used for |
|---|---|---|---|
| `mcp__moz__get_bugzilla_bug` | MCP | yes (primary read) | Bug + comments + history fetch. |
| `bmo-to-md` | `~/.cargo/bin/bmo-to-md` | optional | Markdown render of a bug. |
| `searchfox-cli` | `~/.cargo/bin/searchfox-cli` | optional | Codebase search (Step 7). |
| `socorro-cli`, `profiler-cli` | not installed by default | optional | Skipped gracefully if absent. |

## Out of scope

This skill is **single-bug interactive only**. The following are
intentionally not implemented (hooks reserved):

- Batch from a buglist URL.
- Watch-list polling / stale-NI detection across sessions.
- Cron daemon mode.
- Wiki write-back via `/firefox-wiki:add`.

See `~/Work/worklog/mozilla/triage-skills-comparison.md` for a
landscape view of other triage tooling (`media-bug-triage`,
`alwu-claude-skills/triage`, `triage-wizard`) and when to use each.
