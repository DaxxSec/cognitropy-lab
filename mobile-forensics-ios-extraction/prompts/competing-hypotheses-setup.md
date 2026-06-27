# Competing Hypotheses Setup (ACH)

## Purpose

Turn a raw investigative question plus an artifact inventory into a structured ACH starting point: a mutually-exclusive, exhaustive hypothesis set and a diagnosticity matrix skeleton. Use at the start of analysis, before forming an opinion.

## Prompt Template

```
You are an iOS forensic examiner applying Analysis of Competing Hypotheses.

Investigative question: [ONE FALSIFIABLE SENTENCE]

Available artifacts (with source DB and reliability):
- [ARTIFACT 1 — e.g. sms.db row, KnowledgeC unlock event]
- [ARTIFACT 2]
- [ARTIFACT 3]
Notable absences: [EXPECTED-BUT-MISSING ARTIFACTS]
Constraints: [DEVICE/LOCK-STATE/TIME WINDOW]

Please:
1. Enumerate mutually-exclusive, collectively-exhaustive hypotheses (include a null and a "someone/something else or fabrication/sync" hypothesis).
2. For each hypothesis, predict the evidence that should be PRESENT and the evidence that should be ABSENT if it were true.
3. Build the evidence × hypothesis matrix skeleton and mark each cell Consistent / Inconsistent / N-A.
4. Flag which evidence items are diagnostic (inconsistent with at least one hypothesis) vs non-diagnostic.
```

## Expected Output

- A numbered hypothesis set with predicted present/absent signatures.
- A scored C/I/N matrix skeleton.
- A short list of the high-diagnosticity evidence items to prioritise.
