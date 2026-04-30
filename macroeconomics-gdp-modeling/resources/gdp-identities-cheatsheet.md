# GDP Identities Cheatsheet

A compact reference for the three measurement approaches and how their differences propagate through forecasts.

## 1. Expenditure Identity

$$Y = C + I + G + (X - M)$$

| Symbol | Component | Typical US share | FRED ID (real, chained) |
|--------|-----------|------------------|-------------------------|
| $C$ | Personal Consumption Expenditures | ~67% | `PCECC96` |
| $I$ | Gross Private Domestic Investment | ~17% | `GPDIC1` |
| $G$ | Government Consumption + Investment | ~17% | `GCEC1` |
| $X$ | Exports of Goods and Services | ~11% | `EXPGSC1` |
| $M$ | Imports of Goods and Services | ~14% | `IMPGSC1` |
| $Y$ | Real GDP | 100% | `GDPC1` |

Decomposition of investment:
- Nonresidential fixed: structures, equipment, IP products
- Residential fixed: housing
- Change in private inventories (CIPI) — the most volatile, most-revised component

## 2. Production / Value-Added Identity

$$Y = \\sum_i \\text{VA}_i \\quad \\text{where} \\quad \\text{VA}_i = \\text{Output}_i - \\text{Intermediate Inputs}_i$$

By industry, NAICS-aligned. The BEA publishes `IRPD` GDP-by-industry tables on a delayed schedule. Useful for sectoral nowcasting (e.g. healthcare, finance).

## 3. Income Identity (GDI)

$$\\text{GDI} = \\text{COE} + \\text{NOS} + \\text{CFC} + (T_p - S_p)$$

- **COE** — Compensation of Employees (FRED `A4102C1Q027SBEA`)
- **NOS** — Net Operating Surplus
- **CFC** — Consumption of Fixed Capital (depreciation)
- **$T_p - S_p$** — Taxes − Subsidies on production and imports

GDI ≠ GDP in practice. The **statistical discrepancy** (`A032RC1Q027SBEA`) is published by BEA. GDPplus (`GDPPLUS` at FRED) blends the two.

## 4. Real vs. Nominal vs. Chained

- **Nominal:** current prices, current quantities.
- **Real (fixed-base Laspeyres):** quantities at base-year prices. Substitution bias.
- **Chained:** Fisher ideal index of Laspeyres and Paasche, chained quarterly. Modern BEA standard since 1995.

The BEA reports the GDP price index (`GDPCTPI`) and PCE price index (`PCECTPI`) separately. The chain-weighting means real component shares **do not sum to real GDP exactly** away from the base year — the residual is the chain-weighting error and shows up in detailed decompositions.

## 5. Annualised vs. QoQ Conventions

- **US:** headline is annualised QoQ — `((Y_t / Y_{t-1})^4 - 1) * 100`.
- **EU:** headline is non-annualised QoQ — `(Y_t / Y_{t-1} - 1) * 100`.
- **YoY (any):** `(Y_t / Y_{t-4} - 1) * 100`.

The custody manifest must record the convention used for any forecast reported externally.

## 6. Common Component-Level FRED IDs (Real, Chained, US)

| Component | FRED ID |
|-----------|---------|
| Real GDP | `GDPC1` |
| Real PCE | `PCECC96` |
| Real PCE Goods | `PCDGCC96` (durable) / `PCNDC96` (nondurable) |
| Real PCE Services | `PCESVC96` |
| Real Gross Private Investment | `GPDIC1` |
| Real Nonresidential Fixed | `PNFIC1` |
| Real Residential Fixed | `PRFIC1` |
| Change in Private Inventories | `CBIC1` |
| Real Government Consumption + Investment | `GCEC1` |
| Real Exports | `EXPGSC1` |
| Real Imports | `IMPGSC1` |
| Real GDI | `A261RX1Q020SBEA` |
| Statistical Discrepancy | `A032RC1Q027SBEA` |

## 7. Useful Identities for Nowcasting

- **Bridge identity:** quarterly GDP growth as weighted sum of monthly indicator quarterly aggregates.
- **Approximate accounting identity:** changes in component shares roughly track changes in their growth rates weighted by base-period shares.
- **Stock–flow link:** investment level = capital stock change + depreciation; CFC bridges levels and flows.

## 8. Pitfalls

- Mixing SA and NSA in the same regression silently — never. Manifest the SA method per series.
- Mixing real and nominal — never. Manifest `units` and check before regressions.
- Using the latest revised series for backtests of a "real-time" model — never. Always source from sealed vintages.
- Reporting an annualised number in an EU report — convert and label explicitly.
