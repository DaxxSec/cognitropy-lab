# Wildfire Management & Containment — Workflows and Methodology

Step-by-step procedures and the **decision trees** that are this workspace's core technique. `concepts.md` is *what things are*; this file is *what the agent does with them*. Every tree below shows the branch and the selecting condition so the output is auditable.

## The Operational Arc (methodology phases)

Tie every command to where it sits in the incident's life:

### Phase 1 — Size-up
Gather origin/perimeter, current fire behavior (flame length, ROS, spotting), fuel model, slope/aspect, weather now + forecast, values at risk, resources on scene/ordered. Output a one-paragraph size-up. *(`/red-flag-readiness`, `/spread-projection`)*

### Phase 2 — Strategy
Set the strategic intent: full perimeter control vs. point/zone protection vs. confine/contain vs. monitor. Choose direct/indirect/parallel per flank. *(`/containment-strategy`)*

### Phase 3 — Tactics & commitment
Assign divisions, build line from anchor points, triage structures, set evacuation triggers — gating every commitment through LCES and go/no-go. *(`/structure-triage`, `/fireline-capability`, `/lces-check`, `/evac-triggers`, `/resource-order`)*

### Phase 4 — Containment & holding
Hold and improve line, chase slop-overs and spots, report % containment as segments complete.

### Phase 5 — Mop-up → control → out
Grid and cold-trail inside the line; declare controlled, then out. *(`/mop-up-plan`)*

### Phase 6 — Learn
Plan-vs-actual review each shift. *(`/after-action-review`)*

---

## Decision Tree 1 — Structure Triage

For each structure in the threatened segment, walk the tree. Output the category + the deciding condition.

```
Is there time to act before the fire front arrives (vs. projected arrival)?
├─ NO  → Is there immediate life hazard (occupants present)?
│        ├─ YES → NON-DEFENSIBLE — RESCUE DRIVE-BY (life rescue only, no property defense)
│        └─ NO  → NON-DEFENSIBLE — PREP & LEAVE (quick prep if safe en route; do not stay)
└─ YES → Is there a viable SAFETY ZONE + ESCAPE ROUTE for the assigned crew?
         ├─ NO  → NON-DEFENSIBLE — PREP & LEAVE (no safe place to be during front passage)
         └─ YES → Does the structure have survivable space + non-combustible roof/hardening
                  so a crew can hold it through/just after the front?
                  ├─ NO  → NON-DEFENSIBLE — PREP & LEAVE
                  └─ YES → Will it likely survive WITHOUT on-site forces (good space + hardened)?
                           ├─ YES → DEFENSIBLE — STAND ALONE (patrol / check, don't commit)
                           └─ NO  → DEFENSIBLE — PREP & HOLD (the primary engage category)
```

**Hard rule:** safety zone + escape route is the gate. No safe place to be → never "Prep & Hold," regardless of property value.

## Decision Tree 2 — Suppression Capability by Flame Length

Map observed/projected flame length to what can hold the line (the "Hauling Chart" interpretation — exact bands in `references.md`).

```
What is the flame length at the active edge?
├─ < 4 ft   → Direct attack feasible: handcrews & engines at the edge can hold.
├─ 4–8 ft   → Too intense for direct handline. Use dozers, engines, retardant;
│             or go INDIRECT (line back + burnout).
├─ 8–11 ft  → Direct/parallel ground attack likely ineffective at the head.
│             Crown/torching/spotting probable → indirect line + air support;
│             prioritize structure triage and point protection.
└─ > 11 ft  → Crowning, major spotting, control efforts at the head are UNLIKELY to succeed.
              Disengage from frontal fight → indirect, anchor & flank from the rear,
              protect life/values, wait for a change in fuel/weather/topography.
```

Always pair the capability call with `/lces-check` before committing the recommended resource.

## Decision Tree 3 — Go / No-Go Risk-Management Gate

Run before committing any crew to a division (the NWCG Risk Management Process condensed). A single unmitigated NO is a stop.

```
1. Are the 10 Standard Fire Orders being followed?            (No → STOP)
2. Are any of the 18 Watch Out Situations present & unmitigated?  (Yes → mitigate or STOP)
3. Is LCES established and communicated to everyone?          (No → STOP)
4. Have instructions been given AND understood (briefed)?     (No → STOP)
   → If every check passes: GO (with the mitigations noted).
   → Any item unresolved: NO-GO — re-engage only after mitigation or as a direct attack from the black.
```

**Mitigation, not optimism.** "We'll keep an eye on it" is not a mitigation. A named lookout, a tested radio frequency, a timed escape route, and a measured safety zone are.

## Decision Tree 4 — Evacuation Staging (Ready / Set / Go!)

For each protective-action zone, convert projected fire arrival time into staged triggers.

```
Estimate fire ARRIVAL TIME at the zone boundary (from /spread-projection).
├─ Arrival > ~6 hr OR fire not yet aligned toward zone
│     → READY: notify residents, situational awareness, prepare go-kits.
├─ Arrival within the warning window (zone-specific lead time, often ~2–6 hr)
│     → SET: voluntary evacuation; vulnerable populations leave now; stage resources.
└─ Arrival imminent / egress threatened / spotting into zone
      → GO: recommend mandatory evacuation order to the AHJ NOW;
        if egress is already compromised → recommend SHELTER-IN-PLACE / refuge
        (last resort) rather than putting evacuees on a burning road.
```

**Trigger points are geographic + temporal:** a named ridge/road the fire reaching = the trigger, sized so the order precedes arrival by the zone's required clearance time. Lead time must exceed expected evacuation duration (population, road capacity, time of day).

## Workflow — Containment Strategy Selection

**Goal:** choose attack mode per flank and lay out anchor-flank-pinch line.

1. Establish an **anchor point** at the heel (road, the black, rockslide) — never start line in the open.
2. For each segment, run Decision Tree 2 (capability) → direct where flame length <4 ft, indirect where hotter or terrain too steep.
3. Work the **flanks** from the anchor toward the head ("pinch" the head off) — don't fight the head frontally when it's running.
4. Locate indirect line on defensible features (ridgetops, roads, fuel breaks, prior burns); plan burnout to remove fuel between line and fire.
5. Account for **spotting distance** (place line beyond the spotting envelope where possible) and **slop-over** patrol.
6. Reconcile the plan against resources (`/resource-order`) and re-gate through go/no-go.

**Decision points:** if the head is crowning (Tree 2 → >8–11 ft) → abandon perimeter control on the head, switch to point protection + indirect; if a wind shift is forecast → pre-identify which flank becomes the head and pull crews off it before the shift.

## Workflow — Mop-up & Containment-to-Control

**Goal:** secure the line so it cannot rekindle, then declare controlled → out.

1. Grid the interior to a **mop-up depth** appropriate to fuels/wind (e.g. 100% cold-trail near structures; a feasible gridded depth elsewhere).
2. **Cold-trail** by bare hand — feel for residual heat in stumps, root channels, duff; dig out and extinguish or stir-and-soak.
3. Use IR/thermal where available to find buried heat; prioritize heat near the line and near values.
4. Declare segment-by-segment **% contained** as completed line holds; declare **controlled** when the whole perimeter is secured and spots are out; declare **out** when no heat remains.

**Decision points:** wind event forecast before mop-up is complete → re-prioritize heat nearest the line and any unburned interior islands; limited resources → cold-trail the structure-adjacent and downwind segments first.
