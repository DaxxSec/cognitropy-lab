# Prompt — Current-Quarter Nowcast Decision Note

Use after `/build-nowcast` to produce a one-page decision note for the desk or research head.

---

You are writing a current-quarter GDP nowcast decision note for an internal audience that knows the methodology.

**Inputs you will be given:**
- `target_quarter` (e.g. 2026Q2)
- `model_class` (`dfm` / `bridge` / `midas`)
- `point_forecast`, `band_68`, `band_95`
- `change_vs_prior_nowcast` (point and signed percent)
- `top_5_indicator_contributions` (named series with signed contribution to the nowcast change)
- `recent_data_anomalies` (any large surprises or revisions in the indicator panel)
- `model_artifact_ref`, `forecast_artifact_ref`

**Structure:**

### Bottom line (2 sentences)
Headline nowcast in the user's reporting convention (annualised SAAR for US; QoQ for euro area). State the directional change vs. the prior nowcast.

### Drivers (table)
Markdown table: indicator | this period contribution | direction. Five rows, ordered by absolute contribution.

### Risk and asymmetries (short paragraph)
- Where are the bands wider than usual? Why?
- Are any indicators behaving anomalously (large surprises, suspected revision)?
- Are there known upcoming releases this week that would materially update the nowcast?

### Comparison with external nowcasts (optional)
If `external_nowcasts` (Atlanta Fed GDPNow, NY Fed Nowcast) are available in `inputs/external_nowcasts/`, briefly compare. Do NOT use external nowcasts as inputs.

### Recommendation
- Hold / publish / wait for the next release.
- If wait: name the trigger (e.g. "wait for the May ISM print on May 1").

### Reproducibility footer
Pin: model artifact path + hash, forecast artifact path + hash, vintage cutoff date. A reader with the workspace and the manifests must be able to rebuild this number.

**Tone:** terse, decision-oriented, no padding. Decision-makers read the bottom line and the recommendation; everything else is supporting evidence.
