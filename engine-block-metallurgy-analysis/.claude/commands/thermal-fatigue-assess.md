# /thermal-fatigue-assess

Assess thermal-fatigue and high-cycle-fatigue cracking risk in hot-zone features (valve bridges, bore bridges, deck) and fit a remaining-life estimate using a Bayesian-prior Weibull model.

## Inputs

- Crack location and pattern (network of short oxidized cracks → thermal; single striated origin → HCF)
- Material and its expected thermal-fatigue resistance; service thermal cycling history if known
- Any prior fleet failure data for this part/grade (counts and times) to inform the reliability prior

## Steps

1. Classify the cracking: thermal fatigue (multiple short cracks, oxidized faces, hot zone) vs. mechanical HCF (single origin, striations) vs. combined — use `/fracture-surface-read` output.
2. Identify the driver: ΔT magnitude and cycle count, restraint geometry, and any material contributor (chill, steadite network, low nodularity lowering fatigue strength).
3. Set a **Bayesian reliability prior** on the Weibull shape/scale (β, η) from grade base rates or fleet history; treat the observed failure time(s) as data.
4. Update the posterior on (β, η); report the posterior B10/characteristic life with a credible interval — a few failures sharpen an a-priori estimate without a full fleet test.
5. Convert "material lowered fatigue resistance" vs. "service over-cycled the part" into a likelihood ratio and pass to `/bayes-evidence-update`.

## Output

`outputs/<case-id>/thermal-fatigue.md`: crack classification, driver analysis, the Weibull posterior (β, η, B10 with credible interval), and the LR contribution separating material vs. service cause.

## Notes

- Thermal-fatigue networks are usually oxidized on the crack faces — a clean fracture face argues for a recent mechanical event instead.
- Don't over-trust a Weibull fit on 1–2 failures without an informative prior; report the credible interval, not just a point life.
