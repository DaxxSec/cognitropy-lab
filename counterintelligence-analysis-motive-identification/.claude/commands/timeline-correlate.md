# /timeline-correlate — Build the Indicator/Life-Event Chronology

Construct a chronologically ordered indicator + life-event timeline to expose causation, stressors, and access-change correlations. The motive profile gains explanatory power once the timeline is in place; without it, indicators are static observations.

## Inputs
- Populated indicator checklist with timestamps
- Motive profile draft
- Source material for life-event reconstruction (employment history, public-record events, polygraph timeline notes if available)

## Steps

### 1. Pre-condition
- At least 3 indicators with timestamps
- Life-event data available (promotion/demotion, marital status changes, financial events, foreign travel, bereavement, geopolitical events affecting the subject's home country or affiliation)

If insufficient timestamps, return to source acquisition. A timeline with only two timestamped events is not informative.

### 2. Event Extraction
Pull every dated indicator from the checklist. Pull every dated life event. Mark each with: date, domain (or life-event category), source, classification, indicator-checklist item ID (if applicable).

### 3. Construct Timeline
Build a markdown table sorted by date:

| Date | Event | Domain / Category | Source | Classification | Notes |
|---|---|---|---|---|---|
| 2025-08-15 | Promotion (TS/SCI compartment X added) | Life-event/access | HR record | U | Sets new access baseline |
| 2025-09-02 | Foreign-contact (relative) reported | Foreign Contacts | SF-86 update | U | Properly disclosed; reported voluntarily |
| 2025-11-04 | Divorce filing | Life-event | Public court record | U | Legal stressor |
| 2026-01-18 | Financial-domain indicator cluster (5 items) | Financial | Credit-monitoring report | U | Significant debt accumulation |
| 2026-02-22 | Off-hours queries outside compartment X scope | Technical/Access | DLP audit | C | Anomalous access |
| 2026-03-09 | Foreign-contact (associate of original relative) appears | Foreign Contacts | OSINT memo | U | Not previously reported |

Add a Mermaid `timeline` diagram for visual review.

### 4. Correlation Pass
Walk the timeline looking for:
- **Stressor → indicator pattern.** Financial event followed by lifestyle change. Divorce followed by foreign-contact pattern. Bereavement followed by access anomaly.
- **Access-change → indicator pattern.** New clearance followed by behavioral shift. Position change followed by access anomaly.
- **External-event → indicator pattern.** Geopolitical event affecting subject's home country followed by ideological-domain indicator.
- **Cluster patterns.** Indicator density that increases, decreases, or oscillates over time.

For each correlation, name explicitly: "Indicator [X] follows event [Y] by [Z] days, consistent with motive [M]."

### 5. Reverse-Causation Check
For each correlation, ask whether the indicator pattern could be the *cause* of the apparent stressor rather than the result. Examples:
- Subject's gambling caused the divorce, not the other way around
- Subject's access anomaly was already underway before the foreign contact appeared
- Subject's ideological alignment predates the geopolitical event by years

Where reverse causation cannot be ruled out, note explicitly.

### 6. Hypothesis Generation
For each robust correlation, write a causation hypothesis: *"The [event] in [date] precedes the [indicator cluster] of [date range], consistent with [motive] motive activation."*

Keep hypotheses minimal — name only causation patterns supported by ≥2 corroborating events.

### 7. Save Outputs
- `outputs/<date>-timeline.md` — table + Mermaid diagram + correlation paragraphs
- Append a `## Correlation Hypotheses` section to the motive profile draft
- Update `planning/plan.md` with any new gaps revealed by the timeline (e.g., "subject's financial state pre-2025-08 not yet examined")

### 8. Log
Append session entry to `work-log/session-log.md` with date, timeline version, correlations identified.

## Output Format Example (Mermaid)

```
timeline
  title Indicator and Life-Event Chronology — Subject [ref]
  2025-08    : Job role expansion (TS/SCI compartment X added)
  2025-09    : Foreign-contact (relative) reported on SF-86 update
  2025-11    : Divorce filing (open court record)
  2026-01    : Financial indicator cluster — 5 items
  2026-02    : Off-hours queries outside compartment X scope
  2026-03    : Foreign-contact (associate of relative) appears, unreported
```

## Decision Points
- If no causal pattern is identifiable, that is a finding. Report "no causal pattern identified" — do not invent one.
- If the timeline reveals an indicator predates all examined sources (the indicator is "always there"), the motive analysis must extend backward through the subject's record, not just forward.
- Geographic and travel data is privileged context — handle within the constraints file's classification and USPER rules.
