# Elasticity Reference — Common Values, Sources, Interpretation

A literature-prior reference. The agent uses this when the user has no internal data and needs to populate scenario cards or matrices with defensible numbers.

**Citation discipline.** When the agent uses any value here, it cites the original source in the scenario card. Priors are *priors*, not measurements of the user's specific market.

## 1. Reading the Tables

- All values are **point estimates with typical CIs in brackets** when available.
- "SR" = short-run (≤ 1 year). "LR" = long-run (3–5 years). Values without an SR/LR label are mid-horizon.
- Studies are listed by canonical author/year; full citations live at the bottom of this document.
- *Strongly recommend* re-estimating from the user's data when stakes are non-trivial. Priors get the conversation started, not concluded.

## 2. Own-Price Elasticity of Demand (`εd`)

### 2.1 Food & Agriculture (B2C)

| Category | εd (SR) | εd (LR) | Source |
|---|---|---|---|
| Beef | -0.7 [-0.9, -0.5] | -1.2 | USDA ERS (2022) |
| Pork | -0.7 | -1.0 | USDA ERS (2022) |
| Chicken | -0.5 | -0.8 | USDA ERS (2022) |
| Eggs | -0.3 [-0.4, -0.2] | -0.5 | Andreyeva et al. (2010) |
| Coffee (ground, retail) | -0.4 to -0.7 | -0.8 to -1.2 | Okrent & Alston (2012) |
| Wheat flour (retail) | -0.3 | -0.5 | Andreyeva et al. (2010) |
| Sugar | -0.3 to -0.5 | -0.7 | Andreyeva et al. (2010) |
| Soft drinks | -0.8 to -1.2 | -1.4 | Andreyeva et al. (2010) |

### 2.2 Energy

| Category | εd (SR) | εd (LR) | Source |
|---|---|---|---|
| Gasoline (US retail) | -0.05 to -0.20 | -0.40 to -0.80 | Hughes, Knittel, Sperling (2008); Davis & Kilian (2011) |
| Residential electricity | -0.10 to -0.25 | -0.30 to -0.50 | Espey & Espey (2004) (meta) |
| Natural gas (residential) | -0.10 to -0.30 | -0.50 to -0.80 | EIA (current) |

### 2.3 Telecom & Digital

| Category | εd | Source |
|---|---|---|
| Cable TV | -1.5 to -2.5 | Goolsbee & Petrin (2004) |
| Mobile telephony (developed markets) | -0.5 to -1.0 | Various (ITU summaries) |
| Streaming subscription (consumer SaaS) | -1.0 to -2.5 | Industry analyst syntheses; few peer-reviewed estimates |
| Cloud compute (B2B) | -0.3 to -0.8 | Limited public estimates; firm-specific recommended |

### 2.4 Transportation

| Category | εd (SR) | εd (LR) | Source |
|---|---|---|---|
| Air travel (leisure) | -1.0 to -1.5 | -1.8 | Brons et al. (2002) (meta) |
| Air travel (business) | -0.4 to -0.8 | -0.7 | Brons et al. (2002) |
| Public transit | -0.3 to -0.5 | -0.7 to -0.9 | Litman (TDM Encyclopedia) |

### 2.5 Healthcare

| Category | εd | Source |
|---|---|---|
| Outpatient care | -0.1 to -0.2 | RAND HIE; replications |
| Prescription drugs (branded, with generic substitutes) | -0.3 to -0.6 | Various; insurer-formulary studies |
| Cosmetic / elective procedures | -1.0 to -1.5 | Limited but consistent |

### 2.6 Consumer Durables

| Category | εd | Source |
|---|---|---|
| Automobiles (new) | -0.8 to -1.5 | Berry, Levinsohn, Pakes (1995) |
| Major appliances | -1.0 to -2.0 | Industry estimates |

## 3. Cross-Price Elasticity (`εxy`)

Cross-elasticity is *pairwise* — values depend heavily on the substitute pair. These are typical magnitudes by category; for any specific pair, estimate or look up.

| Pairing | εxy (typical) | Notes |
|---|---|---|
| Same category, same quality tier (e.g., Pepsi/Coke) | 0.5 to 1.5 | Strong substitution |
| Same category, different tier (premium ↔ economy) | 0.3 to 1.0 | Asymmetric: economy → premium weaker than premium → economy under stress |
| Adjacent categories (butter ↔ margarine) | 0.3 to 0.8 | Hausman et al. (1994) |
| Cross-category functional substitute (DVD rental ↔ streaming) | 0.2 to 1.5 | Time-varying as one category emerges |
| Complements (printers ↔ ink, console ↔ games) | -0.5 to -1.5 | Tighter pairs more negative |

