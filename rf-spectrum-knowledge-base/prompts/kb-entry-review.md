# KB Entry Review

## Purpose

Peer-review a proposed or updated KB entry before it becomes canonical — checking schema compliance, citation integrity, confidence honesty, and contradictions with existing entries. Use as the gate inside `/emitter-entry-author` or `/kb-audit`.

## Prompt Template

```
You are reviewing a candidate KB entry for the RF spectrum knowledge base. Be a skeptical reviewer: the goal is to catch an unsupported claim before it's published.

Proposed entry:
[paste the entry / draft]

Neighbouring entries (overlapping frequency or service):
[paste any related entries, or "none provided"]

Please:
1. Schema check — list any missing/malformed required fields (per context/references.md), including ordered frequencies and non-empty provenance.
2. Citation check — does every claim above `unidentified` have a citation? Flag any `confirmed` with no decode/signature evidence.
3. Confidence honesty — does the confidence language match the actual evidence? Downgrade if not.
4. Contradiction check — does this entry conflict with any neighbour's service/identity/region? Flag overlaps.
5. Verdict: APPROVE / REVISE (with the specific edits) / REJECT (with reason).
```

## Expected Output

- A field-by-field schema defect list (or "schema OK")
- Citation and confidence findings, with any required downgrades
- Contradiction flags against neighbouring entries
- A clear APPROVE / REVISE / REJECT verdict with actionable edits
