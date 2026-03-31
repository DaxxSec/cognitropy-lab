# Getting Started with Hydraulic Engineering Fluid Dynamics Workspace

## Prerequisites
- Python 3.10+ with pip or conda
- Basic familiarity with hydraulic engineering concepts
- Flow data or a USGS gauge number for your project area

## Quick Start (5 minutes)

1. Clone this workspace repository
2. Run `/onboard` to configure for your project — the agent will interview you about your system, data, and goals
3. Install the Python environment: `pip install numpy scipy pymc arviz matplotlib pandas`
4. Try `/analyze-flow` with a simple open channel calculation to see Bayesian uncertainty in action

## First Analysis Walkthrough

Start simple — take a known channel cross-section and some observed stage-discharge pairs:

1. Run `/analyze-flow` and provide your geometry and observations
2. The agent will set up a Bayesian model, calibrate Manning's n, and show you the posterior distribution
3. You'll get a rating curve with uncertainty bands — compare to your deterministic estimate
4. If the result looks reasonable, try `/flood-model` with your gauge data for flood frequency analysis

## Key Concepts to Understand
- **Posterior distribution**: What the data tells us about uncertain parameters, combining prior knowledge with observations
- **Credible interval (HDI)**: The range containing X% of the posterior probability — analogous to confidence intervals but with a direct probability interpretation
- **Convergence diagnostics**: Checks that the MCMC sampler explored the parameter space properly — the agent runs these automatically and flags issues

## Need Help?
- Check `resources/` for reference tables (Manning's n, Hazen-Williams C, convergence checklist)
- Use the "Explain Bayesian Results" prompt in `prompts/` to translate technical output for stakeholders
- The agent logs all analyses in `work-log/` for reproducibility
