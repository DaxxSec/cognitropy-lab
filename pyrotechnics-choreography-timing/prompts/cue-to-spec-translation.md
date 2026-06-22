# Cue-to-Spec Translation

## Purpose

Translate an artistic brief and a music track into formal timing obligations — turn "the finale should feel huge and land on the drops" into named, checkable specs with tolerances. Use at the start of design, before any verification.

## Prompt Template

```
You convert artistic intent for a fireworks show into formal, checkable proof obligations.

I have:

- **Artistic brief:** [DESCRIBE the feel, structure, accent moments, finale intent]
- **Music map:** [BEAT/DOWNBEAT TIMES or PATH; mark the "drops"/hero moments]
- **Inventory available:** [bores/effect types on hand]
- **Site & framework:** [outdoor 1123 | proximate 1126; rough geometry; permit limits]
- **Context:** [show length, audience, constraints]

Please:
1. Identify the hero cues (beat-locked) and assign each a sync tolerance τ by role.
2. Express the artistic goals as SYNC / DENSITY / RUNTIME obligations with explicit tolerances.
3. Note which safety obligations (SEP, FALLOUT, REUSE, CURR, CHAN) the brief will stress (e.g. dense finale → CURR/SEP).
4. Flag any artistic goal that is likely to conflict with a safety obligation, and say which must yield (safety wins).
5. Emit the draft spec catalog with assumptions listed separately.
```

## Expected Output

- A hero-cue list with per-cue sync tolerances.
- Artistic obligations (SYNC/DENSITY/RUNTIME) written formally with tolerances.
- A note of the safety obligations the brief stresses and any predicted conflicts.
- A draft spec catalog ready for `/verify-schedule`.
