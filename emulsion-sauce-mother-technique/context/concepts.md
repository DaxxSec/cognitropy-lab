# Emulsion Sauce Mother Technique — Core Concepts

Background the agent should read before acting. Two halves: the **emulsion science + sauce taxonomy**, and the **peer-review model** that governs how technique changes are validated. Optimised for fast recall.

## What an emulsion is

An emulsion is a kinetically stable dispersion of one immiscible liquid as droplets within another. Two types matter in sauce work:

- **Oil-in-water (o/w)** — fat droplets dispersed in a water phase. This is the family that matters here: mayonnaise, hollandaise, vinaigrette (when emulsified) are all o/w. The continuous (outer) phase is water-based, which is why they feel light/creamy rather than greasy.
- **Water-in-oil (w/o)** — water droplets in a fat phase (butter, some spreads). Rare in classic sauce work.

Emulsions are **thermodynamically unstable** — left alone, droplets coalesce and the phases separate to minimise interfacial energy. The cook's job is to make them *kinetically* stable for long enough: small droplets, enough emulsifier at the interface, and a continuous phase viscous enough to slow droplet movement.

### Stability tiers (this drives everything)

| Tier | Holds for | Examples | What provides stability |
|------|-----------|----------|--------------------------|
| **Temporary** | seconds–minutes | shaken vinaigrette | mechanical only; no/weak emulsifier |
| **Semi-permanent** | hours–days | mustard vinaigrette, beurre blanc | partial emulsifier (mustard, milk solids, lecithin) |
| **Permanent** | weeks (refrigerated) | mayonnaise, aïoli | full emulsifier load (egg yolk lecithin + protein), small droplets |

Hollandaise is a special case: chemically permanent-capable (yolk lecithin) but **thermally fragile** — held warm, protein can over-coagulate (curdle) or the fat can break out if temperature swings.

## The emulsion "mother" technique and the family tree

In the classical (Carême → Escoffier) mother-sauce system, the emulsified branch has two mothers; everything else is a **derivative (daughter)** made by controlled substitution:

- **Mayonnaise** (cold, raw egg yolk + neutral oil + acid) → **aïoli** (+ garlic), **rémoulade** (+ cornichon/caper/herb/mustard), **tartare** (+ pickle/caper/herb), **Marie Rose / cocktail** (+ ketchup/brandy), **gribiche** (+ chopped cooked egg) [gribiche is yolk-based, often grouped here].
- **Hollandaise** (warm, egg yolk + clarified butter + acid reduction) → **béarnaise** (tarragon/shallot/vinegar reduction), **choron** (béarnaise + tomato), **foyot/Valois** (béarnaise + meat glaze), **maltaise** (+ blood-orange), **mousseline/Chantilly** (+ whipped cream), **noisette** (+ brown butter).
- **Vinaigrette** (acid + oil ± emulsifier) → the open-ended dressing family.

**Mother-technique principle:** validate the mother once, and a daughter is a *documented delta* (one or two controlled additions), not a new recipe to re-validate from scratch. This is exactly why the peer-review framing fits — a daughter's review can be scoped to its delta.

## The five emulsion variables

Every emulsion outcome is governed by these. They are the controlled variables in any review:

1. **Phase ratio (oil : water).** More oil → thicker, but past ~3:1–4:1 by volume for yolk mayo the emulsion crowds and risks breaking. Water phase too small = nothing to disperse into.
2. **Emulsifier load.** Egg yolk supplies **lecithin** (phospholipid surfactant) + **lipoproteins**. One large yolk stabilises roughly 175–250 mL (¾–1 cup) of oil. Mustard, milk solids, honey, and even garlic paste add emulsifying/co-stabilising capacity.
3. **Droplet size (shear).** Finer shear (immersion blender) = smaller droplets = thicker, more stable, whiter sauce. Whisk = coarser, glossier, more fragile.
4. **Temperature.** Cold sauces tolerate fast oil addition poorly; ingredients near room temp emulsify more reliably. Warm sauces (hollandaise) must stay in a narrow band — yolk thickens ~63–70 °C, curdles ~80–85 °C.
5. **Oil-addition rate.** The classic lever: add oil too fast before enough droplets are formed and stabilised → the emulsion can't keep up → break. Start drop-by-drop, accelerate once it "takes."

### HLB (Hydrophilic-Lipophilic Balance)

