---
description: Post-incident analysis using the FACETS human-factors framework.
---

# /incident-review

> This command handles sensitive material. Respect agency peer-review policy before any external release.

## Inputs

- Incident vitals: date, location, party composition, outcome (near miss / partial burial / full burial / injury / fatality).
- Conditions: weather overnight and morning-of, bulletin in effect, relevant observations.
- Decision path: objective, route chosen, turnbacks considered, last decision point, trigger.
- Equipment, rescue response, time-to-extraction.

## Steps

1. Reconstruct the decision timeline. One row per decision point.
2. For each decision, tag **FACETS** traps that may have been in play:
   - **F**amiliarity - slope skied before
   - **A**cceptance - desire to be accepted by group or peers
   - **C**ommitment - reluctance to abandon a plan
   - **E**xpert halo - deference to a more experienced party member
   - **T**racks / scarcity - fear of missing untracked snow
   - **S**ocial facilitation - larger group amplifying risk acceptance
3. Reconstruct the snowpack that failed: weak layer depth, slab properties, problem type.
4. Compare the conditions to the bulletin in effect. Note any mismatch.
5. Extract 2-3 **actionable lessons** assigned to:
   - Training / curriculum
   - Operations / route selection
   - Bulletin language / product
6. Draft an internal peer-review memo in `outputs/incident-reviews/YYYY-MM-DD-<id>.md`.

## Output

- Decision timeline with FACETS tags
- Conditions vs. bulletin comparison
- 2-3 actionable lessons with owner
- Peer-review memo (internal only until release approved)

## Absolute Rules

- No victim blaming language.
- No personally identifying information in any public-facing derivative.
- Keep the frame: "what could any of us learn from this?" not "who screwed up?"
