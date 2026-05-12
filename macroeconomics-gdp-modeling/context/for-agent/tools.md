# Tools — Concrete Recipes for Sources, Models, and Custody

This is the agent's how-to: every external source has a worked retrieval pattern, every model class has a `statsmodels` / `sklearn` / `pymc` recipe, and every custody operation has a code snippet. Update this file when a source's API contract changes.

## A. Source Retrieval

### A.1 FRED / ALFRED

```python
import requests, os, hashlib, json
from datetime import datetime, timezone

def fetch_alfred(series_id: str, vintage: str) -> dict:
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "realtime_start": vintage,
        "realtime_end": vintage,
        "api_key": os.environ["FRED_API_KEY"],
        "file_type": "json",
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return {
        "raw_bytes": r.content,
        "sha256": hashlib.sha256(r.content).hexdigest(),
        "retrieved_utc": datetime.now(tz=timezone.utc).isoformat(),
        "json": r.json(),
    }
```

ALFRED returns `observations` with `realtime_start` / `realtime_end` indicating the vintage window for each value. Persist the full `r.content` as the raw evidence; never re-fetch and overwrite.

### A.2 BEA NIPA

```python
def fetch_bea(table_id: str, freq: str = "Q") -> dict:
    url = "https://apps.bea.gov/api/data"
    params = {
        "UserID": os.environ["BEA_API_KEY"],
        "method": "GetData",
        "DataSetName": "NIPA",
        "TableName": table_id,           # e.g. "T10101"
        "Frequency": freq,
        "Year": "X",
        "ResultFormat": "JSON",
    }
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    return r.content
```

BEA NIPA tables: `T10101` (real GDP, % change), `T10105` (real GDP levels), `T20100` (PCE), `T50100` (investment).

### A.3 OECD SDMX

OECD MEI accepts SDMX-JSON. Country-quarterly real GDP example:

```
https://stats.oecd.org/SDMX-JSON/data/QNA/USA.B1_GE.LNBQRSA.Q/all
```

Use `pandasdmx` for typed parsing. Always store the raw JSON response in the vintage `raw/` directory before parsing.

### A.4 Eurostat SDMX

```
https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/namq_10_gdp/Q.CLV10_MEUR.SCA.B1GQ.EA19?format=JSON
```

Dataset `namq_10_gdp` is the canonical euro-area GDP table. `pandasdmx` works against this endpoint as well.

### A.5 National stats offices

Most national offices expose either SDMX or a custom REST API. Examples: ONS (UK) — `https://api.ons.gov.uk`, INSEE (France), Destatis (Germany), IBGE (Brazil). For each, store the raw response and document the endpoint in the manifest entry.

## B. Hashing and Sealing

### B.1 Hash a file

```python
def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()
```

### B.2 Append to the custody index (atomic)

```python
def append_manifest(entry: dict, index_path: str) -> None:
    with open(index_path, "r+") as f:
        idx = json.load(f)
        idx["items"].append(entry)
        f.seek(0)
        json.dump(idx, f, indent=2)
        f.truncate()
```

Appending is the only allowed mutation; never delete or rewrite an entry. Corrections go in as new `kind: "correction"` entries that reference the prior entry by index.

### B.3 GPG detach-sign

```bash
gpg --detach-sign --armor --local-user "$KEY_FP" outputs/manifests/v2026-04-30.json
```

Verify with `gpg --verify outputs/manifests/v2026-04-30.json.asc outputs/manifests/v2026-04-30.json`.

## C. Modeling Recipes

### C.1 Bridge equation

```python
import statsmodels.api as sm
X = sm.add_constant(quarterly_indicators)
model = sm.OLS(quarterly_gdp_growth, X).fit(cov_type="HAC", cov_kwds={"maxlags": 4})
```

### C.2 DFM (statsmodels)

```python
from statsmodels.tsa.statespace.dynamic_factor import DynamicFactor
mod = DynamicFactor(panel_standardised, k_factors=1, factor_order=2,
                    error_order=0, error_cov_type="diagonal")
res = mod.fit(disp=False)
nowcast = res.forecast(steps=h)
```

### C.3 BVAR with Minnesota prior (statsmodels + manual prior)

```python
from statsmodels.tsa.api import VAR
var = VAR(endog=panel)
res = var.fit(maxlags=4, ic="bic")
# Bayesian shrinkage applied via posterior mode of conjugate Normal-Inverse-Wishart;
# implementation in helpers/bvar_minnesota.py (user-authored or from BVAR package).
```

### C.4 Gradient Boosted Regressor

```python
from sklearn.ensemble import GradientBoostingRegressor
gbr = GradientBoostingRegressor(
    n_estimators=300, max_depth=3, learning_rate=0.05,
    subsample=0.7, random_state=42,
)
gbr.fit(X_train, y_train)
```

Always set `random_state` and persist via `joblib.dump`.

### C.5 Pseudo-real-time backtest harness

```python
def realtime_backtest(make_panel_at, fit, score, decision_dates):
    errs = []
    for d in decision_dates:
        panel = make_panel_at(d)               # only vintages with retrieved_utc <= d
        target = realised_value_for(d, latest=False)  # use stable later-revision vintage
        f = fit(panel)
        errs.append(score(f.forecast(steps=1), target))
    return errs
```

The honesty of the backtest depends entirely on `make_panel_at` only sourcing from sealed vintages with `retrieved_utc <= d`.

## D. Diagnostic Tests

### D.1 Diebold–Mariano

```python
import numpy as np
from scipy import stats

def dm_test(e1, e2, h=1):
    d = e1**2 - e2**2
    n = len(d)
    mean = d.mean()
    # HAC variance (Newey-West) with bandwidth h-1
    gamma0 = np.var(d, ddof=1)
    gammas = [np.cov(d[:-k], d[k:], ddof=1)[0, 1] for k in range(1, h)]
    var_d = gamma0 + 2 * sum(gammas)
    dm = mean / np.sqrt(var_d / n)
    p = 2 * (1 - stats.norm.cdf(abs(dm)))
    return dm, p
```

### D.2 Coverage diagnostic

```python
covered = ((realised >= lower) & (realised <= upper)).mean()
```

A 95% band whose realised coverage is below 0.85 over a 20-quarter window indicates underestimated forecast variance; investigate.

## E. Custody Manifest Schema (operational)

See `resources/custody-manifest-schema.md` for the JSON Schema. Operationally:

- Every `kind` ∈ {`vintage`, `nowcast`, `model`, `forecast`, `revision_audit`, `comparison`, `release`, `correction`}.
- Every entry carries a `git_sha` field referencing a clean commit.
- Every entry carries `created_utc` in ISO-8601.
- Hash-bearing fields end in `_sha256`.
- Path fields are repository-relative.

When in doubt, validate the entry against the schema before writing.
