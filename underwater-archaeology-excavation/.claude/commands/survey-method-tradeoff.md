# /survey-method-tradeoff

Select a remote-sensing survey package on a cost-vs-coverage-vs-resolution basis, before any disturbance.

## Inputs

- The detection problem: is target structure exposed or buried? Ferrous or not? Is stratigraphy the question?
- Search area size and water depth.
- Available platforms and instrument day-rates.
- Required positional accuracy and the downstream use of the data (find vs. evaluate vs. record).

## Steps

1. Read `context/references.md` ("Survey Instrument Selection").
2. Map the detection problem to candidate instruments: exposed relief → side-scan/MBES; buried iron → magnetometer; buried structure/strata → sub-bottom profiler; recording → photogrammetry.
3. For each candidate, tabulate cost (day-rate × area/lane-km), coverage rate, resolution, and what it *cannot* see.
4. Compose the **minimum package** that answers the question — usually a wide-area finder plus a confirmer, not every instrument.
5. Always add a **ground-truth** line: targeted diver/ROV inspection of anomalies before any excavation decision.
6. Check the package against the budget and the value of the information it buys (does it actually reduce a CBA-driving uncertainty?).

## Output

`outputs/survey-package-<site>-YYYY-MM-DD.md`: the recommended instrument package, the cost/coverage/resolution table, what each instrument leaves blind, the ground-truth plan, and the CBA uncertainty the survey is bought to reduce.

## Notes

- Survey is cheap relative to excavation — its main value is reducing the epistemic uncertainty that would otherwise force a conservative (expensive) excavation decision.
- No single instrument is complete: magnetometers ignore non-ferrous sites; side-scan ignores buried material. Compose deliberately.
- Don't buy resolution you won't use — a recording-grade survey is wasted if the decision only needs presence/absence.
