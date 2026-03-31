#!/usr/bin/env python3
"""Bug triage report browser - serves a filterable list of ./reports/bug-*-triage.md files."""

import http.server
import json
import re
import sys
import threading
import webbrowser
from pathlib import Path

REPORTS_DIR = Path(__file__).parent.parent.parent.parent / "reports"


def parse_report(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    def field(pattern, default=""):
        m = re.search(pattern, text)
        return m.group(1).strip() if m else default

    bug_id_match = re.match(r"bug-(\d+)-triage", path.stem)
    bug_id = bug_id_match.group(1) if bug_id_match else path.stem

    severity_priority = field(r"\*\*Severity\s*/\s*Priority:\*\*\s*(.+)")
    if not severity_priority:
        sev = field(r"\*\*Severity:\*\*\s*(.+)")
        pri = field(r"\*\*Priority:\*\*\s*(.+)")
        if sev or pri:
            severity_priority = f"{sev} / {pri}"

    research_summary_match = re.search(r"## Research Summary[^\n]*\n\n([\s\S]*?)(?:\n## |\Z)", text)
    research_summary = research_summary_match.group(1).strip() if research_summary_match else ""

    return {
        "id": bug_id,
        "filename": path.name,
        "generated": field(r"\*\*Generated:\*\*\s*(.+)"),
        "bug_url": field(r"\*\*Bug URL:\*\*\s*(https?://\S+)"),
        "summary": field(r"\*\*Summary:\*\*\s*(.+)"),
        "reporter": field(r"\*\*Reporter:\*\*\s*(.+)"),
        "product": field(r"\*\*Product:\*\*\s*(.+)"),
        "component": field(r"\*\*Component:\*\*\s*(.+)"),
        "severity_priority": severity_priority,
        "security_sensitive": field(r"\*\*Security Sensitive:\*\*\s*(.+)"),
        "research_summary": research_summary,
        "full_text": text,
        "file_url": path.resolve().as_uri(),
    }


def load_reports() -> list:
    if not REPORTS_DIR.exists():
        return []
    reports = []
    for p in sorted(REPORTS_DIR.glob("bug-*-triage.md"), reverse=True):
        try:
            reports.append(parse_report(p))
        except Exception as e:
            print(f"Warning: could not parse {p.name}: {e}", file=sys.stderr)
    return reports


_TEMPLATE_PATH = Path(__file__).parent / "template.html"


def make_html(reports: list) -> bytes:
    payload = json.dumps(reports, ensure_ascii=False)
    html = _TEMPLATE_PATH.read_text(encoding="utf-8").replace("__REPORTS_JSON__", payload)
    return html.encode("utf-8")


class Handler(http.server.BaseHTTPRequestHandler):
    html_bytes: bytes = b""

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(self.html_bytes)))
            self.end_headers()
            self.wfile.write(self.html_bytes)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, fmt, *args):
        pass  # suppress request logging


def main():
    reports = load_reports()
    print(f"Loaded {len(reports)} triage reports from {REPORTS_DIR}", file=sys.stderr)

    Handler.html_bytes = make_html(reports)

    server = http.server.HTTPServer(("", 0), Handler)
    port = server.server_address[1]
    url = f"http://localhost:{port}/"
    print(f"Serving at {url}  (Ctrl+C to stop)", file=sys.stderr)

    threading.Timer(0.3, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.", file=sys.stderr)


if __name__ == "__main__":
    main()
