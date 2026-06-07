# Epidemiological Disease-Spread Modeling — Workflows and Methodology

Step-by-step procedures and decision trees for running tasks in this workspace. The technique throughline is **time-series trend analysis**: every workflow treats the surveillance stream as a series to be cleaned, decomposed, inverted (delay → infection), summarised (Rt, r, phase), projected, and scored.

## Workflow 0: Series intake and triage (always run first)

**Goal:** Know what you're holding before you model it.

### Steps

1. Identify the **stream** (cases / hospitalisations / deaths / ED / positivity / wastewater) and its expected lag and ascertainment behaviour.
2. Identify the **time index**: is the date *onset*, *specimen*, *report*, or *death*? Rt and nowcasting want onset/infection; report-date series need shifting.
3. Record the **data snapshot date** and aggregation grain (daily/weekly; national/regional).
4. Plot the raw series. Eyeball for: weekly periodicity, holiday cliffs, zero-runs, level shifts (definition changes), and the truncated tail.
5. Decide the **count model**: Poisson vs negative-binomial (almost always NB — check variance/mean).

### Decision Points

- If date = report and a delay distribution exists → plan a `/nowcast` (and consider deconvolution to onset before Rt).
- If strong weekly structure → `/decompose-trend` or a 7-day window before visual trend calls.
- If multiple streams available → triangulate; prefer ascertainment-stable streams (hospitalisations, wastewater) for the trend call.

## Workflow 1: Time-varying Rt estimation (Cori / EpiEstim)

**Goal:** Near-real-time read on whether transmission is growing.

### Steps

1. Get incidence on the **right date axis** (onset or infection). If only report dates exist, deconvolve the reporting delay first, or use a method that models it (EpiNow2).
2. **Nowcast the tail** (Workflow 3) so the most recent window isn't biased downward.
3. Specify the **serial/generation interval** (mean, SD, parametric form) from `context/references.md` or estimated from pair data; propagate its uncertainty (`estimate_R` with `si_distr` / `make_config` uncertain SI).
4. Choose the **estimation window** τ (e.g. 7 days): shorter = more responsive, noisier; longer = smoother, lagged. State it.
5. Run EpiEstim (`estimate_R`) or epyestim; obtain Rt with 95% credible intervals per window.
6. **Do not pre-smooth** the input series — let the Bayesian window absorb noise (Gostic et al.).
7. Interpret against 1.0; report the date the CI last excluded 1, and the right-truncation caveat for the final window.

### Decision Points

- If reporting delays are substantial and varying → use **EpiNow2** (joint delay + nowcast + Rt) instead of bare EpiEstim.
- If you need the *cohort* Rt (who-infected-whom, retrospective) → Wallinga-Teunis, accepting right-truncation.

## Workflow 2: Growth rate and doubling time (r ↔ Rt)

**Goal:** Communicate epidemic speed and cross-check Rt.

### Steps

1. Restrict to a window plausibly exponential (early growth or a clean segment).
2. Fit `log(count) ~ time` (Poisson/NB GLM with log link, or log-linear with a robust SE), recover slope **r** and CI.
3. **Doubling time = ln(2)/r** (halving time if r<0).
4. Convert to **Rt** via Euler-Lotka with the generation interval: for gamma(mean μ, shape k), `R = (1 + rμ/k)^k`. Report alongside the renewal-based Rt as a consistency check.

### Decision Points

- If the segment is visibly curving → not exponential; drop r, use Rt + decomposition instead.
- If r CI spans 0 → "no clear growth/decline"; report the slope CI, not a doubling time.

## Workflow 3: Nowcasting the truncated present

**Goal:** Estimate what recent counts will become once reporting completes.

### Steps

1. Build (or import) the **reporting-delay distribution** from the reporting triangle (event date × delay).
2. Choose a method: simple multiplier (inverse-CDF reweighting), generative/Bayesian nowcast (`surveillance::nowcast`, `epinowcast`, EpiNow2), or hierarchical delay model.
3. Apply to the last *k* time points (k ≥ max plausible delay); produce nowcast counts with intervals.
4. Replace/annotate the truncated tail; mark which points are nowcast vs observed in `outputs/`.

### Decision Points

- If the delay distribution is **non-stationary** (changing over the epidemic) → model time-varying delay; a fixed multiplier will mislead.
- If delay data are unavailable → exclude the truncated window from trend calls rather than guess.

## Workflow 4: Trend / seasonal decomposition

**Goal:** Separate secular trend from weekly and seasonal structure.

### Steps

