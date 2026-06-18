# Amorphous Metal Bulk Glass Formation — Workflows and Methodology

What the agent *does* with the concepts. Every workflow ends in a capacity statement backed by a kinetic margin (`concepts.md` = the physics; this file = the procedure). Technique lens: **capacity planning models**.

## Workflow 1: Plan an Amorphous-Metal Production Run (the master loop)

**Goal:** Turn a demand forecast + candidate alloy(s) into a defensible "good parts per period" plan with the binding constraint named.

### Steps
1. **Forecast & geometry.** List products, their demand over the period, and each part's **minimum-cooling section** (the thickest spot that must stay amorphous).
2. **Thermal landmarks.** For each alloy, run `/dsc-landmarks` (Tg, Tx, Tm, Tl, ΔTx) and `/kissinger-kinetics` (Ea, n, K₀) — the inputs every downstream model needs.
3. **GFA → castability.** Run `/gfa-assess` to score Trg/ΔTx/γ and estimate Rc and Dmax. Map products to alloys: a product is *castable* only if its min-cooling section < Dmax.
4. **Cooling/forming budgets.** `/cooling-budget` confirms the mold beats Rc with margin for cast parts; `/tpf-window` sets the per-heat time budget for thermoplastically-formed parts.
5. **Yield.** `/crystallization-yield` predicts crystalline fraction at the critical location → first-pass yield per product.
6. **Throughput & bottleneck.** `/line-throughput` combines cycle times + yield → good-parts/hr and the constraint (machine vs crystallization clock).
7. **Reconcile to demand.** `/product-mix-plan` allocates constrained capacity across the forecast; flag products that don't fit and propose alloy/geometry changes.
8. **QA load.** `/amorphicity-qa` sets a sampling plan sized so verification doesn't become the new bottleneck.

### Decision Points
- If **min-cooling section > Dmax** for every available alloy → product is infeasible as cast; redesign geometry, switch to higher-GFA (often costlier) alloy, or decline.
- If the **bottleneck is the crystallization clock** (TPF window / quench), efficiency programs on machines won't help — elevate the *kinetic* constraint (lower Tl via composition, raise cooling rate, widen ΔTx).
- If **yield variance is oxygen-driven**, treat melt prep (`/melt-flux-spec`) as the capacity lever, not the press.

## Workflow 2: GFA Screening Decision Tree (alloy down-select)

**Goal:** Rank candidate compositions by castable thickness before committing melt time.

### Steps
1. Gather Tg, Tx, Tl for each candidate (DSC or literature).
2. Compute Trg, ΔTx, γ (and γm/δ if borderline).
3. Rank by γ and Trg primarily; use ΔTx to break ties when thermoplastic forming is planned.
4. Cross-check against the representative table in `references.md` — a γ near a known Dmax anchors the thickness estimate.
5. Down-select to the 1–3 alloys whose estimated Dmax covers the product geometries.

### Decision Points
- If **two parameters disagree** (e.g. high Trg but small ΔTx) → high Trg favours casting thickness; small ΔTx warns the supercooled liquid is unstable → poor for TPF. Choose by *process route*.
- If all candidates fall below threshold → no down-select; report "no adequate glass-former for this geometry" and escalate to composition design.

## Workflow 3: Thermoplastic-Forming (TPF) Window Determination

**Goal:** Find the forming temperature and the seconds-per-heat budget that maximise throughput without crystallizing the part.

### Steps
1. From `/kissinger-kinetics`, build K(T) for crystallization onset across the supercooled-liquid region (Tg → Tx).
2. For each candidate forming temperature T_form, compute the **time-to-onset** t_x(T_form) from JMAK at a small allowable crystalline fraction (e.g. X = 1%).
3. Subtract the required forming time (fill/emboss/blow time) → **time margin**. Net margin > 0 means feasible.
4. Trade-off: higher T_form → lower viscosity (faster fill, easier feature replication) **but** shorter t_x. Pick the T_form that maximises (parts per heat) = floor(t_x / cycle-per-part) while keeping margin.
5. Express as a per-heat capacity: parts/heat × heats/hr = TPF station rate.

### Decision Points
- If even the lowest T_form gives t_x < forming time → the alloy's supercooled liquid is too unstable for TPF; switch alloy (larger ΔTx) or process route (as-cast net shape).
- If viscosity at the safe T_form is too high to fill features → the part needs a wider ΔTx alloy, not a hotter, riskier hold.

## Workflow 4: Crystallization-Clock Bottleneck Loop (TOC's five focusing steps, kinetics edition)

**Goal:** Raise line capacity by attacking the true constraint, iteratively.

### Steps (the five focusing steps, specialised)
1. **Identify** the constraint via `/line-throughput`: is it a machine station, or the crystallization clock (quench Rc margin / TPF window)?
2. **Exploit** it: if kinetic, run every cast/form at the *fastest safe* cooling and the *optimal* T_form; if a machine, minimise its changeover/idle.
3. **Subordinate** everything else to the constraint: stage melts, buffer WIP (Little's Law) so the constraint never starves or blocks.
4. **Elevate** the constraint: kinetic → composition tweak to lower Tl / widen ΔTx, better mold heat extraction, fluxing; machine → add a station.
5. **Repeat** — once elevated, the bottleneck usually moves (often to QA); re-run `/line-throughput` and `/amorphicity-qa`.

### Decision Points
- If elevating the kinetic constraint forces a costlier alloy → take it back to `/product-mix-plan` as a cost-vs-capacity trade, not a unilateral metallurgy decision.

## Methodology Phases — Yield Diagnosis (when capacity drops without a process change)

### Phase 1 — Localize
Is the crystallinity at the surface (oxide skin / nucleation) or the centre (cooling-rate / thickness)? `/amorphicity-qa` on sectioned samples answers this.

### Phase 2 — Attribute
Surface/skin → oxygen or nucleant regression → `/melt-flux-spec`. Centre → cooling-rate loss → `/cooling-budget` (mold decay) or a section/geometry change.

### Phase 3 — Quantify & contain
`/crystallization-yield` re-estimates yield with the suspected cause's parameters; confirm the gap matches the observed drop, fix the input, and tighten sampling until yield recovers, then relax the plan back to steady-state.
