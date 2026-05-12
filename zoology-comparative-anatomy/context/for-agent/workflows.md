# Workflows — Step-by-Step Procedures

*Reference document for the agent. Every slash command maps to one of these workflows.*

## Workflow A: Single-Specimen Inspection (`/inspect`)

**Trigger:** user supplies a specimen ID + photos / dissection notes / paper reference + target body system (or "all").

**Pre-flight checks:**
1. Is provenance complete? (institutional accession, taxon, sex if available, age class, preservation, locality, holding institution.) If not — halt, request from user.
2. Is the nomenclatural convention selected in `role.md`? If not — halt, request.
3. Is the appropriate version of the checklist (`resources/vertebrate-body-plan-checklist.md`) loaded for the taxon? Adapt per-clade — record adaptations.

**Execution:**

1. Open `outputs/inspections/<specimen-id>__<system>.md` (one file per system; aggregate to `<specimen-id>__full.md` if all-systems).
2. Write the **Provenance** block (template in `domain-knowledge.md` §5).
3. Walk the checklist for the target system, structure-by-structure:
   - State the structure name (in the chosen convention; secondary citation in parens).
   - Record **presence** (present / absent / damaged-uncertain).
   - Record **count** if the structure is countable (vertebrae, foramina, etc.).
   - Record **measurement(s)** with unit and instrument. Estimated-from-photo flagged as such.
   - Record **character state** if a coded character set is defined for this project.
   - Notes — anything noteworthy, unusual, equivocal.
   - Citations / cross-refs to other structures or prior literature.
4. After the system is complete, write a brief **System summary** paragraph noting any features that diverge from the modal expectation for the taxon.
5. If any structure couldn't be evaluated (specimen damage, photo angle missing, fluid preservation obscuring detail), record it explicitly as `presence: damaged-uncertain` or `presence: not-evaluable` — never silently omit.

**Output validation:**
- Every structure listed in the checklist appears in the record (or is explicitly marked not-applicable for the taxon, with reason).
- Every measurement has units.
- Every character-state coding has a state ID matching the project's character set.
- Provenance block is complete.

## Workflow B: Comparative Analysis (`/compare`)

**Trigger:** user supplies a list of specimen IDs (≥2, typically ≥1 per taxon being compared) + structures of interest.

**Pre-flight:**
1. Are inspections (Workflow A) on file for every specimen × structure cell? If not — propose to run them first or use published descriptions (if user supplies citations).
2. Is the phylogenetic context known? (User-supplied tree or published reference.)
3. Is the homology question explicit? E.g. "Are the X structures of taxon A and B homologous, and if so what character states differ?"

**Execution:**

1. Open `outputs/comparisons/<structure>__<taxa>.md`.
2. Write a **Question** section: state the explicit homology / character-state question being asked.
3. Write a **Specimens** table (taxon, specimen ID, source — direct inspection record vs. published description with citation).
4. **Homology assessment** for the structure(s):
   - Topology: same position relative to invariant landmarks across taxa? Document.
   - Ontogeny: known from each taxon? If yes, do they correspond? If no, flag as data gap.
   - Phylogenetic congruence: does the homology hypothesis fit a published tree? Cite.
   - **Decision:** *homologous*, *putatively homologous (justify what evidence is missing)*, *homoplastic (specify type — convergence / parallelism / reversal)*, or *insufficient data*.
5. **Character-state differences** — for each taxon, the state of the structure on each character of interest. Use the project's character set if defined; otherwise propose a character set inline and write states.
6. **Candidate apomorphies** — note any state that's potentially synapomorphic for a clade containing the compared taxa, citing the tree.
7. **Discussion** paragraph — functional interpretation, evolutionary scenario candidates, what would resolve remaining uncertainty.

**Output validation:**
- Every specimen referenced has provenance traceable to an inspection record or cited publication.
- Every homology claim has explicit topology / ontogeny / congruence reasoning OR is flagged as putative.
- Convergence is never called homology; loss-then-regain (reversal) is distinguished from primary homoplasy.

## Workflow C: Landmark Cataloging (`/landmark`)

**Trigger:** user supplies a specimen ID + body region (typically a 2D image view or a 3D mesh region).

**Pre-flight:**
1. Is the body region defined precisely? ("Skull lateral view" is acceptable; "skull" alone is not — specify view or 3D vs. 2D).
2. Is image scale calibrated? (Scale bar present and length stated, OR pixel-to-mm calibration provided.)

