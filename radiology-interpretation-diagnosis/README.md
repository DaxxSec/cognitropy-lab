# Radiology Interpretation Diagnosis Workspace

> Read molecular-gastronomy spheres like radiographs: a fixed search pattern, a ranked differential for every defect, a Sphere-RADS category that carries an action, and an FMEA that ranks the whole process by risk.

## What This Workspace Does

This is a Claude Code workspace for **quality-controlling molecular-gastronomy spherification** — basic, reverse, and frozen-reverse — built around one borrowed idea: a finished sphere is an *imaging study*, and it deserves to be read with the same discipline a radiologist brings to a chest film. A radiologist does not glance and pronounce. They first confirm the study is *technically adequate* (correct exposure, positioning, no artifacts), then sweep it with a **fixed search pattern** so they don't stop at the first abnormality ("satisfaction of search"), generate a **differential diagnosis** for each finding, and file a **structured report** whose standardized category (a RADS score) maps directly to a management recommendation.

This workspace transplants that interpretive method onto the spherification bench. Before any batch is "read," `/study-quality` checks it is diagnostic-quality (alginate degassed, calcium salt and concentrations in range, acidic bases buffered with citrate). Then `/read-batch` walks a fixed pattern — shape → membrane → surface → buoyancy → burst → flavor — logging every finding. `/differential` ranks the *process* root causes of each defect from a defect **gamut** (the radiology term for a finding-keyed list of causes), `/sphere-rads` assigns a 0–5 category with a built-in action, and `/structured-report` emits the canonical readout. The build's technique is **Failure Mode and Effects Analysis (FMEA)**: `/fmea-process` enumerates the ways spherification fails, scores each by Severity × Occurrence × Detection to get a Risk Priority Number, and drives corrective work by RPN rather than by whichever defect annoyed the chef most recently.

## Why This Workspace Exists

Spherification is notoriously finicky and notoriously taught by anecdote: "rest the alginate," "don't leave them in too long," "use reverse for anything acidic." Each tip is real, but the knowledge is scattered, the failures recur, and a kitchen rarely has a repeatable way to say *why* a batch failed or *how bad* it is. Diagnostic radiology solved the analogous problem decades ago — turning a subjective "looks suspicious" into reproducible categories (BI-RADS, LI-RADS, Lung-RADS), structured reports, double-reading, and formal error review. This workspace codifies spherification QA the same way: a technical-adequacy gate, a search pattern that resists premature closure, a differential discipline, standardized categories with actions, and an FMEA that makes the whole process auditable instead of folkloric.

## Getting Started

### Prerequisites

- Spherification pantry: **sodium alginate**, a calcium salt (**calcium chloride** for baths, **calcium lactate** or **calcium lactate gluconate** for reverse bases), **sodium citrate** (acid buffer), optional **xanthan gum** (viscosity) and **sodium hexametaphosphate** (water softener for reverse baths).
- A **0.01 g scale**, an immersion blender, pipettes/syringes or a spherification spoon, slotted spoons, and a fine sieve.
- A **pH meter or strips** and (optional) a **refractometer** (°Brix) — your quantitative "densitometry."
- Claude Code. No internet required to run the workflow; the recommended MCP servers below are optional enhancers.

### Quick Start

