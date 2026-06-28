# /double-read

Inter-taster reliability protocol: have two assessors independently score the same spheres, quantify agreement, and reconcile discordance — the RADPEER/double-reading analog.

## Inputs

- A batch and the subjective scale in question (usually **burst** and **texture**).
- Two assessors and a sample of N spheres.

## Steps

1. Both assessors score the same N spheres **independently and blind** to each other on the agreed scale.
2. Compute **% concordance** and **Cohen's κ**; band it via `references.md` (κ<0.4 poor … >0.8 near-perfect).
3. Pull the **discordant** spheres and review them together.
4. Classify each disagreement as **definition drift** (the scale is ambiguous) or **real batch variability**.
5. Tighten the scale definition where it drifted; record the κ trend so the QA scale itself improves over time.

## Output

`outputs/double-read-<batch>-YYYY-MM-DD.md` — the paired scores, κ, the discordant set with resolutions, and any scale-definition changes.

## Notes

- Low κ usually means the **scale** is vague, not that an assessor is wrong — fix the definition before blaming a taster.
- Reserve double-reading for service-critical or disputed batches; it's the QA equivalent of a second radiologist, not an every-batch tax.
