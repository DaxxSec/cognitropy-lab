# Project Context

> Populated by `/onboard`. Until then this stub describes the default project shape so the agent has something to read on first run.

## Default Configuration (override during onboarding)

- **Jurisdiction:** United States
- **Primary target series:** `GDPC1` (Real Gross Domestic Product, chained 2017 dollars, quarterly, BEA via FRED)
- **Component panel (quarterly):** `PCECC96`, `GPDIC1`, `GCEC1`, `EXPGSC1`, `IMPGSC1`
- **Indicator panel (monthly, for nowcast):**
  - Labour: `PAYEMS`, `AHETPI`, `AWHAETP`
  - Activity: `INDPRO`, `RRSFS`, `HOUST`, `PERMIT`
  - Surveys: `NAPM` (ISM), `UMCSENT`
  - Trade: `IR`, `IQ` (BEA monthly trade)
- **Modeling approach:** dual-track — DFM nowcast for h=0; small BVAR(4) with Minnesota prior for h=1..4.
- **Forecast horizons:** h=0 (nowcast), h=1..4 quarters ahead.
- **Vintage retention:** indefinite (append-only). Public publication minimum: 7 years.
- **Publication regime:** internal research note + signed release bundle for any external publication.

## Key Decisions to Lock During Onboarding

1. Country/region (US default; eurozone uses Eurostat SDMX flow `namq_10_gdp`).
2. Whether to ingest seasonally-adjusted-only or both SA and NSA series (NSA enables custom seasonal adjustment audit).
3. Custody granularity — per-series manifests or per-day rollup. Per-day is the default and is what the commands assume.
4. Which model class is "the" published forecast — only one model is the headline; others are research/parallel.
5. Embargo handling — any series under press embargo at retrieval time is sealed but flagged `embargoed_until: <timestamp>` in the manifest; release commands refuse to bundle embargoed series before that timestamp.

## Out of Scope (by default — re-scope only with explicit user opt-in)

- High-frequency (daily) GDP indicators like the Brave-Butters-Kelley index.
- Subnational GDP (state, MSA, county).
- Real-time monetary or fiscal policy reaction rules — this workspace forecasts GDP, it does not optimise policy.
- Cross-country panel cointegration models — single-jurisdiction by default.
