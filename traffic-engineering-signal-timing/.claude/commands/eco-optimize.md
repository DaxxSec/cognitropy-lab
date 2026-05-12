# /eco-optimize — Multi-Objective Cycle / Split Tuning

Generate the Pareto frontier of timing candidates trading delay against environmental cost. Produces a frontier plot and a knee-point recommendation.

## Required Inputs
- Validated baseline from `/timing-baseline`
- HCM 7 capacity model in memory (or saved structure)
- CMEM modal coefficients from `resources/cmem-modal-fuel-rates.md`
- Constraint set:
  - Min cycle (typically max(60 s, max-walk + clearance + min-cross + lost time))
  - Max cycle (agency policy; commonly 120–150 s)
  - Min green per phase (MUTCD ped where applicable, NACTO bike)
  - Max v/c ceiling (typically 0.95)

## Procedure

### 1. Define Search Space
- Cycle: `[C_min, C_max]` in 5 s increments.
- Splits: discretize to 1 s; satisfy ring/barrier sums.
- Reject any (C, splits) violating min-green or ped-clearance constraints up front.

### 2. Webster Bootstrap
Compute `C_W = (1.5 * L + 5) / (1 - sum(y_i))` and use as the centerpoint of the search. Document.

### 3. Inner Loop (Per Candidate)
For each `(C, splits)` in the feasible set:
a. Compute v/c per HCM 7 for every critical lane group.
b. Compute control delay per HCM 7 Eq. 19-22.
c. Estimate per-vehicle stops `S = (1 - g/C) / (1 - min(1, X) * g/C)`.
d. Translate to CMEM modal time fractions (idle, accel, cruise, decel) using approach speed and stops.
e. Look up CMEM modal rates per fleet weight (`resources/cmem-modal-fuel-rates.md`); produce per-link CO, NOx, VOC, PM2.5, CO2, fuel.
f. Sum to corridor totals.
g. Estimate Leq noise from accelerating-vehicle count + truck %.
h. Append `[C, splits, delay, CO2, NOx, PM2.5, fuel, noise, v/c_max]` to the candidate set.

### 4. Pareto Filter
- Sort by delay ascending.
- Sweep keeping only non-dominated candidates across the objective vector `[delay, CO2, NOx, PM2.5, fuel, noise]`.

### 5. Constraint Check
Drop any frontier candidate violating:
- v/c > 0.95 anywhere
- Pedestrian phase < walk + clearance
- Yellow + red < ITE recommended
- Agency cycle cap

### 6. Visualize
Plot the frontier on `(delay, CO2)` axes; size markers by NOx, color by PM2.5. Annotate the Webster point and the baseline point. Save to `outputs/pareto-{peak}-{date}.png`.

### 7. Recommend
- Knee-point detection (Kneedle algorithm) to surface the geometric balance.
- If a binding constraint exists (NAAQS NOx ceiling, transit OTP), filter first then pick min-delay within the subset.
- Document the chosen plan with rationale.

### 8. Re-run on MOVES4
Hand the chosen plan + ≤ 2 alternates to `/emissions-model --moves` for the regulatory deliverable. CMEM is the inner loop, MOVES is the report.

### 9. Output
Save to `outputs/eco-optimize-{peak}-{date}/`:
- `frontier.csv` — all Pareto candidates
- `frontier.png` — visualization
- `recommended.md` — chosen plan, rationale, expected delta vs. baseline
- `alternates.md` — runner-up plans for sensitivity discussion

### 10. Log
Append to `work-log/{YYYY-MM-DD}.md` with the candidate count, the Webster point, the chosen plan, and any constraint that pruned candidates.
