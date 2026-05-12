# Prompt — Revision Post-Mortem

Use after `/audit-revision` produces its decomposition table; this prompt turns the table into a stakeholder-facing post-mortem.

---

You are writing a one-page post-mortem explaining why a published GDP forecast differed from a newly released official print.

**Inputs you will be given:**
- `target_quarter` (e.g. 2024Q1)
- `prior_vintage` (date)
- `new_vintage` (date)
- `prior_print_value`, `new_print_value` (level and percent)
- `decomposition`: `{data_revision, model_drift, innovation}` each with level and percent contributions
- `component_contributions`: dict `{C, I, G, NX, ...}` of revision contributions
- `model_artifact_ref` (path + hash)
- `prior_forecast_ref` (path + hash)

**Structure your post-mortem as:**

### Headline (2 sentences)
State the prior print vs. new print and the headline delta. State which decomposition component dominates.

### Decomposition (table)
Markdown table: component | level contribution | percent contribution. Cite the sub-aggregates (C, I, G, NX) with the largest moves.

### Narrative (1 short paragraph)
Explain the dominant driver in plain language. Distinguish "the source revised the past" from "the model missed something" from "this was a genuine surprise."

### Implications for the model (1 short paragraph)
- If data revision dominated: do not refit aggressively; document the revision pattern.
- If model drift is large: open a `planning/` ticket and recommend `/estimate-model --refit`.
- If innovation is large and same-signed across recent quarters: flag bias; recommend specification review.

### What changes for the next forecast
A bullet list of concrete next steps with command names where applicable.

### References
Pin the manifest entry references for the prior forecast, prior vintage, new vintage, and model artifact. The reader must be able to walk back from the post-mortem to every input.

**Tone:** professional, honest, non-defensive. The post-mortem is the mechanism by which forecast skill is built — bury an honest assessment and you lose the learning.
