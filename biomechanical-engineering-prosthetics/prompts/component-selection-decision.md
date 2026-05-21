# component-selection-decision

## Purpose

Use when faced with a specific component selection question for a known patient — typically a foot, knee, or liner change decision driven by activity goals, fit problems, payer access, or new-formulary entry.

## Prompt Template

```
Acting as the biomechanical engineer supporting a component-selection decision for a known patient.

Patient summary:

- **Patient ID / pseudonym:** [VALUE]
- **K-level:** [VALUE]
- **Component type under decision:** [foot / knee / liner / suspension / sleeve]
- **Current component (model + duration of use):** [VALUE]
- **Reason for considering change:** [activity-goal shift / fit complaint / wear-out / recall / formulary change / payer access change]
- **Candidate components to consider:** [list 2-4 models with vendor]
- **Patient priorities (verbatim):** [VALUE]
- **Payer / formulary constraints:** [VALUE]
- **Recent gait-lab / pressure-mat data summary:** [SPC chart state — in-control / signals; gait asymmetry status]
- **Recent PROMs trajectory:** [stable / improving / declining]

Please:
1. Map each candidate component against the patient's K-level, payer formulary, activity goals, and current measurement data.
2. Cite the relevant ISO testing data and any MAUDE history for each candidate (note: agent doesn't have live MAUDE access; flag if a fresh lookup is needed).
3. Identify the trade-offs between candidates in terms of: weight, durability cycles, response characteristic, learning curve, replacement cost, service availability.
4. Recommend a primary candidate + a fallback, with rationale tied to measurement data and patient priorities.
5. Specify what new measurements should be collected post-change (re-baseline gait? re-run pressure-map?) and the expected timeline for confirming the change was beneficial.
6. Note any regulatory / consent / documentation requirements specific to the candidate.
```

## Expected Output

- Candidate-comparison table with axes (weight, durability per ISO, formulary status, etc.)
- Trade-off analysis tying each axis to this patient's specific situation
- Primary + fallback recommendation with rationale
- Post-change measurement plan (re-baseline trigger, monitoring cadence)
- Regulatory + consent checklist

## Notes

- The agent cannot make the clinical decision; it produces a structured proposal for the CPO and prescribing physician.
- Always check FDA MAUDE for the candidate components before recommending — recent recall or field-action events may eliminate a candidate.
- For microprocessor components (C-Leg, Genium, Empower, Proprio), include training-burden assessment — these components require structured patient education and gait-retraining, not just a fitting.
- Cost is part of the patient's decision too; payer-covered components vs. patient-pay-difference scenarios should be surfaced, not hidden.
