# /report-eia — NEPA/CEQA-Style Environmental Impact Assessment

Produce a defensible, citable environmental finding for a recommended timing plan, suitable for FHWA Categorical Exclusion documentation, CMAQ application, or state CEQA equivalent.

## Required Inputs
- Recommended plan from `/scenario-compare`
- MOVES4 (or EMFAC2021 in CA) results for the recommended plan and baseline
- Sensitive-receptor inventory along the corridor (schools, hospitals, senior facilities, residences within 200 ft)
- Local air-quality basin attainment status by pollutant
- Local Climate Action Plan target if applicable
- EPA EJScreen pull for corridor-adjacent census blocks

## Procedure

### 1. Class of Action
- Confirm with FHWA division: most retiming qualifies as a CE under 23 CFR 771.117(c)(28) (operational/ITS).
- Document threshold checks (no acquisition of significant land, no significant air-quality impact, no historic/cultural impact).

### 2. Air-Quality Finding
For each criteria pollutant:
- **Baseline:** corridor emission inventory (kg/day or lb/day per pollutant).
- **Project:** corridor emission inventory under recommended plan.
- **Delta:** project − baseline (sign convention: negative = beneficial).
- **NAAQS context:** state attainment status; cite the relevant SIP commitment if non-attainment.
- **Conformity finding:** for non-attainment / maintenance areas, document conformity per 40 CFR Part 93 Subpart B.

### 3. Greenhouse Gas Finding
- Annualized CO2-eq delta (t-CO2-eq/yr).
- Comparison to local Climate Action Plan reduction target (% of corridor's notional share).
- Equivalents (passenger-cars-off-road, gallons-of-gasoline-not-burned).

### 4. Noise Finding
- Spot-check Leq dB(A) at sensitive receptors before vs. after.
- If reduction > 3 dB or absolute level changes class (e.g., from "Moderate" to "Low"), call it out; otherwise note de minimis.
- Comparison to local noise ordinance limits if residential adjacency.

### 5. Environmental Justice Screen
- Pull EPA EJScreen for census blocks within 0.25 mi of the corridor.
- Identify any block in 80th-percentile or higher for environmental burden + low-income/minority demographics.
- Document distribution of project benefits (delay reduction, emission reduction, ped service) across these blocks.
- If burden falls on EJ communities while benefits flow elsewhere, flag and propose mitigation.

### 6. Pedestrian / Bicycle / Transit Finding
- Compare ped delay, ped LOS, bike-friendly green, transit OTP (if TSP).
- Document ADA compliance; APS, walk-clearance, accessible-pedestrian-signal coverage unchanged or improved.

### 7. Cumulative Impacts
- Identify other planned corridor projects (capital, signal, transit) within ~1 mi or upstream/downstream.
- Document interaction (does this retiming complement or conflict with the planned BRT?).

### 8. Mitigation (if needed)
- If any impact dimension worsens beyond de minimis, propose mitigation.
- Common mitigations: enhanced ped countdown timer, leading pedestrian interval (LPI), bike box, additional detection.

### 9. Public Engagement Note
- CE generally not subject to public comment, but document any informal stakeholder outreach.
- State CEQA may require notice of intent — flag and route to the appropriate agency liaison.

### 10. Assemble Report
Use FHWA CE Documentation Toolkit format. Sections:
1. Project Description (corridor, intersections, timing change, study period).
2. Purpose & Need (delay, environmental drivers, funding context).
3. Alternatives Considered (no-build, recommended, alternates).
4. Environmental Impact Findings (sections 2–7 above).
5. Mitigation (if any).
6. Conclusion / CE Determination.
7. Appendix A: MOVES4 methodology and inputs.
8. Appendix B: EJScreen pull.
9. Appendix C: HCM 7 capacity worksheets.

Save to `outputs/eia-{corridor}-{date}.md` (or .pdf via `pandoc`).

### 11. Log
Append to `work-log/{YYYY-MM-DD}.md` with the CE/EA/EIS determination, the air-quality finding sign, and the routing destination (FHWA division, state DOT, MPO).
