# Formal Show Verification

## Purpose

Run a full verification pass over a show: build the cue model, discharge the obligation catalog, and report which obligations hold (with margins) and which are refuted (with counterexamples). Use at design checkpoints and before sign-off.

## Prompt Template

```
You are verifying a fireworks display as a timed, safety-critical system. Assume a licensed
operator firing manufactured devices under permit. Do NOT produce any chemistry/manufacture content.

Show inputs:

- **Cue list / source:** [PASTE OR PATH — note whether times are FIRE or EFFECT times]
- **Safety framework:** [NFPA 1123 outdoor | NFPA 1126 proximate] + permit limits: [VALUES]
- **Site geometry:** [spectator line, no-fire zones, firing positions]
- **Wind (nominal & worst-case forecast):** [SPEED + DIRECTION]
- **Firing hardware:** [modules, pins, max simultaneous per module]
- **Music map / hero cues + tolerance τ:** [BEAT TIMES or PATH, τ in ms]

Please:
1. Build the canonical cue sheet (fire AND effect timelines, t_clear, radius, channel).
2. Generate the proof-obligation catalog (SEP, REUSE, CURR, CHAN, RUNTIME, SYNC, FALLOUT, DENSITY) with tolerances.
3. Discharge each obligation: verdict + robustness margin, or a concrete counterexample (ids, quantity, amount, time).
4. List refutations ranked by severity (safety before artistic) and route each to its repair class.
5. State the sign-off readiness (not-ready if any safety obligation is open or refuted).
```

## Expected Output

- A canonical cue sheet with both timelines.
- A spec catalog with per-obligation tolerances.
- A verification report: verdicts, margins, written-out counterexamples.
- A ranked refutation list and a sign-off readiness verdict.
