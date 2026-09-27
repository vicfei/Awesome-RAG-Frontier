# Inclusion criteria

Rules, not vibes. If an entry stops qualifying, it gets flagged or dropped by the same process that added it.

## Projects (auto-tracked)

1. **RAG-central.** Retrieval / knowledge grounding must be a core capability of the project, not an incidental feature of a broader platform. Borderline cases say so in their one-liner.
2. **Alive.** A commit or release within the last 6 months. Entries dormant 6–12 months get a ⚠️ marker in the table; past 12 months they leave the main tables.
3. **Traction.** One of:
   - ≥ 300 stars, or
   - an institutional home we trust (research lab, company OSS program), or
   - clear influence (forked/cited/embedded by entries already tracked).
4. **Runnable.** A public repo with install and run instructions. Announcement-only repos are not entries.

## Papers (curated)

1. Peer-reviewed at a venue we track, **or** companion code with real adoption, **or** demonstrable industry influence.
2. The *Frontier* subsection favors the last ~18 months. Older papers belong in *Paradigms* only if they named a pattern people still use.
3. Weekly arXiv digest drafts (`news/_drafts/`) feed this section; a human decides what graduates.

## Categories

`kb-products` / `frameworks` / `graphrag` / `parsing` / `evaluation` / `research` / `collections` — defined in `data/projects.json`. A new category requires a PR that explains the gap the current seven fail to cover.

## Neutrality & disclosure

Maintainers may list projects they work on **if the entry meets the same bar as everything else** and the affiliation is disclosed here. Disclosure is a trust feature, not a disqualifier.

Current disclosures:

- Founding maintainer: historical top-20 contributor to **Tencent/WeKnora** (listed under `kb-products`).

## Removal

Open an issue. Stale and unmaintained gets removed; historically important gets a legacy note instead of a silent delete.
