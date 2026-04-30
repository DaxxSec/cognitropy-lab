# /estimate-model — Fit a Horizon-Extending GDP Model with Full Lineage

Fit a longer-horizon GDP forecasting model (BVAR, small DSGE, or ML regressor) and emit a tagged training-run artifact. Use this when extending beyond the nowcast horizon, or when comparing model classes.

## Required Inputs

- Model class: `var`, `bvar`, `dsge` (small open-economy or 3-equation NK), `ml-gbr` (gradient boosted regressor), `ml-elasticnet`.
- Training window: start and end vintage dates (default: 1995-Q1 through latest sealed quarter).
- Target series and exogenous panel (read from `context/project.md`).
- Hyperparameters: lag length, BVAR Minnesota prior tightness, DSGE calibration set, GBR `max_depth`/`learning_rate`/`n_estimators`/`random_state`.

## Steps

### 1. Pre-flight lineage check
Confirm: clean git working tree, latest vintages sealed, target series and all exogenous series accounted for. Refuse to fit if any series is missing a current seal.

### 2. Build the training matrix from sealed vintages
For each historical quarter, load the **vintage that was current at the time** (real-time matrix), not the latest revised series. This is the "real-time" training set that gives honest validation. Record the vintage policy in the manifest.

### 3. Fit
- **VAR / BVAR:** `statsmodels.tsa.api.VAR` / Bayesian variant with Minnesota prior. Lag selection by BIC unless overridden.
- **DSGE:** state-space estimation via `statsmodels` or `pymc`; record posterior draws if Bayesian.
- **ML-GBR:** `sklearn.ensemble.GradientBoostingRegressor` or `xgboost`, with feature engineering described in `context/for-agent/workflows.md`.
- **ML-ElasticNet:** `sklearn.linear_model.ElasticNetCV`.

### 4. Validate (pseudo-real-time backtest)
Walk-forward fit/forecast over the last 40 quarters using only the vintage available at decision time. Compute RMSFE, MAE, log-score, and Diebold–Mariano vs. the previous-best model in `outputs/models/`.

### 5. Tag and seal the artifact
- Save `outputs/models/<class>__<YYYY-MM-DD>__<git_sha>.joblib`.
- Sidecar JSON with: model class, hyperparameters, random seed, library versions (`numpy`, `pandas`, `statsmodels`, `scikit-learn`, `arch`, `pymc` if used), input vintage manifest entries (paths + sha256), training period, validation metrics, fit duration.
- Append a `kind: "model"` entry to `outputs/manifests/INDEX.json`.

### 6. Compare to incumbent
If a previous model artifact exists for the same target series, run a paired Diebold–Mariano test on the overlapping pseudo-real-time validation period. Log the result.

### 7. Write a fit report
`outputs/forecasts/<class>__fitreport__v<YYYY-MM-DD>.md` summarising the fit, validation metrics, comparison to incumbent, and recommended action (promote, keep parallel, retire).

## Output

A tagged model artifact, a JSON sidecar with training-run lineage, an updated custody manifest, a fit report, and a decision recommendation. The model is now eligible to be referenced by `/release-forecast`.

## Reproducibility Contract

A future user with this workspace, the sealed vintages, the same git SHA, and the same Python environment must be able to rerun this command and obtain a model artifact whose hash matches (modulo non-deterministic floating-point reductions, which the manifest documents per backend). If the rerun differs by more than the documented tolerance, file an issue in `planning/` — that is a reproducibility regression.
