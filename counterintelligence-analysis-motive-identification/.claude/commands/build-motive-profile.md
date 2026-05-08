# /build-motive-profile — Map Indicators onto MICE-RC

Map the populated indicator checklist onto the six-category MICE-RC framework with weighted evidence. Produce a draft motive profile that distinguishes corroborated motive hypotheses from indicator patterns of concern from null findings.

## Inputs
- Populated indicator checklist (`outputs/<date>-indicator-checklist.md`)
- Domain-knowledge reference (`context/for-agent/domain-knowledge.md`)
- Constraints file (`context/constraints.md`)

## Steps

### 1. Pre-condition Check
- Indicator checklist is at least 70% populated
- At least one indicator has a timestamp
- Sources are documented for every indicator
- Gaps inventory exists

If any pre-condition fails, return to `/indicator-checklist`.

### 2. Per-Category Indicator Mapping
For each MICE-RC category, list the corroborated indicators consistent with that motive:

- **M — Money**
- **I — Ideology**
- **C — Compromise** (subject's exploitable behavior)
- **E — Ego / Excitement**
- **R — Revenge**
- **C — Coercion** (active duress by hostile service)

An indicator may map to more than one category. Note shared indicators explicitly.

### 3. Weight Each Indicator-to-Motive Mapping
For each (indicator, motive) pair, score:

| Dimension | Scale |
|---|---|
| Source reliability | A (highest) → F (cannot be judged) |
| Information credibility | 1 (confirmed by independent source) → 6 (cannot be judged) |
| Specificity to this motive | High / Medium / Low (does the indicator point uniquely to this motive, or could it support several?) |
| Recency | <12mo / 12-36mo / >36mo |

### 4. Domain Coverage Check
A motive hypothesis requires corroboration across at least two domains. For each candidate motive, list which domains contributed corroborated indicators. Flag any motive supported by only one domain as **"indicator pattern of concern, not motive finding."**

### 5. Null Hypothesis Construction
Construct the null hypothesis explicitly: *"The indicator pattern is consistent with normal life events for someone in this subject's role and circumstance."* For each indicator cluster, articulate the most plausible benign explanation. The null is a real hypothesis, not a rhetorical formality — many cases close on the null.

### 6. Initial Confidence Assessment
For the leading hypothesis (and any close alternative), rate initial confidence using ICD 203 lexicon:
- Probability: almost certainly / highly likely / likely / roughly even / unlikely / highly unlikely / almost no chance
- Confidence in the assessment (separate from probability): high / moderate / low — driven by source reliability, corroboration density, recency

Record what would *change* the confidence: which gap, if closed, would move the assessment up or down.

### 7. Draft Motive Profile
Write `outputs/<date>-motive-profile-draft.md`:

```markdown
# Motive Profile Draft — Subject [case-internal-ref] — [date]

## Inspection Basis
- Indicator checklist version: [filename]
- Domains populated: [list]
- Source reliability summary: [A-1 count, B-2 count, etc.]

## MICE-RC Mapping
### Money
- Corroborating indicators: [list with source refs]
- Domain coverage: [list domains]
- Initial weight: [low / medium / high / dominant / not present]

### Ideology
... (same structure for each MICE-RC letter)

## Null Hypothesis
- Articulation: [the most plausible benign explanation]
- Indicators consistent with null: [list]

## Leading Hypothesis (if any)
- Hypothesis: [name + one-sentence framing]
- Probability (ICD 203 lexicon): [...]
- Confidence: [...]
- Drivers of confidence: [...]
- Indicator pattern: [domain coverage and key items]

## Close Alternatives
- [list with summary]

## Gaps That Would Change the Assessment
- [list with the specific source-acquisition step needed]

## Status
- Draft / Ready for timeline / Ready for ACH / Ready for peer review
```

### 8. Log
Append session entry to `work-log/session-log.md` with date, profile version, hypotheses identified, gaps that would change confidence.

## Decision Points
- If two MICE-RC categories are tied with comparable weighting, **do not collapse**. Mixed-motive profiles are common (Money + Ego in Hanssen, Money + Compromise in many cases) and informative.
- If the null is competitive with the leading hostile motive, the finding is "no actionable motive identified" — that is a valid, valuable output.
- If a motive lacks domain coverage, do not advance it to the finding stage. Either close the gap or downgrade the language.
- Never write a motive hypothesis that the populated checklist cannot support. The checklist is the floor; assertions above it are speculation.
