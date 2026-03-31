# Bayesian MCMC Convergence Checklist

Use this checklist after every MCMC run before trusting posterior results.

## Mandatory Checks

### 1. R-hat (Gelman-Rubin Statistic)
- [ ] R-hat < 1.01 for ALL parameters
- If R-hat > 1.01: chains haven't mixed. Run longer, reparameterize, or use stronger priors.
- ArviZ: `az.summary(trace)` — check `r_hat` column

### 2. Effective Sample Size (ESS)
- [ ] ESS_bulk > 400 for all parameters (sufficient for reliable mean/median)
- [ ] ESS_tail > 400 for all parameters (sufficient for reliable credible intervals)
- If ESS low: increase draws, thin chains, or reparameterize to reduce autocorrelation
- ArviZ: `az.summary(trace)` — check `ess_bulk` and `ess_tail` columns

### 3. Divergences
- [ ] Zero divergent transitions
- If divergences present: increase `target_accept` (try 0.95, 0.99), reparameterize model
- Common cause: tight curvature in posterior (e.g., highly correlated parameters)
- ArviZ: `az.plot_trace(trace, divergences='top')`

### 4. Trace Plots
- [ ] Chains look like "hairy caterpillars" — well-mixed, stationary
- [ ] No trends, drifts, or stuck chains
- [ ] All chains exploring the same region
- ArviZ: `az.plot_trace(trace)`

## Recommended Checks

### 5. Posterior Predictive Check
- [ ] Simulated data from posterior looks like observed data
- If systematic mismatch: model misspecification — revisit likelihood function
- ArviZ: `az.plot_ppc(trace)`

### 6. Prior Sensitivity
- [ ] Results don't change drastically with reasonable alternative priors
- If highly sensitive: you don't have enough data to overcome the prior — report this
- Method: re-run with doubled prior variance, compare posteriors

### 7. Energy Plot (NUTS-specific)
- [ ] Marginal energy and energy transition distributions overlap well
- Poor overlap → inefficient exploration, consider reparameterization
- ArviZ: `az.plot_energy(trace)`

## Quick ArviZ Diagnostic Script
```python
import arviz as az

# After sampling: trace = pm.sample(...)
summary = az.summary(trace)
print(summary[['mean', 'sd', 'hdi_5%', 'hdi_95%', 'ess_bulk', 'ess_tail', 'r_hat']])

# Visual diagnostics
az.plot_trace(trace)
az.plot_energy(trace)
az.plot_ppc(trace)  # requires posterior_predictive in trace
```

## When Convergence Fails — Decision Tree
1. R-hat > 1.05 → Double the number of draws, check if it improves
2. Still failing → Check for multimodality: `az.plot_pair(trace)` — multiple clusters?
3. If multimodal → Model may be non-identifiable. Add constraints or informative priors
4. Divergences > 0 → Increase `target_accept` to 0.95 or 0.99
5. Still diverging → Reparameterize (e.g., non-centered parameterization for hierarchical models)
6. ESS < 100 → Strong autocorrelation. Try thinning or longer chains
7. All else fails → Simplify model. Can you fix some parameters? Reduce dimensionality?
