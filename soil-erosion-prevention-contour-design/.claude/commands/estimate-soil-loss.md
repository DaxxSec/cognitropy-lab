# /estimate-soil-loss

Estimate average annual sheet-and-rill soil loss with RUSLE and compare it against the soil-loss tolerance T — the field's erosion capacity budget.

## Inputs

- Slope steepness (%) and slope length (ft or m) for the LS factor.
- Soil mapping unit or texture → erodibility **K** and tolerance **T** (from soil survey, else estimate from `context/references.md`).
- Local rainfall erosivity **R** (R-factor map / RUSLE2 / regional value).
- Cover scenario(s) → **C** (current and any proposed practice).
- Support practice → **P** (up-and-down, contour, strip crop, terrace).
- Units preference (US t/ac/yr or SI t/ha/yr) — state it.

## Steps

1. Read `context/concepts.md` "RUSLE" and "Soil-loss tolerance T".
2. Resolve each factor; log the source of every value (survey vs estimate vs assumption). Confirm LS slope length is the *flow* length, not field width.
3. Compute `A = R·K·LS·C·P` for the current practice.
4. Compute utilization = A/T. Classify: A ≤ T adequate; A > T over-utilized.
5. If proposed practices were given, recompute A and A/T for each and tabulate the deltas (which factor moved, by how much).
6. State RUSLE's validity caveat (average-annual, sheet+rill only, not gully/ephemeral) and whether field evidence of concentrated flow warrants a separate structure.

## Output

`outputs/soil-loss/rusle-<field>-YYYY-MM-DD.md` — the factor table with sources, A and A/T for each scenario, the practice-comparison deltas, units stated explicitly, and a one-line adequacy verdict per scenario.

## Notes

- Do **not** confuse RUSLE's cover-management C with the rational runoff coefficient C — they are different numbers used by different commands.
- If A ≤ T on do-nothing, the cheapest valid recommendation is monitoring + maintenance — don't over-prescribe earthwork.
- Prefer RUSLE2 over hand lookup where available; it handles time-varying cover and deposition the table form cannot.
