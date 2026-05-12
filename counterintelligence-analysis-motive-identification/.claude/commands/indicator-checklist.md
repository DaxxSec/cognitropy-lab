# /indicator-checklist — Run the 5-Domain Standardized Inspection Checklist

Apply the canonical 5-domain inspection checklist (`resources/indicator-taxonomy.md`) against a packet of source material. Produce a populated checklist with every observation traceable to its source. This is the load-bearing instrument of the workspace.

## Inputs
- Source packet (path or description)
- Date of inspection
- Inspector identity (analyst billet)
- Existing prior checklist for this subject (if iterating)

## Steps

### 1. Predication Re-confirmation
Re-confirm the analyst is operating within the authority captured at onboarding. If the source packet falls outside that scope (e.g., it includes material on a different subject), stop and ask whether that material is in scope.

### 2. Source Inventory
For every document in the packet, record:
- Document type (SF-86, OF-306, foreign-contact report, polygraph report, DLP export, badge log extract, supervisor referral, OSINT memo, etc.)
- Originating agency or system
- Date of information
- Date received
- Classification
- Reliability (A–F per Admiralty Code), Credibility (1–6)

Save the inventory as the header of `outputs/<date>-indicator-checklist.md`.

### 3. Domain 1 — Financial
Walk every Financial-domain item from `resources/indicator-taxonomy.md` §1. For each, mark one of:
- **No indicator** — examined, nothing in source material relevant
- **Possible indicator (uncorroborated)** — observation present, single source, requires further inquiry
- **Indicator (corroborated)** — observation present, corroborated across two or more sources OR by an A-1 source
- **Unexamined** — domain item could not be examined due to source absence

For each indicator, record: source citation, date of information, false-positive alternatives considered, recency (within 12 months / 12-36 months / older).

### 4. Domain 2 — Foreign Contacts
Same procedure, §2. **Critical reminders:**
- Reject items that rest only on national origin or religious/ethnic identity without independent contact behavior
- Distinguish reported and properly disclosed contacts (not adverse) from unreported close-and-continuing contact (potentially adverse)
- Travel patterns require corroborating context, not bare itinerary

### 5. Domain 3 — Lifestyle
Same procedure, §3. **Critical reminders:**
- This domain has the highest false-positive rate
- Apply false-positive notes generously — divorce, bereavement, financial shock, illness, relocation are normal life events, not indicators in themselves
- Lifestyle indicators are most useful in correlation with other domains, not standalone

### 6. Domain 4 — Ideological
Same procedure, §4. **Critical reminders:**
- Bar is documentable hostility expressed in actionable form, not opinion
- First-Amendment-protected expression alone is not an indicator
- Whistleblower-protected disclosures are explicitly excluded
- Statements must be contemporaneous and attributable; rumor or hearsay is not an indicator

### 7. Domain 5 — Technical / Access
Same procedure, §5. Cross-reference against any DLP, UEBA, badge, printer, or audit-log access the analyst has within authority.
- Access outside need-to-know without operational justification
- Anomalous download or USB activity
- Off-hours access patterns inconsistent with role
- Personal-device-in-compartmented-space incidents
- Probing of security controls beyond role-appropriate

### 8. Cross-Domain Pre-Check
Before saving, scan the populated checklist for cross-domain corroboration. Note explicitly any indicator pattern that already shows up in two or more domains — that is the seed of the motive profile.

### 9. Gap Inventory
List every checklist item marked **Unexamined**. These are not "no indicator" — they are work that has not yet been done. Note the source acquisition step needed to close each gap (and whether the analyst is authorized to take it).

### 10. Save and Log
- Save populated checklist to `outputs/<date>-indicator-checklist.md`
- Append session entry to `work-log/session-log.md`: date, source set examined, items examined, gaps identified, time spent
- Update `planning/plan.md` with revised next-step list

## Output Format

```markdown
# Indicator Checklist — Subject [case-internal-ref] — [date]

## Source Inventory
| Doc | Type | Origin | Date of Info | Date Received | Classification | Reliability | Credibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... |

## Domain 1 — Financial
| Item | Status | Source | Date | False-positive considered | Recency | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... |

## Domain 2 — Foreign Contacts
... (same structure)

## Domain 3 — Lifestyle
... (same structure)

## Domain 4 — Ideological
... (same structure)

## Domain 5 — Technical / Access
... (same structure)

## Cross-Domain Pre-Check
- ... patterns observed across two or more domains

## Gap Inventory
- ... unexamined items and source-acquisition steps needed
```

## Decision Points
- If technical/access shows indicators of *active* compromise (data exfiltration in progress, ongoing unauthorized contact), pause analytic work and notify operational chain — analytic outputs do not delay operational response.
- If the checklist is <50% populated due to source gaps, do not proceed to motive profiling. Acquire more sources first.
- Iterate. The first checklist run is rarely the last; treat it as a versioned artifact with revision history.
