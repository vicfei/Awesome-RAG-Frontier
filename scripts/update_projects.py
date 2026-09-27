#!/usr/bin/env python3
"""Refresh tracked-project stats and regenerate README project tables.

Reads data/projects.json, queries the GitHub API for star counts, last-push
dates, and archived flags, rewrites the auto-generated project tables in
README.md and README.zh-CN.md between the frontier markers, and stores
data/stats.json as a fallback for rate-limited runs.

Stdlib only. Set GITHUB_TOKEN or GH_TOKEN to raise rate limits (GitHub
Actions provides GITHUB_TOKEN automatically).
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_FILE = ROOT / "data" / "projects.json"
STATS_FILE = ROOT / "data" / "stats.json"
README_FILES = [ROOT / "README.md", ROOT / "README.zh-CN.md"]

STALE_AFTER_DAYS = 180

BLOCK_START = "<!-- frontier:projects:start -->"
BLOCK_END = "<!-- frontier:projects:end -->"
BADGE_RE = re.compile(r"!\[refreshed\]\([^)]*\)")
API_ROOT = "https://api.github.com/repos/"


def fetch_repo(full_name: str, token: str | None) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-rag-frontier-refresh",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(API_ROOT + full_name, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code in (403, 429):
            return {"_rate_limited": True}
        if error.code == 404:
            return {"_not_found": True}
        raise


def collect_stats(repos: list[str], token: str | None) -> dict:
    previous: dict = {}
    if STATS_FILE.exists():
        previous = json.loads(STATS_FILE.read_text(encoding="utf-8")).get("repos", {})
    stats: dict[str, dict] = {}
    for name in repos:
        meta = fetch_repo(name, token)
        if meta.get("_rate_limited"):
            print(f"rate limited, keeping cached data: {name}", file=sys.stderr)
            if name in previous:
                stats[name] = previous[name]
        elif meta.get("_not_found"):
            print(f"NOT FOUND: {name} — fix owner/name in data/projects.json", file=sys.stderr)
            if name in previous:
                stats[name] = previous[name]
        else:
            stats[name] = {
                "stars": meta.get("stargazers_count"),
                "pushed_at": (meta.get("pushed_at") or "")[:10],
                "archived": bool(meta.get("archived")),
            }
        time.sleep(0.3)
    return stats


def dormancy_flag(entry: dict) -> str:
    # criteria.md: entries dormant 6–12 months get a ⚠️ marker; the
    # >12-month removal itself stays a human decision.
    pushed = entry.get("pushed_at")
    if not pushed:
        return ""
    try:
        pushed_date = date.fromisoformat(pushed)
    except ValueError:
        return ""
    if date.today() - pushed_date > timedelta(days=STALE_AFTER_DAYS):
        return " ⚠️"
    return ""


def build_tables(config: dict, stats: dict, lang: str) -> str:
    today = date.today().isoformat()
    stale_note = f"⚠️ = archived or dormant >{STALE_AFTER_DAYS // 30} months"
    if lang == "en":
        headers = ("Project", "Why it matters", "Stars", "Last push")
        footer = (
            f"_Auto-refreshed weekly — last refresh {today}. {stale_note}. "
            "Raw stats: [data/stats.json](data/stats.json)._"
        )
    else:
        headers = ("项目", "一句话点评", "Stars", "最近推送")
        footer = (
            f"_每周自动刷新，最近一次：{today}。⚠️ = 已归档或沉寂超过 {STALE_AFTER_DAYS // 30} 个月。"
            "原始数据见 [data/stats.json](data/stats.json)。_"
        )
    desc_key = "en" if lang == "en" else "zh"
    parts: list[str] = []
    for category in config["categories"]:
        title = category["title_en"] if lang == "en" else category["title_zh"]
        items = [item for item in config["items"] if item["category"] == category["id"]]
        items.sort(
            key=lambda item: (
                (stats.get(item["repo"]) or {}).get("stars") is None,
                -((stats.get(item["repo"]) or {}).get("stars") or 0),
            )
        )
        rows = [f"| {headers[0]} | {headers[1]} | {headers[2]} | {headers[3]} |", "| --- | --- | :--: | :--: |"]
        for item in items:
            entry = stats.get(item["repo"]) or {}
            stars = entry.get("stars")
            stars_text = f"{stars:,}" if isinstance(stars, int) else "—"
            pushed = entry.get("pushed_at") or "—"
            flag = " ⚠️" if entry.get("archived") else dormancy_flag(entry)
            display = item["repo"].split("/", 1)[1]
            rows.append(
                f"| [{display}](https://github.com/{item['repo']}){flag} "
                f"| {item.get(desc_key) or item.get('en', '')} "
                f"| {stars_text} | {pushed} |"
            )
        parts.append(f"### {title}\n\n" + "\n".join(rows))
    parts.append(footer)
    return "\n\n".join(parts)


def splice(text: str, block: str) -> str:
    start = text.index(BLOCK_START) + len(BLOCK_START)
    end = text.index(BLOCK_END)
    return text[:start] + "\n\n" + block + "\n\n" + text[end:]


def main() -> int:
    config = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    repos = [item["repo"] for item in config["items"]]
    stats = collect_stats(repos, token)

    badge_code = date.today().isoformat().replace("-", "--")
    badge = f"![refreshed](https://img.shields.io/badge/refreshed-{badge_code}-2ea44f)"
    for path in README_FILES:
        text = path.read_text(encoding="utf-8")
        text = splice(text, build_tables(config, stats, "zh" if "zh-CN" in path.name else "en"))
        if BADGE_RE.search(text):
            text = BADGE_RE.sub(lambda _: badge, text, count=1)
        path.write_text(text, encoding="utf-8")
        print(f"updated {path.name}")

    STATS_FILE.write_text(
        json.dumps(
            {"generated_at": date.today().isoformat(), "repos": stats},
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    missing = sorted(set(repos) - set(stats))
    if missing:
        print(f"no data for: {', '.join(missing)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
