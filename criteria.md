# Inclusion criteria

Rules, not vibes. If an entry stops qualifying, it gets flagged or dropped by the same process that added it.

## Projects (auto-tracked)

1. **RAG-central.** Retrieval / knowledge grounding must be a core capability of the project, not an incidental feature of a broader platform. Borderline cases say so in their one-liner. For courses/tutorials: RAG must be a mainline module or the capstone — general LLM courses where RAG is one lesson among many don't qualify, however many stars they have (yes, that means 100k★ course repos get excluded on purpose).
2. **Alive.** A commit or release within the last 6 months. Entries dormant 6–12 months get a ⚠️ marker in the table; past 12 months they leave the main tables.
3. **Traction.** One of:
   - ≥ 300 stars, or
   - an institutional home we trust (research lab, company OSS program), or
   - clear influence (forked/cited/embedded by entries already tracked).
4. **Runnable.** A public repo with install and run instructions. Announcement-only repos are not entries.

## Radar (pre-threshold watchlist)

Promising entries that don't clear the bar yet, tracked in `data/radar.json` and rendered under a separate section. Rules:

1. Still **runnable and RAG-central** — the radar is for early-stage, not vaporware.
2. Must ride a **visible wave** or show unusual quality for its size; a PR should say which.
3. **Graduation is automatic in spirit**: once an entry meets the full project criteria, it moves up; the weekly refresh keeps its stats honest either way.
4. Archived entries stay only as historical markers of a wave (the ⚠️ flag shows them for what they are).

## Papers (curated)

1. Peer-reviewed at a venue we track, **or** companion code with real adoption, **or** demonstrable industry influence.
2. The *Frontier* subsection favors the last ~18 months. Older papers belong in *Paradigms* only if they named a pattern people still use.
3. Weekly arXiv digest drafts (`news/_drafts/`) feed this section; a human decides what graduates.

## Enterprise practices (curated)

1. **First-party or verifiable.** Vendor engineering blogs, conference talks with stable URLs, postmortems. No slide decks on rotting cloud-drive links, no content marketing.
2. **Dated.** Year required when the source states one; `—` otherwise (never guess).
3. **Technical depth over marketing.** The entry must teach something an operator can act on.

## Categories

`kb-products` / `frameworks` / `graphrag` / `parsing` / `evaluation` / `research` / `collections` — defined in `data/projects.json`. A new category requires a PR that explains the gap the current seven fail to cover.

## Neutrality & disclosure

Maintainers may list projects they work on **if the entry meets the same bar as everything else** and the affiliation is disclosed here. Disclosure is a trust feature, not a disqualifier.

Current disclosures:

- Founding maintainer: historical top-20 contributor to **Tencent/WeKnora** (listed under `kb-products`).

## Removal

Open an issue. Stale and unmaintained gets removed; historically important gets a legacy note instead of a silent delete.
