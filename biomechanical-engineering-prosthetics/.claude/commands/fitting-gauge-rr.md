# /fitting-gauge-rr

Run a Gauge R&R (Repeatability & Reproducibility) study on a measurement system used in the practice — caliper, 3D socket scanner, pressure mat, force plate, motion capture. Reports % R&R and % contribution per the AIGM MSA Manual.

## Inputs

- **Measurement system** — what device, model, configuration, software version.
- **Sample parts** — typically 5-10 parts (sockets, foot units, scan-test fixtures) spanning the practice's normal range of measurement values. The parts should be representative of the population, not all clustered at one value.
- **Operators** — 2-3 typical operators (fitters, technicians). All operators must be normally trained on this system.
- **Trials per operator per part** — typically 3 (sometimes 2 for time-constrained studies; never 1).
- **Measurement variable** — what's being measured (e.g. socket trimline length in mm; PTB-region peak pressure in kPa; tibial alignment in deg).
- **Tolerance specification** (optional) — design spec for % tolerance calculation; without it, R&R is reported only against process variation.

## Steps

1. Read `context/references.md` "AIAG MSA acceptance thresholds" — the standard <10% / 10-30% / >30% R&R bands.
2. Design the run: random order of (operator, part, trial) combinations to break out operator and run-order effects. Don't let operators measure the same part in adjacent trials (memory bias).
3. Collect data; tabulate as `operator, part, trial, value`.
4. Run the ANOVA-method Gauge R&R (preferred over the older "average and range" method). Calculate:
   - Repeatability (equipment variation, EV) — within-operator within-part variance
   - Reproducibility (appraiser variation, AV) — between-operator within-part variance
   - Part-to-part variation (PV)
   - Total Gauge R&R = √(EV² + AV²)
   - % Study Variation = 100 × R&R / Total Variation
   - % Contribution = 100 × R&R² / Total Variation²
   - % Tolerance (if tolerance provided) = 100 × R&R × 6 / Tolerance Range
   - Number of distinct categories (NDC) = 1.41 × PV/R&R, rounded down
5. Apply acceptance criteria (AIAG):
   - % R&R < 10% → System acceptable
   - % R&R 10-30% → Acceptable depending on cost/criticality
   - % R&R > 30% → Unacceptable; system needs improvement
   - NDC ≥ 5 → System discriminates enough; <5 = inadequate
6. Decompose causes if R&R is high: large EV → equipment / fixturing issue; large AV → operator training inconsistency.
7. Write study report at `outputs/gauge-rr/<system-id>/<YYYY-MM-DD>-rr-study.md` with full breakdown, plots (operator-by-part interaction plot, range chart by operator), and pass/fail with recommended actions.

## Output

A markdown Gauge R&R report containing: study design, sample data table, ANOVA results, EV / AV / PV / R&R / % Study / % Contribution / NDC / % Tolerance, acceptance verdict per AIAG, root-cause decomposition if marginal/failing, recommended actions (operator retraining, fixturing improvement, system replacement). Plots saved as PNG alongside.

## Decision points

- **If only one operator is available** → you can only measure Repeatability, not Reproducibility. Report it as a Gauge Repeatability study (not R&R) and flag the limitation.
- **If parts cluster at a single value** → PV is artificially small, % R&R is inflated. Re-select parts spanning the population range and re-run.
- **If operators disagree systematically (one always reads high)** → that's a bias, not just reproducibility — investigate training delta, calibration drift on per-operator setup, or measurement procedure ambiguity.
- **If NDC < 5 but % R&R is acceptable** → the system can detect differences but not finely enough; not a process-capability blocker but a flag for fine-tolerance work.

## Notes

- Pressure mapping mats notoriously have R&R challenges from hysteresis and operator-induced loading variation. Expect 15-30% R&R; >30% means the mat itself is the problem.
- 3D socket scanners with structured-light hardware typically achieve <5% R&R on geometric measurements; if yours is worse, suspect ambient-lighting interference or scanner calibration drift.
- Repeat Gauge R&R quarterly for high-criticality systems, annually for routine. Run after any hardware service or software update.
- Cross-reference with `/socket-fit-control-chart` and `/manufacturing-cpk-audit` — those analyses' validity depends on the underlying R&R being acceptable.
