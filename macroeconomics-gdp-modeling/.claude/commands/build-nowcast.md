# /build-nowcast — Construct or Refresh a Current-Quarter GDP Nowcast

Spin up (or refresh) a current-quarter GDP nowcast using the sealed vintages as the only inputs. Default model class is a small dynamic factor model (DFM); supports bridge equations and MIDAS regressions.

## Required Inputs

- Target series (e.g. `GDPC1`), already sealed for this vintage.
- Indicator panel: monthly series (payrolls, IP, retail sales, ISM, hours, real PCE goods, building permits) — all must be sealed in the latest vintage.
- Model class: `dfm` (default), `bridge`, `midas`.
- Reference quarter: defaults to the current quarter; allow override for backfilled tests.

## Steps

### 1. Verify input lineage
For each declared input series, look up the latest vintage in `outputs/manifests/INDEX.json`. Refuse to build if any series is older than the target vintage cutoff (typical rule: indicators must be at most one release cycle behind today's run).

### 2. Build the indicator panel
Load the parquet vintages, align to a monthly grid, apply the canonical transformations (log first difference for real series, MoM percent for diffusion indices, level for surveys). Record every transformation step in the run manifest.

### 3. Fit the model
- **DFM:** estimate via Kalman filter / EM. One factor by default; allow user to override. Identify factor loadings by anchoring the first loading on payrolls = 1 (a standard convention).
- **Bridge:** OLS of quarterly GDP growth on quarterly aggregates of the monthly indicators.
- **MIDAS:** Almon-lag MIDAS regression with a small number of lags.

For every fit:
- Pin `numpy`/`pandas`/`statsmodels` versions.
- Pin random seed (where applicable).
- Save the fitted model to `outputs/models/nowcast__<class>__<YYYY-MM-DD>__<git_sha>.joblib`.
- Save the JSON sidecar with hyperparameters, input vintage hashes, validation RMSFE on a 20-quarter pseudo-real-time backtest.

### 4. Produce the nowcast
- Forecast the current quarter, log the point forecast, 68% and 95% bands.
- Decompose the forecast into indicator contributions (Stock–Watson decomposition for DFM, regression decomposition for bridge/MIDAS).
- Write `outputs/forecasts/nowcast_<targetQ>__v<YYYY-MM-DD>.json` with the point forecast, bands, decomposition, model artifact hash, and input vintage manifest reference.

### 5. Append to the custody manifest
Add a `kind: "nowcast"` entry to `outputs/manifests/INDEX.json` referencing the model and forecast artifacts.

### 6. Write a decision note
Drop a one-page note in `work-log/<YYYY-MM-DD>.md` summarising: model class, biggest indicator contribution this round, change vs. last nowcast, any data anomalies (large revisions, missing series).

## Output

A sealed nowcast forecast JSON, a tagged model artifact, an updated custody manifest, and a dated decision note. Optionally trigger `/release-forecast` if this nowcast is the one to be published externally.

## Validation Targets

- **In-sample RMSFE:** compare to the published GDPNow / NY Fed Nowcast for the same quarter (informational only — never use external nowcasts as inputs to your own).
- **Coverage:** 95% bands should cover the realised print ≥ 85% of the time on a rolling 20-quarter window. Below 80% triggers a model review note in `planning/`.
