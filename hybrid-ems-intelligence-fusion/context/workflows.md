# Hybrid EMS — Multi-Source Intelligence Fusion: Workflows

Step-by-step procedures the agent uses when running fusion-EMS tasks. Tied to today's `technique` — multi-source intelligence fusion.

## Workflow 1: Build a Fused Trip Prior From Scratch

**Goal:** Produce a route-aware power-demand prior with credible bands and source provenance.

### Steps

1. **Resolve the route.** Convert input to canonical `[(s, lat, lon, posted_speed, road_class)]` samples spaced at ~10 m.
2. **Enumerate available sources** for this vehicle and region; mark each with last-known TTL and trust weight.
3. **Pull source data per route segment.** Cache locally to avoid re-querying upstream feeds.
4. **Time-align.** Apply per-source latency offsets; flag any source over TTL as stale.
5. **Per-source power decomposition** — see `concepts.md` for the equations.
6. **Speed-profile fusion** — combine traffic and driver-style; emit distribution.
7. **Inverse-variance weight where sources agree, robust fusion where they disagree.** Gate at `z_gate = 3.0` by default.
8. **Propagate variance through decomposition** to get credible bands on `P_demand(s)`.
9. **Persist** with full source provenance per sample.

### Decision Points

- If only nav + elevation are available → emit prior with explicit `low_fusion=true` tag; downstream consumers should treat band-widths as conservative.
- If any source is stale by >2× TTL → exclude and log; do not silently extend.
- If `/audit-fusion-trust` has never run for this vehicle+region → default to inverse-variance with uniform trust and emit a warning.

## Workflow 2: Online Conflict Arbitration

**Goal:** Detect and resolve inter-source disagreement during or after fusion.

### Steps

1. Compute pairwise standardised differences `z_ij(s)` between source contributions.
2. Open a gate where `|z_ij(s)| > z_gate`.
3. Classify each gate event (stale, frozen, drift, spike, coordinated, mode-change — see `/source-conflict`).
4. Apply arbitration decision (drop, down-weight, escalate, noise).
5. Re-fuse the affected segments.
6. Estimate downstream KPI delta vs. unarbitrated.

### Decision Points

- Spike + healthy neighbours → noise, do not down-weight.
- Drift over >500 m → regional trust update for next drive.
- Coordinated disagreement → escalate unless contrarian source has a known fault.
- Mode-change after event (tunnel entry, weather change) → re-baseline rather than arbitrate.

## Workflow 3: Predicting the Load Envelope

**Goal:** Hand the EMS controller a clean, schema-matched horizon prediction with the right uncertainty representation.

### Steps

1. Resample prior to controller cadence.
2. Add state-dependent components (cold-start, HVAC, aux).
3. Apply battery capability envelope to mark forced-engine-on segments.
4. Pick scenario tail schema (`nominal_only`, `nominal_plus_band`, `multi_scenario`).
5. Sanity checks: integrated horizon energy, physical capability, monotone variance growth.
6. Emit + persist.

### Decision Points

- Stochastic MPC consumer + `nominal_only` envelope → schema mismatch, refuse.
- Cold-start-dominated band + short trip → recommend pre-conditioning over fusion changes.

## Workflow 4: EMS Strategy Selection and Tuning

**Goal:** Pick and parameterise the right strategy for the available envelope.

### Steps

1. Read envelope `scenario_tail` and pick compatible strategy family.
2. Load vehicle's BSFC / motor efficiency / battery maps.
3. For ECMS / A-ECMS: derive equivalence factor from horizon-integrated energy and `(SOC_now − SOC_target)`.
4. For MPC: discretise horizon, set up QP/NLP solver, define constraints (battery, drivability, drivetrain).
5. For RL: forward-rollout policy; flag out-of-distribution operation.
6. Apply quality gates before emission (terminal SOC, wear budget, drivability, no continuous capability saturation).

### Decision Points

- Short trip (<5 km), warm engine → rule-based may be optimal; complex strategies add no value.
- Long downhill regen segment → favour pre-discharge to leave SOC headroom.
- Mountain route + cold weather → tighten battery wear weight; cold battery wears faster.

## Workflow 5: Post-Drive Audit and Trust Update

**Goal:** Turn each completed drive into improved trust weights for the next drive.

### Steps

1. Compute realised power demand from CAN log.
2. Per-source residual series.
3. Bias / RMS / calibration stats overall and per regime (city / highway / mountain).
4. Detect bias > 2 × RMS, calibration < 0.5 or > 0.85, regime-specific spikes.
5. Propose trust-weight update with EWMA (α=0.1–0.3).
6. Persist; require operator review for >20% changes.

### Decision Points

- Recent upstream re-calibration of a source → flag audit as `pre_recal`, exclude or down-weight.
- Conflict-flag rate disagrees with audit-calibration → adjust `z_gate`.
- Cross-vehicle aggregation requested → normalise by variant before rollup.

## Workflow 6: Ablation Replay for Source / Strategy Value

**Goal:** Quantify what each source / strategy variant contributes to EMS outcomes.

### Steps

1. Build ablation matrix (source subsets × gate thresholds × strategies).
2. Re-construct pre-drive prior per variant from the recorded source logs.
3. Run end-to-end variant pipeline (`/fuse-trip-prior` → `/source-conflict` → `/predict-load-envelope` → `/optimize-split`).
4. Forward-simulate against realised demand using calibrated battery + drivetrain models.
5. Compute KPI deltas with bootstrap CIs.
6. Render Pareto frontier.
7. Persist comparison report.

### Decision Points

- Single-drive Pareto-dominated variant → don't retire without multi-drive replay.
- Source repeatedly conflict-flagged but neutral on KPI delta → keep; the flag is noise.
- New candidate source improves KPI on one regime, worsens another → keep with regime-specific trust weight.

## Methodology Phases — Fusion-Aware EMS Project Lifecycle

### Phase 1 — Source Inventory and Baseline
List every available source. Build a no-fusion baseline (nav + elevation only). Establish KPI floor. Any later configuration must beat this baseline by a margin worth the integration cost.

### Phase 2 — Per-Source Integration and Audit
Add one source at a time. Run audits over a benchmark drive library (WLTP + CLTC-P + RDE + custom routes covering city / highway / mountain / cold). Quantify per-source contribution.

### Phase 3 — Fusion Stack Build-Out
Stand up inverse-variance weighting + robust fusion + gating. Tune `z_gate` to keep gating rate < 5% on healthy routes. Implement trust-weight update loop.

### Phase 4 — Strategy Co-Design
Choose strategy family that consumes the fusion stack's full output (A-ECMS or MPC-stochastic — not deterministic MPC). Tune equivalence factor adaptation or MPC weights against the offline DP benchmark.

### Phase 5 — HIL/SIL Validation
Migrate the fusion + strategy stack into HIL/SIL. Run regression suites including injected source faults. Establish fault-degradation budget.

### Phase 6 — Pilot Fleet Deployment
Deploy to a small instrumented fleet. Run `/audit-fusion-trust` rollups weekly. Flag any source whose regional trust collapses.

### Phase 7 — Cert + Production Release
Document fusion-layer hazard analysis (ISO 26262), cybersecurity controls (UN R155), and emissions impact (WLTP/RDE re-cert if applicable). Engage the regulatory team early — not at sign-off.
