# Composition Conformance Review

## Purpose

Use when you have OES/XRF results and need to judge material identity and grade conformance with measurement uncertainty handled honestly (pass / fail / indeterminate), and to compute the carbon equivalent and its microstructural prediction.

## Prompt Template

```
Act as the lab metallurgist verifying a casting's composition against its intended grade.
Treat near-limit elements as indeterminate, not as pass/fail, and reconcile the carbon-equivalent
prediction with the observed microstructure.

Inputs:
- **Intended grade & element windows:** [e.g. ASTM A536 65-45-12, Mg 0.03–0.05]
- **Measured composition (with method & uncertainty):** [element: value ± unc, ... ; OES, cal date]
- **Microstructure observed (if any):** [graphite type, nodularity %, matrix]

Please:
1. Tabulate each element vs. its window and mark pass / fail / indeterminate using the stated uncertainty.
2. Compute carbon equivalent (CE = %C + (%Si + %P)/3) and predict hypo/hypereutectic behavior and chill tendency.
3. Check the CE prediction against the observed microstructure and flag any contradiction.
4. Give a joint conformance probability and, if off-spec, the likelihood ratio it contributes toward a material/casting root cause.
```

## Expected Output

- An element-by-element conformance table (measured ± vs spec, verdict)
- Carbon equivalent with its microstructural prediction and the metallography cross-check
- A joint conformance probability and any LR contribution to the failure posterior
- A re-test recommendation for any indeterminate element
