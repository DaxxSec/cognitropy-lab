# Soil Microbiome — Workflows and Methodology

Step-by-step procedures the agent uses for longitudinal monitoring, all framed through the **time-series trend analysis** lens that this workspace's `technique` calls for.

## Workflow 1: Designing or Auditing a Sampling Programme

**Goal:** Lock in replication, cadence, depth, compositing, and storage *before* the first sample is collected — the only inexpensive moment in microbiome work.

### Steps

1. State the question. "Did treatment X shift the microbiome?" needs different replication than "Is soil health trending up?"
2. Pick replication: minimum 3 plots per treatment; prefer 4-6 for mixed-effects-model power.
3. Pick cadence by question class: seasonal cycle = monthly; disturbance recovery = dense early (week 1, 2, 4) tapering; long-term trend = quarterly to annually.
4. Pick depth strata: at minimum 0-10 cm vs 10-30 cm. Subsoil (>30 cm) only when subsoil microbiome matters to the question.
5. Specify compositing: 5-10 cores per plot, mixed in the field, subsampled — variance reduction without sample-count blowup.
6. Specify storage: flash-freeze in liquid N or -80°C; in the field, dry ice minimum. Anything warmer biases the result.
7. Specify covariate capture per visit: temperature, moisture, pH, EC, total C/N, prior management. Without covariates, time-series trends are uninterpretable.
8. Specify sequencing pipeline up front: primer set, kit, denoising tool (DADA2 / Deblur), reference DB version. Lock these for the duration of the study; switching mid-study creates batch effects that look like biology.

### Decision Points

- If treatments are confounded with time (e.g. treated plots all sampled later in the day) → re-randomise sampling order.
- If cadence is constrained by budget → favour denser early sampling for disturbance studies; favour spread-out sampling for trend studies.
- If primer set is being chosen → 515F/806R (16S V4) is the EMP standard; ITS1F/ITS2 for fungi. Stick to one per study.

## Workflow 2: Compositional Normalisation (the prerequisite for everything else)

**Goal:** Convert raw relative-abundance counts into a representation that supports linear modelling, trend tests, and distance calculations without the compositionality trap.

### Steps

1. Filter low-prevalence taxa: typical threshold is "present in ≥10% of samples at ≥0.01% relative abundance." Justify the threshold; record it.
2. Add a pseudo-count to handle structural zeros (typical: 0.5 or imputation via `zCompositions`).
3. Apply CLR (centered log-ratio) for general-purpose linear modelling. Apply ILR (isometric log-ratio) when balances between known taxonomic groups matter.
4. As a robustness check (not a primary fix), rarefy to even depth — verify trends survive both transformations.
5. Where possible, anchor compositional data to absolute counts: qPCR of total 16S, flow cytometry, spike-ins (e.g. *Sketococcus*).
6. Document every step in `outputs/normalisation-YYYY-MM-DD.md`.

### Decision Points

- If a taxon has structural zeros in some samples → check whether zero is biological absence vs. detection limit; treatment matters.
- If absolute counts disagree dramatically with relative trends → trust the absolute. The relative shift may be entirely a denominator effect.
- If rarefaction loses >30% of samples at the chosen depth → re-evaluate sequencing depth; rarefaction depth must respect the lowest sample.

## Workflow 3: Monotonic Trend Testing (Mann-Kendall + Theil-Sen)

**Goal:** Test whether a univariate time series (alpha diversity, qPCR copy number, CLR-transformed taxon abundance) shows a monotonic trend, with a magnitude estimate.

### Steps

1. Verify the series is on the right scale: CLR-transformed for taxa, log-transformed for qPCR, untransformed for diversity indices.
2. Check for ties and seasonality. Heavy ties → use exact Kendall variance. Annual seasonality → use **Seasonal Mann-Kendall**; sub-seasonal autocorrelation → use **Block-Bootstrap MK**.
3. Run Mann-Kendall: report Kendall's tau, S statistic, p-value, and N.
4. Run Theil-Sen for slope: median pairwise slope, plus 95% bootstrap CI on the slope.
5. Apply FDR correction (Benjamini-Hochberg) when testing many taxa simultaneously.
6. Report direction (increasing / decreasing / no trend), magnitude per unit time, and significance after FDR.

### Decision Points

- If p > 0.05 with a small N → "absence of evidence not evidence of absence"; report the CI on the slope, not just the p-value.
- If the slope is significant but the magnitude is biologically trivial → say so explicitly. Statistical significance ≠ agronomic significance.
- If the trend is non-monotonic (e.g. unimodal) → MK will miss it; switch to STL decomposition or change-point detection.

