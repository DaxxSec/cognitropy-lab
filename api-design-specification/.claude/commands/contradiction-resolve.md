# /contradiction-resolve

Adjudicate a single `CONFLICT` block from a fusion brief. Produces a memo with the decision, the rationale, and the alternative that was rejected, so the next engineer doesn't relitigate. One memo per conflict.

## Inputs

- **Fusion brief** path and the `CONFLICT` topic line being resolved.
- **Conflicting claims** with their source ratings (copied from the brief).
- **Decision owner** — usually the technical lead for the surface; security/infra has lane veto where applicable.

## Steps

1. **Restate the conflict.** One paragraph: the spec element, the disagreeing sources, the substantive disagreement (not "people disagree" — the actual contested claim).
2. **Tabulate the positions.** One row per position: `position | supporting sources | combined rating | impact if chosen`. Combined rating uses the higher of corroborated A–F + 1–6 ratings; if positions are evenly matched, say so.
3. **Apply the default ordering** (from `context/concepts.md`): Standards > Peer specs > Internal corpus > Telemetry > Tickets > Stakeholder opinion. Note where this case agrees with the default and where it diverges.
4. **Apply known overrides.** Tier-1 customer ticket overrides corpus; security stakeholder overrides peer spec in the security lane; etc. If an override applies, name it.
5. **Decide.** One sentence stating the chosen position and the *single* rationale: "Chose position X because the standards-source dominates and the override case (tier-1 ticket) does not apply here."
6. **Document the rejected alternative.** Two-three sentences on what the rejected position was, why it was attractive, and what specifically caused it to lose. This is the bit that prevents the next engineer from re-running the same debate.
7. **Update the brief.** Replace the `CONFLICT — see /contradiction-resolve <topic>` line in the brief with `RESOLVED — see outputs/adjudication/<date>-<topic>.md` and the chosen position's claim block.

## Output

`outputs/adjudication/<date>-<topic>.md` with five sections: `Conflict`, `Positions`, `Default ordering & overrides`, `Decision`, `Rejected alternative considered`. Mark `STATUS: RESOLVED <date> by <name>` at the top.

## Notes

- An adjudication that is later overturned should not be deleted — append an `## Overturned <date> by <reason>` section and create a new memo. The audit trail must include the change of mind.
- If the decision is "stay with the conflict and revisit in N weeks", mark `STATUS: DEFERRED until <date>` and note what additional data is required.
- The combined rating column is the single most informative line for a reviewer in a hurry. Keep it scannable.
- Watch for **source-poisoning** patterns: a stakeholder filing tickets to manufacture a "ticket source" supporting their preferred position. Flag explicitly in the memo if suspected.
