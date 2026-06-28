# Radiology Interpretation Diagnosis — Reference Tables

Lookup data the agent grep's during a task. Compact by design — defer to `concepts.md` for theory and to upstream sources for full specs.

## Sphere-RADS — structured category scale

Modeled on ACR RADS (BI-RADS/Lung-RADS): a category that *carries an action*.

| Category | Meaning | Typical findings | Management action |
|---|---|---|---|
| **RADS-0** | Non-diagnostic | Prep error: un-rested alginate, unbuffered acid, dead bath | Remake; do not interpret |
| **RADS-1** | Negative / ideal | Round, uniform thin membrane, sinks, clean burst, true flavor | Serve; archive as reference batch |
| **RADS-2** | Benign variant | Minor cosmetic (slight tail), no functional defect | Serve; note for cosmetic tuning |
| **RADS-3** | Probably correctable | Floaters, mild thin spots, slight bitterness | Re-rest / re-rinse / re-bath; re-read |
| **RADS-4** | Suspicious / likely fail | Frequent ruptures, rubbery zones, weak burst | Adjust recipe (alginate %, bath time); pilot again |
| **RADS-5** | Failing | Collapse, no membrane, no burst, off-flavor | Reject batch; root-cause via FMEA |

## Defect → gamut (finding-keyed root causes, ranked)

| Defect (finding) | Differential — ranked process causes |
|---|---|
| **Tailing / teardrop** | Low viscosity (add xanthan) → drop height too high → dosing too fast |
| **Floating spheres** | Trapped air (un-rested alginate) → bubbles in base → base less dense than bath |
| **Thin / ruptured membrane** | Bath time too short → alginate % too low → acidic base (pH<3.6) → top thinned by floating |
| **Rubbery, no burst (basic)** | Over-bathed (too long) → calcium too high → sphere fully gelled before serving |
| **Premature gelling in bath (reverse)** | Hard-water bath (Ca²⁺) → bath contaminated → calcium too high in base |
| **Weeping / wrinkled surface (syneresis)** | Over-gelled → held too long → high-G alginate too brittle |
| **Bitter / metallic flavor** | Calcium-chloride carry-over (under-rinsed) → CaCl₂ used in eaten base |
| **Cloudy / grainy** | Undissolved alginate/calcium → blended too cold → un-strained base |

## Spherification recipe quick-reference (starting points; calibrate per liquid)

| Parameter | Basic | Reverse | Frozen reverse |
|---|---|---|---|
| Alginate | 0.5–1.0% in base | 0.5% in **bath** | 0.5% in bath |
| Calcium | CaCl₂ / Ca-lactate 0.5–1.0% in **bath** | Ca-lactate-gluconate 1–2% in base | 1–2% in base (frozen) |
| Bath time | 1–3 min (serve fast) | 2–4 min (then rinse) | until thawed + 2–3 min |
| Best for | neutral, low-Ca, caviar/serve-now | acidic, alcoholic, dairy, make-ahead | large/round, make-ahead |
| Stability | gels through; minutes | stops at bath exit; storable | storable |
| Buffer | citrate if pH<3.6 | citrate in base if acidic | citrate in base if acidic |

## FMEA scoring scales (1–10) + Action Priority

| Score | Severity (effect) | Occurrence (frequency) | Detection (chance it escapes to service) |
|---|---|---|---|
| 1–2 | cosmetic only | rare (<1 batch in 50) | almost always caught |
| 3–4 | minor texture/flavor | occasional | usually caught |
| 5–6 | guest notices, plate off | intermittent | sometimes missed |
| 7–8 | dish unservable | frequent | often missed |
| 9–10 | safety/allergen/choking | nearly every batch | nearly undetectable pre-service |

- **RPN = S × O × D** (1–1000); rank descending.
- **AIAG-VDA Action Priority** (H/M/L) from an S·O·D lookup supersedes hard RPN thresholds in the modern handbook — High AP must be actioned regardless of RPN.

## Inter-rater agreement (Cohen's κ) bands

| κ | Interpretation |
|---|---|
| < 0.20 | slight | 0.21–0.40 fair | 0.41–0.60 moderate | 0.61–0.80 substantial | 0.81–1.00 near-perfect |

## E-numbers / additive labeling (EU)

| Additive | E-number | Role |
|---|---|---|
| Sodium alginate | E401 | gelling polymer |
| Calcium chloride | E509 | bath calcium (bitter) |
| Calcium lactate | E327 | base calcium (neutral) |
| Calcium lactate gluconate | (blend of E327/E578) | reverse base calcium |
| Sodium citrate | E331 | acid buffer / sequestrant |
| Xanthan gum | E415 | viscosity |
| Sodium hexametaphosphate | E452i | water softener (bath) |

## Upstream Catalogues

- **Khymos hydrocolloid recipes** — https://blog.khymos.org/recipe-collection/texture/ — practical alginate/spherification reference.
- **ACR Reporting & Data Systems (RADS)** — https://www.acr.org/Clinical-Resources/Reporting-and-Data-Systems — the structured-category model.
- **ACR Appropriateness Criteria** — https://www.acr.org/Clinical-Resources/ACR-Appropriateness-Criteria — modality-selection logic for `/select-method`.
- **AIAG-VDA FMEA** — https://www.aiag.org/quality/automotive-core-tools/fmea — S/O/D, RPN, Action Priority.
- **Reeder & Felson's Gamuts in Radiology** — https://gamuts.net/ — finding-keyed differential lists.
- **Modernist Cuisine** — https://modernistcuisine.com/ — canonical spherification technique.
