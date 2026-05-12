# Crash-Energy Reference — Vehicle Classes, Test Geometries, Bollard Ratings

Quick-reference data for `/crash-kinematics`. All values are public-domain reference; cite the source when used in an artefact.

## 1. Vehicle class curb-mass ranges (kg)

Sourced from SAE / IIHS class definitions and manufacturer published curb weights.

| Class | Curb mass (kg) | Representative examples (no endorsement) |
|-------|----------------|------------------------------------------|
| Subcompact / mini | 900–1100 | Smart, Fit-class |
| Compact car | 1100–1400 | Civic-class, Corolla-class |
| Mid-size car | 1400–1700 | Camry-class, Accord-class |
| Full-size sedan | 1700–2000 | Charger-class, Impala-class |
| Compact SUV | 1500–1800 | RAV4-class, CR-V-class |
| Mid-size SUV | 1800–2200 | Explorer-class, Grand Cherokee-class |
| Full-size SUV | 2300–2700 | Suburban, Tahoe, Expedition |
| Armoured full-size SUV (B6) | 3200–3700 | (typical aftermarket B6 conversion) |
| Half-ton pickup | 2200–2700 | F-150-class |
| Three-quarter / heavy-duty pickup | 2800–3500 | F-250+, 2500+ |
| Light commercial van | 1900–2700 | Transit, Sprinter |
| Box truck (Class 3–6) | 4500–11000 | Pedestrian-mall ramming class |
| Tractor unit (Class 7) | 9000–12000 unloaded | |
| Tractor unit (Class 8, GVWR 33000+ lb) | 10000–18000 unloaded; 36000+ loaded | Highest-energy ramming class |

Citation: SAE J1100, IIHS class definitions, manufacturer specifications.

## 2. Canonical crash-test geometries and reference KE

| Test | Geometry | Speed | KE_reference | Source |
|------|----------|-------|--------------|--------|
| NHTSA NCAP frontal full-width | Rigid barrier, 100% overlap | 56 km/h (35 mph) | ≈ 165 kJ for 1500 kg vehicle | NHTSA NCAP protocol |
| IIHS small-overlap frontal | Rigid barrier, 25% overlap | 64 km/h (40 mph) | ≈ 245 kJ for 1700 kg vehicle | IIHS small-overlap protocol |
| Euro NCAP MPDB | Mobile progressive deformable barrier, 50% overlap | 50 km/h closing | ≈ 195 kJ relative | Euro NCAP frontal MPDB protocol |
| IIHS side / pole | Mobile barrier into door OR rigid pole | 50 km/h (31 mph) | ≈ 110 kJ | IIHS side test protocol |
| Euro NCAP far-side | Driver-side oblique impact | 50 km/h | ≈ 110 kJ | Euro NCAP far-side protocol |

Reference KE values are approximate; consult the test protocol for the specific tested vehicle for exact numbers.

## 3. Delta-V → injury severity bands (real-world crash data)

Sourced from NHTSA Fatality Analysis Reporting System (FARS) and Crash Investigation Sampling System (CISS) regressions, modern restraint systems, belted occupants.

| ΔV protected (km/h) | ΔV protected (mph) | Modal injury (AIS) | Severity label |
|---------------------|---------------------|---------------------|----------------|
| < 16 | < 10 | 0–1 | None / minor |
| 16–32 | 10–20 | 1–2 | Minor to moderate |
| 32–48 | 20–30 | 2–3 | Moderate to serious |
| 48–64 | 30–40 | 3–4 | Serious to severe |
| > 64 | > 40 | 4–5+ | Severe to fatal |

AIS = Abbreviated Injury Scale (AAAM). AIS 3 is the threshold for "serious injury" in many policy contexts.

## 4. IIHS cabin intrusion bands (small-overlap test; footwell measurement)

| Intrusion (cm) | IIHS rating | Survivability connotation |
|----------------|-------------|---------------------------|
| < 10 | Good | Survivable; injuries likely minor-moderate |
| 10–20 | Acceptable | Survivable; serious injury possible |
| 20–30 | Marginal | Severe injury likely |
| > 30 | Poor | Severe-to-fatal likely; egress may be impaired |

Citation: IIHS Small Overlap Frontal Crashworthiness Evaluation Protocol.

## 5. Bollard / barrier crash-test ratings

Three standards in common use; vendor cut-sheets list ratings per fixture.

### ASTM F2656-20 (formerly DoS K-rating)

Format: `M-50 P1` — vehicle weight + speed + penetration.

| Vehicle weight | Code | Vehicle |
|----------------|------|---------|
| 1100 kg (small car) | C | Compact car |
| 2300 kg (mid-size) | M | Mid-size SUV / pickup |
| 6800 kg (med truck) | MT | Box truck |
| 29500 kg (heavy truck) | H | Tractor-trailer |

| Speed | Code | km/h | mph |
|-------|------|------|-----|
| 30 mph | 30 | 48 | 30 |
| 40 mph | 40 | 64 | 40 |
| 50 mph | 50 | 80 | 50 |

Penetration distance:
- P1: ≤ 1 m
- P2: 1.01–7.0 m
- P3: 7.01–30 m
- P4: > 30 m

