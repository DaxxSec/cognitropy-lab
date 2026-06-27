# References — Lookup Tables & Sources

Compact lookup data for the commands. Not prose — cheat-sheets, ranges, and pointers.

---

## Bloom's revised taxonomy — verbs by level (cognitive process)

| Level | Use for objectives like | Sample measurable verbs |
|---|---|---|
| Remember | recall facts/terms | define, list, label, name, recall, state |
| Understand | explain ideas | summarize, classify, explain, paraphrase, infer |
| Apply | use in new situations | compute, execute, implement, solve, demonstrate |
| Analyze | break down, relate | differentiate, organize, attribute, compare, deconstruct |
| Evaluate | judge against criteria | critique, justify, appraise, defend, select |
| Create | produce new work | design, construct, generate, compose, plan |

**Avoid as objective verbs** (not observable): understand, know, appreciate, be aware of,
be familiar with, grasp, learn. Replace with a verb above.

---

## ABCD checklist

- [ ] **Audience** named · [ ] **Behavior** = observable verb · [ ] **Condition** stated ·
  [ ] **Degree** = the future mastery threshold.

---

## BKT parameter ranges (sanity bounds)

| Param | Meaning | Typical | Hard cap (else degenerate) |
|---|---|---|---|
| p-init `P(L₀)` | already mastered before instruction | 0.1 – 0.4 | — |
| p-transit `P(T)` | learn per opportunity | 0.05 – 0.3 | — |
| p-slip `P(S)` | master answers wrong | 0.05 – 0.2 | **< 0.30** |
| p-guess `P(G)` | non-master answers right | 0.1 – 0.3 | **< 0.30** (≤ 0.25 for 4-option MC) |

If a fit returns `S` or `G` ≥ 0.5 the model is "gaming" the data → constrain and/or fix the item.

---

## Beta prior cheat-sheet

| Beta(α, β) | Interpretation | Strength (α+β) |
|---|---|---|
| Beta(1, 1) | uniform — no information | 2 |
| Beta(2, 2) | weakly centered at 0.5 | 4 |
| Beta(8, 2) | likely already capable (mean 0.8) | 10 |
| Beta(2, 8) | likely novice (mean 0.2) | 10 |
| Beta(20, 5) | strong belief in capability (mean 0.8) | 25 |

- Posterior after `k`/`n`: `Beta(α+k, β+n−k)`. Mean `(α+k)/(α+β+n)`.
- SME elicitation → (α, β): pick mean `m` and pseudo-count `c`; set `α = m·c`, `β = (1−m)·c`.

---

## Mastery decision thresholds (common conventions)

| Stakes | Posterior-mean threshold | CI rule |
|---|---|---|
| Formative / practice | 0.80 | mean only |
| Course objective | 0.90 – 0.95 | 80% CI lower bound ≥ 0.75 |
| High-stakes / certification | 0.95+ | 90% CI lower bound ≥ 0.85 |

---

## ROPE defaults for curriculum evaluation

- Proportion-of-objectives-met effect: ROPE ≈ ±0.02 to ±0.05.
- Standardized mean gain (Cohen's d-like): ROPE ≈ ±0.1.
- Adopt when the credible interval lies wholly outside the ROPE on the positive side.

---

## ECD glossary

- **Student model** — latent mastery variables (what we hold beliefs about).
- **Evidence model** — `P(response | mastery)`; carries slip/guess and the scoring rules.
- **Task model** — the item family that elicits the evidence.
- **Construct-irrelevant variance** — response variation caused by something other than the
  target skill (reading load, UI, time pressure).
- **Constructive alignment** — objective, activity, and assessment all target the same verb/level.

---

## Key papers & books

- Corbett, A. & Anderson, J. (1995). *Knowledge Tracing.* User Modeling and User-Adapted Interaction.
- Mislevy, R., Almond, R. & Lukas, J. (2003). *A Brief Introduction to Evidence-Centered Design.* ETS.
- Anderson, L. & Krathwohl, D. (2001). *A Taxonomy for Learning, Teaching, and Assessing.*
- Biggs, J. & Tang, C. *Teaching for Quality Learning at University* (constructive alignment).
- Mager, R. *Preparing Instructional Objectives.*
- Kruschke, J. (2014). *Doing Bayesian Data Analysis* (Beta–Bernoulli, ROPE, credible intervals).
- Pardos, Z. & Heffernan, N. (2010). *Modeling Individualization in a BKT model.*
- VanLehn, K. (2006). *The Behavior of Tutoring Systems.* (mastery/ITS context)
- Embretson, S. & Reise, S. *Item Response Theory for Psychologists.*

## Standards / frameworks

- Quality Matters (QM) Rubric — alignment of objectives, assessments, materials, activities.
- Bloom's Digital Taxonomy — verb mappings for online tasks.
- Backward Design (Wiggins & McTighe, *Understanding by Design*) — start from desired evidence.

## Tooling

| Tool | Use | Link |
|---|---|---|
| pyBKT | fit & predict BKT from response logs | https://github.com/CAHLR/pyBKT |
| pgmpy | discrete Bayesian networks (skill graph) | https://pgmpy.org |
| PyMC | hierarchical IRT, custom evidence models | https://www.pymc.io |
| cmdstanpy / Stan | same, with Stan backend | https://mc-stan.org |
| numpy / scipy.stats | closed-form Beta–Bernoulli, Beta quantiles | https://scipy.org |
