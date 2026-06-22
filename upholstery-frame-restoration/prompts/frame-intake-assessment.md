# Frame Intake Assessment

## Purpose

Use at the start of a job to turn a freshly-stripped frame into a structured assessment: characteristics to measure, joints to grade, conservation status, and the SQC plan for the piece. Drives the opening of a traveler.

## Prompt Template

```
You are the quality-engineering agent for an upholstery frame restoration bench.
Assess this incoming bare frame and propose the measurement + SQC plan.

I have stripped a frame:

- **Piece type / period:** [e.g. Edwardian open-arm chair, c.1905]
- **Conservation status:** [antique/significant | utility/modern]
- **Wood species (if known):** [VALUE]
- **Visible condition:** [racking? joint gaps? splits? corner-block state? fastener state?]
- **Current MC / ambient RH & temp:** [VALUE]
- **Destination environment (if known):** [humid / arid / typical interior]

Please:
1. List the quality characteristics worth tracking for THIS piece, each with a datum and a suggested tolerance, noting which are conservation-sensitive.
2. Flag which gauges need a gage R&R before their data can be trusted.
3. Identify the likely structural priorities (corner blocks / racking / specific joints) to grade first.
4. State the moisture readiness question and whether glue-up should wait.
5. Outline the traveler structure and which control charts this frame should feed.
```

## Expected Output

- A characteristic list with datums, tolerances, and conservation flags.
- Gauges requiring MSA before use.
- Ranked structural priorities for joint grading.
- A glue-up readiness call (cleared / condition first).
- A traveler + control-chart plan for the job.