So `M50/P1` = mid-size SUV at 50 mph stopped within 1 m. Common high-spec rating for diplomatic / executive sites.

### PAS 68 (UK / international)

Format: `V/[mass kg]/[mph]/90:0/0.0` — vehicle type, mass, speed, impact angle, penetration / debris.

Common ratings:
- `V/2500N3/64/90:0/0.0` — 2500 kg N3-class vehicle at 64 km/h, 90° impact, zero penetration
- `V/7500N3/64/90:0/0.0` — 7500 kg N3-class vehicle at 64 km/h

### IWA 14-1 (international workshop agreement)

Similar to PAS 68 with harmonised vehicle type codes (M1, N1, N2, N3 commercial classes).

## 6. Cross-reference — credible attacker class to required rating

| Credible attacker | Closing speed credible up to | Required ASTM F2656 (minimum) | Required PAS 68 / IWA 14-1 |
|-------------------|-----------------------------:|-------------------------------|-----------------------------|
| Compact car | 40 mph (64 km/h) | C40 | V/1500N1/64/90 |
| Mid-size SUV | 40 mph (64 km/h) | M40 | V/2500N1/64/90 |
| Full-size SUV / pickup | 50 mph (80 km/h) | M50 | V/3500N2/80/90 |
| Light commercial van | 50 mph (80 km/h) | M50 | V/3500N2/80/90 |
| Box truck (Class 3–6) | 50 mph (80 km/h) | MT50 | V/7500N3/80/90 |
| Tractor unit (Class 8) | 50 mph (80 km/h) | H50 | V/30000N3/80/90 |

If the venue's existing HVM doesn't meet the minimum for the credible attacker class, the kinematics workflow flags this and the route survey escalates to venue management for uplift OR routes around the venue.

## 7. Closing-speed estimation by lane geometry

A key input the workspace doesn't always have direct evidence for: how fast can an attacker actually close on the principal? Approximate caps based on lane geometry:

| Lane geometry | Realistic closing-speed cap |
|---------------|----------------------------|
| Straight, ≥ 200 m run-up, no obstacles | At posted speed limit + 50% (gravity / acceleration permitting) |
| Straight, 50–200 m run-up | 50–80 km/h depending on vehicle class acceleration |
| Straight, < 50 m run-up | 30–50 km/h |
| One bend (90°) approach | Reduce by 30–50% from straight equivalent |
| Two bends or chicane | Reduce to 20–40 km/h |
| Speed bumps in approach | Reduce by 30% |
| Jersey-barrier serpentine | 15–25 km/h cap |
| ASTM-rated bollard line | Effective closing speed = 0 against rated class |

Acceleration assumption: civilian vehicles 0.3–0.4 g sustained; light trucks 0.2–0.3 g; box trucks loaded 0.1–0.15 g; tractor units loaded 0.05–0.1 g. Use these to compute lane-length-limited closing speeds.

## 8. Quick worked-example library (for reference, not for use as planning shortcut)

Each of these is a specific kinematics calculation — the agent should re-derive for the actual scenario, not copy-paste from here. They exist to anchor intuition.

### Example A — Stopped sedan at venue gate, full-size SUV ramming attacker
- m_attacker 2500 kg, m_protected 1500 kg, v_closing 80 km/h (22.2 m/s)
- ΔV_protected = 2500/4000 × 22.2 ≈ 13.9 m/s ≈ 50 km/h → AIS 3–4
- KE_attacker ≈ 617 kJ (~2.5× IIHS small-overlap ref) → intrusion likely Poor

### Example B — Same scenario, principal rolling at 15 km/h same-direction
- v_closing = 80 − 15 = 65 km/h (18.1 m/s)
- ΔV_protected = 2500/4000 × 18.1 ≈ 11.3 m/s ≈ 41 km/h → AIS 2–3 (drops one band)

### Example C — Light commercial van attacker at urban approach (chicane-capped 25 km/h)
- m_attacker 2400 kg, m_protected 1500 kg (sedan), v_closing 25 km/h (6.94 m/s)
- ΔV_protected = 2400/3900 × 6.94 ≈ 4.27 m/s ≈ 15 km/h → AIS 0–1
- KE_attacker ≈ 58 kJ (well below IIHS small-overlap ref) → intrusion Good or better

The chicane is doing more work in Example C than the sedan's restraints could have done if the geometry weren't constrained. This is the reason geometry constraints are usually the highest-leverage mitigation.

## Citations

- SAE J1100 — Motor Vehicle Dimensions
- IIHS Vehicle Class Definitions and Crashworthiness Test Protocols (small-overlap, side, roof)
- NHTSA New Car Assessment Program Test Protocol
- Euro NCAP Frontal Mobile Progressive Deformable Barrier Test Protocol
- AAAM Abbreviated Injury Scale (AIS) 2015 / 2008 update
- ASTM F2656-20 Standard Test Method for Crash Testing of Vehicle Security Barriers
- PAS 68:2013 Impact test specifications for vehicle security barriers
- IWA 14-1:2013 Vehicle security barriers — Performance requirements, vehicle impact test method
- DHS CISA Vehicle Ramming Attack Mitigation reference materials
- Gabauer DJ, Gabler HC, "Comparison of Roadside Crash Injury Metrics Using Event Data Recorders," AAAM/SAE
