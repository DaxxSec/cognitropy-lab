# Core Workflows — Signal Timing with Environmental Impact Assessment

## Workflow 1: Baseline Performance Characterization

**Goal:** Quantify what the corridor is doing today on every dimension that matters.

### Steps
1. **Inventory.** Confirm intersection list, controller make/model/firmware, NEMA phase plan, detection types per approach, lane geometry. Save to `context/for-agent/environment.md`.
2. **Pull existing timing.** Acquire current cycle, splits, offsets, time-of-day plans from controller logs (preferred) or as-builts. ATSPM "Split Monitor" gives the running record over the past N days; the official plan is the spec.
3. **Get demand.** Turning-movement counts (TMCs) for AM/MD/PM/off-peak, ideally 13-hour or 7+9-hour count days. If no TMCs, derive from ATSPM detector volumes + classification ratios.
4. **HCM 7 capacity model.** Build the lane-group flow ratios `y_i = v_i / s_i`. Compute v/c for each critical lane group, control delay per HCM 7 Eq. 19-22, LOS per Exhibit 19-8.
5. **Field validation.** Spot-check modeled queue lengths and delays against ATSPM PCDs and floating-car runs (3+ runs each direction per peak).
6. **Baseline emissions.** Run `/emissions-model` on baseline using CMEM modal lookup; save inventory by pollutant per intersection per peak.
7. **Document.** Save baseline to `outputs/baseline-{date}.md` with delay, LOS, fuel, CO2, NOx, PM2.5, PM10, AOG%, ped delay, queue length.

### Decision Points
- If detector data unavailable: use TMC + HCM defaults but flag uncertainty in the report.
- If ATSPM exists but is mis-configured (phantom calls, miscoded detectors): fix or exclude from the analysis explicitly.
- If TMCs are > 18 months old in a growing corridor: get a fresh count or apply a documented growth factor.

## Workflow 2: Multi-Objective Cycle / Split Optimization

**Goal:** Generate a Pareto frontier of cycle/split candidates trading delay against environmental cost.

### Steps
1. **Bound the search.** Cycle range typically 60–150 s in 5 s increments; split range subject to minimum-green and ped-clearance constraints.
2. **Webster bootstrap.** Compute Webster's optimal cycle as the seed; use as the centerpoint of the search.
3. **Inner loop (CMEM).** For each candidate (C, splits) within constraints:
   a. Solve HCM 7 capacity for v/c, delay, queue.
   b. Convert delay → CMEM stops + idle + accel cycle counts.
   c. Compute CO2, NOx, fuel from CMEM modal lookup.
   d. Score on objective vector `[delay, CO2, NOx, PM2.5, fuel, noise]`.
4. **Pareto filter.** Drop dominated candidates; keep frontier.
5. **Constraint check.** Drop any candidate violating MUTCD ped, MUTCD yellow, agency cycle cap, or v/c > 0.95 anywhere.
6. **Visualize.** Plot frontier on delay × CO2 axes (Pareto curve), color by NOx tier. Save to `outputs/pareto-{peak}-{date}.png`.
7. **Recommend.** Pick the knee-point (Kneedle algorithm) or the user's binding-constraint point; document why.
8. **Re-run finalist on MOVES.** CMEM is fast but MOVES is the regulatory deliverable; re-run the chosen plan and ≤ 2 alternatives on MOVES4 for the report.

### Decision Points
- If the frontier collapses to a single point: cycle is constrained by minimums; consider geometric or demand fix instead.
- If two points have equal delay but different CO2: pick lower CO2 unless a non-emissions reason (transit OTP) overrides.
- If user has a NAAQS exceedance constraint: filter frontier first by NOx ceiling, then optimize delay within that subset.

## Workflow 3: Corridor Coordination Design

**Goal:** Build a green-wave coordination plan across 3+ adjacent signals with emissions-weighted bandwidth.

