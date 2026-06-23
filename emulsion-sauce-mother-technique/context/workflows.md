# Emulsion Sauce Mother Technique — Workflows and Methodology

Procedures and decision trees, organised around today's technique: **peer-review workflows**. `concepts.md` says what things are; this file says what the agent *does*.

## Workflow 1: The peer-review pipeline (the spine)

**Goal:** Move a formula from draft to canonical sign-off with a defensible review trail.

### Phases

1. **Submit** — Author provides the formula + intended use (dip, dress, coat, hold-for-service). Assign a formula ID and a round number (R1).
2. **Normalise** — Run `/formula-normalize`: convert to ratio / baker's-% notation, list controlled variables (ratio, emulsifier load, temperature, shear method, oil-addition rate), flag missing values. Reviewers compare normalised forms, never prose.
3. **Safety pre-screen** — Gate: raw-yolk → pasteurised? acid/pH adequate? hold conditions defined? A Safety class-4 here stops the round; no sensory work on an unsafe formula.
4. **Assign reviewers** — ≥3 reviewers, author excluded from blinded scoring. Confirm the panel is calibrated (`/reviewer-calibrate`) — if κ/ICC is below threshold, calibrate before scoring.
5. **Generate evidence** — Run `/stability-assay` (objective stability) and `/tasting-panel` (sensory). Discrimination test first ("is the change even detectable?"), then descriptive/hedonic if it is.
6. **Score against rubric** — Each reviewer scores stability, texture, flavour balance, reproducibility, safety on the defined scale; defects logged via `/defect-grade`.
7. **Moderate** — `/review-round` aggregates: weighted score, defect tally, inter-rater agreement. Moderator resolves splits and writes the verdict.
8. **Verdict** — *Sign-off* / *minor revise* / *major revise* / *reject*. Sign-off **requires** reproducibility evidence (≥2 preparers × ≥2 replicates).
9. **Revise & re-review** — Minor revise → re-review only the changed delta (next round R2 scoped). Major revise → full re-review.
10. **Publish** — On sign-off, write a sign-off certificate to `outputs/` (formula ID, normalised formula, scores, panel agreement, allergen list, reviewers, date). It becomes a mother eligible for `/derivative-design`.

### Decision Points

- If **Safety class-4** at any phase: reject immediately; route back to author.
- If **inter-rater agreement below threshold** (e.g. ICC < 0.6): the *panel* failed, not the formula — recalibrate and re-score, do not issue a verdict.
- If **stability fails but flavour wins**: major revise toward stability (more emulsifier, finer shear, ratio fix) — a tasty sauce that breaks on the pass is a reject for service use.
- If only the **delta changed** since last sign-off: scope a minor re-review, don't re-validate the whole mother.

## Workflow 2: Building the mother emulsion (the technique itself)

**Goal:** Produce a stable, reproducible mother emulsion as a control or sign-off candidate.

### Steps (cold yolk mayonnaise as the canonical example)

1. Bring yolk, acid, and oil to **room temperature** (reduces break risk).
2. Combine the **water phase first**: yolk + a little acid (lemon/vinegar) + salt + optional mustard (insurance emulsifier). Whisk to loosen.
3. **Start the oil drop-by-drop**, whisking (or blending) continuously, until the mixture visibly thickens and "takes" (the emulsion is established).
4. **Accelerate** the oil to a thin steady stream; maintain shear. Thin with a few drops of water/acid if it gets too stiff (re-opens the water phase for more oil).
5. **Finish:** adjust seasoning and acid last; record final ratio, total oil per yolk, shear method, time.
6. Log everything for `/formula-normalize`. A batch with no variable log cannot be a control.

### Warm-emulsion (hollandaise) variant

- Make an acid reduction (or use lemon). Whisk yolks + a little water over a **bain-marie**; cook until ribbon stage (~63–70 °C) — thickened but never scrambled.
- Off heat, whisk in **warm clarified butter** slowly. Hold within the safe-warm band; if it thickens too far, loosen with warm water.
- Hold-time clock starts now; log it for safety review.

## Workflow 3: Break diagnosis and repair

**Goal:** Decide whether a failed emulsion is recoverable, and how.

### Decision tree

1. **Is it broken (coalesced) or just creamed (separated, droplets intact)?**
   - *Creamed* (re-whisking re-blends it): just re-emulsify; not a true failure.
   - *Broken* (greasy, curdled, won't re-blend): continue.
2. **Cold sauce (mayo/aïoli) broke:** start a fresh emulsion base (a clean bowl with a teaspoon of water or a fresh yolk or a bit of made mayo) and **whisk the broken sauce into it slowly**, drop by drop — re-stabilising the released oil into new droplets.
3. **Warm sauce (hollandaise) curdled from heat:** if curds are mild, whisk a spoon of cold water (or an ice cube) off-heat to drop temperature and re-emulsify; if severely scrambled, start a new yolk base and whisk the broken sauce in.
4. **Root-cause** (record for review): oil added too fast? ratio too oil-heavy (crowding)? temperature wrong? insufficient emulsifier? — feed the cause back into `/formula-normalize` so the next round fixes the variable, not the symptom.

## Workflow 4: Deriving a daughter sauce

**Goal:** Expand the family from a signed-off mother with a scoped review.

### Steps

1. Start from a **signed-off** mother (cite its formula ID and certificate).
2. Express the daughter as a **delta**: additions (garlic → aïoli, tarragon reduction → béarnaise), substitutions, or ratio tweaks.
3. Check the delta doesn't break the emulsion budget (e.g. watery additions reduce stability; add as paste or reduce first).
4. Scope review to the **delta only** (flavour/texture impact of the addition + any stability change) — the mother is already validated.
5. Run a focused `/tasting-panel` (often a duo-trio vs the mother) and a quick `/stability-assay` if the addition is aqueous.
6. Sign off the daughter referencing the mother; update the family tree in `outputs/`.

## Methodology Phases — Sensory test selection

### Phase 1 — Discrimination ("is it different?")
Triangle test (pick the odd sample of three) or duo-trio. Establishes that a formula change is *perceptible* at all before spending effort characterising it.

### Phase 2 — Description ("how is it different?")
Quantitative Descriptive Analysis with a trained panel: rate attributes (gloss, body, acidity, fattiness, garlic intensity) on fixed scales. Produces a sensory profile.

### Phase 3 — Affective ("is it preferred?")
9-point hedonic liking scale with naïve consumers, or paired-preference. Only meaningful after discrimination confirms a real difference and the panel is calibrated.
