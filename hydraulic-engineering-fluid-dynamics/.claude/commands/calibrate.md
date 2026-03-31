# Calibrate — Bayesian Parameter Calibration

Fit hydraulic model parameters to field observations using Bayesian MCMC inference. Produces posterior distributions that capture both parameter uncertainty and measurement error.

## Required Inputs
1. **Parameters to calibrate** — List with physical bounds (e.g., Manning's n ∈ [0.01, 0.15])
2. **Hydraulic model** — Description of the model relating parameters to predictions (Manning's, HEC-RAS, EPANET, custom)
3. **Field observations** — Measured values with estimated measurement uncertainty
   - e.g., stage readings ±0.05 ft, discharge measurements ±10%
4. **Prior information** — What you know before seeing data (textbook ranges, manufacturer specs, experience)

## Analysis Steps
1. Define parameter space and physical constraints
2. Construct prior distributions:
   - Uniform for poorly known parameters (within physical bounds)
   - Normal/log-normal for well-characterized parameters with prior mean and spread
3. Build likelihood function:
   - Wrap hydraulic model as Python callable: f(parameters) → predicted observations
   - Define residual model: observed - predicted, accounting for measurement error
   - Typically Gaussian likelihood with known or estimated observation error
4. Run PyMC NUTS sampler: 4 chains × 2000 draws (1000 warmup)
5. Convergence diagnostics: R-hat, ESS, divergences, trace plots
6. Posterior analysis:
   - Marginal distributions for each parameter
   - Joint distributions and correlation structure
   - Identifiability assessment (are parameters well-constrained?)
7. Posterior predictive check: simulate data from posterior, compare to observations
8. Export calibrated parameter posteriors for use in subsequent analyses

## Output Artifacts
- `outputs/calibration/posterior_summary.csv` — Parameter statistics (mean, median, HDI)
- `outputs/calibration/trace_plots.png` — MCMC chain diagnostics
- `outputs/calibration/pair_plot.png` — Joint posterior distributions showing correlations
- `outputs/calibration/ppc_plot.png` — Posterior predictive check
- `outputs/calibration/calibration_report.md` — Methodology and results narrative

## Usage
```
/calibrate
```
Describe your model, parameters, and observations when prompted.
