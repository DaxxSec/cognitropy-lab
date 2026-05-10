# /treatment-compare

Mixed-effects model with `time × treatment` for replicated plot trials; the right tool for "did treatment X change the trajectory?"

## Inputs

- Long-format data (CSV/TSV): columns `sample_id, plot, treatment, time, response, [covariates]`.
- Response variable: alpha-diversity index, CLR-transformed taxon, qPCR copy number, or soil-health proxy.
- Covariates of interest (temperature, moisture, pH, EC, total C/N, prior management).
- For differential abundance across many taxa: switch to `MaAsLin2` or `ALDEx2` instead.

## Steps

1. Read `context/workflows.md` "Treatment Comparison (Mixed-Effects)".
2. Sanity-check the data: no missing factor levels, balanced or near-balanced replication, response on the right scale.
3. Choose the model:
   - Continuous response: `lme4::lmer(response ~ time * treatment + covariates + (1|plot))`.
   - Count response: `glmmTMB(response ~ time * treatment + covariates + (1|plot), family=nbinom2)`.
   - Compositional taxa across many ASVs: `MaAsLin2::Maaslin2(...)` with `random_effects="plot"`.
4. Fit; check residuals (`DHARMa::simulateResiduals`).
5. Report:
   - Main effect of treatment.
   - Treatment × time interaction (this is the key test for "treatments diverged over time").
   - Covariate effects.
6. Apply FDR correction (BH) when many taxa are tested in parallel.
7. Plot estimated trajectories per treatment with 95% confidence ribbons (use `ggeffects::ggpredict` or equivalent).

## Output

A markdown file `outputs/treatment-compare-YYYY-MM-DD.md` containing: model formula, sample-size summary by group, main effects table, interaction test, covariate effects, residual diagnostic summary, FDR-adjusted results if applicable, and a textual description of the estimated trajectories.

## Notes

- Random-effect variance near zero → plots are exchangeable; can drop `(1|plot)`.
- Interaction significant but small → report effect size; statistical and biological significance differ.
- Covariates explain most variance → the management story may be smaller than expected; report covariate-controlled trajectories alongside raw.
- For unbalanced designs with crossed random effects (plot × time-block) → `glmmTMB` handles this more gracefully than `lme4`.
- When many taxa are tested (e.g. 200 ASVs) → use `MaAsLin2` directly; running `lmer` per taxon and then FDR-correcting is the slow, less-statistically-coherent way.