**Execution:**

1. Open `outputs/landmarks/<specimen-id>__<region>.md`.
2. List landmarks. For each:
   - **Name** — unambiguous, ideally tied to a published landmark scheme (e.g. Klingenberg 2011, Adams & Otárola-Castillo 2013 for geomorph, MorphoSource convention).
   - **Definition** — anatomical position in words, replicable.
   - **Type** (Bookstein 1991):
     - **Type I** — discrete juxtaposition of tissues (e.g. tip of canine, tooth-tooth contact, suture intersection). Highest replicability.
     - **Type II** — local property of geometry (e.g. point of maximum curvature). Medium replicability.
     - **Type III** — extremal point relative to another landmark (e.g. point on margin most distant from landmark X). Lowest replicability; flag.
   - **Coordinates** if image-derived (with image reference and units).
   - **Notes** — replicability concerns, alternative definitions in literature, missing data status.
3. Compile a **Replicability summary** at the bottom: count of Type I/II/III, expected inter-observer error class.

**Output validation:**
- Landmark list is non-empty and named.
- Each landmark has a definition replicable by another worker without seeing your output.
- Type assignment is justified.

## Workflow D: Trait-Matrix Construction (`/trait-matrix`)

**Trigger:** user supplies taxa list + character set (or "derive from prior inspections").

**Pre-flight:**
1. Are inspection records on file for every taxon? If not — propose to do them first.
2. Is the character set explicit, with state definitions? If "derive from inspections" — agent extracts characters from inspection records, lists them, and asks user to confirm scope before coding.
3. What's the matrix format? (NEXUS / TSV / both.)

**Execution:**

1. Open `outputs/matrix/<project-slug>.tsv` (rows = taxa, columns = character IDs, cells = states; missing = ?, inapplicable = -).
2. Open `outputs/matrix/<project-slug>.notes.md` (one section per character):
   - Character ID, name, state definitions (with state IDs 0, 1, 2, ...).
   - **Homology statement** — why the structure being coded is treated as the same structure across taxa (cite topology / ontogeny / phylogenetic source).
   - Per-taxon coding rationale + citation (inspection record file path or publication).
   - Any inapplicable / missing flags and why.
3. Write the matrix file. Ensure every taxon × character cell either has a state, ?, or -. No blanks.
4. If NEXUS output requested, write a properly-formatted NEXUS data block including TAXA + CHARACTERS + MATRIX.

**Output validation:**
- Matrix is complete (no blank cells).
- Every character has a state-definition in the notes file.
- Every coding has a citation.
- Homology of each character is explicitly justified.

## Workflow E: Report Synthesis (`/report`)

**Trigger:** user requests a report; project slug identifies the body of inspections / comparisons / matrix to draw from.

**Pre-flight:**
1. What's the target voice? (`role.md` → output voice setting: manuscript / curation / classroom / field-notebook / cladistic-coding.)
2. What's the scope? (Single specimen, one body system across taxa, full project synthesis.)
3. Are there ethical / embargo flags on `context/project.md`? If so, mark output accordingly.

**Execution by voice:**

- **Manuscript-ready** — IMRaD or descriptive-monograph structure. Title / Abstract / Introduction (with phylogenetic + biological context) / Materials and Methods (specimens, methods, character set) / Results (descriptive, by system or by character) / Discussion (homology, evolutionary scenario, comparison to literature) / References. Use the user's target journal style if specified.
- **Curation entry** — Terse, structured. Specimen × identification × notes × diagnostic features × condition × authority for ID change (if re-identifying).
- **Classroom handout** — Pedagogically scaffolded. Begin with one-sentence summary, define terms in margin, end with three discussion questions.
- **Field-notebook** — Date / locality / specimens encountered / observations / sketches (referenced) / questions for follow-up.
- **Cladistic coding** — NEXUS-compatible terse character descriptions, suitable for inclusion in a Mesquite character-list block.

Always include:
1. Specimen list with provenance.
2. Methods section sufficient to reproduce.
3. Citations to source inspections and any external literature.
4. Embargo notice if applicable.

**Output validation:**
- Voice matches the user's preference in `role.md`.
- Every claim is sourced (inspection record file path, citation, or explicit "novel observation").
- Provenance preserved through to the final document.
