# /fireline-capability — Flame Length → Suppression Capability

Convert observed or projected flame length (and rate of spread) into fireline intensity and the suppression resource type that can actually hold the line, using the Hauling-Chart interpretation — so a flank isn't assigned to a handcrew it will overrun.

## Inputs

- Flame length at the edge in question (ft), observed or projected
- Rate of spread (chains/hr) if available
- Fuel model and slope for context
- The segment/flank being evaluated (head, left flank, right flank, heel)

## Steps

1. Take the flame length; if only ROS/fuel/weather is given, estimate flame length via BehavePlus or the references table, and state the assumption.
2. Compute fireline intensity with Byram's relation `I = (L/0.45)^(1/0.46)` (Btu/ft/s) and report it.
3. Walk Decision Tree 2 in `context/workflows.md` to the band: <4 ft, 4–8 ft, 8–11 ft, >11 ft.
4. Translate to a capability call: direct handline / dozer-engine-retardant or indirect / indirect + air + point protection / disengage from frontal fight.
5. Note implied behavior (torching, spotting, crowning) for the upper bands and the downstream effect on line placement.
6. Hand the recommended resource type to `/lces-check` and `/containment-strategy`.

## Output

A capability call appended to the operational-period notes / `outputs/`: flame length, computed intensity, the band, the recommended tactic and resource type, and the implied fire-behavior caveats.

## Notes

- This sizes *capability at the edge*, not whether you have the resources — that's `/resource-order`.
- Above ~8–11 ft the honest answer is usually indirect + values protection; do not recommend a frontal fight to "try."
- Flame length varies along the perimeter — run per flank, not once for the whole fire.
