# /structured-report

Emit the canonical QA readout for a batch in a fixed, reproducible structure — the spherification analog of a radiology report.

## Inputs

- The adequacy verdict (`/study-quality`), findings table (`/read-batch`), differentials (`/differential`), and category (`/sphere-rads`).
- The pinned recipe header.

## Steps

1. **Technique** — record method, full recipe (alginate %, calcium salt + %, bath time, pH, temperature), rest interval, and sample size. Reproducibility lives here.
2. **Findings** — the per-station observations and their frequencies, neutrally described.
3. **Impression** — the synthesized read: the dominant defect and its most-likely cause.
4. **Category** — Sphere-RADS-n.
5. **Corrective action** — the specific change + which command runs it.
6. **Re-test interval** — when/whether to re-read (basic: minutes; reverse: stable).

## Output

`outputs/report-<liquid>-YYYY-MM-DD.md` in the six-section structure. One report per batch; reports are the audit trail and the FMEA's Occurrence data source.

## Notes

- Keep Findings and Impression separate — findings are observations anyone can verify; the impression is your synthesis.
- A report without its full Technique block is unreproducible; a "burst score" needs its bath time and rest interval to mean anything.
