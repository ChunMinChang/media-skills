# media-skills
Mozilla Media related agent skills

## Shared utilities

The `shared/` directory holds resources used by more than one skill and is
deployed alongside the individual skill folders (e.g. to
`~/.claude/skills/shared/`):

- `shared/Bugzilla.md` — REST endpoint reference and severity/security
  guidance, parsed by the WebFetch-based skills.
- `shared/bmo_client.py` — Python module with API-key resolution, an
  authenticated HTTP wrapper, and Phabricator/attachment helpers. Imported
  by the `sec-approval` and `uplift-request` scripts via a sibling
  `sys.path` shim.
- `shared/bmo-check-auth` — standalone CLI that any skill (or shell user)
  can run to verify a Bugzilla API key is configured, without ever
  printing it.

**Design principle: the Bugzilla API key never reaches Claude.** Helper
scripts in this repo expose only auth probes (`check_auth`,
`ensure_auth`) and the results of API calls made on the user's behalf —
no function returns or prints the key value. Code added to `shared/` or
to any skill must keep this contract: read the key from disk/env inside
the process that needs it for an HTTP header, and never `print()` or
return it. The internal helpers in `bmo_client.py` that do hold the key
in-process are prefixed with `_` (e.g., `_resolve_api_key`,
`_require_api_key`) and must not be imported outside the module.

Skills are expected to be deployed as a bundle. Copying a single skill
folder without `shared/` will surface a friendly error from any script
that imports `bmo_client`.
