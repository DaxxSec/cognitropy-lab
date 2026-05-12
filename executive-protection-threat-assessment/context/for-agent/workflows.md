# Core Workflows — Executive Protection Threat Assessment with Crash-Kinematics Cross-Application

Five workflows. The risk scoring matrix is the spine of all of them; crash kinematics enters whenever a workflow involves a vehicle.

---

## Workflow 1: Build the Risk Scoring Matrix

**Goal:** Produce a principal-specific 5×5 risk matrix populated across the 10 standard threat categories, with evidence-graded cells and posture mapping.

### Steps

1. **Confirm prerequisites** — `context/project.md`, `context/role.md`, and `context/constraints.md` are populated. If any are still `{{...}}`, run `/onboard` first.
2. **Pull the rubric** — Read `resources/threat-tier-rubric.md` for the principal's calibration. If this principal is new, instantiate from the default rubric and tune.
3. **Walk the 10 threat categories** (see `domain-knowledge.md` §1.6). For each:
   a. Identify named adversaries, capability inventory, and opportunity windows for the engagement.
   b. Score Intent, Capability, Opportunity each 1–5 — combine into a Likelihood (median, conservative) cell.
   c. Score Impact independently (worst plausible outcome).
   d. Cite at least one evidence anchor per cell with grade A/B/C/D.
   e. Map cell to posture (G/Y/O/R) per `domain-knowledge.md` §1.4.
   f. Assign mitigation layer (§1.8) and note which countermeasure(s) apply.
4. **Run the kinematics override.** For category 2 (vehicle-borne attack), do NOT score impact qualitatively. Hand off to Workflow 4 (`/crash-kinematics`) and ingest its delta-V band as the impact score.
5. **Record assumptions and unknowns explicitly.** Each cell has a "what we'd need to know to upgrade evidence grade" line.
6. **Save** as `outputs/<engagement-id>-risk-matrix.md` with a Mermaid heatmap rendering and a row table.
7. **Log** the session in `work-log/<YYYY-MM-DD>.md` with cell counts at each posture (e.g. "13 Green, 4 Yellow, 2 Orange, 1 Red — sole Red is vehicle-borne ramming at venue gate").

### Decision points
- If more than one cell is Red without independent evidence anchors of grade A, re-examine — likely overweighting.
- If every cell is Green, re-examine — likely under-collected. A real engagement always has *some* Yellow.
- If evidence on any Red is grade C or D, downgrade to Orange pending further collection. Flag what would upgrade it to A.

---

## Workflow 2: Pre-Engagement Threat Assessment

**Goal:** For a specific date, location, or itinerary, produce the deliverable threat assessment used by the detail leader to brief the principal.

### Steps

1. **Itinerary intake** — Walk the engagement leg-by-leg (arrival, transits, static positions, departures). Each leg becomes its own row.
2. **Pull the active matrix** — `outputs/<engagement-id>-risk-matrix.md` from Workflow 1. If older than 7 days OR threat environment shifted, refresh first.
3. **Per-leg delta application** — For each leg, identify which matrix rows are *active* (e.g. ramming threat is mostly during transits, not during a closed indoor static). Down-weight inactive rows.
4. **Pre-attack indicator scan** — Check `domain-knowledge.md` §1.7 against any reporting from the last 14 days. If ≥1 indicator is present in the engagement geography or against principal's profile class, recalibrate likelihood +1 in the relevant rows.
5. **Run dependent workflows** for legs that need them:
   - Vehicle leg → `/route-survey` + `/crash-kinematics`
   - Static venue leg → `/route-survey --venue` + perimeter-scoped scoring
   - Arrival/departure choreography → `/protective-formation`
6. **Aggregate** — Build a leg-keyed posture summary. Roll up worst-cell per leg.
7. **Mitigation coverage map** — For every Orange/Red cell, list which mitigation layer is engaged and which is *not*; flag any gap.
8. **Generate the deliverable** via `/report-findings`. Save as `outputs/<engagement-id>-tha-<date>.md`.
9. **Log** — `work-log/<date>.md` with deliverable hash and brief-recipient identity.

