# Prompt — Field Survey Brief

## Purpose

Open a new survey engagement. Capture the inputs `/survey-plan` needs in one structured exchange, so the engagement begins from a written record rather than a half-remembered conversation.

## Prompt Template

```
We're opening a new EM field-mapping engagement. Capture the brief.

SITE: [site name / address / floor / unit]
CLIENT: [organisation, point of contact, role]
OBJECTIVE: [occupational compliance | general-public compliance | EMC pre-screen | TSCM | fringe-field mapping | environmental baseline]
STANDARD TO MEET: [ICNIRP 2020 | IEEE C95.1-2019 | FCC OET-65 | IEC 62232 | CISPR 32 | IEC 61786 | IEC 60601-2-33 | informational only]
EXPECTED DOMINANT SOURCES: [list — e.g. 700/2100/3500 MHz cellular, 2.4/5 GHz Wi-Fi, 50 Hz transformer, MRI fringe field, …]
FREQUENCY RANGE: [explicit, or "wide baseline"]
ACCESS WINDOW: [date / time / duration]
INSTRUMENT KIT: [probes / antennas / analyser model + cal status]
PPE / SAFETY ENVELOPE: [exclusion zones, dosimetry plan]
SCOPE EXCLUSIONS: [areas / equipment not in scope]
REPORTING DEADLINE: [date + format]
AUTHORIZATION: [written authorization on file — yes/no]
TSCM ONLY — LEGAL BASIS: [contract / law-enforcement scope / not applicable]

Build the survey plan. Walk the top-level decision tree from `context/workflows.md`, choose the standard's relevant limit table, propose a grid + probe + detector + dwell budget, and produce the sign-off-ready scope document.
```

## Expected Output

- A scope document `outputs/plans/<date>-<site-slug>-survey-plan.md` with the inputs verbatim, the chosen tree branch, the grid spec, the parameter table, the dwell budget, and a sign-off line.
- A grid sheet `outputs/plans/<date>-<site-slug>-grid.csv` ready to fill in on site.
- A short "open questions" list of anything the brief left ambiguous — to be resolved with the client before fieldwork.