## Workflow 4: Seasonal Decomposition (STL)

**Goal:** Separate the trend component from the seasonal cycle and remainder so that trend tests downstream are not confounded by seasonality.

### Steps

1. Verify the series has full seasonal coverage (≥2 full cycles for STL to estimate the seasonal component reliably).
2. Interpolate small gaps; for larger gaps, prefer state-space (Kalman-smoothed) decomposition over interpolation.
3. Run STL: `stl(series, s.window=<period>, robust=TRUE)`. Period = 12 for monthly, 4 for seasonal.
4. Plot trend, seasonal, remainder separately; eyeball before tests.
5. Apply trend tests (Mann-Kendall) to the **trend component**, not the raw series.
6. Apply autocorrelation diagnostics to the remainder; significant autocorrelation = the seasonal model is wrong.

### Decision Points

- If the seasonal component is small relative to the trend → STL was overkill; apply MK to the raw series.
- If the remainder shows clear structure (autocorrelation, conditional variance) → an ARIMA / state-space model fits better than STL alone.
- If the seasonal pattern is not annual (e.g. crop-rotation cycle) → set the period to the rotation length; default monthly will mislead.

## Workflow 5: Change-Point Detection on Community Distance

**Goal:** Detect when the community shifted — not which taxa shifted — using compositional distance from a baseline window.

### Steps

1. Compute Aitchison distance (or weighted UniFrac, or Bray-Curtis with caveats) from each sample to the centroid of a defined baseline window.
2. Plot distance over time.
3. Run PELT (`changepoint` in R or `ruptures.Pelt` in Python) with a penalty calibrated by BIC or by elbow on a penalty sweep.
4. For streaming sensor-based companion data (CO₂ flux, EC), run Bayesian Online Change-Point Detection in parallel; cross-check.
5. Annotate change points against the management timeline (treatments, weather events, harvests).
6. Report each detected change point with: date, magnitude (Δ in distance), 95% CI on the timing, and the candidate cause from the timeline overlay.

### Decision Points

- If many change points are detected → penalty is too low; tighten it.
- If a change point coincides exactly with a sequencing-batch boundary → suspect batch effect; re-analyse with batch correction (`ComBat`, `MMUPHin`).
- If no change points are detected but treatment is "obviously" different → the metric may be insensitive; try alpha-diversity series or specific functional-gene qPCR.

## Workflow 6: Disturbance Recovery Quantification

**Goal:** Quantify the recovery trajectory after a defined disturbance event.

### Steps

1. Define pre-disturbance baseline window (≥3 samples before the event).
2. Compute Aitchison-distance-from-baseline at each post-disturbance time point.
3. Fit a recovery curve (exponential decay or saturating exponential).
4. Report: time-to-X% recovery (typical X = 75% or 90%), asymptote (does the community fully recover or stabilise at a new state?), and confidence intervals on both.
5. Compare across treatments / sites: parallel recovery curves with shared asymptote vs. divergent trajectories.

### Decision Points

- If the curve doesn't saturate → sampling stopped too early; either extend or fit a linear segment with caveats.
- If the asymptote ≠ baseline → the system has shifted to a new stable state ("regime shift"); quantify the shift, don't call it incomplete recovery.
- If recovery is faster than the sampling cadence → sample more densely; week 1, 2, 4 minimum for biology-fast disturbances (drought rewetting, fumigation lift).

## Workflow 7: Treatment Comparison (Mixed-Effects)

**Goal:** Test for treatment effects on a longitudinal trajectory while accounting for plot-level random variation.

### Steps

1. Format data: long format, columns `sample_id, plot, treatment, time, response (CLR-transformed taxa or diversity index), covariates`.
2. Fit a mixed-effects model: `response ~ time * treatment + covariates + (1|plot)` using `lme4::lmer` or `glmmTMB`.
3. For compositional differential abundance: use `MaAsLin2` with random-effect support, or `ALDEx2::aldex.glm` with covariates.
4. Report main effect of treatment, treatment × time interaction (the key test for "treatments diverged over time"), and covariate effects.
5. Apply FDR control across all taxa.
6. Plot estimated trajectories per treatment with confidence ribbons.

### Decision Points

- If random-effect variance is near zero → plots are essentially exchangeable; can drop the random effect.
- If treatment × time interaction is significant but the magnitude is small → report effect size, not just the p-value.
- If covariates explain most of the variance → the management story may be smaller than expected; report covariate-controlled trajectories alongside raw.
