# Report Generation Guide

## Available Report Types

### 1. Condition Assessment Report
Use prompt: `prompts/condition-assessment.md`

Produces a formal inspection report suitable for regulatory submission. Includes:
- Dam description and inspection summary
- Feature-by-feature condition ratings
- Instrumentation data review
- Potential failure mode screening
- Prioritized recommendations

### 2. Anomaly Analysis Report
Use prompt: `prompts/anomaly-report.md` or command `/analyze-readings`

Produces a technical analysis of instrumentation data. Includes:
- Data quality assessment
- Statistical anomaly detection results
- Trend analysis
- Cross-instrument correlation findings
- Recommended actions by severity

### 3. Potential Failure Mode Analysis (PFMA) Screening
Use prompt: `prompts/failure-mode-screening.md`

Produces a screening-level PFMA suitable for risk-informed decision making. Includes:
- Applicable failure modes for the dam type
- Initiating conditions and load cases
- Current level of concern
- Recommended investigations

### 4. EAP Gap Analysis
Use command `/eap-review`

Reviews an Emergency Action Plan against FEMA 64 requirements. Includes:
- Component completeness check
- Scenario coverage assessment
- Contact information currency flags
- Prioritized improvement recommendations

## Report Formatting
All reports follow structured templates with clear section headers, severity ratings, and traceable references. Reports are designed to be professional and suitable for regulatory submission after review by a licensed Professional Engineer.
