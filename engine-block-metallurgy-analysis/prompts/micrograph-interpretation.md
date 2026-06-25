# Micrograph Interpretation

## Purpose

Use to interpret a metallographic image set (as-polished + etched) of a cast-iron or aluminium block, producing a graphite/matrix/defect read with the prep artefacts ruled out and the result expressed as evidence for the case posterior.

## Prompt Template

```
Interpret this metallographic image set as a forensic metallurgist. Read the as-polished image
before the etched one, separate genuine features from preparation artefacts, and classify per
ASTM A247 / ISO 945.

Inputs:
- **Material / intended grade:** [e.g. gray iron A48 Class 35]
- **Images:** [as-polished and etched; magnification; calibrated?]
- **Etchant used:** [e.g. 2% Nital]
- **Question to answer:** [grade conformance? defect ID? degeneration check?]

Please:
1. Classify graphite form/distribution/size and (if Mg-treated) estimate nodularity %.
2. Read the matrix phases and flag unwanted phases (carbides/chill, steadite, martensite/decarb).
3. Distinguish real porosity/defects from pull-out, comet tails, or over-etch artefacts, citing the as-polished/etched comparison.
4. State whether the microstructure matches the intended grade, and the likelihood ratio it contributes to the failure hypotheses.
```

## Expected Output

- Graphite classification (type/size/distribution, nodularity % if applicable)
- Matrix phase read with any unwanted phases flagged
- An explicit artefact-vs-feature judgment for anything that looks like a defect
- Grade match verdict and the LR contribution to the posterior
