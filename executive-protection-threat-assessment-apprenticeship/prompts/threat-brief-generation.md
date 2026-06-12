# Threat Brief Generation

## Purpose

Produce a concise protective-intelligence threat brief for a detail before a movement or shift change — the daily/operational distillation of the standing assessments into "what the detail needs to know now."

## Prompt Template

```
You are a protective-intelligence analyst briefing an executive-protection detail.

I have the following inputs:

- **Principal / movement:** [PRINCIPAL ROLE + WHAT'S HAPPENING + WHEN/WHERE]
- **Current risk tier:** [T1–T4]
- **Active persons of concern:** [LIST OR "none"]
- **Recent indicators:** [SURVEILLANCE REPORTS / THREAT COMMS / ANOMALIES]
- **Posture:** [DETAIL SIZE, SD/CS, LE LIAISON]

Please:
1. Summarise the threat picture in 3–5 bullets a detail leader can absorb in 60 seconds.
2. Call out any change since the last brief and what it triggers.
3. List the top 3 pre-attack indicators the detail should watch for today.
4. State the immediate-action priority if the threat materialises (get off the X to where).
```

## Expected Output

- A one-page brief: threat picture, deltas, watch-for indicators, immediate-action priority.
- No PII beyond what the detail operationally needs; redaction-safe.
- Clear enough to read aloud at a shift change.
