# Session Log Template

Use one entry per session. Append; do not overwrite. Always relative time (T-) for movement-related items; absolute date for planning-cell items.

## Entry Template

```
## YYYY-MM-DD — <session theme>
- Operator (placeholder): [DETAIL_LEAD], [PLANNER_A]
- Window (if applicable): <window codename>
- Phase: [onboard / threat-baseline / route-survey / scoring / comparison / contingency / brief / advance / movement / after-action]

### Did
- [bullet — concrete actions taken]

### Decided
- [bullet — what was chosen / approved / rejected and why, in one line]

### Outstanding
- [bullet — what's blocked, what needs more info, what the next session must address]

### Sensitive items NOT logged here
- [reference only — e.g. "real PIs in outputs/<window>/sensitive/principal-profile.md"]
```

## First Entry — Workspace Creation

## 2026-04-28 — Workspace authored

- Operator: cognitropy-daily-build
- Phase: scaffold
- Did: authored CLAUDE.md, README, CREATION_REPORT, all `context/` files including `for-agent/{domain-knowledge,workflows,environment,tools}.md`, all 9 slash commands, 3 prompts, 4 resources, planning/plan.md, this session-log seed, and user-docs.
- Decided: scope is defensive-only; matrix is canonical 5×5; route plans require primary + alternate + abort minimum.
- Outstanding: no real principal yet; first `/onboard` will populate `context/project.md`.
