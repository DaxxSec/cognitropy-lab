# Analyze Flow — Bayesian Hydraulic Flow Analysis

Run a hydraulic flow analysis with Bayesian uncertainty quantification on roughness and loss parameters.

## Required Inputs
Provide or point me to:
1. **Channel/pipe geometry** — Cross-section dimensions, slope, material, age
2. **Observed flow data** — Stage-discharge pairs, flow monitoring records, or design flows
3. **Flow regime** — Open channel (uniform/GVF), pressurized, or mixed

## Analysis Steps
1. Parse and validate input geometry and flow data
2. Select appropriate flow equation (Manning's, Darcy-Weisbach, Hazen-Williams)
3. Define prior distributions for uncertain parameters:
   - Manning's n: based on channel classification + user judgment
   - Loss coefficients: from fitting guides or manufacturer data
4. Build PyMC model with hydraulic equation as likelihood
5. Run MCMC: 4 chains × 2000 draws (1000 warmup), NUTS sampler
6. Check convergence: R-hat < 1.01, ESS > 400, zero divergences
7. Report posterior parameter summaries with 90% HDI
8. Generate predictive flow curves with uncertainty bands
9. Save all outputs to `outputs/flow-analysis/`

## Output Artifacts
- `outputs/flow-analysis/posterior_summary.csv` — Parameter statistics
- `outputs/flow-analysis/trace_plots.png` — MCMC diagnostics
- `outputs/flow-analysis/rating_curve.png` — Flow prediction with credible intervals
- `outputs/flow-analysis/analysis_report.md` — Narrative summary

## Usage
```
/analyze-flow
```
Then provide your geometry and data when prompted, or reference files in `resources/`.
