# Domain Knowledge — Executive Protection Threat Assessment with Crash-Kinematics Cross-Application

This file is the substantive reference the agent reads on demand during every workflow. Two halves: (1) protective intelligence and risk scoring matrix doctrine, (2) automotive crash test interpretation re-cast for vehicle-borne attack analysis.

---

## Part 1 — Protective Intelligence & Risk Scoring

### 1.1 The threat triangle

Most protective intelligence frameworks (US Secret Service Protective Intelligence Manual, DSS-style threat assessment, ASIS PSP body of knowledge) reduce a threat to three coexistent legs:

- **Intent** — does the actor want to harm or disrupt this principal?
- **Capability** — does the actor have the means (vehicles, weapons, technique, access)?
- **Opportunity** — does the engagement give them a window?

A threat with all three is "live"; a threat missing any one is "latent". Every cell of the risk matrix maps to a triangle: likelihood is roughly intent × capability × opportunity, expressed on a 1–5 scale; impact is the consequence severity if all three coincide.

### 1.2 Likelihood scale (5-band, evidence-graded)

| Score | Label | Indicators (any of) | Typical evidence grade |
|-------|-------|---------------------|------------------------|
| 1 | Negligible | No intent + no capability + no opportunity | C–D |
| 2 | Low | Latent intent OR capability OR opportunity, no convergence | C |
| 3 | Moderate | Two legs present; third would have to be acquired | B–C |
| 4 | High | All three legs present, no specific timing indicator | A–B |
| 5 | Imminent | All three legs present + specific timing or precursor indicator | A |

### 1.3 Impact scale (5-band)

| Score | Label | Worst-plausible outcome to principal |
|-------|-------|-------------------------------------|
| 1 | Negligible | Embarrassment, minor reputational; no physical risk |
| 2 | Minor | Disruption to schedule; minor injury possible |
| 3 | Moderate | Schedule loss + minor-to-moderate injury OR significant reputational |
| 4 | Major | Hospitalisation injury, persistent reputational, principal mission failure |
| 5 | Catastrophic | Life-threatening injury or death, fatal mission failure, geopolitical fallout |

### 1.4 The 5×5 matrix and posture mapping

```
         Impact →
        1   2   3   4   5
   ┌───┬───┬───┬───┬───┐
 5 │ Y │ O │ R │ R │ R │
   ├───┼───┼───┼───┼───┤
 4 │ G │ Y │ O │ R │ R │
L  ├───┼───┼───┼───┼───┤
   │ G │ Y │ Y │ O │ R │  3
   ├───┼───┼───┼───┼───┤
   │ G │ G │ Y │ Y │ O │  2
   ├───┼───┼───┼───┼───┤
   │ G │ G │ G │ Y │ Y │  1
   └───┴───┴───┴───┴───┘
```
- **G (green) — Monitor.** No specific countermeasure needed; situational awareness only.
- **Y (yellow) — Mitigate by procedure.** Adjust route, timing, communication. No new equipment.
- **O (orange) — Mitigate by countermeasure.** Add formation depth, hardened vehicle, additional advance, LE liaison.
- **R (red) — Avoid or harden.** Cancel/reschedule, or full hardening (armoured platform, alternate-route discipline, explicit law-enforcement coverage).

The matrix is *tunable* per principal — a sitting head of state's "yellow" is a corporate executive's "red". `resources/threat-tier-rubric.md` captures the principal-specific calibration.

### 1.5 Evidence grades

| Grade | Definition |
|-------|------------|
| A | Multi-source, two or more independent reliable sources, includes physical/forensic or first-party reporting |
| B | Single reliable source (named LE liaison, vetted intel feed, confirmed first-party) |
| C | Open-source unverified — news report, social media, public filing without independent confirmation |
| D | Speculative — analyst inference without source, hypothesis only |

Reports filter and footnote by grade. A D-grade threat scored 5×5 is suspect; an A-grade threat scored 3×4 is actionable.

### 1.6 Threat categories common to EP

Use this taxonomy when populating the matrix:
1. **Targeted physical assault on principal** (assassination, kidnapping, beating)
2. **Vehicle-borne attack** (ramming, intercept, PIT, motorcade ambush) — see Part 2 for the kinematics tooling
3. **IED / explosive device** (VBIED, IED at venue, mail bomb)
4. **Firearms attack at static venue** (active shooter, sniper)
5. **Hostile surveillance / pre-attack indicators**
6. **Mob / disorderly crowd** (uncoordinated, situational)
7. **Activist disruption** (non-violent, reputational primary)
8. **Cyber / technical** (geolocation leak, comms intercept, deepfake at speech)
9. **Accidental / environmental** (vehicle accident not adversarial, medical emergency, weather)
10. **Insider** (member of staff, vendor, host party with access)

