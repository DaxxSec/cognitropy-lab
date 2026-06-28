# /resource-order — Prioritized, Qualification-Aware Resource Order

Translate a containment plan into a prioritized resource order — crews, engines, dozers, aircraft — with rationale, sequencing, and qualification/safety constraints, so the ask matches the plan and the chain of command.

## Inputs

- The containment plan (`/containment-strategy`) and structure-triage results
- On-scene resources and their types/qualifications
- Per-segment line work required (length, fuels, slope) and target completion window
- Known logistics constraints (access, water, air operations availability, night ops)

## Steps

1. For each plan segment, estimate the line work and pick the resource type using production rates (`context/references.md`) and the capability band.
2. Compute the rough resource quantity to complete the segment within the operational period (line length ÷ production rate × time), and state the assumptions.
3. Add **structure-protection** engines for "Prep & Hold" structures and **air resources** (retardant for line prep / slowing the head; not as a standalone fix) where appropriate.
4. Prioritize the order: life safety / evacuation support → values protection → perimeter control → mop-up.
5. Apply **qualification and jurisdiction** constraints — don't order a resource into work beyond its red-card or outside its authority; note mutual-aid needs and ordering channel.
6. Sequence arrivals (what's needed now vs. next period) and note span-of-control/logistics (water, food, relief).

## Output

A resource order to `outputs/resource-order-<date>.md`: prioritized list of resource type × quantity, the segment each supports, the production/time basis, qualification/jurisdiction notes, arrival sequencing, and the ordering channel. Framed as a recommendation to the IC.

## Notes

- Production rates are order-of-magnitude and drop hard with slope, heavy fuels, and night ops — plan conservatively.
- Air resources support ground forces; they rarely contain a fire alone. Don't order tankers as a substitute for line.
- Never order a resource into an assignment that fails `/lces-check`.
