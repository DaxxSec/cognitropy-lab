# Workflows — Designing & Assessing a Curriculum Bayesianly

How an instructional designer actually moves from a competency statement to a live,
posterior-driven curriculum. The eight phases map onto the commands; the worked example and
decision trees are what the agent imitates.

---

## The eight-phase methodology

### Phase 1 — Define competencies & objectives  → `/draft-objectives`
Start from the competency or accreditation outcome. Decompose into 4–12 objectives, each with a
Bloom verb, ABCD condition/degree, and a one-line justification of why it matters. The **Degree**
becomes the mastery threshold later — write it as something a posterior can clear.

### Phase 2 — Build the skill graph  → `/build-skill-graph`
Arrange objectives into a prerequisite DAG. Draw an edge A→B only if mastering A is genuinely
needed before B is learnable. Keep it sparse. Note for each edge the strength of dependence (this
seeds the CPT). The graph is simultaneously the sequencing plan and the remediation router.

### Phase 3 — Elicit priors  → `/elicit-prior`
For each objective set a `Beta(α₀, β₀)` (or BKT `p-init`). Three sources, in order of preference:
1. **Baseline data** — a pretest gives empirical successes/failures → direct Beta counts.
2. **Cohort history** — prior offerings' mastery rates → informative prior with modest strength.
3. **SME judgement** — elicit a most-likely mastery and a confidence; convert to (α, β).
Record the source and strength. A strong prior on no evidence is a red flag.

### Phase 4 — Design evidence & assessments  → `/map-evidence`, `/design-mastery-check`
Bind each objective to ≥ 1 item that elicits the right Bloom level. For each item set slip `s` and
guess `g` (ECD evidence model). `/design-mastery-check` then sizes the checkpoint: how many items
of what quality are needed so the *posterior* credible interval is narrow enough to decide. High-`g`
items need more of them to reach the same certainty.

### Phase 5 — Instantiate the student model  → (`/build-skill-graph` + priors)
Combine the graph, priors, and evidence models into a runnable model: discrete Bayesian net
(`pgmpy`), per-skill BKT (`pyBKT`), or a hierarchical IRT model (PyMC/Stan). This is the object that
gets updated.

### Phase 6 — Update mastery during instruction  → `/update-mastery`
As responses arrive, update posteriors (BKT for sequential learning, Beta closed form for a fixed
checkpoint). Output per objective: posterior mean, credible interval, and the met / not-yet
decision.

### Phase 7 — Adaptive sequencing  → `/sequence-content`
Pick each learner's next objective: the lowest unmastered node whose prerequisites are mastered
(maximise expected learning, avoid items the learner can't yet attempt). Route failures *backward*
to the implicated prerequisite, not forward.

### Phase 8 — Summative Bayesian evaluation  → `/evaluate-curriculum`, `/audit-alignment`
After a cohort, evaluate the design itself: Bayesian A/B or pre-post on mastery gains (posterior,
ROPE, P(improvement)), plus an alignment audit to catch objectives that drifted from their
assessments. Feed conclusions back into Phase 1.

---

## Worked example — one BKT update

Skill: "compute a conditional probability". Parameters `p-init=0.30, p-transit=0.15,
p-slip=0.10, p-guess=0.20`. Current belief before opportunity *t*: `Lₜ = 0.30`.

**Observation: learner answers correctly.**

1. Condition on correct:
   `L'ₜ = 0.30·(1−0.10) / [ 0.30·(0.90) + 0.70·0.20 ]`
   `     = 0.27 / (0.27 + 0.14) = 0.27 / 0.41 ≈ 0.659`
2. Apply learning: `Lₜ₊₁ = 0.659 + (1−0.659)·0.15 ≈ 0.659 + 0.051 = 0.710`

One correct answer moved belief from 0.30 → 0.71. **A second correct** (repeat with `Lₜ=0.710`):
condition → `0.710·0.9 / (0.710·0.9 + 0.290·0.2) = 0.639 / (0.639+0.058) ≈ 0.917`; learn →
`0.917 + 0.083·0.15 ≈ 0.929`. Two corrects ⇒ `≈0.93` — still short of a `0.95` mastery rule, which
is the point: high-guess items make the model appropriately cautious.

**Contrast: an incorrect after the first correct** (`Lₜ=0.710`): `0.710·0.10 / (0.710·0.10 +
0.290·0.90) = 0.071 / (0.071+0.261) ≈ 0.214`, then learn → `≈0.331`. One slip-or-genuine-error
drops belief hard — exactly why you don't declare mastery on a single correct.

---

## Decision tree — "met / re-teach / advance"

```
After updating P(mastery) for the current objective:

  posterior mean ≥ threshold (e.g. 0.95)?
    └─ yes → is the 80% CI lower bound ≥ floor (e.g. 0.80)?
              ├─ yes → MET → /sequence-content for the next node
              └─ no  → mastery likely but uncertain → give 1–2 more items
                       (/design-mastery-check sized for the gap), re-update
    └─ no  → mean materially below threshold (e.g. < 0.6)?
              ├─ yes → NOT MET → route to the implicated prerequisite
              │        (/sequence-content backward), re-teach, then re-assess
              └─ no  → borderline (0.6–0.95) → deliver more practice on THIS
                       objective, keep updating until it resolves up or down
```

## Decision tree — "is this item carrying evidence?" (used in `/calibrate-bkt`)

```
Fitted parameters for an item/skill:
  p-slip > 0.30 OR p-guess > 0.30 ?
    ├─ p-guess high  → too cueing / too easy to guess → add distractors,
    │                  remove giveaways, or convert to constructed response
    ├─ p-slip high   → ambiguous wording / construct-irrelevant load →
    │                  rewrite stem, isolate the construct
    └─ both fine     → keep; item is informative
  Also: many parameter sets fit equally (flat likelihood)?
    └─ identifiability problem → constrain S,G < 0.3, add priors, pool learners
```

## Curriculum-evaluation workflow (`/evaluate-curriculum`)

1. Define the outcome (e.g. mean posterior mastery across objectives, or fraction of objectives
   met) for control (old design) and treatment (revision).
2. Put a prior on the effect; compute the **posterior over the effect size** (PyMC/Stan, or a
   Beta-difference for proportion-met).
3. Define a **ROPE** — the band of effect sizes too small to act on (e.g. ±0.02 of proportion met).
4. Decide:
   - CI entirely outside ROPE, on the positive side → **adopt**.
   - CI entirely inside ROPE → **practically equivalent**, don't churn the curriculum.
   - CI straddling → **inconclusive**, gather more cohorts.
5. Report `P(effect > 0)` and the decision, not a p-value.
