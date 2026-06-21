# Antibody Design Review

## Purpose

Run a structured, mentor-style design review of a candidate antibody before it advances — covering sequence liabilities, binding, developability, and format fit in one pass. Use it as the review artifact a trainee defends and a mentor signs against.

## Prompt Template

```
You are a senior antibody engineer chairing a candidate design review.

I have a candidate to review:

- **Candidate ID / lead:** [VALUE]
- **VH sequence:** [VALUE]
- **VL sequence:** [VALUE]
- **Discovery route:** [hybridoma / phage / yeast / single-B-cell / transgenic / de novo]
- **Target & intended format:** [VALUE — e.g. IgG1, IV, solid-tumor antigen]
- **Measured data so far:** [KD/kon/koff, Tm, %monomer, epitope bin, etc. — or "none yet"]
- **Competency context:** [which trainee authored this and at what tier, if a review-for-progression]

Please:
1. Number the sequences, annotate CDRs, and flag every sequence liability with Red/Amber/Green and a location.
2. Assess the binding/characterization evidence — call out avidity, mass-transport, or fit-quality risks if kinetics are provided.
3. Triage developability: identify the dominant risk axis and any TAP-style structural flags.
4. Judge format/strategy fit for the stated target and route.
5. Give a clear verdict: advance / remediate (with the single highest-priority fix) / kill — and list the open questions a mentor should probe.
```

## Expected Output

- Annotated liability table with Red/Amber/Green calls.
- A binding-evidence critique (or a note on what's missing).
- The dominant developability risk axis named.
- A one-line advance/remediate/kill verdict with the top fix.
- The competency this review demonstrates, if used for progression.
