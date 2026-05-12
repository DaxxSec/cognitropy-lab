# /recruit-vector-assessment — Evaluate Probable Recruitment Vectors

Where the indicator pattern suggests external influence (foreign contact, unexplained communication, external pressure markers), evaluate the probable recruitment vector against hostile-service tradecraft using the RASCLS framework. This command is **only run when those external indicators are present**; if the indicator pattern is purely internal (e.g., self-initiated insider compromise driven by Revenge), skip this step.

## Inputs
- Populated indicator checklist (foreign-contact and/or technical-domain items present)
- Motive profile draft
- Timeline (if `/timeline-correlate` has been run)
- Domain knowledge (`context/for-agent/domain-knowledge.md` — RASCLS section)

## Steps

### 1. Pre-condition
At least one of:
- Foreign-contact indicators (corroborated, not single-source)
- External communication patterns inconsistent with declared activity
- External pressure markers (financial flows from external sources, evidence of coercion)

If none, the recruit-vector frame is not applicable. Document that conclusion and proceed to peer-review.

### 2. Contact-Pattern Reconstruction
For each foreign or external contact relationship in the indicator base, record:
- Contact name (or pseudonym; preserve source-protection conventions)
- Affiliation (if known) — note that affiliation alone is not attribution
- First contact date
- Subsequent contact frequency
- Channel(s) — in-person, phone, encrypted messaging, email, social, dead-drop, etc.
- Initiation pattern — who initiates each contact?
- Topics discussed — declared and observed
- Asks made of the subject, declared and observed
- Subject's response pattern

### 3. RASCLS Pattern Match
Walk the contact pattern against each RASCLS principle:

| Principle | Indicator |
|---|---|
| **R — Reciprocation** | Gifts, hospitality, favors that obligate the subject; meals, travel, professional opportunities |
| **A — Authority** | Status difference between contact and subject (academic, governmental, social) leveraged in interactions |
| **S — Scarcity** | Framing the subject's information or access as uniquely needed; "only you can provide this" |
| **C — Commitment & Consistency** | Small disclosures by the subject that are then leveraged into larger ones; escalation pattern |
| **L — Liking** | Personal rapport, manufactured friendship, shared identity emphasis |
| **S — Social Proof** | "Others in your position already cooperate"; introduction to other "cooperators" |

Mark each principle: **Present (corroborated) / Possibly present / Not observed**.

### 4. Vector Type Classification
Based on the RASCLS pattern, classify the vector type:

- **Volunteer (walk-in)** — Subject initiates contact unprompted. Often ideologically motivated; RASCLS pattern is minimal because the recruitment was not externally driven.
- **Cold approach** — Hostile service approaches without prior cultivation. Heavy use of A and S in early contact.
- **Cultivated recruit** — Long-cycle development relationship (months to years). Heavy use of R, L, C&C; S deployed late.
- **Coerced** — Active duress (kidnapping, sextortion, threat to family). May show no positive RASCLS pattern; instead shows fear-driven compliance markers.
- **Unwitting** — Subject does not realize the recipient of their information is hostile-aligned. Pattern shows S and L, with no acknowledgment of recipient's affiliation by the subject.
- **Internal (no external recruiter)** — All indicators point to subject acting alone, motivated internally. RASCLS pattern is absent. (This can apply when the foreign-contact indicators turn out to be unrelated coincidence.)

### 5. Service-Attribution Caution
Tradecraft fit suggests **how** a recruitment would unfold, not which service is behind it. Resist naming a specific service from contact pattern alone. If service attribution is being made elsewhere in the case (operational reporting, technical attribution from communications), reference that attribution as a separate input — do not produce service attribution from the analytic motive workspace.

### 6. Vector Assessment Output
Write `outputs/<date>-recruit-vector.md`:

```markdown
# Recruit-Vector Assessment — Subject [ref] — [date]

## Contact-Pattern Summary
- Contacts examined: [count]
- Contact-relationship duration: [from–to]
- Channels observed: [list]

## RASCLS Pattern Match
| Principle | Status | Indicators |
|---|---|---|
| R — Reciprocation | Present / Possible / Not observed | ... |
| A — Authority | ... | ... |
| ... |

## Vector Type
- Classification: [vector type]
- Confidence: [ICD 203 lexicon] — [justification]
- Indicators consistent with this vector: ...
- Indicators inconsistent with this vector: ...

## Alternative Vector Hypotheses
- [vector] — could explain ... but inconsistent with ...
- [vector] — could explain ... but inconsistent with ...

## Service-Attribution Note
- The vector type **does not** attribute to a specific service. Attribution, if needed, must rest on independent evidence (operational, technical) outside this analytic frame.
```

### 7. Append to Motive Profile
Add a `## Recruit-Vector` section to the motive profile draft summarizing the vector type and how it shapes the motive interpretation. Example: a *cultivated* recruit pattern alongside Money + Compromise indicators tells a different story than a *volunteer* pattern alongside Ideology indicators.

### 8. Log
Append session entry to `work-log/session-log.md`.

## Decision Points
- If RASCLS pattern is absent and foreign-contact indicators are isolated, the vector is most plausibly **internal or coincidental** — and that should be the finding, not a thinly stretched recruitment hypothesis.
- If the contact pattern shows clear recruitment tradecraft but the subject does not appear to be cooperating, the case is potentially "**target of attempt, not recruited**" — that is critical for protective response, not adverse adjudication.
- If coercion indicators are present, the operational response shifts from adjudication to extraction. Pause the analytic chain and notify operational leadership.
