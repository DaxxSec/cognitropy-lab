# /training-postmortem

Drive a blameless postmortem after a SEV-1/SEV-2 training incident is resolved, and extract action items that prevent recurrence.

## Inputs

- The incident record(s) and run log from `outputs/`
- The resolution: what mitigation worked and at what cost
- Metrics around the incident (wasted GPU-hours, wall-clock lost, budget burned)
- The config/data/code state before and after the incident

## Steps

1. **Reconstruct the timeline** — first signal → detection → each action → resolution, with both timestamps *and* training steps. Note detection lag explicitly.
2. **Quantify impact** — GPU-hours wasted, wall-clock lost, budget burned, and any data/metric-integrity consequences.
3. **Find the root cause blamelessly** via "5 whys", landing on a *system* condition (config / infra / data / code) — never an individual.
4. **List contributing factors** — what made detection slow or recovery hard (missing alert, sparse checkpoints, no runbook, ambiguous ownership).
5. **Write action items** — each assignable, falsifiable, prioritised. The strongest convert into a new alert threshold (`/run-healthcheck`) or a brand-new runbook in `.claude/commands/`.
6. **Capture what went well** so good practices survive, and circulate the postmortem.

## Output

`outputs/postmortem-<id>.md`: timeline, impact, root cause, contributing factors, prioritised action items (with owners), and "what went well". New failure classes get promoted into runbooks.

## Notes

- Blameless means the language describes the *system*: "the config allowed an LR with no warmup", not "X set a bad LR".
- The best postmortem output is a *deleted future incident* — i.e. a new alert or runbook, not just a writeup.
- Even a clean recovery deserves a lightweight postmortem if detection was slow; slow detection is itself the finding.
