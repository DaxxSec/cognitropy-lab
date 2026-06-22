# /timing-spec

Author the formal specification catalog — turn the show's safety and artistic rules into named, labeled proof obligations the verifier can discharge.

## Inputs

- The canonical cue sheet (`outputs/cue-sheet-*.md`).
- Safety framework: NFPA 1123 (outdoor) or 1126 (proximate), plus any stricter AHJ permit conditions.
- Firing-hardware limits: per-module max simultaneous e-matches / current budget, channel count.
- Artistic goals: which cues are "hero" (beat-locked), the music length, density preference.

## Steps

1. Select the framework and pull the binding numbers (min distances, max bore, runtime tail) from `context/references.md` and the permit.
2. Instantiate the canonical obligation set from `context/concepts.md` (SEP, REUSE, CURR, CHAN, RUNTIME, SYNC, FALLOUT, DENSITY), giving each a stable ID.
3. For each obligation write: a one-line plain statement, a formal statement (interval / geometry / STL form), the tolerance or margin, and the command that discharges it.
4. Mark each obligation's initial status `open`; record any premises as `assumed` (e.g. `A1: wind ≤ 12 mph SW`) so the weather gate can later discharge them.
5. Tag obligations safety vs. artistic (safety dominates in triage) and note any that bind together (finale → SEP+CURR+CHAN).

## Output

`outputs/spec-catalog-YYYY-MM-DD.md`: the obligation table (ID, statement, formal form, tolerance, status, discharging command, safety/artistic tag) plus the assumptions list `A1..An`.

## Notes

- An obligation without a tolerance is not checkable — always pin the number (±τ, ≥0 s, ≥ d ft).
- Keep assumptions explicit and few; each one becomes a show-day gate condition.
- Re-run when the framework, hardware, or artistic goals change — not on every cue edit (that's `/verify-schedule`).
