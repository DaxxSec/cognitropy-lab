# Circuit Reliability Review

## Purpose

Periodic health review of a detection's reliability — the "is the circuit still open?" check. Decides keep / retune / retire based on reliability over conditions, not a single snapshot. Run on a cadence (monthly) or after a major environment change.

## Prompt Template

```
You are reviewing the reliability of a production detection rule using the
REL% (reliability over conditions) framing in context/concepts.md.

- **Rule:** [NAME / ID, deployed date, current FOT]
- **Review window:** [DATE RANGE + index versions]
- **Alert outcomes in window:** [TP / FP / muted counts, by hour-of-day if available]
- **Triage branch-path summary:** [mostly Q2-closes? ever reaching Q3? from /triage-tree]
- **Known-bad coverage:** [did it catch purple-team / incident activity? ]

Please:
1. Compute reliability: fraction of attack instances caught vs FP load carried,
   and how both vary across the diurnal cycle.
2. Locate the operating point: at FOT, below LUF (storming/muted), or above MUF (silent)?
3. Recommend keep / retune / retire, with the trigger evidence.
4. If retune: name the root-cause environment change (space weather) and the
   command sequence to fix it.
```

## Expected Output

- A reliability figure with its window (never a bare number).
- The rule's operating-point diagnosis (FOT / below LUF / above MUF).
- A keep/retune/retire decision with evidence.
- For retunes, a root-caused, command-mapped remediation plan.
