# Two-Taxa Comparison — Prompt Template

**Use case:** You have inspections (or published descriptions) for two taxa and want a structured comparison of one or more homologous structures.

## Prompt

Compare `[STRUCTURE(S)]` between:

1. `[TAXON A]` — specimen(s): `[IDS]` — source: `[inspection record path / publication citation]`
2. `[TAXON B]` — specimen(s): `[IDS]` — source: `[inspection record path / publication citation]`

Phylogenetic context: `[CITE TREE — e.g. "Upham et al. 2019 mammalian tree" or "I'll supply the topology"]`.

Question to answer: `[STATE THE EXPLICIT HOMOLOGY / CHARACTER-STATE QUESTION]`.

Run `/compare`. Walk all five sections: question, specimens, homology assessment (topology + ontogeny + phylogenetic congruence), character-state differences, discussion (including candidate apomorphies and what additional data would resolve uncertainty). Halt if any specimen lacks a traceable inspection record or citation, or if homology can't be grounded — flag putative.

Output `outputs/comparisons/[STRUCTURE]__[TAXA].md`. Distinguish convergence / parallelism / reversal explicitly; never silently call homoplasy homology.
