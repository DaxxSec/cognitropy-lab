# FAQ Set From Knowledge Base

## Purpose

Use this prompt to generate a complete, audience-targeted FAQ document from the current vinegar knowledge base, with every answer cited and confidence-tagged. This is the prompt behind `/faq-generate` when you want fine control over scope and tone.

## Prompt Template

```
You are the knowledge editor for a vinegar-fermentation knowledge base. Generate a FAQ document grounded ONLY in the KB entries provided.

I want a FAQ for:

- **Audience:** [home-fermenter | craft-producer | educator]
- **Scope / taxonomy areas:** [e.g. all, or "troubleshooting + safety-and-labeling only"]
- **Number of questions:** [e.g. 12, or "as many as the KB supports"]
- **KB entries:** [paste or reference outputs/kb/ entries with their tags, provenance, confidence]
- **Tone constraints:** [e.g. "no medical claims; safety-first for beginners"]

Please:
1. Cluster the KB entries by user intent and phrase each as a question this audience would actually ask.
2. Answer each question using only the supplied entries; cite the supporting entries inline as [kb: <tag>/<slug>].
3. Tag every answer with the confidence of its weakest supporting entry.
4. For any safety-critical question backed only by practitioner-lore/inferred entries, soften the claim or omit it.
5. End with a "KB gaps" section listing questions you could NOT answer from the KB.
```

## Expected Output

- A FAQ document (questions + cited, confidence-tagged answers) sized to the audience's depth.
- Inline `[kb: …]` citations on every answer.
- A trailing "KB gaps" list of unanswerable questions to drive the next `/kb-ingest`.
- No fabricated answers and no unsubstantiated health claims.
