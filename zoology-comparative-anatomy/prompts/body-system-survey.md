# Body-System Survey Across Multiple Taxa — Prompt Template

**Use case:** You're surveying ONE body system across SEVERAL taxa (e.g. cardiovascular system across 6 amniote lineages) — typically the prep-step for a comparative-anatomy paper or classroom material.

## Prompt

Survey the `[BODY SYSTEM — e.g. "cardiovascular system"]` across the following taxa:

1. `[TAXON 1]` — specimen(s): `[IDS]`
2. `[TAXON 2]` — specimen(s): `[IDS]`
3. `[TAXON 3]` — specimen(s): `[IDS]`
... (continue list)

Goal: `[descriptive monograph chapter / classroom comparison / character-set scoping for cladistic analysis / other]`.

Workflow:
1. For each taxon × specimen, run `/inspect` for the named system if no inspection record exists yet.
2. For each pair of taxa, run `/compare` for key sub-structures of the system (e.g. heart chambering, aortic arch retention, atrial septum, ventricular septum, major systemic arteries, major veins).
3. Build a survey table: rows = taxa, columns = sub-structures, cells = state summary (with state code if a character set is defined).
4. Run `/report` with voice = `[manuscript-ready / classroom-handout / cladistic-coding]`. Output a synthesis document tying the comparisons together with phylogenetic context.

Output the survey table as `outputs/reports/[BODY-SYSTEM]-survey-table.md` and the report as `outputs/reports/[BODY-SYSTEM]-survey-[VOICE].md`. Halt if any taxon's inspection records are incomplete or if homology of a sub-structure across the surveyed range cannot be grounded.
