# /faq-generate — Generate or Refresh the Spectrum FAQ

Mine recurring analyst questions and the contents of the knowledge base to produce a grounded, citable FAQ document — the defining technique of this workspace.

## Inputs

- A question log: prior `/kb-query` calls, analyst tickets, chat history, or a hand-written list of recurring questions
- The KB at `outputs/kb/` and glossary at `outputs/glossary.md`
- Optional: the existing `outputs/faq.md` to refresh rather than rebuild

## Steps

1. **Cluster questions.** Group the question log by topic and intent (identification, legality, "what's on this band", measurement how-to, troubleshooting). Count frequency of each cluster — high-frequency clusters become FAQ entries first.
2. **Draft answers from the KB only.** For each cluster, compose a concise answer grounded in specific KB entries. Cite entry IDs. If the KB doesn't support an answer, mark the question `OPEN` and route it to `/gap-scan` instead of inventing content.
3. **Add canonical reference answers.** For evergreen questions (band edges, ISM rules, legality caveats), cite `context/references.md` and authoritative external sources, not just observed entries.
4. **Structure and de-duplicate.** Organize into sections (Getting started · Identifying signals · Bands & allocations · Legal & ethical · Measurement & tools · Troubleshooting). Merge near-duplicate questions; prefer the user's own phrasing for findability.
5. **Stamp and diff.** Write `outputs/faq.md` with a `last_generated` date and, if refreshing, a short "what changed" note (questions added / answers updated / questions newly OPEN).

## Output

`outputs/faq.md` — a sectioned FAQ where every factual claim cites a KB entry or a reference, plus an `OPEN QUESTIONS` appendix listing questions the KB cannot yet answer (input to `/gap-scan`).

## Notes

- The FAQ is a *view* of the KB, never a second source of truth. If an answer and its cited entry disagree, the entry wins and the FAQ is regenerated.
- Re-run after any significant ingest so the FAQ doesn't drift stale; record cadence in the file header.
- Keep answers short; link to the full entry for depth. A FAQ that restates whole entries stops being a FAQ.
