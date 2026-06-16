# Quorum Gate Checklist

## Purpose

For a named candidate root cause, generate the minimum set of independent corroborating tests required to commit — the quorum gate that stops premature, single-witness diagnoses.

## Prompt Template

```
You are an emissions root-cause adjudicator. Define the quorum required to commit this candidate; do not assume it's correct.

I have:

- **Candidate root cause:** [e.g. "catalytic converter B1 oxygen-storage loss"]
- **Vehicle:** [YEAR/MAKE/MODEL/ENGINE]
- **Evidence collected so far:** [LIST with results]
- **Sensors proven faithful:** [LIST]
- **Tools available:** [scan/Mode 06, smoke machine, scope, gas analyzer, ...]

Please:
1. Restate the candidate as a falsifiable claim.
2. Enumerate the quorum set — the independent tests that must each agree (each must be a distinct witness, not a repeat of one suspect sensor).
3. Mark each member satisfied / failed / not-yet-collected.
4. Verdict: quorum met (ready to commit) or not met (list the exact missing/contradicting test and how to collect it).
```

## Expected Output

- The candidate as a falsifiable claim
- A witness list with each member's status and why it's independent
- A met / not-met verdict with the next decisive test if not met
