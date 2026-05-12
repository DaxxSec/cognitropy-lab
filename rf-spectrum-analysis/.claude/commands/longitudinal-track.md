# /longitudinal-track

Refresh the symptom trajectory for one or more subjects. The trajectory plot is the "patient chart" for the spectrum — chronological severity scores, control-chart status, and intervention markers in one canvas.

## Inputs

- **Subjects** — list of channel/emitter identifiers, or `--all-active` for every subject with at least one assessment in the last 90 days.
- **Window** — default `last-12-weeks`; can be `since-baseline`, `last-N-weeks`, or absolute range.
- **Cadence** — `weekly` or `monthly` resampling for the rolling severity tier.

## Steps

1. **Collect records.** Read every `outputs/symptoms/*.md`, `outputs/interventions/*.md`, and `outputs/charts/*.json` referencing each requested subject within the window.
2. **Resample severity to a uniform cadence.** Forward-fill last-known tier between assessments; mark periods with no recent assessment as `data-gap` rather than implying continuity.
3. **Plot the trajectory.** Per subject, a stacked panel:
   - **Top:** severity tier over time, with shaded bands for Tier 1–4 thresholds.
   - **Middle:** the primary tracked metric's X-bar (or EWMA) from `/control-chart-build`, with the same date axis.
   - **Bottom:** intervention markers as vertical lines, labelled with the rung.
4. **Detect trajectory patterns.** Classify each subject as one of: `stable-low`, `stable-elevated`, `improving-post-intervention`, `worsening`, `relapsing-remitting`, `data-gap`. The classifier rules are listed in `context/workflows.md` § "Trajectory classification".
5. **Flag follow-up debt.** Any subject without a recent assessment whose window-end tier ≥2 → add to the follow-up debt list.
6. **Compose the trajectory report.** Markdown summary with the plots embedded (or referenced), the classification per subject, and the follow-up debt.

## Output

- `outputs/trajectories/<YYYY-MM-DD>/<subject>.png` — per-subject trajectory plot.
- `outputs/trajectories/<YYYY-MM-DD>/report.md` — narrative summary with classifications and follow-up debt list.
- `outputs/trajectories/<YYYY-MM-DD>/data.json` — machine-readable record (input for `/process-capability-report` and `/spectrum-mdt-handoff`).

## Notes

- **A `data-gap` is a finding, not a non-finding.** Subjects that haven't been re-assessed but were Tier 2+ at last check are the most likely place for silent regressions.
- **Don't average tiers.** The tier is ordinal not interval. Report mode/max within the window, not mean.
- **Relapsing-remitting** is the most easily missed pattern — short-window EWMA charts often miss it. Use a 12-week window minimum for this classification.
- Run this command on a calendar — weekly is appropriate for a site with multiple Tier 2+ subjects; monthly is fine for a stable site.
