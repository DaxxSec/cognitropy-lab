# /threat-decay-model

Model the rate at which a site loses heritage value in place, so the CBA can price the **cost of inaction** and rank rescue urgency.

## Inputs

- Threat mechanisms present: physical (scour, storm exposure, sediment loss), biological (shipworm, microbial), anthropogenic (trawling, anchoring, development, looting), and climate (warming, deoxygenation, sea-level/erosion change).
- Environmental data: sediment mobility, exposure history, biological activity, proximity to fishing/shipping/development.
- Significance figure (from `/site-significance-score`).
- Planning horizon and discount rate.

## Steps

1. Read `context/concepts.md` ("Site Formation Theory") — preservation potential and threat are two sides of the same process.
2. For each mechanism, estimate an **annual probability of significant loss** and the fraction of value it would remove (some threats are catastrophic, some erosive).
3. Combine into a **value-decay curve** over the horizon: expected surviving significance vs. time under the do-nothing option.
4. Compute **expected heritage loss** = significance × cumulative loss probability over the horizon, discounted.
5. Separate **aleatoric** uncertainty (will a storm hit this year?) from **epistemic** (we don't know the scour rate) — they motivate monitoring vs. survey respectively.
6. Translate into urgency: imminent + catastrophic → rescue/stabilisation now; slow + erosive → monitor and re-evaluate.
7. Feed the expected-loss figure into `/insitu-vs-excavate` (the do-nothing branch).

## Output

`outputs/threat-decay-<site>-YYYY-MM-DD.md`: per-mechanism probabilities, the value-decay curve, the discounted expected-loss figure, the aleatoric/epistemic split, and an urgency classification.

## Notes

- Looting risk rises sharply once a site's location is public — factor disclosure into the threat model.
- Climate threats (deoxygenation reversing anoxic preservation, increased storminess) are increasingly the binding mechanism and are easy to omit.
- The expected-loss figure is the entire economic case for rescue archaeology — get its probability right or the CBA is hollow.
