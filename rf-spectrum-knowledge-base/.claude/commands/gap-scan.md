# /gap-scan — Find Coverage Gaps, Stale Entries, and Unknowns

Scan the knowledge base for what's missing or rotting — unmonitored bands, unidentified emitters, stale entries, and unanswered questions — and emit a prioritized backlog.

## Inputs

- The KB at `outputs/kb/`, the OPEN questions from `outputs/faq.md` / `outputs/query-log.md`
- A coverage target: the frequency ranges and regions this KB is *supposed* to cover (from `context/references.md` or user-supplied)
- Current date (to compute staleness against each entry's `review_by`)

## Steps

1. **Compute band coverage.** Tile the target range into segments. Mark each segment `covered` (has ≥1 active entry), `thin` (one stale/low-confidence entry), or `dark` (no entries) — dark segments inside the target are gaps.
2. **Collect unidentified emitters.** List all entries with `identification = unidentified` or `confidence = probable`; these are knowledge debts waiting on a positive ID.
3. **Detect staleness.** Flag entries past `review_by`, or whose `last_seen` predates the most recent sweep that should have re-detected them (possible silent disappearance).
4. **Pull OPEN questions.** Gather every question `/kb-query` and `/faq-generate` couldn't answer.
5. **Prioritize.** Score each gap by `impact × tractability`: impact = how often the band/question comes up + safety/legal relevance; tractability = how easily a single capture or lookup would close it. Sort descending into a backlog.

## Output

`outputs/gap-backlog-<date>.md`: a ranked table of gaps (type, location/band, why it matters, suggested action — recapture / identify / refresh / research), plus a coverage heat-summary (covered / thin / dark segment counts).

## Notes

- A KB that only grows looks healthy but silently rots — staleness gaps matter as much as missing bands.
- Pair the backlog with `/kb-ingest-sweep`: the top "dark band" gaps directly become the next sweep's priority frequencies.
- Distinguish "emitter gone" (legitimately disappeared → mark `historical`) from "we stopped looking" (coverage gap) — they need opposite actions.
