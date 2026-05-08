# Counterintelligence Motive Identification Workspace

> An agent workspace for authorized counterintelligence analysts, insider-threat program managers, and corporate security investigators to build defensible motive assessments on subjects of interest, using standardized inspection checklists drawn from ICD 700-series doctrine, DCSA insider-threat program guidance, and the MICE-RC analytic framework.

## What This Workspace Does

This workspace converts raw indicator data — financial reporting, foreign-contact disclosures, lifestyle observations, access-pattern logs, ideological statements, polygraph notes — into a structured motive assessment that another analyst could reproduce from the same source set. It does this by enforcing **standardized inspection checklists** at every analytic stage, so that motive findings trace cleanly from observation through framework to confidence rating.

The agent guides you through the full assessment pipeline: open a case under proper authority, run the 5-domain indicator checklist, map indicators onto MICE-RC, build a correlation timeline, evaluate recruitment vectors, peer-review the draft, and produce a final ICD 203-compliant motive finding.

## Why This Workspace Exists

CI motive analysis is an old craft with a checklist-driven core that gets repeatedly reinvented in spreadsheets and tribal knowledge across insider-threat programs. The same six categories of indicators appear in every major espionage case from the Walker ring to Aldrich Ames to recent insider-threat compromises, and the same analytic biases (single-hypothesis tunnel vision, ignoring base rates, conflating indicator with proof) compromise repeated investigations.

This workspace codifies the doctrine that already exists — DoD CI manuals, ICD 203/205 analytic standards, the MICE-RC framework, the DCSA insider-threat indicator taxonomy — into reusable command workflows that produce defensible, peer-reviewable findings. Standardization is not a bureaucratic burden here; it is what makes a CI assessment hold up when it matters most.

## Getting Started

### Prerequisites
- **Authorization to conduct the inquiry.** This workspace presumes you operate inside a properly opened CI investigation, an authorized insider-threat program (DoD 5205.16, EO 13587 derivatives), or a contractual private-sector engagement. Workspace cannot establish authority for you.
- **Source material.** Reportable financial disclosures (SF-86, OF-306), foreign-contact reports, security-incident logs, polygraph reports if applicable, supervisor referrals, badge/access logs, DLP/UEBA outputs.
- **Case management.** Either a sanctioned CI case-management system (CIIS, FBI Sentinel, agency equivalent) or, for unclassified work, a hardened local system you can audit. This workspace is the analytic layer, not the system of record.
- **Classification handling.** Match this workspace's storage classification to the highest source level. Default assumption: unclassified or CUI; treat anything else by exception with the user's classification officer.

### Quick Start
1. Run `/onboard` to capture analyst authority, jurisdiction, classification level, subject category, and reporting chain.
2. Run `/indicator-checklist` once per fresh indicator set; iterate as new material arrives.
3. Run `/build-motive-profile` after the indicator checklist is at least 70% complete.
4. Run `/timeline-correlate` once you have ≥3 timestamped indicators across ≥2 domains.
5. Run `/recruit-vector-assessment` if the indicator pattern suggests external influence or contact.
6. Run `/peer-review-checklist` before treating the finding as analytically mature.
7. Run `/produce-ci-finding` to package the assessment for the cognizant CI office or program leadership.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Capture analyst authority, jurisdiction, classification, subject category, success criteria | First-time setup; re-run when scope changes |
| `/indicator-checklist` | Apply the 5-domain standardized inspection checklist (financial, foreign contacts, lifestyle, ideological, technical/access) | After receiving each new packet of source material |
| `/build-motive-profile` | Map indicators onto the MICE-RC framework with evidence weighting and gap identification | After the indicator checklist is substantially populated |
| `/timeline-correlate` | Construct a chronologically ordered indicator/life-event timeline to expose causation patterns | When ≥3 indicators have timestamps |
| `/recruit-vector-assessment` | Evaluate probable recruitment vectors and hostile-service tradecraft fit | When foreign contact, travel, or external-pressure indicators surface |
| `/peer-review-checklist` | Run the structured analytic peer-review checklist (ICD 203, ACH, alternatives) | Before any motive finding is reported externally |
| `/produce-ci-finding` | Generate the final motive analysis finding with confidence ratings, alternatives, and reporting recommendation | Closing analytic phase |

