# Analyze Readings

Perform automated anomaly detection on dam instrumentation data.

## Usage
Provide instrumentation data as:
- CSV file with columns: timestamp, instrument_id, reading, unit
- Optionally include: reservoir_elevation, temperature, quality_flag
- Or paste tabular data directly

## Analysis Pipeline
1. **Data Quality**: Check for gaps, stuck sensors, out-of-range values
2. **Baseline Statistics**: Calculate historical mean, standard deviation, percentiles
3. **Seasonal Adjustment**: Remove reservoir-level and temperature correlations if data available
4. **Anomaly Detection**: Apply Z-score, CUSUM, and trend analysis
5. **Threshold Check**: Compare against action/alert/failure levels if defined
6. **Cross-Correlation**: Check if anomalies appear across related instruments
7. **Classification**: Rate each finding by severity and confidence

## Output
An anomaly analysis report with:
- Summary of findings (flagged instruments and severity)
- Statistical details for each anomaly
- Recommended monitoring frequency adjustments
- Suggested follow-up actions
