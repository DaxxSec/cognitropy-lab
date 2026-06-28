# Radiology Interpretation Diagnosis — Core Concepts

Background the agent reads before acting. This workspace QA's molecular-gastronomy **spherification** through the **interpretive discipline of diagnostic radiology**: a finished sphere is "read" like an imaging study — checked for technical adequacy, swept with a fixed search pattern, given a differential and a standardized category, and governed by an FMEA. Optimised for fast recall, not exhaustive theory.

## The governing analogy

A radiologist does not look and pronounce. They (1) confirm the study is *technically adequate*, (2) sweep it with a disciplined **search pattern** so no region is skipped, (3) describe each **finding** neutrally, (4) build a **differential diagnosis** ranked by likelihood, (5) assign a **structured category** (a RADS score) that maps to a management action, and (6) issue a **report**. Spherification QA deserves the same rigor. A sphere has an adequacy gate (degassed, buffered, correctly dosed), inspectable regions (shape, membrane, surface, buoyancy, burst, flavor), defects with multiple possible causes, and a process whose risk can be ranked. Read the batch; don't taste-and-shrug.

## Spherification chemistry taxonomy

- **The reaction.** Sodium alginate (a brown-seaweed polysaccharide of β-D-mannuronate **M** and α-L-guluronate **G** blocks) cross-links in the presence of divalent calcium (Ca²⁺) via the **"egg-box" model**: Ca²⁺ ions chelate buckled G-blocks, zipping chains into a gel membrane. **High-G** alginates gel firm and brittle; **high-M** gel soft and elastic.
- **Basic spherification.** Alginate (≈0.5–1.0%) is blended into the *flavored liquid*; droplets fall into a **calcium bath** (calcium chloride ≈0.5–1.0%, or calcium lactate). A membrane forms outside-in. Gelling **continues as long as Ca²⁺ keeps diffusing inward**, so basic spheres keep thickening and must be rinsed and served within minutes — they eventually gel solid.
- **Reverse spherification.** Calcium lives in the *base* (calcium lactate or **calcium lactate gluconate** ≈1–2%); droplets fall into an **alginate bath** (≈0.5%). The membrane forms inside-out and **stops gelling once the sphere leaves the bath**, so reverse spheres are stable, storable, and liquid-cored indefinitely. Preferred for **acidic, alcoholic, or high-calcium (dairy)** liquids.
- **Frozen reverse spherification.** Freeze the calcium base in hemisphere molds, then bathe the frozen pucks in the alginate bath — yields perfectly round, large spheres ("ravioli," yolks) with controllable membrane.
- **The pH gate.** Alginate gels poorly below **pH ≈ 3.6**; acidic bases must be buffered up with **sodium citrate** (which also sequesters interfering ions). This is the single most common silent failure.
- **Viscosity & buoyancy control.** Thin liquids tail into teardrops; **xanthan gum** thickens them so droplets stay round. Trapped air (from un-rested alginate) makes spheres **float**, which leaves the top membrane thin and rupture-prone — alginate solutions must **rest/refrigerate to degas** (often 15 min–overnight).
- **Water chemistry.** Hard tap water's Ca²⁺ can prematurely gel an alginate bath; **sodium hexametaphosphate** (or distilled water) sequesters it. Calcium **chloride** tastes bitter/saline (bath only, rinse well); calcium **lactate / lactate gluconate** are flavor-neutral (safe in the eaten base).

## Diagnostic-radiology interpretation taxonomy

- **Technical adequacy.** Before reading, confirm the study is diagnostic: correct exposure, positioning, no motion/artifact. A non-diagnostic study is *repeated*, not over-read. (Spherification analog: degassed, buffered, dosed, calibrated bath.)
- **Search pattern.** A fixed, exhaustive scan path (e.g. chest-film **ABCDEF**: Airway, Bones, Cardiac, Diaphragm, Effusions, Fields/Foreign-bodies). Defends against **satisfaction of search** — stopping after the first abnormality and missing a second.
- **Finding vs interpretation.** A *finding* is an observation ("3 mm thin spot on the upper pole"); the *interpretation* is its meaning. Keep them separate so the report is reproducible.
- **Differential diagnosis & gamuts.** For a finding, enumerate causes ranked by probability. A **gamut** (Reeder) is a finding-keyed list of candidate causes — exactly the structure used here for defect→root-cause.
- **Structured reporting / RADS.** ACR Reporting & Data Systems (**BI-RADS** breast, **LI-RADS** liver, **Lung-RADS**, **PI-RADS** prostate, **TI-RADS** thyroid) map findings to a **category 0–5/6**, each with a *management recommendation*. The category is the deliverable — it standardizes language and forces an action.
- **Modality appropriateness.** **ACR Appropriateness Criteria** pick the right modality for a clinical question (X-ray vs CT vs MRI vs US). Analog: pick basic vs reverse vs frozen-reverse for a liquid.
- **Diagnostic performance.** Sensitivity, specificity, PPV/NPV, ROC. Inspection methods have these too (does the float test actually catch thin membranes?).
- **Reliability & peer review.** **Double reading**, inter-observer agreement via **Cohen's κ**, and **RADPEER** peer review. Analog: independent tasters scoring "burst," reconciled.
- **Diagnostic error.** Cognitive traps: **satisfaction of search**, **anchoring**, **premature closure**, **framing/availability bias**. Reviewed at **M&M / error-rounds**.

