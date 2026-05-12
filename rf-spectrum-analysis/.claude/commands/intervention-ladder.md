# /intervention-ladder

Map a graded severity tier to a proportionate intervention step. Modelled directly on the WHO analgesic ladder: don't reach for the strongest option first; escalate one rung at a time, document the response, escalate again only if response is inadequate.

## Inputs

- **Symptom record** — path to a `/symptom-assess` output under `outputs/symptoms/`.
- **Site constraints** — fixed installations (`antenna welded to mast`), operational windows (`no changes during trading hours`), or budget caps (`no capex this quarter`).
- *(Optional)* **Recent intervention history** — relevant prior rungs already tried for this subject.

## Steps

1. **Read the tier** from the symptom record (`Tier 1`–`Tier 4`).
2. **Select the candidate rung** using the table below as the default. Adjust ±1 rung based on documented site constraints.

   | Tier | Default rung | Rationale |
   |------|--------------|-----------|
   | Tier 1 (0–8) | **Rung 0 — Observe** | Re-grade in 1–2 weeks. No action. |
   | Tier 2 (9–16) | **Rung 1 — Reconfigure receiver** | Antenna re-aim, polarisation rotate, gain/AGC retune, FFT/window change to confirm. Low cost, reversible. |
   | Tier 2 (9–16) | **Rung 2 — Reassign channel** | Switch the affected service to a less-congested channel; verify with a follow-up symptom-assess. |
   | Tier 3 (17–24) | **Rung 3 — Site investigation** | On-site walk with a directional antenna or handheld analyser; locate the source; document. |
   | Tier 3 (17–24) | **Rung 4 — Mitigate at source** | Shield, filter, replace, or negotiate with the source operator. |
   | Tier 4 (25+) | **Rung 5 — Regulatory / safety escalation** | File with regulator (FCC OET, Ofcom), invoke safety stop on dependent systems, or trigger SecOps incident if interference is adversarial. |

3. **Justify ±1 deviation.** If you skip a rung (e.g. straight to Rung 3 because a previous Rung 1+2 cycle was unsuccessful), say so explicitly.
4. **Plan the intervention.** Write the concrete action: who, what, when, expected duration, expected effect, rollback plan.
5. **Define success criteria.** What does Rung *k* working look like? Always express it as a measurable change on the same metric the control chart tracks (e.g. "X-bar of noise-floor on Ch 36 drops back inside ±2σ within 7 days").
6. **Mark a re-assessment date.** Default: 7 days for Rungs 1–2, 14 days for Rungs 3–4, ad-hoc for Rung 5. The re-assessment runs `/symptom-assess` again on the same subject so the result is comparable.

## Output

`outputs/interventions/<YYYY-MM-DD>-<symptom-slug>.md` containing:
- Linked symptom record and tier.
- Selected rung with justification.
- Concrete action plan and rollback.
- Success criteria expressed in measurable terms.
- Re-assessment date.

## Notes

- **The ladder is bidirectional.** If Rung 2 succeeds and stays succeeded for 4+ weeks of `/longitudinal-track`, step *down* — return monitoring cadence to baseline.
- **Do not skip rungs without justification.** The most common failure is "the engineer hates retuning so we file a regulator complaint instead". Document the actual evidence trail.
- **Rung 5 is high-blast-radius.** Regulator complaints are public, contentious, and sometimes radicalising; SecOps incidents wake people up. Only use when Tier 4 is genuinely warranted.
- Pair every Rung 1–4 action with a follow-up `/control-chart-build` on the same metric; if the chart doesn't move, neither did the symptom.
