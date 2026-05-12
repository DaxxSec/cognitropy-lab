# Custody Manifest Schema

The custody manifest is the single source of truth for every artifact this workspace produces. Each entry is append-only; corrections add a new entry that references a prior one.

## Top-Level Index — `outputs/manifests/INDEX.json`

```json
{
  "schema": 1,
  "items": [ /* entries below */ ]
}
```

## Entry: `vintage`

```json
{
  "kind": "vintage",
  "id": "vintage:fred-alfred:GDPC1:2026-04-30",
  "source": "fred-alfred",
  "series_id": "GDPC1",
  "vintage_date": "2026-04-30",
  "retrieved_utc": "2026-04-30T13:02:11Z",
  "raw_path": "outputs/vintages/fred-alfred/GDPC1/raw/2026-04-30.json",
  "raw_sha256": "…",
  "parquet_path": "outputs/vintages/fred-alfred/GDPC1/v2026-04-30.parquet",
  "parquet_sha256": "…",
  "license": "FRED Terms of Use",
  "embargoed_until": null,
  "git_sha": "…",
  "agent": "claude-code:macroeconomics-gdp-modeling/v1.0",
  "prior_vintage_diff": {
    "rows_added": 0,
    "rows_revised": 1,
    "max_abs_revision_pct": 0.32
  },
  "created_utc": "2026-04-30T13:02:13Z"
}
```

## Entry: `model`

```json
{
  "kind": "model",
  "id": "model:bvar:2026-04-30:abc1234",
  "model_class": "bvar",
  "hyperparameters": {
    "lags": 4,
    "minnesota_lambda": 0.1,
    "shrinkage_strategy": "litterman"
  },
  "training_window": ["1995-Q1", "2026-Q1"],
  "input_vintages": [
    {"id": "vintage:fred-alfred:GDPC1:2026-04-30", "sha256": "…"},
    {"id": "vintage:fred-alfred:PAYEMS:2026-04-30", "sha256": "…"}
  ],
  "artifact_path": "outputs/models/bvar__2026-04-30__abc1234.joblib",
  "artifact_sha256": "…",
  "sidecar_path": "outputs/models/bvar__2026-04-30__abc1234.json",
  "validation": {
    "method": "pseudo_realtime_walkforward",
    "horizon_quarters": [0, 1, 2, 3, 4],
    "rmsfe": [0.4, 0.6, 0.8, 0.9, 1.0],
    "mae": [0.3, 0.45, 0.6, 0.7, 0.8],
    "log_score": null
  },
  "library_versions": {
    "numpy": "1.26.4",
    "pandas": "2.2.1",
    "statsmodels": "0.14.1",
    "scikit-learn": "1.4.0"
  },
  "random_seed": 42,
  "git_sha": "…",
  "created_utc": "2026-04-30T15:11:42Z"
}
```

## Entry: `nowcast` / `forecast`

```json
{
  "kind": "nowcast",
  "id": "nowcast:dfm:2026-04-30:abc1234",
  "model_ref": "model:dfm:2026-04-26:abc1234",
  "target_quarter": "2026Q2",
  "decision_date": "2026-04-30",
  "point": 1.8,
  "band_68": [1.4, 2.2],
  "band_95": [0.9, 2.7],
  "convention": "annualised_qoq",
  "decomposition": {
    "PAYEMS": 0.4,
    "INDPRO": 0.3,
    "RRSFS": 0.2,
    "NAPM": 0.1
  },
  "forecast_path": "outputs/forecasts/nowcast_2026Q2__v2026-04-30.json",
  "forecast_sha256": "…",
  "git_sha": "…",
  "created_utc": "2026-04-30T15:33:00Z"
}
```

## Entry: `revision_audit`

```json
{
  "kind": "revision_audit",
  "id": "revision_audit:GDPC1:2024Q1:2026-04-30",
  "series_id": "GDPC1",
  "target_quarter": "2024Q1",
  "prior_vintage_id": "vintage:fred-alfred:GDPC1:2026-04-15",
  "new_vintage_id": "vintage:fred-alfred:GDPC1:2026-04-30",
  "model_ref": "model:bvar:2026-03-30:def5678",
  "decomposition": {
    "data_revision": 0.2,
    "model_drift": -0.1,
    "innovation": 0.3
  },
  "audit_path": "outputs/forecasts/revision_audit__2024Q1__v2026-04-30.md",
  "audit_sha256": "…",
  "git_sha": "…",
  "created_utc": "2026-04-30T16:05:00Z"
}
```

## Entry: `comparison`

```json
{
  "kind": "comparison",
  "id": "comparison:2026-04-30",
  "forecast_set_refs": ["forecast:bvar:…", "forecast:dfm:…", "forecast:gbr:…"],
  "realised_target_vintage_id": "vintage:fred-alfred:GDPC1:2026-04-30",
  "horizons": [0, 1, 4],
  "report_path": "outputs/forecasts/comparison__2026-04-30/REPORT.md",
  "report_sha256": "…",
  "git_sha": "…",
  "created_utc": "2026-04-30T17:20:00Z"
}
```

## Entry: `release`

```json
{
  "kind": "release",
  "id": "release:2026-04-30",
  "audience": "client",
  "bundle_path": "outputs/forecasts/release__2026-04-30/",
  "manifest_path": "outputs/forecasts/release__2026-04-30/manifest.json",
  "manifest_sha256": "…",
  "signature_path": "outputs/forecasts/release__2026-04-30/manifest.json.asc",
  "signing_fingerprint": "…",
  "included_forecast_refs": ["forecast:bvar:…"],
  "git_sha": "…",
  "created_utc": "2026-04-30T18:00:00Z"
}
```

## Entry: `correction`

```json
{
  "kind": "correction",
  "id": "correction:2026-04-30:001",
  "corrects_id": "model:bvar:2026-04-29:abc0000",
  "reason": "validation metric was computed with leaked future vintage; recomputed against sealed prior vintages",
  "corrected_fields": ["validation.rmsfe"],
  "new_values": {"validation.rmsfe": [0.45, 0.65, 0.85, 0.95, 1.05]},
  "git_sha": "…",
  "created_utc": "2026-04-30T19:30:00Z"
}
```

## Validation Rules

- `id` is globally unique within the index.
- `git_sha` references a clean commit (the agent verifies before writing).
- All `*_sha256` are 64-character hex digests.
- All `*_utc` are ISO-8601 with `Z` timezone.
- `corrects_id` (corrections only) must reference an existing entry by `id`.
- Corrections never delete or rewrite the original — they exist alongside it.

## Why This Schema Is What It Is

The schema is deliberately verbose. Every redundancy (e.g. carrying both `id` references and `sha256` digests on input pointers) exists so an auditor with the manifest alone — without git, without the artifacts — can still verify integrity by cross-checking hashes. When the artifacts are then provided, the chain closes.
