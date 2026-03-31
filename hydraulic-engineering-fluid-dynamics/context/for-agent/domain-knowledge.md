# Domain Knowledge: Hydraulic Engineering + Bayesian Methods

## Fundamental Equations

### Open Channel Flow
- **Manning's Equation**: Q = (1/n) × A × R^(2/3) × S^(1/2)
  - Q = discharge (m³/s), n = Manning's roughness coefficient, A = cross-sectional area (m²)
  - R = hydraulic radius = A/P (P = wetted perimeter), S = channel slope (m/m)
  - Key uncertainty: Manning's n varies with flow depth, vegetation state, sediment transport

### Pressurized Pipe Flow
- **Darcy-Weisbach**: h_f = f × (L/D) × (V²/2g)
  - f = friction factor (from Moody diagram or Colebrook-White), L = pipe length, D = diameter
- **Hazen-Williams**: V = k × C × R^0.63 × S^0.54
  - C = roughness coefficient (degrades with age: new CI = 130, 50-year CI ≈ 80-100)

### Energy & Momentum
- **Bernoulli Equation**: z₁ + p₁/γ + V₁²/2g = z₂ + p₂/γ + V₂²/2g + h_L
- **Momentum Equation**: ΣF = ρQ(V₂ - V₁) — used for hydraulic jumps, forces on bends

### Flood Frequency
- **Log-Pearson Type III (LP3)**: Standard USGS method (Bulletin 17C)
  - log(Q_T) = X̄ + K_T × s, where K_T depends on skew and return period T
- **Generalized Extreme Value (GEV)**: Flexible 3-parameter distribution for annual maxima
  - Parameters: location (μ), scale (σ), shape (ξ) — ξ controls tail behavior

## Bayesian Methods for Hydraulics

### Why Bayesian?
Traditional frequentist methods give point estimates and confidence intervals based on repeated sampling assumptions. Bayesian methods instead produce **posterior distributions** — full probability distributions over parameters given observed data and prior knowledge. This is more natural for engineering: "What's the probability Manning's n is between 0.03 and 0.05 given our field measurements?" rather than "If we repeated this experiment infinitely..."

### Bayes' Theorem Applied
P(θ|data) ∝ P(data|θ) × P(θ)
- **P(θ)** = Prior: Engineering judgment, literature values, manufacturer specs
- **P(data|θ)** = Likelihood: How well the hydraulic model predicts observed data for parameter values θ
- **P(θ|data)** = Posterior: Updated parameter distribution incorporating both prior knowledge and observations

### Key Applications

#### 1. Parameter Calibration
- **Problem**: Manning's n for a natural channel — textbook says 0.03-0.05, but what value fits THIS reach?
- **Prior**: Uniform(0.025, 0.065) or Informational based on channel classification
- **Likelihood**: Run HEC-RAS for candidate n values, compare predicted stage to measured stage
- **Posterior**: Distribution of n values consistent with both prior knowledge and field data
- **Tool**: PyMC with NUTS sampler, ArviZ for diagnostics

#### 2. Flood Frequency with Bayesian GEV
- **Problem**: 40-year gauge record — what's the 500-year flood with honest uncertainty?
- **Prior**: Weakly informative priors on GEV parameters from regional regression
- **Likelihood**: GEV density evaluated at observed annual maxima
- **Posterior**: Joint distribution of (μ, σ, ξ), from which any return-period quantile has a credible interval
- **Advantage**: Naturally handles short records, regional information, and non-stationarity (time-varying μ)

#### 3. Infrastructure Reliability
- **Problem**: What's the probability that pipe segment X surcharges during a 10-year storm?
- **Method**: Monte Carlo — sample rainfall, runoff coefficients, pipe roughness from their distributions, run hydraulic model, count exceedances
- **Output**: P(surcharge) with uncertainty, not just pass/fail against a single design storm

#### 4. Bayesian Networks for Risk
- **Structure**: Directed acyclic graph linking condition → capacity → loading → consequence
- **Use case**: Dam safety portfolio risk ranking — combine dam condition scores, spillway capacity uncertainty, PMF estimates, and downstream population into a single risk metric with uncertainty

### Convergence Diagnostics
Never trust MCMC output without checking:
- **R-hat < 1.01**: Chains have mixed (Gelman-Rubin statistic)
- **ESS > 400**: Effective sample size sufficient for reliable posterior summaries
- **Trace plots**: No trends, good mixing, stationarity after warmup
- **Divergences = 0**: No numerical issues (reparameterize if needed)

## Units and Standards
- SI preferred for calculations (m, m³/s, Pa), with US customary conversions noted
- ASCE 7 for structural loading on hydraulic structures
- FEMA P-259 and Bulletin 17C for flood frequency analysis
- AWWA M14 for backflow prevention, M32 for distribution network modeling
- AASHTO Drainage Manual for highway hydraulics
