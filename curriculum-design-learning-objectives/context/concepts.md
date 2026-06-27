# Concepts — Bayesian Learning-Objective Assessment

This is the domain knowledge the commands draw on. It connects three normally-separate
literatures: how to **write** learning objectives, how to **structure evidence** about them
(Evidence-Centered Design), and how to **reason** about mastery under uncertainty (Bayesian
inference, Bayesian Knowledge Tracing).

---

## 1. Learning objectives — what makes one measurable

A learning objective is a statement of what a learner will be able to *do*. To be usable as a
Bayesian claim it must be **observable** (so evidence can bear on it) and **bounded** (so a
posterior can be thresholded).

**Revised Bloom's taxonomy (Anderson & Krathwohl, 2001)** — the cognitive-process dimension,
ascending:

1. Remember · 2. Understand · 3. Apply · 4. Analyze · 5. Evaluate · 6. Create

Each level pairs with a knowledge dimension (factual, conceptual, procedural, metacognitive).
The verb signals the level and therefore the *kind of evidence* that counts: "list" (Remember) is
evidenced by recall items; "critique" (Evaluate) requires a constructed response or rubric.

**ABCD format** — a fully specified objective names:

- **A**udience — who ("the learner")
- **B**ehavior — an observable verb ("derives", "classifies")
- **C**ondition — under what circumstances ("given a labeled dataset, without a calculator")
- **D**egree — the standard ("with ≥ 90% of cases correct", "within 2 significant figures")

The **Degree** is what later becomes the mastery threshold. "Understands recursion" is not
evidenceable; "traces a recursive function's call stack for an input of depth ≤ 4 with no errors"
is.

**SMART** objectives (Specific, Measurable, Achievable, Relevant, Time-bound) and **Mager's**
three-part objectives (performance, condition, criterion) are compatible restatements of ABCD.

**Constructive alignment (Biggs).** The objective, the learning activity, and the assessment must
target the same verb at the same Bloom level. Misalignment — teaching "apply" but assessing
"remember" — is the single most common defect and *no amount of Bayesian assessment fixes it*,
because the evidence is measuring the wrong construct.

---

## 2. Evidence-Centered Design (ECD)

ECD (Mislevy, Almond & Lukas) is the bridge from objectives to a probabilistic model. It separates
three models that the commands populate:

- **Student model** — the latent variables we care about: mastery of each objective/skill. In the
  Bayesian framing these are the things we hold posteriors over.
- **Evidence model** — how an observed response relates to the latent variable: the *scoring*
  (what counts as correct) and the *measurement* link, i.e. `P(response | mastery state)`. This is
  where **slip** and **guess** live.
- **Task model** — the family of tasks/items that can elicit the evidence (item format, stimulus,
  affordances).

The evidence model is the conditional probability table that makes Bayesian updating possible.
For a binary item and a binary skill it has just two numbers:

- **slip** `s = P(incorrect | mastered)` — a master makes a careless error.
- **guess** `g = P(correct | not mastered)` — a non-master gets it right by luck or partial cue.

So `P(correct | mastered) = 1 − s` and `P(correct | ¬mastered) = g`. An item with high `g` (e.g.
4-option MC with cues) or high `s` (ambiguous wording) carries little evidence — this is why item
quality and the inference are inseparable.

---

## 3. Bayesian updating of mastery — the Beta–Bernoulli core

Treat mastery probability `θ` for an objective as an unknown in `[0,1]`. The **Beta(α, β)**
distribution is the conjugate prior for Bernoulli/binomial evidence:

- Prior `Beta(α₀, β₀)`. Interpret `α₀` as "prior successes + 1-ish", `β₀` as "prior failures";
  `α₀+β₀` is the prior's *strength* (pseudo-count). `Beta(1,1)` is uniform (no information);
  `Beta(8,2)` says "probably already fairly capable".
- Observe `k` successes in `n` independent attempts → posterior `Beta(α₀ + k, β₀ + n − k)`.
- Posterior mean `= (α₀+k)/(α₀+β₀+n)`. Posterior **credible interval** (e.g. the central 80%)
  is read directly off the Beta quantiles.

This conjugacy is what lets `/update-mastery` and `/design-mastery-check` run in closed form with
no sampler. The catch: raw Beta–Bernoulli assumes each attempt is an i.i.d. draw from a *fixed*
`θ` — fine for a snapshot mastery check, wrong when learning is happening between attempts. For the
learning-over-time case, use BKT.

---

## 4. Bayesian Knowledge Tracing (BKT)

BKT (Corbett & Anderson, 1995) is a two-state hidden Markov model per skill: the latent state is
**mastered / not-mastered**, and it can *transition* from not-mastered to mastered between
opportunities (learning). Four parameters:

