# Satellite Communication Protocols — Workflows and Methodology

How the agent actually designs a link, tied to today's technique: **cost-benefit analysis frameworks**. `concepts.md` says what the pieces are; this file says what to *do* with them. The spine is a seven-phase pipeline; the workflows below are the procedures inside it.

## Methodology Phases — Define → Budget → Bound → Audit → Optimize → Allocate → Commit

### Phase 1 — Define
Capture mission geometry, band, and the two targets (rate, availability) plus the quality floor. Fix the optical train's stages (`/open-link-budget`). Nothing is "tunable" until its controlling lever is named.

### Phase 2 — Budget
Trace the cascade in dB to a margin number (`/cascade-budget`). Keep clear-sky and rain-faded columns side by side. A budget that doesn't close yet is fine — it tells you how many dB you are shopping for.

### Phase 3 — Bound
Compare the achieved efficiency to Shannon (`/shannon-gap`). This sets the Strehl and, crucially, the **regime** — power-limited vs bandwidth-limited — which decides which levers cost-benefit will favor.

### Phase 4 — Audit
Decompose implementation loss into aberrations and price each corrector (`/aberration-audit`). Often the cheapest dB is here, in software, not in hardware.

### Phase 5 — Optimize
Rank every lever by marginal dB-per-dollar and walk each to its knee (`/aperture-tradeoff`, `/modcod-pareto`). Buy dB from the cheapest source until the margin gap closes.

### Phase 6 — Allocate
Decide how much margin to hold and against what (rain, pointing, aging, interference), and whether static margin, ACM, or diversity buys availability cheapest (`/rain-margin-economics`). Consider an optical crosslink where it dominates (`/optical-crosslink-eval`).

### Phase 7 — Commit
Gate-check, justify every lever, run sensitivity, and lock the prescription with provenance (`/commit-design`).

---

## Workflow 1: Full Budget Cascade + Capacity Gap

**Goal:** A closed link budget with its distance-from-Shannon quantified.

### Steps
1. Trace EIRP → FSPL → atmosphere → G/T → C/N₀ → Es/N₀ → Eb/N₀, carrying a running total after each stage.
2. Subtract implementation loss (from the aberration audit) before computing final margin.
3. Compute Shannon `η_max = log₂(1+SNR)` and the capacity Strehl `η_ach/η_max`.
4. Classify the regime and name where the cheapest dB lives.

### Decision Points
- If **margin ≥ target** and **Strehl ≈ 1**: the link is well-designed — check for *over*-design before adding anything.
- If **margin < target** and **power-limited**: shop dB from aperture / G/T / power (Workflow 2).
- If **margin < target** and **bandwidth-limited**: a higher-order MODCOD or more bandwidth is the cheaper buy (Workflow 3 / `/modcod-pareto`).

## Workflow 2: Marginal dB-per-Dollar Lever Sweep

**Goal:** Close a margin gap at minimum cost.

### Steps
1. List the candidate levers and their marginal-benefit law (dish ∝ D², power +1 dB/dBW to saturation, G/T per −ΔK, software correctors per the audit).
2. Attach a marginal cost ($, and kg/W where binding) to each.
3. Sort by **dB-per-dollar**; buy from the top until the gap closes or the lever hits its knee/constraint.
4. Re-run Workflow 1 to confirm the new margin and that no narrowed beamwidth re-opened a pointing-loss gap.

### Decision Points
- If a **software corrector** beats hardware on $/dB: fix the aberration first.
- If the **next dB-per-dollar** falls below the next-best lever: stop on that lever, switch.
- If a **hard constraint binds** (EIRP/PFD limit, mass, HPA saturation, un-pointable beam): that lever is exhausted regardless of cost.

## Workflow 3: Availability and Margin Economics

**Goal:** Meet the *economically justified* availability, not blindly the requested one.

### Steps
1. Build the rain fade-exceedance curve (ITU-R P.618) and read the dB needed per availability target.
2. Price each dB three ways — static margin, ACM, site diversity — including the clear-sky opportunity cost of static dB.
3. Compute expected annual outage cost and the **marginal $ per nine**; find where the next nine costs more than the outage it prevents.
4. Recommend the cheapest mitigation mix to the justified availability; flag gold-plating above it.

### Decision Points
- If fades are **deep but infrequent** (Ka/Q/V): ACM usually beats static margin.
- If the band is **high and a second site is affordable**: diversity decorrelation often beats both.
- If the **marginal $ per nine > outage cost prevented**: stop below the requested availability and say so.

## Workflow 4: RF-vs-Optical Crosslink Decision

**Goal:** Choose RF, free-space optical, or hybrid for a given hop.

### Steps
1. Build both budgets in the same cascade form for the hop.
2. Quantify the optical pointing (PAT) cost/risk and the weather-availability hit for space-to-ground.
3. Compare capacity gained vs SWaP/$ spent vs availability and licensing delta.

### Decision Points
- If the hop is **inter-satellite (vacuum)**: optical usually dominates — huge capacity, no weather, no spectrum filing, low intercept probability.
- If **space-to-ground**: prefer **hybrid** — optical for clear-sky bulk, RF or cloud-free-line-of-sight diversity for availability.
- If the platform **cannot meet µrad pointing** within SWaP: optical is out regardless of its budget.
