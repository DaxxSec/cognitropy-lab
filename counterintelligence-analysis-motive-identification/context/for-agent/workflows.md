# Core Workflows — Counterintelligence Motive Analysis

> Each workflow is a standardized inspection checklist. The conversational language is for analyst comfort; the steps are fixed and must be completed in order.

## Workflow 1: Indicator Inspection — The 5-Domain Sweep

**Goal:** Take a packet of source material and produce a populated 5-domain indicator checklist with every observation traceable to its source.

### Steps
1. **Predication confirmation.** Confirm the inquiry is within the analyst's authority for this subject. If unclear, halt and refer to counsel.
2. **Source inventory.** List every source document available for this packet. Mark classification, originating agency or system, date of information, date received, and reliability rating (A/B/C/D/E per the legacy NATO source-reliability scale, or equivalent).
3. **Financial domain pass.** Walk every financial-domain checklist item (`resources/indicator-taxonomy.md` §1). For each, mark: *No indicator / Possible indicator (needs corroboration) / Indicator (corroborated)* with the source citation. Note the false-positive alternatives that were considered.
4. **Foreign-contacts domain pass.** Same procedure, §2. Be especially careful here: this is the domain where USPER protections, religion, and national origin most often improperly creep in. Reject items that rest only on national origin without independent contact behavior.
5. **Lifestyle domain pass.** Same procedure, §3. This domain has the highest false-positive rate. Apply the false-positive notes generously.
6. **Ideological domain pass.** Same procedure, §4. The bar is documentable hostility expressed in actionable form, not opinion. Reject items that rest on First-Amendment-protected expression alone.
7. **Technical/access domain pass.** Same procedure, §5. Cross-reference DLP, badge, and audit logs where available within authority.
8. **Gap inventory.** List checklist items that could not be examined due to source absence. These are not "no indicator" — they are unexamined. The motive profile must distinguish.
9. **Save populated checklist** to `outputs/<date>-indicator-checklist.md`.
10. **Log to `work-log/`.** Date, source set examined, items examined, gaps identified.

### Decision Points
- If any single indicator is timestamped, log it now in a chronology stub for `/timeline-correlate`.
- If the technical/access domain reveals indicators of active compromise (data exfiltration in progress, ongoing unauthorized contact), pause analytic work and notify operational chain — analytic outputs do not delay operational response.
- If a checklist item requires a step outside analyst authority (subpoena, search, interview), document the step needed and **stop**; do not proceed to motive profiling without examining the gap.

## Workflow 2: Motive Profiling — MICE-RC Mapping

**Goal:** Map the populated indicator checklist onto MICE-RC categories and produce a draft motive profile with weighted evidence.

### Steps
1. **Pre-condition check.** Indicator checklist is at least 70% populated, with timestamps on at least one item, sources documented, gaps inventoried.
2. **Per-category candidate listing.** For each MICE-RC letter (Money, Ideology, Compromise, Ego, Revenge, Coercion), list the corroborated indicators from the checklist that are consistent with that motive category. An indicator may map to more than one category (Money + Compromise often co-occur).
3. **Weighting.** For each indicator-to-motive mapping, score:
   - **Source reliability** (A=highest, E=lowest)
   - **Information credibility** (1=confirmed by independent source, 6=not judged)
   - **Specificity** (does the indicator point uniquely to this motive, or could it point elsewhere?)
   - **Recency** (within 12 months / 12-36 months / older)
4. **Domain coverage check.** A candidate motive needs corroboration across at least two domains. Flag any motive supported by only one domain as "indicator pattern of concern, not motive finding."
5. **Null hypothesis.** Construct the null hypothesis explicitly: "The indicator pattern is consistent with normal life events for someone in this subject's role and circumstance." Articulate the most plausible benign explanations for each cluster.
6. **Draft motive profile.** Write the profile in `outputs/<date>-motive-profile-draft.md`:
   - Subject ID (case-internal, not PII)
   - Inspection date and indicator-set version
   - Per-MICE-RC-category: corroborating indicators, weighting, gaps
   - Null hypothesis articulation
   - Initial confidence assessment, ICD 203 lexicon
   - Items needing further inspection
7. **Log to `work-log/`.**

### Decision Points
- If two motive categories are tied with comparable weighting, do not collapse them — present both. Mixed-motive profiles (Money + Ego, Ideology + Revenge) are common and informative.
- If the null hypothesis is competitive with the leading hostile motive, the finding is "no actionable motive identified" — and that is a valid, valuable output.

## Workflow 3: Timeline Correlation

**Goal:** Build a chronologically ordered indicator + life-event timeline that exposes causation, stressors, and access-change correlations.

