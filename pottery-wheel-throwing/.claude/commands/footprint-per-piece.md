# /footprint-per-piece

Run a cradle-to-gate environmental impact assessment for one finished piece — clay, water, firing energy, and glaze — with an explicit functional unit and system boundary.

## Inputs

- The functional unit ("one finished, food-safe 350 ml mug").
- System boundary (cradle-to-gate vs. gate-to-gate).
- Per-piece clay mass (net of reclaim, from `/clay-reclaim-balance`), water use, glaze mass, and the per-piece firing-energy share (from `/firing-energy-audit` ÷ load density).
- The grid CO₂e factor (fetch a current value; state it).

## Steps

1. Read `context/concepts.md` → "Environmental impact assessment for ceramics" and follow ISO 14040 phases.
2. **Goal & scope:** restate the functional unit and boundary up front; an assessment without them is not comparable.
3. **Inventory (LCI):** tabulate clay (kg), water (L), firing energy (kWh, both bisque and glaze shares), and glaze material (g, with hazardous constituents flagged via `/glaze-hazard-screen`).
4. **Impact (LCIA):** convert energy → kg CO₂e via the grid factor; water → L (stress-weighted if regional); glaze toxics → hazard flag with the relevant limit.
5. **Interpretation:** attribute shares (expect firing to dominate, ~60–90%), run one sensitivity case (e.g. +30% load density, or off-peak/gas), and state the headline per-piece number with its unit and boundary attached.

## Output

`outputs/footprint-<form>-YYYY-MM-DD.md`: the functional unit, boundary, LCI table, LCIA results, hotspot, sensitivity, and the headline per-piece footprint — defensible enough to back a public claim.

## Notes

- Never publish a number without its functional unit and boundary; that is how eco-claims become misleading.
- If the result will support a marketing claim, keep the boundary cradle-to-gate and disclose it — do not switch to gate-to-gate to look better.
