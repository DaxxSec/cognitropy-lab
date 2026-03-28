# /report — System Health Report

Generate a structured health report for the aquaponics system.

## Input
- Current parameter readings
- Work log data (if available in `work-log/`)
- Active alerts

## Report Structure
Follow Workflow 7 in `context/for-agent/workflows.md`.

## Output Format
Generate a complete markdown report:

```markdown
# Aquaponics System Health Report
**Date:** YYYY-MM-DD HH:MM
**System:** [system name from context/project.md]

## Executive Summary
[1-2 paragraph overview]

## Current Parameter Status
| Parameter | Value | Baseline | Status | Trend |
|---|---|---|---|---|
| pH | | | | |
[etc.]

## Active Alerts
[severity-tagged list]

## 7-Day Trend Analysis
[if log data available]

## Nitrogen Cycle Health
[efficiency score and assessment]

## Maintenance Recommendations
[prioritized action list]

## Upcoming
[scheduled tasks, harvest windows]
```

Save the report to `outputs/health-report-YYYY-MM-DD.md`
