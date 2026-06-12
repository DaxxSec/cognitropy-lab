# /progression-review

Aggregate an apprentice's portfolio, place them on the Dreyfus ladder, make evidence-based entrustment decisions, and find the weakest EPA to drive deliberate practice.

## Inputs

- The apprentice's portfolio of `signoff-*` evidence records and `outputs/roster.md`
- Review cadence trigger (monthly) or a pending entrustment decision
- Any AARs and live-operation observations since the last review

## Steps

1. Aggregate evidence **per EPA**; require **≥2 independent observations** at a level before raising the entrustment ceiling to it — no single-artifact promotions.
2. Look across EPAs for a coherent **Dreyfus stage** pattern; update the role (Trainee → Shift → Advance → Detail Leader → Detail Commander) only when the pattern supports it.
3. Make explicit **entrustment decisions** per EPA with written rationale; flag any EPA where *live-operation* use should still be bounded below the recorded level.
4. Identify the **weakest EPA** (lowest entrustment or thinnest evidence) — the deliberate-practice target.
5. Update `outputs/roster.md` and write a dated review record.

## Output

`outputs/progression-<apprentice>-<date>.md` — per-EPA evidence summary, updated entrustment levels with rationale, Dreyfus stage call, the weakest-EPA target, and any live-operation bounds. Roster updated.

## Notes

- Advancing on tenure or likeability is the cardinal sin — it puts an under-qualified agent between the principal and a threat. Keep every decision auditable.
