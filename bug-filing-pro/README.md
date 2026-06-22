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

### Dependencies

- **Python 3.8+** (standard library only — no extra packages).
- **`bmo-file-bug` script** — ships with this skill. Imports `bmo_client` from
  the sibling `shared/` directory, which is deployed automatically with the
  media-skills bundle (reached through the installed skill symlink via
  `../shared`).

### Bugzilla API key setup

A Bugzilla API key is required for every write (create, attach, flag). Generate
one at <https://bugzilla.mozilla.org/userprefs.cgi?tab=apikey>, then pick **one**
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
