# /chemistry — Full Water Chemistry Analysis

Comprehensive water chemistry evaluation including parameter interactions, mineral balance, and plant nutrient availability.

## Input
Current readings including:
- Core parameters: pH, NH3, NO2, NO3, DO, Temp
- Extended parameters (if available): KH, GH, Fe, Ca, Mg, K, P, EC/TDS

## Analysis
Follow the Water Chemistry Workflow in `context/for-agent/workflows.md` — Workflow 6.

## Key Analyses Performed

1. **Nitrogen cycle efficiency** — NH3→NO2→NO3 conversion rates
2. **NH3 toxicity fraction** — Calculate actual toxic NH3 based on pH and temperature
3. **Buffering capacity assessment** — KH adequacy for system bioload
4. **Mineral balance** — Plant macronutrient and micronutrient status
5. **Adjustment recommendations** — Specific products and dosage calculations

## Ammonia Toxicity Calculation
Always calculate free NH3 fraction, not just report total ammonia:
- Formula: NH3_fraction = 1 / (1 + 10^(pKa - pH))
- pKa adjustment: pKa = 0.0901821 + (2729.92 / (temp_K))
- Toxic NH3 (ppm) = total_NH3 × NH3_fraction

## Output
Full chemistry report with:
- All parameters with assessment and recommendations
- Toxicity-adjusted ammonia risk level
- Plant nutrient deficiency/excess indicators
- Prioritized chemistry adjustments with dose calculations
- Save option to `outputs/chemistry-YYYY-MM-DD.md`
