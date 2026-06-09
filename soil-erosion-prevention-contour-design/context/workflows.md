# Soil Erosion Prevention (Contour Design) — Workflows and Methodology

What the agent *does* with the concepts. The backbone is a capacity-planning pipeline: characterize **demand**, set the **capacity budget**, **size** structures, compute **utilization** and **headroom**, find the **bottleneck**, **stress-test**, and schedule **capacity refresh**. Don't repeat concept definitions here — see `context/concepts.md`.

## The capacity-planning pipeline (master sequence)

### Phase 1 — Demand characterization
Quantify the loads the system must absorb. (a) Annual erosion demand via RUSLE A (`/estimate-soil-loss`). (b) Peak runoff demand at a chosen return period via rational or CN method, after establishing Tc (`/forecast-runoff-capacity`, `/budget-infiltration`). (c) Storm sediment-yield demand via MUSLE for any trap structure (`/plan-sediment-basin`). Record the design storm(s) and return period(s) — they are the service-level target.

### Phase 2 — Capacity budget
Set the budgets the demand is measured against. Soil: pull the soil-loss tolerance **T** for each mapping unit. Hydraulic: the target is that every conveyance carries Qₚ with freeboard. Storage: the target service life for basins/terraces. Without Phase 2 numbers, Phase 4 sizing has nothing to be "adequate" relative to.

### Phase 3 — Practice selection
Choose the contour practice set that brings A within T and routes runoff safely (decision tree below). Cheapest-first: cover/residue (C) and contouring (P) before earthwork; terraces and waterways when slope length or concentrated flow demand it.

### Phase 4 — Sizing
Dimension each chosen structure: terrace interval and grade (`/design-terrace-interval`), contour/key-line alignment (`/layout-contour-lines`), waterway cross-section (`/size-grassed-waterway`), basin volume (`/plan-sediment-basin`), check-dam series (`/space-check-dams`).

### Phase 5 — Utilization & headroom
For each structure compute utilization = demand/capacity (Qₚ/Q_cap; A/T; stored/storage) and headroom (freeboard; T−A; spare storage). Tabulate. Flag any utilization > 1.0 (under-designed) and any < ~0.4 (likely over-built — note for cost review, don't reflexively shrink safety structures).

### Phase 6 — Bottleneck identification
Rank structures by utilization. The highest-utilization element is the system bottleneck — it fails first and governs the system's true service level. Improving anything else first is wasted capital.

### Phase 7 — Stress test
Re-run Phases 1/5 with intensified demand: higher return period, climate-scaled rainfall depth, worse cover scenario (`/stress-test-design-storm`). Report the storm magnitude at which the bottleneck's utilization crosses 1.0 — that is the system's real capacity ceiling.

### Phase 8 — Capacity-refresh schedule
Convert time-varying capacity loss (sediment fill, cover/vegetation degradation, channel sedimentation) into a maintenance calendar (`/schedule-maintenance-capacity`). The schedule is part of the design; a basin without a cleanout cadence is an undersized basin.

## Workflow A: Field-to-design first pass

**Goal:** Take a slope/field from raw survey to a justified contour-design recommendation with capacity numbers.

### Steps
1. Gather inputs: slope %, slope length, soil mapping unit (→ K, T), land use/cover (→ C), drainage area, local R-factor and IDF data.
2. Run `/estimate-soil-loss` → A and A/T utilization on the *current* (do-nothing) practice.
3. If A ≤ T already: document the margin and stop at monitoring + maintenance. If A > T: continue.
4. Run the practice-selection decision tree → candidate practice set.
5. Size the structures (Phase 4 commands) and run `/forecast-runoff-capacity` for any channel.
6. Build the utilization/headroom table; identify the bottleneck.
7. Stress-test; record residual risk above design.
8. Emit a recommendation with the capacity-plan narrative (see `prompts/capacity-plan-narrative.md`).

### Decision points
- If concentrated flow paths exist (swales gullying): a grassed waterway or check-dam series is required regardless of RUSLE A.
- If slope length is the dominant LS driver: terraces; otherwise contouring/strip cropping may suffice.
- If permitting/impoundment is implicated: flag for jurisdictional + engineer review before sizing finalizes.

## Workflow B: Practice-selection decision tree

**Goal:** Pick the minimal practice set that brings A ≤ T and conveys design runoff safely.

```
Is there concentrated flow (defined channel / ephemeral gully)?
├─ Yes → Is it an incised/active gully?
│        ├─ Yes → check-dam series + grade control (/space-check-dams); consider diversion above
│        └─ No  → grassed waterway in the drainageway (/size-grassed-waterway)
└─ No (sheet/rill dominant) → Is slope length the main LS driver?
         ├─ Yes (long slope) → terraces (/design-terrace-interval)
         │        └─ level (humid, permeable, storage) vs graded (carry to outlet)?
         └─ No  → Is A still > T after max practical cover (C)?
                  ├─ Yes → contour strip cropping, else contour cultivation (lower P)
                  └─ No  → cover/residue management alone; monitor
```

### Decision points
- Always add cover/residue (C) before earthwork — it is the cheapest utilization reduction.
- Above the critical contour row length, contouring overtops → escalate to strip cropping or terraces.
- Graded structures always need a **stable, designed outlet** (waterway, diversion, or armored drop) — never discharge a graded terrace onto bare slope.

## Workflow C: Capacity stress test & climate sensitivity

**Goal:** Find the storm magnitude that breaks the bottleneck and quantify climate headroom.

### Steps
1. Establish the baseline design return period and its Qₚ / sediment demand.
2. Define scenario ladder: e.g. design (10-yr), +1 step (25-yr), +2 step (100-yr), plus a depth-scaling factor (e.g. +10/+20% rainfall intensity per regional climate guidance).
3. For each scenario recompute demand and utilization across all structures.
4. Plot utilization vs scenario; mark where each structure crosses 1.0.
5. Report the bottleneck's failure scenario and the cheapest capacity addition that buys one scenario step of headroom.

### Decision points
- If the bottleneck fails below the design storm: the design is inadequate — return to Phase 4.
- If structures fail in clusters at the same scenario: the system is balanced (good) but brittle (no spare); recommend a system-wide safety factor rather than one fix.
- If one element fails far earlier than the rest: targeted reinforcement of that single bottleneck is the efficient fix.
