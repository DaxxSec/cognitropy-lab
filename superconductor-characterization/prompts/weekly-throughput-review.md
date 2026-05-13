# weekly-throughput-review

## Purpose

Run every Monday morning to compare last week's planned vs. actual queue performance, identify drift in service-time or cryogen burn, and update the capacity model before the new week's commitments are made. The output is a single page a lab lead can take to the planning meeting.

## Prompt Template

```
You are the characterization lab capacity reviewer. Produce this week's throughput review.

I have the following inputs:

- **Reporting week:** [YYYY-Www]
- **Planned vs actual samples completed:** [N planned / M actual; list deferrals and reasons]
- **Planned vs actual cryostat hours per server:** [VALUE]
- **Planned vs actual magnet hours per magnet:** [VALUE]
- **LHe inventory at week-start / week-end / total consumed:** [VALUE]
- **Recovery plant uptime and L/day liquefied:** [VALUE]
- **Incidents (quenches, cryostat faults, contact-resistance reworks):** [VALUE]
- **Updated service-time samples from completed measurements:** [VALUE]
- **Context:** [any external event that disturbed the plan — vendor delay, holiday, equipment delivery]

Please:
1. Compute attainment ratios: completed / planned, cryostat-hours actual / planned, helium burn actual / planned.
2. Update E[S] and Var[S] for each measurement type using this week's samples; report the new C_s².
3. Recompute ρ for the current 4-week horizon with the new service-time estimates; compare to last week's forecast.
4. Identify drift: where did the plan miss, and why (service-time creep, intake spike, cryostat downtime, helium loss)?
5. Recommend three actions for the coming week — most-impact first; tie each to a specific command rerun (`/sample-queue-plan`, `/lhe-budget`, `/magnet-ramp-schedule`).
6. List samples promoted / demoted in priority because of this week's results.
7. Highlight any incident that needs `prompts/cryostat-incident-debrief.md` follow-up.
8. End with the one number that summarises the week: utilisation ρ across the cryostat fleet.
```

## Expected Output

- One-page markdown report at `outputs/_capacity/weekly/<YYYY-Www>.md`.
- Updated `outputs/_capacity/service-times.csv` with this week's samples appended.
- Updated horizon-level capacity plot (ρ vs week) — re-runs `/sample-queue-plan` against the new E[S].
- Three-action list with owners and deadlines, posted to the lab planning channel.
- A red / amber / green status line on whether utilisation is sustainable.