**BLP-derived industry estimates** (when share data exists, BLP gives matrices of these per pair; Berry, Levinsohn, Pakes 1995 for autos is the canonical example).

## 4. Income Elasticity of Demand (`εY`)

| Category | εY | Notes |
|---|---|---|
| Food (aggregate) | 0.3 to 0.5 | Necessity |
| Food away from home | 1.0 to 1.5 | Mild luxury |
| Beef vs. chicken | beef higher εY than chicken | Substitution toward beef as income rises |
| Public transit | -0.3 to 0.0 | Often inferior |
| Air travel | 1.5 to 2.5 | Luxury |
| Higher education | 1.0 to 1.5 | Mild luxury |
| Healthcare (aggregate) | 0.2 to 0.6 | Insurance and demographics dominate |
| Luxury goods (handbags, watches) | 2.0 to 4.0 | Highly cyclical |
| Used cars | -0.5 to 0.0 | Inferior in some segments |

## 5. Supply Elasticity (`εs`)

| Category | εs (SR) | εs (LR) | Notes |
|---|---|---|---|
| Crude oil | 0.05 to 0.15 | 0.5 to 1.0 | Drilling lead times |
| Major grains (wheat, corn) | 0.1 to 0.3 | 0.5 to 1.5 | Annual planting cycle limits SR |
| Coffee | ~0.2 SR | 0.5–1.0 LR | Tree maturity 3–5 years |
| Manufacturing (low capacity utilization) | 1.0 to 3.0 | high | Spare capacity makes εs large |
| Manufacturing (high capacity utilization) | 0.1 to 0.5 | 1.0+ | Capacity-constrained, must invest |
| Software / SaaS | very high (often modeled as ∞) | very high | Marginal cost ≈ 0 |
| Real estate (urban) | 0.0 to 0.5 SR | 0.5 to 1.5 LR | Permits and construction lags |

## 6. How to Use These in the Workspace

1. **Pick the closest analog category** to the user's market.
2. **Adjust for horizon** — SR vs. LR is the single biggest source of error.
3. **Use a range, not a midpoint** — the matrix cell will straddle multiple tiers if the prior CI is wide.
4. **Cite the source in the scenario card.** "Andreyeva et al. (2010)" beats "literature consensus."
5. **Re-estimate before high-stakes scoring.** A prior is for triage; a register row that drives a $10M hedging decision deserves an internal estimate or a paid-data prior, not a 2010 textbook value.

## 7. Citations (full)

- Andreyeva, T., Long, M.W., & Brownell, K.D. (2010). *The impact of food prices on consumption: a systematic review of research on the price elasticity of demand for food.* American Journal of Public Health, 100(2), 216–222.
- Berry, S., Levinsohn, J., & Pakes, A. (1995). *Automobile prices in market equilibrium.* Econometrica, 63(4), 841–890.
- Brons, M., Pels, E., Nijkamp, P., & Rietveld, P. (2002). *Price elasticities of demand for passenger air travel: a meta-analysis.* Journal of Air Transport Management, 8(3), 165–175.
- Davis, L.W., & Kilian, L. (2011). *Estimating the effect of a gasoline tax on carbon emissions.* Journal of Applied Econometrics, 26(7), 1187–1214.
- Espey, J.A., & Espey, M. (2004). *Turning on the lights: a meta-analysis of residential electricity demand elasticities.* Journal of Agricultural and Applied Economics, 36(1), 65–81.
- Goolsbee, A., & Petrin, A. (2004). *The consumer gains from direct broadcast satellites and the competition with cable TV.* Econometrica, 72(2), 351–381.
- Hausman, J., Leonard, G., & Zona, J.D. (1994). *Competitive analysis with differentiated products.* Annales d'Économie et de Statistique, 34, 159–180.
- Hughes, J.E., Knittel, C.R., & Sperling, D. (2008). *Evidence of a shift in the short-run price elasticity of gasoline demand.* The Energy Journal, 29(1), 113–134.
- Litman, T. (current). *Transportation elasticities.* Victoria Transport Policy Institute, TDM Encyclopedia.
- Okrent, A.M., & Alston, J.M. (2012). *The demand for disaggregated food-away-from-home and food-at-home products in the United States.* USDA ERR-139.
- USDA Economic Research Service (2022). *Food consumption and demand briefings* (multiple).
