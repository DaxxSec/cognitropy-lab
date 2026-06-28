# /containment-strategy — Attack Mode & Anchor-Flank-Pinch Plan

Choose direct vs. indirect vs. parallel attack per flank and lay out a containment-line plan anchored at the heel, flanking toward the head — the strategic spine of an operational period.

## Inputs

- Current perimeter / fire anatomy (origin, heel, head, flanks, fingers, known spots)
- Per-flank flame length / capability (from `/fireline-capability`)
- Fuel model, slope, aspect; available natural barriers, roads, ridges, prior burns
- Resources available or orderable; forecast weather and any wind shift
- Strategic intent (full perimeter control / point or zone protection / confine)

## Steps

1. Establish the **anchor point** at the heel (road, the black, rock) — line construction starts here, never in the open.
2. For each segment, take the capability band: direct where flame length <4 ft; indirect/parallel where hotter, steeper, or unsafe at the edge.
3. Plan the **flanking** sequence from the anchor toward the head to pinch the head off; do not assign a frontal fight on a running head.
4. Locate indirect line on defensible features and define **burnout** segments (fuel to remove, ignition sequence, holding forces).
5. Account for **spotting distance** (place line beyond the envelope where feasible) and assign slop-over/spot patrol.
6. Pre-plan the wind-shift contingency: name which flank becomes the head on the forecast shift and the trigger to pull crews off it.
7. Reconcile against resources (`/resource-order`) and gate the plan through the go/no-go tree.

## Output

A containment plan to `outputs/containment-plan-<date>.md`: anchor point, per-segment attack mode + line location, burnout segments, spotting/slop-over patrol, wind-shift contingency, and the resource ask. Suitable as input to the IAP/operational briefing.

## Notes

- Anchor → flank → pinch the head. Fighting the head head-on is how crews get burned over.
- Indirect costs acreage but buys safety and defensible line — that trade is usually correct above 8 ft flame length.
- Every committed segment still has to pass `/lces-check`; a clever plan with no escape route is a no-go.
