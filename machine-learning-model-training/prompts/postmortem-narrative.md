# Blameless Postmortem Narrative

## Purpose

Convert a resolved incident's timeline and resolution into a polished, *blameless* postmortem with assignable action items. Use after recovery, once the facts are known.

## Prompt Template

```
You are facilitating a blameless postmortem for a training incident. Be rigorous and system-focused; never attribute fault to a person.

I have a resolved incident:

- **Incident summary:** [WHAT HAPPENED, ONE LINE]
- **Severity:** [SEV-x]
- **Timeline (raw):** [BULLETS: first signal → detection → actions → resolution, with times + steps]
- **Resolution:** [WHAT MITIGATION WORKED]
- **Impact:** [GPU-HOURS WASTED, WALL-CLOCK LOST, BUDGET, DATA/METRIC EFFECTS]
- **State before/after:** [CONFIG/DATA/CODE DELTA]

Please:
1. Write a clean chronological timeline (timestamps AND training steps; call out detection lag).
2. Run a "5 whys" to a system-level root cause (config/infra/data/code) — blameless language only.
3. List contributing factors that slowed detection or recovery.
4. Produce prioritised, assignable, falsifiable action items — flag which should become a new alert threshold or a new runbook.
5. Note what went well.
```

## Expected Output

- A blameless chronological timeline
- A system-level root cause via 5-whys
- Contributing factors
- Prioritised action items with owners (alert/runbook conversions flagged)
- "What went well" section, ready to save to `outputs/postmortem-<id>.md`
