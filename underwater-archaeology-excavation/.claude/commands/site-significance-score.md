# /site-significance-score

Score a site's archaeological significance with a structured rubric, producing the **benefit currency** the CBA needs instead of an asserted "this is important".

## Inputs

- Site description, period/date estimate, type, and known parallels.
- Preservation state and what survives (structure, cargo, organics, personal material).
- Prior research context: what questions the site could answer; how rare it is regionally/nationally.
- Optional: existing Historic Environment Record / national register entry.

## Steps

1. Read `context/references.md` ("Significance Assessment Criteria").
2. Score each dimension on a fixed scale (e.g. 0–4): research/scientific value, historic value, aesthetic/artistic value, communal/social value, rarity, period representativeness, group/association value, preservation potential.
3. Justify each score in one line with a concrete reason — a score with no justification is not defensible to a reviewer.
4. Apply weights appropriate to the decision context (a research grant weights research value; a public museum weights communal value). State the weights.
5. Aggregate to a single weighted significance figure and a qualitative tier (local / regional / national / international).
6. Note the **epistemic uncertainty** — which scores would move most with cheap further evaluation (Phase 2/3).
7. Hand the figure to `/insitu-vs-excavate`, `/threat-decay-model`, and `/recovery-prioritization` as the benefit input.

## Output

`outputs/significance-<site>-YYYY-MM-DD.md`: the scored, justified, weighted rubric, the aggregate figure and tier, the weighting rationale, and a note on which scores are most uncertain.

## Notes

- Significance inflation is the field's default bias — every excavator's site feels significant. The rubric exists to discipline that.
- Significance is *relative to a question and a context*; record both so the score is interpretable.
- Where significance is highly uncertain, recommend a cheap evaluation phase before committing the CBA to it.
