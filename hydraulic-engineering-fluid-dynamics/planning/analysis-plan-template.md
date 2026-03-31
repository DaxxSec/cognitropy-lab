# Analysis Plan Template

## Project
<!-- Brief description of the hydraulic analysis project -->

## Objectives
1. <!-- Primary analysis objective -->
2. <!-- Secondary objectives -->

## Data Requirements
| Data Type | Source | Status | Quality Notes |
|-----------|--------|--------|---------------|
| Flow records | | Needed / Available | |
| Geometry | | Needed / Available | |
| Terrain | | Needed / Available | |
| Asset condition | | Needed / Available | |

## Analysis Sequence
1. **Data acquisition and QC** — [estimated effort]
2. **Exploratory analysis** — [estimated effort]
3. **Model setup** — [estimated effort]
4. **Bayesian calibration** — [estimated effort]
5. **Production runs** — [estimated effort]
6. **Results interpretation** — [estimated effort]
7. **Reporting** — [estimated effort]

## Key Uncertainties
- Parameter: [which parameters are uncertain, what priors will be used]
- Model: [which model assumptions might not hold]
- Data: [data quality concerns, record length limitations]

## Success Criteria
- [ ] Convergence achieved (R-hat < 1.01, ESS > 400)
- [ ] Posterior predictive checks pass
- [ ] Results are defensible under regulatory review
- [ ] Uncertainty ranges are communicated to stakeholders

## Pivot Triggers
- If MCMC doesn't converge: reparameterize, use stronger priors, or simplify model
- If data quality is poor: switch to informative priors, reduce model complexity
- If results contradict engineering judgment: investigate model specification, check likelihood

## Deliverables
1. <!-- Technical memorandum -->
2. <!-- Summary presentation -->
3. <!-- Data files and reproducible analysis code -->
