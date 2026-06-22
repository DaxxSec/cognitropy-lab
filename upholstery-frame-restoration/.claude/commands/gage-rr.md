# /gage-rr — Measurement System Analysis (Gage R&R)

Quantify how much of the observed variation in a frame characteristic comes from the **measurement method** (gauge + operators) versus the frames themselves — run before any frame data is trusted.

## Inputs

- The characteristic and its measurement method/jig (e.g. diagonal tape for squareness, caliper for joint gap, pin moisture meter).
- Study data: **~10 representative frames × 3 operators × 2–3 trials**, measured blind and in random order (or a request to design the study if data isn't collected yet).
- The tolerance band (to express R&R as % of tolerance as well as % of study variation).

## Steps

1. If no data: design the crossed study (10 parts spanning the range, 3 operators, 3 trials, randomized & blinded) and stop for collection.
2. Compute **Repeatability (EV)** from within-operator trial ranges (equipment variation).
3. Compute **Reproducibility (AV)** from the spread of operator averages (appraiser variation), corrected for repeatability.
4. Compute **GRR = √(EV² + AV²)**, **Part Variation (PV)**, **Total Variation (TV)**.
5. Report **%GRR = GRR/TV**, **%GRR vs tolerance**, and **ndc = 1.41·(PV/GRR)**.
6. Verdict per `context/references.md`: <10% accept, 10–30% conditional, >30% reject. Diagnose whether EV (gauge) or AV (operator/datum) dominates and recommend the fix.

## Output

An MSA report: EV, AV, GRR, PV, TV, %GRR (study and tolerance), ndc, the dominant component, and the verdict with corrective recommendation. Save to `outputs/<characteristic>-gagerr.md`.

## Notes

- Resolution rule: the instrument must discriminate to ≤ 1/10 of the tolerance, or %GRR is doomed regardless of technique.
- AV-dominated → the datum/method is ambiguous; standardize and re-train (cheap fix). EV-dominated → the gauge/fixture is noisy (harder fix).
- In hand-measured craft work the measurement system is *often* the largest variance source — this command frequently explains a "frame problem" that was really a measurement problem.
