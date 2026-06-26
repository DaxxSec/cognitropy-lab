# /concentration-report

Produce the final, defensible concentration for a sample — blank-corrected, recovery-corrected, with breakdowns and honest uncertainty. This is the deliverable; everything upstream exists to make this number trustworthy.

## Inputs

- Screening record (`/screen-sample`) with confirmed-plastic counts and the primary false-positive correction.
- Blank-correction vector + LOD (`/blank-audit`).
- Recovery-correction factors (`/qa-recovery-spike`).
- Sample size metric: volume filtered (L or m³), or dry mass of sediment/biota (kg dw).

## Steps

1. **Start from confirmed-plastic counts**, applying the primary-screen false-positive correction (don't report raw stained/visual counts as plastic).
2. **Blank-correct** per category by subtracting the blank vector; any category below LOD reports as "< LOD", not zero and not a point estimate.
3. **Recovery-correct** per size/polymer stratum (divide by recovery fraction). State the size reporting floor — below it, report qualitatively only.
4. **Normalize** to the sample metric: particles/L or particles/m³ for water, particles/kg dw for sediment/biota; add mass concentration (µg/L) if particle masses were estimated from size × polymer density.
5. **Propagate uncertainty.** Combine counting (Poisson) uncertainty, blank-subtraction uncertainty, and recovery uncertainty. Report a confidence interval, not just a point value — low counts have wide intervals and over-precise numbers mislead.
6. **Break down** the result: by polymer, size class, and morphology (fragment/fiber/film/bead/foam), plus the % confirmed vs inferred.
7. **Stamp provenance:** method version, mesh/pore size class, digestion + density medium, detector + HQI threshold, blank LOD, recovery factors, and the linked custody chain. A number without its method is not reportable.

## Output

A concentration report under `outputs/reports/<sample-id>.md`: final concentration with CI, polymer/size/morphology breakdowns, all corrections shown explicitly, the size reporting floor, and the full provenance stamp. This result feeds `/contamination-anomaly`.