1. Clone this workspace and open it in Claude Code.
2. Run `/select-method` with your target liquid's pH, calcium content, alcohol, and viscosity — it recommends basic vs reverse vs frozen-reverse and a starting recipe.
3. Make a pilot batch, then run `/study-quality` to confirm it's diagnostic-quality before you judge it.
4. Run `/read-batch` to sweep the batch with the fixed search pattern, then `/differential` on any finding and `/sphere-rads` to categorize.
5. Run `/membrane-titration` to lock the bath-time window, and `/fmea-process` to stand up the risk register that governs the recipe going forward.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/select-method` | Pick basic / reverse / frozen-reverse + starting recipe | New liquid, before the first batch |
| `/study-quality` | Technical-adequacy gate before interpretation | Every batch, before reading defects |
| `/read-batch` | Fixed search-pattern inspection; logs all findings | Each batch evaluation |
| `/differential` | Rank process root causes of a defect from its gamut | When a finding needs a cause |
| `/sphere-rads` | Standardized 0–5 category + management action | After the read, to grade the batch |
| `/structured-report` | Canonical QA readout (technique→findings→impression→action) | To document/sign off a batch |
| `/membrane-titration` | Bath-time vs thickness/burst sweep; sets the window | Calibrating a new recipe or salt |
| `/fmea-process` | Build/score the process FMEA; rank by RPN | Standing up or revising the risk register |
| `/double-read` | Inter-taster reliability + discordance reconciliation | Service-critical or disputed batches |
| `/error-rounds` | Retrospective on a service failure; names the bias | After a batch fails in service |

## Directory Structure

```
radiology-interpretation-diagnosis/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke spherification-QA commands
├── context/
│   ├── concepts.md           # Radiology interp + spherification chemistry + the crosswalk
│   ├── workflows.md          # Read pipeline, FMEA loop, method tree, double-read
│   └── references.md         # Sphere-RADS table, recipe cheat-sheet, gamuts, links
├── prompts/                  # 5 reusable prompt templates
└── outputs/                  # Reports, titration sweeps, FMEA tables, error rounds
```

## Example Use Cases

### Bring a temperamental cocktail sphere under control
A mango-passionfruit base keeps rupturing on the pass. `/study-quality` flags the base at pH 3.2 (below alginate's gel threshold), `/select-method` switches it to reverse spherification with a citrate-buffered base, and `/membrane-titration` finds the 2.5–3.5 min bath window that survives plating.

### Diagnose a batch of floating, weak-walled spheres
`/read-batch` logs buoyancy + thin-membrane findings; `/differential` ranks "trapped air from un-rested alginate" above "low alginate %"; `/sphere-rads` scores it RADS-3 (re-rest and re-bath), and the cause feeds straight into the FMEA's detection column.

### Make the recipe auditable for a multi-cook line
`/fmea-process` turns the kitchen's recurring failures into a ranked risk register; `/double-read` quantifies how much two cooks disagree on "burst," and `/error-rounds` converts the last service failure into a standing guardrail instead of a shrug.

## Recommended MCP Servers

- **Filesystem / Git MCP** — version recipes, Sphere-RADS reports, titration sweeps, and the FMEA in `outputs/` as a QA-as-code record across services.
- **HTTP / fetch MCP** — pull hydrocolloid spec sheets and food-additive references (E-numbers, supplier data) to confirm grades, doses, and allergen statements.

## Legal & Ethical Considerations

- **Food safety first.** Use food-grade additives at culinary concentrations only; calcium chloride is bitter and mildly irritating at high dose — keep it to bath use, not the eaten base. Reverse-spherification bases are frequently dairy or nut purées: declare allergens.
- **The radiology analogy is methodological, not clinical.** "Sphere-RADS," "differential," and "FMEA" here borrow medical/engineering *rigor*; nothing in this workspace is medical advice or implies clinical validity.
- **Labeling.** If spheres are sold, disclose additives per local regulation (e.g. EU E-numbers: alginate E401, calcium chloride E509, calcium lactate E327, sodium citrate E331).

## Technical References

- [Khymos — Texture / Hydrocolloids](https://blog.khymos.org/recipe-collection/texture/) — Martin Lersch's hydrocolloid recipe collection; the practical reference for alginate spherification.
- [Modernist Cuisine — Spherification](https://modernistcuisine.com/) — the canonical modern treatment of basic vs reverse spherification.
- [ACR Reporting & Data Systems (RADS)](https://www.acr.org/Clinical-Resources/Reporting-and-Data-Systems) — BI-RADS, LI-RADS, Lung-RADS et al.; the structured-reporting model Sphere-RADS imitates.
- [ACR Appropriateness Criteria](https://www.acr.org/Clinical-Resources/ACR-Appropriateness-Criteria) — evidence-based modality selection; the model for `/select-method`.
- [AIAG-VDA FMEA Handbook](https://www.aiag.org/quality/automotive-core-tools/fmea) — the modern FMEA standard (Severity/Occurrence/Detection, RPN, Action Priority).
- [Reeder and Felson's Gamuts in Radiology](https://gamuts.net/) — finding-keyed differential lists; the model for this workspace's defect gamuts.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
