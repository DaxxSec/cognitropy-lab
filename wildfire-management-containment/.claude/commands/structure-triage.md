# /structure-triage — WUI Structure-Protection Triage

Classify each threatened structure in a wildland-urban-interface segment into the four NWCG defensibility categories using the structure-triage decision tree, so resources are committed only where firefighters can be safe and a home can actually be saved.

## Inputs

- Structure list for the threatened segment (addresses/IDs; ideally with construction, roof type, survivable space notes, access road)
- Projected fire arrival time per structure or zone (from `/spread-projection`)
- Available crew/engine resources and their qualifications
- Safety-zone and escape-route availability near each structure

## Steps

1. For each structure, pull or request: time before front, presence of a viable safety zone + escape route, survivable space quality, roof/construction hardening, access, and occupant status.
2. Walk Decision Tree 1 in `context/workflows.md`, recording the branch taken and the condition that selected it.
3. Assign one of: **Defensible–Stand Alone**, **Defensible–Prep & Hold**, **Non-Defensible–Prep & Leave**, **Non-Defensible–Rescue Drive-By**.
4. For "Prep & Hold," note the required safety zone and the prep actions (clear combustibles, close vents/windows, pre-deploy hose/water, identify TRIGGER to disengage).
5. Flag any structure where occupant life hazard exists — that escalates to a rescue priority regardless of property defensibility.
6. Produce a prioritized engage/patrol/leave list and explicitly name the structures resources will **not** defend and why.

## Output

A triage table to `outputs/structure-triage-<segment>-<date>.md`: one row per structure with category, the deciding condition, required safety zone, disengagement trigger, and occupant/life-hazard flag. Includes an explicit "not defending" list with rationale.

## Notes

- The gate is **safety zone + escape route**, never property value. No safe place to be → never "Prep & Hold."
- Re-run when fire behavior or arrival time changes materially — a Prep & Hold can degrade to Rescue Drive-By in one wind shift.
- Pair every "Prep & Hold" with `/lces-check` before crews commit.
