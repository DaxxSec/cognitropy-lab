# /weight-transfer-plan

Plan the diurnal and seasonal **weight transfer** — how the system shifts active capacity between joints — and produce a ramp-coordination schedule with NERC BAL-001-2 ACE-budget compliance check. The puppetry frame: a clean weight transfer is the difference between a coordinated puppet step and a stumble.

## Inputs

- `project_id` — articulation graph identifier.
- `pairing` — output of `/lead-follow-pairing` (the pairs and their followers).
- `BA_id` — Balancing Authority responsible for the portfolio. Determines the applicable BAL-001-2 ACE limit (CPS-1, CPS-2, BAAL).
- `representative_days` — 4 to 12 days that span the operating envelope: hottest day, coldest day, lowest-net-load day (spring), highest-net-load day, two outage days. Load and resource series for each.
- `ramp_horizon` — `10min | 30min | 1hour | 4hour`. The 10-minute is for BAL-001 compliance; the others map to ISO ancillary-services products.
- `forecast_lag` — `day_ahead | 4hour | 1hour | 5min`. Operationally, day-ahead matters for unit commitment; 5-min matters for SCED.

## Steps

1. **Choreography intake (`W-0`).** Verify pairing is complete, BA identified, ≥4 representative days supplied. Abort with REWORK at W-0 on missing inputs.
2. **Per-representative-day walk.** For each day:
   - Compute the lead joint's expected hourly output.
   - Compute the residual load shape (gross load − fixed/firm generation − leads).
   - Identify the **weight-transfer windows**: hours where the residual load is rising or falling steeper than the lead alone can match. These are the "puppet steps" — the moments where one joint hands motion off to another.
   - For each window, write a primary–secondary assignment: which joint leads the motion, which follower closes the gap, which drive (curtailment / DR) handles overflow.
3. **Walk `W-1` — ACE-budget check.** Sum the 10-minute net-load ramp implied by the schedule and compare to the BA's BAAL or CPS-2 limit. Any window exceeding the limit gets flagged for storage augmentation or for explicit DR commitment.
4. **Walk `W-2` — ramp-rate feasibility per joint.** Storage: discharge ramp rate (typically full-power within seconds for lithium, minutes for flow). Hydro: spillway and Francis-turbine ramp limits (often 10-30% of nameplate per minute). Gas peakers: warm-start lag (5-15 min cold, 1-5 min warm). Flag windows that exceed the joint's mechanical ramp.
5. **Walk `W-3` — sympathetic-motion echo.** Where two leads in the same shed both ramp down together (cloud cell over two solar joints, wind speed dropping across one MERRA-2 cell), the *combined* ramp the followers must absorb is larger than the sum-of-individual-leads case. Pull from `/sympathetic-motion-audit` and adjust.
6. **Walk `W-4` — seasonal transfer.** Across the representative days, identify the seasonal weight-transfer themes: who carries summer evenings (often solar→battery→gas), who carries winter mornings (often firm→wind→demand), who carries shoulder-season low-net-load hours (curtailment drive).
7. **Aggregate `W-5`.** Emit a per-day choreography table and a portfolio-level seasonal narrative.
8. Save to `outputs/<project_id>/weight-transfer-plan-<YYYYMMDD>.md`.

## Output

Markdown plan containing:

- Per-day choreography table: `time_window, primary_joint, secondary_joint, drive, expected_ramp_mw_per_10min, BAL-001 check`.
- Seasonal narrative (summer peak, winter peak, shoulder, low-net-load).
- ACE-budget compliance summary against BAL-001-2 limits.
- Storage-follower duty-cycle implications (cycles/year per follower) — feeds into degradation modelling.
- Per-day and portfolio-level verdicts.
- Suggested follow-up: `/slack-budget-check` if any drive saturates; back to `/lead-follow-pairing` if a follower's ramp rating is the bottleneck.

## Notes

- The weight-transfer plan is a *planning* artifact, not a real-time dispatch order. Operations runs SCED every 5 minutes; this command writes the choreography that SCED is expected to land near.
- If the plan calls for a curtailment drive to handle ramps, double-check the OATT and the PPA — many PPAs cap deliverable curtailment hours per year. Beyond the cap, the IPP eats the lost revenue.
- Hydro reservoir joints carry seasonal flexibility that battery joints cannot match — but they also carry environmental flow constraints (downstream temperature, fish passage windows) that often bind in the same months the system needs them most. Coordinate with the FERC license, not just the resource model.
- DR drives are *non-binding* by default. A weight-transfer plan that depends on DR for >10% of capacity-coincident-hour ramp should carry a `MONITOR` verdict regardless of other outputs.
