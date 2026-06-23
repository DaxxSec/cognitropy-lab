# Emulsion Sauce Mother Technique — Reference Tables

Compact lookup data. Defer to upstream sources (McGee, Modernist Cuisine) for fuller treatment.

## Emulsifiers & HLB (o/w needs HLB ≈ 8–18)

| Emulsifier | Source | Role | HLB (approx) | Notes |
|------------|--------|------|--------------|-------|
| Lecithin (phospholipid) | egg yolk, soy | primary surfactant | ~8 | the workhorse of yolk sauces |
| Egg-yolk lipoproteins | egg yolk | co-stabiliser / film | — | paired with lecithin; 1 yolk ≈ 175–250 mL oil |
| Mustard (ground/prepared) | seed | co-emulsifier + flavour | — | mucilage stabilises vinaigrette/mayo |
| Milk solids/casein | dairy, butter | protein stabiliser | — | beurre blanc, mousseline |
| Garlic paste | allium | weak co-stabiliser | — | aïoli leans on yolk; garlic adds little stability |
| Honey | — | viscosity + mild surfactant | — | common vinaigrette stabiliser |

## Mother → daughter family map

| Mother | Base | Daughters (delta) |
|--------|------|-------------------|
| **Mayonnaise** | raw yolk + oil + acid (cold) | aïoli (+garlic), rémoulade (+cornichon/caper/herb/mustard), tartare (+pickle/caper), Marie Rose (+ketchup/brandy), gribiche (+chopped egg) |
| **Hollandaise** | yolk + clarified butter + acid (warm) | béarnaise (+tarragon/shallot reduction), choron (béarnaise+tomato), foyot (béarnaise+meat glaze), maltaise (+blood orange), mousseline (+whipped cream), noisette (+brown butter) |
| **Vinaigrette** | acid + oil ± emulsifier | mustard vinaigrette, honey-dijon, herb/shallot dressings (open-ended) |

## Ratio & stability cheat-sheet

| Sauce | Typical phase ratio | Emulsifier | Stability tier |
|-------|---------------------|------------|----------------|
| Vinaigrette (classic) | ~3:1 oil:acid | none / weak | temporary |
| Vinaigrette (mustard) | ~3:1 | mustard | semi-permanent |
| Mayonnaise | up to ~3–4:1 oil:water-phase by vol | 1 yolk / ~175–250 mL oil | permanent |
| Hollandaise | ~115–175 mL butter / yolk | yolk lecithin | thermally fragile |
| Beurre blanc | butter into reduced acid | milk solids | semi-permanent |

## Temperature reference (warm emulsions)

| Point | Temp | Meaning |
|-------|------|---------|
| Yolk begins to thicken | ~63–65 °C / 145–149 °F | ribbon stage target |
| Yolk fully set / sabayon | ~70 °C / 158 °F | upper working edge |
| Yolk curdles (scrambles) | ~80–85 °C / 176–185 °F | thermal break |
| Food-safety danger zone | 4–60 °C / 40–140 °F | minimise hold time within |

## Defect-severity scale (0–4)

| Grade | Label | Meaning |
|-------|-------|---------|
| 0 | none | no detectable defect |
| 1 | minor | detectable by trained taster only; no impact on use |
| 2 | noticeable | a naïve consumer would notice; usable |
| 3 | major | impairs the sauce's purpose |
| 4 | critical | unusable / unsafe — automatic reject |

> Any **Safety** defect ≥3, or any single class-4, is an automatic round reject regardless of other scores.

## Review rubric (default weights — tune per use-case)

| Criterion | Weight | Scored on |
|-----------|--------|-----------|
| Emulsion stability | 25% | `/stability-assay` grade |
| Texture / mouthfeel | 20% | descriptive panel |
| Flavour balance | 25% | descriptive + hedonic |
| Reproducibility | 20% | preparer × replicate variance |
| Safety | 10% (gate) | pass/fail, overrides on fail |

## Sensory & inter-rater-reliability scales

| Tool | Use | Threshold guidance |
|------|-----|--------------------|
| Triangle test (ASTM E1885) | discrimination | significant if correct picks exceed chance (binomial p<0.05) |
| 9-point hedonic scale | preference/liking | 1=dislike extremely … 9=like extremely |
| QDA (descriptive) | attribute profiling | trained panel, fixed line scales |
| Cohen's κ | 2 raters, categorical | <0.4 poor, 0.4–0.6 moderate, 0.6–0.8 good, >0.8 strong |
| Krippendorff's α | n raters, any scale | ≥0.80 acceptable, 0.667 minimum tolerable |
| ICC | n raters, ratings | <0.5 poor, 0.5–0.75 moderate, 0.75–0.9 good, >0.9 excellent |

## Reproducibility log — required fields

`formula_id, preparer, replicate, phase_ratio, emulsifier_load, oil_addition_rate, shear_method, temperature, ambient_temp, total_time, final_pH, outcome, defect_grades`

## Upstream catalogues

- **Harold McGee, *On Food and Cooking*** — https://www.curiouscook.com/ — emulsion science reference.
- **Modernist Cuisine (Myhrvold et al.)** — https://modernistcuisine.com/ — quantitative emulsion + sauce methodology.
- **Serious Eats / The Food Lab (Kenji López-Alt)** — https://www.seriouseats.com/the-food-lab — tested, reproducible emulsion methods.
- **Escoffier, *Le Guide Culinaire*** — https://en.wikipedia.org/wiki/Le_Guide_Culinaire — classical mother/daughter sauce taxonomy.
- **ASTM sensory standards (E1885 triangle test)** — https://www.astm.org/ — blind discrimination test methods.
- **Griffin HLB scale (1949)** — https://en.wikipedia.org/wiki/Hydrophilic-lipophilic_balance — emulsifier classification.