## The crosswalk (the workspace's central model)

| Diagnostic radiology | Spherification QA |
|---|---|
| Imaging study (the radiograph) | A batch of spheres (the specimen under read) |
| Modality choice (ACR Appropriateness) | Method choice: basic / reverse / frozen-reverse for this liquid |
| Technically adequate study | Diagnostic-quality batch: degassed, buffered (pH≥3.6), dosed, bath calibrated |
| Search pattern (ABCDEF; no satisficing) | Inspection pattern: shape → membrane → surface → buoyancy → burst → flavor |
| Finding (a described abnormality) | A defect observation (tail, float, thin spot, rubbery core, weeping) |
| Differential diagnosis (ranked causes) | Ranked **process** causes of the defect |
| Gamut (finding → DDx list) | Defect gamut (defect → candidate root causes) |
| RADS category 0–5 + management | Sphere-RADS 0–5 + management action (remake / re-rest / serve) |
| Structured report (impression + rec) | Structured QA report (impression + corrective action) |
| Sensitivity / specificity / PPV | Inspection-method sensitivity (float test, squeeze test) |
| Double reading / κ / RADPEER | Inter-taster reliability; reconciled discordance |
| Hounsfield density / quantitative measure | Membrane thickness, bath time, °Brix, pH (the quantitative axis) |
| Satisfaction of search | Stopping at the first defect, missing co-occurring ones |
| Anchoring / premature closure | "It's always the alginate %" — fixing on one cause too early |
| Follow-up / surveillance interval | Re-test interval (basic: minutes; reverse: stable/storable) |
| FMEA / HFMEA (patient-safety) | Process FMEA: failure modes ranked by RPN = S×O×D |

## FMEA (today's technique)

**Failure Mode and Effects Analysis** scores each failure mode on three 1–10 scales — **Severity** (how bad the effect on the plate/guest), **Occurrence** (how often it happens), **Detection** (how *un*likely it is to be caught before service; 10 = nearly undetectable). **RPN = S × O × D** (1–1000); rank descending and attack the top. The modern **AIAG-VDA** approach supplements RPN with an **Action Priority (AP: High/Medium/Low)** lookup to avoid RPN's threshold games. Radiology uses the same tool as **Healthcare FMEA (HFMEA)** for patient-safety process risk — which is exactly why it bridges cleanly into structured spherification QA.

## Common Failure Modes

- **Skipped adequacy gate** — reading a non-degassed/un-buffered batch and "diagnosing" a defect that is really a prep error.
- **Satisfaction of search** — logging the first defect (e.g. tailing) and missing the co-occurring one (thin membrane), so the corrective action is incomplete.
- **Anchoring** — blaming alginate concentration for every defect when the differential points elsewhere (air, bath time, pH).
- **Over-bathing (basic)** — leaving basic spheres in the calcium bath too long → fully gelled, rubbery, no liquid burst.
- **Under-buffered acid** — acidic base below pH 3.6 won't gel; membrane is fragile or absent.
- **Air entrapment** — un-rested alginate → floaters with thin, rupture-prone top membranes.
- **Calcium-chloride carry-over** — insufficient rinse → bitter/metallic spheres scored as a "flavor finding."

## Operating Constraints

- **Food-grade only, culinary doses.** Hydrocolloids and calcium salts must be food-grade; calcium chloride stays in the bath, not the eaten base.
- **Allergens & labeling.** Alginate is seaweed-derived; reverse bases are often dairy/nut. Declare allergens; for sale, label additives (EU E-numbers: alginate E401, CaCl₂ E509, calcium lactate E327, sodium citrate E331).
- **The analogy is methodological.** Sphere-RADS and "differential" borrow medical *rigor*, not medical authority — nothing here is clinical advice.
