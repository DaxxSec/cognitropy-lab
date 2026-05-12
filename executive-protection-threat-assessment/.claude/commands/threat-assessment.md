# /threat-assessment — Pre-Engagement Threat Assessment

Produce the deliverable threat assessment for a specific date, location, or itinerary. The assessment is leg-keyed (each itinerary leg gets its own row), grounded in the active risk matrix, and includes mitigation coverage analysis.

## Required Inputs

- Engagement-id (must already exist with onboard + risk-matrix run)
- Itinerary leg-by-leg (arrival, transits, statics, departures, with timing)
- Latest 14-day pre-attack indicator scan
- Active risk matrix from `outputs/<engagement-id>-risk-matrix.md`

## Procedure

### 1. Itinerary intake
List each leg with:
- Leg ID (L01, L02, …)
- Start / end location
- Start / end time
- Transport mode (motorcade / on-foot / aircraft / lift)
- Public exposure level

### 2. Pull and refresh the matrix
- Read `outputs/<engagement-id>-risk-matrix.md`
- If older than 7 days OR a pre-attack indicator surfaced → call `/risk-matrix --recalibrate` first
- Load the recalibrated matrix

### 3. Per-leg row activation
For each leg, identify which of the 10 matrix rows are *active*:
- Vehicle-borne attack: active for transits, inactive for indoor statics
- Active shooter at static venue: active for static legs, modulated by ingress/egress
- Hostile surveillance: active across all legs (it's a precursor, not an event)
- IED: active where attacker has placement opportunity
- Crowd / mob: active only for public-exposed legs

Down-weight inactive rows; do not delete them — record "not applicable to this leg" with reason.

### 4. Pre-attack indicator scan
Run the indicator checklist from `domain-knowledge.md` §1.7 against the last 14 days of reporting. If any indicator hits in this geography or against this principal class, recalibrate likelihood +1 in the relevant rows for the active engagement window.

### 5. Run dependent workflows
For each leg requiring drill-down:
- Vehicle leg → `/route-survey` and `/crash-kinematics` (the latter for at least the most credible vehicle-borne scenario)
- Static venue leg → `/route-survey --venue` for perimeter scoring
- Arrival/departure → `/protective-formation` to confirm choreography

### 6. Aggregate posture
Build a leg-keyed posture summary table:

| Leg | Worst-cell posture | Driving cell(s) | Mitigation engaged |
|-----|--------------------|-----------------|--------------------|
| L01 | Orange | Vehicle-borne ramming, surveillance | Routing, formation, LE liaison |
| L02 | Yellow | Crowd disruption | Timing, formation |
| L03 | Red | Vehicle-borne ramming + active shooter | Hardening, routing, LE coverage, medical pre-position |

### 7. Mitigation coverage map
For every Orange/Red cell, list:
- Each mitigation layer that *is* engaged (with what specifically)
- Each layer that is *not* engaged (with why — out of scope, not authorised, not feasible)
- Coverage gap recommendations (uplift to second layer, etc.)

### 8. Recommendation block
- Proceed / proceed-with-mitigation / reschedule / cancel
- For proceed-with-mitigation: list the specific actions and who owns them
- For reschedule / cancel: state the cell driving the recommendation explicitly

### 9. Save and log
Save as `outputs/<engagement-id>-tha-<YYYY-MM-DD>.md`. Log to `work-log/<date>.md` with deliverable hash and brief recipient (codename only).

## Output

A markdown deliverable with the following sections in this order:
1. Executive summary (≤ 150 words)
2. Engagement scope (codename, dates, geography)
3. Itinerary leg list
4. Refreshed matrix (link or embed)
5. Pre-attack indicator scan results
6. Per-leg posture table
7. Mitigation coverage map
8. Recommendation
9. Assumptions and unknowns
10. Distribution list (codename only)

## Decision rules

- Aggregated Red with no covering mitigation layer → recommend **cancel** or **reschedule**
- Aggregated Red with full mitigation layer engaged → recommend **proceed; recalibrate at engagement +24h**
- Aggregated Orange with single-layer mitigation → recommend **uplift to two layers** before engagement
- Aggregated Yellow → proceed with monitoring
- Any cell raised by pre-attack indicator → carry the recalibration into the next engagement assessment automatically
