# /score-forecast

Backtest probabilistic forecasts against realised observations using proper scoring rules, so the next forecast is honest about its own skill.

## Inputs

- One or more **quantile/probabilistic forecasts** (with forecast origin + horizon) from `/forecast-incidence`.
- The **realised** observed series (truth data; final/revised values where possible).
- Scoring scope: which scores (WIS / CRPS / coverage / pinball), and whether to compare methods.

## Steps

1. Read `context/workflows.md` "Workflow 8" scoring sub-steps.
2. Align each forecast to its realised target at the matching origin + horizon (mind data revisions — score against final, note the vintage).
3. Compute **WIS** (Weighted Interval Score) per forecast — the forecast-hub standard; decompose into dispersion / over-prediction / under-prediction.
4. Compute **interval coverage**: do the 50% and 95% intervals cover 50% and 95% of outcomes? (calibration).
5. Compute **CRPS** (full predictive distribution) and per-quantile **pinball loss** as needed.
6. Compare methods / the ensemble on mean WIS across origins and horizons; rank them.
7. Diagnose miscalibration (e.g. 95% coverage ≪ 95% → intervals too narrow → under-modelled overdispersion).
8. Write the scorecard + figures to `outputs/`.

## Output

`outputs/forecast-score-<stream>-<snapshot-date>.md` + figures: a scorecard (method × horizon → WIS, coverage, CRPS), the WIS decomposition, calibration plot, a ranked recommendation of which method/weights to trust, and concrete fixes for any miscalibration.

## Notes

- Use **scoringutils** (R, or its Python port) — don't hand-roll WIS; the decomposition and orientation are easy to get wrong.
- Lower WIS is better; WIS reduces to absolute error for a point forecast, so it fairly compares point and probabilistic submissions.
- Score against **final** observations and record the truth vintage; scoring against still-revising data flatters recent forecasts.
- Good calibration ≠ low error — report both coverage and WIS.
