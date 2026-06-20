# Pottery Wheel Throwing — Workflows and Methodology

Step-by-step procedures the agent runs. `concepts.md` says what things are; this file says what to *do*. Every workflow keeps the environmental-impact-assessment lens active, because the engine's technique for this build is EIA.

## Workflow 1: Studio flow optimization (signal-timing the studio)

**Goal:** find the bottleneck, set the batch cadence, and coordinate the stages so a production week runs at maximum throughput with minimum greenware sitting idle.

### Steps
1. **Inventory the stages.** List wheels, drying capacity, trimming benches, and kiln(s) with their counts and a measured duration for each stage (from `context/` logs).
2. **Compute saturation flow per stage** (`/throwing-saturation-flow`). For serial stages: pieces/hour a worker sustains. For the kiln: pieces per cycle ÷ cycle hours.
3. **Compute demand ÷ capacity (X) for each stage.** The stage with the highest X is the bottleneck. If any X > 1 the studio is oversaturated there — no scheduling fixes it; go to Workflow 2 / capacity decision.
4. **Set cycle length with Webster** (`/cycle-length-optimize`): `C₀ = (1.5L + 5)/(1−Y)`, using kiln load/unload as the dominant lost time L. High L pushes toward longer cycles (bigger, less frequent firings).
5. **Split capacity across product lines** (`/kiln-phase-split`): give each line green time proportional to its critical flow ratio `yᵢ = qᵢ/sᵢ`.
6. **Coordinate offsets** (`/green-wave-schedule`): schedule throwing so each batch reaches the kiln just as a firing slot opens — the green wave. Output a dated production calendar to `outputs/`.

### Decision Points
- If the bottleneck is the **kiln** (the usual case): the fix is load density and firing schedule, not faster throwing. Go to Workflow 2.
- If the bottleneck is **drying**: add drying capacity (cabinet, fan, dehumidifier) before adding wheels — it is the cheap fix.
- If the bottleneck is the **potter's hands**: that is a labor/skill constraint; scheduling only smooths it, it cannot raise the ceiling.

## Workflow 2: Kiln capacity and footprint optimization

**Goal:** raise pieces-per-firing and cut per-piece energy in one move — the convergence lever.

### Steps
1. **Measure the kiln envelope** (`/kiln-load-density`): interior W×D×H, shelf thickness, post heights, and the dimensions of the target form(s).
2. **Solve the packing**: maximize pieces per firing across shelf levels, respecting clearance for even heat and that ware cannot touch (glaze firing) or can nest (bisque). Report the load density and the marginal piece each extra shelf adds.
3. **Audit firing energy** (`/firing-energy-audit`): rated kW × effective firing hours, or measured kWh; identify soak and cooling losses; pick electric-vs-gas and apply the grid CO₂e factor.
4. **Compute energy per piece** = firing energy ÷ pieces in the firing. Re-run at the optimized load density to show the drop.
5. **Decide the schedule**: fewer, fuller firings (raises utilization) vs. more frequent firings (cuts queue delay). Trade off using Workflow 1's delay numbers — the optimum is the lowest cycle count that keeps the kiln's X below ~0.9.

### Decision Points
- If load density is already high and energy/piece is still large: the lever is **the firing itself** — off-peak tariff, better insulation/elements, a controller upgrade, or a tighter cone schedule.
- If electric grid CO₂e is high and gas is available: model both; gas may win on CO₂e even if it loses on cost, or vice-versa. State the factor.

## Workflow 3: Production-run environmental impact assessment (ISO 14040)

**Goal:** a defensible cradle-to-gate footprint for a real production run (e.g. 200 mugs), structured the way a real LCA is.

### Phase 1 — Goal & scope
Define the **functional unit** ("one finished, food-safe 350 ml mug") and the **system boundary** (cradle-to-gate vs. gate-to-gate). State assumptions and the grid CO₂e factor up front. A run EIA that skips this is not comparable to anything.

### Phase 2 — Inventory (LCI)
Tally every input for the run:
- **Clay**: mass thrown, minus reclaim recovered, = net clay consumed (`/clay-reclaim-balance`).
- **Water**: throwing + glazing + cleanup, by measurement or reasonable per-piece estimate.
- **Energy**: bisque firing share + glaze firing share, allocated per piece by load density (`/firing-energy-audit`).
- **Glaze**: material mass applied + application loss; flag hazardous constituents (`/glaze-hazard-screen`).

### Phase 3 — Impact assessment (LCIA)
Convert inventory to impact categories: energy → kg CO₂e (via grid factor), water → litres (and a stress-weighted figure if regional), glaze toxics → a hazard flag with the relevant exposure/leaching limit. Attribute shares; expect firing to dominate.

### Phase 4 — Interpretation
Identify the hotspot (firing, ~always), test sensitivity (what if load density +30 %? off-peak? gas?), and write the result with its functional unit and boundary attached. `/footprint-per-piece` emits the per-unit number; the run report multiplies and totals.

### Decision Points
- If the goal is a **public eco-claim**: keep the boundary cradle-to-gate and disclose it; do not cherry-pick gate-to-gate to look better.
- If the goal is **internal cost-cutting**: gate-to-gate is fine; focus on the addressable levers from Workflow 2.

## Workflow 4: Glaze safety gate (runs before any food-contact or sale)

### Steps
1. Parse the recipe into materials and percentages (`/glaze-hazard-screen`).
2. Flag hazardous constituents (lead, barium, cadmium, lithium, manganese, soluble colorants) against the reference table.
3. For food-contact ware: require an ASTM C738/C895 leach test plan; recommend a stable liner glaze for the food surface if the decorative glaze is suspect.
4. For studio safety: note silica content and dust-control requirements; for waste: note drain-disposal prohibition and reclaim/settle path.
5. Gate: **do not** advance a suspect food-contact glaze to production on recipe inspection alone — the leach test is the gate, not the analysis.

> Don't repeat `concepts.md`. This file is the procedure; the formulas, mappings, and constraints live in `concepts.md` and `references.md`.
