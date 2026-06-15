# /kb-query — Answer a Spectrum Question, Grounded in the KB

Answer a spectrum question using **only** the knowledge base, with explicit citations and a clean abstain path when the KB doesn't cover it.

## Inputs

- A natural-language question (e.g. "what's the emitter at 868.3 MHz in Region 1?", "is the 433 MHz noise floor up vs. baseline?")
- The KB at `outputs/kb/`, glossary, and FAQ
- Optional: a required region / location filter

## Steps

1. **Normalize the question.** Expand abbreviations using the glossary; extract the constraints (frequency, band, region, service, time window).
2. **Retrieve.** Search KB entries by frequency-range overlap first, then by service/name/keyword. Pull the top matching entries and their provenance.
3. **Assess sufficiency.** Decide whether the retrieved entries actually answer the question. If coverage is partial or absent → **abstain**: say exactly what is and isn't known, and emit an OPEN question for `/gap-scan`. Do **not** fill the gap from general knowledge.
4. **Compose the grounded answer.** Answer in 1–3 sentences, citing entry IDs inline (`[kb:868300-lora-meter]`). Attach a confidence drawn from the cited entries' own confidence and recency (a `historical` or stale entry lowers it).
5. **Log the exchange.** Append the question + answer + cited IDs to `outputs/query-log.md` so it can later seed `/faq-generate`.

## Output

A grounded answer with inline citations and a confidence label, plus an appended line in `outputs/query-log.md`. On insufficient coverage: an explicit "not in KB" answer and a new OPEN question entry.

## Notes

- Citation or abstention is mandatory — an answer with neither is a defect. This is the workspace's core discipline.
- Prefer the most recent supporting capture; flag if the only support is older than the entry's `review_by` date.
- "I don't know, and here's the gap" is a *successful* outcome, not a failure — it routes work to `/gap-scan`.
