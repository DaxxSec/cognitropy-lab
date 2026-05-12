# /symptom-assess

Grade an emitter, interference event, or user complaint on a multi-axis 0–10 severity rubric modelled on the Edmonton Symptom Assessment System (ESAS-r). This is the moment where "something is off on 433" becomes a number you can defend, chart, and escalate.

## Inputs

- **Subject** — either a frequency/channel (`433.92 MHz`, `Ch 36 5GHz`), a named persistent emitter from the baseline, or a user-reported complaint (`Wi-Fi keeps dropping in conference room 4B`).
- **Observation window** — start/stop timestamps for the measurement evidence.
- **Evidence references** — paths under `outputs/` to sweep CSVs, packet-loss logs, user reports.
- **Comparator** — the baseline manifest at `outputs/baseline-<site>-<date>/manifest.md` to grade *against*.
- *(Optional)* **Affected systems / SLA** — what this symptom is hurting and to what spec.

## Steps

1. **Identify the symptom axis.** Choose from: persistent-elevated carrier, intermittent burst, broadband noise floor rise, channel saturation, drift, spurious emission, harmonic, intermod, denial-of-service-shaped.
2. **Score the four axes (0–10).**
   - **Intensity** — `0` indistinguishable from baseline → `10` ≥30 dB above baseline limits.
   - **Frequency** — `0` single event → `10` continuous duty cycle.
   - **Distress** — `0` no system affected → `10` safety-critical or compliance-critical failure.
   - **Trend** — `-5` improving fast → `0` stable → `+5` worsening fast.
   Document evidence behind each score in 1–2 sentences.
3. **Compute total severity tier.** Sum the absolute axis scores (intensity + frequency + distress + |trend|). Map: `0–8 = Tier 1 (watchful)`, `9–16 = Tier 2 (active monitoring)`, `17–24 = Tier 3 (intervene)`, `25+ = Tier 4 (escalate)`. See `context/references.md` for the rubric.
4. **Rule out artefact.** Confirm the symptom isn't a measurement artefact: gain compression, antenna handling, USB ground loop, FFT leakage. If artefact is plausible, downgrade by one tier and note `artefact-suspected` in the record.
5. **Snapshot the supporting waterfall.** Save a PNG or PSD snapshot of the offending channel ±20% bandwidth to `outputs/symptoms/<id>/evidence.png` so the assessment is auditable.
6. **Write the assessment.** Emit a structured Markdown record (see Output) so it can be reviewed in MDT and tracked longitudinally.

## Output

`outputs/symptoms/<YYYY-MM-DD>-<short-slug>.md` with:
- Header: subject, observation window, assessor, baseline reference.
- Per-axis score with one-sentence justification.
- Total severity, tier, and the rule-out review.
- Linked evidence: waterfall PNG, sweep CSVs, packet logs.
- A suggested next command (typically `/intervention-ladder`).

## Notes

- This is a **graded clinical-style record**, not a feelings sheet. Every axis score must point at evidence. If you cannot point at evidence, the score is 0.
- `Distress` is the lever that most often moves an emitter from Tier 2 to Tier 3. A 6 dB elevation on an unused band is Tier 1; the same elevation on a band used for medical telemetry is Tier 3.
- Re-grade weekly during active monitoring. Trend is the axis that ages fastest.
