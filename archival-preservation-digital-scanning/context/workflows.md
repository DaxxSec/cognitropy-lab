# Archival Preservation Digital Scanning — Workflows and Methodology

Procedures and decision trees the agent runs. Centered on today's technique — **resource optimization algorithms** — applied across the digitization pipeline. `concepts.md` says *what things are*; this file says *what the agent does with them*.

## The Pipeline (end-to-end)

```
intake → triage condition → prioritize (optimize) → schedule (optimize)
       → spec capture profile → capture → QA → package (AIP) → preserve (fixity)
                                                        └→ derive access deliverables
```

Optimization sits at two gates (prioritize, schedule) and informs two more (forecast, cost). Preservation craft owns the rest. They interlock: condition triage feeds handling multipliers into prioritization and scheduling; QA reject rates feed back into the forecast.

## Workflow 1: Optimize the digitization priority queue

**Goal:** select and order the lots that maximize preserved value under fixed capacity.

### Steps
1. Normalize every lot to estimated images (throughput table in `references.md`); reject rows missing condition or rights.
2. Score weighted value `V = 0.40·preservation_urgency + 0.30·access_demand + 0.20·uniqueness − 0.10·rights_risk` (each factor normalized 0–1; weights are an explicit, overridable policy).
3. Estimate cost in capture-hours = `images × per-image-time × condition-handling-multiplier`.
4. Solve 0/1 knapsack: maximize Σ V subject to Σ cost ≤ capacity (DP if ≤ ~few hundred lots; else greedy `V/cost` with stated optimality gap).
5. Pin active-decay lots to the front (urgency override), then order the rest by value density.
6. Re-solve at 80% and 120% capacity for the stakeholder sensitivity table.

### Decision Points
- If a lot is actively decaying: **pin to front**, bypass the knapsack ranking.
- If condition or rights is missing: hold the lot out until resolved — do not guess.
- If > ~few hundred lots: use greedy and report the optimality gap rather than waiting on exact DP.

## Workflow 2: Minimize makespan across capture stations

**Goal:** clear the selected batch in the least wall-clock time without violating equipment or handling constraints.

### Steps
1. Build the (lot × station) compatibility matrix from material type, max size, and operator certification.
2. Compute per-station durations = `images / station_throughput_for_material`, inflated by handling multipliers.
3. Schedule with LPT (longest jobs first), then local-search swaps that reduce the max-loaded station (R||Cmax is NP-hard — heuristic + bounded gap).
4. Honor pins (color-managed sets on one station) and deadlines first; surface any deadline that can't be met.
5. Report per-station utilization; flag bottleneck (> 90%) and idle (< 50%) stations with one rebalancing move.
6. Reserve target-chart shots at shift start and a daily calibration/maintenance block.

### Decision Points
- If one oversized/fragile/color-critical lot dominates makespan: split or outsource it rather than reshuffling everything.
- If a deadline can't be met: escalate the conflict; do not silently slip.
- After day 1: replace estimated throughput with measured rates and re-run.

## Workflow 3: Forecast backlog drawdown

**Goal:** answer "when will we be done?" and "what would more capacity buy?" honestly.

### Steps
1. Service rate = throughput × productive hours × stations × **utilization discount** (~0.60–0.75, never 1.0).
2. If accessions keep arriving, model as M/M/c: check stability `ρ = λ/(c·μ) < 1`.
3. Drawdown months = `backlog / (service_rate − arrival_rate)`; add the QA reject-rate rework adjustment.
4. Run scenarios (add station/shift, outsource, hire); express results as months saved and Δcost per month saved.
5. Report optimistic/expected/pessimistic from the utilization range — never single-point false precision.
6. Name the binding constraint: capacity-bound, prep-bound, or QA-bound.

### Decision Points
- If `ρ ≥ 1`: the backlog never clears at current capacity — report the stability gap, not a date.
- If reject rate > ~10%: fix QA/capture before trusting any forecast (rework dominates).

## Workflow 4: Capture → QA → package (the preservation core)

**Goal:** produce trustworthy, standard-conformant masters and turn them into AIPs.

### Steps
1. `/spec-capture-profile` per material class: standard + level, resolution, bit depth, color space, target charts, file outputs, conformance checklist.
2. Capture, shooting the target chart per the profile's cadence.
3. `/audit-image-quality`: analyze the chart (OECF, ΔE, SFR/MTF, uniformity, noise) against tolerances; decide per-image pass/rescan and per-batch verdict.
4. Route rejects grouped by root cause; correct the capture chain once, not image-by-image.
5. `/assemble-aip-package`: generate derivatives, capture MIX technical + PREMIS provenance, build the METS structure, compute SHA-256 fixity, bag and validate.
6. Start the fixity regime with `/audit-fixity-integrity`.

### Decision Points
- If the **target chart fails**: the whole session is suspect — fix the chain and reshoot, never cherry-pick images.
- If metric drift is trending (not a hard fail yet): investigate lamp aging / stale profile before it costs a day.
- If rights are cleared and access is needed: branch to `/derive-access-deliverables`; otherwise dark-archive.

## Methodology note — keep optimization honest

- **Measure, then re-optimize.** Every optimization (queue, schedule, forecast) is seeded with estimates and converges as measured rates replace them. Re-run on real data.
- **Hard gates beat heavy weights.** Preservation urgency and no-transit custody are encoded as overrides/gates, not as large coefficients that money could outvote.
- **Surface the policy.** Weighting choices and capacity assumptions go in the output so stakeholders see (and can challenge) the trade-offs, not just the ranking.
