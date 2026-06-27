# Prompt — SME Prior-Elicitation Interview

## Purpose
Structure a short interview that converts a subject-matter expert's intuition into a defensible
`Beta(α, β)` prior mastery distribution, with the right strength (pseudo-count).

## Prompt Template
```
You are eliciting a prior mastery distribution from a subject-matter expert. Keep it conversational
but convert answers to numbers.

Objective: "{{OBJECTIVE}}"
Cohort: {{COHORT_DESCRIPTION}}

Ask, one at a time, and record answers:
1. "Of 10 typical learners entering this unit, how many could already do this?"  → most-likely mastery m.
2. "Could it plausibly be as low as __ or as high as __?"  → spread → confidence/pseudo-count c
   (wide spread → c≈4; narrow → c≈20).
3. "Is there a subgroup for whom this differs?"  → note for an equity check.

Then compute:
- α = m·c, β = (1−m)·c
- Report Beta(α, β): mean, 80% credible interval, strength c, and a plain-language reading.
- Run a prior predictive check: does the implied mastery range match the expert's stated low/high?
  If not, reconcile with the expert.
Flag if a strong prior rests on weak evidence.
```

## Expected Output
A documented `Beta(α, β)` prior with source = SME, strength, interval, an equity note, and the
prior-predictive reconciliation — ready for `/elicit-prior` to record.