Griffin's HLB scale (0–20) rates a surfactant's water vs oil affinity. **o/w emulsifiers need HLB ≈ 8–18.** Egg-yolk lecithin (~8) sits at the low end of the o/w range — it works for sauces because it's paired with yolk lipoproteins and the right phase ratio. Useful as a reasoning tool when proposing non-traditional stabilisers.

## Why emulsions break (failure physics)

- **Coalescence** — droplets merge because too little emulsifier covers the interface, or droplets are too large (under-sheared).
- **Creaming / sedimentation** — droplets rise (oil) or settle under gravity (Stokes' law: rate ∝ droplet radius² × density difference / viscosity). Bigger droplets and thin continuous phase = fast separation. Often reversible by re-mixing if not yet coalesced.
- **Phase inversion** — too much dispersed phase flips o/w into w/o; the sauce suddenly turns greasy/oily.
- **Thermal break (hollandaise)** — over-heating coagulates yolk protein into curds and releases the butterfat; under-heating never sets.
- **Acid/salt shock** — dumping acid or salt at the wrong moment can destabilise the protein network.

## Defect taxonomy (what reviewers grade)

| Class | Defect | Typical cause |
|-------|--------|---------------|
| Appearance | broken/oiled-off, weeping, dull | coalescence, creaming, under-shear |
| Texture | too thin, too thick/gluey, grainy/curdled | wrong ratio, over-shear, thermal break |
| Flavour | flat, over-acidic, raw-oil/bitter, over-salted | balance error, low-quality oil, seasoning |
| Safety | unsafe raw egg, danger-zone hold | unpasteurised yolk, no hold-time control |

Severity is graded on a **0–4 scale** (see `references.md`): 0 = none, 1 = minor, 2 = noticeable, 3 = major, 4 = critical/reject. Any single class-4 (especially Safety) is an automatic reject regardless of other scores.

## The culinary peer-review model (today's technique)

Peer review here borrows the structure of scientific/editorial review and adapts it to sensory work:

- **Roles.** *Author* (proposes the formula), *reviewers* (score independently against the rubric), *moderator/editor* (aggregates, resolves disputes, issues the verdict). The author is never an unblinded sensory scorer of their own formula.
- **Blinding.** *Single-blind* (tasters don't know which sample is which), *double-blind* (server doesn't either). Blinding kills the "I made it so it's good" bias.
- **Rubric.** A fixed set of weighted criteria (stability, texture, flavour balance, reproducibility, safety) scored on a defined scale so verdicts are comparable across formulas and rounds.
- **Inter-rater reliability.** Reviewers must *agree* before their scores mean anything. Measured with **Cohen's κ** (two raters, categorical), **Krippendorff's α**, or **intraclass correlation (ICC)** for ratings. Calibrate first (`/reviewer-calibrate`); untrained panels produce noise dressed as data.
- **Sensory test types.** *Discrimination* (triangle test, duo-trio: "are these different?"), *descriptive* (Quantitative Descriptive Analysis: trained panel rates attributes), *affective/hedonic* (9-point liking scale, naïve consumers). Use discrimination to prove a change is detectable, descriptive to characterise it, hedonic to prove preference.
- **Verdict states.** *Accept / sign-off*, *minor revise* (re-review only the delta), *major revise* (full re-review), *reject*. Sign-off requires reproducibility evidence (≥2 preparers × ≥2 replicates), not just a winning taste score.

## Common Failure Modes

- **Single-replicate sign-off** — declaring a formula "validated" from one good batch by one cook; it won't reproduce.
- **Unblinded enthusiasm** — the creator scores their own sauce highly; the review is theatre.
- **Uncalibrated panel** — reviewers disagree wildly, so the data is unusable; mistaken for "the sauce is controversial."
- **Confusing creaming with breaking** — a creamed (separated-but-intact) emulsion is often re-mixable; treating it as broken wastes the batch.
- **Chasing flavour while ignoring stability** — the tastiest sauce that breaks on the pass fails in service.
- **Mixing certification conditions** — comparing a sauce held at 4 °C against one held at room temp and calling the difference "the formula."

## Operating Constraints

- **Food safety is non-negotiable.** Raw-yolk sauces → pasteurised egg + acidification; warm sauces → hold-time + temperature control (danger zone 4–60 °C / 40–140 °F). A safety failure overrides any sensory result.
- **Reproducibility is a sign-off gate**, not a nice-to-have: ≥2 preparers × ≥2 replicates with logged variables.
- **Allergen tracking** is mandatory on every signed-off formula (egg, mustard, dairy, oils/nuts).
