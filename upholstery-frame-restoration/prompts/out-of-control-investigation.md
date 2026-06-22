# Out-of-Control Investigation (OCAP)

## Purpose

Use when a control chart fires a Western Electric/Nelson signal. Drives a disciplined root-cause hunt across the 6 Ms so a real assignable cause is found and removed — rather than the bench tampering with a stable process.

## Prompt Template

```
You are the quality-engineering agent for an upholstery frame restoration bench.
A control chart has signalled. Run the out-of-control action plan.

I have a chart signal:

- **Characteristic & chart:** [e.g. front-rail joint gap, I-MR]
- **Rule(s) fired:** [e.g. Rule 1: point beyond 3σ at frame #34; Rule 4: 9 points below center]
- **Recent context / what changed:** [new restorer? new glue lot? humidity swing? new jig? wood source?]
- **Measurement confidence:** [gage R&R %GRR for this gauge, if known]

Please:
1. First rule out a measurement error — say whether to re-measure or re-run gage R&R before believing the signal.
2. Bracket the change in time and list candidate assignable causes across the 6 Ms (Method, Machine/jig, Material/wood+glue, Measurement, Man/restorer, Mother-nature/RH).
3. Propose a 5-Whys line for the most likely cause.
4. Specify how to verify the cause (reproduce/remove it) and confirm the chart returns to control.
5. Recommend the standard update (traveler checklist, jig spec, glue-up MC window) that prevents recurrence.
```

## Expected Output

- A measurement-error ruling (re-measure / trust).
- A 6-Ms candidate-cause list bracketed to the change.
- A 5-Whys chain to a verifiable root cause.
- A verification step and a control-restoration check.
- A concrete standard/standard-work update to prevent recurrence.
