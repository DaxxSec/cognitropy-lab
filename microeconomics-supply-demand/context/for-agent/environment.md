# Environment — Data Sources, File Conventions, Tooling

## Expected Data Sources

The agent should ask the user which of these are available; the answers go into `context/project.md`.

### Internal (firm)

- **Sales transactions** — typically a database export or CSV with at minimum: `date`, `sku`, `units_sold`, `unit_price`, `discount_amount`, `customer_segment`. Rolled up to the granularity needed (daily / weekly / monthly).
- **Cost of goods** — input cost time series, by input. Critical for any supply-side scoring.
- **Promotional history** — paired with sales; the discount/lift relationship is the cleanest source of own-price elasticity.
- **Inventory levels** — proxy for supply elasticity in the short run.
- **Customer panel data** — if the firm has a panel (loyalty program, account-level), enables segment-level elasticity estimation.

### External (commercial / public)

- **Commodity futures and forward curves** — CME, ICE, LME. Used as leading indicator for likelihood scoring (`/score-supply-shock`).
- **Macro indicators** — FRED (CPI, PPI, household income, consumer sentiment), Eurostat, OECD. Income elasticity scoring.
- **Census / population data** — for demand-side N changes.
- **Trade and shipping data** — Panjiva, ImportGenius, Bill of Lading filings; supply-disruption leading indicator.
- **Competitor pricing** — scrapes, Numerator/IRI panel data, public price lists. Cross-elasticity scoring.
- **Regulatory pipelines** — Federal Register, EUR-Lex, agency dockets. Structural risk scoring.
- **Weather and crop reports** — USDA WASDE for ag; NOAA for weather-driven supply shocks.

### Literature priors (when no data exists)

`resources/elasticity-reference.md` aggregates published elasticity estimates by category (ag, energy, healthcare, telecom, consumer durables, consumer staples, services). Cite the specific source when using a prior.

## File Conventions

The workspace uses these directories with the following content:

| Path | Purpose | Naming |
|---|---|---|
| `outputs/supply-<slug>-<date>.md` | Supply-shock scenario cards | `supply-brazil-drought-2026-04-27.md` |
| `outputs/demand-<slug>-<date>.md` | Demand-shock scenario cards | `demand-recession-mild-2026-04-27.md` |
| `outputs/stress-<slug>-<date>.md` | Equilibrium stress tests | `stress-tariff-15pct-2026-04-27.md` |
| `outputs/elasticity-matrix-<date>.md` + `.png` + `.csv` | 2D elasticity matrices | `elasticity-matrix-2026-04-27.{md,png,csv}` |
| `outputs/cross-elasticity-<date>.{md,png,csv}` | Cross-elasticity heat maps | as above |
| `outputs/risk-register-<date>.md` | Consolidated registers | `risk-register-2026-04-27.md` |
| `planning/risk-register.md` | Living register (always-current) | single file, scenario rows appended |
| `planning/plan.md` | Active assessment plan | single file |
| `work-log/<YYYY-MM-DD>.md` | Daily session log | one per day |

When a file is generated, the agent always notes the path in chat and writes the date stamp into the filename. *Never* overwrite an old scenario card; create a new one and let history accumulate.

## Slug Conventions

- Lowercase, kebab-case.
- Descriptive over generic: `brazil-drought` not `supply-shock-1`.
- Include the year if reusing a recurring scenario name: `recession-mild-2026`.

## Calibration File Conventions

The calibrated likelihood, impact, and (optional) detectability scales live in `context/constraints.md` — never in scenario cards. Scenario cards reference the scale in `constraints.md`; if the scale changes, the agent re-scores affected scenarios on next invocation rather than silently letting old scores point to a redefined anchor.

## Python Environment (Optional)

For workflows that benefit from quantitative computation:

```
python -m venv .venv
source .venv/bin/activate
pip install numpy pandas scipy statsmodels matplotlib seaborn linearmodels
```

The agent should use these only when the user has provided data; otherwise it works in qualitative/literature-prior mode.

## OS / Shell Notes

- The agent assumes a POSIX shell (macOS, Linux, WSL).
- Plot rendering uses matplotlib's `Agg` backend (writes PNG without a display).
- File I/O uses UTF-8 throughout.

## Privacy and Data Handling

- The agent should never write raw customer-identifying data into scenario cards or the register. Aggregated counts and segment labels only.
- If the user supplies competitor pricing data, the agent confirms it was obtained through legitimate channels (public scrapes, paid panel) before using it. No tortious-interference data, no leaked internals.
