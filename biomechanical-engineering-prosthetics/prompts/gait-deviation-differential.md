# gait-deviation-differential

## Purpose

Use when a gait-lab session shows a specific deviation (excessive trunk lean, drop-off at heel-strike, lateral whip, vaulting, etc.) and the question is differential diagnosis — is it socket-fit, alignment, component, gait pattern, or measurement artefact?

## Prompt Template

```
Acting as the biomechanical engineer reviewing a gait-deviation finding for differential diagnosis.

Session context:

- **Patient ID / pseudonym:** [VALUE]
- **Amputation level + side:** [VALUE]
- **K-level + time since fit:** [VALUE]
- **Observed deviation (specific):** [e.g. "excessive lateral trunk lean over prosthetic side during stance, peak 12° at midstance"]
- **Deviation severity vs. last session:** [new / worsening / stable / improving]
- **Patient-reported symptoms (if any):** [pain location / discomfort / instability / fatigue]
- **Recent SPC chart state:** [in-control / signals present — describe]
- **Recent component changes:** [VALUE]
- **Walking aid status:** [none / cane / crutches / walker]
- **Gait-lab measurement system state:** [last Gauge R&R date + result]

Please:
1. Build a differential list — the top 4-6 candidate causes of this specific deviation in this patient, in rank order of prior probability.
2. For each candidate cause, name the diagnostic test or measurement that would discriminate it from the others (e.g. "if cause is alignment varus, then prosthetic-side knee adduction moment should be elevated; if cause is residual-limb pain, then patient should reduce prosthetic-side stance time").
3. Recommend the discrimination sequence — what to check first, what conditional follow-ups depending on result.
4. Flag whether any candidate causes have immediate safety implications (component fatigue precursor, fall risk).
5. Note the cross-references to other workspace commands that should be run as part of the discrimination (`/socket-fit-control-chart`, `/gait-asymmetry-detect`, `/manufacturing-cpk-audit` for component-side queries, etc.).
```

## Expected Output

- Ranked differential diagnosis list with prior-probability framing
- Per-candidate discrimination test definition
- Sequential discrimination plan
- Safety-flag highlights for any urgent-investigation candidates
- Cross-references to relevant workspace commands

## Notes

- Don't propose a single cause; the value of this prompt is the *differential* — surfacing the alternatives.
- Measurement artefact is ALWAYS a candidate cause; if Gauge R&R is stale, that goes near the top of the list.
- Cite Perry & Burnfield or another gait-deviation reference for the kinematic/kinetic interpretation; don't reason from first principles when published reference patterns exist.
- Some deviations are *compensatory* — the patient is doing something deliberate to avoid a different pain or instability. Don't "fix" a compensation without understanding what it's compensating for.
