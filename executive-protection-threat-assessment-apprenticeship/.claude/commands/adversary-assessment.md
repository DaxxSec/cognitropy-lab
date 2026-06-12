# /adversary-assessment

Work up a specific threat actor across capability × intent × opportunity, applying behavioural-threat-assessment lenses, and generate EPA-3 / EPA-8 evidence.

## Inputs

- Subject identifier (person of concern, fixated individual, group) — lawful protective-intelligence nexus required
- All available indicators: communications, behaviours, prior contacts, public record
- The principal's risk profile (from `/protectee-risk-profile`)
- Apprentice author + current EPA-3 entrustment level

## Steps

1. Score **capability** (means, skills, weapons access), **intent** (stated, inferred, trajectory on the path to intended violence), and **opportunity** (proximity, knowledge of routine) — 1/3/5 per `context/references.md`.
2. Apply **TRAP-18** proximal warning behaviours and classify the subject as **hunter vs howler**; weight communicated threats appropriately (low correlation with action).
3. Check for **leakage** and **energy-burst / last-resort** indicators of mobilisation.
4. Assign a management recommendation: **monitor / interview / law-enforcement referral / harden** — with triggers that would escalate it.
5. Record the **EPA-3 (and EPA-8 if part of standing watch)** entrustment observation for the author.

## Output

`outputs/adversary-<subject-id>-<date>.md` — CIO scoring table, BTAM lens findings, hunter/howler call, management recommendation with escalation triggers, and the EPA evidence footer. Feed into `/attack-cycle-map`.

## Notes

- Structured **professional judgement**, not a numeric checklist that promotes a score to a verdict.
- Do not treat lawful protest/speech as a threat absent articulable indicators of intended violence.
