# Workflows

## Workflow 1: Bayesian Flow Analysis (`/analyze-flow`)

### Inputs Required
- Channel or pipe geometry (cross-section, slope, material)
- Observed flow data (stage-discharge pairs, flow monitoring records)
- Prior information on roughness/loss coefficients

### Steps
1. **Data ingestion** — Parse geometry and flow data, check units, identify outliers
2. **Prior specification** — Set prior distributions for uncertain parameters based on:
   - Channel type lookup tables (natural, lined, pipe material/age)
   - User-provided expert judgment
   - Regional studies or manufacturer data
3. **Model setup** — Define the hydraulic model (Manning's/Darcy-Weisbach) as the likelihood function
4. **MCMC sampling** — Run PyMC NUTS sampler with 4 chains × 2000 draws (1000 warmup)
5. **Convergence check** — Verify R-hat < 1.01, ESS > 400, zero divergences
6. **Posterior analysis** — Report parameter posterior summaries (mean, median, 90% HDI)
7. **Predictive simulation** — Generate flow predictions with full uncertainty bands
8. **Output** — Save posterior samples, diagnostic plots, and flow rating curves to `outputs/`

### Decision Tree: Which Flow Equation?
- Open channel, uniform flow → Manning's equation
- Open channel, gradually varied flow → Standard step method with Manning's n
- Pressurized pipe, turbulent → Darcy-Weisbach (preferred) or Hazen-Williams
- Mixed (open channel + pressure) → SWMM dynamic wave routing

## Workflow 2: Probabilistic Risk Assessment (`/risk-assess`)

### Inputs Required
- Asset inventory (pipe segments, structures, dams with condition data)
- Hazard characterization (design events, environmental loads)
- Consequence data (downstream receptors, population, economic value)

### Steps
1. **Asset characterization** — Compile condition indices, material, age, capacity
2. **Hazard modeling** — Define loading distributions (storm events, operational demands)
3. **Fragility analysis** — For each asset, estimate P(failure | loading level)
   - Use Bayesian updating if inspection or test data is available
4. **Consequence estimation** — Map failure modes to consequences (flood area, service interruption, cost)
5. **Risk calculation** — Risk = ∫ P(hazard) × P(failure|hazard) × Consequence d(hazard)
6. **Ranking** — Sort assets by risk score, identify uncertainty-dominated vs. clearly high-risk
7. **Sensitivity analysis** — Which uncertain inputs most affect the ranking?
8. **Output** — Risk register with confidence intervals, prioritized action list

## Workflow 3: Flood Frequency Modeling (`/flood-model`)

### Steps
1. **Data retrieval** — Pull annual maximum series from USGS dataretrieval or user-provided records
2. **Exploratory analysis** — Plot time series, check for trends, identify outliers per Bulletin 17C
3. **Distribution fitting** — Bayesian GEV or LP3 fitting via MCMC
4. **Regional skew** — Incorporate USGS regional skew as informative prior (Bulletin 17C approach)
5. **Return period curves** — Generate Q vs. T curves with 90% credible intervals
6. **Non-stationarity check** — Optional: fit time-varying location parameter to test for trend
7. **Comparison** — Plot Bayesian estimates against frequentist B17C for validation
8. **Output** — Flood frequency curves, posterior parameter summaries, annual exceedance probability table

## Workflow 4: Pipe Network Analysis (`/pipe-network`)

### Steps
1. **Network definition** — Import or define pipe network topology (nodes, pipes, demands)
2. **Demand uncertainty** — Define demand distributions per node (mean + variance from billing data)
3. **Roughness uncertainty** — Age-dependent C-factor distributions from literature
4. **Monte Carlo simulation** — Sample N=1000+ demand/roughness scenarios
5. **Hydraulic solve** — Run EPANET/WNTR for each scenario
6. **Reliability metrics** — Calculate P(pressure < standard) at each node, P(velocity > limit) in each pipe
7. **Critical component identification** — Rank pipes by contribution to system unreliability
8. **Output** — Reliability maps, critical pipe lists, pressure deficit probability distributions

## Workflow 5: Bayesian Calibration (`/calibrate`)

### Steps
1. **Define parameters** — List parameters to calibrate (n, C, K, etc.) with physical bounds
2. **Set priors** — Informative or weakly informative based on engineering knowledge
3. **Define observations** — Field measurements with measurement uncertainty
4. **Build likelihood** — Wrap hydraulic model as a Python function returning predicted vs. observed residuals
5. **Run MCMC** — PyMC NUTS, 4 chains, assess convergence
6. **Posterior predictive check** — Simulate data from posterior parameters, compare to observed
7. **Parameter reporting** — Summaries with HDI, correlation structure, identifiability assessment
8. **Save calibrated model** — Export posterior samples for use in subsequent analyses
