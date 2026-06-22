# /restoration-traveler — Per-Frame Job Traveler & Inspection Record

Generate a job traveler (router sheet) that follows one frame through the shop, capturing every measurement, checkpoint, sign-off, and disposition — serving as both the SQC traceability record and the conservation treatment record in one document.

## Inputs

- Frame ID, piece type/period, owner/job reference, intake date.
- The quality characteristics to track for this piece and their tolerances/datums.
- The planned process steps (strip → assess → condition → re-glue/reinforce → re-square → release) and the restorers involved.

## Steps

1. Open the traveler header: frame ID, piece description, conservation status, intake photos reference, and the responsible restorer(s).
2. Lay out the **measurement plan** — each characteristic with its datum, instrument, tolerance, and the gage R&R reference for that gauge.
3. Add a **checkpoint row per process step** with fields for value(s), operator, date, MC/RH, and pass/hold/sign-off.
4. Link each measured value to its **running control chart** (`/control-chart`) and each defect to the **Pareto log** (`/defect-pareto`) so the traveler feeds the shop-level statistics.
5. Reserve a **disposition & ethics block**: per-member keep/repair/replace with the conservation rationale, and the final release sign-off (all checkpoints passed or holds resolved).

## Output

A complete traveler markdown: header, measurement plan, per-step checkpoint table, chart/Pareto links, and disposition/release block. Save to `outputs/<frame-id>-traveler.md` and keep it the single source of truth for the job.

## Notes

- The traveler is simultaneously the **conservation documentation** required by AIC ethics and the **traceability** required by SQC — write it once, satisfy both.
- A measurement without its metadata (datum, instrument, operator, MC, RH) is not traceable; the traveler's job is to make leaving them out impossible.
- Don't release a frame with an open hold — an unresolved out-of-control checkpoint is a hold, not a footnote.
