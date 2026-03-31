# Constraints

## Engineering Ethics
- All outputs are for informational and analytical support only — not a substitute for licensed PE review
- The agent must flag when results approach life-safety thresholds and recommend professional review
- Never present probabilistic results as guarantees of safety or failure

## Data Handling
- Do not commit real infrastructure location data, SCADA credentials, or sensitive facility information to public repositories
- Anonymize or generalize site-specific data in examples and work logs
- Note data provenance and quality for all inputs used in analysis

## Computational
- Bayesian MCMC chains should run convergence diagnostics (R-hat, ESS) before reporting posteriors
- Monte Carlo simulations should report the number of samples and convergence metrics
- Large model runs should estimate runtime before executing

## Regulatory
- Clearly state which design standards and guidelines are being applied
- Flag when analysis assumptions deviate from regulatory requirements
- Distinguish between code-minimum and risk-informed design recommendations

*Updated by `/onboard` with project-specific constraints.*
