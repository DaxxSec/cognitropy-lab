# /space-weather

Snapshot the "detection space weather" — environmental shifts that perturb baselines — and score the disturbance on a K-index scale. Phase 8 monitoring.

## Inputs

- Change feed since the last snapshot: deployments, new/decommissioned log sources, patch windows, config changes.
- Active incidents / outages.
- Threat-intel / campaign notes (an active campaign raises the malicious-signal "solar flux").

## Steps

1. Enumerate every disturbance since the last snapshot.
2. Score each on the K-index scale (see `context/references.md`): K0–2 quiet, K3–4 active, K5–6 minor storm, K7–9 severe storm — by expected baseline impact.
3. Map each disturbance to the rules whose noise floor / diurnal baseline it invalidates (e.g. a new EDR rollout floods process-creation telemetry → all process-count rules now stale).
4. For K5+ disturbances, recommend a **baseline freeze** on affected sources (re-baselining now would poison the floor).
5. For passed disturbances, queue the affected rules for `/tune-rule` once conditions return to quiet.

## Output

`outputs/space-weather-YYYY-MM-DD.md` — the disturbance list with K-scores, the affected-rule mapping, baseline-freeze recommendations, and the retune queue.

## Notes

- The single most important rule: **do not re-baseline during a storm.** A floor measured during an outage gets baked in and silences the rule for weeks.
- A quiet K-score with rising FP load across many rules means an *un-logged* disturbance — investigate before tuning individual rules.
