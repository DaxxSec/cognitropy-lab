# /composition-cross-check

Verify OES/XRF composition against the intended grade spec, compute carbon equivalent, and express conformance as a probability that accounts for measurement uncertainty.

## Inputs

- OES (bulk) and/or XRF (spot) element results, with the instrument and its calibration date
- The intended grade and its element windows (see `context/references.md`)
- For Mg-treated irons: residual Mg target

## Steps

1. Tabulate each measured element against its spec window; attach the method's measurement uncertainty (±) per element.
2. Compute carbon equivalent `CE = %C + (%Si + %P)/3`; predict hypo/hypereutectic behavior and chill tendency.
3. **Cross-validate against metallography** — the CE prediction (e.g. primary dendrites vs. kish graphite) must agree with what `/graphite-morphology-classify` saw; flag any contradiction (often a sampling or ID error).
4. For each element, compute a conformance probability from the measurement uncertainty (within limits → high; within ±1σ of a limit → indeterminate; clearly outside → low).
5. Roll up a joint conformance assessment and translate any off-spec finding into a likelihood ratio for the material/casting hypothesis.

## Output

`outputs/<case-id>/composition-check.md`: element table (measured ± vs spec), CE, conformance probability per element, joint verdict, and the LR contribution.

## Notes

- An element one measurement-uncertainty from the limit is **indeterminate**, not a fail — recommend re-test rather than concluding.
- Low residual Mg in a part expected to be ductile/CGI is strong evidence toward graphite degeneration; route it to the posterior immediately.
