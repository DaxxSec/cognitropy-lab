# 5-Domain Indicator Taxonomy

> Canonical reference taxonomy for the 5-domain inspection checklist. Adapted from DCSA Insider Threat Indicator guidance, DoD CI doctrine, and the unclassified PERSEREC case literature. Use as the structured inspection list for `/indicator-checklist`.

## How to Read This Taxonomy

Each item is phrased as an *observation*, not a *judgment*. Indicators are flags for inquiry, never accusations. Each domain section ends with a **false-positive alternatives** subsection naming the most common benign explanations the analyst must rule in or out before scoring an item as a corroborated indicator.

Each item has a stable identifier (e.g., `F-01`) used in checklist output for traceability.

## Domain 1 — Financial

### Acute pressure indicators
- `F-01` Sudden unexplained personal debt accumulation (multi-account, short window)
- `F-02` Garnishment, bankruptcy filing, or active collections
- `F-03` Reported gambling, addiction, or other compulsive expenditure
- `F-04` Major medical, eldercare, or family-emergency expense exceeding emergency reserves
- `F-05` Investment losses concentrated in time
- `F-06` Identity-theft event creating financial pressure

### Acute affluence indicators
- `F-07` Sudden unexplained large purchases (vehicle, property, luxury) inconsistent with income
- `F-08` Frequent unexplained travel (volume or destination inconsistent with means)
- `F-09` Repayment of long-standing debts in lump sum without documented source
- `F-10` Cash deposits or transactions just below reporting thresholds (structuring)

### Concealment indicators
- `F-11` Foreign bank accounts or holdings not reported on SF-86 / OF-306 / equivalent
- `F-12` Cash flows that bypass normal financial channels
- `F-13` Use of family members' accounts for personal transactions
- `F-14` Income that does not appear on tax filings

### False-positive alternatives (must rule in or out)
- Inheritance from a documented estate
- Divorce settlement
- Legitimate side business with documentable income (sole proprietorship, consulting)
- Mid-career compensation jumps with documented employment record
- Family medical event with insurance claim trail
- Cryptocurrency holdings (legitimate but harder to baseline)

## Domain 2 — Foreign Contacts

### Disclosed contacts
*Note: properly disclosed contacts are not adverse indicators. Disclosure is what the subject was supposed to do. The rest of this section is about UNDISCLOSED or anomalous contacts.*

### Undisclosed close-and-continuing contact indicators
- `FC-01` Unreported close-and-continuing contact with non-US persons (or analogous in other jurisdictions)
- `FC-02` Contact via channels suggesting concealment (ephemeral messaging, dead-drop, third-country meet-up)
- `FC-03` Contact pattern with documentable hostile-service ties (where independently established)
- `FC-04` Family members in countries with documented coercive practice toward diaspora, not previously declared

### Travel indicators
- `FC-05` Travel to countries of CI concern with stated purpose inconsistent with itinerary
- `FC-06` Anomalous travel duration, frequency, or routing
- `FC-07` Travel without notification when notification is required
- `FC-08` Travel with restricted-communications profile (subject hard to reach, deviates from expected timeline)
- `FC-09` Repeat-visit pattern to single foreign location with no clear declared purpose

### Communication indicators
- `FC-10` Communication patterns inconsistent with stated foreign-contact relationships
- `FC-11` Encrypted communications with foreign nationals not declared
- `FC-12` Unusual third-party contact patterns (intermediaries, cut-outs)

### False-positive alternatives
- Legitimate family relationships (the family connection is itself never an indicator; the *contact behavior* is)
- Academic collaboration with declared partners
- Legitimate business travel with employer authorization
- Journalism or research activity within authorized scope
- Unfamiliar communication apps adopted for ordinary reasons

### Critical exclusion
National origin, ethnicity, or religion alone is **not** an indicator. The bar is *contact behavior* that is undisclosed, anomalous, or inconsistent with declared purpose.

## Domain 3 — Lifestyle

### Stress and life-event indicators
- `L-01` Recent divorce, separation, or marital crisis
- `L-02` Recent bereavement of close family member
- `L-03` Recent legal trouble (criminal charge, civil suit, custody dispute)
- `L-04` Recent significant health diagnosis affecting subject or close family
- `L-05` Recent geographic relocation under stress
- `L-06` Recent loss of housing or housing instability

### Behavioral-change indicators
- `L-07` Sudden change in social associates (new associations, dropped associations)
- `L-08` Personality or affect change observed by colleagues
- `L-09` Substance use compromising judgment, work performance, or driving record
- `L-10` Sudden secrecy about life outside work
- `L-11` Pattern of expressing extreme dissatisfaction with role, organization, or country

