# Sensor Anomaly Analysis Prompt

I have instrumentation data from a dam monitoring system that needs anomaly analysis.

## Dam Context
- **Dam Name**: [name]
- **Dam Type**: [type]
- **Instruments Included**: [list of instrument types — piezometers, inclinometers, weirs, etc.]
- **Data Period**: [start date] to [end date]
- **Reading Frequency**: [daily/weekly/monthly]

## Data
[Paste CSV data or describe the data file being provided]

## Known Thresholds
[If action/alert/failure thresholds are defined for any instruments, list them here. If not defined, I will use statistical methods to flag outliers.]

## Specific Concerns
[Any particular instruments or trends you want me to focus on]

## Requested Analysis
1. Data quality assessment
2. Statistical anomaly detection across all instruments
3. Trend analysis for gradual changes
4. Cross-instrument correlation check
5. Severity-ranked findings with recommended actions