### Decision points
- If aggregated posture is "Red with no mitigation layer covering" → recommend cancellation/reschedule, do not paper over.
- If posture is "Red but full mitigation layer engaged" → proceed, mark as "monitor closely; recalibrate at engagement +24h".
- If posture is "Orange with single-layer mitigation" → recommend uplift to two-layer (e.g. routing + formation, not just formation).

---

## Workflow 3: Route Survey & Venue Advance

**Goal:** Score a planned route or venue against the matrix, identify chokepoints, ambush geometry, IED predictability, and departure exfil paths.

### Steps

1. **Geometry intake** — Get route geojson/polyline OR venue floor-plan with arrival/departure points. Annotate timing.
2. **Chokepoint identification** — Mark every point where the motorcade or principal cannot deviate (one-lane bridges, narrow gates, single elevators, choke-loaded escalators).
3. **Predictability scoring** — For each chokepoint: is it forced (no alternate) or mitigable (alternate exists)? Forced chokepoints score higher likelihood-of-targeting because attacker confidence in principal location is high.
4. **Ambush geometry** — For each chokepoint, score:
   - Available standoff for attacker setup (longer = more PSA / sniper risk; shorter = closer-quarters threats)
   - Concealment availability for attacker
   - Egress for attacker after attack
   - Egress for protected motorcade (this is often what differentiates Yellow from Orange)
5. **IED predictability scan** — Are there fixed roadside features (planters, news boxes, parked cars) at chokepoints that would conceal a VBIED placement? Mark and note inspection regime.
6. **Vehicle attack approach analysis** — For each chokepoint, identify credible attacker approach lanes (cross-streets, parking exits, parallel routes). For each, run the kinematics handoff (Workflow 4).
7. **Bollard / barrier audit** — Where the venue has hostile-vehicle mitigation, look up the rating (ASTM F2656, PAS 68, IWA 14-1) and verify it covers the credible attacker class from `crash-energy-reference.md`.
8. **Exfil paths** — Identify primary, alternate, and contingency exfil from each chokepoint. Score each on principal-vehicle-class drivability (e.g. armoured Suburban turning radius vs. narrow alley).
9. **Save** as `planning/route-survey-<engagement-id>-<leg>.md` with annotated map and chokepoint table.

### Decision points
- If a chokepoint scores "forced + concealed + close standoff + bollards under-rated" → escalate to a Red cell in the engagement matrix and require alternate route or layered LE coverage.
- If exfil from a chokepoint requires backing down a single lane → recommend vehicle order change so the chase car can become the lead-out.

---

## Workflow 4: Crash-Kinematics Vehicle Attack Analysis

**Goal:** Produce a quantitative analysis of a credible vehicle-borne attack scenario using delta-V, kinetic-energy, and intrusion methodology from `domain-knowledge.md` Part 2.

### Steps

1. **Scenario intake** — Specify:
   - Geometry (head-on, oblique 30°, side, small-overlap, PIT, box-in)
   - Attacker vehicle class (one or a range)
   - Attacker closing speed (one or a range)
   - Protected vehicle class and motion state (stationary or moving with closing-velocity contribution)
   - Impact location on protected vehicle (front, A-pillar, driver door, rear corner)
2. **Map to canonical test geometry** — Use the table in `domain-knowledge.md` §2.7. State the analogue.
3. **Compute ΔV_protected** — Use perfectly-inelastic equation (§2.2) as the conservative bound. State both attacker and protected ΔV.
4. **Compute KE partition** — Total KE; show energy that goes into protected-vehicle acceleration vs. crumple absorption.
5. **Read injury band** — From §2.3, map ΔV_protected to AIS band.
6. **Estimate intrusion band** — Scale KE against the canonical test reference KE (§2.5); read intrusion-rating band.
7. **Range, don't point-estimate** — Where mass or speed is uncertain, run the calculation at the 25th and 75th percentile of the range and present both.
8. **Mitigation analysis** — For each available mitigation:
   - Protected-vehicle motion: how much does v_closing drop if principal vehicle is moving at 30 km/h same-direction?
   - Mass uplift: how does ΔV change if principal vehicle is class-uplifted (e.g. mid-size SUV → armoured full-size SUV)?
   - Geometry constraint: at what closing-speed cap does the AIS band drop one tier? What route geometry imposes that cap?
   - Bollard class: what F2656 / PAS 68 rating is required to stop the credible attacker class at the credible closing speed?
