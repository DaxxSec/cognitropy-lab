# DTC Causal DAG (Leader / Follower)

## Purpose

Given a set of stored DTCs, produce the causal DAG — which codes are root **leaders** and which are downstream **followers** — so the case chases the cause, not the cascade.

## Prompt Template

```
You are an emissions root-cause adjudicator. Build the causal DAG of these DTCs; do not propose repairs.

I have:

- **Vehicle:** [YEAR/MAKE/MODEL/ENGINE]
- **Stored / pending / permanent DTCs:** [LIST with status]
- **Freeze-frame conditions per code (if known):** [VALUES]
- **Sensor-trust map (from cross-validation):** [which sensors are faithful/Byzantine]
- **Context:** [complaint, recent work]

Please:
1. Group codes that set under similar conditions (likely shared cause).
2. Map known causal chains (e.g. misfire → catalyst/lean/O₂ followers).
3. Demote any code whose only support is a Byzantine sensor.
4. Name the candidate leader(s) and list each follower as "explained by" its leader.
```

## Expected Output

- A leader → follower DAG with the reasoning for each edge
- A shortlist of candidate root causes (the leaders) for `/build-quorum`
- Any codes flagged as possible Byzantine artifacts rather than real faults
