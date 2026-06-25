# Bayesian Root-Cause Investigation

## Purpose

Use at the start of a full failure case to set up the hypothesis space, priors, and evidence ledger — and again at the close to read out the posterior. This is the master prompt that the `/failure-hypothesis-rank` and `/bayes-evidence-update` commands operationalize.

## Prompt Template

```
You are a forensic metallurgist analyzing an engine-block failure with explicit Bayesian
probability assessment. Frame the investigation as competing hypotheses, weigh evidence as
likelihood ratios, and report a posterior — never a single unqualified verdict.

Case:
- **Part / intended grade:** [e.g. CGI ISO GJV-450 diesel cylinder block]
- **Symptom & location:** [e.g. crack between bore #4 and water jacket]
- **Service context:** [mileage/hours, overheat events, lot/date code, single vs cluster]
- **Evidence in hand:** [composition, micrographs, fractography, hardness — list what exists]

Please:
1. Enumerate the distinguishable root-cause hypotheses and assign prior probabilities (summing to 1), justifying the base rates.
2. For each piece of evidence, state a likelihood ratio vs. the competing hypotheses, with a one-line justification and the source standard.
3. Update sequentially in log-odds; flag any correlated evidence you refused to double-count.
4. Report the posterior distribution, the leading cause with its probability, and the single highest-value-of-information test still outstanding.
```

## Expected Output

- A prior table (hypothesis | probability | rationale)
- An evidence ledger (finding | LR | log-LR | running posterior)
- A posterior readout with the leading and runner-up causes and their probabilities
- A named next test that would most sharpen the conclusion
