# /audit-image-quality — Objective QA against the capture profile

Evaluate a batch of captured images against the measurable conformance criteria in their capture profile and produce a pass / rescan decision per image, with the failing metric named.

## Inputs

- Path to the image batch (masters) and the matching capture profile from `/spec-capture-profile`.
- The target-chart images shot for the batch (objective/device-level target) and the chart's reference data.
- The standard's tolerances (carried in the profile's conformance checklist).

## Steps

1. **Verify file conformance.** Format, bit depth, color space, embedded ICC profile, dimensions, and naming — anything off here is an automatic fail before pixel analysis.
2. **Analyze the target chart.** From the chart, measure tone reproduction (OECF), white balance, color accuracy (ΔE against reference patches), and spatial frequency response (SFR/MTF) for resolution. Use the analysis tools in `context/references.md`.
3. **Compare to tolerances.** Score each metric against the standard's aim and tolerance (e.g. ΔE mean/max, OECF deviation, MTF50, illumination uniformity, noise). Mark each metric pass/marginal/fail.
4. **Spot-check the images themselves.** Sample for focus, framing/cropping, color cast, dust/artefacts, and missing pages/items — chart conformance doesn't catch a fingerprint on plate 12.
5. **Decide per image and per batch.** An image fails if any hard metric fails; the batch fails if the chart fails (systemic) or the reject rate exceeds the agreed threshold.
6. **Route rejects.** Group failures by root cause (focus, color, framing, capture-chain drift) so the rescan list is actionable and the chain can be corrected once rather than image-by-image.

## Output

`outputs/qa-report-<batch>.md`: the per-metric chart results vs. tolerance, the per-image pass/rescan list with the failing metric, the batch verdict, and the root-cause-grouped rescan worklist. Feed the worklist into the next `/optimize-scanner-schedule` run.

## Notes

- A failing target chart means *every* image in that session is suspect — fix the capture chain and reshoot the session, don't cherry-pick.
- Track metric drift over time. A slow ΔE creep is a lamp aging or a profile going stale; catching the trend prevents a whole day's rejects.
- QA reject rate is a direct input to throughput forecasts — a 15% reject rate silently inflates every completion estimate. Report it back to `/forecast-backlog-drawdown`.
