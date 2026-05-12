# /spectrum-mdt-handoff

Produce a structured multidisciplinary-team (MDT) handoff for a spectrum issue. Adapted from the palliative-care MDT case-presentation format — one document that an RF engineer, a SecOps analyst, a facilities lead, and an executive sponsor can all read and agree on next actions from.

## Inputs

- **Subject** — channel/emitter under discussion. Required.
- **Latest symptom-assess record** — path under `outputs/symptoms/`.
- **Latest control chart** — path under `outputs/charts/`.
- **Latest trajectory entry** — path under `outputs/trajectories/`.
- **Audience disciplines** — one or more of `rf-eng`, `secops`, `facilities`, `compliance`, `clinical-eng` (for medical), `business-sponsor`.
- *(Optional)* **Decision required** — the single decision the MDT must make (e.g. "Approve regulator filing", "Approve channel reassignment of clinical telemetry").

## Steps

1. **Compose the case summary.** Two paragraphs max. What the spectrum subject is, when it started behaving abnormally, and what's been tried. Skip RF jargon a facilities lead can't parse, or define it inline.
2. **State the severity trajectory.** Insert the trajectory plot. Annotate intervention markers in plain language.
3. **Quantify the impact.** From the symptom record and capability report: "Telemetry packet-loss is currently 7.2% against a 2.0% SLA. Cpk = 0.61, not capable. Estimated 12,000 lost packets/day."
4. **Differential.** List 2–4 plausible causes with the evidence for and against each. This is the most-skipped section in real incidents — force it.
5. **Options table.** Each option: name, intervention rung, expected duration, expected cost (time/money/business risk), and the audience whose buy-in is required.
6. **Recommended path.** State the recommendation explicitly. Bind it to the success criteria from the intervention record (so re-assessment is unambiguous).
7. **Required decisions.** A bulleted list of yes/no decisions the MDT needs to leave the meeting with. If the meeting can't make them, name the decision-maker not present.
8. **Sign-off line.** Each discipline initials and dates next to the recommended path so the artefact is auditable.

## Output

`outputs/mdt-handoffs/<YYYY-MM-DD>-<subject-slug>.md` — Markdown brief, designed to be readable in 5 minutes by all listed disciplines. Optional companion PDF for archival via `pandoc`.

## Notes

- **Audience aware, not audience-flattering.** Each discipline gets the data relevant to its decision; nobody gets a watered-down summary. The MDT model assumes everyone is competent in their domain.
- **One subject per handoff.** Bundling four channels into one brief produces a meeting where nothing decides. Spin separate briefs.
- **The differential is the test of seriousness.** If you can only generate one cause, the analysis is incomplete; loop back to `/symptom-assess`.
- **Don't write recommendations the sponsor can't act on.** If facilities can't move an antenna this quarter, the recommendation should reflect that and revisit at next budgeting cycle.
