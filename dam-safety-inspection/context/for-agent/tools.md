# Tools and Analysis Methods

## Anomaly Detection Methods

### Statistical Threshold Detection
- **Z-score analysis**: Flag readings beyond ±2σ or ±3σ from the rolling mean
- **Modified Z-score (MAD-based)**: More robust to outliers than standard Z-score; uses median absolute deviation
- **IQR method**: Flag readings outside Q1 - 1.5×IQR or Q3 + 1.5×IQR bounds
- **Percentile-based**: Flag readings exceeding historical 95th/99th percentile

### Trend Analysis
- **Linear regression**: Detect gradual trends (increasing seepage, progressive settlement)
- **Moving average crossover**: Short-term average crossing long-term average signals regime change
- **Cumulative sum (CUSUM)**: Detect small persistent shifts in mean value
- **Rate of change**: Flag acceleration (second derivative) in displacement or seepage data

### Seasonal Decomposition
- **STL decomposition**: Separate time series into Seasonal, Trend, and Residual components
- **Reservoir-level correlation**: Regress instrument readings against reservoir elevation to establish expected behavior, then analyze residuals
- **Temperature correlation**: Account for thermal effects on concrete dam joint movements and piezometer readings

### Pattern Recognition
- **Stuck sensor detection**: Identify instruments reporting identical values over multiple readings (sensor failure)
- **Drift detection**: Identify gradual sensor drift that may indicate instrument malfunction vs. actual change
- **Correlation analysis**: Compare related instruments (e.g., adjacent piezometers) to identify localized vs. systemic changes

## Inspection Checklist Generation

### Approach
1. Identify dam type and key structural features
2. Select applicable failure modes for that dam type
3. Map each failure mode to observable indicators
4. Generate checklist items organized by dam feature (crest, upstream slope, downstream slope, abutments, spillway, outlet works, toe area, instrumentation)
5. Include both visual and measurement-based checks
6. Add reference photos/descriptions of what each deficiency looks like

### Severity Rating Scale
Based on FEMA condition rating terminology:
- **Satisfactory**: No deficiencies noted. Dam performing as designed.
- **Fair**: Minor deficiencies exist but do not affect dam safety. Routine maintenance needed.
- **Poor**: Deficiency requires remediation. Increased monitoring and engineering evaluation needed.
- **Unsatisfactory**: Dam safety deficiency exists. Urgent remediation required. Restrict reservoir if appropriate.
- **Not Rated / Insufficient Data**: Unable to assess condition. Additional investigation required.

## Reporting Templates

### Condition Assessment Report Structure
1. Executive Summary
2. Dam Description and History
3. Current Condition (by feature)
4. Instrumentation Data Review
5. Anomaly Analysis Results
6. Potential Failure Mode Screening
7. Recommendations (prioritized by severity)
8. References and Data Sources

### Anomaly Report Structure
1. Summary of Findings
2. Data Description and Quality Assessment
3. Analysis Methods Applied
4. Anomalies Detected (with severity classification)
5. Correlation and Context Analysis
6. Recommended Actions
7. Appendix: Raw Data and Statistical Details
