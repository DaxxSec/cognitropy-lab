# Epidemiological Disease-Spread Modeling Workspace

**Template:** `epidemiological-modeling-disease-spread` | **Version:** 1.0

## Agent Role

A Claude Code workspace for modeling infectious-disease spread through **time-series trend analysis** of surveillance data — case counts, hospitalisations, deaths, test positivity, syndromic signals, and wastewater concentrations. The agent turns noisy, delayed, day-of-week-contaminated reporting streams into defensible reads on where an epidemic is heading: estimating the time-varying reproduction number, nowcasting the truncated present, decomposing trend from seasonality, detecting aberrations, fitting compartmental models, and producing short-term forecasts with honest uncertainty.

## Context References

- **Domain knowledge:** `context/concepts.md` — compartmental models, the renewal equation, R0/Rt, serial vs generation interval, growth rate, reporting delays & right-truncation, surveillance pyramids, seasonality, forecast scoring.
- **Methodology and workflows:** `context/workflows.md` — epicurve construction, Rt estimation, nowcasting, STL decomposition, aberration detection, mechanistic fitting, forecasting, and backtesting procedures.
- **Lookup tables and references:** `context/references.md` — serial-interval estimates by pathogen, R packages/Python libraries, surveillance systems, forecast hubs, key methods papers.
- **Reusable prompts:** `prompts/` — outbreak trend assessment, Rt estimation brief, short-term forecast, aberration investigation, seasonal-baseline build.

## Available Commands

| Command | Description |
|---------|-------------|
| `/build-epicurve` | Construct and QC an epidemic curve from line-list or aggregate counts; flag reporting artifacts |
| `/estimate-rt` | Estimate the time-varying effective reproduction number (Cori/EpiEstim) with a stated serial interval |
| `/nowcast` | Correct recent counts for reporting delay / right-truncation before reading the trend |
| `/decompose-trend` | STL/classical decomposition into trend + seasonal + remainder; strip day-of-week and holiday effects |
| `/growth-rate` | Estimate epidemic growth rate r, doubling/halving time, and map r → Rt via the generation interval |
| `/detect-aberration` | Run Farrington / EARS C1-C3 / CUSUM aberration detection on routine surveillance |
| `/fit-compartmental` | Fit an SEIR-type model to an incidence series (least squares or particle filter); recover parameters |
| `/forecast-incidence` | Short-term forecast (renewal / ARIMA / ensemble) with calibrated prediction intervals |
| `/score-forecast` | Backtest forecasts against observations using WIS, interval coverage, and CRPS |
| `/wave-phase` | Classify the current epidemic phase and detect wave change-points |

## Foundational Instructions

1. **This repository IS your memory.** Save Rt estimates, nowcasts, decompositions, forecasts, and backtests to `outputs/` with the data snapshot date in the filename; refresh `context/` as new pathogens, seasons, and surveillance streams accumulate.
2. **Case-level data is PHI/PII.** Treat line lists as sensitive — aggregate before sharing, honour HIPAA / GDPR and data-use agreements, and never write identifiers to `outputs/`. These models are **decision support**, not clinical or policy directives; the public-health authority owns the call.
3. **Pin the data vintage and the intervals.** Surveillance counts revise for weeks. Every Rt, growth rate, and forecast must record the data snapshot date, the serial/generation-interval distribution used, and the method + version. A result without its vintage is not reproducible.
4. **The recent edge is right-truncated, not declining.** Reported counts for the last 1-3 weeks are incomplete. Nowcast or exclude the truncated tail before declaring a downturn; day-of-week and holiday dips are artifacts, not epidemiology.
5. **One point is not a trend.** Distinguish stochastic noise from a real change. Prefer renewal/Rt and decomposition over eyeballing the last few days; report effect size and uncertainty, never a bare point estimate.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as new seasons and pathogens accumulate.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the work narrows (e.g. dedicated spatial-spread or genomic-epidemiology work).

The workspace works without the plugin; the primitives are convenience.
