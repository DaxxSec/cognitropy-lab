# /faq-generate

Produce an audience-targeted FAQ document grounded entirely in the knowledge base, with every answer traceable to its supporting KB entries.

## Inputs

- Target audience: `home-fermenter`, `craft-producer`, or `educator` (sets depth and tone).
- Optional scope filter: limit to taxonomy areas (e.g. only `troubleshooting` + `safety-and-labeling`).
- Optional length target (number of questions) — otherwise driven by KB coverage.

## Steps

1. Read `context/workflows.md` §G (FAQ generation) and `context/concepts.md` §9 (FAQ design principles).
2. Load the KB from `outputs/kb/` (and `_index.md`).
3. Cluster entries by **user intent** and phrase each cluster as a question the chosen audience would actually ask (plain for home, process/compliance for producer, mechanism/citation for educator).
4. Answer each question **only** from KB entries; cite supporting entries inline (`[kb: <tag>/<slug>]`).
5. Tag each answer with the confidence of its **weakest** supporting entry. For safety-critical questions, soften or omit anything resting solely on `practitioner-lore`/`inferred`.
6. List unanswerable questions in a trailing **"KB gaps"** section instead of fabricating answers.
7. Write `outputs/faq/<audience>-YYYY-MM-DD.md`.

## Output

- `outputs/faq/<audience>-YYYY-MM-DD.md` — the FAQ document, each answer cited and confidence-tagged, with a KB-gaps appendix.
- A short coverage note in chat (questions answered vs. gaps).

## Notes

- A FAQ is a **projection** of the KB at a moment in time — regenerate after KB changes rather than hand-editing the published file.
- Never present a health/therapeutic claim as fact; if the KB only has `practitioner-lore` on a topic, frame it as "some practitioners report…".
- If two KB entries contradict on a question, surface the disagreement rather than silently picking one — and run `/kb-audit`.
