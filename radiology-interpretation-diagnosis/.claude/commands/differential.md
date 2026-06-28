# /differential

For an observed defect, generate a ranked differential of *process* root causes from its gamut — separating the finding from its explanation.

## Inputs

- The defect finding (from `/read-batch`), e.g. "floating spheres, thin top membrane."
- The batch recipe and process facts (rest time, bath time, pH, calcium source).

## Steps

1. Look up the defect's **gamut** in `references.md` (finding → ranked candidate causes).
2. Re-rank the candidates given *this* batch's recipe — e.g. if alginate was clearly un-rested, promote "trapped air" above "low alginate %."
3. State the **discriminating test** for the top one or two causes (a measurement or a controlled re-make that would confirm/exclude).
4. Name the **most likely cause** and the corrective action, plus the runner-up to keep in mind (guards against premature closure).
5. Note whether the defect is a **one-off transient** or a **recurring** mode (the latter goes into the FMEA).

## Output

A ranked cause list with the discriminating test and a single recommended action. Attach to the batch report; recurring causes flow to `/fmea-process`.

## Notes

- Keep *finding* and *cause* separate: "thin membrane" is the finding; "bath time too short" is one candidate cause among several.
- Resist anchoring on alginate concentration — air, pH, and bath time cause more thin-membrane defects than dilution does.
