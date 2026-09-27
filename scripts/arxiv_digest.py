#!/usr/bin/env python3
"""Generate an arXiv digest draft of recent RAG papers for human curation.

Pulls the newest submissions from RAG-relevant arXiv categories and filters
them locally against RAG keywords, instead of relying on server-side phrase
search — the export endpoint rejects complex search_query values in some
environments (HTTP 406). The exact request shape below (cat:<category> +
sortBy + sortOrder + max_results) is verified against the live API.

Writes news/_drafts/arxiv-<date>.md as a checklist, not the final digest —
a human picks the keepers and folds them into README → Papers and the next
news post.
"""
from __future__ import annotations

import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "news" / "_drafts"
ATOM = "{http://www.w3.org/2005/Atom}"

CATEGORIES = ("cs.CL", "cs.IR", "cs.AI", "cs.LG")
KEYWORDS = ("retrieval-augmented", "retrieval augmented", "graphrag")
WINDOW_DAYS = 14
MAX_RESULTS = 100  # per category
HEADERS = {
    "User-Agent": "Awesome-RAG-Frontier/1.0 (weekly digest tracker)",
    "Accept": "application/atom+xml",
}


def fetch_category(category: str) -> list[dict] | None:
    query = (
        f"search_query=cat:{category}"
        f"&sortBy=submittedDate&sortOrder=descending&max_results={MAX_RESULTS}"
    )
    request = urllib.request.Request(
        "https://export.arxiv.org/api/query?" + query, headers=HEADERS
    )
    # The export endpoint answers bursty traffic with 406; pace requests
    # gently and back off progressively when it still complains. Persistent
    # 406 on one category (observed behind some corporate proxies) means
    # network-level filtering — return None so the digest keeps partial
    # coverage instead of dying.
    backoffs = (20, 40, 60)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = response.read()
            print(f"fetched {category} (attempt {attempt + 1})", flush=True)
            break
        except urllib.error.HTTPError as error:
            if error.code not in (403, 406, 429) or attempt == 3:
                print(f"skipping {category}: {error}", file=sys.stderr, flush=True)
                return None
            print(f"{category} throttled ({error.code}), backing off {backoffs[attempt]}s", flush=True)
            time.sleep(backoffs[attempt])
    else:
        return None
    root = ET.fromstring(payload)
    entries = []
    for entry in root.findall(ATOM + "entry"):
        published = datetime.fromisoformat(
            (entry.findtext(ATOM + "published") or "").replace("Z", "+00:00")
        )
        entries.append(
            {
                "published": published,
                "title": " ".join((entry.findtext(ATOM + "title") or "").split()),
                "link": entry.findtext(ATOM + "id") or "",
                "summary": " ".join((entry.findtext(ATOM + "summary") or "").split())[:280],
            }
        )
    return entries


def main() -> int:
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=WINDOW_DAYS)
    by_link: dict[str, dict] = {}
    fetched_any = False
    for category in CATEGORIES:
        batch = fetch_category(category)
        if batch is None:
            continue
        fetched_any = True
        for entry in batch:
            if entry["published"] >= cutoff and entry["link"] not in by_link:
                by_link[entry["link"]] = entry
        time.sleep(10)  # arXiv API courtesy pause between categories
    if not fetched_any:
        print("no category could be fetched", file=sys.stderr)
        return 1

    def matches(entry: dict) -> bool:
        haystack = (entry["title"] + " " + entry["summary"]).lower()
        return any(keyword in haystack for keyword in KEYWORDS)

    entries = sorted(
        (entry for entry in by_link.values() if matches(entry)),
        key=lambda entry: entry["published"],
        reverse=True,
    )
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"arxiv-{now:%Y-%m-%d}.md"
    lines = [
        "<!-- draft: auto-generated arXiv candidates, not yet curated -->",
        f"# arXiv draft — {now:%Y-%m-%d}",
        "",
        f"{len(entries)} RAG-flavored papers from the last {WINDOW_DAYS} days "
        f"(newest {MAX_RESULTS} per category in {', '.join(CATEGORIES)}, keyword-filtered). "
        "Curate the keepers into README → Papers and the next news post; delete the rest.",
        "",
    ]
    for entry in entries:
        lines.append(
            f"- [ ] **{entry['title']}** — {entry['published']:%Y-%m-%d} — {entry['link']}"
        )
        lines.append(f"      > {entry['summary']}")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
