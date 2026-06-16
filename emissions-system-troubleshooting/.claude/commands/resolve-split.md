# /resolve-split

Split-brain tiebreaker: when two candidate root causes both have partial support, design the single decisive discriminating test that falsifies one branch — instead of repairing both.

## Inputs

- Two (or more) competing candidate root causes, each with partial evidence
- The evidence ledger to date
- The discriminating-test options available given the vehicle and tools

## Steps

1. State both hypotheses and exactly which evidence supports each.
2. Find a **discriminator** — a test whose outcome is *different* under each hypothesis (e.g. P0420 split between "dead cat" and "exhaust leak": an exhaust-leak smoke/listen test, or watching if the rear O₂ tracks the front only when loaded, separates them cleanly).
3. Prefer the test that is cheapest, most reversible, and most decisive (one test, two distinct predicted results).
4. Run it; log the result; the hypothesis whose prediction failed is **falsified** and dropped.
5. If the discriminator is ambiguous, design a second one — never commit through an unresolved split.

## Output

A tiebreaker record appended to the ledger: the competing hypotheses, the discriminating test, its predicted-vs-actual results, and the surviving hypothesis (now ready for `/build-quorum` / `/commit-diagnosis`).

## Notes

- The failure mode this prevents is the "parts cannon" — replacing both suspects and never learning which was the cause.
- A good discriminator is falsification-shaped: it should be able to *kill* a hypothesis, not just be consistent with it.
