# /acidity-calc

Compute theoretical vs. measured acetic-acid yield, GK value, and titratable acidity for a batch, and flag overoxidation and below-floor risks.

## Inputs

- Starting ABV (or Brix to estimate ethanol) of the substrate.
- Titration data (volume + normality of NaOH, sample volume) **or** a measured acidity %.
- Current residual ethanol if known.
- Target jurisdiction (for the acidity floor) — default US FDA 4%.

## Steps

1. Read `context/references.md` (formulas) and `context/concepts.md` §5 (parameters) and §2 (overoxidation).
2. **Project** theoretical acidity from starting ABV using `~1% ABV → ~1% acetic acid` (note the ~1.04 g/g stoichiometric ceiling).
3. **Compute measured acidity** from titration: `acidity% = (V_NaOH × N × 6.005) / V_sample`. If acidity % was supplied directly, validate it against the titration if both are present.
4. Compute **conversion efficiency** = measured ÷ theoretical, and **GK** = acidity % + residual ethanol %.
5. **Flag risks:** measured below the jurisdiction floor (with margin) → not legally vinegar; residual ethanol ≈ 0 with an overoxidation-prone strain → harvest now; efficiency well under ~80% → investigate aeration/temperature/strain.
6. Write the worksheet to `outputs/`.

## Output

- A worksheet printed to chat: theoretical acidity, measured acidity, efficiency %, GK, and risk flags.
- `outputs/acidity/<batch-id>-YYYY-MM-DD.md` with the numbers and assumptions.

## Notes

- pH is **not** a substitute for titratable acidity — always titrate for the legal/product number.
- Leave ~0.2–0.5% residual ethanol at harvest as an overoxidation buffer.
- If only Brix is known, estimate ethanol first (potential alcohol from sugar) and carry that uncertainty through.
