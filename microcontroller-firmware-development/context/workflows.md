# Microcontroller Firmware Development — Workflows and Methodology

Procedures and decision trees, all framed by today's technique: **cost-benefit analysis**. Concepts live in `concepts.md`; this file is what the agent *does* with them. Throughline: name the currencies, put the numbers on the table, pick the best trade, and log it.

## Workflow 1: MCU Selection Matrix

**Goal:** pick the part that minimizes lifetime cost while meeting every hard requirement.

### Steps
1. List **hard requirements** (must-haves: peripherals, min flash/RAM, power floor, temp range, certifications) — these are filters, not scores.
2. Filter the candidate list to parts that pass every hard requirement.
3. Define **weighted criteria** (e.g. unit cost @volume 30%, flash/RAM headroom 20%, active+sleep power 20%, peripheral fit 15%, ecosystem/tooling 15%).
4. Score each surviving candidate 1–5 per criterion; compute the weighted total.
5. Sanity-check the winner against **NRE vs COGS** at the real volume, and reserve headroom; record the matrix in `outputs/projects/<name>/mcu-matrix.md`.

### Decision Points
- If two candidates tie → prefer the **more mature ecosystem** (lower NRE risk) unless volume is huge enough that the COGS delta dominates.
- If nothing passes the hard filters → relax a *soft* requirement or add an external part (a cost trade), never a hard safety/cert one.

## Workflow 2: Flash/RAM Budget Loop

**Goal:** keep the binary fitting with headroom, and decide cut-vs-optimize when it doesn't.

### Steps
1. Establish the **ceiling** (part flash/RAM) and a **headroom reserve** (e.g. keep 15–20% free for field fixes).
2. From the `.map`/`size` output, attribute usage to modules; record the baseline.
3. On each feature, re-measure; if the reserve is threatened, open a **cut-or-optimize** decision.
4. Rank candidate reductions by `bytes_saved ÷ engineering_hours` (and by risk); this is `/optimize-roi`.
5. Apply only the reductions whose ROI clears the bar to restore the reserve — stop there.

### Decision Points
- Plenty of headroom → **do not optimize** (marginal value ≈ 0); spend the hours on features or tests.
- Reserve breached → take the highest-ROI cuts first (e.g. `newlib-nano`, `--gc-sections`, drop an unused HAL) before hand-optimizing code.
- Still over after high-ROI cuts → escalate to an **MCU re-spin** decision (Workflow 1) rather than unmaintainable micro-optimization.

## Workflow 3: Build-vs-Buy a Stack Component

**Goal:** choose commercial / open-source / in-house on true total cost of ownership.

### Steps
1. Define the component's requirements and the **certification/security bar** it must meet.
2. Cost **buy**: license (per-unit or one-time), integration hours, support, redistribution terms.
3. Cost **open-source**: integration + maintenance hours, **license obligation** (GPL copyleft vs permissive), upstream health.
4. Cost **in-house**: engineering months + ongoing maintenance + the risk it under-delivers on a hard requirement (e.g. a certified BLE stack).
5. Compare TCO over the product's life at the real volume; record the decision and the license terms.

### Decision Points
- Closed-source product + only-GPL option → the license cost is "can't ship as-is" — exclude or budget a commercial license.
- Safety/security-critical (crypto, radio, RTOS) → bias toward **proven/certified** even at higher buy price; in-house crypto is almost never the cheapest once risk is priced.

## Workflow 4: Optimization-ROI Gate

**Goal:** never spend engineering on an optimization that isn't worth it.

### Steps
1. State the **budget pressure** the optimization relieves (flash/RAM/cycles/µA) and by how much, **measured** not guessed.
2. Estimate the **cost**: engineering hours, added complexity, maintainability/readability hit, and regression risk.
3. Compute `ROI = value_of_resource_freed ÷ cost`; value is ~0 if the budget isn't tight.
4. Decide: do it, defer it (log as tech debt), or reject it.
5. If done, re-measure to confirm the saving materialized; revert if it didn't.

### Decision Points
- Budget not tight → **reject/defer** regardless of how clever the optimization is.
- High saving, low risk, tight budget → do it now.
- High saving, high risk (e.g. hand-asm in a safety path) → require review/tests; the risk is part of the cost.

## Workflow 5: Power (Energy) Budget

**Goal:** hit the battery-life target by spending microamps deliberately.

### Steps
1. Define the **duty cycle**: events per hour, active time per event, and sleep mode between.
2. Measure or datasheet the current in each mode (run, sleep, stop, radio TX/RX).
3. Compute **average current** = Σ(mode_current × fraction_of_time); battery life = capacity ÷ average current.
4. Identify the dominant term (usually radio TX or a leaky peripheral) and trade against it.
5. Price any new feature in **µA of average current** before accepting it; log the budget.

### Decision Points
- Target missed by a lot → attack the dominant term (lower TX duty, deeper sleep, better part) before micro-savings.
- A pricier MCU with much lower stop-mode current may pay for itself in battery → feed into Workflow 1.

## Workflow 6: Release Gate (defect & debt triage)

**Goal:** decide what blocks the release on cost-benefit, not on perfectionism or panic.

### Steps
1. List open defects and tech debt with **severity** (safety/security > data loss > functional > cosmetic) and a fix cost/risk.
2. Hard rule: **safety/security defects block** — they are not subject to cost-benefit deferral.
3. For the rest, weigh user impact × likelihood against fix cost and regression risk near a freeze.
4. Decide fix-now / defer-to-patch / won't-fix; record the rationale.
5. Confirm the build is reproducible and the budgets (flash/RAM/power) still hold at ship.

### Decision Points
- Near a freeze, a risky fix for a low-impact bug → defer; the regression risk outweighs the benefit.
- Any safety/security item → fix or do not ship; no deferral.

## Methodology Phases (project arc)

### Phase 1 — Frame the budgets
Name every binding currency (flash, RAM, µA, $, dev-hours, cert) and its ceiling. No design without budgets.

### Phase 2 — Architect by trade
Select MCU (W1), scheduler (`/rtos-vs-baremetal`), and stack build-vs-buy (W3); reserve headroom.

### Phase 3 — Build and measure
Implement features; re-measure flash/RAM/power each step (W2, W5). Profile before any optimization (W4).

### Phase 4 — Gate the release
Triage defects/debt (W6); confirm budgets and reproducibility; ship with the decision log intact.