9. **Save** as `outputs/<engagement-id>-kinematics-<scenario-id>.md` with:
   - Inputs (assumptions stated)
   - Calculation traces
   - ΔV / KE / intrusion bands
   - Mitigation deltas
   - One-paragraph "what this means for posture" summary
10. **Hand the impact band back to Workflow 1 / 2** — overwrite the qualitative impact score for the relevant matrix cell with the kinematics-derived band.

### Decision points
- If the scenario ΔV puts the principal in AIS 4–5 band and no mitigation drops it below AIS 3 → matrix cell is Red. No vehicle-only countermeasure suffices; routing or geometry change is required.
- If a credible attacker class exceeds the rated bollard line at the venue → escalate to venue management for temporary class uplift (e.g. additional concrete jersey barriers) or change route.
- If protected-vehicle motion drops ΔV by ≥1 AIS band → make "no stationary holds at the gate" a hard recommendation in the report.

---

## Workflow 5: Protective Formation Selection

**Goal:** Recommend a detail formation, vehicle order, lead/follow distances, and arrival/departure choreography given the engagement's threat posture.

### Steps

1. **Pull the engagement matrix** — Identify the 1–2 cells driving the formation requirement (typically vehicle-borne or surveillance).
2. **Determine vehicle count available** — From `context/for-agent/environment.md` and engagement budget.
3. **Match formation to threat tier** — From `resources/threat-tier-rubric.md`:
   - Yellow → 2-vehicle (principal + chase)
   - Orange → 3-vehicle (lead + principal + chase) OR 4-vehicle if vehicle-borne is the dominant cell
   - Red → 4–5 vehicle with hardened platform; consider LE escort
4. **Vehicle order optimisation** — The chase car role depends on the dominant kinematics scenario:
   - If trail-side intercept is dominant → chase car must be heavier than credible attacker class and trail close enough to intercept (typically 1–1.5 vehicle lengths)
   - If head-on ramming at gate is dominant → lead vehicle does the screening; chase car is exfil-positioned
   - If T-bone block is dominant → flanker or weave-pattern formation reduces broadside exposure
5. **Lead/follow distance derivation** — Closer is harder to penetrate, farther preserves response time. Default: 1.5 vehicle lengths in urban speeds; 3 vehicle lengths at 80+ km/h.
6. **Arrival/departure choreography** — Specifically address §2.9 of `domain-knowledge.md`:
   - Never stationary at the venue gate during principal entry/exit; minimum motion = 15 km/h roll-through
   - Pre-cleared sterile arrival lane separated from public traffic by physical barrier
   - Departure path pre-confirmed and visually verified < 10 minutes before egress
7. **Save** as `planning/formation-<engagement-id>.md` with diagrammed vehicle order, distance schedule, and choreography sequence.

### Decision points
- If the credible attacker class exceeds the chase car class in mass → escalate the chase platform or add a secondary chase. A lighter chase against a heavier attacker is a kinematic *liability*, not a mitigation.
- If LE escort is available → integrate as outermost layer; do NOT collapse the detail's own chase role into the LE car.
- If the engagement is high-press / high-visibility, formation must balance threat mitigation against visible posturing — the protectee's mission is part of the optimisation function, not just survivability.

---

## Cross-workflow rules

- **Every workflow ends with a `work-log/<date>.md` entry.** This is non-negotiable; the workspace's institutional memory depends on it.
- **Every persisted artefact uses the principal codename, not real identity.**
- **Every kinematics-touched output explicitly states assumed masses and speeds.**
- **Refusal triggers are global** — see `context/constraints.md`. Any workflow can short-circuit into a refusal at any step.
