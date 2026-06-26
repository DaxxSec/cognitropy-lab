# Vinegar Fermentation & Acetobacter Culture Workspace

> A Claude Code workspace that ferments vinegar *and* its own knowledge — pairing acetic-acid-bacteria fermentation expertise with a sourced knowledge base and on-demand FAQ generation.

## What This Workspace Does

Vinegar making sits at the intersection of microbiology, food chemistry, and craft. The craft knowledge — which strain tolerates 12% ABV, why the mother sank, how to read a stalled batch, what acidity floor your jurisdiction requires — lives scattered across textbooks, papers, forum threads, and the producer's own notebook. This workspace does two things at once: it advises on the **acetous fermentation itself** (two-stage conversion, mother-culture health, aeration, overoxidation, acidity targets, safety), and it runs a **knowledge-management loop** that captures everything learned into a structured, cited knowledge base and turns that base into audience-ready FAQ documents.

The "knowledge base and FAQ generation" technique shapes the whole workspace. Sources go in through `/kb-ingest`, which produces canonical KB entries tagged with a taxonomy, provenance, and a confidence level. `/faq-generate` reads the KB and writes a FAQ document tailored to an audience — home fermenter, craft producer, or educator — with every answer traceable to its source entries. `/kb-audit` keeps the base honest by surfacing gaps, contradictions, and unsourced claims. The domain commands (`/troubleshoot-batch`, `/acidity-calc`, `/strain-profile`, …) feed the same loop: a resolved problem becomes a new KB entry, which becomes a new FAQ answer.

The result is a workspace that gets smarter every batch. The fermentation knowledge compounds instead of evaporating, and the public-facing FAQ is never out of sync with what the producer actually knows.

## Why This Workspace Exists

Acetic acid bacteria are unforgiving teachers. They are obligate aerobes that die quietly when starved of oxygen; they overoxidize a finished vinegar back toward water and CO₂ if you stop watching residual ethanol; and they reward record-keeping while punishing anecdote. Producers accumulate exactly the kind of tacit, troubleshooting-heavy knowledge that a structured KB is built for — but almost no one captures it systematically, so the same questions get re-answered batch after batch.

This workspace codifies the fermentation science **and** the discipline of capturing it. It treats every batch log, every diagnosed failure, and every reference paper as an input to a living knowledge base, and it makes generating a trustworthy, cited FAQ a one-command operation rather than a writing project.

## Getting Started

### Prerequisites

- **Claude Code** with this workspace as the working directory.
- A substrate ferment to work from (cider, wine, diluted spirit, rice wash) or an existing batch program.
- A **mother of vinegar** / AAB starter culture, or an unpasteurized raw vinegar to capture one from.
- Optional but recommended: a titration kit (NaOH + phenolphthalein) or an acidity test kit for titratable acidity, a hydrometer for starting ABV/Brix, and a thermometer.
- Any source material you want in the KB — books, PDFs, batch notebooks, forum exports.

### Quick Start

