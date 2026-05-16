# /regulation-compare — Posterior Probability of Regulatory Compliance

Convert a posterior injury distribution into a **posterior probability of compliance** with a specific regulation (FMVSS, UNECE, Euro NCAP, IIHS). This is the command that produces the deliverable a regulator or court will read.

## Inputs

- Test ID and occupant position.
- Regulation identifier (`FMVSS-208`, `FMVSS-214`, `FMVSS-301`, `UNECE-R94`, `UNECE-R95`, `UNECE-R137`, `EuroNCAP-AOP-2026`, `IIHS-SmallOverlap-2024`).
- Regulation revision date (regulations change; pin the revision in force at test date).
- Output from `/injury-posterior` for the occupant in question.
- Optional: regulatory threshold override (e.g. a proposed amendment value, for regulatory-impact analysis).

## Steps

1. **Pull threshold table.** From `context/references.md`, retrieve the active thresholds for the regulation + revision. For FMVSS 208: HIC15 ≤ 700, Nij ≤ 1.0, chest deflection ≤ 63 mm (5th-female), peak chest accel ≤ 60 g, femur force ≤ 10 kN.
2. **Map posterior to threshold.** For each criterion, compute P(criterion ≤ threshold | data) from the posterior samples produced by `/injury-posterior`. This is the per-criterion compliance probability.
3. **Combine into a joint compliance probability.** Many regulations require **all** criteria to pass — compute P(all criteria within threshold | data) from joint posterior samples (not from independent marginals; the criteria are correlated through shared dummy / vehicle / pulse posteriors).
4. **Report directional margin.** For each criterion, the posterior probability of margin > 10% (and < 10% margin = "tight"), giving a regulator-readable risk picture beyond pass/fail.
5. **Compare against threshold override.** If a proposed regulation revision is provided, repeat the analysis with the new threshold and report ΔP(compliant) — the regulatory-impact estimate.
6. **Cross-reference with `/restraint-likelihood`.** If restraint posterior favours "degraded," the compliance memo must call this out — a tight pass with a degraded restraint is more risky than a tight pass with a healthy restraint.

## Output

`outputs/<test-id>/compliance/<occupant>/<regulation>.md`:
- Per-criterion compliance posterior (median, 5/95 percentiles, P(pass)).
- Joint P(all criteria pass | data).
- Posterior margin to threshold per criterion.
- Restraint-system cross-reference.
- Verbatim citation of the regulation revision in force.

Also `outputs/<test-id>/compliance/<occupant>/<regulation>.json` for downstream tooling.

## Notes

- Many publications report compliance as binary. The posterior probability is more honest: "P(compliant with FMVSS 208 | data) = 0.78" tells a regulator more than "Passed."
- Regulatory revisions sometimes apply different thresholds to different occupant percentiles (5th-female vs. 50th-male vs. 95th-male). Pull the right threshold per occupant.
- When P(compliant) is between 0.5 and 0.8, the responsible answer is to retest or re-elicit the dummy prior — not to publish a borderline claim either way.
- Never paraphrase regulatory text in the deliverable. Quote it.
