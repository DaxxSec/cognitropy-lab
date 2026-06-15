# Gap Prioritization

## Purpose

Triage a raw knowledge-gap backlog into a ranked work plan by impact and tractability, so the next sweep and the next research effort go where they pay off most. Use after `/gap-scan` produces an unordered list of dark bands, unknowns, stale entries, and OPEN questions.

## Prompt Template

```
You are planning the next cycle of work for the RF spectrum knowledge base. Prioritize this gap backlog.

Gaps:
- [dark band: 700-720 MHz, no entries]
- [unidentified emitter: 433.92 MHz bursty]
- [stale entry: kb:1090000-adsb past review_by]
- [OPEN question: "what's the LoRa channel plan here?"]
- ...

Context:
- **Coverage mandate:** [which bands/regions this KB must cover]
- **Available effort:** [e.g. one 2-hour sweep session + research time]
- **Constraints / safety / legal priorities:** [e.g. must keep aeronautical band current]

Please:
1. Classify each gap (dark band / unidentified / stale / OPEN question / contradiction).
2. Score each on impact (how often it comes up + safety/legal weight) and tractability (how cheaply one capture or lookup closes it), 1-5 each.
3. Rank by impact x tractability; call out quick wins vs. deep investigations.
4. Translate the top dark-band/unknown gaps into concrete priority frequencies for the next `/kb-ingest-sweep`.
```

## Expected Output

- A scored, ranked backlog table (gap, type, impact, tractability, score, action)
- A "do first" shortlist separating quick wins from deeper investigations
- A priority-frequency list ready to drive the next sweep
