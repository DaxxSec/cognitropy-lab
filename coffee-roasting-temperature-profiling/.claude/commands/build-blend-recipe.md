# /build-blend-recipe

Compose a blend from component green lots, costing it correctly on roasted weight and drawing each component down in inventory while preserving per-lot traceability.

## Inputs

- The blend's target ratio (e.g. 60/30/10) and whether components are roasted **pre-blend** (each to its own profile) or **co-roasted** (one profile).
- Each component lot ID (from `/track-green-lot`): landed green cost, measured roast loss/yield, on-hand quantity, crop year, certs.
- Target output quantity (roasted) for the blend SKU, and the batch size.

## Steps

1. Read `context/concepts.md` ("Roasted costing", "Inventory & supply-chain model") and `context/references.md` (formulas).
2. Convert the roasted blend target into **green needed per component**: roasted share ÷ that component's yield (pre-blend), grossing each up by its own roast loss.
3. Cost each component on roasted weight: (landed green cost ÷ yield); sum weighted by ratio → blend roasted cost/kg. Show the gap vs a naive green-price estimate.
4. Check feasibility: does on-hand cover each component? Which component hits its reorder point or crop-year staleness first (the binding constraint on the blend's life)?
5. Record the recipe with **per-component lot genealogy** and cert status (the blend's certifiable claim is only as strong as its weakest-segregated component).
6. Draw inventory down per component; flag re-balancing if a lot runs out (a substitute changes cup and cost — re-validate).

## Output

`outputs/blends/<blend-sku>-vX-YYYY-MM-DD.md` — the ratio, per-component green-needed and roasted cost, blended cost/kg with the vs-naive gap, feasibility + binding constraint, full per-lot genealogy and cert status, and the inventory drawdown.

## Notes

- Cost on **roasted** weight per component — components at different roast levels have different yields, so green-price ratios ≠ roasted-cost ratios.
- A blend can only claim a certification if every component's chain-of-custody supports it and the mass-balance is documented.
- When a component lot is exhausted, treat the substitute as a new recipe version and re-cup; don't silently swap.