Each category gets a row in the risk register; cells are scored with citations.

### 1.7 Pre-attack indicators (the recalibration triggers)

Standard taxonomy (DSS, FBI Behavioural Threat Assessment Center, MOSAIC):
- Surveillance — repeated photography, vehicle on parallel route, drone overflight
- Probing — testing access, schedule guessing, vendor-impersonation calls
- Elicitation — social-engineering staff for principal's schedule
- Acquisition — funds movement, vehicle/weapon purchase, body-armour purchase
- Rehearsal — dry runs along expected motorcade route
- Funding — sudden cash flow into adversary cell

Detection of any indicator is grounds to recalibrate the matrix upward by ≥1 likelihood tier in the relevant rows, with evidence-grade noted.

### 1.8 Mitigation layer mapping

When a cell turns orange or red, recommendations come from a fixed catalogue — the report shows which layer is engaged:

| Layer | Examples |
|-------|----------|
| Routing | Alternate routes, randomisation pattern, avoidance of known chokepoints |
| Timing | Off-peak movement, surprise schedule, advance arrival before crowd build-up |
| Formation | Vehicle order, lead/follow distance, chase-car role, flanker positions |
| Vehicle | Hardening level (B4/B6/B7 BR), runflats, tyre-deflation device readiness |
| Medical | TCCC-trained medic in motorcade, IFAK readiness, hospital pre-coordination |
| LE liaison | Host-country LE escort, intel exchange, traffic plan |
| Comms | Encrypted comms, pre-briefed code words, EAP / exfil triggers |
| Counter-surveillance | SD assets pre-deployed, pattern analysis on inbound surveillance |
| Counter-tech | Cell-network awareness, drone detection, RF discipline |

### 1.9 Documentation discipline

A defensible threat assessment:
- Names every threat in the categorical taxonomy (1.6)
- Scores L and I against the rubric (1.2, 1.3)
- Cites at least one evidence anchor per cell
- States the grade (1.5)
- Maps the cell to a posture (1.4) and a layer (1.8)
- Records assumptions and unknowns explicitly
- Is reviewed within 24 h of any pre-attack indicator detection (1.7)

---

## Part 2 — Crash Test Interpretation, Re-cast for Vehicle-Borne Attack Analysis

This is where the workspace earns its crossover. EP detail leaders typically reason about vehicle threats qualitatively. Crashworthiness engineers have spent fifty years reasoning about vehicle collisions quantitatively, and the *physics is the same*. We borrow their framework.

### 2.1 The four canonical crash test geometries

| Test | Geometry | EP-relevant analogue |
|------|----------|----------------------|
| Frontal full-width (NCAP, IIHS) | Vehicle into rigid barrier at 56 km/h, full width | Head-on ramming attack |
| Frontal small-overlap (IIHS) | 25% overlap with rigid barrier at 64 km/h | Edge-of-lane intercept; corner ramming |
| Moderate overlap deformable barrier (Euro NCAP MPDB) | 40% overlap with deformable face at 50 km/h closing | Glancing intercept; driver-side ramming |
| Side / pole (IIHS, NCAP, Euro NCAP) | Mobile barrier or pole into driver door at 50 km/h | T-bone block; broadside intercept |

Each one already has decades of test data on vehicle-class behaviour, intrusion measurements, and dummy injury values. The EP analyst can reason about a ramming scenario by asking: *which canonical test is this most like, and what does the test data say happens?*

### 2.2 Delta-V — the primary severity metric

Delta-V is the change in velocity of the protected vehicle's centre of mass during the collision. It is the strongest single predictor of occupant injury severity in real-world crash data (Gabauer & Gabler, NHTSA crash-injury datasets).

**For a perfectly inelastic two-vehicle collision** (the worst-case for the lighter vehicle):

```
ΔV_protected = m_attacker / (m_protected + m_attacker) × v_closing
ΔV_attacker  = m_protected / (m_protected + m_attacker) × v_closing
```

