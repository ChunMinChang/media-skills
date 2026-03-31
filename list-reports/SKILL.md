---
name: list-reports
description: Launch a local web server and open a browser page listing all bug triage reports in ./reports, with live JS text filtering.
---

# List Bug Triage Reports

Launch a local python web server that displays media-bug-triage reports from your `./reports/` folder, in a filterable and sortable browser UI.

## UI

**Individual rows, each dedicated to summaryzing one report** - In each row, display entries with the following information from the report:

| What | Color | Notes |
|------|-------|-------|
| Bug ID | Green | format: 'Bug NNNNN', linked to the bug in Bugzilla |
| Report generated date | Gray | Date when the report was generated |
| Component | Red | The component to which the bug belongs |
| Severity/Priority | Gray | The severity and priority of the bug |
| Reporter | Black | The user who reported the bug |

Additionally, the browser fetches the following live properties from Bugzilla asynchronously after the page loads, and updates each row as results arrive:

| What | Color | Notes |
|------|-------|-------|
| Status | Green unless RESOLVED, then Black. | The current status of the bug |
| Severity | Red if S1/S2, Green otherwise | The current severity of the bug |
| Priority | Red if P1/P2, Green otherwise | The current priority of the bug |

Finally, display the report's research summary text, up to 500 characters.

## Instructions

Run the following command from the repository root:

```
python3 .claude/skills/list-reports/server.py
```

The script picks a free port automatically and opens the browser. Tell the user:
- The server is running and their browser should have opened automatically.
- Print the url with port number (e.g. http://localhost:12345) in case the browser did not open.
- Users can type in the filter box to search across bug IDs, summaries, components, severity, and report text
- Users can use the **Sort** dropdown to sort by Bug ID, Date, Component, Reporter, Status, Severity, or Priority, and toggle ascending/descending with the arrow button
- Press Ctrl+C in the terminal to stop the server when done

Do not do anything else. Just run the command.

## REST API Quick Reference

| Endpoint | Purpose |
|----------|---------|
| `GET https://bugzilla.mozilla.org/rest/bug/{id}?include_fields=id,summary,status` | Fetch id,summary, and status |
| `GET https://bugzilla.mozilla.org/rest/bug/{id}` | Fetch all bug fields |
| `GET https://bugzilla.mozilla.org/rest/bug/{id}/comment` | Fetch all comments |
| `GET https://bugzilla.mozilla.org/rest/bug/{id}/history` | Fetch change history |
| `GET https://bugzilla.mozilla.org/rest/bug/{id}/attachment` | Fetch attachment metadata |
| `GET https://bugzilla.mozilla.org/rest/bug?product=...&component=...&creation_time=...&summary=...` | Search bugs |

Use the `include_fields` query parameter to limit response size when only a subset of fields is needed.