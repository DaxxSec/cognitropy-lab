# /release-gate

Triage open defects and tech debt for a release on cost-benefit — fix-now vs defer vs won't-fix — with safety and security defects exempt from deferral, so "ship it" is a deliberate decision, not perfectionism or panic.

## Inputs

- The open defect + tech-debt list, each with a severity and a fix cost/risk estimate
- Proximity to the freeze/release and the regression risk of late changes
- The current budgets (flash/RAM/power) and build reproducibility status

## Steps

1. Classify each item by **severity**: safety/security > data loss > functional > cosmetic.
2. Apply the **hard rule**: safety/security defects **block** the release — they are not subject to cost-benefit deferral.
3. For the rest, weigh **user impact × likelihood** against **fix cost + regression risk** near the freeze.
4. Decide fix-now / defer-to-patch / won't-fix for each; record the rationale.
5. Confirm budgets still hold at ship and the **build is reproducible** (toolchain + flags pinned).

## Output

`outputs/projects/<name>/release-gate.md` — the triaged list with verdicts and rationale, the blocking items, and the budget/reproducibility sign-off.

## Notes

- Near a freeze, a risky fix for a low-impact bug usually **defers** — the regression risk outweighs the benefit.
- No safety or security item ships unfixed; if it can't be fixed in time, the release slips. That line is not negotiable.
