# /compare-forecasts — Score Forecast Sets Against Realised Vintages

Run a head-to-head comparison of multiple forecast sets (own model variants, consensus, SPF, GDPNow) against realised vintages. Honest scoring uses the vintage that was current at decision time as the forecast input set, and a stable later-revision vintage as the realised target.

## Required Inputs

- Forecast sets: list of paths to JSON forecast bundles (own forecasts under `outputs/forecasts/`; external forecasts loaded into `inputs/external_forecasts/`).
- Realised target vintage: which vintage to treat as ground truth (default: latest sealed vintage at run time).
- Evaluation horizons: list of `h` values (`h=0` nowcast, `h=1`, `h=4`, etc.).
- Window: number of quarters to include in the comparison (default: last 20 realised quarters).

## Steps

### 1. Align observations
For each forecast set, build a `(target_quarter, horizon, decision_date, point_forecast, lower95, upper95)` table. Drop any observations where the decision date precedes the existence of an input vintage required by that forecast (i.e. cannot have used data not yet released).

### 2. Compute headline metrics per forecast set
- **RMSFE** by horizon.
- **MAE** by horizon.
- **Bias** (mean signed error).
- **Coverage** (fraction of realised observations falling inside 95% bands).
- **Log score** if forecasts are probabilistic.

### 3. Pairwise tests
For each pair of forecast sets:
- **Diebold–Mariano** test on squared errors (HAC variance, lag = h-1).
- **Giacomini–White** conditional predictive ability test where appropriate.

### 4. Visualisations
Produce `outputs/forecasts/comparison__<YYYY-MM-DD>/` with:
- `metrics.csv` — full metric table.
- `dm_matrix.csv` — pairwise DM stats and p-values.
- `errors_by_quarter.png` — line chart of forecast errors over time.
- `coverage_band.png` — coverage diagnostic.

### 5. Write a comparison report
`outputs/forecasts/comparison__<YYYY-MM-DD>/REPORT.md`:
- Top-line: which forecast set wins on RMSFE at each horizon.
- Where the wins are statistically significant vs. the runner-up.
- Failure modes: which periods (recessions, COVID, supply shocks) caused which forecasts to diverge.
- Recommendation: keep current model, swap to a different variant, ensemble.

### 6. Append to custody manifest
Add a `kind: "comparison"` entry referencing all input forecast manifests and the comparison artifacts.

## Output

A timestamped comparison directory containing metrics, statistical tests, plots, and a written recommendation. This is the artifact for quarterly model-review meetings.

## Caveats

- **External forecasts are inputs, not benchmarks for retro-fit.** Never tune your model class to beat the consensus on a backtest; that's overfitting to the comparison.
- **Real-time discipline.** External forecasts (SPF, GDPNow) carry their own decision dates; align them to the same decision-date axis as your own forecasts.
- **Sample selection bias.** If you only compare on quarters where all sets have a forecast, you may select away from inception-period quarters where new sets were warming up. Document the inclusion rule.
