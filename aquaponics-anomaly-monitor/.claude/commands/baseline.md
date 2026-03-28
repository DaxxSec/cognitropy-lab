# /baseline — Establish System Baselines

Derive system-specific anomaly detection thresholds from stable historical readings.

## Requirements
- At least 7 consecutive days of stable readings
- No known events during this period (fish additions, treatments, equipment failures)
- Consistent reading times preferred (morning + evening)

## Input
Accept data as:
- CSV file path (columns: timestamp, pH, temp, nh3, no2, no3, do, ec, notes)
- Pasted CSV rows
- Series of pasted daily readings

## Calculation Method
Follow the statistical method in `context/for-agent/workflows.md` — Workflow 4.

For each parameter:
1. Calculate mean (μ) and standard deviation (σ)
2. Normal range: μ ± 1.5σ
3. Warning threshold: μ ± 2σ (or textbook limit, whichever is more conservative)
4. Critical threshold: μ ± 3σ (or species hard limit, whichever is more conservative)
5. Note: If σ is very low (perfect readings), use minimum variance of 5% of mean

## Output
Generate a baseline profile document and:
1. Display the calculated thresholds table
2. Note any parameters with unusually high variance (needs investigation)
3. Compare to textbook species defaults — flag if system baselines are outside safe species ranges
4. Save to `outputs/baseline-YYYY-MM-DD.md`
5. Recommend updating `context/project.md` baselines section
