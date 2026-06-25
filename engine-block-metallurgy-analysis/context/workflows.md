# Engine Block Metallurgy Analysis — Workflows and Methodology

Step-by-step procedures and decision trees the agent runs. The spine is the **Bayesian failure-analysis loop**; the other workflows feed evidence (likelihood ratios) into it.

## Workflow 1: The Bayesian failure-analysis loop

**Goal:** Convert a stack of lab observations into a defensible posterior distribution over root causes.

### Steps

1. **Frame the hypothesis space.** Enumerate mutually-distinguishable root causes for this part + symptom (e.g. H₁ casting defect, H₂ thermal fatigue, H₃ overheat/abuse, H₄ mechanical overload). Add a catch-all "other/undetermined."
2. **Set prior odds.** Anchor on base rates for this material and service condition (see `context/references.md` priors table). A high-mileage field return tilts priors toward service causes; a near-zero-hours warranty failure tilts toward material/casting causes. Write the priors down as probabilities summing to 1.
3. **Collect evidence in decreasing order of expected information.** Usually: composition → metallography → fracture/defect → mechanical. Each finding gets a **likelihood ratio** vs. each hypothesis (how probable is *this* observation if H is true?).
4. **Update sequentially** with `/bayes-evidence-update`: multiply odds by each LR in log-odds space; keep a running ledger of (finding, LR, source standard).
5. **Check independence.** Before multiplying two LRs, confirm the findings aren't two views of the same physical event; if correlated, combine them into one LR or model the dependency.
6. **Report the posterior.** Leading cause + probability, runner-up + probability, and the single test with the highest expected posterior swing still outstanding.

### Decision Points

- If the posterior leader is < 0.6 and a cheap discriminating test exists → recommend that test before concluding (highest value of information).
- If two hypotheses share all available evidence (LRs ≈ equal) → they are not yet separable; say so and identify the orthogonal test that breaks the tie.
- If composition is already off-spec → raise the casting/material prior *before* weighing microstructure, but do not collapse to certainty.

## Workflow 2: Metallographic examination (evidence generator)

**Goal:** Produce graphite, matrix, and defect observations with calibrated likelihood ratios.

### Steps

1. Section per `/sample-prep-protocol`; keep orientation (transverse vs longitudinal to the suspected crack) recorded.
2. Mount, grind (120→1200 grit), polish (9→3→1 µm diamond, final 0.05 µm colloidal silica).
3. **As-polished read first** — graphite morphology and porosity are judged before etching (etching attacks graphite edges and can mimic flake).
4. Etch (2% Nital for matrix; see references) and read matrix phases, chill, steadite, any martensite/decarb.
5. Quantify: graphite type/size/distribution (A247), nodularity % (image analysis, ASTM E2567/ISO 945-4), inclusion rating (E1245), phase fractions (E562 point count).
6. Translate each quantified observation into an LR against the live hypotheses and pass to Workflow 1.

### Decision Points

- If as-polished shows degenerate graphite in a Mg-treated iron → strong LR for material/process escape; check residual Mg in composition.
- If matrix shows martensite only at a hot zone → localized overheat (service), not bulk heat-treat error.

## Workflow 3: Compositional verification (anchors the prior)

**Goal:** Confirm material identity and grade conformance; quantify the probability the part met spec.

### Steps

1. Run OES (bulk) and/or XRF (spot); capture instrument + calibration date.
2. Compute carbon equivalent and compare microstructure prediction (hypo/hypereutectic, chill tendency) to what metallography showed — they must agree.
3. Compare each element to the grade spec window; flag deviations with their measurement uncertainty (±) so "marginal" is distinguished from "clearly out."
4. Produce a conformance probability per element using the measurement uncertainty, then a joint conformance assessment.

### Decision Points

- If an element is within ±1 measurement-uncertainty of the limit → "indeterminate," not "pass/fail"; recommend re-test.
- If residual Mg low in a part expected to be ductile/CGI → strong evidence toward graphite-degeneration cause.

## Methodology Phases — ASM-style failure analysis (Vol. 11)

The case structure that the Bayesian loop runs inside:

### Phase 1 — Collection of background data and as-received documentation
Service history, part identity, intended grade; photograph and dimension before touching the part.

### Phase 2 — Non-destructive and visual examination
Visual, dye-penetrant/MPI, dimensional. Locate the crack origin region *before* sectioning so the cut preserves it.

### Phase 3 — Destructive characterization
Sectioning, metallography, fractography (SEM), composition, hardness/mechanical. This is where Workflows 2–3 generate evidence.

### Phase 4 — Synthesis and reporting
Run the Bayesian update (Workflow 1), state the posterior, recommend corrective action and the outstanding high-value test. Retain the archive specimen.
