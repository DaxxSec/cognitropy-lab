# KB Entry Canonicalize

## Purpose

Use this prompt to turn a raw note, quote, or observation into one or more canonical knowledge-base entries that match the workspace schema — the manual companion to `/kb-ingest` when you want to hand-shape a tricky source.

## Prompt Template

```
You are the KB curator for a vinegar-fermentation knowledge base. Convert the raw material below into canonical KB entries.

Canonical schema per entry: title, body, taxonomy (one+ of: microbiology, biochemistry, methods, parameters, troubleshooting, measurement, safety-and-labeling, styles, equipment), provenance (source + locator), confidence (measured | published | practitioner-lore | inferred), related.

Raw material:

- **Source type:** [own-batch | authoritative | community/anecdote | my-reasoning]
- **Source locator:** [book p.#, DOI, URL, batch ID, "personal observation"]
- **Raw text / note:** [paste]

Please:
1. Split the material into ATOMIC claims (one fact/topic per entry — do not bundle).
2. Assign each a default confidence from the source type, adjusting if the content warrants.
3. Tag each with the correct canonical taxonomy term(s); do NOT invent new tags without flagging it.
4. Flag any claim that contradicts a likely-existing entry as a CONTRADICTION for /kb-audit.
5. Output each entry as a ready-to-save Markdown block with the full schema filled in.
```

## Expected Output

- One Markdown block per atomic claim, each with title / body / taxonomy / provenance / confidence / related filled in.
- Correct confidence mapping from the source type, with any justified adjustments noted.
- Any contradictions or new-tag requests flagged explicitly for `/kb-audit`.
