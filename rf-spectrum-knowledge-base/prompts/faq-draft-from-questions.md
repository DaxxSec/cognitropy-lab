# FAQ Draft From Questions

## Purpose

Convert a batch of recurring analyst questions into grounded FAQ Q&A pairs, each cited to KB entries or references — or flagged OPEN when the KB can't yet answer. Use when refreshing `outputs/faq.md` after an ingest or a wave of similar questions.

## Prompt Template

```
You are the RF spectrum knowledge engineer. Generate FAQ entries from these questions, grounded ONLY in the knowledge base and references — never from general knowledge.

Questions (with frequency of asking if known):
- [question 1] (asked [N] times)
- [question 2]
- [question 3]
- ...

Available knowledge: outputs/kb/, outputs/glossary.md, context/references.md

Please:
1. Cluster the questions by topic and intent; order clusters by how often they're asked.
2. For each, write a 1-3 sentence answer citing specific KB entry ids ([kb:...]) or references ([ref:...]).
3. If the KB does not support an answer, mark the question OPEN — do NOT invent content — and note what evidence would close it.
4. Assign each answer a confidence and a "last verified" date drawn from the cited entries.
5. Output in the FAQ entry template from context/references.md, grouped into sections.
```

## Expected Output

- Sectioned FAQ entries, each answer carrying inline citations, confidence, and a verified date
- An `OPEN QUESTIONS` list for anything the KB can't answer (hand off to `/gap-scan`)
- A short "what changed" note if refreshing an existing FAQ (added / updated / newly OPEN)
