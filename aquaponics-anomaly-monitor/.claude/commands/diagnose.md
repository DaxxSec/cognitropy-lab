# /diagnose — Root Cause Analysis

Deep-dive differential diagnosis for a specific parameter anomaly.

## Usage
`/diagnose ammonia`
`/diagnose pH crash`
`/diagnose dissolved oxygen`
`/diagnose no2 spike`

## Workflow
Follow the appropriate RCA workflow from `context/for-agent/workflows.md` — Workflow 3.

## Process
1. Identify the anomalous parameter from the command argument
2. Present the ranked differential diagnosis (most likely causes first)
3. Ask confirmatory questions to narrow down the cause
4. As answers come in, update the probability ranking
5. When confident, present:
   - Most likely root cause
   - Supporting evidence
   - Recommended treatment
   - How to confirm resolution
   - Prevention for next occurrence

## Output Structure
```
DIAGNOSING: [parameter] [current value vs. normal]

DIFFERENTIAL DIAGNOSIS:
  1. [Most likely cause] — [Evidence supporting / against]
  2. [Second cause] — [Evidence supporting / against]
  3. [Third cause] — [Evidence supporting / against]

CONFIRMATORY QUESTIONS:
  - [Question 1]
  - [Question 2]

[After questions answered:]

ASSESSMENT: [Confirmed/likely cause]
TREATMENT PLAN: [Step-by-step actions]
RESOLUTION INDICATORS: [How to know it's fixed]
PREVENTION: [What to change to prevent recurrence]
```