Where m is mass and v_closing is the relative velocity at impact. This is the conservation-of-momentum baseline; real collisions are partially elastic, so true ΔV is slightly lower for both, but the inelastic value is the conservative bound for survivability planning.

### 2.3 Delta-V → injury bands (real-world crash data)

| ΔV of protected vehicle | Modal injury severity (belted, modern vehicle) |
|-------------------------|------------------------------------------------|
| < 16 km/h (10 mph) | None / minor |
| 16–32 km/h (10–20 mph) | Minor to moderate (AIS 1–2) |
| 32–48 km/h (20–30 mph) | Moderate to serious (AIS 2–3) |
| 48–64 km/h (30–40 mph) | Serious to severe (AIS 3–4) |
| > 64 km/h (40+ mph) | Severe to fatal (AIS 4–5+) |

These bands derive from NHTSA Fatality Analysis Reporting System (FARS) and Crash Investigation Sampling System (CISS) regressions; they are doctrine-grade for real-world planning. AIS = Abbreviated Injury Scale, the standard EMS/trauma severity code.

### 2.4 Kinetic energy partitioning

The total kinetic energy at impact is partitioned between (a) accelerating the protected vehicle (ΔV²), (b) crumpling structures, (c) elastic rebound, and (d) other (heat, sound, fragment ejection). For vehicle-borne attack analysis we care about (a) and (b).

```
KE_total = ½ m_attacker v_attacker² + ½ m_protected v_protected²
```

When the protected vehicle is stationary at impact (queued at a venue gate, stopped at a light) the entire attacker KE goes into accelerating + crumpling the protected vehicle. This is the single highest-severity geometry the workspace will encounter — a heavy attacker into a stopped principal vehicle — and it maps cleanly to the IIHS small-overlap test scaled up.

### 2.5 Cabin intrusion and survivability

IIHS rates cabin intrusion in centimetres at multiple measurement points (footwell, instrument panel, A-pillar, steering column). Their published bands for the small-overlap test:

| Intrusion (footwell, cm) | IIHS rating | Survivability connotation |
|--------------------------|-------------|---------------------------|
| < 10 cm | Good | Survivable; injuries likely minor-moderate |
| 10–20 cm | Acceptable | Survivable; serious injury possible |
| 20–30 cm | Marginal | Severe injury likely |
| > 30 cm | Poor | Severe-to-fatal likely; egress may be impaired |

For an attack scenario, the workspace estimates intrusion based on attacker mass × velocity² scaled to the test's reference KE, then reads off the band.

### 2.6 Vehicle-class reference inventory

Critical for the calculation — what masses are we dealing with? Categories below are SAE / IIHS class definitions, with curb-mass representative ranges:

| Class | Curb mass (kg) | Common attacker examples |
|-------|----------------|--------------------------|
| Compact car | 1100–1400 | Older sedan, civilian rental |
| Mid-size car | 1400–1700 | Common rental, taxi |
| Compact SUV | 1500–1800 | Common civilian SUV |
| Mid-size SUV | 1800–2200 | Police-style SUV |
| Full-size SUV | 2300–2700 | Suburban, Escalade-class |
| Pickup half-ton | 2200–2700 | F-150, Silverado 1500 |
| Pickup heavy-duty | 2800–3500 | F-250+, Silverado 2500+ |
| Light commercial van | 1900–2700 | Ford Transit, Sprinter — historically attacker-favoured |
| Box truck (Class 3–6) | 4500–11000 | The "Nice 2016" / pedestrian-mall ramming class |
| Tractor unit (Class 7–8) | 10000–18000 unloaded; 36000+ loaded | Highest-energy ramming class |

The workspace's `crash-energy-reference.md` resource keeps this table with sources.

### 2.7 The four EP attack geometries, mapped

| EP geometry | Crash-test analogue | Intuition |
|-------------|---------------------|-----------|
| Head-on ramming (attacker stationary blocker → principal driving in) | Frontal full-width at protected vehicle's speed | Principal's driver bears the ΔV; airbags and crumple do their job within design speed |
| Head-on ramming (attacker driving into stationary principal) | Inverted full-width — full attacker KE into stopped principal | Highest severity per kg of attacker; cabin intrusion can exceed even small-overlap test |
| Edge ramming / oblique intercept | Small-overlap (25%) | Crumple structure mostly bypassed; A-pillar takes load directly; survivability depends heavily on platform |
| T-bone block (attacker into driver/passenger side) | Side-impact pole or moving deformable barrier | Door beams + curtain airbags are the principal defence; intrusion is hardest to control here |
| PIT (rear corner contact at low ΔV to spin) | None canonical — closer to NHTSA evasive-handling tests | ΔV may be modest but loss-of-control is the threat; recovery distance + driver training dominate |
| Box-in (multi-vehicle low-speed corral) | None canonical | Very low ΔV; threat is *immobilisation*, not occupant injury; egress / breakout planning dominates |

