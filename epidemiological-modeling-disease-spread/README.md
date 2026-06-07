# Epidemiological Disease-Spread Modeling Workspace

> Turn noisy disease-surveillance time series into defensible reads on epidemic direction — reproduction number, nowcasts, trend decomposition, aberration alarms, and calibrated short-term forecasts.

## What This Workspace Does

Infectious-disease surveillance arrives as a time series: daily or weekly counts of cases, hospital admissions, deaths, ED visits, test positivity, or wastewater viral load. The signal is real but the series is contaminated — reporting lags, weekend dips, holiday cliffs, retrospective data revisions, and right-truncation at the present edge all masquerade as epidemiology. This workspace is built to separate the **trend** (is transmission growing, plateauing, or declining?) from the **artifacts**.

The organising lens is **time-series trend analysis**: every command treats the surveillance stream as a series to be decomposed, smoothed, nowcast, and projected. The renewal equation links the observed incidence series to a time-varying reproduction number `Rt`; STL decomposition separates secular trend from seasonal and day-of-week structure; aberration-detection algorithms compare the present against a modelled baseline; mechanistic SEIR fits and renewal-based forecasts project the trend forward with quantified uncertainty; and backtesting scores those projections so the next forecast is honest about its own skill.

This is **decision support for surveillance and modelling teams**, not a clinical or policy engine. It produces estimates, intervals, and caveats — a public-health authority owns the action.

## Why This Workspace Exists

The hardest part of epidemic analysis is not the model — it is reading a trend off data that is delayed, revised, and incomplete at exactly the moment decisions are made. The most recent fortnight of any surveillance series is the most decision-relevant and the least trustworthy: it is right-truncated, so a real plateau looks like a decline. Teams that eyeball the last few raw points routinely call a peak that has not happened or miss one that has. This workspace codifies the practitioner discipline — nowcast before you read the edge, pin the serial interval and the data vintage, prefer Rt and decomposition over the naked epicurve, and score your forecasts so you know whether to trust them.

## Getting Started

### Prerequisites

- **R (≥4.1)** with `EpiEstim`, `EpiNow2`, `surveillance`, `incidence2`, `fable`/`forecast`, and `scoringutils`; **or Python (≥3.10)** with `epyestim`, `statsmodels`, `numpyro`/`scipy`, and `scoringutils` (Python port) — pick one stack.
- A surveillance time series: a **line list** (one row per case with onset/report dates) or **aggregate counts** (date + count, ideally by stratum).
- An estimate of the **serial interval** or **generation interval** for the pathogen (mean + SD, or a discretised distribution) — see `context/references.md` for starting values.
- The **data snapshot date** and, where available, a **reporting-delay distribution** (time from onset → report) for nowcasting.

### Quick Start

