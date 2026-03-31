# Risk Assess — Probabilistic Infrastructure Risk Assessment

Perform a Bayesian risk assessment on hydraulic infrastructure assets, combining hazard probability, structural vulnerability, and downstream consequence.

## Required Inputs
1. **Asset inventory** — List of assets with: ID, type, material, age, condition score, capacity
2. **Hazard characterization** — Design events or loading distributions (e.g., storm return periods)
3. **Consequence data** — Downstream receptors, population exposure, economic value, environmental sensitivity

## Analysis Steps
1. Ingest and validate asset inventory
2. Define hazard loading distributions from historical data or design standards
3. Estimate fragility curves — P(failure | loading) for each asset class
   - Update with inspection/condition data via Bayesian updating if available
4. Quantify consequences per failure mode (flooding extent, service interruption, repair cost)
5. Integrate risk: Risk = ∫ P(hazard) × P(failure|hazard) × Consequence
6. Rank assets by expected annual risk with uncertainty bounds
7. Perform sensitivity analysis — identify which uncertainties drive the ranking
8. Generate risk register and prioritized action list

## Output Artifacts
- `outputs/risk-assessment/risk_register.csv` — Ranked asset list with risk scores and confidence intervals
- `outputs/risk-assessment/sensitivity_tornado.png` — Sensitivity analysis chart
- `outputs/risk-assessment/risk_matrix.png` — Likelihood vs. consequence plot
- `outputs/risk-assessment/assessment_report.md` — Narrative report with methodology and findings

## Usage
```
/risk-assess
```
Provide your asset inventory data or point to files in `resources/`.
