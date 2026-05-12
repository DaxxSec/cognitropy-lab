# Attack Modality Case Base — Methodology Only

A case base of *modalities* of vehicle-borne and physical attacks against principals or principal-class targets, presented to inform the workspace's risk scoring and kinematics analyses. **Methodology and lessons only — no operational instructions, no glorification, no "how-to".**

Each entry is anonymised at the operational level and references the modality, public-record outcome, and the protective lessons.

## Purpose

To inform:
- The base-rate columns in `domain-knowledge.md` §1.6 (which threat categories are realised in which sectors and geographies)
- The "credible attacker class" inputs to `/crash-kinematics` for given geographies and target classes
- The "what could happen here" vocabulary used in `/route-survey` chokepoint assessment

This is **not** a target list, **not** a planning aid for offensive use, and **not** a "what if I were an attacker" exercise.

## Modality 1 — Pedestrian-mall vehicle ramming

**Open-source pattern:** Box-truck or commercial vehicle into pedestrian-dense space. Public-record incidents in Nice (2016), Berlin (2016), New York (2017), Toronto (2018), London (2017), Stockholm (2017).

**Attacker class observed:** Box trucks (Class 3–6, 4500–11000 kg) and light commercial vans (1900–2700 kg).

**Closing-speed observed:** 60–100 km/h sustained in straight pedestrian malls; lower (15–40 km/h) in constrained/turning approaches.

**Protective lessons:**
- ASTM F2656 / PAS 68 / IWA 14-1 rated bollards are the categorically-strongest mitigation; venues without them have no kinematic defence
- Temporary measures (concrete jersey barriers placed correctly) provide partial mitigation
- Geometry constraint (chicanes, deflection furniture) often outperforms posture or formation-only mitigations

**Workspace implication:** When the engagement is in a pedestrian-dense static venue, *Modality 1* is the default credible vehicle-borne scenario unless rated HVM is documented.

## Modality 2 — Motorcade ambush at chokepoint

**Open-source pattern:** Attacker(s) wait at a chokepoint (intersection, narrow bridge, mandatory stop) with vehicle(s) and/or weapons. The principal vehicle is forced to slow or stop, attack initiates.

**Attacker class observed:** Multi-vehicle teams; attacker vehicles often passenger sedans and SUVs.

**Closing-speed observed:** Variable — chokepoint geometry sometimes enables high-energy ramming, more often the attack is firearms-led with vehicle as block/intercept.

**Protective lessons:**
- Forced chokepoints are the dominant predictor; chokepoint avoidance > chokepoint hardening
- Chase car role configuration matters (block vs. exfil-position) and depends on whether ramming or firearms is the primary modality
- Pre-attack surveillance is almost universal in coordinated motorcade ambushes — surveillance-detection is high-leverage

**Workspace implication:** `/route-survey` weighs chokepoint identification as the central activity for any motorcade leg. `/protective-formation` configures chase role to the dominant chokepoint scenario.

## Modality 3 — Static-venue arrival ramming at gate

**Open-source pattern:** Attacker drives a vehicle at the principal's vehicle as it slows or stops at a venue gate. The geometry is essentially the IIHS small-overlap or frontal full-width test, depending on offset.

**Attacker class observed:** Wide range — civilian sedans, SUVs, and commercial vehicles.

**Closing-speed observed:** 40–80 km/h depending on approach lane length and lane geometry.

**Protective lessons:**
- The kinematics-derived rule "never stationary at the gate" (`domain-knowledge.md` §2.9) is the highest-leverage protective behaviour — drops ΔV by ≥ one AIS band
- Pre-cleared sterile arrival lane physically separated from public traffic (jersey or rated barriers) is the structural mitigation
- Venue-side chicane in the final 50 m of approach caps attainable closing speed and is often more effective than vehicle hardening

**Workspace implication:** `/protective-formation` step 6 (arrival/departure choreography) is mandatory for any Orange or Red engagement. `/crash-kinematics` is run for the venue-gate scenario as the default credible vehicle-borne row in the matrix.

## Modality 4 — PIT or low-energy block-and-attack

**Open-source pattern:** Attacker(s) corral or spin the principal vehicle at low closing energy to immobilise, then attack on foot or with a second vehicle.

**Attacker class observed:** Civilian sedans / SUVs.

**Closing-speed observed:** Low — 20–40 km/h.

**Protective lessons:**
- Low ΔV → occupant injury from the impact alone is typically minor; the threat is *immobilisation* and what follows
- Driver training (evasive driving, EVOC) and chase-car interposition dominate this modality
- Egress / breakout planning matters more than vehicle hardening here

**Workspace implication:** Kinematics for this modality emphasise loss-of-control and breakout, not occupant injury. `/protective-formation` configures chase to interpose; `/route-survey` identifies geometries where boxing-in is feasible.

## Modality 5 — VBIED at static venue

**Open-source pattern:** A vehicle-borne improvised explosive device parked or driven at a venue. Distinct from ramming: the threat is the device, not the kinetic impact.

**Attacker class observed:** Civilian and commercial vehicles, depending on payload.

**Protective lessons:**
- Standoff distance is the primary mitigation (DHS / FEMA RMS publications give standoff tables by payload class)
- Inspection regime suppresses likelihood; VBIED detection at the perimeter is the structural mitigation
- The kinematics methodology of this workspace does not directly cover blast effects — refer to FEMA RMS series and DHS CISA materials for blast-effect modelling

**Workspace implication:** `/route-survey` IED-predictability scan is the relevant workflow, not `/crash-kinematics`. The matrix's IED row is scored separately from the vehicle-borne row.

## Modality 6 — Hostile surveillance leading to attack

**Open-source pattern:** The first observable phase of most coordinated attacks against principals — surveillance, probing, rehearsal — before the attack itself.

**Attacker class observed:** Variable; the threat actor is human, not vehicular.

**Protective lessons:**
- Pre-attack indicators (`domain-knowledge.md` §1.7) are detection-grade not prevention-grade — but they are recalibration-grade for the matrix
- Counter-surveillance assets pre-deployed to high-likelihood observation positions are the classic mitigation
- Pattern analysis on inbound surveillance reports often reveals adversary identity faster than any single sighting

**Workspace implication:** This modality is its own row in the matrix and its own input to `/risk-matrix --recalibrate`. Surveillance detection is layered into `/route-survey` step 8.

## What this case base does NOT contain

- Specific attacker tradecraft instructions
- Tactical advice that would assist any attacker
- Identifying details about specific incidents beyond what is publicly documented
- Anything that could be repurposed for offensive planning

If a request asks for content that *would* fit any of those, the agent refuses and logs the refusal in `work-log/<date>.md`.

## Citations

- DHS CISA, Vehicle Ramming Attack Mitigation reference materials
- FEMA Risk Management Series, RMS-Series Publications (especially RMS-426 and RMS-453 on bombing/vehicle-borne attack mitigation)
- US Secret Service Office of Protective Operations, public training material
- DSS Diplomatic Security publications
- Public news reporting and after-action analyses for the modalities cited above (no specific incident references included here to keep the case base modality-focused)
