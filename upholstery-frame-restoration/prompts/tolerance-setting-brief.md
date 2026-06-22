# Tolerance-Setting Brief

## Purpose

Use when deciding what tolerances a frame characteristic should actually carry. Balances functional need, the period/value of the piece, and conservation ethics against the bench's demonstrated capability — so tolerances are neither sloppy nor impossibly tight for a hand process.

## Prompt Template

```
You are the quality-engineering agent for an upholstery frame restoration bench.
Help me set defensible tolerances for a characteristic.

I need a tolerance for:

- **Characteristic:** [e.g. seat-box squareness Δd; leg-length spread; joint gap]
- **Piece type / period / value:** [VALUE]
- **Function / load:** [structural seat joint | decorative | light-use]
- **Conservation status:** [antique/significant | utility]
- **Demonstrated process capability:** [σ̂ from the in-control chart, current Cpk if known]
- **Customer / use expectations:** [VALUE]

Please:
1. Recommend USL/LSL (or a one-sided limit) with the reasoning from function, period, and use.
2. Check the proposed tolerance against the bench's capability — is a Cpk ≥ 1.33 achievable, or is the tolerance tighter than the hand process can hold?
3. Note where conservation ethics should LOOSEN the tolerance (retain sound original material that's slightly off-nominal).
4. State the measurement resolution needed (≤ 1/10 of the tolerance) and whether the current gauge qualifies.
5. Give the final recommended tolerance plus any conditions (e.g. valid only once the process is in control).
```

## Expected Output

- Recommended limits with functional/period justification.
- A capability reality-check (achievable vs. aspirational).
- Conservation-driven loosening notes where original material is involved.
- The measurement-resolution requirement and gauge adequacy.
- A final tolerance recommendation with conditions.
