#!/usr/bin/env python3
"""Sweep GitHub for recently-created RAG repos with early traction.

The arXiv digest misses repo-first waves — tools and engines that ship
before any paper (the 2026-09 decision-layer wave lived as repos for
weeks before the writeups). This sweep searches for repositories created
within the last WINDOW_DAYS days that match RAG keywords, keeps those
with early traction, and writes a curation draft next to the arXiv one
in news/_drafts/. A human decides what graduates — radar, main tables,
or neither.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "news" / "_drafts"

QUERIES = ("rag", "retrieval augmented generation", '"knowledge base" llm')
WINDOW_DAYS = 14
MIN_STARS = 20
HEADERS = {"Accept": "application/vnd.github+json", "User-Agent": "Awesome-RAG-Frontier-sweep"}


def search(token: str | None, query: str, cutoff: str) -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "q": f"{query} created:>{cutoff}",
            "sort": "stars",
            "order": "desc",
            "per_page": 30,
        }
    )
    headers = dict(HEADERS)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(
        "https://api.github.com/search/repositories?" + params, headers=headers
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response).get("items", [])
        except urllib.error.HTTPError as error:
            if error.code in (403, 429) and attempt < 2:
                print(f"search throttled ({error.code}), backing off 20s", file=sys.stderr)
                time.sleep(20)
                continue
            print(f"search failed for {query!r}: {error}", file=sys.stderr)
            return []
    return []


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    cutoff = (date.today() - timedelta(days=WINDOW_DAYS)).isoformat()

    tracked: set[str] = set()
    for name in ("projects.json", "radar.json"):
        path = ROOT / "data" / name
        if path.exists():
            tracked |= {
                item["repo"]
                for item in json.loads(path.read_text(encoding="utf-8")).get("items", [])
            }

    found: dict[str, dict] = {}
    for query in QUERIES:
        for item in search(token, query, cutoff):
            full = item["full_name"]
            if full in tracked or item["stargazers_count"] < MIN_STARS:
                continue
            found.setdefault(
                full,
                {
                    "stars": item["stargazers_count"],
                    "created": (item.get("created_at") or "")[:10],
                    "desc": (item.get("description") or "").strip(),
                    "url": item.get("html_url") or f"https://github.com/{full}",
                },
            )
        time.sleep(2)  # search API courtesy pause

    rows = sorted(found.values(), key=lambda row: -row["stars"])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"github-sweep-{date.today().isoformat()}.md"
    lines = [
        "<!-- draft: auto-generated GitHub sweep candidates, not yet curated -->",
        f"# GitHub sweep — {date.today().isoformat()}",
        "",
        f"{len(rows)} new RAG-flavored repos created since {cutoff} with ≥{MIN_STARS} stars "
        f"(searches: {' / '.join(QUERIES)}; tracked entries already excluded). "
        "Curate: radar-worthy? main-table-worthy? neither? Check the keepers, delete the rest.",
        "",
    ]
    for full, row in sorted(found.items(), key=lambda pair: -pair[1]["stars"]):
        lines.append(f"- [ ] **{full}** — {row['stars']}★ — created {row['created']} — {row['url']}")
        lines.append(f"      > {row['desc'] or '(no description)'}")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(rows)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
