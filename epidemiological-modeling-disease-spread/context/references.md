# Epidemiological Disease-Spread Modeling — Reference Tables

Lookup data the agent reaches for during tasks. Compact by design — defer to the cited primary sources for authoritative values. **All interval/R0 figures are approximate published central estimates; they vary by setting, variant, and study — confirm against a current source and propagate uncertainty.**

## Serial interval, generation interval & R0 by pathogen (starting values)

| Pathogen | Serial interval (mean, days) | R0 (typical range) | Notes |
|----------|------------------------------|--------------------|-------|
| Influenza (seasonal) | ~2.6–3.6 | 1.2–1.4 | Short SI → responsive Rt; strong winter seasonality |
| SARS-CoV-2 (ancestral) | ~4.5–5.2 | 2.5–3.5 | Pre-symptomatic transmission → SI can be < incubation |
| SARS-CoV-2 (Omicron) | ~2.8–3.5 | higher effective | Shorter SI than ancestral |
| RSV | ~7–8 | ~3 | Winter seasonal, paediatric burden |
| Measles | ~11–12 | 12–18 | Very high R0; herd-immunity threshold ~92–95% |
| Mpox (clade IIb, 2022) | ~7–10 | 1.1–1.5 | Network-dependent in MSM populations |
| Ebola (EVD) | ~15 | 1.5–2.5 | Long SI; deaths a key stream |
| MERS-CoV | ~7–8 | < 1 (0.5–0.9) | Sub-critical with superspreading |
| Smallpox | ~17–22 | 5–7 | Historical; long generation |
| Norovirus | ~3–4 | ~2 | Fast, explosive point-source outbreaks |
| Pertussis | ~22–28 | 12–17 | Long SI; waning immunity |
| Mumps / Rubella | ~18 / ~18 | 10–12 / 6–7 | Vaccine-preventable, seasonal |

Discretise continuous intervals to the data's time step (`epitrix::gamma_mucv2shapescale` + `distcrete`, or `epyestim` discretisation). Gamma is the usual parametric form.

## r ↔ R conversion cheat-sheet

- **Doubling time** `Td = ln(2)/r`; **halving time** `Th = ln(2)/|r|` when r<0.
- **Euler-Lotka:** `1/R = ∫ e^{−r a} g(a) da` (g = generation-interval pdf).
- **Gamma generation interval** (mean μ, shape k, so SD = μ/√k): `R = (1 + r μ / k)^k`.
- **Herd-immunity threshold:** `1 − 1/R0`. **Final epidemic size:** `R∞ = 1 − e^{−R0 R∞}` (solve implicitly).
- Source: Wallinga & Lipsitch 2007, *Proc. R. Soc. B* (https://doi.org/10.1098/rspb.2006.3754).

## R / Python tooling

| Tool | Lang | Role |
|------|------|------|
| `EpiEstim` | R | Instantaneous Rt (Cori method) — default for `/estimate-rt` |
| `EpiNow2` | R | Joint reporting-delay + nowcast + Rt + forecast (renewal) |
| `epinowcast` | R | Bayesian nowcasting of right-truncated counts |
| `surveillance` | R | Farrington/`farringtonFlexible`, EARS, `hhh4`, `nowcast`, `boda` |
| `incidence2` | R | Epicurve construction from line lists |
| `R0` / `EpiLPS` | R | R0/Rt via EG/ML / Laplacian P-splines |
| `projections` | R | Branching-process short-term projection |
| `mem` | R | Moving Epidemic Method seasonal thresholds |
| `forecast` / `fable` / `feasts` | R | ARIMA, ETS, STL decomposition |
| `pomp` | R | Particle filter / pMCMC for stochastic compartmental fits |
| `scoringutils` | R | WIS, interval coverage, CRPS — for `/score-forecast` |
| `epitrix`, `distcrete` | R | Interval discretisation helpers |
| `epyestim` | Py | Rt estimation (Cori) |
| `statsmodels` (`tsa.STL`, ARIMA) | Py | Decomposition, statistical forecasting |
| `numpyro` / `PyMC` / `cmdstanpy` | Py | Bayesian compartmental inference |
| `EoN` | Py | Epidemics on networks (spatial/contact — hand-off) |
| `epiweeks` / `prophet` | Py | MMWR weeks; multi-seasonal forecasting |

## Surveillance systems & data sources

- **WHO FluNet / FluID** — global influenza virological + syndromic — https://www.who.int/tools/flunet
- **US CDC FluView / ILINet / RESP-NET / NREVSS** — https://www.cdc.gov/fluview
- **US CDC NNDSS** — notifiable disease weekly tables (Farrington baseline source)
- **US CDC NWSS** (wastewater) / **WastewaterSCAN** — ascertainment-free leading signal
- **ECDC ERVISS / TESSy** — European respiratory virus surveillance — https://erviss.org
- **Our World in Data** — curated cross-country epidemic series — https://ourworldindata.org
- **ProMED / HealthMap** — event-based / early-warning
- **GISAID / Nextstrain** — genomic context for variant-driven trend shifts

## Forecast hubs (format + truth data)

- **US COVID-19 Forecast Hub** (Reich Lab) — https://covid19forecasthub.org
- **US CDC FluSight** — seasonal influenza hospitalisation forecasts
- **European Respicast / COVID-19 Forecast Hub** — https://respicast.ecdc.europa.eu
- **hubverse** — standard hub data model + `hubUtils`/`scoringutils` tooling — https://hubverse.io

## Key methods papers

- **Cori et al. 2013**, *Estimating Time-Varying Reproduction Numbers* (EpiEstim) — https://doi.org/10.1093/aje/kwt133
- **Wallinga & Teunis 2004**, cohort Rt — https://doi.org/10.1093/aje/kwh255
- **Gostic et al. 2020**, *Practical considerations for measuring Rt* — https://doi.org/10.1371/journal.pcbi.1008409
- **Abbott et al. 2020**, EpiNow2 — https://doi.org/10.12688/wellcomeopenres.16006.2
- **Cleveland et al. 1990**, STL — https://www.wessa.net/download/stl.pdf
- **Farrington et al. 1996**, outbreak detection — https://doi.org/10.2307/2983331
- **Held, Höhle & Hofmann 2005**, `hhh4` endemic-epidemic — https://doi.org/10.1191/1471082X05st098oa
- **Bracher et al. 2021**, proper scoring of epidemic forecasts (WIS) — https://doi.org/10.1371/journal.pcbi.1008618
- **Cramer et al. 2022**, ensemble forecast evaluation — https://doi.org/10.1073/pnas.2113561119

## MMWR / epiweek convention

Surveillance weeks follow the **MMWR** standard (week starts Sunday; week 1 = first week with ≥4 days in the new year). Use `epiweeks` (Py) / `MMWRweek` (R); never align weekly series by naive calendar week.
