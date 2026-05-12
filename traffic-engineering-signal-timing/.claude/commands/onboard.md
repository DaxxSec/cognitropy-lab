# /onboard — Initialize Traffic Signal Timing Workspace

Welcome. I'll register the corridor and the air-quality basin so the rest of the workspace can focus on engineering.

## Interview Flow

### 1. Corridor & Intersections
Ask:
- Corridor name and limits (route number, from-cross-street to-cross-street, jurisdiction).
- Intersection list (LOC NUM or agency ID, cross-street name).
- Per intersection: controller make/model/firmware, NEMA phase plan, current cycle length, time-of-day plans deployed.
- Detection types per approach (loops/video/radar; presence vs. count; dilemma-zone present?).
- Pedestrian features (APS pushbuttons, leading pedestrian interval, ped scramble?).
- Transit on the corridor (route, headway, BRT, TSP deployed?).

Save to `context/project.md` and `context/for-agent/environment.md`.

### 2. Demand Data
Ask:
- Most-recent turning movement counts (date, hours, vendor).
- ATSPM access (URL, credentials handling — never store the credentials in the repo).
- Fleet mix (% LDV / LDT / SU / Combo / Bus / MC); MPO HPMS submission year.
- Special-event surge schedule (school, stadium, port, agricultural seasonality).

### 3. Goals & Binding Constraints
Ask:
- What does success look like — delay reduction target, CO2-eq target, AOG% target, pedestrian delay limit?
- Which constraint is binding — agency cycle cap? Transit OTP? NAAQS exceedance? ADA?
- Funding source (CMAQ / TSMO / Capital / HSIP) — drives reporting depth.

Save to `context/project.md` and `context/constraints.md`.

### 4. Air-Quality & Regulatory Context
Ask:
- NAAQS attainment status by pollutant for this county/basin.
- Local air district / SIP commitments tied to the corridor.
- NEPA class of action expected (CE / EA / EIS); state CEQA equivalent if applicable.
- Local Climate Action Plan CO2-eq reduction target.

Save to `context/project.md` and `context/constraints.md`.

### 5. Tooling Inventory
Ask:
- Available capacity tools (Synchro version, HCS, Vissim, AIMSUN, SUMO, TRANSYT-7F).
- MOVES4 install path (or note "needs install"); EMFAC2021 if California.
- Python environment available for the Pareto inner loop.

Save to `context/for-agent/environment.md` and `context/for-agent/tools.md`.

## Post-Onboard Actions
1. Suggest a study-period schedule (AM, MD, PM, off-peak) based on declared peaks.
2. Recommend whether to begin with `/timing-baseline` (if data exists) or with manual model build (if not).
3. Create the initial analysis plan in `planning/plan.md` with the dated milestones.
4. Log the onboarding session in `work-log/`.
