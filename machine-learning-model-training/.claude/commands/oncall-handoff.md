# /oncall-handoff

Produce a shift-handoff document for a long multi-day run so the next on-call picks up with full context and no surprises.

## Inputs

- Current run state: step, loss, grad_norm, throughput, GPU mem headroom
- The running incident log for this run (from `outputs/`)
- Open issues / watchpoints and any pending mitigations
- Next checkpoint ETA and remaining-budget estimate
- Escalation contacts and the metrics/alert dashboard link

## Steps

1. **Summarise current health** on the four axes (correctness, liveness, efficiency, integrity) with a one-line GREEN/YELLOW/RED per axis.
2. **List open incidents** with their severity, current state, and the next action expected.
3. **Call out watchpoints** — metrics trending toward a threshold, a node that retried, a checkpoint that's due, a long-sequence batch coming up.
4. **State the "do not touch" list** — in-progress mitigations the next shift should let run.
5. **Provide the runbook map** — which runbook to open for the failures most likely on this run, plus escalation contacts.
6. **Record ETA + budget** — next checkpoint, estimated completion step, remaining GPU-hour budget.

## Output

`outputs/handoff-<run>-<date>-<shift>.md`: a scannable handoff with the health summary, open issues, watchpoints, do-not-touch list, runbook map, and ETAs/contacts.

## Notes

- A good handoff is scannable in 60 seconds — lead with RED/YELLOW items.
- Always include the *last good checkpoint step* explicitly; it's the first thing the next shift needs in a crisis.
- Append handoffs to the same run log so the postmortem has the full multi-shift timeline.
