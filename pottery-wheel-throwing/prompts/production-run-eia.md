# Production-Run Environmental Impact Assessment

## Purpose

Use to produce a defensible cradle-to-gate environmental impact assessment for a whole production run, structured as an ISO 14040 LCA, suitable for an eco-claim or an internal reduction plan.

## Prompt Template

```
You are running an ISO 14040 life-cycle assessment of a pottery production run. Begin by fixing the functional unit and system boundary; do not report any number without them.

Run details:
- **Functional unit:** [e.g. "one finished, food-safe 350 ml mug"]
- **Run size:** [PIECES]
- **System boundary:** [cradle-to-gate / gate-to-gate]
- **Clay:** [KG purchased] | reclaim workflow: [yes/no, rate]
- **Water:** [estimate or per-piece L]
- **Kiln:** [MODEL, CU FT] | bisque + glaze firings for the run: [COUNT] | measured kWh: [VALUE or "rated kW = X"]
- **Glaze:** [recipe / hazardous constituents]
- **Grid CO₂e factor:** [gCO₂e/kWh and source]

Please:
1. Goal & scope: restate functional unit and boundary.
2. Inventory (LCI): tabulate clay, water, firing energy (bisque + glaze), glaze.
3. Impact (LCIA): convert to kg CO₂e, L water, and glaze-hazard flags; attribute shares.
4. Interpretation: name the hotspot, run one sensitivity case (load density / off-peak / fuel), and give per-piece and run totals.
```

## Expected Output

- A goal-and-scope statement with functional unit and boundary.
- An LCI inventory table and an LCIA results table with attributed shares.
- The identified hotspot (expect firing) and a sensitivity case.
- Per-piece and whole-run headline figures with units and boundary attached.
