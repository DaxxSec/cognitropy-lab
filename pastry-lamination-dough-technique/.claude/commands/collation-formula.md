# /collation-formula

Compute and notate the fat/dough layer count for a fold regimen, the way a codicologist notates a manuscript's quire structure with a collation formula.

## Inputs

- Fold regimen — an ordered list of turns, e.g. `single, single, single` or `book, single, single`.
- Lock-in style (optional) — English/single-fold or French envelope (affects the starting layer assumption).
- Target product (optional) — to compare against the canonical layer count (croissant ≈ 27 fat layers).

## Steps

1. Map each turn to its multiplier: single/letter/trifold = ×3, book/double/wallet = ×4 (see `context/references.md`).
2. Multiply the sequence to get **fat layers** (start from the single lock-in layer = 1).
3. Estimate **total alternating leaves** ≈ 2 × fat layers + 1.
4. Write the **collation formula** in compact notation, e.g. `S·S·S = 3³ = 27 fat layers (~55 leaves)`.
5. Compare to the product's canonical target; flag over- or under-lamination and suggest a regimen that hits the target if needed.

## Output

A short layer report saved to `outputs/collation-<product>-<date>.md`: the regimen, the formula, fat-layer and total-leaf counts, and a pass/adjust verdict against the target.

## Notes

- Resting between turns does not change the count but is required for the layers to survive to the bake — note rest needs alongside the formula.
- Too many layers (e.g. 3⁶ for a croissant) yields thin, fragile leaves that weld easily; the formula is a design check, not just bookkeeping.