1. Clone or open this workspace in Claude Code.
2. Skim `context/concepts.md` for the AAB taxonomy and the two-stage pathway, then `context/references.md` for the acidity-standard and strain tables.
3. Seed the knowledge base: run `/kb-ingest` on your first source (a chapter, a paper, or your existing batch notes). Entries land under `outputs/kb/`.
4. Log your live culture with `/culture-log` and sanity-check a batch's numbers with `/acidity-calc`.
5. Generate your first FAQ with `/faq-generate` for the "home fermenter" audience, then run `/kb-audit` to see what the KB is still missing.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/kb-ingest` | Parse a source into canonical KB entries with provenance, taxonomy tags, and confidence | Whenever you have a new book chapter, paper, batch log, or forum thread to absorb |
| `/faq-generate` | Build an audience-targeted FAQ document grounded in the KB, fully cited | When you need a FAQ for a website, product insert, class, or onboarding doc |
| `/kb-audit` | Report KB gaps, contradictions, stale/unsourced claims, and orphan FAQs | Periodically, or before publishing a FAQ, to keep the base trustworthy |
| `/troubleshoot-batch` | Diagnose a stalled/off batch from symptoms → ranked causes + fixes, capture resolution to KB | A batch isn't acidifying, the mother won't form, or there's an off aroma |
| `/acidity-calc` | Theoretical vs. measured acetic-acid yield, GK value, titratable acidity; flag overoxidation | Planning a batch, checking conversion, or deciding when to harvest |
| `/culture-log` | Record a mother-culture maintenance / back-slop event with lineage + vigor | Every time you split, feed, or transfer a mother |
| `/method-select` | Recommend Orleans / generator / submerged-acetator for the batch's constraints | Scaling up, choosing equipment, or balancing speed vs. quality |
| `/strain-profile` | Build/update an AAB genus/strain profile (T, ethanol tolerance, overoxidation, cellulose) | Sourcing a new strain or characterizing the one you have |
| `/safety-review` | Review a recipe/batch for acidity-floor, pasteurization, labeling, and claim compliance | Before selling, gifting, or labeling any finished vinegar |

## Directory Structure

```
vinegar-fermentation-acetobacter-culture/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 9 bespoke domain commands
├── context/
│   ├── concepts.md           # AAB microbiology, biochemistry, methods, KB/FAQ model
│   ├── workflows.md          # Ferment lifecycle, KB ingestion, FAQ gen, troubleshooting tree
│   └── references.md         # Strain/condition tables, acidity standards, formulas, links
├── prompts/                  # Reusable prompt templates
└── outputs/                  # KB entries, FAQ docs, troubleshooting logs, audits
```

## Example Use Cases

### Standing up a producer knowledge base
A small cidery starts a vinegar line. They run `/kb-ingest` across their fermentation textbook, two AAB papers, and three years of batch notebooks. Within an afternoon they have a tagged, cited KB and a first `/faq-generate` FAQ for their tasting-room staff.

### Rescuing a stalled batch and learning from it
A barrel that should have hit 5% acidity is stuck at 2% with a sunken mother. `/troubleshoot-batch` walks the symptom tree (aeration loss → temperature drop → ethanol too high for the strain), recommends corrective aeration and a back-slop, and writes the diagnosis into the KB so the next stall is a lookup, not a mystery.

### Publishing a compliant FAQ
Before launching a product page, `/kb-audit` flags an unsourced "raw vinegar cures X" claim and a contradiction about minimum acidity. `/safety-review` confirms the batch clears the FDA 4% floor, and `/faq-generate` produces a public FAQ with only cited, compliant answers.

## Recommended MCP Servers

- **Filesystem MCP** — read source PDFs/notebooks for `/kb-ingest` and write KB/FAQ artifacts under `outputs/`.
- **Fetch / web MCP** — pull official acidity standards (FDA CPG, EU/regional vinegar regulations) and culture-collection strain data for `/strain-profile` and `/safety-review`.
- **SQLite/CSV MCP** (optional) — query batch and titration logs over time when the KB grows beyond flat files.

## Legal & Ethical Considerations

- **Minimum acidity for sale.** In the US, FDA defines vinegar as ≥4 g acetic acid per 100 mL (4% acidity); many regional standards require ≥5–6%. Product below the floor is mislabeled. `/safety-review` checks this.
- **No medical claims.** "Raw," "with the mother," and "unfiltered" are descriptive, but health/therapeutic claims (cures, detoxes, treats) are regulated and generally not permitted without substantiation. The KB tags such statements as `practitioner-lore`/`inferred`, never as fact, and FAQs must not present them as medical advice.
- **Pasteurization and shelf stability.** Raw, mother-containing vinegar will keep fermenting and may continue to form sediment/film; labeling should set expectations. High-acidity vinegar is self-preserving, but infused/diluted products may not be.
- **This workspace gives food-craft guidance, not regulatory or medical authority.** Confirm requirements with your jurisdiction's food-safety regulator before commercial sale.

## Technical References

- [FDA Compliance Policy Guide Sec. 525.825 — Vinegar, Definitions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cpg-sec-525825-vinegar-definitions-adulteration-vinegar-water) — US definitions and the ≥4% acidity basis.
- [Komagataeibacter and the reclassification of cellulose-producing AAB (Yamada et al.)](https://doi.org/10.1007/s12275-012-2249-4) — modern taxonomy of *Acetobacter xylinum* → *Komagataeibacter*.
- [Acetic Acid Bacteria: Ecology and Physiology (review)](https://doi.org/10.1146/annurev-food-030212-182512) — AAB metabolism, ethanol oxidation, overoxidation.
- [Vinegars of the World (Solieri & Giudici, eds.)](https://doi.org/10.1007/978-88-470-0866-3) — production methods, regional styles, and biochemistry reference.
- [DSMZ](https://www.dsmz.de/) / [ATCC](https://www.atcc.org/) — culture collections for *Acetobacter* / *Komagataeibacter* / *Gluconobacter* strains and their documented optima.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
