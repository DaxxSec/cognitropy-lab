# Curriculum Design — Bayesian Learning-Objective Assessment

> A Claude Agent workspace for writing measurable learning objectives and designing curricula
> whose mastery decisions are driven by **Bayesian evidence** — posterior mastery probabilities,
> not seat-time or a single cut score.

Most curriculum tooling stops at "write a learning objective and a quiz." This workspace treats
the whole curriculum as a **probabilistic model**: each objective is a claim about a latent
mastery variable, each assessment item is observable evidence with a known error rate
(slip/guess), and "this learner has met the objective" is a *posterior credible interval clearing
a threshold*. It is built around three complementary frameworks — **Bloom-aligned objective
design**, **Evidence-Centered Design (ECD)**, and **Bayesian Knowledge Tracing (BKT)** — so the
objectives you write are the same objects your assessment engine updates beliefs about.

It is a daily Cognitropy build: **Education & Training**, technique *Bayesian probability
assessment*. (Engine roll was *Finance & Economics / macroeconomics GDP modeling*; the slug
collided with an existing build, so the deterministic anti-collision fallback selected this
domain while preserving the Bayesian technique — a fitting pairing.)

## What you can do with it

- Turn fuzzy competency statements into **measurable, evidenceable objectives** (Bloom verb +
  ABCD condition/degree) each carrying an explicit prior mastery assumption.
- Lay objectives out as a **prerequisite skill graph** (a Bayesian network DAG) so sequencing
  and remediation follow the dependency structure.
- **Elicit Beta priors** from subject-matter experts or cohort baselines and update them with
  evidence as learners work.
- Run **Bayesian Knowledge Tracing** to maintain a live `P(mastery)` per objective and decide
  met / re-teach / advance by a credible-interval rule.
- **Calibrate** BKT parameters from historical response logs and diagnose degenerate fits.
- **Evaluate** a curriculum revision with a Bayesian A/B comparison (posterior over the effect,
  ROPE, probability of improvement) instead of a p-value.

## Getting started

**Prerequisites**

- Claude Code (or any agent runner that reads `CLAUDE.md` + `.claude/commands/`).
- For the quantitative commands, a Python 3.10+ environment with any of: `pyBKT` (BKT fitting),
  `pgmpy` (Bayesian networks), `PyMC` or `cmdstanpy` (general Bayesian inference), `numpy`/`scipy`.
  The commands degrade gracefully to closed-form Beta–Bernoulli math when no PPL is available.
- Learner response data is optional to start: you can design objectives, skill graphs, and
  evidence models with SME-elicited priors before any data exists.

**Quick start**

1. Open this folder as your workspace; `CLAUDE.md` orients the agent.
2. `/draft-objectives` for the unit you're building — start from the competency, get back
   measurable objectives with priors.
3. `/build-skill-graph` to wire the objectives into a prerequisite DAG.
4. `/map-evidence` to bind objectives to assessment items and set slip/guess parameters.
5. As responses arrive, `/update-mastery` to maintain posteriors and `/sequence-content` to
   pick what each learner does next.
6. After a cohort completes, `/evaluate-curriculum` to judge whether a revision actually helped.

## Command reference

| Command | Inputs | Output |
|---|---|---|
| `/draft-objectives` | Topic/competency, level, cohort context | Measurable objectives w/ Bloom level, ABCD parts, prior |
| `/build-skill-graph` | Objective set | Prerequisite DAG + edge rationales + CPT stubs |
| `/elicit-prior` | Objective, SME inputs or baseline data | Beta(α, β) prior + interpretation |
| `/map-evidence` | Objectives, item bank | Objective→item map + slip/guess per item (ECD evidence model) |
| `/update-mastery` | Learner responses, priors, evidence model | Posterior `P(mastery)` + credible interval + decision |
| `/sequence-content` | Skill graph, current posteriors | Ranked next-objective recommendation + rationale |
| `/calibrate-bkt` | Historical response logs | Fitted (p-init, p-transit, p-slip, p-guess) + identifiability report |
| `/design-mastery-check` | Objective, target interval width | Assessment blueprint (item count, mix, stop rule) |
| `/evaluate-curriculum` | Pre/post or A/B outcome data | Posterior over effect, ROPE decision, write-up |
| `/audit-alignment` | Objectives, activities, assessments | Alignment matrix + orphan/gap/mis-level flags |

## Directory structure

```
curriculum-design-learning-objectives/
├── CLAUDE.md                  # Agent role + command index
├── README.md                  # This file
├── .claude/commands/          # 10 bespoke domain commands
├── context/
│   ├── concepts.md            # Objectives, ECD, BKT, Bayesian nets, IRT, failure modes
│   ├── workflows.md           # 8-phase methodology + BKT worked example + decision trees
│   └── references.md          # Bloom verbs, parameter ranges, priors, papers, tooling
├── prompts/                   # Reusable prompt templates
└── outputs/                   # Generated objective sets, graphs, posteriors, reports
```

## Example use cases

1. **New micro-credential.** Design 12 objectives for an "Intro to Statistics" badge, wire the
   prerequisite graph (descriptive → probability → inference), and set a mastery rule of
   `P(mastery) ≥ 0.90` with the 80% credible interval above 0.75.
2. **Adaptive remediation.** A learner fails two items on "hypothesis testing"; `/update-mastery`
   drops the posterior below threshold and `/sequence-content` routes them back to the
   "sampling distributions" prerequisite rather than forward.
3. **Item-bank triage.** `/calibrate-bkt` reveals an item with `p-guess = 0.6` — effectively a
   coin flip; it's flagged for revision because it carries almost no evidence.
4. **Course revision decision.** After piloting a flipped-classroom version, `/evaluate-curriculum`
   returns a 93% posterior probability that mastery gains improved, with the effect's credible
   interval mostly outside the ROPE — a defensible "adopt" decision.
5. **Accreditation alignment.** `/audit-alignment` produces the objective ↔ activity ↔ assessment
   matrix accreditors ask for and flags two objectives with no aligned assessment.

## Recommended tools / MCP servers

- **pyBKT** — fast BKT fitting and prediction from response logs.
- **pgmpy** — discrete Bayesian networks for the skill graph + exact/approx inference.
- **PyMC / Stan (cmdstanpy)** — hierarchical IRT, partial pooling across cohorts, custom evidence models.
- A filesystem MCP server to persist objective sets and posteriors under `outputs/`.

## Notes on rigor & ethics

- **Reproducibility:** always record priors, evidence-model parameters, and the data window used.
  A posterior without its prior is not a result.
- **Construct validity:** Bayesian machinery does not rescue a misaligned objective — garbage
  evidence, confident garbage posterior. Run `/audit-alignment` first.
- **Equity:** subgroup-biased priors or items with differential slip/guess can systematically
  under-credit mastery; surface and correct these, don't launder them through the math.

## References

- Corbett & Anderson (1995), *Knowledge Tracing: Modeling the Acquisition of Procedural Knowledge.*
- Mislevy, Almond & Lukas (2003), *A Brief Introduction to Evidence-Centered Design.*
- Anderson & Krathwohl (2001), *A Taxonomy for Learning, Teaching, and Assessing* (revised Bloom).
- Biggs & Tang, *Teaching for Quality Learning at University* (constructive alignment).
- Kruschke (2014), *Doing Bayesian Data Analysis* (Beta–Bernoulli, ROPE, credible intervals).
- pyBKT: https://github.com/CAHLR/pyBKT · pgmpy: https://pgmpy.org · PyMC: https://www.pymc.io
