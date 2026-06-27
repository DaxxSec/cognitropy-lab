# /elicit-prior

Parameterise a `Beta(α₀, β₀)` prior mastery distribution (or BKT `p-init`) for an objective from
the strongest available evidence — baseline data, cohort history, or SME judgement.

## Inputs
- The objective and its cohort context.
- One of: pretest results (k correct / n attempts), prior-offering mastery rate, or SME estimate
  (most-likely mastery + confidence).

## Steps
1. Pick the source in priority order: baseline data > cohort history > SME judgement; record which.
2. **Data path:** set `Beta(α₀, β₀) = Beta(1+k, 1+(n−k))` (or use raw counts as pseudo-counts).
3. **History path:** convert the historical rate `m` and a modest strength `c` to `α₀=m·c, β₀=(1−m)·c`.
4. **SME path:** elicit most-likely mastery `m` and a confidence → pseudo-count `c` (low confidence
   → c≈4; high → c≈20); set `α₀=m·c, β₀=(1−m)·c`.
5. Run a prior predictive sanity check: does the prior's implied mastery interval match intuition?
   If a strong prior rests on no real evidence, weaken it.
6. State the interpretation (mean, 80% interval, strength) in plain language.

## Output
The prior `Beta(α₀, β₀)` (and `p-init`), its source, strength, mean, 80% credible interval, and a
one-line plain-language reading. Appended to the objective's entry in `outputs/`.