### 2.8 Worked example

Threat: a 2400-kg full-size SUV closing at 80 km/h on a stopped principal sedan (1500 kg) at a venue gate.

```
v_closing = 80 km/h = 22.2 m/s
m_attacker = 2400 kg, m_protected = 1500 kg

ΔV_protected (perfectly inelastic) = 2400 / (1500 + 2400) × 22.2 m/s
                                   = 2400 / 3900 × 22.2
                                   ≈ 13.7 m/s ≈ 49 km/h

Protected ΔV ≈ 49 km/h → "Serious to severe (AIS 3–4)" band per 2.3.

KE_attacker = ½ × 2400 × 22.2² ≈ 591 kJ
This is roughly 2.4× the energy in the IIHS small-overlap reference test (≈ 245 kJ for the test geometry).
Expected intrusion: significantly worse than IIHS "Poor" rating in a non-hardened sedan.
Survivability: low without B-level vehicle hardening or kinematic mitigation (motion of principal vehicle to reduce m_protected stationary multiplier).
```

The matrix cell for "ramming attack at venue gate, full-size SUV class" gets:
- Likelihood: from intent + capability + opportunity (separately scored)
- Impact: 5 (catastrophic) — derived directly from the kinematics, not guessed

This is the workspace's signature contribution — the impact column on vehicle-borne attack rows comes from physics, not vibes.

### 2.9 Mitigation that is actually *kinematically* supported

Once you reason in delta-V and energy:

- **Protected-vehicle motion reduces ΔV non-trivially.** If the principal vehicle is moving in the same direction as the attacker at 30 km/h closing, ΔV drops by the same fraction. *Don't park stationary at the gate.* This is why arrival/departure choreography matters more than most details realise.
- **Mass uplift on the protected platform changes the ratio.** A 2300-kg armoured SUV vs. a 1500-kg sedan as the principal vehicle dramatically reduces ΔV against most civilian-class attackers.
- **Lane geometry constrains attacker closing speed.** A serpentine final-approach geometry (jersey-barrier chicane) physically caps the attacker's pre-impact velocity — often the single highest-leverage built-environment mitigation.
- **Bollards class-rated to attacker class.** ASTM F2656 / PAS 68 / IWA 14-1 ratings tell you what attacker mass × velocity a bollard line is rated to stop. The workspace cross-references these ratings against the credible attacker-class inventory.

### 2.10 What this framework does *not* do

- It does not replace a real collision-reconstruction engineer for incident review.
- It does not predict outcomes precisely — uncertainty in mass and closing speed is large; output is a band, not a number.
- It does not endorse offensive use of vehicles by the protective detail. PIT and similar manoeuvres against a threat vehicle are within some details' authorities and outside others'; the workspace flags the legal scope but does not advocate.

The framework's value is in *prioritising* — separating "credible vehicle threat that warrants a hardened platform" from "low-energy harassment that does not".

---

## References & sources

- US Secret Service Office of Protective Operations / Protective Intelligence — public training material
- FBI Behavioural Threat Assessment Center, public publications
- Department of State Diplomatic Security Service — public training references
- ASIS International, Protection of Assets, Crisis Management volume
- NHTSA NCAP New Car Assessment Program — published test methodology
- IIHS Small Overlap Frontal Crashworthiness Evaluation — test protocol & ratings band
- Euro NCAP test protocols (frontal MPDB, side, AEB)
- Gabauer & Gabler, "Comparison of Roadside Crash Injury Metrics Using Event Data Recorders," AAAM/SAE
- ASTM F2656-20 — Standard Test Method for Crash Testing of Vehicle Security Barriers
- PAS 68 / IWA 14-1 — vehicle security barrier standards
- DHS CISA, Vehicle Ramming Attack Mitigation reference materials
- NIST SP 800-30 r1 — Guide for Conducting Risk Assessments
- ISO 31000 — Risk management principles and guidelines