- **p-init** `P(L₀)` — probability the skill is already mastered before instruction (the prior).
- **p-transit** `P(T)` — probability of moving unmastered → mastered at each opportunity.
- **p-slip** `P(S)` — `P(incorrect | mastered)`.
- **p-guess** `P(G)` — `P(correct | ¬mastered)`.

**Update (per response).** Let `Lₜ = P(mastered before opportunity t)`.

1. Condition on the observed response (Bayes):
   - if correct: `L'ₜ = Lₜ(1−S) / [ Lₜ(1−S) + (1−Lₜ)G ]`
   - if incorrect: `L'ₜ = Lₜ·S / [ Lₜ·S + (1−Lₜ)(1−G) ]`
2. Account for learning during the opportunity: `Lₜ₊₁ = L'ₜ + (1−L'ₜ)·T`.

Predicted probability of a correct *next* response: `Lₜ(1−S) + (1−Lₜ)G`.

BKT is the time-aware generalisation of the Beta–Bernoulli snapshot: `/update-mastery` uses BKT
when responses are sequential across instruction, and the Beta closed form for a single
fixed-mastery checkpoint.

**Mastery decision.** A common rule is "mastered when `P(Lₜ) ≥ 0.95`". Prefer the
credible-interval-aware version: require the posterior mean over threshold *and* the lower bound of
the chosen credible interval above a floor, so a wide, uncertain posterior doesn't trip the rule.

---

## 5. Bayesian skill networks (prerequisite graphs)

When objectives have prerequisite structure, model them as a **Bayesian network** (a DAG of
skill nodes). Edges encode that mastery of a prerequisite raises the prior on a dependent skill;
conditional probability tables (CPTs) quantify "given prerequisites mastered/not, P(this skill)".
Benefits:

- Evidence on one skill propagates: nailing an advanced item raises belief in its prerequisites
  ("explaining away" and backward inference).
- Sequencing falls out of the graph — never recommend a node whose parents are still unmastered.
- Tools: `pgmpy` for discrete nets; dynamic Bayesian networks (DBNs) generalise BKT to multi-skill,
  multi-step settings.

Keep the graph **sparse and defensible** — every edge should have an instructional rationale, or
inference becomes an uninterpretable tangle.

---

## 6. Item Response Theory (IRT) — when items vary in difficulty

BKT treats items of a skill as interchangeable. When items differ systematically in difficulty,
IRT models `P(correct)` as a function of learner ability `θ` and item parameters:

- **Rasch / 1PL:** difficulty `b` only.
- **2PL:** difficulty `b` + discrimination `a`.
- **3PL:** adds a guessing asymptote `c` (the IRT cousin of BKT's guess).

Estimating ability and item parameters Bayesianly (e.g. hierarchical priors in PyMC/Stan) gives
partial pooling across learners and items — valuable with sparse data. Use IRT when the item bank
is heterogeneous; use BKT when the question is "has this learner mastered the skill *yet*".

---

## 7. Decisions under the posterior — credible intervals & ROPE

- **Credible interval (CI):** the Bayesian interval — "there's a 90% probability mastery is in
  [0.78, 0.94]". Report it; thresholding the mean alone hides uncertainty.
- **ROPE (Region of Practical Equivalence):** a band around "no effect" used in
  `/evaluate-curriculum`. To claim a revision helped, the effect's credible interval should sit
  largely *outside* the ROPE. This replaces the p-value with a statement about practically
  meaningful change.
- **Probability of improvement:** `P(effect > 0)` read off the posterior — directly answers the
  stakeholder's actual question ("did it get better?").

---

## 8. Common failure modes

| Failure | Symptom | Mitigation |
|---|---|---|
| **Misalignment** | High posteriors but learners can't perform | `/audit-alignment` before trusting any number |
| **Degenerate BKT** | `p-slip > 0.5` or `p-guess > 0.5` after fitting | Constrain `S,G < 0.3`; the model is "gaming" the data; revise the item |
| **Prior misspecification** | Posteriors barely move / move wildly | Match prior strength to real prior knowledge; do a prior predictive check |
| **Construct-irrelevant variance** | Reading load or UI confounds the skill | Isolate the construct in the task model |
| **Identifiability** | Many parameter sets fit equally | Bound parameters, add priors, pool across learners (hierarchical) |
| **Threshold on the mean** | A wide posterior trips "mastered" on luck | Require the CI lower bound over a floor, not just the mean |
| **Independence violation** | Items share a stem/scaffold | Score the cluster as one piece of evidence, not n independent ones |
| **Equity blind spot** | A subgroup's mastery is systematically under-credited | Check slip/guess and priors for differential function across subgroups |
