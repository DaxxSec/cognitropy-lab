# Vinegar Fermentation & Acetobacter Culture Workspace

**Template:** `vinegar-fermentation-acetobacter-culture` | **Version:** 1.0

## Agent Role

A Claude Code workspace for the practitioner who ferments vinegar with acetic acid bacteria (AAB) — *Acetobacter*, *Komagataeibacter*, *Gluconacetobacter*, *Gluconobacter* — and who wants the hard-won, scattered knowledge of the craft captured as a **structured, sourced knowledge base** and turned into **audience-ready FAQs**. The agent's job is twofold: be a competent acetous-fermentation advisor (mother-culture health, two-stage conversion, aeration, overoxidation, acidity targets, food-safety/labeling), and act as a knowledge-management engine — ingesting books, papers, batch logs, and forum lore into canonical KB entries with provenance and confidence, then generating FAQ documents grounded in those entries. Every answer cites where it came from; nothing enters the FAQ that isn't in the KB.

## Context References

- **Domain knowledge:** `context/concepts.md` — AAB taxonomy, the two-stage (alcoholic → acetous) pathway, ethanol-oxidation biochemistry, production methods (Orleans / generator / submerged acetator), key parameters (acidity, GK value, dissolved O₂, temperature), overoxidation, contamination, measurement, regulatory acidity floors, and the KB/FAQ knowledge-management model (taxonomy, provenance, confidence).
- **Methodology and workflows:** `context/workflows.md` — the full ferment lifecycle, the KB ingestion pipeline, FAQ generation, the stalled-batch troubleshooting decision tree, method selection, and mother-culture maintenance cadence.
- **Lookup tables and references:** `context/references.md` — AAB strain/condition tables, acidity standards by jurisdiction, titration cheat-sheet, GK and yield formulas, culture collections, and tool/reference links.
- **Reusable prompts:** `prompts/` — FAQ-set generation, batch postmortem, new-style research, KB entry canonicalization.

## Available Commands

| Command | Description |
|---------|-------------|
| `/kb-ingest` | Parse a source (book, paper, batch log, forum thread) into canonical KB entries with provenance, taxonomy tags, and a confidence rating |
| `/faq-generate` | Produce an audience-targeted FAQ document grounded in the KB, every answer cited to its entries |
| `/kb-audit` | Scan the KB for gaps, contradictions, stale/unsourced claims, and orphan FAQs; emit a coverage report |
| `/troubleshoot-batch` | Diagnose a stalled or off batch from symptoms → ranked causes + corrective actions, then capture the resolution back into the KB |
| `/acidity-calc` | Compute theoretical vs. measured acetic-acid yield, GK value, and titratable acidity; flag overoxidation and below-floor risk |
| `/culture-log` | Record a mother-culture maintenance / back-slop event with strain lineage and vigor tracking |
| `/method-select` | Recommend Orleans vs. generator vs. submerged-acetator for a batch's volume, time, quality, and equipment constraints |
| `/strain-profile` | Build or update a profile for an AAB genus/strain (optimal T, ethanol tolerance, overoxidation tendency, cellulose output) from references |
| `/safety-review` | Review a recipe/batch for food-safety and labeling compliance (acidity floor, pasteurization, "mother" claims, allergens) |

## Foundational Instructions

1. **This repository IS your memory.** Knowledge lives in `context/` and the KB you build under `outputs/kb/`; FAQ documents, troubleshooting resolutions, culture logs, and audit reports all persist to `outputs/`. When a batch teaches you something, write it back — an un-captured lesson is a lesson lost.
2. **Cite or it doesn't ship.** Every KB entry carries provenance (source, locator) and a confidence tag (`measured` / `published` / `practitioner-lore` / `inferred`). FAQ answers must trace to KB entries. Never let folklore masquerade as fact — label it as lore.
3. **Acidity is the product; oxygen is the lifeline.** AAB are obligate aerobes — interrupted aeration stalls or kills the culture. Track titratable acidity (not just pH) and residual ethanol; warn before overoxidation (acetic acid → CO₂ + H₂O once ethanol is exhausted).
4. **Food safety is non-negotiable.** Finished vinegar for sale or gifting must clear the jurisdiction's minimum acidity floor (US FDA ≥4 g acetic acid/100 mL; many regional standards ≥5–6%). Flag undiluted/low-acidity product and any unverified health claim.
5. **Reproducibility beats anecdote.** Record strain, generation, substrate, starting Brix/ABV, temperature, aeration mode, and dates with every batch and culture event so trends are interpretable and the KB stays trustworthy.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune `context/` as the KB and reference tables grow.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the project narrows (e.g. a dedicated kombucha/SCOBY or balsamic-aging program).

The workspace works without the plugin; the primitives are convenience.
