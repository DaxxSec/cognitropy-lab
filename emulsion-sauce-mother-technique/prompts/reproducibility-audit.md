# Reproducibility Audit Prompt

## Purpose

Use this prompt before sign-off (or before publishing a recipe) to confirm a formula will actually reproduce in another kitchen — the reproducibility gate, not a taste test.

## Prompt Template

```
You are auditing an emulsion formula for reproducibility ahead of sign-off. A formula that worked once is a draft; the bar is that a different cook can re-derive it from the record alone.

I want to audit a formula for reproducibility:

- **Formula ID / normalised form:** [paste]
- **Replicate evidence:** [how many preparers × replicates, with logs?]
- **Logged variables:** [ratio, emulsifier load, oil-addition rate, shear method, temperature, ambient temp, total time, final pH]
- **Outcome variance across batches:** [what differed between batches?]
- **Intended audience:** [pro kitchen / home cook / cookbook reader]

Please:
1. Check every required reproducibility-log field is present; list any that are UNSPECIFIED.
2. Assess whether ≥2 preparers × ≥2 replicates is met; if not, say what's missing to clear the gate.
3. Identify variables likely to drift in another kitchen (ambient temp, oil brand, egg size) and how to pin them.
4. Judge whether the instructions are deterministic enough for the intended audience (a home cook needs more pinned than a pro line).
5. Give a gate verdict: reproducibility PASS / FAIL, with the exact gaps to close.
```

## Expected Output

- A completeness check of the reproducibility-log fields.
- A preparer × replicate gate assessment.
- A list of drift-prone variables and how to pin them.
- An audience-fit judgement on instruction determinism.
- A PASS/FAIL reproducibility-gate verdict with remediation steps.
