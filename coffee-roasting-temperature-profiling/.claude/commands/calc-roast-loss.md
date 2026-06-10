# /calc-roast-loss

Compute roast weight loss (shrinkage) and green→roasted yield for a batch, and reconcile it against both development quality and the inventory ledger.

## Inputs

- Charge (green) weight and drop (roasted) weight for the batch — from a calibrated scale.
- The batch's roast level / profile and its expected weight-loss band.
- The green lot ID (to post the inventory move) and the green's moisture (high-moisture green loses more).

## Steps

1. Read `context/concepts.md` ("Roast loss, yield, conversion") and `context/references.md` (weight-loss bands by level; formulas).
2. Compute **loss % = (green − roasted)/green × 100** and **yield = roasted/green**.
3. Compare loss to the expected band for the target level: unusually **low** loss → suspect underdevelopment; unusually **high** → suspect too-dark/over (or wet green). Cross-check with `/diagnose-roast-curve` if off-band.
4. Post the inventory move: decrement the green lot by charge weight, increment roasted SKU by drop weight; tag with lot ID + profile version.
5. Roll up periodically: aggregate yields per lot/SKU; reconcile cumulative green-out vs roasted-in against the ledger (within shrink/spillage tolerance).
6. Feed the realized yield into `/forecast-roast-schedule` and roasted-cost calcs (cost ÷ yield).

## Output

`outputs/batches/<batch-id>-loss-YYYY-MM-DD.md` — loss %, yield, comparison to the expected band with a development flag if off, and the posted inventory move (green decrement / roasted increment). Monthly roll-up to `outputs/inventory/reconciliation-<period>.md`.

## Notes

- Always label weights **green** or **roasted** — and cost roasted coffee on roasted weight (cost ÷ yield), or margin is overstated by the loss %.
- A reconciliation gap beyond shrink tolerance usually means a mis-tagged batch, scale error, or wrong lot charged — investigate before trusting the ledger.
- Yield is green-, moisture-, and roast-level-specific; don't reuse one SKU's yield for another.