1. Clone this workspace and drop your series into `outputs/` (or point commands at its path).
2. Run `/build-epicurve` to construct and QC the epidemic curve, surfacing weekend effects, zero-runs, and the right-truncated tail.
3. Run `/nowcast` to correct the recent edge for reporting delay before reading any trend off it.
4. Run `/estimate-rt` with your serial interval to get the time-varying reproduction number with credible intervals.
5. Run `/forecast-incidence` for a short-term projection, then `/score-forecast` once observations land to check calibration.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/build-epicurve` | Construct and QC an epidemic curve from line-list or aggregate data | First contact with any new series; before any modelling |
| `/estimate-rt` | Time-varying effective reproduction number via Cori/EpiEstim | "Is transmission growing?" — the core trend question |
| `/nowcast` | Correct recent counts for reporting delay / right-truncation | Before reading the trend at the present edge |
| `/decompose-trend` | STL/classical decomposition; strip day-of-week + holiday effects | Series with strong weekly/seasonal structure |
| `/growth-rate` | Growth rate r, doubling/halving time, r → Rt conversion | Early exponential phase; quick communication of speed |
| `/detect-aberration` | Farrington / EARS C1-C3 / CUSUM outbreak detection | Routine surveillance — "is today anomalous vs baseline?" |
| `/fit-compartmental` | Fit SEIR-type model to incidence; recover parameters | Mechanistic understanding, scenario projection, R0 |
| `/forecast-incidence` | Short-term forecast with calibrated prediction intervals | 1-4 week ahead projections for planning |
| `/score-forecast` | Backtest forecasts (WIS, coverage, CRPS) | After observations arrive; choosing among methods |
| `/wave-phase` | Classify epidemic phase; detect wave change-points | Situational awareness; communicating where we are |

## Directory Structure

```
epidemiological-modeling-disease-spread/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke epidemiology + time-series commands
├── context/
│   ├── concepts.md           # Compartmental models, renewal eq., Rt, delays, scoring
│   ├── workflows.md          # Estimation, nowcasting, forecasting, backtesting procedures
│   └── references.md         # Serial intervals, tooling, surveillance systems, papers
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Rt estimates, nowcasts, forecasts, backtests
```

## Example Use Cases

### "Has the wave peaked, or is the dip just the weekend?"
Run `/build-epicurve` then `/nowcast` to correct the truncated edge, then `/estimate-rt`. A nowcast-corrected Rt crossing 1 from above is a peak; a Friday→Sunday dip in raw counts is not.

### Standing up automated outbreak detection for a notifiable disease
Use `/detect-aberration` with the Farrington algorithm over several years of weekly counts to set a seasonally-adjusted baseline, then schedule it to flag weeks exceeding the upper threshold.

### Producing a 2-week-ahead hospitalisation forecast for capacity planning
`/forecast-incidence` (renewal or ensemble) generates the projection with prediction intervals; `/score-forecast` against the realised counts tells you whether your intervals are calibrated before the next round.

### Recovering R0 and the latent period from an early outbreak curve
`/fit-compartmental` fits an SEIR model to the growth phase, returning R0, the incubation/latent split, and parameter uncertainty for scenario work.

### Communicating epidemic speed to non-modellers
`/growth-rate` translates the curve into a doubling/halving time and an equivalent Rt — the numbers decision-makers actually use.

## Recommended MCP Servers

- **Filesystem MCP** — read surveillance CSVs from a data drop and write estimates/forecasts back to `outputs/`.
- **Fetch / HTTP MCP** — pull open surveillance feeds (WHO FluNet, US CDC FluView/RESP-NET, ECDC, Our World in Data) and forecast-hub truth data.
- **Python/Jupyter execution MCP** — run `EpiEstim`/`epyestim`, STL, and scoring code and capture plots into `outputs/`.

## Legal & Ethical Considerations

- **Case-level data is protected health information.** Line lists carry PII/PHI. Aggregate before sharing, follow HIPAA / GDPR and any data-use agreement, suppress small cell counts, and never persist identifiers in `outputs/` or commits.
- **Models inform; authorities decide.** Outputs are estimates with uncertainty, not directives. Surface assumptions (serial interval, ascertainment, delay model) and never present a point forecast without its interval.
- **Avoid stigma and misattribution.** Frame geographic/demographic strata carefully; a higher count can reflect more testing, not more disease. State ascertainment caveats explicitly.

## Technical References

- [Cori et al. 2013, *A New Framework and Software to Estimate Time-Varying Reproduction Numbers* (EpiEstim)](https://doi.org/10.1093/aje/kwt133) — the instantaneous-Rt method most commands lean on.
- [Gostic et al. 2020, *Practical considerations for measuring Rt*](https://doi.org/10.1371/journal.pcbi.1008409) — the pitfalls every Rt estimate must avoid (right-truncation, smoothing, interval choice).
- [Abbott et al. 2020, *EpiNow2 / estimating Rt with reporting delays*](https://doi.org/10.12688/wellcomeopenres.16006.2) — renewal-based nowcast + Rt + forecast pipeline.
- [Cleveland et al. 1990, *STL: Seasonal-Trend decomposition*](https://www.wessa.net/download/stl.pdf) — the decomposition behind `/decompose-trend`.
- [Farrington et al. 1996, *A statistical algorithm for the early detection of outbreaks*](https://doi.org/10.2307/2983331) — the aberration detector behind `/detect-aberration`.
- [Cramer et al. 2022, *Evaluation of individual and ensemble probabilistic forecasts of COVID-19 mortality* (WIS)](https://doi.org/10.1073/pnas.2113561119) — scoring used by `/score-forecast`.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
