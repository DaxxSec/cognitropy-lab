# Courtroom Findings Summary

## Purpose

Translate a completed ACH examination into a defensible, plain-language summary for non-technical readers (counsel, court, jury) that states confidence and the alternatives ruled out — without overclaiming. Use at the reporting stage.

## Prompt Template

```
You are summarising an iOS forensic examination for a non-technical audience. Be accurate, calibrated, and free of jargon and overstatement.

- **Question:** [INVESTIGATIVE QUESTION]
- **Surviving hypothesis:** [FROM THE ACH MATRIX]
- **Confidence:** [calibrated level + basis]
- **Key supporting evidence:** [ARTIFACTS]
- **Alternatives refuted:** [HYPOTHESIS → evidence that refuted it]
- **Limitations:** [sealed data / single-source findings / sensitivity dependencies]

Please:
1. State the conclusion in one or two plain sentences, with its confidence.
2. Explain, without jargon, the main evidence and what it does and does not prove.
3. List the alternative explanations considered and why each was ruled out.
4. State the limitations honestly, including anything that could change the conclusion.
```

## Expected Output

- A plain-language conclusion with explicit confidence.
- A short, honest account of supporting evidence and its limits.
- The refuted alternatives and the stated limitations — no overclaiming.
