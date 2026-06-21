# /threshold-band

Find the rule's usable operating window — the LUF/MUF analog — and set the FOT operating point. Phase 3, the quantitative core of the build.

## Inputs

- Candidate rule (from `/draft-detection`).
- Noise floor + required-SNR margin (from `/noise-floor`).
- An evaluation set: benign history plus any known-bad markers (atomic tests, prior incidents).
- FP budget (alerts/day the team can absorb) and recall floor (minimum acceptable detection rate).

## Steps

1. Sweep the threshold across its range (e.g. failed-logon count 3 → 50, or anomaly score 1 → 10).
2. At each step, compute FP load (from benign history) and recall (from known-bad).
3. **LUF** = the loosest threshold at which FP load is still within budget — below it, the rule storms.
4. **MUF** = the strictest threshold at which recall still meets the floor — above it, real attacks skip over (false negatives).
5. If `LUF ≥ MUF`, the window is closed: the rule cannot satisfy both budgets on this telemetry. Stop and escalate to `/coverage-map` (need better signal).
6. Set **FOT ≈ 0.85 × MUF** (back ~15% off the strict edge toward sensitivity) so normal diurnal variation doesn't push the operating point above the MUF.
7. Record the margin from FOT to both edges — that margin is the rule's resilience to drift.

## Output

`outputs/threshold-band-<rule>-YYYY-MM-DD.md` — the sweep table (threshold vs FP-load vs recall), the identified LUF and MUF, the chosen FOT, and the drift margins.

## Notes

- A wide LUF↔MUF window = a robust circuit. A narrow one = a fragile rule that will need frequent `/tune-rule` cycles.
- Closed window (`LUF ≥ MUF`) is not a tuning problem — it's a telemetry problem. Don't paper over it with a threshold compromise that satisfies neither budget.
