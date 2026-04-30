# Series Catalog — Real-Time Sources

A reference of the most-used series IDs across FRED/ALFRED, BEA, OECD MEI, and Eurostat. Use this when configuring `context/project.md` during onboarding.

## US — FRED / ALFRED

### GDP and components (quarterly, real, chained)
| Series ID | Description |
|-----------|-------------|
| `GDPC1` | Real Gross Domestic Product |
| `GDP` | Nominal GDP |
| `GDI` | Gross Domestic Income (real) |
| `GDPPLUS` | Aruoba–Diebold–Scotti / BEA blend |
| `PCECC96` | Real PCE |
| `GPDIC1` | Real Gross Private Domestic Investment |
| `GCEC1` | Real Government Consumption + Investment |
| `EXPGSC1` | Real Exports |
| `IMPGSC1` | Real Imports |
| `CBIC1` | Real Change in Private Inventories |

### Monthly indicators (for nowcast panel)
| Series ID | Description |
|-----------|-------------|
| `PAYEMS` | Total Nonfarm Payrolls |
| `UNRATE` | Civilian Unemployment Rate |
| `INDPRO` | Industrial Production Index |
| `RRSFS` | Real Retail and Food Services Sales |
| `HOUST` | Housing Starts |
| `PERMIT` | Building Permits |
| `NAPM` | ISM Manufacturing PMI (composite) |
| `UMCSENT` | UMich Consumer Sentiment |
| `PCEPI` | PCE Price Index |
| `CPIAUCSL` | CPI All Items |
| `IR` | Real Imports of Goods (monthly) |
| `IQ` | Real Exports of Goods (monthly) |

### External nowcast benchmarks (informational only)
| Series ID | Description |
|-----------|-------------|
| `GDPNOW` | Atlanta Fed GDPNow |
| `STLENI` | St. Louis Fed Economic News Index |

## Euro Area — Eurostat SDMX

Dataset `namq_10_gdp` covers quarterly GDP and components. Key dimensions:
- `freq=Q`
- `unit=CLV10_MEUR` (chained linked volumes, 2010 reference, millions of euro) or `CP_MEUR` for current prices
- `s_adj=SCA` (seasonally and calendar-adjusted) or `NSA`
- `na_item=B1GQ` (GDP) plus `P31_S14_S15`, `P5G`, `P3_S13`, `P6`, `P7` for components
- `geo=EA19` for euro area or country code (`DE`, `FR`, `IT`, ...)

Example URL:
```
https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/namq_10_gdp/Q.CLV10_MEUR.SCA.B1GQ.EA19?format=JSON
```

## OECD MEI — SDMX

Quarterly National Accounts (`QNA`) and Main Economic Indicators (`MEI`). Country-quarterly real GDP example:

```
https://stats.oecd.org/SDMX-JSON/data/QNA/USA.B1_GE.LNBQRSA.Q/all
```

Where:
- `LNBQRSA` = Index, seasonally adjusted, 2015 base
- `LNBQR` = Index, NSA
- `B1_GE` = GDP at market prices, output approach

For composite leading indicators (CLIs): dataset `MEI_CLI`.

## UK — ONS API

Base: `https://api.ons.gov.uk/timeseries/`
Real GDP quarter-on-quarter (CVM SA): `IHYR/dataset/QNA`.

## Brazil — IBGE / BCB

IBGE Sidra API for quarterly accounts; Brazilian Central Bank (`BCB`) for monthly activity proxies (IBC-Br).

## Japan — Cabinet Office, BoJ

Cabinet Office QE (Quarterly Estimates) for GDP; BoJ Tankan for survey indicators.

## License Tags (record per series in manifest)

| Source | License |
|--------|---------|
| FRED / ALFRED | "FRED Terms of Use" — public, attribute SLFRB |
| BEA | "US Government Work" — public domain |
| OECD | "OECD Terms" — non-commercial reuse with attribution |
| Eurostat | "Eurostat Reuse" — generally open, attribute |
| ONS UK | "Open Government Licence v3.0" |
| IBGE | "CC BY 4.0" |
| Cabinet Office Japan | "Government of Japan Standard Terms of Use" |

## Vintage Behaviour Notes

- **BEA NIPA:** advance, second, third estimates land at ~T+30, T+60, T+90 days after quarter end. Annual revisions every July; comprehensive revisions ~every 5 years.
- **Eurostat:** preliminary flash at ~T+30, flash at ~T+45, second estimate at ~T+65.
- **OECD MEI:** aggregates national vintages with a 1–2 month lag.
- **ALFRED holds vintages back to 1996 for most US headline series.**

When a comprehensive revision occurs, expect levels to move materially across many quarters; flag prominently in the work-log and run `/audit-revision` against the prior vintage to decompose the impact.
