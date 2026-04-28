# Getting Started — VIP Motorcade Planning Workspace

A walk-through for a detail leader using this workspace for the first movement window.

## Before You Start

You should have:

- Written tasking to protect a specific principal (EP contract or government tasking).
- The principal's threat tier set (Tier 1 / 2 / 3) by the contracting office.
- A movement window with rough origin/destination pairs.
- Access to a planning workstation with markdown + an offline GIS tool of your choice.

You should *not* be using this workspace to:

- Plan movements you are not authorized to plan.
- War-game public officials' or executives' real schedules without authority.
- Generate red-team / attacker-side outputs.

If any of those apply, stop. The agent will refuse them and so should you.

## Step 1 — Onboard

Run `/onboard` and answer the interview honestly. Use placeholders for the principal — `[PRINCIPAL]`, callsigns, codenames. Real names and addresses do not belong in any synced file.

Onboarding takes ~30 minutes for a Tier 2 / Tier 3 corporate or diplomatic principal, longer for Tier 1 (where the threat-baseline call alone may be hours).

The workspace will write:

- `context/project.md` (sanitized)
- `context/role.md`
- `context/constraints.md`
- `planning/plan.md` (refreshed)
- `planning/comparison-weights.md` (new, copied from the defaults and tuned)

## Step 2 — Build the Threat Baseline

Run `/threat-baseline`. Have your authorized intel inputs ready:

- For corporate Tier 3 in low-risk AOR: open sources only (OSAC, State, FCDO, ACLED).
- For diplomatic Tier 2: open + your unit's intel summaries.
- For Tier 1: full unit feed plus host-nation liaison brief.

The baseline drives every subsequent likelihood score, so it has to be honest. Do not pad indicators that aren't there; do not minimize indicators that are.

Output: `outputs/threat-baseline-<YYYY-MM-DD>.md` with an explicit expiry date.

## Step 3 — Survey Three Candidate Routes per Leg

For each leg in the movement window, identify three candidate routes. Drive each one with the advance team (Tier 1 / Tier 2). Run `/route-survey` per route, capturing the 32-point checklist per segment.

Aim for 15–35 segments per 20-minute urban leg. Long unsegmented stretches hide variance.

Outputs: `outputs/<route-codename>/survey.md` × 3.

## Step 4 — Score Each Route

For each surveyed route, run `/risk-score`. The agent will:

- Anchor likelihood to the threat baseline.
- Score inherent L × I.
- Apply only mitigations actually present on this leg.
- Score residual L × I.
- Roll up to a route-level number with max-residual + High+ count.

Outputs: `outputs/<route-codename>/scoring-sheet.md` × 3.

## Step 5 — Compare and Decide

Run `/route-compare`. The agent applies your tuned weights, vetoes any Extreme-residual routes, and picks primary, alternate, and abort. Document any override (the principal asks for a specific route, the contracting office prefers one over another) in the decision file.

Output: `planning/route-decision-<YYYY-MM-DD>.md`.

## Step 6 — Plan Contingencies

Run `/contingency-plan` against the chosen primary. The agent will produce a one-page drill card per High+ residual segment, matched to the dominant hazard.

Outputs: `outputs/<route-codename>/contingencies/<segment>-<hazard>.md`.

## Step 7 — Advance and Brief

At appropriate lead time:

- `/advance-checklist` (T-72 h to T-12 h depending on tier and complexity).
- `/movement-brief` at T-2 h, producing operational, driver, and principal briefs.

## Step 8 — Move, Then After-Action

Run the movement. Within 24 hours, run `/after-action`. Be honest about deviations; the calibration of the matrix depends on it.

Output: `outputs/<window>/after-action-<YYYY-MM-DD>-<leg>.md`.

## Common First-Time Pitfalls

- **Skipping the alternate.** Two routes is a binary, not a choice. Always three.
- **Over-mitigating on paper.** "Advance team has cleared the route" cannot apply to all 30 segments simultaneously. Be specific.
- **Center-drifting the matrix.** Defaulting to L=3, I=3 is a calibration failure. Demand an anchor for every L≥3 and I≥3.
- **Treating the abort as an afterthought.** The abort is the most important route on the list when things go wrong. Score it for *survivability*, not comfort.
- **Forgetting to sanitize.** Real names and addresses leaving the local clone is the OPSEC failure that the workspace is built around preventing.

## Where to Get Help

- The agent's slash commands always have a "Refusal Conditions" or "Decision Rules" section — read it before going outside the rails.
- The 5×5 matrix card is at `resources/5x5-risk-matrix.md`.
- The doctrine bibliography is at `resources/doctrine-references.md`.
- For methodology questions, the principal source is `context/for-agent/domain-knowledge.md`.
