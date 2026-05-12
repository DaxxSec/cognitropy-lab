# /report — Synthesize inspections into a comparative anatomy report

Pulls inspection records, comparisons, landmark catalogs, and trait matrix into a finished deliverable matching the user's voice setting.

## Inputs

Required:
- **Project slug** OR **specimen list** — what's the report's scope?
- **Voice** — read from `context/role.md` if set, otherwise ask.

Optional:
- Target journal style (for manuscript voice).
- Explicit table of contents the user wants enforced.

## Pre-flight

1. Confirm voice. Choices:
   - **Manuscript-ready** — IMRaD or descriptive-monograph structure, journal-target style.
   - **Curation entry** — terse, structured, museum-CMS-compatible.
   - **Classroom handout** — pedagogically scaffolded with margin definitions and discussion questions.
   - **Field-notebook** — informal but provenance-complete.
   - **Cladistic-coding** — NEXUS-compatible terse character descriptions.
2. Check for embargo / sensitive-locality flags on `context/project.md`. Mark output accordingly.
3. Inventory available inputs: how many inspection records, comparisons, landmark files, matrix files apply to this scope?

## Procedure (by voice)

### Manuscript-ready

Standard sections:
1. **Title** — descriptive, includes taxon and structure focus.
2. **Abstract** — 150-250 words, structured (background / methods / results / conclusions).
3. **Introduction** — phylogenetic + biological context. State the question. Cite prior work. End with hypotheses.
4. **Materials and Methods** — specimens (table with provenance), inspection methodology, character set, analytical methods, software versions.
5. **Results** — descriptive, organized by system or by character. No interpretation.
6. **Discussion** — homology assessment, evolutionary scenarios, comparison to literature, limitations, future work.
7. **References** — formatted to target journal style if specified.
8. **Tables / Figures** — referenced inline.

### Curation entry

```
specimen_id: <accession>
identification: <binomial + author>
identifier: <user>
identification_date: <YYYY-MM-DD>
prior_identification: <previous binomial if re-identified>
diagnostic_features: <bullet list>
condition: <fluid / dried / mounted / fossil / other>
provenance: <locality summary + accession history>
notes: <any peculiarity worth recording>
authority_for_change: <if re-identifying — basis>
```

### Classroom handout

- One-sentence learning objective at top.
- Two-column body: anatomy on left, terms/definitions in margin on right.
- End with three discussion questions tied to the anatomy.
- Length: one to four printed pages.

### Field-notebook

- Date.
- Locality (coarse to user's preference).
- Specimens encountered (provenance fields).
- Observations (numbered, briefly).
- Sketches referenced (file paths).
- Questions for follow-up.

### Cladistic-coding

- Character-by-character, NEXUS-compatible.
- One paragraph per character: name, states with state IDs, ordering, definition with topology / ontogeny justification.
- Ready for paste into Mesquite character-list block.

## Always include

- Specimen list with provenance.
- Methods sufficient to reproduce.
- Citations to source inspections + external literature.
- Embargo notice if applicable.

## Output

`outputs/reports/<title>.md`

## Validation

- Voice matches `role.md` setting.
- Every claim is sourced (inspection record path / citation / explicit "novel observation" with justification).
- Provenance is traceable from final document back to specimens.
- Embargo / sensitive-locality flags propagated.
