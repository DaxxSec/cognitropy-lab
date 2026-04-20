---
description: Terrain-scale go / no-go analysis for a specific aspect / elevation / slope with current problem types overlaid.
---

# /slope-check

## Inputs

- Slope parameters: aspect, elevation, slope angle, start zone complexity, runout exposure, trigger potential from above.
- Proposed objective (ski line, crossing, control route).
- Party: size, experience, equipment.
- Current bulletin (problem types active, hazard per band).
- Today's observations relevant to this slope.

## Steps

1. **Terrain rating**: simple / challenging / complex (ATES if available).
2. **Overlay active problems** onto this aspect / elevation. Only problems whose distribution includes this feature count.
3. **Load analysis**: recent HN, wind loading direction, solar, rain-on-snow, explosive work nearby.
4. **Trigger sensitivity**: solo skier vs. group vs. mechanized vs. remote trigger from thin spots.
5. **FACETS scan**: surface heuristic traps relevant to this objective (familiarity, tracks, expert halo, etc.).
6. **Call**: go / mitigate / no-go with primary reason.
7. **State what would change the call**: explicit evidence (e.g. "new ECTN result on a representative slope" or "24 h without natural activity") that would move the recommendation.

## Output

- Structured decision record in `outputs/slope-checks/YYYY-MM-DD-<slope-id>.md`
- One-paragraph verbal summary for the user
- FACETS tags identified
