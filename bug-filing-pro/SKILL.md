---
name: bug-filing-pro
description: File a Bugzilla bug directly via the BMO REST API with full power the prefilled enter_bug.cgi form can't do — create the bug AND upload one or more attachments (logs, patches, testcases, screenshots) AND set bug-/attachment-level flags (needinfo?, review?, sec-approval?, approval-mozilla-*?, tracking flags) in one confirmed operation. Also attaches files to, and sets flags on, existing bugs. Use when the user wants to actually submit a bug (not just open a draft form), attach files while filing, or set flags. For a simple file-it-myself-in-the-browser draft with no attachments, prefer the form-based `bug-filing` skill instead. Requires a Bugzilla API key.
argument-hint: "create | attach <bug-id> | flags <bug-id> (see README)"
allowed-tools:
  - Bash(python3:*)
  - Bash(./mach file-info:*)
  - Read
  - Glob
  - AskUserQuestion
  - Write
---

# Bug Filing (Pro) Skill

Files and edits Bugzilla bugs through the BMO REST API, so it can do what the
form-based `bug-filing` skill cannot: **submit the bug, attach multiple files,
and set every flag** — in a single confirmed run.

> Dependencies and Bugzilla API-key setup live in [`README.md`](./README.md).
> Point the user there if `bmo-file-bug --check-auth` fails.

## When to use this vs. the form-based `bug-filing` skill

- **This skill (`bug-filing-pro`)** — the user wants the bug *actually filed*,
  needs to **attach files** (logs, patches, reduced testcases, `about:support`,
  screenshots) and/or **set flags**, or wants to attach/flag an **existing** bug.
- **Plain `bug-filing`** — the user just wants a prefilled `enter_bug.cgi` form
  opened to review and submit by hand, with no attachments or flags.

The bug is created under the API-key owner's identity. Because of that, **every
write is gated**: always dry-run + preview, then get explicit confirmation,
*then* file. Never skip the confirmation step.

## Security

The Bugzilla API key grants full write access under the user's identity. It is
resolved inside `shared/bmo_client.py` and **never enters the conversation**.
Never read, echo, or pass the key. To verify it is wired up (prints presence and
source path, never the value):

```
python3 .claude/skills/bug-filing-pro/bmo-file-bug --check-auth
```

## Workflow (filing a new bug)

### Step 1 — Determine product and component
If the change touches a file in the tree, run
`./mach file-info bugzilla-component <file>` on a representative file. Output is
`Product :: Component`; split on `::`. If it returns `UNKNOWN`, pick the closest
sensible component. Otherwise ask the user.

### Step 2 — Choose the bug type
- `defect` — shipping software misbehaving (regression, crash, error).
- `enhancement` — a new feature, or changing how a feature behaves.
- `task` — config/refactor/tooling/tests/docs with no user-facing change.

### Step 3 — Draft the summary and description
- Keep the summary short and specific.
- Wrap code identifiers (functions, vars, files, prefs, flags) in backticks.
- For a test-failure bug, link the test dashboard:
  `https://tests.firefox.dev/test.html?test=<path>`.
- Write the description to a file and pass it with `--description-file` (so real
  newlines and markdown survive shell quoting).

### Step 4 — Gather attachments and flags
- Simple files: one `--attach <path>` each (type and `is_patch` auto-detected).
- For per-attachment summaries/flags/privacy, write an `--attachments-json` file
  (schema below).
- Bug-level flags: `--flag 'name:status[:requestee]'` (e.g.
  `--flag 'needinfo:?:dev@mozilla.com'`).
- Tracking flags are *fields*, not flags: `--field cf_status_firefox142=affected`.

### Step 5 — Dry-run and preview (REQUIRED)
Run with `--dry-run`. Default `--preview html` opens a local page rendering the
full request (fields, flags, attachments table); use `--preview form` to show
the body in BMO's native enter-bug form (body only — do not submit it).

```
python3 .claude/skills/bug-filing-pro/bmo-file-bug create \
    --product Core --component "Audio/Video: Playback" \
    --summary "<summary>" --description-file /tmp/desc.md \
    --type defect --severity S2 --priority P2 \
    --flag 'needinfo:?:dev@mozilla.com' \
    --attach /tmp/crash.log --attach /tmp/fix.patch \
    --dry-run --preview html
```

Show the user the printed payload.

### Step 6 — Confirm, then file
Confirm with `AskUserQuestion`, "Looks good, file the bug" as the first
(recommended) option. Only on approval, re-run the **exact same command without
`--dry-run`** (and without `--preview`). The script creates the bug, uploads each
attachment, sets flags, then prints the bug URL.

If an attachment fails after the bug is created, the script reports which
succeeded and prints the precise `bmo-file-bug attach <id> …` retry command —
relay it; the bug itself is already filed.

## Other operations

**Attach to an existing bug:**
```
python3 .claude/skills/bug-filing-pro/bmo-file-bug attach <bug-id> \
    --attach /tmp/repro.html --dry-run --preview html
```

**Set flags / fields on a bug or attachment:**
```
python3 .claude/skills/bug-filing-pro/bmo-file-bug flags <bug-id> \
    --flag 'needinfo:?:dev@mozilla.com' --field cf_status_firefox142=fixed \
    --attachment <attId> --attachment-flag 'review:+' --dry-run
```

**List a bug's attachments and their flags:**
```
python3 .claude/skills/bug-filing-pro/bmo-file-bug list <bug-id>
```

## Reference

### Flag syntax
`name:status[:requestee]` — status is one of `?` `+` `-` `X`. Colon-separated so
hyphenated names (`sec-approval`, `approval-mozilla-beta`) are unambiguous.
Examples: `review:?:rev@mozilla.com`, `sec-approval:?`, `approval-mozilla-beta:+`.

### `--attachments-json` schema (array of objects)
```json
[
  {
    "path": "/tmp/fix.patch",
    "summary": "Proposed fix",
    "file_name": "fix.patch",
    "content_type": "text/plain",
    "is_patch": true,
    "is_private": false,
    "comment": "optional comment posted with the attachment",
    "flags": [{"name": "review", "status": "?", "requestee": "rev@mozilla.com"}]
  }
]
```
Only `path` is required; everything else is auto-detected or optional.

## Notes
- A new bug is created under the API-key owner's account — confirm before filing.
- BMO has no atomic "create + attach" call: the script creates the bug, then
  uploads attachments one per request, all within the single confirmed run.
