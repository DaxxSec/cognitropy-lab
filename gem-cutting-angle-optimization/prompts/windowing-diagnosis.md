# Windowing / Defect Diagnosis

## Purpose

Use when a finished stone shows a window, fish-eye, nailhead, or off meet-points and you need to decide whether the cause is the *design* (wrong angles for the RI) or the *machine* (runout / dished lap delivering a different angle than you set).

## Prompt Template

```
You are the faceting-optimization agent. Diagnose a cut defect and assign root cause.

The finished stone has a problem:

- **Material / RI:** [MATERIAL, RI]
- **Observed defect:** [window / fish-eye / dark center / off meet-points / poor polish]
- **Intended proportions:** [table %, crown angle, pavilion angle, depth %]
- **Measured/achieved proportions:** [same fields, as cut]
- **Machine condition at time of cut:** [spindle TIR, lap flatness, lap grit, dop length]

Please:
1. Grade achieved vs intended and compute the per-parameter delta.
2. Decide design-vs-machine: is the pavilion delta larger than the tolerance budget?
3. If machine: name the implicated component (runout / lap dishing / index) and the trend evidence.
4. If design: state the corrected angle for this RI.
5. Give the corrective action and whether any recent stones should be re-graded.
```

## Expected Output

- Achieved-vs-intended grade table with deltas.
- A design-vs-machine root-cause verdict with reasoning.
- The specific corrective angle change or maintenance task.
- A note on whether other recent cuts are suspect.
