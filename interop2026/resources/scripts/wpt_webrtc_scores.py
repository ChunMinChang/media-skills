#!/usr/bin/env python3
"""
Fetch current WPT scores for Interop 2026 WebRTC tests.

Usage:
    python3 wpt_webrtc_scores.py

Outputs:
    Per-test scores for Firefox, Chrome, and Safari for all tracked
    webrtc/, webrtc/protocol/, and webrtc/simulcast/ paths.

Requirements: Python 3.8+, requests (pip install requests)
"""

import json
import sys
import urllib.request
from collections import defaultdict

WPT_PREFIXES = ["/webrtc/", "/webrtc/protocol/", "/webrtc/simulcast/"]

RUNS_URL = (
    "https://wpt.fyi/api/runs"
    "?label=experimental&label=master"
    "&product=firefox&product=chrome&product=safari"
    "&aligned=true&max-count=1"
)


def fetch_json(url):
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode())


def fetch_results(results_url):
    """Download and parse a wpt summary_v2.json.gz file (actually plain JSON)."""
    with urllib.request.urlopen(results_url) as resp:
        return json.loads(resp.read().decode())


def filter_webrtc(results):
    """Return {path: [passes, total]} for tracked WebRTC paths."""
    out = {}
    for path, counts in results.items():
        for prefix in WPT_PREFIXES:
            if path.startswith(prefix):
                out[path] = counts
                break
    return out


def main():
    print("Fetching latest aligned WPT runs...", file=sys.stderr)
    runs = fetch_json(RUNS_URL)

    browsers = {}
    for run in runs:
        name = run["browser_name"]
        version = run["browser_version"]
        results_url = run["results_url"]
        revision = run["revision"]
        print(f"  {name} {version} @ {revision}  → {results_url}", file=sys.stderr)
        browsers[name] = {
            "version": version,
            "revision": revision,
            "results": filter_webrtc(fetch_results(results_url)),
        }

    # Collect all paths
    all_paths = set()
    for b in browsers.values():
        all_paths.update(b["results"].keys())

    all_paths = sorted(all_paths)

    print()
    print(f"{'Path':<65} {'FF':>8} {'CR':>8} {'SA':>8}")
    print("-" * 95)

    totals = defaultdict(lambda: [0, 0])  # [passes, total] per browser
    for path in all_paths:
        row = f"{path:<65}"
        for bname in ("firefox", "chrome", "safari"):
            b = browsers.get(bname, {})
            counts = b.get("results", {}).get(path, [0, 0])
            p, t = counts[0], counts[1]
            totals[bname][0] += p
            totals[bname][1] += t
            pct = f"{p}/{t}" if t else "n/a"
            row += f" {pct:>8}"
        print(row)

    print("-" * 95)
    print(f"{'TOTAL':<65}", end="")
    for bname in ("firefox", "chrome", "safari"):
        p, t = totals[bname]
        pct = f"{p}/{t} ({100*p//t}%)" if t else "n/a"
        print(f" {pct:>8}", end="")
    print()


if __name__ == "__main__":
    main()
