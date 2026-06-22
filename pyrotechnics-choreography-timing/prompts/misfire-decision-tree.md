# Misfire Decision Tree

## Purpose

Generate the live-show misfire / dud / hangfire decision tree for a specific show, product set, and regulatory regime — the shooter's contingency card. Use before show day. Decision sequencing only; physical handling stays with the licensed operator.

## Prompt Template

```
Build a misfire/hangfire DECISION tree for the firing line. Sequence operator decisions only.
Do NOT describe how to physically handle a live device — defer all stand-off/handling to the
permit, NFPA, and product guidance, leaving wait intervals as named parameters.

I have:

- **Firing system:** [electric module type / channels; manual or auto-fire]
- **Show structure:** [key chains/finale; which cues have downstream dependencies]
- **Regulatory regime + permit:** [jurisdiction; stand-off intervals as PARAMETERS]
- **Site plan:** [abort signal, safed-state procedure, personnel positions]
- **Context:** [anything that changes the continue/abort calculus]

Please:
1. Enumerate anomaly classes: no-fire, low/partial break, suspected hangfire, cascading/safety-relevant.
2. For each, give the decision branch: immediate action → wait interval (as a permit-referenced parameter) → continue/abort criterion.
3. State the explicit NEVER rules (never approach a hangfire, never blind re-fire, never compress the wait).
4. Map branches to the specific positions/chains they apply to.
5. Render as a one-page tree printable for the firing position.
```

## Expected Output

- A decision tree by anomaly class (action → wait → continue/abort).
- The explicit never-rules.
- A per-position/chain dependency map.
- A printable one-page contingency card, with wait intervals left as permit-referenced parameters.
