# /changepoint-detect

Detect community-level shifts using PELT or Bayesian Online Change-Point Detection on an Aitchison-distance-from-baseline series.

## Inputs

- Path to a CLR-transformed count table (output of `/clr-transform`).
- Baseline window: list of sample IDs (or date range) defining "pre-change" reference.
- Detection method: `PELT` (offline, full series available) or `BOCPD` (online / streaming).
- Penalty preference for PELT: BIC, MBIC, or manual sweep.
- Optional companion sensor series (CO₂ flux, EC) for cross-check.

## Steps

1. Read `context/workflows.md` "Change-Point Detection on Community Distance".
2. Compute the centroid of the baseline window in CLR space.
3. Compute Aitchison distance (Euclidean in CLR) from each post-baseline sample to the centroid; produce a (date, distance) series.
4. Run PELT:
   - R: `changepoint::cpt.meanvar(series, method="PELT", penalty=...)`.
   - Python: `ruptures.Pelt(model="rbf").fit_predict(...)`.
5. Calibrate penalty: BIC for default; if too many or too few change points, sweep penalty and pick by elbow.
6. For streaming companion data, run BOCPD (`bayes_changepoint_python` or hand-rolled with conjugate priors); compare detected timings.
7. Annotate change points against the management timeline (treatments, weather, harvests) — propose causal candidates.

## Output

A markdown file `outputs/changepoint-YYYY-MM-DD.md` containing: baseline window definition, distance-series description, detected change points (date, magnitude Δ in distance, 95% CI on timing, candidate cause from timeline), and any cross-check disagreements between PELT and BOCPD.

## Notes

- Many change points detected → penalty too low; tighten it.
- A change point at a sequencing-batch boundary → suspect batch effect; rerun with batch correction (`ComBat`, `MMUPHin`) and recheck.
- No change points but treatment is "obviously" different → the metric is insensitive; try alpha-diversity series or a specific functional-gene qPCR series in parallel.
- Aitchison distance assumes CLR-transformed input; running this on raw relative abundances is wrong.