1. Choose period: **7** for daily surveillance (day-of-week), **52/53** for weekly seasonal series.
2. Run **STL** (`stl`, `feasts::STL`, `statsmodels.tsa.STL`); for count data consider STL on `log(count+1)` or an additive-on-sqrt scale.
3. Inspect the three components: trend (the signal), seasonal (subtract), remainder (noise + anomalies).
4. For genuine seasonal pathogens, fit/store the seasonal baseline (basis for Workflow 6 thresholds).

### Decision Points

- If the remainder shows a structured spike → candidate aberration (Workflow 5) or data error.
- If multiple seasonalities (weekly + annual) → MSTL or `prophet` with multiple seasonal terms.

## Workflow 5: Aberration / outbreak detection

**Goal:** Flag whether the current count exceeds an expected baseline.

### Steps

1. Build a **baseline** from historical counts excluding past outbreak periods and accounting for seasonality + trend.
2. Pick an algorithm: **Farrington / `farringtonFlexible`** (seasonal, overdispersion-aware — default for notifiable disease), **EARS C1/C2/C3** (short-baseline, new diseases), or **CUSUM** (sustained small shifts).
3. Set the threshold (e.g. upper bound of the predictive interval) and run prospectively over recent weeks.
4. For each flagged point: record observed vs expected, exceedance, and the alarm score.

### Decision Points

- Short or no history → EARS (uses a 7-day sliding baseline). Long history → Farrington.
- Looking for slow drifts rather than spikes → CUSUM.
- Many strata tested → control false alarms (FDR / raise thresholds).

## Workflow 6: Seasonal baseline / epidemic threshold (e.g. MEM, Serfling)

**Goal:** Define "above-normal" for a seasonal pathogen.

### Steps

1. Assemble ≥3-5 prior seasons of weekly counts/rates.
2. Fit a **Serfling cyclic regression** (sinusoidal + trend) or apply the **Moving Epidemic Method (MEM, `mem` package)** to derive pre-epidemic, intensity, and post-epidemic thresholds.
3. Overlay the current season; mark threshold crossings (epidemic onset/offset, intensity level).

## Workflow 7: Compartmental model fitting

**Goal:** Recover mechanistic parameters (R0, latent/infectious periods) from a curve.

### Steps

1. Choose structure (SEIR default; add D if fitting deaths) and the **observation model** (NB on incidence with reporting fraction + delay).
2. Pick inference: least-squares / MLE (`optim`) for speed; **particle filter / pMCMC** (`pomp`) or HMC (Stan/numpyro) for stochastic dynamics + full uncertainty.
3. Fit to the **infection-date** curve (deconvolve first) over the growth-to-peak window.
4. Recover β, γ, σ → derive R0 = β/γ, latent and infectious periods; report posteriors/CIs.
5. Run posterior-predictive check: simulate and overlay on data.

### Decision Points

- Identifiability problems (flat likelihood ridges) → fix one parameter from `context/references.md` priors; report what was fixed.
- Stochastic small-number dynamics (early outbreak) → particle filter, not deterministic ODE.

## Workflow 8: Short-term forecasting + backtesting

**Goal:** Project 1-4 weeks ahead and know if the projection is trustworthy.

### Steps

1. Generate forecasts from ≥2 methods: **renewal/Rt projection** (EpiNow2/`projections`), **statistical** (ARIMA/ETS/Prophet), optionally **mechanistic**.
2. Produce **quantile/probabilistic** forecasts (e.g. 23 quantiles, hub format), not point estimates.
3. Build an **ensemble** (median or weighted) — typically the most skilful.
4. **Backtest** on held-out history: refit at past time origins, forecast forward, compare to realised.
5. Score with `/score-forecast`: **WIS**, interval **coverage** (50%/95%), **CRPS**; decompose WIS into over/under/dispersion.
6. Choose / weight methods by realised skill; record in `outputs/`.

### Decision Points

- 95% coverage well below 95% → intervals too narrow (overdispersion under-modelled); widen / use NB.
- One method dominates WIS across origins → up-weight it, but keep the ensemble for robustness.

## Methodology Phases — epidemic stage read (`/wave-phase`)

### Phase 1 — Introduction / sporadic
Low counts, high stochasticity. Aberration detection (Workflow 5) over trend estimation; Rt unstable.

### Phase 2 — Exponential growth
r > 0, Rt > 1 with CI excluding 1. Growth rate + doubling time communicate well; fit compartmental on this window.

### Phase 3 — Peak / plateau
Rt → 1; growth rate → 0. Change-point near the inflection. Beware: a *nowcast-corrected* plateau, not a raw-tail dip.

### Phase 4 — Decline
Rt < 1, halving time positive. Watch for resurgence (Rt creeping back to 1) and reporting artifacts mimicking decline.

### Phase 5 — Endemic / inter-wave
Counts settle to a seasonal baseline; switch to Workflow 6 thresholds and routine aberration detection.
