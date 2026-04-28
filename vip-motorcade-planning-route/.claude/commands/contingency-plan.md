# /contingency-plan — Generate Waypoint-Tied Contingency Drills

For each meaningfully exposed segment, produce a single-page contingency drill card matched to its dominant hazard.

## Required Inputs
- A route decision at `planning/route-decision-<YYYY-MM-DD>.md`
- The scoring sheet for the chosen primary (and alternate)
- Motorcade composition for this leg
- Hospital network from `outputs/liaison-contacts.md` (sanitized)

## Procedure

### 1. Pull High+ Residual Segments
From the primary's scoring sheet, list every segment with residual band ≥ High. These are the segments that need an *attributable* drill rather than just a generic SOP reference.

### 2. Match Hazard → Drill
For each segment, take the dominant hazard and produce the matched drill:

#### Complex Ambush
- Direction of speed-through (always *away* from initiation, never through it)
- CAT employment plan — where the CAT vehicle peels off and from which side
- MEDEVAC route from this exact segment (separate doc; include lat/longs of nearest trauma facility)
- Comms call sequence (callsign, push, host-nation liaison number)
- "Go Loud" signal — when does the principal go from quiet posture to active escape?

#### IED / VBIED
- Standoff distance for safe halt (typical 100 m for VBIED, 50 m for roadside)
- Alternate egress — which way is the motorcade going *now*?
- EOD callout protocol — host-nation EOD in this jurisdiction, contact, ETA estimate
- Cordon plan — who blocks what

#### Crowd Surge / Crush
- Push-through plan vs hard-stop and cover (which the planner picks based on density and speed)
- Principal cover protocol (shield, prone, into vehicle)
- Alternate dismount point if planned dismount becomes untenable

#### Medical (principal collapse / injury)
- Nearest trauma facility from this segment, and route to it
- Hospital diversion authority — who decides we go to hospital vs back to the safe house
- Onboard medical kit responsibilities (named detail member, what they grab)

#### Vehicle Breakdown
- Tow plan or push plan (push the principal vehicle into cover, redistribute people)
- Fall-back vehicle assignment — who consolidates and where the principal moves
- "Blow the load" criterion — if not back in motion within X minutes, abort

#### Sniper / Long-Range Precision
- Block sightlines (vehicle positioning relative to identified standoff)
- Speed-through; do not stop, do not return fire from open vehicle
- Reroute trigger — which segments to skip if a sniper indicator surfaces mid-leg

#### Spoof Comms / Fake Checkpoint
- Verification protocol with host-nation liaison (callback to a known number, not the channel that called us)
- Refusal-to-stop authority and "soft cordon vs hard cordon" decision
- Default behavior: do not stop without verification on encrypted host-nation channel

### 3. Drill Card Format
Each drill is one page, written from the operator's POV. Format:

```
# Drill: <segment-id> — <hazard>
**Trigger:** [what initiates the drill]
**Decision authority:** [detail leader / driver / on-scene]
**Action — vehicle by vehicle:**
  - Lead: [action]
  - Principal: [action]
  - Follow: [action]
  - CAT: [action]
**Comms:** [call sequence]
**MEDEVAC if injury:** [route + facility placeholder]
**Abort criterion:** [what makes us shift to the abort route]
**Time-to-clear estimate:** [seconds]
```

### 4. Resolve Drill Conflicts
If a segment has two dominant hazards with conflicting optimal responses (e.g. ambush calls speed-through, crowd calls stop-and-cover):
- Rank by current likelihood from the threat baseline.
- Higher-likelihood hazard becomes the primary drill; the other becomes the secondary, with a recognition trigger that switches the response.

### 5. Storage and Brief Inclusion
- Each drill: `outputs/<route-codename>/contingencies/<segment-id>-<hazard-slug>.md`.
- The movement brief includes the top-3 drills (by residual ranking) on the 1-page driver brief, full set in the operational brief.

## Decision Rules

- If a contingency requires capability the detail does not actually have on this leg (e.g. CAT is not in this motorcade): the drill is *invalid as written*. Either change the mitigation plan and re-score, or accept the residual and document the gap.
- If the abort route depends on a hospital that is closed at this hour: redirect to the next-nearest, document, and re-score abort survivability.
- Never write a drill that involves offensive action beyond defensive break-contact / fix-the-ambush. If a drill begins to read as an attack template, stop and re-frame defensively.
