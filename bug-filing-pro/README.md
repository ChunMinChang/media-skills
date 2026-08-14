## bug-filing-pro

File and edit Bugzilla bugs directly through the BMO REST API — the full-power
companion to the form-based [`bug-filing`](https://searchfox.org/mozilla-central/source/.claude/skills/bug-filing)
skill. It does the things the prefilled `enter_bug.cgi` form cannot:

- **Create** a bug and, in the same confirmed run, **upload one or more
  attachments** (logs, patches, reduced testcases, `about:support`, screenshots),
  each with its own summary, content type, and flags.
- **Set flags** at any level: bug flags (`needinfo?`), attachment flags
  (`review?`, `sec-approval?`, `approval-mozilla-*?`, `data-review?`), and
  tracking flags (`cf_status_firefox*`) as fields.
- **Set the status whiteboard** directly with `--whiteboard` when creating or
  updating a bug.
- **Attach to** and **set flags on** existing bugs.

Every write is gated behind a `--dry-run` preview plus explicit confirmation.

### Usage

```
bmo-file-bug create  --product P --component C --summary S --description-file F [...]
bmo-file-bug attach  <bug-id> --attach PATH [--attach PATH ...]
bmo-file-bug flags   <bug-id> --flag 'name:status[:requestee]' [...]
bmo-file-bug list    <bug-id>
bmo-file-bug --check-auth
```

Run any `create`/`attach`/`flags` command with `--dry-run` first to preview the
exact payload; add `--preview html` (default) for a local full-fidelity browser
preview, or `--preview form` to view the body in BMO's native enter-bug form.
Run `bmo-file-bug create --help` for the full option list. See
[`SKILL.md`](./SKILL.md) for the end-to-end workflow.

`create --group` accepts either Bugzilla's internal group name, such as
`media-core-security`, or the visible UI label, such as
`Security-Sensitive Media Bug`. Visible labels are resolved through Bugzilla's
group metadata before the dry-run payload is displayed.

`create --whiteboard TEXT` sets the bug's status whiteboard. The `flags`
subcommand accepts the same option for an existing bug; pass an empty value to
clear it.

### No API key? Body-only fallback

A Bugzilla API key is required to file **attachments and flags** (the whole point
of this skill). But filing a bug's **body** doesn't need one — anyone logged into
bugzilla.mozilla.org can submit a prefilled form themselves. So `create` accepts
`--browser-file`:

```
bmo-file-bug create --product P --component C --summary S --description-file F \
    --browser-file
```

This opens the prefilled `enter_bug.cgi` form in your browser for you to review
and **Submit** under your own account — no key, no API call. It cannot carry
attachments or flags; if you pass any, it lists them so you can add them manually
after filing (or set a key to automate). `attach` and `flags` have no browser
fallback — they always require a key.

| Goal | API key? | How |
|---|---|---|
| File body only, submit it yourself | No | `create … --browser-file` |
| File body **+ attachments + flags** | Yes | `create …` (REST API) |
| Attach to / set flags on a bug | Yes | `attach` / `flags` |

### Dependencies

- **Python 3.8+** (standard library only — no extra packages).
- **`bmo-file-bug` script** — ships with this skill. Imports `bmo_client` from
  the sibling `shared/` directory, which is deployed automatically with the
  media-skills bundle (reached through the installed skill symlink via
  `../shared`).

### Bugzilla API key setup

A Bugzilla API key is required for any API write — creating with attachments or
flags, and all `attach`/`flags` operations. (Body-only filing can skip the key
via `--browser-file`, above.) Generate one at
<https://bugzilla.mozilla.org/userprefs.cgi?tab=apikey>, then pick **one**
storage option. The script checks these sources in order — this is the **same
config used by the `sec-approval` and `uplift-request` skills**, so if those
work, this does too:

| Priority | Source | Notes |
|---|---|---|
| 1 | `BMO_API_KEY` env var | One-off / ephemeral shell |
| 2 | `~/.config/bugzilla/config.toml` | Recommended for daily use |
| 3 | `~/.config/bmo-to-md/config.toml` | Reused if `bmo-to-md` is already configured |

**Option 1 — persistent (recommended):**

```bash
mkdir -p ~/.config/bugzilla
cat > ~/.config/bugzilla/config.toml << 'EOF'
api_key = "YOUR_KEY"
EOF
chmod 600 ~/.config/bugzilla/config.toml
```

**Option 2 — one-off (current shell only):**

```bash
export BMO_API_KEY="YOUR_KEY"
```

Verify the key is wired up without printing it:

```bash
python3 .claude/skills/bug-filing-pro/bmo-file-bug --check-auth
```

### Security

The API key grants full write access under your identity. It is read and used
only inside `shared/bmo_client.py`; no part of this skill ever returns, prints,
or passes the key value. All writes go through that module's authenticated
`api()` helper, and `--check-auth` reports only presence and source path. The
bug is created under the key owner's account, which is why the skill always
previews and asks for confirmation before writing.
