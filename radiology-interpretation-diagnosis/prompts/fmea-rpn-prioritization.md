# FMEA RPN Prioritization

## Purpose

Convert a list of observed/anticipated spherification failure modes into a scored, ranked FMEA so corrective effort goes where risk is highest. Use to stand up or revise the process risk register.

## Prompt Template

```
You are building a process FMEA for spherification using the S/O/D scales and
Action-Priority guidance in context/references.md.

- **Process scope:** [STEPS, e.g. hydrate → rest → buffer → dose → form → bath → rinse → hold]
- **Failure modes observed/anticipated:** [LIST]
- **Occurrence data:** [FREQUENCIES FROM PAST REPORTS / estimates]
- **Current detection controls:** [WHAT IS CHECKED BEFORE SERVICE / "none"]

Please:
1. For each mode, state its effect on the plate/guest and score Severity, Occurrence,
   Detection (1-10 each).
2. Compute RPN = S×O×D and assign Action Priority (H/M/L).
3. Rank descending; for High-AP / top-RPN items, recommend a corrective action, preferring
   detection controls when D dominates.
4. Flag any Severity 9-10 (safety/allergen/choking) modes to act on regardless of RPN.
```

## Expected Output

- A ranked FMEA table (step, mode, effect, S, O, D, RPN, AP, action).
- Detection-driven items routed to inspection fixes, recipe-driven items to recipe changes.
- Safety modes surfaced independently of their RPN.
