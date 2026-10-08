# Contributing

Thanks for helping track the frontier. Three ways in:

## Add a project

1. Edit [`data/projects.json`](data/projects.json): pick the right category, add `repo`, `en`, `zh`. The one-liners are judgments ("why it matters"), not descriptions — the project's own README covers "what it is".
2. Optionally run `python3 scripts/update_projects.py` to regenerate tables locally; if you skip it, the weekly Action does it for you.
3. Check your entry against [criteria.md](criteria.md) in the PR description.

## Add a paper

Edit the **Papers** section of `README.md` **and** `README.zh-CN.md` in the same PR. Keep the one-liner to a single judgment. The weekly arXiv and GitHub-sweep drafts in `news/_drafts/` are good hunting ground.

## Report news

Open an issue with links and dates. "This Month in RAG" entries must be verifiable from release notes or papers — no vibes.

## House rules

- If you maintain (or are paid by) something you're adding, say so in the PR. Disclosed affiliations are welcome; hidden ones are not.
- Don't reformat other sections while you're here; diffs stay reviewable.
- PRs that swap descriptions for marketing copy get pushed back on.
