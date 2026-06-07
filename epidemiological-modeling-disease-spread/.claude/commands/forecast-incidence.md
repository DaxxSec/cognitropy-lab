# /forecast-incidence

Produce a short-term (1-4 week) probabilistic forecast of a surveillance series, combining renewal, statistical, and (optionally) mechanistic methods into a calibrated ensemble.

## Inputs

- The cleaned, nowcast-corrected series and the forecast **horizon** (weeks/days ahead).
- Rt / generation interval (for the renewal forecast) and the count model.
- Output **quantile set** (default the forecast-hub 23 quantiles) and whether to ensemble.

## Steps

1. Read `context/workflows.md` "Workflow 8: Short-term forecasting + backtesting".
2. Generate ≥2 component forecasts:
   - **Renewal / Rt-projection** — `EpiNow2` or `projections` (branching process) carrying current Rt forward with its uncertainty.
   - **Statistical** — ARIMA / ETS (`forecast`/`fable`) or Prophet on the de-seasonalised series.
   - **Mechanistic** (optional) — simulate forward from the `/fit-compartmental` posterior.
3. Emit **probabilistic** forecasts (full quantile set), never point estimates.
4. Build an **ensemble** (median or skill-weighted) across components.
5. Sanity-check intervals against historical volatility; widen if obviously over-confident.
6. Hand off to `/score-forecast` once observations arrive to confirm calibration.
7. Write forecasts + figure to `outputs/`.

## Output

`outputs/forecast-<stream>-<snapshot-date>.md` + figure: per-method and ensemble quantile forecasts with fan chart, the assumptions (Rt held vs evolving, generation interval), the horizon, and a plain-language summary ("most likely range next 2 weeks: X–Y").

## Notes

- Ensembles almost always beat any single model out-of-sample — the central finding of the COVID/Flu forecast hubs.
- Renewal forecasts assume Rt persists; state that assumption — a turning point will be missed if Rt is changing.
- A forecast without intervals is not a forecast; propagate every uncertainty source you can.
- Distinguish a **forecast** (best estimate of the future) from a **scenario projection** (conditional "what if" — longer horizon, not scored against reality the same way).
