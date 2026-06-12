# /apprentice-tasking

Generate the next supervised assignment that targets an apprentice's weakest competency at the edge of their ability, fading scaffolding as entrustment grows.

## Inputs

- The weakest EPA and current entrustment level (from `/progression-review`)
- Available real assignments and the upcoming operational schedule
- The apprentice's Dreyfus stage and learning notes

## Steps

1. Take the **weakest EPA** from the latest progression review.
2. Choose a **real or scenario assignment** that exercises *exactly* that competency, set **one entrustment level above** where the apprentice is comfortable (the deliberate-practice edge).
3. Set the **scaffolding to remove** (cognitive-apprenticeship fade: modelling → coaching → scaffolding → articulation → reflection → exploration) and the **specific feedback target**.
4. Assign supervisor, due date, the supervision level appropriate to current entrustment, and the WBA (`/competency-signoff`) that will close the loop.
5. Confirm the tasking never requires the apprentice to operate **above** their current entrustment on a **live** detail; if it would, route the live portion to a qualified agent and keep the apprentice on the scenario.

## Output

`outputs/tasking-<apprentice>-<date>.md` — the assignment, the targeted EPA and edge level, scaffolding-fade plan, supervisor/due-date, and the closing WBA. Feeds back into the dual-purpose loop.

## Notes

- Practice the **weakest** competency, not the favourite one. Comfort is the enemy of deliberate practice.
- The "edge of ability" is one step beyond comfort — far enough to stretch, near enough to succeed with support.
