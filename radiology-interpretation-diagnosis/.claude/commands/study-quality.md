# /study-quality

The technical-adequacy gate: confirm a batch is *diagnostic-quality* before you read it for defects — the spherification analog of rejecting an under-exposed film.

## Inputs

- The pinned recipe (alginate %, calcium salt + %, bath salt + %, bath time).
- Process facts: was the alginate rested/degassed? for how long? base pH? bath water source (tap/distilled)?
- A quick look at a few pilot spheres.

## Steps

1. Check **alginate prep**: blended smooth, strained, and **rested to degas** (no visible bubbles). Un-rested → non-diagnostic.
2. Check the **pH gate**: base pH ≥ 3.6, or buffered with sodium citrate. Below → non-diagnostic.
3. Check **concentrations** are in the `references.md` band for the chosen method.
4. Check the **bath**: correct salt for the method, fresh, and (reverse) not hard-water contaminated.
5. Verdict: **diagnostic** → proceed to `/read-batch`; **non-diagnostic** → assign Sphere-RADS-0 and remake.

## Output

A pass/fail adequacy verdict with the specific failing parameter(s). If failed, the exact remake change. Append to the batch's `outputs/` report header.

## Notes

- A non-diagnostic batch must be **remade, not over-read** — diagnosing a "thin membrane" on an unbuffered acid base wastes a differential on a prep error.
- This gate is the single highest-yield habit borrowed from radiology; it prevents most false "defects."
