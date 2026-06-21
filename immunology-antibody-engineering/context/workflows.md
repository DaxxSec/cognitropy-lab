# Workflows — Antibody Engineering as Apprenticeship Progression

Three interleaved loops. **Loop A** moves a candidate antibody through engineering. **Loop B** is the engineering work itself. **Loop C** is the apprenticeship progression that runs *over* the work — every Loop A/B task is also a logged competency-evidence event for Loop C. The organizing technique this build runs on is **apprenticeship progression tracking**: the work and the learning are the same artifacts.

## Loop A — candidate lifecycle (the science pipeline)

**Goal:** take a binder from discovery to a developable, well-characterized lead.

1. **Intake** — capture parental sequence, discovery route, target, and intended format.
2. **Liability scan** — `/sequence-liability-scan` for chemical degradation motifs.
3. **Humanize (if non-human)** — `/humanize-candidate` → CDR graft + minimal back-mutations.
4. **Characterize binding** — `/binding-kinetics` for intrinsic KD/kon/koff; `/epitope-binning` for epitope diversity.
5. **Mature (if needed)** — `/affinity-maturation-plan` when affinity misses the target.
6. **Developability triage** — `/developability-triage` to rank candidates and pick lead + backups.
7. **Decide** — advance the lead, or loop back to remediate the dominant risk.

### Decision points

- If parental is fully human (display/transgenic/single-B-cell) → skip humanization.
- If KD meets target but developability is Red → remediate developability before celebrating affinity.
- If affinity is off-rate-limited below ~100 pM → confirm the assay can resolve it before launching a maturation campaign.

## Loop B — engineering (where the craft lives)

**Humanization decision tree**

- Pick human germlines by canonical-class match, not just identity.
- Straight graft first; measure the affinity gap.
- Add back-mutations in priority order: VH/VL-interface → Vernier → canonical-determining. Stop at the minimal set that recovers affinity within the loss budget.
- Re-scan every variant for new liabilities; score humanness; present the Pareto front (humanness vs affinity), not one maximal graft.

**Affinity-maturation strategy**

- Diagnose the limiting kinetic parameter (kon vs koff) first — it dictates the selection scheme.
- Choose diversification by library ceiling and target: focused CDR-H3 + hotspot libraries for fine-tuning; chain shuffling / error-prone PCR for broad jumps; DMS for epistasis maps.
- Selection pressure: decreasing antigen for KD, competitor off-rate selection for koff, counter-selection for specificity.
- Confirm combinations (epistasis) rather than stacking single winners; guardrail every advancing clone through `/sequence-liability-scan`.

**Developability-remediation tree**

- Find the dominant risk axis (thermal / colloidal / charge-viscosity / poly-reactivity) — candidates usually fail for one reason.
- Sequence liability in a CDR → conservative substitution preserving the canonical residue; verify binding unchanged.
- Hydrophobic/charge patch → surface mutation away from the paratope; recheck TAP-style flags.
- If remediation costs affinity → route back to Loop B maturation.

## Loop C — apprenticeship progression (the technique, made first-class)

**Goal:** carry each trainee competency from observe-only to independent practice on auditable evidence.

### The progression cycle (per competency)

1. **Baseline** — `/competency-map` places the trainee on the Dreyfus scale per competency from logged evidence.
2. **Assign** — `/skills-gap-plan` maps the next gap onto a *real* Loop A/B task at the right scaffolding level.
3. **Practice** — the trainee runs the task (a real command); the output is tagged with the competency it demonstrates.
4. **Log** — the artifact lands in `outputs/` and in the trainee's logbook as an entrustment-relevant rep.
5. **Review** — `/progression-review` periodically weighs accumulated reps and decides advance / hold / remediate.
6. **Entrust** — `/mentor-signoff` records a scoped entrustment step when evidence supports it.
7. **Repeat** — re-cut the gap plan; tiers can rise, hold, or drift down with disuse.

### Scaffolding by tier (cognitive-apprenticeship moves)

- **Novice** → modeling: trainee observes the mentor run the command and narrate reasoning.
- **Advanced Beginner** → coaching + scaffolding: trainee runs it with the mentor checking each step.
- **Competent** → supervised independence: trainee runs it solo, mentor reviews the artifact after.
- **Proficient** → edge-case exposure: hand the unusual scaffolds, fast off-rates, ambiguous bins.
- **Expert** → articulation/exploration: trainee now mentors others and improves the workspace itself.

### The advancement rule (used by `/progression-review`)

A competency advances a tier only on **consistent evidence across multiple independent reps** plus a **mentor entrustment event** — never on a single good result or on logged hours. Entrustment is scoped (standard work vs edge cases) and revocable.

### Decision points

- If self-rating and logged evidence diverge > 1 tier → hold and gather more reps; do not advance on self-report.
- If a role gate is in play → state explicitly whether the role's required entrustment profile is met, per competency.
- If a competency is going stale (no reps in the window) → flag for a refresh task, not silent demotion.

## Methodology phases (how a session typically runs)

### Phase 1 — frame
Identify whether this session is primarily engineering (Loop A/B), assessment (Loop C), or both; load the relevant `context/` sections.

### Phase 2 — execute
Run the engineering command(s); ensure each output tags its competency and lands in `outputs/`.

### Phase 3 — log & review
Append to the trainee logbook; if it's a review checkpoint, run `/progression-review` and update the `competency-map`.
