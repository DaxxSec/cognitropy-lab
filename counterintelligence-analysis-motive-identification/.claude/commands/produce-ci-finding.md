# /produce-ci-finding — Generate the Final CI Motive Finding

Package the peer-reviewed motive assessment as an ICD 203-compliant finding ready for the cognizant CI office, insider-threat hub, security adjudicator, or HR/legal recipient. This is the final step in the analytic chain. Run only after `/peer-review-checklist` has produced a passed sign-off block.

## Inputs
- Motive profile (peer-reviewed, sign-off block populated)
- ACH matrix
- Indicator checklist
- Timeline (if produced)
- Recruit-vector assessment (if produced)
- Reporting-chain destination from `context/project.md`

## Steps

### 1. Pre-condition Check
- Peer-review sign-off block populated and all checks Pass
- ACH dominant hypothesis matches profile leading hypothesis
- Civil-liberties and source-protection checks Pass
- Adverse-action framing Pass

If any precondition fails, **stop** and return to `/peer-review-checklist`.

### 2. Audience Calibration
Frame the finding for its destination:

| Destination | Tone | Detail level | Format conventions |
|---|---|---|---|
| Cognizant CI office (operational) | Direct, action-oriented | Full | Agency-standard finding format if known |
| Insider-threat hub | Analytical, comparative | Full | Hub's referral package conventions |
| Security adjudicator | Whole-person framing | Full + adjudicative-guideline mapping | SEAD-4 / 32 CFR §147 guideline references |
| HR / legal counsel | Privacy-aware, neutral | Bounded — only what's necessary | Strip indicator-specifics that aren't action-bearing |
| FBI Field Office (referral) | Predicate-aware | Full | Agency referral conventions |
| Private-sector engagement report | Professional, fact-tight | As contracted | Engagement-letter format |

### 3. Build the Finding
Compose `outputs/<date>-finding.md` using this structure:

```markdown
# Counterintelligence Motive Finding — Subject [case-internal-ref]

**Date of Finding:** [YYYY-MM-DD]
**Analyst:** [billet]
**Reviewer:** [billet, if separate]
**Authority Basis:** [case number / program section / engagement reference]
**Classification:** [as appropriate]
**Distribution:** [recipient list]

## Executive Summary
[3-5 sentences. The motive hypothesis, its probability, the confidence rating, and the recommended next step. No more.]

## Bottom Line Up Front (BLUF)
- Motive Hypothesis: [name]
- Likelihood (ICD 203): [almost certainly / highly likely / likely / roughly even / unlikely / etc.]
- Confidence: [high / moderate / low]
- Recommendation: [further inquiry / referral to cognizant office / case closure / continuous evaluation flag / no action]

## Indicator Base Summary
- Domains examined: [list]
- Indicators corroborated: [count by domain]
- Indicator pattern in plain language: [2-3 sentences]
- Source-quality summary: [Admiralty Code distribution]

## Motive Mapping (MICE-RC)
For each MICE-RC category, state:
- Indicator presence: corroborated / possible / not present
- Domain coverage: which domains contributed
- Weight contribution to overall finding

## Timeline Findings (if applicable)
- Key correlations: [list]
- Reverse-causation considerations: [where unresolved]

## Recruit-Vector Findings (if applicable)
- Vector type: [classification]
- Confidence: [...]
- Service-attribution note: separated from this finding; this finding does not attribute to a specific service.

## Alternative Hypotheses Considered
- [H0 — Null]: [paragraph; consistent indicators; inconsistencies]
- [H_alt-1]: [paragraph]
- [H_alt-2]: [paragraph]
- ACH inconsistency tally summary: [table or list]

## Confidence Drivers
- What raises confidence: [...]
- What lowers confidence: [...]
- What would change the assessment: [specific source acquisition or analytic step needed]

## Civil-Liberties and Source-Protection Statement
- US Persons / equivalent minimization applied: [yes]
- Indicators based on protected-class characteristics: [none / explicit acknowledgment if any retained with corroboration]
- Whistleblower-protected disclosures excluded: [yes]
- Human-source identifiers stripped: [yes]

## Recommendation
[Specific next step. The recommendation is analytic, not adverse-action. Examples:
- "Refer to cognizant CI office for predicate determination"
- "Continue continuous-evaluation monitoring; re-examine in 6 months or upon new indicator"
- "Close indicator pattern as explained by [benign cause]"
- "Refer to security adjudicator for whole-person review under SEAD-4 Guideline [F/B/etc.]"
- "Refer to general counsel; indicator pattern raises a question outside CI competence"
]

## Adverse-Action Disclaimer
This finding is an analytic motive assessment. It does not by itself constitute grounds for any adverse action against the subject. Termination, security-clearance action, law-enforcement referral, and similar actions require the appropriate independent decision-maker acting on their own predicate.

## Appendices (referenced, not embedded if classified)
- A: Populated indicator checklist — `outputs/<date>-indicator-checklist.md`
- B: Timeline — `outputs/<date>-timeline.md`
- C: ACH matrix — `outputs/<date>-ach.md`
- D: Recruit-vector assessment — `outputs/<date>-recruit-vector.md`
```

### 4. Final Quality Gate
Re-read the finding end-to-end. Check that:
- Probability and confidence are stated separately
- Every MICE-RC category is mentioned (even those marked "not present")
- The null hypothesis is taken seriously, not dismissed
- The recommendation is analytic and bounded
- No language reads as accusation rather than assessment

### 5. Distribution Preparation
Mark the finding for distribution per `context/project.md`. Confirm:
- Classification correctly applied
- Distribution list correct
- Format matches recipient's conventions
- Source-protection rules applied

### 6. Log
Append final entry to `work-log/session-log.md`:
- Finding date and version
- Recipient(s)
- Distribution timestamp (after the analyst transmits, not when this command runs — the agent does not transmit)
- Retention disposition reminder

### 7. Post-Finding Hygiene
- Save the case folder structure for retention per `context/for-agent/environment.md`
- Update `planning/plan.md` to reflect case status (open for further inquiry / referred / closed)
- If the case is closed, archive in line with retention policy. The agent reminds; the analyst executes.

## Decision Points
- If during finding composition a new gap or ambiguity is recognized, **do not** paper over it. Return to the relevant command and remediate — better to delay the finding by a session than to publish an unsupported one.
- If the recipient calls for a different format (e.g., agency-specific referral package), restructure into that format but **preserve every analytic element** — the indicator chain, alternatives, confidence drivers, and adverse-action disclaimer are non-negotiable.
- The analyst is the publisher. The agent is the drafter. The transmission step is the analyst's, not the agent's.
