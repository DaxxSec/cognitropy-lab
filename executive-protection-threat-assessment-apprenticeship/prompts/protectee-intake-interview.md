# Protectee Intake Interview

## Purpose

Generate a structured intake-interview guide to gather the inputs a `/protectee-risk-profile` needs — run with the principal's staff or the principal, at engagement start. (This is a domain task, not a workspace onboarding step.)

## Prompt Template

```
You are an EP intake analyst preparing to interview a new client's staff to build a risk profile.

I have the following inputs:

- **Principal role / sector:** [TITLE, INDUSTRY, PUBLIC PROFILE LEVEL]
- **Known so far:** [ANY EXPOSURE FACTORS OR PRIOR INCIDENTS ALREADY KNOWN]
- **Interviewee:** [WHO — CHIEF OF STAFF / FAMILY / THE PRINCIPAL]
- **Sensitivities:** [TOPICS TO HANDLE WITH CARE]

Please:
1. Produce an interview guide covering exposure factors, routines, residences, travel, family, digital footprint, prior incidents, and persons of concern.
2. Sequence questions from least to most sensitive; flag privacy-sensitive items.
3. Note which answers feed which downstream command (risk profile, advance, route, SDR).
4. Add closing questions on the principal's risk tolerance and acceptable security footprint.
```

## Expected Output

- A sequenced interview guide grouped by topic, with sensitivity flags.
- A mapping of answers → downstream commands.
- Privacy-aware framing; minimise and protect PII captured.
- A short list of follow-up collection tasks the interview will likely surface.
