# /triage — Multi-Alert Prioritization

When multiple parameters are out of range simultaneously, determine the correct intervention order.

## Input
Current alert state (from a previous `/scan` result, or operator description of active issues).

## Workflow
Follow `/triage` workflow from `context/for-agent/workflows.md` — Workflow 2.

## Key Rules
1. DO < 5 mg/L ALWAYS takes priority — fish die in minutes, not hours
2. Never try to fix pH, NH3, and DO simultaneously — pick the highest tier first
3. Rapid partial water change is the universal stabilizer — 20–30% addresses NH3, dilutes toxins, adds buffer — but don't do it if water change water is cold relative to tank (thermal shock)
4. Identify root cause WHILE treating symptoms — symptom-only treatment leads to recurrence

## Output
```
ACTIVE ALERTS: [count] — [severity summary]

TRIAGE ORDER:
  Priority 1: [parameter + action] — Reason: [why this first]
  Priority 2: [parameter + action] — Reason: [why second]
  [etc.]

ROOT EVENT HYPOTHESIS: [most likely underlying cause]

TIME-TO-CRITICAL ESTIMATES:
  [parameter]: [safe for ~X hours without intervention]

AFTER STABILIZATION — INVESTIGATE: [root cause questions]
```
