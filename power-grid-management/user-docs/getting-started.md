# Getting Started — Power Grid Management Workspace

This workspace is a long-lived reasoning environment for grid spatial analysis. It is not a GIS, a load-flow tool, or an OMS — it is a place to *think about* grid problems with an agent that understands grid structure and spatial methods.

## The First Fifteen Minutes

1. **Clone or open this workspace in your Claude environment.**
2. **Run `/onboard`.** Answer honestly about your role and experience — Grid Spatial Analyst calibrates its depth to what you tell it. You can update later.
3. **Skim `context/for-agent/workflows.md`** to see the analytical workflows the agent understands. If your active goal fits one of them, say so when you start the next session.
4. **Add your active analysis to `context/project.md`.** One sentence is enough. Include the decision it informs.
5. **Drop your data references into `resources/` or point to paths.** For sensitive utility data, follow the redaction checklist in `context/constraints.md` *before* pasting.

## How Sessions Typically Go

- You open with a question.
- The agent restates it and asks about data + scope.
- The agent proposes a method and walks through reasoning.
- You either execute in your own tooling and come back with results, or the agent helps you think through a question that doesn't need external tools.
- You log the session before closing.

## How to Get Good Answers

- **Be specific about what you know and don't know.** "I can read a one-line but I don't have load-flow access" is far better than "I'm an analyst."
- **Bring actual data when it matters.** Coordinates, attribute names, CRS, time windows. The agent will refuse to invent data.
- **Say what decision the analysis informs.** An analysis for a screening memo is different from one for a regulatory filing.
- **Use the slash commands.** They scope the agent's behavior appropriately (`/analyze` is rigorous method-first; `/outage` frames spatial investigation; `/map` focuses on design; `/topology` stays on graph reasoning).
- **Push back.** If the agent's reasoning assumes something wrong about your system, say so — it will update.

## When to Escalate Outside This Workspace

- **Operational decisions** — switching, relay setting changes, work orders, permits. Your utility's ops and planning processes own those.
- **Safety-critical live situations** — if uncertainty meets live equipment, stop, preserve the state, escalate to the authorized person on site.
- **Formal reliability events** — NERC / regional reliability coordinator / ISO processes own the investigation of reportable events. This workspace helps you prep, not file.
- **Cyber-physical incidents** — your SOC and E-ISAC processes govern response. This workspace helps you think through the geography, not attribute attacks.