## Directory Structure

```
counterintelligence-analysis-motive-identification/
├── CLAUDE.md                          # Agent role, instructions, command index
├── README.md                          # This file
├── CREATION_REPORT.md                 # Workspace provenance and design notes
├── context/
│   ├── project.md                     # Subject category, scope, success criteria
│   ├── role.md                        # Analyst authority and clearances
│   ├── constraints.md                 # Civil liberties, classification, jurisdictional limits
│   └── for-agent/
│       ├── domain-knowledge.md        # MICE-RC, RASCLS, indicators, case-study patterns, ICD 203 lexicon
│       ├── workflows.md               # 4 core analytic workflows with decision trees
│       ├── environment.md             # Case-management setup, classification handling, audit logging
│       └── tools.md                   # Recommended structured analytic technique tools
├── .claude/commands/
│   ├── onboard.md                     # Authority and scope intake
│   ├── indicator-checklist.md         # 5-domain indicator inspection
│   ├── build-motive-profile.md        # MICE-RC mapping
│   ├── timeline-correlate.md          # Indicator/event chronology
│   ├── recruit-vector-assessment.md   # External influence analysis
│   ├── peer-review-checklist.md       # Analytic review against ICD 203
│   └── produce-ci-finding.md          # Final finding generation
├── prompts/
│   ├── indicator-elicitation.md       # Templated elicitation from supervisor/source interviews
│   ├── ach-matrix-build.md            # Analysis of Competing Hypotheses scaffold
│   └── source-vetting.md              # Vetting reliability of human and document sources
├── resources/
│   ├── mice-rc-checklist.md           # The MICE-RC inspection checklist (canonical instrument)
│   ├── indicator-taxonomy.md          # 5-domain indicator taxonomy with examples and false-positive notes
│   └── espionage-case-references.md   # Walker, Ames, Hanssen, Pollard, Montes, Hernandez, Manning indicator-pattern references
├── planning/                          # Active investigation plans
├── outputs/                           # Drafts and final findings
├── user-docs/
│   ├── getting-started.md             # Quick-start orientation
│   └── checklist-philosophy.md        # Why standardized checklists, and how not to misuse them
└── work-log/
    └── session-log.md                 # Session log template (one file per analytic session)
```

## Why Standardized Inspection Checklists

CI motive analysis without standardized checklists tends to fail in three predictable ways:

1. **Confirmation bias** — The analyst forms a motive theory early and selectively gathers indicators that confirm it. A standardized checklist forces every domain to be examined, even ones the analyst expects to be empty.
2. **Inconsistent thresholds** — Without checklists, the bar for "concerning indicator" varies by analyst, by week, and by case salience. A documented checklist with explicit elements normalizes the bar across cases and analysts.
3. **Loss of defensibility** — When a finding is challenged in legal review, a counsel can ask "what did you check?" If the answer is "I looked at things," the finding does not survive review. If the answer is a populated checklist with documented sources, the finding has a chance.

This workspace's commands are checklists in disguise. The phrasing is conversational, but the steps are fixed. That is intentional.

## Example Use Cases

### Insider-Threat Program — Anomalous Access Pattern
A DLP system flags repeated after-hours access to compartmented project documents by a cleared employee outside the project. Use this workspace to apply the indicator checklist (technical/access domain), correlate against the financial domain (any sudden life events?), and produce a finding that is either "indicators consistent with hostile intent" with reporting recommendation, or "indicators explained by [legitimate alternative]" with case closure recommendation.

### Polygraph Disclosure — Undisclosed Foreign Contact
A polygraph examination surfaces previously undisclosed travel and contact with relatives in a country of CI concern. Use the foreign-contact and ideological domains, run `/recruit-vector-assessment` against the relevant hostile-service tradecraft profiles, and produce a finding for the cognizant CI office.

### Pre-Adjudication Security Review — Financial Distress
A periodic reinvestigation reveals a sudden cluster of debt indicators against a holder of TS/SCI access. Use the financial and lifestyle domains, build a timeline against access changes, and produce a finding that informs continuous-evaluation reporting and the adjudicator's whole-person decision.

