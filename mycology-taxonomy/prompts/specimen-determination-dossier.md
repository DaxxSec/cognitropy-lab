# Specimen Determination Dossier

## Purpose

Use this prompt to drive a full, integrative determination of an unknown fungal specimen end to end — from physical characters through barcode and (if needed) phylogeny to a nomenclaturally validated name — and produce a publishable dossier with explicit evidence and confidence.

## Prompt Template

```
You are a mycology taxonomy curator. Determine this specimen integratively and write a determination dossier.

I have an unknown fungal specimen:

- **Accession:** [ACCESSION NUMBER]
- **Macro characters:** [pileus, hymenophore, stipe, ring/volva, spore print, odour, staining, spot tests]
- **Micro characters:** [spore dims/shape/ornamentation, basidia, cystidia, pileipellis, clamps]
- **Substrate / habitat / locality:** [VALUE]
- **Sequence data:** [markers + files, e.g. ITS .fasta, TEF1 .fasta — or "none yet"]
- **Reference DB versions:** [UNITE SH release, GenBank query date]

Please:
1. Summarise the morphological candidate (genus confidence, provisional species) with supporting and contradicting characters.
2. Interpret the barcode(s): UNITE Species Hypothesis, top hits with reliability judgement, and an identity→confidence read.
3. State whether morphology and barcode agree; if not, decide whether to escalate to phylogeny and why.
4. If escalated, give the phylogenetic placement, support values, and GCPSR verdict on species boundary.
5. Validate the proposed name against MycoBank/Index Fungorum: status, authorship, synonymy, 1F1N.
6. Deliver the final determination with confidence, the species concept used, dissenting evidence, and reproducibility metadata.
```

## Expected Output

- A determination dossier: candidate → evidence (morphology / barcode / phylogeny) → validated name + authorship + status.
- Explicit confidence and the species concept applied; provisional rank (`aff.`/`cf.`/`sp.`) where the data won't support a binomial.
- Reproducibility block: markers, primers, QC thresholds, DB versions, alignment/tree settings, support values.
- A clear next-action if undetermined (secondary marker, fresh collection, candidate novel taxon).
