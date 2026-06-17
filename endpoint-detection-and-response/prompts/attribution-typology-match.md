# Attribution Typology Match

## Purpose

Use to generate ranked attribution hypotheses by matching observed TTPs to known campaign families — comparative typology — while guarding against typology forcing (matching to a famous group just because it's famous).

## Prompt Template

```
You are matching an intrusion to known campaign families. Require discriminating evidence; weight commodity features near zero.

- **Observed TTPs:** [LIST WITH ATT&CK IDs]
- **Bespoke tooling markers:** [CUSTOM LOADERS / MUTEXES / PROTOCOLS / BUILD PATHS]
- **Infrastructure:** [ASN / PROVIDER / NAMING PATTERNS]
- **Reference corpus:** [ATT&CK GROUPS / INTERNAL INTEL / PRIOR CASES]

Please:
1. Build a feature vector of discriminating features only; explicitly drop commodity tooling.
2. Score candidate families, weighting discriminating TTPs far above shared commodity ones.
3. Rank hypotheses with similarity scores and confidence bands (HIGH/MEDIUM/LOW).
4. For the top hypothesis, state what would falsify it and what a false-flag would look like.
```

## Expected Output

- Ranked family hypotheses with scores and confidence bands.
- The specific discriminating TTPs driving each match.
- An explicit falsification / false-flag section for the leading hypothesis.