### Corporate Insider-Threat Engagement — Departing Engineer
An engineer at a defense subcontractor with access to ITAR-controlled designs gives notice and begins downloading unusual volumes of internal documentation. Use the technical/access and lifestyle domains, run `/recruit-vector-assessment` against IP-theft tradecraft, and produce a finding that informs HR, legal counsel, and FBI engagement decisions.

### Source Reliability Review — Walk-In Volunteer
A foreign national approaches a US embassy claiming to offer service against their home government. Use the workspace inverted — the *source* is the subject of motive assessment. Apply MICE-RC to the source's offer, run the recruit-vector framework against the host nation's known dangle/double-agent tradecraft, and produce a vetting finding.

## Recommended MCP Servers

- **filesystem** — For reading source packets, writing finding drafts, and managing case folders.
- **sqlite** or **postgres** — For structured indicator storage with audit trails (one row per indicator with source, date, classification, and checklist-item linkage).
- **memory** — For short-term cross-session continuity within a single case (do not use for classified content).

This workspace is hardware-light. The "tools" of the trade are the analytic frameworks, not the integrations.

## Legal & Ethical Considerations

- **Authorization is the first checklist item.** This workspace cannot make an unauthorized inquiry lawful. If you are not operating under a properly opened CI investigation, an authorized insider-threat program, an executive-branch order, or a contractual engagement, stop and consult counsel.
- **US Persons protections.** If the subject is a US Person, EO 12333, the AG Guidelines for FBI Domestic Investigations, and applicable agency procedures apply. USPER information must be minimized in any product.
- **Civil liberties review.** Indicators are flags for inquiry, not predicates for adverse action. No employment action, security clearance action, or law-enforcement referral should be initiated solely from this workspace's output without the appropriate independent review (HR, security adjudicator, prosecutor).
- **Classification handling.** The workspace itself is unclassified. Findings derived from classified sources must be stored, marked, and transmitted at the appropriate level outside this workspace.
- **No surveillance recommendations.** This workspace does not advise on surveillance, recording, or electronic monitoring. Those activities have their own statutory and policy regimes (FISA, Title III, ECPA, GDPR Article 88, etc.).
- **Source protection.** When a finding cites human-source information, source identity is suppressed in the analytic product per source-protection doctrine.
- **Discrimination prohibitions.** Indicators based on protected-class membership (race, religion, national origin, etc.) without independent corroborating behavior are inadmissible. Religion and national origin are particularly fraught categories — see `context/constraints.md`.

## Technical & Doctrinal References

- [Intelligence Community Directive 203 — Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD%20203%20Analytic%20Standards.pdf)
- [Intelligence Community Directive 205 — Analytic Outreach](https://www.dni.gov/files/documents/ICD/ICD%20205.pdf)
- [DoD Directive 5240.06 — Counterintelligence Awareness and Reporting](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodd/524006p.pdf)
- [DoD 5205.16 — Insider Threat Program](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520516p.pdf)
- [DCSA Insider Threat Indicators](https://www.dcsa.mil/Portals/91/Documents/CTP/tools/InsiderThreatIndicators.pdf)
- [Heuer, *Psychology of Intelligence Analysis* (CIA CSI, 1999)](https://www.cia.gov/static/Pyschology-of-Intelligence-Analysis.pdf)
- [Heuer & Pherson, *Structured Analytic Techniques for Intelligence Analysis*, 3rd ed.](https://us.sagepub.com/en-us/nam/structured-analytic-techniques-for-intelligence-analysis/book259773)
- [Burkett, "An Alternative Framework for Agent Recruitment: From MICE to RASCLS"](https://www.cia.gov/resources/csi/studies-in-intelligence/volume-57-no-1/an-alternative-framework-for-agent-recruitment/)
- [Cialdini, *Influence: The Psychology of Persuasion*](https://en.wikipedia.org/wiki/Influence:_The_Psychology_of_Persuasion) (basis for the RASCLS principles)
- [PERSEREC Espionage Database (DoD historical case archive)](https://www.dhra.mil/PERSEREC/)
