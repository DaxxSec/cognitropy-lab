# Pastry Lamination Dough Technique — Workflows and Methodology

How an expert actually works, organised around this build's technique: **stakeholder communication templates**. Analysis flows left-to-right (codify → run → read → diagnose) and every stage ends in a communication tuned to an audience.

## Workflow 1 — The codicological bake-analysis pipeline

The core loop, mirroring how a codex is studied (describe → transcribe → analyse → publish):

1. **Collate (design).** `/collation-formula` — fix the fold regimen and confirm the target layer count and notation before any dough is mixed. Output: the formula (e.g. `S·S·S = 3³ = 27 fat layers`).
2. **Codify (archive).** `/codify-lamination` — write the reproducible lamination codex: ingredients with %, dough/butter target temps, fold sequence with rests, proof and bake profile, expected crumb. This is the "fair copy" the house archives.
3. **Transcribe (record the run).** After production, `/transcribe-bake` — capture the *actual* run against the codex: real temperatures, real rest times, ambient T/RH, any deviation or correction. Faithful first; do not normalise to the spec.
4. **Read (diagnose).** If the result is off, `/diagnose-crumb` reads the cross-section evidence and names the fault from the visible signature (welding, gum line, bleed, weak feet).
5. **Stratify (root-cause).** `/defect-stratigraphy` traces the named fault back through the build to the stage that produced it (lock-in / turn N / rest / proof / bake).
6. **Communicate (publish).** `/stakeholder-brief` converts the finding into the right artifact for the right person (see Workflow 3).

## Workflow 2 — In-situ adjust vs. rebuild decision tree

When a build is drifting, decide whether to save the block or start over:

```
Is butter still discrete (no through-bleed)?
├─ YES → Is dough/butter temper within window? (see /butter-temper-window)
│        ├─ YES → continue; adjust rest time only. (in-situ)
│        └─ NO  → chill block 20–30 min to re-temper, then continue. (in-situ)
└─ NO (butter bled / layers welding)
         ├─ Pre-bake, < 1 turn done → re-chill hard; may recover. (in-situ, risky)
         └─ Pre-bake, ≥ 2 turns done → layers already merged → REBUILD.
                                        Log as defect; run /defect-stratigraphy.
```

Rule of thumb: temper faults caught early are recoverable; structural welding past two turns is not — escalate to a rebuild and a defect report rather than shipping a bready batch.

## Workflow 3 — Stakeholder communication workflow (the technique)

Every analysis is routed to an audience using a template from `prompts/`. The paleographer's discipline — *exact, layered, audience-aware description* — is what makes each communication trustworthy.

| Audience | Question they have | Template / prompt | Tone & length |
|---|---|---|---|
| Production line baker | "How exactly do I make this today?" | `production-spec-sheet` | Imperative, one page, numbers + timings |
| Head pastry chef / QA | "What failed and what's the fix?" | `lamination-defect-report` | Evidence → root cause → corrective action |
| F&B cost controller | "What did the defect cost; what's the yield?" | `cost-yield-memo` | Numbers-first, waste %, butter cost |
| Junior baker (training) | "Why does this step matter?" | `lamination-training-brief` | Explanatory, the "why" behind each fold |
| Front-of-house / marketing | "How do we describe this to guests?" | `menu-description-copy` | Sensory, accurate, allergen-declared |

**The five-part communication frame** (applied inside each template): **Audience → Purpose → Key message (one line) → Evidence (the transcription/diagnosis) → Action (what to do next).** Never send evidence without an action, or an action without its evidence.

## Workflow 4 — Onboarding a new ingredient lot

1. `/provenance-trace` — log the new flour/butter lot (supplier, lot #, fat % / protein %, receipt date).
2. `/butter-temper-window` — recompute the working temper window for the new fat %.
3. Run one codified test bake; `/transcribe-bake` it; `/diagnose-crumb` the result.
4. If crumb matches expectation, update the codex's material section; if not, `/defect-stratigraphy` and adjust before rolling the lot into production.
5. `/stakeholder-brief` → short change note to the line so the shift knows the lot changed and why.
