# /kb-audit

Scan the knowledge base for gaps, contradictions, stale claims, weak sourcing, and orphan FAQ answers; emit a prioritized coverage report.

## Inputs

- Path to the KB (default `outputs/kb/`).
- Optional focus: a taxonomy area or a confidence level to concentrate on.
- Optional FAQ directory (default `outputs/faq/`) to check for orphaned answers.

## Steps

1. Read `context/workflows.md` §H (KB audit) and the canonical taxonomy in `context/references.md`.
2. **Coverage:** tally entries per taxonomy tag; flag thin (<3 entries) or empty areas.
3. **Contradictions:** collect all `CONTRADICTION` markers and any entries that disagree on the same claim; list each pair for resolution.
4. **Staleness:** flag `measured` entries from old batch IDs that newer entries appear to supersede.
5. **Sourcing:** flag entries missing provenance, and `practitioner-lore` entries that your own batches now confirm (candidates to promote to `measured`).
6. **Orphans:** parse FAQ files; flag answers whose cited entries no longer exist or were edited.
7. Write a prioritized fix list to `outputs/audits/kb-audit-YYYY-MM-DD.md`.

## Output

- `outputs/audits/kb-audit-YYYY-MM-DD.md` — coverage table, contradiction pairs, staleness/sourcing flags, orphan list, ranked by impact.
- A one-line health summary in chat (e.g. "62 entries, 2 contradictions, 3 thin areas, 1 orphan FAQ answer").

## Notes

- Run before any `/faq-generate` you intend to publish.
- Resolve contradictions by evidence, not recency — a `published` source can outrank a newer `practitioner-lore` note.
- Audit reports are themselves dated artifacts; keep them so taxonomy drift is visible over time.
