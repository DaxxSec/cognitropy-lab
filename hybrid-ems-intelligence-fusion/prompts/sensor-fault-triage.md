# Sensor / Source Fault Triage

## Purpose

Use when a vehicle reports unexpected EMS behaviour (excessive engine on/off, SOC oscillation, missed regen opportunities) and you suspect a fusion-layer cause. Walks through the most-likely-to-least-likely failure modes before pulling in calibration.

## Prompt Template

```
You are triaging a fusion-EMS anomaly. Apply the failure-mode list in `concepts.md` and the source-conflict classes in `.claude/commands/source-conflict.md`.

Anomaly report:
- **Vehicle / variant:** [identifier]
- **Symptom:** [observed behaviour, e.g. engine cycling 4× more than baseline on a familiar commute]
- **First observed:** [date / time / drive id]
- **Frequency:** [first time / intermittent / persistent]
- **Recent changes:** [OTA update / re-calibration / new source / new region of operation]
- **Available data:** [CAN log / V2X log / cloud feed cache / `/audit-fusion-trust` recent reports — list what you have]

Please:
1. Rank the candidate failure modes from most to least likely given the symptom and recent changes. Cite the workspace's failure-mode list.
2. For the top three candidates, list the diagnostic signal you would look at in the available data to confirm / rule out.
3. Identify what's MISSING from the data set above that would materially improve the triage; specify the smallest reproduction you could request from the test team.
4. Recommend the next action — replay analysis, source isolation drive, calibration team handover — and the rationale.
```

## Expected Output

- A ranked candidate list with rationale tied to the symptom.
- Per-candidate diagnostic checklist against available data.
- A targeted data request if anything is missing.
- A single next-action recommendation with a clear hand-off path.
