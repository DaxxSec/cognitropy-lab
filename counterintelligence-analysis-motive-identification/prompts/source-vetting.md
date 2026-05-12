# Prompt — Source Vetting Checklist

> A reusable scaffold for assessing the reliability of a human or document source whose information is feeding the indicator base.

## When to Use
- New source enters the indicator base — anonymous tip, walk-in volunteer, peer referral, former associate of subject, paid informant
- Reliability rating is unknown, stale, or contested
- The motive profile leans heavily on a single source — that source's vetting becomes load-bearing
- Periodic re-vetting of long-standing sources

## The Twin-Axis Framework

A source is rated on two independent axes (Admiralty Code):

**Source reliability (the source's track record):**
| Code | Meaning |
|---|---|
| A | Completely reliable — historic record of accurate reporting, no known motive to deceive |
| B | Usually reliable — minor issues in past, but most reports validated |
| C | Fairly reliable — mixed track record, sufficient validation history |
| D | Not usually reliable — repeated issues with accuracy or candor |
| E | Unreliable — known to fabricate or distort |
| F | Reliability cannot be judged — new or untested source |

**Information credibility (this specific report):**
| Code | Meaning |
|---|---|
| 1 | Confirmed by other independent sources |
| 2 | Probably true — consistent with other information |
| 3 | Possibly true — neither confirmed nor contradicted |
| 4 | Doubtful — inconsistent with other information |
| 5 | Improbable — contradicted by other reliable information |
| 6 | Truth cannot be judged — insufficient corroboration |

Rate **each indicator** with both codes, e.g., a B-2 indicator. The motive profile aggregates source quality across the indicator base.

## Vetting Checklist for a New Source

### 1. Identification
- Source identifier (case-internal, not real name)
- Source category (single-source human, validated informant, paid asset, anonymous tip, peer referral, automated system)
- Source's relationship to the subject

### 2. Motive Inventory (yes — even sources have motives)
A source is itself subject to motive analysis. Walk:
- **Money:** is the source paid? On contingency?
- **Ideology:** does the source have a political/religious agenda toward the subject?
- **Compromise:** is the source under any duress?
- **Ego:** does the source benefit reputationally from a particular outcome?
- **Revenge:** does the source have a documentable grievance with the subject? **This is the most common reason informant reports overstate adverse indicators.**

Document each.

### 3. Track Record
- How many prior reports has this source provided? On what subjects?
- Of prior reports, what fraction were corroborated? Refuted? Inconclusive?
- Has the source ever been caught fabricating?
- Are there gaps in the record (long absences, refusals to report)?

### 4. Access Verification
- Does the source have plausible access to the information they're reporting?
- Is the access lawful and within expected scope?
- Could the source be reporting hearsay rather than direct observation? Probe for direct vs. indirect knowledge per indicator.

### 5. Candor Indicators
- Has the source volunteered information that is *against* their interest? (Counter-motive evidence — strengthens reliability)
- Has the source ever refused to embellish when given the opportunity?
- Has the source ever recanted or revised? Under what circumstance?

### 6. Independence Check
- Is this source repeating information they obtained from another source? (Reduces independence — a chain of single sources is not corroboration)
- Could two ostensibly independent sources have a common upstream origin?

### 7. Operational Considerations
- What is the source-protection regime?
- What disclosure controls apply if this finding is shared?
- Does the source's identity need to be withheld even from peer reviewers within the analytic chain?

## Output Format

```markdown
# Source Vetting — Source [internal-ref] — [date]

## Identification
- Internal ref: ...
- Category: ...
- Relationship to subject: ...

## Motive Inventory
- Money: [...]
- Ideology: [...]
- Compromise: [...]
- Ego: [...]
- Revenge: [...]

## Track Record
- Prior reports: [count]
- Corroborated: [...] | Refuted: [...] | Inconclusive: [...]
- Notable history: [...]

## Access Verification
- Plausible access: [yes/partial/no]
- Direct vs. indirect: [breakdown]

## Candor Indicators
- Counter-motive disclosures: [...]
- Recantations: [...]

## Independence Check
- Upstream sources: [...]
- Independence rating: [strong / moderate / suspect]

## Reliability Rating
- Source reliability (Admiralty Code): [...]
- Justification: [...]

## Caveats for Use
- This source's information must be corroborated by [domain / source type] before being elevated to "corroborated indicator"
- Do not cite this source by identifier in any analytic product
- ...
```

## Cautions
- A new source defaults to **F** (cannot be judged) until enough track record exists. F-rated single-source information is not a basis for a motive finding.
- A grievance-driven source may produce factually accurate reporting *and* be unreliable — accuracy and reliability are not the same axis. Probe both.
- Do not assign reliability based on the source's social position or institutional affiliation. A senior official can be an unreliable source; a low-status informant can be a reliable one.
- Re-vet long-standing sources periodically. Reliability decays.
