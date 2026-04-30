# Domain Knowledge — Macroeconomics GDP Modeling under Chain-of-Custody

This file is the agent's reference for GDP measurement, real-time data discipline, modeling methodology, and the forensic chain-of-custody concepts that underpin the workspace. Read this before authoring any forecast.

## 1. What GDP Actually Is

GDP can be measured three ways; in equilibrium they are equal, but in practice they differ due to imputation choices and statistical discrepancy.

### Expenditure Approach
$$\\text{GDP} = C + I + G + (X - M)$$
- **C** — Personal Consumption Expenditures (PCE): durables, nondurables, services. ~67% of US GDP.
- **I** — Gross Private Domestic Investment: nonresidential fixed (structures, equipment, IP), residential, change in private inventories.
- **G** — Government Consumption + Investment: federal (defense + nondefense) + state and local.
- **X − M** — Net Exports of Goods and Services.

### Production (Output / Value-Added) Approach
Sum of value added across industries (Compensation of Employees + Gross Operating Surplus + Taxes − Subsidies on production), aggregated by NAICS / NACE / ISIC.

### Income Approach (GDI)
$$\\text{GDI} = \\text{Compensation} + \\text{Net Operating Surplus} + \\text{Consumption of Fixed Capital} + \\text{Taxes on Production} - \\text{Subsidies}$$

