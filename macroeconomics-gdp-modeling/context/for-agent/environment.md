# Environment

> Populated by `/onboard`. Defaults below describe the assumed environment.

## Operating System

- macOS 13+ or Linux (Ubuntu 22.04+ tested). Windows works under WSL2; native Windows untested for the GPG signing path.

## Python

- **3.10 or 3.11** (3.12 also works; some scientific stacks lag — pin via `requirements.txt`).
- Virtual environment via `venv` or `uv` recommended.

### Required Packages

```
pandas>=2.0
numpy>=1.24
statsmodels>=0.14
scikit-learn>=1.3
arch>=6.0
pyarrow>=14   # parquet IO
fastparquet   # alternative parquet engine
requests
```

### Optional Packages

```
xgboost            # gradient boosted regressors
lightgbm           # alternative GBR
pymc>=5            # Bayesian DSGE / BVAR
dynamax            # state-space models in JAX
linearmodels       # for panel/IV variants
matplotlib         # comparison plots
seaborn            # comparison plots
duckdb             # local OLAP over sealed parquet
```

## Tooling

- **git** — required. Every model fit pins a SHA; the agent refuses to fit a dirty tree.
- **gpg** — optional but recommended for any external publication. Used by `/release-forecast` to detach-sign the manifest.
- **X-13ARIMA-SEATS** — optional; used by `statsmodels.tsa.x13_arima_analysis` for custom seasonal adjustment audits.

## API Keys (read from environment)

| Variable | Purpose | How to obtain |
|----------|---------|---------------|
| `FRED_API_KEY` | FRED / ALFRED retrieval | https://fred.stlouisfed.org/docs/api/api_key.html |
| `BEA_API_KEY` | BEA NIPA direct (optional; FRED mirrors most series) | https://apps.bea.gov/api/signup/ |
| `ECB_API_KEY` | Optional, for ECB SDW | not required for euro-area data via Eurostat |

The agent **never logs** key values. The custody manifest records only that a key was present at retrieval time, not its value.

## Disk

- Default budget: 2 GB / year per ~50-series panel under daily snapshotting.
- Sealed vintage parquet files compress well (~5–20 KB per series-vintage); the raw source responses are larger but small relative to model artifacts.
- Plan for offsite backup of `outputs/vintages/` and `outputs/manifests/` — these are the irrecoverable evidence.

## Network

- Retrieval is HTTPS only. Default timeout: 30s with 5 retries on 5xx with exponential backoff.
- The agent respects rate limits (FRED: 120 requests/min; OECD/Eurostat: ~1 request/sec safe).
- A polite default `User-Agent` of `cognitropy-gdp-agent/1.0 (+contact-from-context)` is set on all outbound calls.

## Repository Layout (operational)

The workspace is itself a git repository. Recommended `.gitignore`:

```
# Python
__pycache__/
*.pyc
.venv/
.env

# OS
.DS_Store

# Sealed vintages: track with git LFS if size grows; otherwise commit
# (manifest files MUST be committed — they are the audit trail)
```

Sealed vintages and manifests **must be committed** — they are the audit trail. If size becomes a problem, route to git-lfs rather than to a non-tracked store.
