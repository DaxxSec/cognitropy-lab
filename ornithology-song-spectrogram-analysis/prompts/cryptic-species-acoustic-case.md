# Cryptic-Species Acoustic Case

## Purpose

Build the acoustic argument for or against a species limit between cryptic taxa — the case a checklist committee would scrutinize. Use after `/confusion-audit` has quantified what voice can resolve.

## Prompt Template

```
You are an avian bioacoustician assembling a vocal case on species limits between cryptic taxa. Argue from diagnostic characters and a confusion matrix, and weight innate (suboscine/non-passerine) voices more heavily than learned ones.

Taxa under consideration:
- **Taxon 1 vocal profile:** [CHARACTERS WITH RANGES, N INDIVIDUALS]
- **Taxon 2 vocal profile:** [CHARACTERS WITH RANGES, N INDIVIDUALS]
- **Confusion matrix:** [OFF-DIAGONAL RATES FROM /confusion-audit]
- **Learning mode:** [OSCINE (LEARNED) / SUBOSCINE / NON-PASSERINE (INNATE)]

Please:
1. Identify which characters are diagnostic (non-overlapping) vs which merely vary.
2. Assess separation strength from the confusion matrix (how often voice gets it right).
3. Weigh by learning mode — discount learned-song differences relative to innate ones.
4. Conclude: voice supports a split, supports lumping, or is non-diagnostic (corroborate by genetics/morphology). Frame it in Tobias-style scoring terms where possible.
```

## Expected Output

- A diagnostic-vs-variable character breakdown
- A separation-strength read from the confusion matrix
- A learning-mode-weighted judgment
- A split / lump / non-diagnostic conclusion with the corroboration needed
