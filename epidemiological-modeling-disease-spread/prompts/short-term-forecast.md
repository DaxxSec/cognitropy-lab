# Short-Term Forecast Request

## Purpose

Use when you need a calibrated 1-4 week-ahead probabilistic forecast of a surveillance series for planning (e.g. hospital capacity), with an ensemble and a plan to score it.

## Prompt Template

```
Produce a short-term probabilistic forecast for this surveillance series, hub-style.

- **Target stream:** [cases / hospitalisations / deaths / ED]
- **Series & path:** [file path; cleaned + nowcast-corrected?]
- **Horizon:** [e.g. 1-2 weeks / 1-4 weeks ahead]
- **Quantiles:** [forecast-hub 23 quantiles, or specify]
- **Rt / generation interval:** [for the renewal component]
- **Backtest history available:** [how many past origins for scoring]
- **Decision context:** [what the forecast feeds — capacity, staffing, alerting]

Please:
1. Generate at least two component forecasts (renewal/Rt-projection + statistical ARIMA/ETS; add mechanistic if a fit exists).
2. Emit full quantile forecasts, not point estimates.
3. Build a median or skill-weighted ensemble.
4. Sanity-check intervals against historical volatility.
5. Backtest on held-out origins and report WIS, 50%/95% coverage, and CRPS.
6. State the key assumption (Rt held vs evolving) and what would break the forecast.
```

## Expected Output

- A fan chart of per-method and ensemble quantile forecasts over the horizon.
- A backtest scorecard (WIS, coverage, CRPS) and the recommended method/weights.
- The stated assumptions and a plain-language "most likely range" summary for the decision-maker.
- A flag distinguishing this forecast from a longer-horizon scenario projection.
