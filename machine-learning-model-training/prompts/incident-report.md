# Incident Report Generator

## Purpose

Turn raw, messy training-failure symptoms (log snippets, a metric screenshot description, an on-call message) into a structured incident report with a severity and a routed runbook. Use this at the *start* of an incident, before mitigation.

## Prompt Template

```
You are a training-run reliability engineer. Triage this training incident.

I have a training failure:

- **First anomalous signal:** [METRIC + VALUE + TIMESTAMP + STEP]
- **Symptom(s):** [WHAT BROKE — NaN loss / OOM / slow / hang / bad data / crash]
- **Run config:** [MODEL SIZE, PRECISION, LR+SCHEDULE, BATCH, PARALLELISM]
- **Fleet/infra:** [GPUS, NODES, SCHEDULER]
- **Latest checkpoint:** [PATH + STEP]
- **Recent changes:** [CONFIG/DATA/CODE CHANGES SINCE LAST GOOD RUN, IF ANY]
- **Logs:** [PASTE RELEVANT LINES]

Please:
1. Assign a severity (SEV-1..4) with a one-line justification (blast radius × reversibility).
2. Classify the failure into a known class and name the runbook to open.
3. State the single most important stabilising action to take right now.
4. List the 3 most likely root-cause hypotheses, most-likely first.
5. Draft the incident-report header (severity, class, routed runbook, first action, empty timeline).
```

## Expected Output

- A severity with justification
- Failure class + routed runbook name
- One immediate stabilising action
- Ranked root-cause hypotheses
- A ready-to-save incident header for `outputs/`
