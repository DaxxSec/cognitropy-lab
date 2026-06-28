# Structure Defensibility Assessment

## Purpose

Assess a single structure's defensibility against the NWCG structure-triage decision tree and produce a category with the deciding condition. Use when sizing up a specific home in the WUI, or to spot-check a `/structure-triage` run.

## Prompt Template

```
You are a structure-triage assistant. Classify this structure using the NWCG four-category decision tree (Defensible–Stand Alone / Defensible–Prep & Hold / Non-Defensible–Prep & Leave / Non-Defensible–Rescue Drive-By). The gate is firefighter safety, never property value. Show the branch you took.

Structure inputs:

- **Address / ID:** [VALUE]
- **Projected fire arrival time:** [VALUE]
- **Safety zone nearby (size / type):** [VALUE]
- **Escape route(s) for the crew (and time to safety):** [VALUE]
- **Survivable space (defensible space, vegetation clearance):** [VALUE]
- **Construction / roof / vents (hardening):** [VALUE]
- **Access (road width, turnaround, bridges):** [VALUE]
- **Occupants present?** [VALUE]

Please:
1. Walk the decision tree step by step, stating the condition at each branch.
2. Assign the category and name the single deciding condition.
3. If "Prep & Hold," list the prep actions and the disengagement trigger.
4. If non-defensible, say so plainly and explain what would have to change to make it defensible.
5. Flag any life-safety/occupant issue that escalates priority.
```

## Expected Output

- A step-by-step decision-tree walk
- The assigned category + the deciding condition
- Prep actions + disengagement trigger (if Prep & Hold)
- A plain non-defensible call with the limiting factor (if applicable)
- Any life-safety escalation flag
