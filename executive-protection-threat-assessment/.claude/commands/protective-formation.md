# /protective-formation — Recommend Detail Formation, Vehicle Order, and Choreography

Recommend a detail formation, vehicle order, lead/follow distances, and arrival/departure choreography for the engagement, derived from the active threat matrix and the kinematics scenarios it has been informed by.

## Required Inputs

- Active risk matrix (`outputs/<engagement-id>-risk-matrix.md`)
- Vehicle inventory (`context/for-agent/environment.md`)
- Latest `crash-kinematics` outputs for the engagement
- Engagement leg(s) under consideration

## Procedure

### 1. Identify the formation-driving cells
From the active matrix, identify the 1–2 cells driving the formation requirement. Typically:
- Vehicle-borne attack (most often the driver)
- Hostile surveillance leading to attack
- Active shooter at static venue (where formation governs ingress/egress)

If the dominant cell is from another category (e.g. crowd disruption), formation is constrained primarily by that cell's mitigation needs.

### 2. Vehicle count and class match
From the inventory, list vehicles available for the engagement. For each:
- Class
- Curb mass
- Hardening level
- Driver and EVOC certification

### 3. Tier-to-formation mapping
Apply the principal-tuned rubric from `resources/threat-tier-rubric.md`:

| Posture | Default formation | Vehicle count |
|---------|-------------------|---------------|
| Yellow | Principal + chase | 2 |
| Orange | Lead + principal + chase | 3 |
| Orange (vehicle-borne dominant) | Lead + principal + chase + counter-vehicle | 4 |
| Red | Lead + principal + chase + counter-vehicle + LE escort | 4–5 |
| Red (extreme) | As above + outer LE perimeter + alternate-route ghost motorcade | 5+ |

### 4. Vehicle order optimisation
Order is determined by the dominant kinematics scenario:

- **Trail-side intercept dominant** → chase car must be ≥ attacker class mass and trail close enough to intercept (1–1.5 vehicle lengths). State the chase platform's mass; if lighter than credible attacker, escalate.
- **Head-on ramming at gate dominant** → lead vehicle screens; chase car positioned for exfil, not interception. The lead's job is to take the impact if it occurs.
- **T-bone block dominant** → flanker vehicle on the threatened side, OR weave-pattern movement to deny lateral lock-on.
- **Surveillance-led attack dominant** → counter-surveillance asset deployed forward of the route; formation widens following distances to give the chase observation time.

### 5. Lead/follow distance derivation
- Urban speeds (< 50 km/h): 1.5 vehicle lengths
- Suburban / arterial (50–80 km/h): 2 vehicle lengths
- Highway (80+ km/h): 3 vehicle lengths

Tighten by 0.5 if vehicle-borne ramming is the dominant cell (closer = harder to penetrate). Loosen by 0.5 if surveillance-led attack is the dominant cell (more reaction time).

### 6. Arrival / departure choreography
Apply the kinematics-derived rule from `domain-knowledge.md` §2.9: **never stationary at the gate during principal entry/exit**. Specifically:
- Minimum arrival roll-through speed: 15 km/h (drops ramming ΔV by ≥ one AIS band against most civilian-class attackers)
- Pre-cleared sterile arrival lane physically separated from public traffic
- Departure path pre-confirmed and visually verified ≤ 10 minutes before egress
- Lead car opens the curtain (clears gate), chase car closes it (covers exfil); principal vehicle never stops moving until inside the secured envelope

For static venues, choreograph principal-on-foot transitions:
- Vehicle door opens at minimum standoff from venue entry — measured, not eyeballed
- Cover team forms a moving box during the transition
- Greeters / press / staff are pre-staged to avoid principal stops in transit

### 7. Counter-vehicle role definition
If posture is Orange-vehicle-borne or higher and a counter-vehicle is fielded, define its specific role:
- *Block* — close the chase position to physically deny the attacker's approach
- *PIT-capable* — deploy a PIT only if authorised and the scenario class is within authority; flag if not
- *Decoy* — preceding the principal vehicle to absorb a triggered IED before the principal vehicle passes (rarely justified; record reasoning if recommended)

### 8. Comms plan
- Pre-briefed code words for posture changes (raise to Red, exfil, hold, abort)
- EAP / exfil triggers — what observation triggers what action, by whom, on what comms net
- Hospital pre-coordination — confirmed, with route to trauma centre from each leg

### 9. Save and log
Save as `planning/formation-<engagement-id>.md` with:
- Vehicle order diagram (simple ASCII or Mermaid)
- Distance schedule by speed band
- Choreography sequence (arrival, departure, on-foot transitions)
- Counter-vehicle role
- Comms plan
- Posture-driving cell trace (which matrix cells justified each formation choice)

Log to `work-log/<date>.md` with formation tier and vehicle order summary.

## Output

A planning artefact under `planning/` consumed by the threat assessment report and briefed to the detail.

## Decision rules

- Credible attacker class > chase platform class → escalate the chase platform OR add a secondary chase. Do not field a kinematic mismatch.
- LE escort available → integrate as outermost layer; never collapse the detail's own chase role into the LE car (different mission profile, different driver training).
- High-press / high-visibility engagement → balance threat mitigation against visible posturing; the protectee's mission is part of the optimisation function.
- Counter-vehicle PIT recommendation that exceeds detail's lawful authorities → refuse and recommend an authority-compatible alternate (block, route change, LE handoff).
