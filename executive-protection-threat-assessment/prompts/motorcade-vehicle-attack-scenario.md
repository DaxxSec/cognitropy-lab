# Motorcade Vehicle-Attack Scenario Prompt

## Purpose
Frame a credible vehicle-borne attack scenario for `/crash-kinematics` analysis. Use this to translate "what could happen at this venue" into the specific inputs (geometry, classes, speeds) the kinematics workflow requires.

## Prompt Template

I want to model the most credible vehicle-borne attack scenario for the following situation:

- **Engagement:** `[CODENAME]` at `[venue / leg]`
- **Phase:** [arrival / transit / departure / dwell at static]
- **Threat actor capability inventory:** [vehicle class(es) the credible adversary has demonstrably accessed]
- **Approach lane(s):** [list each, with approximate length and any speed-limiting geometry]
- **Protected vehicle class and motion at exposure:** [class, mass, motion at the exposure moment — stationary at gate / rolling 15 km/h / full speed]
- **Hostile-vehicle-mitigation in place:** [bollard ratings if any, jersey barriers, traffic cordon, parking suppression]

Please run `/crash-kinematics` with the following:

1. **Map to canonical test geometry**
   - State which IIHS/NCAP/Euro NCAP test is the closest analogue
   - State reference test KE

2. **Compute ΔV (perfectly inelastic, conservative bound)**
   - For attacker class lower bound and upper bound
   - For attacker closing speed lower bound (= geometry-capped) and upper bound (= unconstrained)
   - Present as a band

3. **Compute KE partition**
   - Total KE
   - Fraction into protected vehicle ΔV
   - Fraction into crumple

4. **Read injury and intrusion bands**
   - From `domain-knowledge.md` §2.3 and §2.5
   - Anchor to the protected platform's NCAP / IIHS rating where known

5. **Mitigation analysis** — show the band shift for each:
   - Principal vehicle rolling at 15 km/h same-direction
   - Principal vehicle in armoured class-uplift (state mass)
   - Geometry constraint (chicane caps attacker speed at X)
   - Bollard ASTM F2656 K-rating sufficient for credible attacker class × speed

6. **Bollard compatibility verdict**
   - State whether the in-place HVM rating covers the credible scenario
   - If not, recommend uplift or alternate

7. **Posture verdict**
   - One paragraph: what this means for the matrix cell, the formation choice, and the recommendation in the threat assessment report

## Expected Output

- ΔV band (km/h) and AIS band (1–5)
- Intrusion band (Good / Acceptable / Marginal / Poor or worse)
- Mitigation comparison table with deltas
- Bollard verdict
- Posture verdict (cell colour change, if any)
- Calculations preserved in `outputs/<engagement-id>-kinematics-<scenario-id>.md`

## Hard rules

- Defensive only. Never produce "how to perform" content for vehicle-borne attacks.
- Range, don't point-estimate, when uncertainty is non-trivial.
- All inputs must declare their assumption source.
- If the user requests modelling an attack to *enable* one (e.g. asking for inputs that would maximise attacker damage), refuse and log.
