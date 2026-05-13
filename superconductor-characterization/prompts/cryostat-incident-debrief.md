# cryostat-incident-debrief

## Purpose

Run after any unplanned event that consumes capacity — magnet quench, cryostat thermal-runaway, contact-resistance rework, instrument failure, cryogen-plant trip. Captures the technical cause, the capacity cost, and the procedural change. The debrief feeds back into `/lhe-budget`, `/sample-queue-plan`, and `/magnet-ramp-schedule` so the model improves with each incident.

## Prompt Template

```
You are the characterization lab post-incident reviewer. Conduct a blameless debrief.

I have the following inputs:

- **Incident date / time:** [VALUE]
- **Type:** [magnet quench / cryostat thermal-runaway / cryogen-plant trip / contact rework / instrument failure / safety event]
- **Detection signal:** [voltage-tap trip / pressure spike / O2 alarm / operator observation]
- **Sample in progress (if any):** [Sample ID, measurement command, fraction complete, recoverable Y/N]
- **Magnet field at incident:** [VALUE]
- **LHe lost:** [VALUE] liters; LN2 lost: [VALUE] liters
- **Measurement / coil voltage trace artifacts:** [pointer to raw file under `outputs/_incidents/`]
- **First-response actions taken:** [VALUE]
- **Operator narrative:** [free text]
- **Context:** [any environmental factor — lab temperature, electrical event, holiday backfill on duty]

Please:
1. State the proximate cause in one sentence and the contributing factors in three.
2. Compute the capacity cost: hours of cryostat/magnet downtime, LHe lost, samples deferred, total lead-time slip propagated through the queue.
3. Identify which command's working assumptions were violated (`/lhe-budget` headroom too thin? `/magnet-ramp-schedule` training underestimated? `/sample-queue-plan` ρ already in stress band?).
4. Propose three procedural changes — each one a concrete edit to a workflow, a command's input default, or a reference table.
5. Recommend whether a magnet retraining schedule, vendor consultation, or safety-officer briefing is required.
6. Estimate the residual risk class (low / medium / high) of a recurrence within 4 weeks if no procedural change is made.
7. Output the updated capacity plan: rerun `/sample-queue-plan` and `/magnet-ramp-schedule` for the next 2 weeks excluding the down-server hours; list which samples slip.
8. End with the one-line lessons-learned entry suitable for the weekly throughput review.
```

## Expected Output

- Incident report at `outputs/_incidents/<YYYY-MM-DD>-<type>.md`.
- Updated capacity plan referenced from the next `/sample-queue-plan` run.
- Procedural-change list, with each item assigned to a workflow file in `context/` or a command default in `.claude/commands/`.
- Residual-risk classification and recommended re-evaluation date.
- A one-line entry for the lab's running incident log.
