# /trait-matrix — Build or update a comparative trait matrix

Produces a structured taxa × characters matrix, with explicit homology justification per character and citation per coding.

## Inputs

Required:
- **Taxa list** (binomials + authors).
- **Character set** — either explicitly defined OR "derive from prior inspections" (agent extracts characters from inspection records on file).

Optional:
- Output format preference: TSV (default) / NEXUS / both.

## Pre-flight

1. Are inspection records on file for every taxon? If not — propose to run `/inspect` for missing taxa before coding.
2. If character set is explicit, are state definitions complete? If "derive from inspections", agent extracts and confirms scope with user before coding.

## Procedure

### Phase 1: Character list

For each character:
- Character ID (1, 2, 3, ...).
- Name (concise, taxonomically meaningful).
- State definitions (state IDs 0, 1, 2, ...; describe each state precisely).
- **Homology statement** — why the structure being coded is treated as the same structure across all taxa being scored. Cite topology / ontogeny / phylogenetic source.
- Notes — ordering (ordered / unordered), weighting (default = 1), any inapplicable conventions.

### Phase 2: Coding

For each taxon × character cell:
- Assign state ID, OR
- `?` for missing data (specimen damaged, structure not evaluable, or no specimen examined for this taxon × character cell), OR
- `-` for inapplicable (e.g. "presence of secondary palate" coded `-` for a fish, where no oral cavity comparable to a palate exists).
- Citation: inspection record file path (preferred) or publication citation.
- If user-supplied or borrowed from another study: indicate the source.

### Phase 3: Output

Write two files:
- `outputs/matrix/<project-slug>.tsv` — rows = taxa, columns = character IDs. First row: header. First column: taxon. Tab-separated. Cells = state IDs, ?, or -.
- `outputs/matrix/<project-slug>.notes.md` — character-by-character rationale (state defs, homology, ordering, per-taxon coding citations).

If NEXUS requested:
- `outputs/matrix/<project-slug>.nex` — properly-formatted NEXUS DATA block (TAXA + CHARACTERS + MATRIX).
- Include CHARSTATELABELS so character names + state names are readable in Mesquite.

## Validation

- Matrix is complete: every cell has a state, ?, or -. No blanks.
- Every character has a state-definition entry in the notes file.
- Every coding has a citation (inspection record path OR publication).
- Homology of each character is explicitly justified.
- NEXUS file (if produced) parses cleanly in Mesquite.

## Common pitfalls

- Coding a character without specifying ordering — defaults to unordered if not specified, but be explicit.
- Mixing `?` (missing data) and `-` (inapplicable) — these are not interchangeable.
- Coding from photos with insufficient resolution — flag as `?` rather than guessing.
- Dropping character ID gaps when removing a character from a working draft (renumber properly or note the gap).
