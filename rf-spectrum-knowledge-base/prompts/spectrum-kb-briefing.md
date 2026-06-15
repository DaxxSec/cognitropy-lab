# Spectrum KB Briefing

## Purpose

Generate a stakeholder briefing about a band, location, or system drawn entirely from the knowledge base — for a manager, compliance owner, or visiting analyst who needs "what do we know about X" without reading raw entries. Use when someone asks for a summary rather than a single answer.

## Prompt Template

```
You are the RF spectrum knowledge engineer. Produce a briefing on the topic below, grounded ONLY in the knowledge base — cite entries, and clearly separate what's known from what's gap.

Briefing topic:
- **Scope:** [a band (e.g. 868 MHz ISM), a location, or a system]
- **Audience:** [manager / compliance / analyst — sets the depth and jargon level]
- **Question behind the request:** [e.g. "is this band getting more congested?", "are we compliant?"]

Available knowledge: outputs/kb/, outputs/faq.md, context/references.md

Please:
1. Summarize what the KB knows in scope: the key emitters (with signature cards), occupancy, and confidence.
2. Highlight anything notable: new emitters, unallocated activity, drift vs. earlier captures, contradictions.
3. State the gaps honestly — what's unidentified, stale, or uncovered in scope — so the briefing isn't falsely complete.
4. Tailor depth to the audience; lead with the answer to the question behind the request.
5. Cite KB entry ids for every factual claim.
```

## Expected Output

- A scoped briefing (lead answer → key emitters → notable changes → honest gaps), written for the stated audience
- Inline `[kb:...]` citations on every claim
- A short "known vs. gap" boundary so the reader never mistakes silence for coverage
