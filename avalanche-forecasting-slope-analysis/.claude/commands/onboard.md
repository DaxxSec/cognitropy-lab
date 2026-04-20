---
description: One-time initialization - establish forecaster profile, zone, data sources, and reporting cadence.
---

# /onboard

Run this exactly once when the workspace is first cloned. Subsequent runs should only be used to update after a role change.

## Interview Flow

Ask the user these questions in order. Update `context/role.md`, `context/project.md`, `context/constraints.md`, and `context/for-agent/environment.md` with their answers.

1. **Name and organization.**
2. **Role and authority level** - public forecaster, resort forecaster, DOT highway program lead, guide, researcher, educator?
3. **Credentials** - AIARE, CAA, AMGA, or other relevant certifications.
4. **Forecast zone(s)** - names, elevation bands, aspects.
5. **Publication channel(s)** - public web, phone hotline, social, InfoEx pro exchange, DOT internal.
6. **Issue cycle** - daily bulletin deadline, update frequency.
7. **Operational season** - planned start and end of issue cycle.
8. **This season's focus areas** - new installs (RACS, avalaunchers), known weak layers already being tracked, zone expansions.
9. **Downstream consumers** - public readers, highway control, internal pros.
10. **Data sources you use** - which weather networks, observation tools, bulletin CMS.
11. **Telemetry format** - how does weather station data land in your workflow (dashboard, CSV, JSON)?
12. **Any safety posture overrides** beyond the defaults in `context/constraints.md`?

## Output

- Populate the four context files above.
- Append a `work-log/YYYY-MM-DD-onboard.md` entry noting who onboarded and when.
- Summarize to the user: "Here's what I captured. If anything is wrong, say so now."

## Validation

- Confirm the user acknowledges the non-negotiable safety posture (no unsigned bulletin publication, no use of the word "safe").
- Confirm InfoEx handling boundaries if relevant.
