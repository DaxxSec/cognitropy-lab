# contradiction-adjudication-memo

## Purpose

Resolve a single `CONFLICT` block from a fusion brief and emit the canonical adjudication memo. Use this prompt directly when running `/contradiction-resolve` to ensure all five required sections are populated.

## Prompt Template

```
I need to adjudicate a contradiction surfaced in the fusion brief at [BRIEF_PATH].

- **Conflict topic:** [ONE_LINE_TOPIC, e.g. "400 vs 422 for malformed filter parameter on GET /v3/orders"]
- **Position A:** [WHAT_SOURCE(S)_SAID, e.g. "Internal corpus uses 400 across 14 operations (rating B2)"]
- **Position B:** [WHAT_OTHER_SOURCE(S)_SAID, e.g. "RFC 4918 §11.2 and Stripe peer spec use 422 for valid-syntax-invalid-semantics (rating A1 + B2)"]
- **Adjudication owner:** [NAME_OR_ROLE]
- **Known overrides in play:** [SECURITY_VETO | TIER_1_CUSTOMER_TICKET | NONE]

Please:
1. Restate the conflict in one paragraph.
2. Tabulate the positions with their supporting sources and combined ratings.
3. Apply the default source ordering from `context/concepts.md`; note where this case diverges.
4. Decide; state the rationale in one sentence.
5. Document the rejected alternative in 2-3 sentences (why it was attractive, what specifically caused it to lose).
6. Write the result to `outputs/adjudication/[DATE]-[TOPIC_SLUG].md` with STATUS: RESOLVED.
7. Update the source fusion brief to replace the CONFLICT line with a RESOLVED line linking the new memo.
```

## Expected Output

- `outputs/adjudication/[DATE]-[TOPIC_SLUG].md` with all five required sections (`Conflict`, `Positions`, `Default ordering & overrides`, `Decision`, `Rejected alternative considered`) and a `STATUS:` header.
- An in-place edit of the originating fusion brief replacing the CONFLICT line.
- Explicit flag if source-poisoning is suspected (e.g. a stakeholder filed tickets that conveniently support their position).
