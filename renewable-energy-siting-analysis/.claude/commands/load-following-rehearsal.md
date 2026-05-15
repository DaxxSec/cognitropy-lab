# /load-following-rehearsal

Run the proposed portfolio against a historical or synthetic load curve and bin the **cues** — moments where the portfolio is asked to stiffen, soften, or land a precise level — by severity. The puppetry analogy: a rehearsal day surfaces every place the choreography drops a beat, before opening night.

## Inputs

- `project_id` — articulation graph identifier.
- `pairing` — output of `/lead-follow-pairing`.
- `weight_transfer_plan` — output of `/weight-transfer-plan`.
- `slack_audit` — output of `/slack-budget-check`.
- `rehearsal_year` — one of: historical year (e.g. `2014` polar vortex, `2021` Texas Uri, `2020` heat dome), a stochastic load year synthesised from the BA's history, or the ISO's published stress-year case.
- `dispatch_logic` — `economic | reliability | hybrid`. Economic mirrors SCED; reliability stresses RA bucket call orders; hybrid is the realistic case.
- `LOLE_target` — typically `0.1 events/year` (1-in-10) per NERC. ISO variations documented in `context/references.md` Table R-6.

## Steps

1. **Rehearsal intake (`R-0`).** Verify pairing, weight-transfer plan, and slack audit are all current (re-run any that are stale before proceeding). Verify the rehearsal year's load and resource data are aligned (same hour-zero, same time zone). Abort at R-0 on misalignment.
2. **Setup the rehearsal harness.** Simulate hourly (or sub-hourly) for the full rehearsal year:
   - Lead joints dispatch per centerline × power curve.
   - Followers dispatch per the weight-transfer plan, subject to ramp and SOC constraints.
   - Drives (curtailment, DR) are called when followers saturate.
3. **Walk `R-1` — cue detection.** Bin every hour-step into one of:
   - **CLEAN** — followers and drives in their middle range; the portfolio "moved fluidly."
   - **STIFFENING** — followers approaching upper SOC bound or upper ramp limit; portfolio is overcommitted on energy.
   - **DROPPING-A-BEAT** — a 1-hour lag between a lead's drop and the follower's response; portfolio missed the cue.
   - **HOLD** — followers exhausted, drives partially called; not yet load shed but operating close to the LOLE limit.
   - **PULL-FROM-SERVICE** — load shed event; LOLE clock incremented.
4. **Walk `R-2` — LOLE and EUE tally.** Sum `PULL-FROM-SERVICE` hours over the rehearsal. Convert to LOLE (events/year, where an event is one continuous block) and EUE (MWh of unserved energy/year). Compare to LOLE_target.
5. **Walk `R-3` — cue clustering.** Cluster cues by time-of-year and meteorological driver: are the `HOLD` cues concentrated in summer evenings? In winter mornings with low-wind / cold-load coincidence? In shoulder-season with low-net-load over-generation? Each cluster maps back to a specific articulation node.
6. **Walk `R-4` — site-shift / size-shift backflow.** For each high-severity cue cluster, identify the upstream node — joint, linkage, drive — most responsible. Recommend an action: storage upsizing, additional joint, transmission upgrade, pair re-selection.
7. **Walk `R-5` — financial overlay.** Compute the lost revenue from curtailment hours, the LMP signal at cue hours, and the capacity-market payment for the portfolio's adjusted capacity credit. The financial overlay is what determines whether a `REWORK` is worth chasing or whether the portfolio is "good enough."
8. **Aggregate `R-6`.** Emit a rehearsal verdict.
9. Save to `outputs/<project_id>/rehearsal-<rehearsal_year>-<YYYYMMDD>.md`.

## Output

Markdown rehearsal containing:

- Rehearsal year, dispatch logic, LOLE target.
- Cue summary: counts of CLEAN / STIFFENING / DROPPING-A-BEAT / HOLD / PULL-FROM-SERVICE.
- LOLE and EUE for the rehearsal year vs target.
- Cue clusters with time-of-year and meteorological annotation.
- Per-cluster upstream node trace.
- Recommended remediation per cluster.
- Financial overlay: total curtailment lost-revenue, LMP-weighted dispatch revenue, capacity-market clearing payment.
- Aggregate verdict: `RA-PASS | RA-REWORK | RA-REJECT`.

## Notes

- One rehearsal year is a *test*, not a proof. A serious siting decision rehearses against ≥3 historical years, ideally including a stress year (Uri, polar vortex, heat dome).
- LOLE math is sensitive to the load shape assumed. EIA Form 930 actuals are the public starting point; the BA's own load forecast is preferable. Document which is used.
- Synthetic load years (stochastic) are useful for tail-risk analysis but should never *replace* historical rehearsals — historical years carry the meteorological texture stochastic synthesis misses.
- A rehearsal that comes back with all CLEAN cues is suspicious. Real grids drop beats; if your portfolio doesn't, the rehearsal harness is probably hiding a constraint (e.g. infinite-bus-bar assumption, perfect-foresight dispatch). Verify before celebrating.
- Always tag whether the rehearsal includes the *other developers* in the queue or just your portfolio. Solo rehearsals over-estimate ELCC by ~15-30% in thick queues.
