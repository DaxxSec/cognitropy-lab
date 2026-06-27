# /build-diagnosticity-matrix

Build and score the ACH evidence × hypothesis matrix, then rank hypotheses by the disconfirming evidence each survives. This is where structured hypothesis testing produces a defensible conclusion.

## Inputs

- The hypothesis set from `/frame-hypotheses`.
- The artifact inventory (extracted + parsed + carved), including notable absences.
- Reliability notes per artifact (tool used, source DB, whether corroborated).

## Steps

1. Lay out a matrix: rows = evidence items (and key absences), columns = hypotheses H1…Hn.
2. Score each cell **C (consistent) / I (inconsistent) / N (not applicable)** — judge consistency with the hypothesis, not "does it support my lead."
3. **Weight by diagnosticity** — evidence consistent with *every* hypothesis carries ~zero weight; flag and largely discount it. Evidence **inconsistent** with one or more hypotheses is what moves the analysis.
4. **Rank hypotheses by the weight of `I` marks against each** — the least-disconfirmed hypothesis survives; do not rank by count of `C` marks.
5. **Sensitivity analysis** — identify the 1–3 evidence items the ranking depends on; test whether a misdate, tool artifact, or planted item flips the result.

## Output

`outputs/ach-matrix-YYYY-MM-DD.md` (and optional CSV): the scored matrix, per-hypothesis disconfirmation tally, the surviving hypothesis with a calibrated confidence, the high-leverage evidence items, and the sensitivity findings.

## Notes

- Rank by refutation, not corroboration — that is the entire point of ACH.
- If the top two hypotheses are near-tied, the data is under-diagnostic: state what artifact would break the tie and go collect it before concluding.
