# /crash-kinematics — Vehicle Attack Scenario Analysis

Apply automotive crash test interpretation methodology — delta-V, kinetic-energy partitioning, IIHS / Euro NCAP cabin-intrusion bands — to a credible vehicle-borne attack scenario. The output gives the threat-assessment its impact score for any vehicle-borne row, replacing qualitative guesswork with computed bands.

This command is the workspace's signature crossover from `Automotive & Engine: vehicle crash test interpretation` into `Security & Intelligence: executive protection threat assessment`.

## Required Inputs

- Scenario geometry (head-on, oblique 30°, side / T-bone, small-overlap 25%, PIT, box-in)
- Attacker vehicle class (single class or range from `resources/crash-energy-reference.md`)
- Attacker closing speed (single value or range)
- Protected vehicle class and current motion state at impact (stationary, rolling 15 km/h, full speed)
- Impact location on protected vehicle (front, A-pillar, driver door, rear corner, frontal-corner offset)
- Optionally: candidate mitigations to evaluate (mass uplift to armoured platform, geometry constraint, bollard line)

## Procedure

### 1. Map scenario to canonical test geometry
Use the table in `domain-knowledge.md` §2.7. State the analogue explicitly:

> "Scenario A maps to IIHS small-overlap (25% overlap, 64 km/h reference). Reference test KE ≈ 245 kJ."

If the scenario does not map cleanly to a canonical test (e.g. PIT, box-in), state which canonical test is the *closest* analogue and which respects in which the kinematics differ.

### 2. Compute delta-V (perfectly inelastic — conservative bound)

```
v_closing = v_attacker − v_protected_relative   (in m/s; sign by geometry)
ΔV_protected = m_attacker / (m_protected + m_attacker) × v_closing
ΔV_attacker  = m_protected / (m_protected + m_attacker) × v_closing
```

State both. Show units (m/s and km/h). If inputs are ranges, compute at the 25th and 75th percentile of each and present the band.

### 3. Compute kinetic energy partition

```
KE_attacker_at_impact = ½ × m_attacker × v_attacker²
KE_protected_at_impact = ½ × m_protected × v_protected²    (zero if stationary)
KE_total = KE_attacker_at_impact + KE_protected_at_impact
```

Show what fraction goes into accelerating the protected vehicle (∝ ΔV_protected²) vs. crumpling structure.

### 4. Read injury band
Use `domain-knowledge.md` §2.3 to map ΔV_protected to AIS band:

| ΔV (km/h) | AIS band | Severity label |
|-----------|----------|----------------|
| < 16 | 0–1 | None / minor |
| 16–32 | 1–2 | Minor to moderate |
| 32–48 | 2–3 | Moderate to serious |
| 48–64 | 3–4 | Serious to severe |
| > 64 | 4–5 | Severe to fatal |

State the band with explicit ΔV value; if a range, state both endpoints.

### 5. Estimate intrusion band
Scale scenario KE against the canonical test's reference KE. Read off the IIHS intrusion band (`domain-knowledge.md` §2.5):

```
KE_ratio = KE_scenario / KE_reference_test
```

- KE_ratio < 0.5 → intrusion likely better than test "Good" (small)
- 0.5–1.0 → comparable to test rating of the protected platform
- 1.0–2.0 → likely 1 band worse than test rating
- > 2.0 → intrusion likely "Poor" or worse regardless of test rating

If the protected platform's IIHS or Euro NCAP rating is known, anchor the band to that rating and adjust by the ratio.

### 6. Mitigation analysis
For each candidate mitigation, recompute ΔV and KE:

| Mitigation | ΔV (km/h) | AIS band | Posture delta |
|------------|-----------|----------|---------------|
| Baseline (stationary principal) | 49 | 3–4 | Red |
| Principal rolling at 15 km/h same-direction | 39 | 2–3 | Orange |
| Principal in armoured class-uplift (2700→3500 kg) | 36 | 2–3 | Orange |
| Geometry constraint (chicane caps attacker at 40 km/h) | 24 | 1–2 | Yellow |
| ASTM F2656 K12-rated bollard at venue gate | n/a (attacker stopped) | 0–1 | Green |

Show the calculation trace for each row. The strongest mitigations are usually geometry constraint and bollard rating; vehicle-side mitigations (mass uplift, hardening) are typically partial.

### 7. Bollard / barrier compatibility check
If the engagement venue has hostile-vehicle-mitigation infrastructure, look up its rating in `resources/crash-energy-reference.md`:

- ASTM F2656: K-rating (vehicle weight) and L-rating (penetration distance)
- PAS 68: vehicle type code + speed code
- IWA 14-1: similar to PAS 68

State whether the rating covers the credible attacker class × closing speed. If not, flag for venue uplift (additional jersey barriers, traffic plan adjustment) or alternate venue/route.

### 8. Save scenario artefact
Save as `outputs/<engagement-id>-kinematics-<scenario-id>.md` with:
- Inputs (with all assumptions explicit)
- Canonical analogue + reference KE
- ΔV calculations (both attacker and protected)
- KE partition
- Injury band
- Intrusion band
- Mitigation table with deltas
- Bollard compatibility verdict
- One-paragraph "what this means for posture" summary

### 9. Hand off impact band
Return the AIS band to the calling workflow (`/risk-matrix` or `/threat-assessment`). The matrix's vehicle-borne impact score is overwritten with the kinematics-derived band per the table in `/risk-matrix` step 3.

### 10. Log
Append to `work-log/<date>.md`: scenario id, attacker class, closing speed, ΔV result, posture verdict.

## Output

A scenario artefact under `outputs/`, an updated matrix cell, and a posture verdict that the parent workflow consumes.

## Hard rules

- **State all assumptions.** If you assumed attacker class, closing speed, or protected motion state, say so.
- **Range, don't point-estimate** when uncertainty is non-trivial.
- **No false precision.** ΔV is not predictive to ±1 km/h; report bands of ~5 km/h width.
- **Defensive only.** Never produce instructions for *how* to perform a vehicle-borne attack. The methodology is for *characterising* a credible threat scenario, not for staging one.