### Vulnerability indicators
- `L-12` Subject describing self as isolated or without support network
- `L-13` Subject expressing financial fear inconsistent with apparent finances
- `L-14` Subject volunteering exploitable information unprompted (sometimes signals self-recruitment readiness or trust-test in development)

### False-positive alternatives
- Any normal life event (divorce, illness, bereavement, relocation) without other corroborating domain indicators is **not** a CI indicator. It is a stressor.
- Personality change attributable to identifiable cause (medication, recent trauma) is not adverse.
- Social associations within the subject's known communities (church, club, family) are not adverse.
- Mental-health treatment is not adverse and is statutorily protected; do not score as indicator.

### Critical caution
This domain has the highest false-positive rate. Apply false-positive notes generously. Lifestyle indicators are most useful in correlation with other domains, not standalone.

## Domain 4 — Ideological

### Documentable hostility indicators
- `I-01` Statements expressing alignment with a hostile state's stated grievance, contemporaneously and attributably
- `I-02` Active and durable hostility toward the employer's mission expressed in actionable form (not opinion)
- `I-03` Affiliation with extremist organizations whose ideology endorses targeted action
- `I-04` Pattern of normalizing leak / unauthorized-disclosure as ethical
- `I-05` Romanticization of historical figures associated with espionage or extremism

### Behavioral concomitants
- `I-06` Seeking compartmented information beyond role with ideological framing
- `I-07` Pattern of confrontational political behavior at work that disrupts mission
- `I-08` Statements aligning with foreign cause as primary identity marker (where corroborated)

### False-positive alternatives — important
- Ordinary political disagreement is **not** an indicator
- Criticism of specific policy is **not** an indicator
- First-Amendment-protected expression is **not** an indicator
- Religion, ethnicity, or national origin is **not** an indicator
- Whistleblower-protected disclosure is **not** an indicator and is statutorily protected

### Critical exclusion
Ideological indicators are the most prone to mishandling. The bar is **documentable, durable, action-oriented hostility** expressed in **attributable** form. Hearsay and rumor do not meet the bar. The motive profile must explicitly note the false-positive analysis for any I-01 through I-08 item.

## Domain 5 — Technical / Access

### Anomalous access indicators
- `T-01` Access to information outside need-to-know with no operational justification
- `T-02` Off-hours access patterns inconsistent with role and not previously baseline-normal
- `T-03` Access to compartments or systems the subject is not assigned to (where audit shows successful access)
- `T-04` Repeated access denials for systems the subject is not assigned to (subject is probing)

### Anomalous transfer indicators
- `T-05` Unusual download volumes (bytes, file count) compared to role baseline
- `T-06` USB / removable-media activity inconsistent with role
- `T-07` Cloud-sync to unsanctioned services
- `T-08` Print volume anomalies, particularly of compartmented documents
- `T-09` Email forwarding to personal accounts of work product

### Security-control indicators
- `T-10` Personal devices in compartmented spaces
- `T-11` Probing of security controls beyond role-appropriate
- `T-12` Tampering with audit-logging or DLP controls
- `T-13` Use of cover or pretext to obtain access

### Behavioral concomitants
- `T-14` Working unusual hours without management awareness or operational basis
- `T-15` Reluctance to take leave (a long-recognized indicator with empirical support)
- `T-16` Insistence on working alone or rejecting collaborative oversight

### False-positive alternatives
- Legitimate research within authorized scope
- Training programs that involve cross-system access
- Transitional projects (subject moving between roles, with documented authorization)
- Genuine system failure causing apparent anomaly
- Personal-device-in-classified-space caused by procedural error rather than intent
- Refusal of leave can have benign explanations (financial inability to take unpaid leave, project completion ethic)

### Cross-correlation
Technical / access indicators are the most directly observable and most directly attributable to the subject. They are also the most easily explained by benign causes. Rule of thumb: a single technical/access anomaly is benign until corroborated; a *pattern* of anomalies, particularly correlated with stressors or external events from other domains, is the canonical indicator.

## Aggregation Rules (recap)

A motive finding requires:

1. Indicators in **at least two domains**, corroborated.
2. **At least one timestamped** indicator.
3. **Documented sources** for every indicator.
4. Survival under **ACH** against the null hypothesis.
5. **Civil-liberties review** passed.

A hypothesis falling short of these is "indicator pattern of concern" warranting further inquiry, not a motive finding.
