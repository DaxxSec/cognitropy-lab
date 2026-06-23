# Emulsion Sauce Mother Technique Workspace

> Develop the foundational emulsified-sauce technique as a peer-reviewed discipline — every formula blind-tasted, replicated across hands, and signed off against an explicit rubric before it joins the canon.

## What This Workspace Does

This workspace treats the **emulsion mother technique** — the core skill of holding fat and water in a single stable phase — as the root of an entire sauce family and develops it the way a research group develops a method: through **peer review**. The cold-yolk line (mayonnaise and its children), the warm-yolk line (hollandaise and its children), and the broken/temporary line (vinaigrette) all descend from one technique with a handful of controllable variables. Get the mother right, document it reproducibly, and the daughters follow.

The peer-review framing is what makes this workspace distinctive. Instead of "the chef tasted it and it's good," a formula here moves through a pipeline: it is **normalised** into ratio notation, assigned **reviewers**, scored against a **rubric** (stability, texture, flavour, reproducibility, safety), put in front of a **calibrated blind panel**, stress-tested for **stability**, graded for **defects**, revised, and only then **signed off**. The output is not a recipe card — it is a technique with a paper trail that a different cook in a different kitchen can reproduce and trust.

It is built for sauce R&D, culinary-school technique standardisation, restaurant menu development, recipe-testing teams (food media, cookbook authors), and anyone who wants their emulsion work to survive contact with another pair of hands.

## Why This Workspace Exists

Emulsion sauces are where home and professional cooks fail most reliably and most mysteriously: mayonnaise that won't come together, hollandaise that curdles on the pass, vinaigrette that splits before it reaches the table. The failures are not random — they are governed by droplet size, phase ratio, emulsifier load, temperature, and shear — but they *feel* random because the technique is usually transmitted as folklore ("add the oil slowly") rather than as a controlled, reviewable method.

This workspace codifies the technique and the review process around it: the physics of why emulsions hold and break, the family tree that lets one validated mother sauce spawn a dozen derivatives, and a peer-review workflow that separates a real improvement from a lucky batch or a flattering palate.

## Getting Started

### Prerequisites

- A working kitchen with the mother-emulsion equipment: balloon whisk and/or immersion blender, bain-marie or double boiler (for warm emulsions), accurate scale (1 g resolution), and an instant-read thermometer.
- Optional but recommended: a small benchtop centrifuge or a way to force-stress emulsions (warm/cold cycling), and identical opaque tasting vessels for blinding.
- Pasteurised egg yolk (or pasteurised-in-shell eggs) for raw-yolk sauces; a food-safety reference for your jurisdiction.
- 3+ tasters available for panel work (calibration needs the same people across sessions).

### Quick Start

1. Clone this workspace and skim `context/concepts.md` for the emulsion + peer-review fundamentals.
2. Run `/emulsify-baseline` to produce a documented control specimen (e.g. a 1-yolk mayonnaise) — every later comparison is against this.
3. Run `/formula-normalize` on any candidate recipe so it is in reproducible ratio notation with a controlled-variable log.
4. Run `/reviewer-calibrate` to align your tasters, then `/review-round` to score the candidate against the rubric.
5. Use `/stability-assay` and `/tasting-panel` to generate the evidence the review round needs, then sign off or revise.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/emulsify-baseline` | Formulate + document a reproducible baseline mother emulsion (the control) | At project start, or when establishing a new house standard to review against |
| `/formula-normalize` | Convert a recipe to ratio / baker's-% notation with a controlled-variable log | Before any formula enters review — reviewers compare normalised forms, not prose |
| `/review-round` | Run one structured peer-review round end-to-end | Each time a draft or revision needs a verdict (accept / revise / reject) |
| `/reviewer-calibrate` | Calibrate the panel for inter-rater reliability | Before trusting any sensory verdict; re-run when tasters change or drift |
| `/tasting-panel` | Design + execute a blind sensory panel and aggregate scores | When a review round needs sensory evidence (discrimination or preference) |
| `/stability-assay` | Stress-test emulsion stability (time/heat/shear/centrifuge) and grade | When stability is a review criterion or two formulas tie on flavour |
| `/break-diagnose` | Diagnose a broken/curdled emulsion and prescribe repair or restart | The moment a batch breaks, or to root-cause a recurring failure |
| `/derivative-design` | Design a daughter sauce off a signed-off mother under reviewer constraints | After a mother is signed off and you want to expand the family |
| `/defect-grade` | Apply the defect-severity taxonomy across appearance/texture/flavour | During review to convert subjective complaints into graded, comparable defects |

## Directory Structure

```
emulsion-sauce-mother-technique/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain commands
├── context/
│   ├── concepts.md           # Emulsion chemistry + family tree + peer-review model
│   ├── workflows.md          # Review pipeline, emulsification, break-repair tree
│   └── references.md          # HLB/emulsifier tables, ratios, defect & sensory scales
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Normalised formulas, review records, panel sheets, sign-offs
```

## Example Use Cases

### Standardising a house mayonnaise across a multi-site restaurant group
Each site's mayo tastes different. Normalise every site's formula, calibrate a cross-site panel, run a blind triangle test, and converge on one signed-off mother that reproduces everywhere.

### Validating a "stabiliser-free hollandaise that holds for service"
A cook claims a hollandaise that survives a 2-hour pass. `/stability-assay` under realistic hold conditions plus a blind panel turns the claim into evidence — or refutes it before it hits the menu.

### Cookbook recipe testing with an audit trail
A cookbook author needs every emulsion recipe to work in readers' kitchens. Two preparers, two replicates, normalised ratios, and a review sign-off per recipe produce the reproducibility the publisher's testers demand.

### Teaching the mother→daughter logic in a culinary program
Use `/emulsify-baseline` + `/derivative-design` to show students how one validated mayonnaise becomes aïoli, rémoulade, and tartare by controlled, reviewed substitutions — not separate recipes.

## Recommended MCP Servers

- **Filesystem MCP** — persist normalised formulas, review-round records, and panel score sheets under `outputs/` as the canonical, diffable review trail.
- **Time / scheduling MCP** — stamp stability assays and hold-time tests accurately (time-on-pass and shelf-life claims live or die on real elapsed time).

## Legal & Ethical Considerations

- **Raw-egg safety.** Mayonnaise and aïoli use raw yolk; default to pasteurised egg and document acid (pH) and hold time. Hollandaise and béarnaise live in the temperature danger zone — set and enforce hold-time limits.
- **Allergen disclosure.** Egg, mustard, dairy (butter sauces), and any nut/seed oils are common allergens; every signed-off formula must carry its allergen list.
- **Honest review.** Blind the panel and disclose reviewer conflicts (the formula's author should not be an unblinded scorer). The point of peer review is to resist exactly the bias an enthusiastic creator brings.

## Technical References

- [Harold McGee, *On Food and Cooking* (emulsions chapter)](https://www.curiouscook.com/) — the standard lay-science account of why emulsions hold and break.
- [Modernist Cuisine — emulsions](https://modernistcuisine.com/) — quantitative treatment of droplet size, emulsifier load, and stability.
- [Serious Eats / The Food Lab — emulsion guides](https://www.seriouseats.com/the-food-lab) — reproducible, tested mayonnaise and hollandaise methodology.
- [ASTM E1885 — Sensory Triangle Test](https://www.astm.org/e1885-04r11.html) — standard method for blind discrimination testing.
- [Griffin, *Classification of Surface-Active Agents by HLB* (1949)](https://en.wikipedia.org/wiki/Hydrophilic-lipophilic_balance) — origin of the HLB scale used to reason about emulsifiers.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