GDP and GDI should equal but rarely do; the **statistical discrepancy** is the residual. Some forecasters use the average of GDP and GDI as a less-noisy growth estimate (Aruoba–Diebold–Scotti, BEA's "GDPplus").

### Real vs. Nominal vs. Chained
- **Nominal GDP:** value at current prices.
- **Real GDP:** value adjusted for price changes. Modern series use **chained dollars** (e.g. chained 2017 dollars in the US), avoiding the substitution bias of fixed-base Laspeyres indices.
- **Annualised growth:** US convention reports `((GDP_t / GDP_{t-1})^4 - 1) * 100` as the headline. EU convention uses non-annualised QoQ.

## 2. Vintages, Real-Time Data, and Why They Matter

A "vintage" is a snapshot of an economic time series at a specific point in time. The same `(observation_date, series_id)` pair has different values across vintages.

### Why Vintages Differ
- **First release ("advance estimate"):** based on incomplete source data; large blocks (services, healthcare, inventories) are imputed.
- **Second / third estimates:** more complete source data; smaller imputations.
- **Annual / benchmark revisions:** incorporate IRS data, business census, BLS QCEW; can revise levels back many years.
- **Comprehensive (NIPA) revisions:** every ~5 years; can change methodology (e.g. capitalising R&D in 2013).

### Real-Time Forecasting Discipline
Honest backtesting must use the vintage **available at decision time**, never the latest revised series. The classic mistake — fitting a model on revised history and "validating" against revised data — produces forecast skill that does not exist in real-time deployment.

The Federal Reserve Bank of Philadelphia's **real-time data set for macroeconomists** (RTDSM) and the FRED ALFRED database are the canonical sources for this.

### Vintage Naming Convention (this workspace)
- File: `outputs/vintages/<source>/<series>/v<YYYY-MM-DD>.parquet` where the date is the **retrieval date**, not the observation date.
- The parquet schema includes a `vintage_date` column matching the retrieval date.
- Original source response is preserved at `outputs/vintages/<source>/<series>/raw/<YYYY-MM-DD>.<ext>`.

## 3. Modeling Methodology

### 3.1 Bridge Equations (h=0 nowcast)
Quarterly GDP regressed on quarterly aggregates of monthly indicators:
$$\\Delta y_t = \\beta_0 + \\sum_k \\beta_k \\Delta x_{k,t} + \\epsilon_t$$
where $x_{k,t}$ is, e.g., the quarterly average of monthly industrial production. Simple, transparent, robust. Fails when monthly indicators have unusual within-quarter timing.

### 3.2 MIDAS (Mixed-Data Sampling) Regressions
Allow direct mapping of monthly (or weekly) indicators to a quarterly target using a parameterised lag polynomial (Almon, exponential Almon, beta lag):
$$y_t = \\beta_0 + \\beta_1 B(L^{1/m}; \\theta) x_t^{(m)} + \\epsilon_t$$
Useful when the timing of within-quarter information matters (e.g. ISM mid-month vs. payrolls early-month).

### 3.3 Dynamic Factor Models (DFM)
Common factors $f_t$ drive a panel of indicators:
$$x_{i,t} = \\lambda_i f_t + \\epsilon_{i,t}, \\quad f_t = A f_{t-1} + u_t$$
Estimated via Kalman filter / EM. The factor is interpreted as the "common business cycle"; the nowcast is the projection of GDP on the factor. Stock & Watson is the canonical reference; the New York Fed Nowcast and Atlanta Fed GDPNow are practitioner implementations.

### 3.4 VAR / BVAR
Vector autoregression of the target with relevant exogenous series. Bayesian VAR with **Minnesota prior** (own-lag coefficients shrunk toward 1, cross-lag toward 0, with overall tightness $\\lambda$) is standard for US/EU horseraces. Reference: Litterman 1986; Banbura, Giannone, Reichlin 2010.

### 3.5 Small DSGE
A 3-equation New Keynesian model (IS curve, Phillips curve, Taylor rule) provides a structural alternative. State-space estimation via Bayesian methods. Useful for counterfactual analysis; less competitive on raw forecast accuracy at short horizons.

### 3.6 ML Regressors
Gradient boosted regressors (`xgboost`, `lightgbm`, `sklearn` GBR) on engineered features (lagged indicators, MoM and YoY transformations, regime dummies). Typical performance: comparable to BVAR at short horizons, occasionally better at h=0 in volatile periods, generally worse for structural interpretation. ElasticNet provides a sparse linear baseline.

## 4. The ML-Training Discipline (Why We Borrow It)

ML practitioners learned the hard way that a model fit is not reproducible unless every input is pinned. The discipline:

| ML practice | GDP-modeling analogue |
|-------------|------------------------|
| Pin random seed | Pin random seed for any sampler / bootstrap |
| Save model artifact (joblib / pickle) | Save fitted model + sidecar JSON |
| Log hyperparameters (MLflow / wandb) | Log hyperparameters in manifest sidecar |
| Pin dataset hash (DVC) | SHA-256 every input vintage |
| Pin code revision (git tag) | Pin git SHA; refuse to fit dirty tree |
| Track experiments | `outputs/manifests/INDEX.json` is the experiment ledger |
| Backtest carefully (no leakage) | Real-time vintage discipline (no peek-ahead) |

This workspace treats every model fit as a reproducible training run. If you cannot rebuild the artifact bit-for-bit from sealed inputs and the pinned git SHA, the fit is not finished.

## 5. The Chain-of-Custody Discipline (Why We Borrow It)

Forensic chain of custody is the practice of recording, for every piece of evidence:
- **Provenance** — where it came from, when, who collected it.
- **Integrity** — a hash that makes tampering detectable.
- **Continuity** — every transfer, transformation, and access is logged.

NIST SP 800-86 is a primer. Applied to GDP forecasting:
- A **vintage** is evidence: who pulled it, from where, when, with what hash.
- A **transformation** (seasonal adjustment, log diff) is a custody event: input hashes, code commit, parameters, output hash.
- A **fitted model** is downstream evidence with a chain back to its inputs.
- A **published forecast** is the final exhibit; its manifest lets a third party walk the chain back to raw bytes.

This converts "I think we used the Q1 advance estimate" into "the manifest shows we used vintage v2024-04-25 with SHA-256 abc123..." — auditable and reproducible.

## 6. Common Failure Modes

### "Look-ahead leakage"
Backtesting with revised data. Solved by always loading the vintage current at decision time.

### "Manifest drift"
Manifest entries that no longer match the artifacts they describe (e.g. someone re-ran a fit with different parameters). Solved by hashing artifacts on write and re-verifying hashes before any release.

### "Embargo violation"
Publishing a forecast that depends on a series under press embargo. Solved by carrying `embargoed_until` on every vintage and gating release.

### "Benchmark revision shock"
A 5-year comprehensive revision moves levels back decades; naive auto-refit produces a discontinuous model. Solved by structured `/audit-revision` decomposition before refitting.

### "Real-time vs. final confusion in evaluation"
Comparing forecasts against the latest revised series rather than a stable later-revision vintage. Solved by tagging the realised target vintage explicitly in `/compare-forecasts`.

### "Single-model overconfidence"
Reporting a point forecast without bands. Solved by always carrying 68%/95% bands and a rolling coverage diagnostic.

### "Pseudo-real-time validation that isn't"
Walk-forward backtest using the latest revised series as the input panel, then claiming "real-time" performance. Solved by sourcing inputs from the vintage parquet store, indexed by decision date.

## 7. Glossary

- **ALFRED** — Archival FRED, the real-time vintage database from the St. Louis Fed.
- **DM test** — Diebold–Mariano test for equal predictive accuracy.
- **DFM** — Dynamic Factor Model.
- **GDPNow** — Atlanta Fed's nowcast.
- **GW test** — Giacomini–White conditional predictive ability test.
- **ISM** — Institute for Supply Management; produces the Manufacturing PMI (and Services PMI).
- **MIDAS** — Mixed-Data Sampling regression.
- **NIPA** — National Income and Product Accounts (US).
- **RMSFE** — Root Mean Squared Forecast Error.
- **RTDSM** — Real-Time Data Set for Macroeconomists (Philadelphia Fed).
- **SA / NSA** — Seasonally Adjusted / Not Seasonally Adjusted.
- **SDMX** — Statistical Data and Metadata eXchange — the API protocol used by OECD, Eurostat, ECB, IMF.
- **SPF** — Survey of Professional Forecasters (Philadelphia Fed).
- **VAR / BVAR** — Vector AutoRegression / Bayesian VAR.
- **X-13ARIMA-SEATS** — Census Bureau seasonal adjustment program.

## 8. Authoritative References

- Stock, J. H. & Watson, M. W. (2016). "Dynamic Factor Models, Factor-Augmented Vector Autoregressions, and Structural Vector Autoregressions in Macroeconomics." *Handbook of Macroeconomics*, Vol. 2A.
- Ghysels, E., Sinko, A., & Valkanov, R. (2007). "MIDAS Regressions: Further Results and New Directions." *Econometric Reviews*.
- Banbura, M., Giannone, D., & Reichlin, L. (2010). "Large Bayesian Vector Auto Regressions." *Journal of Applied Econometrics*.
- Giannone, D., Reichlin, L., & Small, D. (2008). "Nowcasting: The Real-Time Informational Content of Macroeconomic Data." *Journal of Monetary Economics*.
- Diebold, F. X. & Mariano, R. S. (1995). "Comparing Predictive Accuracy." *Journal of Business & Economic Statistics*.
- Croushore, D. & Stark, T. (2001). "A Real-Time Data Set for Macroeconomists." *Journal of Econometrics*.
- NIST SP 800-86. *Guide to Integrating Forensic Techniques into Incident Response.*
- BEA. *Concepts and Methods of the U.S. National Income and Product Accounts.*
