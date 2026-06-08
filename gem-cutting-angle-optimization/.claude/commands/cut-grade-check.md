# /cut-grade-check — Grade Proportions & Flag Optical Defects

Score a finished (or planned) stone's proportions against GIA-style round-brilliant tolerances and flag the optical failure modes its geometry invites.

## Inputs

- Measured proportions: table %, crown angle, pavilion angle, total depth %, girdle thickness, culet.
- Material RI (to interpret pavilion angle against the critical floor).
- (Optional) the intended proportions, if checking a cut against its target.

## Steps

1. Compare each parameter to the Excellent bands in `context/references.md`; mark each green / borderline / out.
2. Run the defect screen:
   - **Window** — pavilion below ~critical-floor margin or too shallow for the RI.
   - **Fish-eye** — shallow pavilion + table > ~60%.
   - **Nailhead / extinction** — pavilion too steep (> ~42° for mid-RI).
3. If checking achieved vs intended, compute the **delta** per parameter; a pavilion delta larger than the tolerance budget points at the machine, not the design (hand off to `/spindle-runout-trend`).
4. Assign an overall grade (Excellent / Very Good / Good / Fair) from the worst-scoring parameters.
5. Recommend the corrective angle change for any out-of-band parameter, or the maintenance check if the deltas implicate the machine.

## Output

A grade report: per-parameter score table, defect flags, overall grade, and corrective recommendation. Save to `outputs/<stone-id>-grade.md`.

## Notes

- Grade bands here are round-brilliant defaults; step cuts and fantasy designs need design-specific targets.
- A perfectly graded plan that windows in reality is a machine problem — always reconcile intended vs achieved before blaming the design.
