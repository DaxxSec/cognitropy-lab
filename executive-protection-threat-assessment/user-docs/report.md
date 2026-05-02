# Sample Report — Walkthrough

This document walks through the structure of a generated `/report-findings` deliverable so the human reader knows what to expect and how to consume it. The example below is *fictional* and uses a fictional codename `PRINCIPAL-ECHO`.

---

## 1. Executive summary (target: ≤ 200 words)

> "Engagement: PRINCIPAL-ECHO conference keynote, 2026-06-12, [city/country]. Aggregated posture: **Orange**, driven by the vehicle-borne ramming row at venue arrival. Pre-attack indicator scan in last 14 days: clean. The scenario kinematics put the principal in AIS band 3–4 against a credible mid-size SUV class attacker at 60 km/h closing if the principal vehicle is stationary at the gate; rolling-arrival choreography drops the band to 2–3 and the additional ASTM F2656 M50 bollards on the venue's east drive bring the band to 0–1 against the same scenario. Recommendation: **proceed with mitigation** — sterile arrival lane, rolling 15 km/h gate transit, chase platform mass-matched to credible attacker class, and pre-deployed counter-surveillance at the south parking lot (high-likelihood observation position). Single Red cell on cyber/comms intercept driven by recent regional pattern is mitigated by encrypted comms and pre-briefed code words. No travel-cancel recommendation. Recalibrate at engagement +24h."

That paragraph is what the principal reads. The rest is for the detail leader.

## 2. Engagement scope

A short table: codename, dates, geography, mission. No real names, no real addresses below city level, no live-tracking links.

## 3. Methodology one-liner

A single paragraph stating the workspace's framework — likelihood × impact 5×5, evidence grades A/B/C/D, kinematics override on vehicle-borne rows. This is for the reader who hasn't seen the workspace before.

## 4. Refreshed risk matrix

A Mermaid heatmap and a table of all 10 threat categories. Each row: L, I, posture colour, evidence grade, mitigation layer.

## 5. Per-leg posture

| Leg | From | To | Mode | Worst posture | Driving cell(s) |
|-----|------|----|----|---------------|-----------------|
| L01 | FBO | Hotel | Motorcade | Yellow | Vehicle-borne (low likelihood urban transit) |
| L02 | Hotel | Venue | Motorcade | Orange | Vehicle-borne (gate arrival) |
| L03 | Venue keynote | — | Static | Yellow | Crowd / activist disruption |
| L04 | Venue | Hotel | Motorcade | Yellow | Vehicle-borne (egress predictability) |
| L05 | Hotel | FBO | Motorcade | Yellow | Vehicle-borne (low — randomised time) |

## 6. Route / venue advance findings

Per-chokepoint table from the route survey. Highlights:
- Forced single-lane chokepoint at venue gate; concealment availability score 3; standoff 30 m
- Bollard line at east drive: ASTM F2656 M50/P1 — covers credible mid-size SUV class
- Parking suppression cordon active in 50 m radius around principal arrival lane

## 7. Vehicle-borne scenario bands

For each kinematics scenario the report shows:
- Inputs (attacker class, speed, principal motion)
- ΔV band (km/h)
- AIS band
- Intrusion band
- Mitigation deltas table

## 8. Formation and choreography

- Vehicle order: lead (Tahoe, 2600 kg, runflats) — principal (Suburban, 2700 kg, B6, runflats) — chase (Tahoe, 2600 kg) — counter-vehicle (Tahoe, 2600 kg)
- Distance schedule: 1.5 vehicle lengths urban; 2 lengths arterial; 3 lengths highway
- Arrival choreography: never stationary at gate; rolling 15 km/h transit through sterile lane
- Departure choreography: visually verified ≤ 10 minutes before; lead clears, chase covers exfil
- Comms plan: encrypted handheld; pre-briefed code words for posture changes; EAP triggers documented

## 9. Mitigation coverage map

For every Orange/Red cell:
- Engaged layer(s)
- Not engaged + reason
- Recommendation if gap

## 10. Recommendation

Proceed / proceed-with-mitigation / reschedule / cancel — one verdict, with the cell that drove it.

## 11. Pre-attack indicator scan

What was looked for, what was found (or "nil"), period covered, sources.

## 12. Assumptions and unknowns

Ranked by what would shift posture most if known. Each unknown is followed by the collection action that would resolve it.

## 13. Distribution

Codename-keyed list with classification handling. The deliverable's SHA-256 hash is recorded in `work-log/<date>.md`.

## Appendices

- **Appendix A — Kinematics worked calculations.** Each scenario's full ΔV / KE / intrusion math, with assumption sources cited.
- **Appendix B — Evidence anchor list.** Every cell's source, grade, and date.

---

## Reading the report well

Three muscles to develop:
1. **Read the executive summary first; if you stop there, you've still got a defensible posture.** The rest is for action and audit.
2. **Spot the assumption drift.** If a cell scored Red is anchored to a single C-grade source and a kinematics scenario whose closing-speed assumption is the upper bound of the credible range, that's a Red built on a stack of conservative bounds. Worth a second look.
3. **Use the mitigation coverage map, not the matrix, to plan the day.** The matrix tells you *what* could go wrong; the coverage map tells you *what's already taking care of it* and *what isn't*.

Generated reports never overwrite — `outputs/<engagement-id>-tha-report-<date>-v<n>.md` increments on each regeneration so the trail is preserved.
