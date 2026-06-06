# Mortar Identification Report

## Purpose

Use when you have field and/or lab data on an original mortar and need a defensible, named identification — the two-track (petrographic + chemical) determination with a confidence statement.

## Prompt Template

```
You are a building-conservation mortar analyst. Identify this historic mortar like a mycologist keying and barcoding a specimen, then name it.

I have an original mortar sample with the following characters:

- **Provenance:** [building, elevation, height, date sampled, drawing ref]
- **Field characters:** [colour, hardness, friability, lime lumps, visible aggregate, cement haze]
- **Acid reaction:** [fizz vigour, residue]
- **Petrography (if any):** [binder character, aggregate mineralogy/roundness, grading, voids, point-counted binder:aggregate]
- **Chemistry (if any):** [acid-digestion binder:aggregate, oxide analysis for HI, XRD phases, TGA steps]
- **Substrate:** [unit type and approximate strength]

Please:
1. Run the dichotomous key to a provisional binder class, recording the lead path.
2. Reconcile the morphology and barcode tracks; flag calcareous-aggregate confounding and any contamination.
3. Compute/estimate the Hydraulic Index and state the binder:aggregate ratio.
4. Assign a binomial name (<binder class> <ratio> (<aggregate descriptor>)) with a determination confidence.
5. Recommend whether to accession it as a type specimen, and any missing confirmatory test.
```

## Expected Output

- Keyed lead path with the character at each couplet.
- Two-track character summary and concordance note.
- HI, binder:aggregate, aggregate grading.
- Assigned binomial name + author/date + confidence (high / medium / provisional `cf.`).
- Accession recommendation and any follow-up test required.
