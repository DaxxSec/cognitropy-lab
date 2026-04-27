# Tools — Libraries, Frameworks, Standards, External Services

The agent uses these as needed; they are *optional*. The workspace is fully usable in qualitative-only mode (no Python, no data) — the calibrated matrices and the elasticity-language bridge are the engine, not the libraries.

## Python Libraries (Optional Quantitative Mode)

### Demand and elasticity estimation
- **`statsmodels`** — `OLS` for log-log demand regressions, `IVRegression` (via `linearmodels`) for instrumental variables when price is endogenous.
- **`linearmodels`** — Panel data (FE, RE), 2SLS, GMM. Use when the user has SKU-by-period panels.
- **`scipy.optimize`** — `curve_fit` for nonlinear demand functional forms; `minimize` for indirect-utility-based discrete choice if the user has share data.

### Equilibrium computation
- **`numpy`** + **`scipy.linalg`** — closed-form equilibrium for linear S/D systems.
- **`scipy.optimize.fsolve`** — for nonlinear equilibrium (e.g., constant-elasticity demand `Q = A·P^εd`).
- **`sympy`** — for symbolic comparative statics (when the user wants formulas, not just numbers).

### Risk computation
- **`numpy`** for L × I and L × I × D arrays.
- **`pandas`** for the register dataframe (rows = scenarios, columns = ISO 31000 schema fields).
- **`scipy.stats`** — for Monte Carlo on elasticity inputs to propagate CI through the matrix.

### Visualization
- **`matplotlib`** + **`seaborn`** — heat maps (`sns.heatmap`), supply-demand curve plots with annotated equilibrium points, tornado diagrams for sensitivity.
- The agent should use the colorblind-friendly palette `viridis` or the COSO-aligned green→yellow→amber→red mapping. *Never* render risk colors only — always include the numeric tier in each cell.

## Standards and Frameworks (Always Cite Specifically)

| Standard | When the agent invokes it |
|---|---|
| **ISO 31000:2018** | Risk register schema, treatment vocabulary (Avoid / Reduce / Transfer / Accept) |
| **IEC 31010:2019** | Risk matrix construction (§B.29), scenario analysis (§B.5–B.10), Bow-tie (§B.13) |
| **NIST SP 800-30 Rev. 1** | Qualitative and semi-quantitative scoring tier definitions (Appendix I) |
| **COSO ERM Framework (2017)** | Heat-map norms, risk-appetite vocabulary |
| **AIAG-VDA FMEA Handbook (2019)** | When the user is using L × I × D (Severity × Occurrence × Detection); cite for the FMEA-specific score interpretation |

When the agent says "the score sits in the amber tier," it should follow with "per the COSO ERM heat-map convention as adopted in `context/constraints.md`" or similar — the methodology is never anonymous.

## External Data Services (Reference Only — User Subscribes If They Use Them)

| Service | Purpose |
|---|---|
| **FRED (St. Louis Fed)** | Macro indicators for income elasticity scoring |
| **CME / ICE / LME** | Forward and futures curves; leading-indicator likelihood evidence |
| **USDA WASDE / FAS** | Agricultural supply forecasts |
| **NOAA** | Weather-driven supply shock leading indicators |
| **Numerator / IRI / NielsenIQ** | Consumer panel data for elasticity estimation |
| **Panjiva / ImportGenius** | Trade-flow leading indicators for supply-chain risk |
| **Bloomberg / Refinitiv** | Multi-asset price/volume; pricier alternative to assembling from individual sources |
| **Federal Register / EUR-Lex** | Regulatory pipeline for structural risk |
| **Comtrade (UN)** | Bilateral trade data for cross-border supply analysis |
| **OECD Stat / Eurostat** | International macro/sectoral data |

The agent should never fabricate data citations. If the user doesn't have access to any of the above, the agent uses literature priors (cited) and labels the score "low-evidence."

## Internal Tooling Touchpoints

These are external systems the user may want the workspace's outputs imported into. The agent produces markdown + CSV exports for each:

- **Archer (RSA)** — risk register import via CSV.
- **ServiceNow IRM** — risk register import via REST or CSV.
- **Resolver** — CSV import.
- **Workiva** — text + table export for SOX/ERM workpaper integration.
- **PowerBI / Tableau** — long-format CSV (one row per scenario × period) for dashboards.

When the user mentions a target system, the agent confirms format requirements before generating exports.

## What the Agent Will Not Do With These Tools

- **Will not** call external paid APIs without explicit user setup; the agent suggests but does not execute.
- **Will not** run any code that pulls competitor data from sources not authorized in `context/constraints.md`.
- **Will not** generate "AI-detected" elasticity values not traceable to either user data or a cited prior.
