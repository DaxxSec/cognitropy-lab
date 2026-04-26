# /compare — Structured comparison of homologous structures across taxa

Cross-taxon analysis grounded in inspection records. Tests homology assertions and codes character-state differences.

## Inputs

Required:
- **Specimen IDs** — at least 2, typically ≥1 per taxon under comparison.
- **Structure(s) of interest** — e.g. "humerus", "cardiovascular system", "tympanic ring".
- **Question** — explicit homology / character-state question. Examples:
  - "Are the humeri of taxa A, B, C homologous, and what state differences exist on character set X?"
  - "Is the tympanic ring of monotremes homologous with that of therians? If so, what's the polarity of the difference?"

Optional:
- Phylogenetic context (user-supplied tree or published reference).

## Pre-flight

1. Confirm an inspection record exists for every specimen × structure cell. If not, propose to run `/inspect` first or use published descriptions (require citation).
2. Confirm the homology question is explicit. Vague "compare these animals" gets returned with a clarifying question.

## Procedure

Walk through five sections in order:

### 1. Question
State the explicit homology / character-state question.

### 2. Specimens
Table: taxon | specimen ID | source (own inspection record path / published description with citation) | provenance summary.

### 3. Homology assessment

For each candidate-homologous structure:
- **Topology** — does it occupy the same position relative to invariant landmarks across taxa? Document.
- **Ontogeny** — known from each taxon? If yes, do developmental origins correspond? If no, flag data gap.
- **Phylogenetic congruence** — does the homology hypothesis fit a published tree? Cite tree.
- **Decision:** *homologous* / *putatively homologous (justify what evidence is missing)* / *homoplastic — convergence / parallelism / reversal* / *insufficient data*.

### 4. Character-state differences
For each character of interest (use project's character set if defined; otherwise propose inline):
- State per taxon, with citation to inspection record cell.
- Polarity assessment (which is plesiomorphic vs. apomorphic; cite outgroup).

### 5. Discussion
- Functional interpretation candidates.
- Evolutionary scenario candidates (in light of phylogenetic context).
- What additional data would resolve remaining uncertainty.

## Output

`outputs/comparisons/<structure>__<taxa>.md`

## Validation

- Every specimen referenced has provenance traceable to an inspection record OR cited publication.
- Every homology claim has explicit topology / ontogeny / congruence reasoning OR is flagged putative.
- Convergence is never silently called homology.
- Loss-then-regain (reversal) is distinguished from primary homoplasy.