### Steps
1. **Pre-condition check.** At least 3 indicators with timestamps; ideally life-event data (promotion, demotion, divorce, bereavement, financial event, foreign travel) is available.
2. **Event extraction.** Pull every dated indicator from the checklist. Pull every dated life event from source material. Mark each with: date, domain, source, classification.
3. **Construct timeline.** A markdown table sorted by date, with columns: Date | Event | Domain | Source | Classification | Notes. Include a Mermaid `gantt` or timeline diagram for visual review.
4. **Correlation pass.** Walk the timeline looking for:
   - **Stressor → indicator pattern:** financial event followed by lifestyle change, divorce followed by foreign-contact pattern
   - **Access-change → indicator pattern:** new clearance followed by behavioral shift, position change followed by access anomaly
   - **External-event → indicator pattern:** geopolitical event affecting subject's home country followed by ideological-domain indicator
   - **Cluster patterns:** indicator density that increases, decreases, or oscillates
5. **Hypothesis generation.** Causation hypotheses are explicitly named: "the divorce in March precedes the financial-domain indicator cluster of April–June, consistent with Money motive activation."
6. **Reverse causation check.** Could the indicator pattern be the cause of the apparent stressor, not the result? (Example: subject's gambling caused divorce, not the other way around.) Note where it cannot be ruled out.
7. **Output.** Save to `outputs/<date>-timeline.md` and append an updated correlation hypothesis section to the motive profile.

### Output Format Example (Mermaid)

```
timeline
  2025-08    : Job role expansion (TS/SCI compartment X added)
  2025-09    : Foreign-contact (relative) reported
  2025-11    : Divorce filing (open court record)
  2026-01    : Financial-domain indicator cluster (5 items)
  2026-02    : Access-domain indicator (off-hours queries outside compartment X scope)
  2026-03    : Foreign-contact (associate of original relative) appears
```

## Workflow 4: Recruit-Vector and Peer-Review

**Goal:** Where indicator pattern suggests external influence, evaluate the probable recruitment vector against hostile-service tradecraft. Then peer-review the entire finding before publication.

### Steps — Recruit-Vector
1. **Pre-condition.** Indicator pattern shows foreign contact, unexplained communication, or external pressure markers. (If not, skip to peer-review.)
2. **Tradecraft fit.** Compare the contact pattern (frequency, escalation, channel, ask-shape) against the RASCLS framework. Identify which RASCLS principles the contact behavior is consistent with.
3. **Service-attribution caution.** Tradecraft fit suggests *how a recruitment would unfold*; it does not attribute to a specific service. Resist the temptation to name a service from contact pattern alone.
4. **Vector assessment.** Output a paragraph naming: probable vector type (volunteer / cold approach / cultivated / coerced), RASCLS principles observed, indicators consistent with each, and confidence rating.
5. **Append to motive profile.**

### Steps — Peer-Review (always required before final finding)
1. **ICD 203 standards check.** Walk every ICD 203 standard (sources rated, confidence characterized, uncertainty explained, intelligence vs. judgment distinguished, argumentation logical, judgments accurate, visuals effective). Score each.
2. **ACH matrix.** Build the Analysis of Competing Hypotheses matrix in `outputs/<date>-ach.md`. List every hypothesis (including null) and every indicator. Rate each cell. Confirm the leading hypothesis is the one with the fewest inconsistencies.
3. **Bias inventory.** Walk the failure-mode table from `domain-knowledge.md` and explicitly state how each potential bias was countered in this analysis.
4. **Civil-liberties check.** Re-walk the constraints file. Confirm no indicator rests on protected-class characteristics alone.
5. **Source-protection check.** Confirm no human source is identifiable from the analytic product.
6. **Adverse-action check.** Confirm the product is framed as analytic, not as a basis for action.
7. **Sign-off.** Analyst initials and date. The product is now ready for `/produce-ci-finding`.

### Decision Points
- If the ACH reveals a tied or near-tied alternative, the finding is "ambiguous motive — multiple hypotheses cannot be discriminated from current source set" and the recommendation is for further inquiry, not a conclusion.
- If any ICD 203 standard cannot be met, the finding is downgraded to "preliminary assessment, not for external dissemination" until the gap is closed.
- If the civil-liberties check fails, the finding is withdrawn entirely; no degraded version is published.

## Failure-Mode Quick Reference

| Symptom | Likely cause | Mitigation |
|---|---|---|
| Motive profile rests on a single indicator | Skipped domain coverage check | Re-run Workflow 1 to find or rule out cross-domain corroboration |
| Timeline shows no correlation | Indicators are actually unrelated | Honest finding: "no causal pattern identified"; report as such |
| Recruit-vector assessment names a specific service | Overreach from tradecraft fit | Walk back to vector-type level only |
| Confidence asserted high with thin sourcing | Confidence-likelihood confusion | Force separation: likelihood ≠ confidence; thin sourcing always lowers confidence |
| ACH dominant hypothesis is null | Indicator pattern is not motive-bearing | Valid output. Close case with appropriate report. |