### Steps
1. **Identify the coordinated phase.** Usually the heaviest through movement; verify with O-D survey or Bluetooth re-ID data.
2. **Pick a common cycle length.** Coordination requires a single cycle (or integer-divisor double-cycle). Use the longest critical-intersection cycle from Workflow 2 as the controlling value.
3. **Compute target speed.** Posted speed is a starting point; field-measured 85th percentile is better; for CO2-min, target 5–7 mph below the lower of those (Barth & Boriboonsomsin 2009).
4. **Solve for offsets.** Maxband / Multiband LP via TRANSYT-7F, Synchro Optimizer, or PuLP. Objective augmented with `–alpha * sum(stops * CO2_per_stop)`.
5. **Time-space diagram.** Plot bands; verify both directions get acceptable bandwidth (typically ≥ 30% of cycle).
6. **Stress test.** Vary platoon dispersion factor; verify band still serves the platoon under realistic dispersion.
7. **TSP / EVP overlay.** If transit signal priority deployed, model the green-extension distribution to ensure coordinated phase recovers on the next cycle.
8. **Emissions delta.** Run `/emissions-model` against baseline (uncoordinated) and coordinated. Document corridor-level CO2/NOx/fuel deltas.

### Decision Points
- If two adjacent signals are > 0.5 mi apart: platoon disperses; coordination yields little benefit; let them run free.
- If cross-street volumes are very high: cap bandwidth at the value that holds cross v/c < 0.9.
- If posted speed differs by > 10 mph between segments: split coordination into sub-corridors.

## Workflow 4: Project-Level MOVES Emissions Inventory

**Goal:** Produce SIP/CMAQ-grade emissions estimates for the recommended plan.

### Steps
1. **Build link table.** Each lane-group movement at each intersection becomes a link with: link-ID, length, average speed, source-type fractions, road-type, time-of-day.
2. **Drive schedule.** From microsimulation (Vissim/SUMO) export second-by-second speed traces per link; aggregate to MOVES-compatible operating-mode bin distributions.
3. **Fleet mix.** From local MPO HPMS submission or default MOVES4 county-level fleet; document source.
4. **Meteorology.** County-month average T, RH from EPA defaults or NOAA local.
5. **Run MOVES4 project-level scale.** Outputs g/hr per pollutant per source-type per link.
6. **Aggregate.** Convert to corridor-level totals per peak, then annualized via time-of-day factors.
7. **Compare to baseline.** Δ for CO, NOx, VOC, PM2.5, PM10, CO2-eq.
8. **Document methodology.** MOVES version, input year, fleet source, drive-schedule source — attach as appendix to `/report-eia` output.

### Decision Points
- For CMAQ application: include both annualized and peak-hour deltas.
- For NEPA Categorical Exclusion documentation: a CMEM-only estimate may suffice; coordinate with FHWA division early.
- For SIP/conformity in a non-attainment area: MOVES4 (or EMFAC2021 in CA) is mandatory.

## Workflow 5: NEPA / CEQA Environmental Impact Assessment

**Goal:** Produce a defensible, citable environmental finding for a retiming project.

### Steps
1. **Class of action.** Most retiming is CE under 23 CFR 771.117(c)(28). Confirm with FHWA division; document if CE applies.
2. **Air quality finding.** Cite the calculated emission deltas (Workflow 4); compare to NAAQS standards; note SIP conformity status.
3. **Climate finding.** CO2-eq delta against agency Climate Action Plan target if applicable.
4. **Noise finding.** Sound-pressure delta from reduced acceleration events; spot-check against noise ordinance limits.
5. **Environmental Justice screen.** EPA EJScreen check on corridor-adjacent census blocks; ensure benefits/burdens equitably distributed.
6. **Public engagement.** Note any required public comment period (generally not for CE, may be for state CEQA).
7. **Assemble report.** Use FHWA CE template with custom air-quality and climate appendices. Save to `outputs/eia-{corridor}-{date}.pdf`.

### Decision Points
- If emission delta is positive (worse) on any pollutant in non-attainment basin: redesign or document mitigation.
- If a sensitive receptor (school, hospital, senior facility) is on the corridor: include a focused exposure analysis.
- If the corridor crosses jurisdictions: each may require its own state-level finding.
