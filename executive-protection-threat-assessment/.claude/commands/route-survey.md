# /route-survey — Risk-Scored Route or Venue Advance

Score a planned route or venue against the active risk matrix. Identify chokepoints, ambush geometry, IED predictability, vehicle-borne approach lanes, bollard rating gaps, and exfil paths.

## Required Inputs

- Route geometry (geojson polyline) OR venue floor-plan with arrival/departure marks
- Engagement timing (arrival window, departure window, expected dwell)
- Active risk matrix from `outputs/<engagement-id>-risk-matrix.md`
- Vehicle inventory from `context/for-agent/environment.md` (so we know what platforms are available and their turning radii)
- Optional flag `--venue` for static-venue advance (skips route-section and runs perimeter scoring)

## Procedure

### 1. Geometry intake
- Annotate the polyline (or floor-plan) with leg-IDs from the threat assessment
- Mark each segment's posted speed limit, expected actual speed, and lane count
- Mark ingress/egress points, parking lots adjacent, and any pedestrian-cross zones

### 2. Chokepoint identification
A chokepoint is any point where the motorcade or principal cannot deviate. Catalogue every one:

| Chokepoint type | Examples |
|------------------|----------|
| Forced single-lane | Bridges, tunnels, narrow alleys, divided-road merges |
| Mandatory stop | Traffic light at intersection, gate scanner, security check |
| Funnelled pedestrian | Single elevator, escalator, narrow corridor |
| Ramp / grade | Loading dock ramp, parking garage curve, entrance ramp |

For each chokepoint, score:
- Forced (Y/N) — is there an alternate?
- Predictable (1–5) — how confidently could an attacker know the principal will pass through it?
- Standoff (m) — distance from chokepoint to nearest concealment a hostile could occupy
- Concealment availability (1–5) — abundance of hostile observation/setup positions

### 3. Ambush geometry analysis
For each chokepoint, evaluate the four ambush dimensions:

- **Approach lanes for an attacker** — list concretely (cross-streets, parking-lot exits, parallel routes)
- **Time-to-target** — at posted/observed speeds, how long does an attacker have between principal entering chokepoint and principal exiting?
- **Egress for attacker** — does the geometry favour attacker escape (good) or trap them (less attractive to attempt)?
- **Egress for protected motorcade** — what alternates exist? Can the chase car become lead-out? Is reverse-direction egress feasible?

Record each as a 1–5 score.

### 4. IED / VBIED predictability scan
At each chokepoint and dwell point:
- Are there fixed roadside features (planters, news boxes, parked cars, dumpsters) that could conceal an IED?
- What's the inspection regime (frequency, last verified inspection)?
- Are there parking spots within 30 m of the principal's path that an attacker could pre-position a VBIED in?

Score IED predictability 1–5 and note the inspection delta needed to suppress it.

### 5. Vehicle-borne approach lane analysis
For each chokepoint, identify the credible attacker approach lanes (from §3 above). For each, hand off to `/crash-kinematics` with:
- Attacker class (worst-credible from the engagement matrix)
- Approach lane length (sets max attainable speed under acceleration model)
- Geometry (head-on, oblique, T-bone)

Aggregate the kinematics outputs back into a per-chokepoint vehicle-attack severity band.

### 6. Bollard / barrier audit
If the venue or route has hostile-vehicle-mitigation infrastructure:
- Identify each barrier line by location
- Record its rating (ASTM F2656, PAS 68, or IWA 14-1) — see `resources/crash-energy-reference.md`
- Cross-check against the credible attacker class × speed
- Flag any gap as a Red sub-finding

If the venue has *no* HVM infrastructure but the credible threat warrants it, recommend temporary measures (concrete jersey barriers, traffic plan, parking suppression in a cordon) and tag for venue management coordination.

### 7. Exfil path analysis
For each chokepoint and dwell point, identify:
- **Primary exfil** — the planned route out
- **Alternate exfil** — secondary if primary is blocked
- **Contingency exfil** — last resort, may require off-road or reverse-direction

For each exfil, score:
- Drivability for principal-vehicle class (e.g. armoured Suburban turning radius vs. narrow alley)
- Time to clear (in minutes) at posted vs. emergency speeds
- LE / liaison ability to clear it dynamically

### 8. Surveillance-detection windows
A route survey isn't only about the route — it's also about *what an attacker doing surveillance on the route would look like*. Identify:
- Likely surveillance positions (high ground, parking-lot stalls with views, café tables)
- The detail's ability to pre-deploy surveillance-detection assets to those positions
- Any historical reporting of suspicious activity at those positions

### 9. Save and integrate
Save as `planning/route-survey-<engagement-id>-<leg>.md` with:
- Annotated map (Mermaid sequence or geojson reference)
- Chokepoint table (one row per chokepoint, all scores above)
- Vehicle-borne handoff results (one row per credible scenario)
- Bollard / barrier verdict
- Exfil plan (primary / alternate / contingency)
- Recommended changes (route alternates, additional advance, LE coverage requests)

### 10. Log
Append to `work-log/<date>.md` with chokepoint count, Red findings count, recommended changes count.

## Output

A planning artefact under `planning/`, plus updates to:
- The matrix's vehicle-borne and IED rows (likelihood) where the survey changed the score
- The mitigation coverage map in the active threat assessment
- Recommendations to detail leader: route changes, advance assets, LE coordination

## Decision rules

- Forced + concealed + close-standoff + bollards under-rated → Red sub-finding; require alternate or layered LE coverage before proceeding
- Exfil from a chokepoint requires backing down a single lane → recommend vehicle order change so the chase car becomes lead-out at that point
- IED predictability ≥ 4 with no inspection regime → require pre-arrival sweep or accept Red posture for that chokepoint
