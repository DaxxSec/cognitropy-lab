# Counterexample Repair

## Purpose

Given a verification counterexample (a refuted obligation), propose the *minimal* cue-sheet edit that discharges it without opening a new violation. Use during the triage→repair step of the verification loop.

## Prompt Template

```
A schedule obligation was refuted. Propose the minimal repair, respecting that safety obligations
dominate artistic ones. Never fix an artistic miss by opening a safety violation.

Counterexample:

- **Refuted obligation:** [ID + statement, e.g. SEP: footprints disjoint while live]
- **Witness:** [cue ids, violated quantity, amount, time/window, wind vector if geometry]
- **Cue sheet excerpt (affected cues + neighbors):** [PASTE]
- **Binding constraints nearby:** [adjacent obligations the repair must not break]

Please:
1. Classify the violation via the constraint-violation triage tree (geometry / time / resource / artistic).
2. Propose the minimal edit (delay cue, re-position, re-rack, split burst, widen τ, drop/downgrade).
3. State which obligations the edit could affect and must be re-verified.
4. Show the before/after for the changed cue fields and the expected new margin.
5. If no edit discharges it without a safety regression, say so and recommend cutting the cue.
```

## Expected Output

- The violation class and chosen repair branch.
- A concrete minimal cue edit (field-level before/after).
- The re-verification set (which obligations to re-run).
- The expected new robustness margin, or an explicit "cut the cue" recommendation.
