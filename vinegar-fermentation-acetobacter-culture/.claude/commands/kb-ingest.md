# /kb-ingest

Parse a source — book chapter, paper, batch log, or forum thread — into canonical vinegar knowledge-base entries with provenance, taxonomy tags, and a confidence rating.

## Inputs

- Path or pasted text of the source (PDF, Markdown, notebook export, URL content).
- Source type (used to set default confidence): `own-batch` → `measured`, `authoritative` → `published`, `community/anecdote` → `practitioner-lore`, `agent-reasoning` → `inferred`.
- Optional taxonomy hint (one of the canonical top-level tags) if the source is narrow.

## Steps

1. Read `context/concepts.md` §9 (KB model) and `context/references.md` (taxonomy + confidence tags).
2. Read the source. Extract **atomic claims** — one fact or topic per candidate entry; do not bundle multiple ideas into one entry.
3. For each claim, build a KB entry: `title`, `body`, `taxonomy` (≥1 canonical tag), `provenance` (source + locator: page, DOI, batch ID, URL, or "personal observation"), `confidence` (per source type above), `related` (links to sibling entries).
4. Deduplicate against existing entries under `outputs/kb/`. If a new claim **contradicts** an existing one, keep both and add a `CONTRADICTION` marker for `/kb-audit` to resolve.
5. Write entries to `outputs/kb/<top-level-tag>/<slug>.md` and update `outputs/kb/_index.md` (title → path → confidence).
6. Report a summary: entries created, merged, flagged; taxonomy areas touched.

## Output

- New/updated entry files under `outputs/kb/<tag>/`.
- Updated `outputs/kb/_index.md`.
- An ingestion summary printed to chat (counts + any contradictions flagged).

## Notes

- Never upgrade confidence to `measured` unless the claim was verified in *this* program's own batches.
- Keep entries short and single-purpose — granularity is what makes `/faq-generate` and `/kb-audit` work.
- Preserve the original wording of safety/regulatory claims; paraphrasing can quietly change meaning.
