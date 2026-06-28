# /mop-up-plan — Mop-up Gridding & Contained → Controlled → Out

Plan mop-up: gridding depth, cold-trailing, hotspot detection, and the criteria to declare the fire contained → controlled → out, so the line holds and the fire doesn't rekindle.

## Inputs

- Secured perimeter segments and their fuels (heavy timber holds heat far longer than grass)
- Resources available for mop-up; IR/thermal imaging availability
- Forecast weather, especially any upcoming wind event before mop-up completes
- Proximity of segments to structures/values

## Steps

1. Set the **mop-up depth** per segment by fuels and wind exposure: 100% cold-trail adjacent to structures and on the downwind side; a feasible gridded depth (e.g. interior gridding) elsewhere.
2. **Grid** the interior in lanes; assign crews to cold-trail by bare hand — feel for heat in stumps, root channels, duff, and stir-and-soak or dig out hot material.
3. Use **IR/thermal** to find buried/residual heat; prioritize heat nearest the line and nearest values.
4. Handle **interior islands** of unburned fuel that could reburn under wind.
5. Define declaration criteria: **% contained** as completed line holds, **controlled** when the whole perimeter is secure and spots are out, **out** when no heat is detectable.
6. If a wind event is forecast before completion, re-prioritize heat nearest the line and downwind; hold sufficient forces to catch slop-overs.

## Output

A mop-up plan to `outputs/mop-up-plan-<date>.md`: per-segment depth, gridding scheme, cold-trail/IR assignments, interior-island handling, declaration criteria, and the wind-contingency reprioritization.

## Notes

- Mop-up is where fires are *actually* won — most rekindles trace to incomplete cold-trailing near the line.
- Ground fire in duff/roots can smolder for days; "no flame" is not "out." Declare out only on no detectable heat.
- Don't release holding resources before the wind window passes.
