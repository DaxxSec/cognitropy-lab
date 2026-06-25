# /optimize-roi

Decide whether a proposed optimization (size, speed, or power) is worth its engineering and risk cost — the gate that stops premature optimization, the canonical waste of embedded engineering time.

## Inputs

- The optimization proposal and the budget pressure it relieves (flash/RAM/cycles/µA), **measured** not guessed
- An estimate of engineering hours, added complexity, and regression risk
- Current headroom in the relevant budget

## Steps

1. Confirm the budget is actually **tight** — if there's ample headroom, the value of the resource freed is ~0 and you stop here.
2. Quantify the **saving** from a real measurement (`.map`, profiler, ammeter), not a hunch.
3. Estimate the **cost**: dev-hours + maintainability/readability hit + regression risk (higher in safety paths).
4. Compute `ROI = value_of_resource_freed ÷ cost`; decide do-now / defer-as-debt / reject.
5. If done, **re-measure** to confirm the saving materialized; revert if it didn't.

## Output

`outputs/projects/<name>/optimize-<target>.md` — the measured pressure, the saving, the cost/risk, the ROI verdict, and the post-change re-measurement.

## Notes

- "Clever" is not a justification — an optimization on a non-tight budget is rejected no matter how elegant.
- Hand-assembly or aggressive tricks in a safety path carry regression risk that is part of the cost; require tests/review.
