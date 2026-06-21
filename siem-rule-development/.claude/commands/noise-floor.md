# /noise-floor

Characterize the benign event-rate noise floor for a log source or entity, establishing the SNR a detection must clear — Phase 2.

## Inputs

- Log source / base query (the events the rule keys on, *before* the malicious condition).
- Entity scope (global, per-host, per-user, per-service-account).
- Observation window — at least 2–4 weeks to cover a full diurnal/weekly cycle.

## Steps

1. Pull the benign baseline event counts over the window (exclude any known-incident periods — don't measure the floor during a storm).
2. Aggregate by hour-of-day and day-of-week; compute median, p95, and peak.
3. Identify the loud QRM sources: the top contributing hosts / accounts / processes that dominate the floor (often service accounts, scanners, backup jobs).
4. Decide whether those QRM sources should be allow-listed out of the circuit or handled by per-entity baselines.
5. Compute the required SNR margin: how far above the per-bucket floor a malicious instance must sit to be reliably separable at the target reliability.

## Output

`outputs/noise-floor-<source>-YYYY-MM-DD.md` — floor statistics table (per hour-of-day), peak/trough ratio, ranked top noise contributors, and the recommended required-SNR margin feeding `/threshold-band`.

## Notes

- Measure the floor on quiet days only. A floor measured during an outage is poisoned (see `/space-weather`).
- A high peak/trough ratio is the signal that a static threshold will fail — route to `/diurnal-baseline`.
