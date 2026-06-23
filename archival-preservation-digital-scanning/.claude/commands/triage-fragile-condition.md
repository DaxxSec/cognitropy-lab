# /triage-fragile-condition — Condition-based handling and routing triage

Assess the physical condition of material and route each lot to the correct path — capture-ready in-house, vendor with conditions, or conservation-first (stabilize before any imaging) — protecting originals from being damaged in the rush to digitize.

## Inputs

- Per-lot condition notes or a condition survey (paper brittleness, tears, mold, media format, signs of chemical decay).
- Material format (bound volume, loose sheet, photograph, acetate/nitrate film, magnetic tape, lacquer/shellac disc, glass plate).
- Available in-house handling capability and any conservation resource.

## Steps

1. **Grade condition.** Assign each lot a grade — pristine / stable / fragile / at-risk / unstable — using the rubric in `context/concepts.md §Condition`. Note format-specific decay markers (vinegar syndrome on acetate, sticky-shed on tape, flaking emulsion on glass plates).
2. **Flag active decay.** Anything actively degrading (acetate off-gassing, nitrate film, mold) is an urgency override — it jumps the preservation queue *and* may require isolation/safety handling before anything else.
3. **Decide the capture path.** Pristine/stable → standard in-house capture. Fragile → in-house with handling multiplier and a conservator consult. At-risk unique → in-house only (no transit). Unstable → **conservation-first**: stabilize before imaging, do not force a capture.
4. **Set handling protocol.** Per lot, specify support cradle/book angle limit, glove/no-glove, polarization for gloss, max handling time, and environmental constraints (humidity, light exposure budget).
5. **Define stop conditions.** Spell out what makes an operator *stop and escalate* mid-capture (new tear, surface lifting, audible cracking) rather than push through.
6. **Feed downstream.** Emit the handling multiplier per lot for `/plan-digitization-queue` and `/optimize-scanner-schedule`, and the no-transit flags for `/model-project-cost`'s make-vs-buy risk gate.

## Output

`outputs/condition-triage-<collection>.md`: the per-lot condition grade, decay flags, assigned capture path, handling protocol, escalation stop-conditions, and the multipliers/flags handed to the planning commands.

## Notes

- The schedule serves the object, never the reverse. If condition says stop, the optimization waits — a digitized surrogate is worthless if capturing it destroyed the original it was meant to preserve.
- Nitrate film and active mold are safety issues, not just preservation issues — route to specialists; do not improvise.
- "We'll be careful" is not a handling protocol. Write the constraints down so every operator follows the same limits.
