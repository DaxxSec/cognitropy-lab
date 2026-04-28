# Core Workflows — VIP Motorcade Planning with Risk Scoring Matrices

The five workflows below cover the full lifecycle of a movement window. Each one drops artefacts into specific paths so the workspace's "repo-is-memory" model holds across cycles.

## Workflow 1: Threat-Baseline-First Planning Cycle

**Goal:** Establish a documented threat baseline before any route is scored, so likelihood numbers have an anchor.

### Steps
1. **Pull principal profile** from `context/project.md`.
2. **Define the threat horizon** — start of movement window minus 30 days, plus the window itself, plus 7 days after.
3. **Identify candidate threat actors** — categorize as state-nexus, organized criminal, ideological / political, lone-actor, opportunist. Apply only those credible against this principal in this AOR.
4. **For each actor, score Intent and Capability** on 1–5 scales. Likelihood for any related hazard is anchored at `min(intent, capability)` unless a specific targeting indicator pushes it higher.
5. **Catalog targeting indicators** within 90 days: prior surveillance attempts, threat communications, similar-profile incidents in the AOR, leaked schedule fragments, third-party warnings.
6. **Document the baseline** in `outputs/threat-baseline-<YYYY-MM-DD>.md` and log it in `work-log/`.

### Decision Points
- If no specific targeting indicator and no prior incident in 12 months for any candidate actor: cap likelihood at 3 across the matrix.
- If a single actor has both Intent ≥4 and Capability ≥4 against this principal class: every segment with matching exposure must be scored at L≥4 unless mitigated.
- If the baseline is older than 14 days: invalidate all scoring runs that depend on it; force a refresh.

## Workflow 2: Route Survey → Segmented Risk Scoring

**Goal:** Take a candidate route from "a line on a map" to a numbered, scored segment list with documented residuals.

### Steps
1. **Get the candidate route** as GPX/KML, address pair, or paper drive.
2. **Drive it (advance team), or walk it on imagery** — never score a route from map alone for high-threat post.
3. **Segment** — break into stretches of uniform exposure (see `domain-knowledge.md §3`). Aim for 15–35 segments on a 20-minute urban leg.
4. **Tag each segment** with: dominant hazards from the typology, chokepoint Y/N, line-of-sight standoff (m), ingress/egress count, jurisdictional zone, host-nation liaison reachable Y/N.
5. **Score each segment**:
   - Inherent L from the threat baseline anchored to that segment's exposure
   - Inherent I from the typology + segment's standoff/density
   - Apply named mitigations
   - Score Residual L and I
   - Note risk class (Low / Moderate / High / Very High / Extreme)
6. **Roll up to route level** — `route_residual = max(segment_residuals)` with `count(High+)` as tie-break.
7. **Output** — write the survey + scoring sheet to `outputs/<route-codename>/scoring-sheet.md` and log to `work-log/`.

### Decision Points
- If any segment ends Extreme residual: the route is a non-starter. Re-engineer (alternate streets, road closure, change of timing) or drop the route.
- If three consecutive segments are High+ residual: this is a corridor problem, not a segment problem. Look for an alternate corridor.
- If the survey reveals a chokepoint not visible from imagery (e.g. construction): re-survey is mandatory before brief.

## Workflow 3: Multi-Criteria Route Comparison

**Goal:** Pick a primary, alternate, and abort from a set of scored candidate routes.

### Steps
1. **Confirm minimum candidate set** — at least three scored routes covering the same origin/destination pair. Two routes is not a comparison; it's a binary.
2. **Pull weights** from `planning/comparison-weights.md` (defaults in `README.md`). Re-confirm with the detail leader; adjust if the principal has overriding preferences.
3. **Score each candidate** on the criteria: max residual risk, count of High+ segments, total time, time variance, deconfliction, profile, principal comfort.
4. **Apply weights** — produce a composite score per route.
5. **Apply hard vetoes** — any Extreme = veto regardless of composite.
6. **Pick** primary (lowest composite, no veto), alternate (second lowest, distinct corridor), abort (third — typically a "drop the principal at hospital / embassy / safe house" route, scored separately on a *survivability* matrix rather than a comfort one).
7. **Document the choice** with the rationale in `planning/route-decision-<YYYY-MM-DD>.md`.

### Decision Points
- If primary and alternate share more than 30% of their segments by length: alternate is too close to be a meaningful fallback. Find a more distinct route.
- If abort is unscored or unsurveyed: stop. The detail does not move without a surveyed abort.
- If the host-nation liaison is unavailable for the chosen primary at the chosen time: pick the alternate.

## Workflow 4: Contingency Plan Generation

**Goal:** For each waypoint that is meaningfully exposed, produce a tied contingency drill.

### Steps
1. **Pull the High+ residual segments** from the route.
2. **For each, identify the dominant hazard** (the one driving the residual score).
3. **Generate the matched contingency** from the typology:
   - Ambush: speed-through direction, CAT employment, MEDEVAC route from this segment
   - IED: standoff distance, alternate egress, EOD callout protocol
   - Crowd: push-through plan, principal cover, alternate dismount point
   - Medical (principal): nearest trauma facility, route from this segment, hospital diversion authority
   - Vehicle breakdown: tow plan, fall-back vehicle assignment
4. **Capture each as a 1-page drill card** under `outputs/<route-codename>/contingencies/<segment>-<hazard>.md`.
5. **Cross-link** in the operational brief.
6. **Rehearse** — at minimum, table-top with the detail. Live drills for sustained-engagement movements.

### Decision Points
- If a segment has two dominant hazards with different optimal responses (e.g. ambush calls for speed-through but crowd calls for stop-and-cover): this is a drill conflict. Resolve by ranking which is *more probable* per baseline; the other becomes the secondary drill.
- If a contingency requires capability the detail lacks (e.g. CAT not on this movement): the contingency is invalid — adjust mitigation plan or accept the residual.

## Workflow 5: Movement Brief, Execution, After-Action

**Goal:** Move the artefacts from the planning cell to the people who execute the movement, then capture what actually happened.

### Steps
1. **At T-72h to T-12h:** Run `/advance-checklist` — counter-surveillance, physical sweep of motorcade vehicles, liaison confirmation, hospital network confirmation, comms test.
2. **At T-2h:** Run `/movement-brief`. Produces:
   - 1-page driver brief (route, comms, MEDEVAC, top-3 contingencies)
   - Operational brief for the detail (full plan, all contingencies, signal silence zones)
   - Principal-facing brief (residual risk in plain language, what to expect, what to do on a "go-loud" command)
3. **During movement:** Detail leader logs deviations and incidents in `work-log/<YYYY-MM-DD>-<leg>.md` (post-movement transcription is acceptable; live logging on safe legs only).
4. **At T+24h:** Run `/after-action`. Captures:
   - What actually happened (deviations, incidents, near-misses)
   - Was the residual score accurate? (calibration check)
   - Updated residual numbers per segment for the next cycle
   - Lessons for the unit's institutional memory
5. **Archive** — full set of artefacts goes to `outputs/<window>-archive/` and is referenced from the next movement's threat baseline.

### Decision Points
- If an incident occurred: AAR is mandatory and must be reviewed by the contracting office before the next movement.
- If three movements pass with all residuals within ±1 of predicted: the matrix is well-calibrated; proceed. If predictions drift more than that, recalibrate the L/I anchor definitions.
