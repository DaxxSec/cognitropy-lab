# Counterintelligence Motive Identification Workspace — Creation Report

**Date Created:** 2026-05-08
**Template:** `counterintelligence-analysis-motive-identification` v1.0
**Category:** Security & Intelligence
**Domain:** counterintelligence analysis motive identification
**Technique:** using standardized inspection checklists
**Day Number:** 44

## Purpose

This workspace converts raw indicator data on a subject of authorized CI inquiry into a defensible, ICD 203-compliant motive assessment by applying standardized inspection checklists drawn from the MICE-RC framework, the DCSA insider-threat indicator taxonomy, ICD analytic standards, and the unclassified PERSEREC case archive. Standardization is the load-bearing layer: every motive hypothesis traces from source → indicator → checklist item → MICE-RC category → confidence rating, and that traceability is what makes the finding survive legal, IG, and adjudicative review.

The domain is a strong fit for the Cognitropy lab: CI motive analysis is an empirical, doctrinally-rich discipline whose core methodology is checklist-driven and whose output is an analytic product, not an operational action. The technique pairing (standardized inspection checklists) is what distinguishes a defensible motive assessment from an ad-hoc one, and the workspace's discipline maps directly onto the technique.

## Workspace Contents

### Core Documentation (3 files)
1. **CLAUDE.md** — Agent role, command index, foundational instructions
2. **README.md** — Comprehensive guide with getting-started, command reference, use cases, doctrinal references
3. **CREATION_REPORT.md** — This file

### Context & Agent Knowledge (7 files)
4. **context/project.md** — Case scope, authority basis, subject category, source inventory, reporting chain
5. **context/role.md** — Analyst identity, organization, clearance, frameworks familiar, restrictions
6. **context/constraints.md** — Authorization, USPER protections, classification, indicator discipline, adverse-action prohibition
7. **context/for-agent/domain-knowledge.md** — MICE → MICE-RC, RASCLS, 5-domain taxonomy, ICD 203 lexicon, ACH, base-rate reasoning, failure modes, case-pattern lessons
8. **context/for-agent/workflows.md** — 4 core workflows (indicator inspection, motive profiling, timeline correlation, recruit-vector + peer-review)
9. **context/for-agent/environment.md** — Workspace classification, system of record, audit logging, source-system access, end-of-session hygiene
10. **context/for-agent/tools.md** — SAT tooling, Admiralty Code, MCP integrations, output formats

### Command Implementations (7 files)
11. **.claude/commands/onboard.md** — Authority confirmation, identity, subject, source inventory, civil-liberties affirmation
12. **.claude/commands/indicator-checklist.md** — 5-domain standardized inspection
13. **.claude/commands/build-motive-profile.md** — MICE-RC mapping with weighted evidence
14. **.claude/commands/timeline-correlate.md** — Indicator + life-event chronology with causation hypotheses
15. **.claude/commands/recruit-vector-assessment.md** — RASCLS pattern match + vector classification (no service attribution)
16. **.claude/commands/peer-review-checklist.md** — ICD 203 walk + ACH matrix + bias inventory + civil-liberties recheck
17. **.claude/commands/produce-ci-finding.md** — ICD 203-compliant finding generation with adverse-action disclaimer

### Prompts (3 files)
18. **prompts/indicator-elicitation.md** — Supervisor/peer interview scaffold with domain-aligned probes
19. **prompts/ach-matrix-build.md** — ACH matrix construction with sensitivity analysis
20. **prompts/source-vetting.md** — Source motive-inventory and Admiralty-Code rating

### Reference Materials (3 files)
21. **resources/mice-rc-checklist.md** — Canonical MICE-RC inspection instrument with per-category items
22. **resources/indicator-taxonomy.md** — 5-domain taxonomy with stable item IDs and false-positive notes
23. **resources/espionage-case-references.md** — Sanitized indicator-pattern references from the unclassified CI record

### User Documentation (2 files)
24. **user-docs/getting-started.md** — Analyst-facing quick-start with pitfalls and pause-conditions
25. **user-docs/checklist-philosophy.md** — Why standardized checklists, and how not to misuse them

### Working Directories (3 files)
26. **work-log/session-log.md** — Append-only session log template
27. **work-log/2026-05-08.md** — Initial creation entry
28. **planning/plan.md** — Phase-structured plan template

## Key Features

### 1. Doctrinal Anchoring
Every analytic step traces to publicly-cited doctrine: ICD 203 for analytic standards, ICD 205 for outreach, DoD 5240.06 for CI awareness, DoD 5205.16 for insider threat, EO 12333 for USPER protections, Heuer 1999 for ACH, Burkett 2013 for RASCLS, the unclassified PERSEREC archive for empirical case patterns.

### 2. MICE-RC Operationalized
The framework is not just described in domain knowledge; it is operationalized as a populated checklist (`resources/mice-rc-checklist.md`) and as the structuring frame of `/build-motive-profile`. Per-category aggregation rules force the analyst to distinguish "indicator pattern of concern" from "motive finding."

### 3. Civil-Liberties Discipline as Code
The `context/constraints.md` file is referenced at every command's predication step. Civil-liberties protections (USPER minimization, protected-class exclusions, whistleblower-protected disclosure exclusions, adverse-action prohibition, source protection) are walked at peer review and re-walked before a finding is produced.

### 4. Mandatory Alternative-Hypothesis Reasoning
The peer-review checklist requires an Analysis of Competing Hypotheses matrix with at least four hypotheses including the null. The dominant hypothesis is the one with fewest *inconsistencies*, not most consistencies — Heuer's foundational ACH discipline. Single-hypothesis findings cannot pass peer review.

### 5. Calibrated Confidence Reporting
The ICD 203 lexicon (almost certainly / highly likely / likely / roughly even / unlikely / highly unlikely / almost no chance) is paired with separate confidence ratings (high/moderate/low). The "high likelihood + low confidence" combination is explicitly supported and disclosed — a real combination the analyst will encounter in source-thin cases.

### 6. Recruit-Vector Without Service Attribution
The RASCLS framework is applied to contact patterns to classify *vector type* (volunteer, cold approach, cultivated, coerced, unwitting, internal) without attributing to a specific hostile service. Service attribution is explicitly noted as a separate evidentiary chain outside this analytic frame.

### 7. The Null-Hypothesis-as-Valid-Finding Frame
The workspace explicitly treats "indicator pattern does not support a motive finding" as a valid, valuable analytic output — not a failure. This frame matches the empirical base rate (most cleared subjects examined are not compromised) and counters the bias toward producing positive findings.

## Design Decisions

- **Doctrine over invention.** The framework is well-trodden; the workspace's value is operationalizing it consistently, not inventing new theory. Where tension between doctrines exists (e.g., MICE vs. MICE-RC vs. RASCLS), MICE-RC is adopted as the working frame because it best handles the contemporary case record.
- **Standardization is the technique.** "Using standardized inspection checklists" is the day's technique pairing, and the workspace pursues it literally — the 5-domain checklist with stable item IDs (`F-01`, `FC-05`, `T-12`, etc.) is the canonical instrument, and the commands are checklists in narrative form.
- **Civil-liberties first, not last.** Protections are wired into onboarding, every command's predication check, peer review, and finding production. They are not a footer paragraph; they are gating conditions.
- **Indicator vs. accusation.** The workspace insists on neutral analytic language ("indicator pattern is consistent with X" not "subject is X") throughout. This is doctrinal discipline, not stylistic preference.
- **Refusal is a feature.** The agent refuses to proceed under unclear authority, refuses to score protected-class characteristics as indicators, refuses single-domain motive findings, refuses to attribute to a specific service from contact-pattern alone, and refuses to publish findings that fail the peer-review checklist. Each refusal is the workspace working correctly.
- **Empirically calibrated.** The case-pattern reference (`resources/espionage-case-references.md`) provides calibration anchors from the unclassified record (Ames, Hanssen, Walker, Pollard, Montes, Snowden, Winner, Shriver, Lee). These are calibration sets, not templates — the workspace is explicit about the difference.

## Files Created

Total: **28 files** across **9 directories**.

| Directory | Files | Purpose |
|---|---|---|
| Root | 3 | Core documentation |
| context/ | 3 | Project, role, constraints |
| context/for-agent/ | 4 | Domain knowledge, workflows, environment, tools |
| .claude/commands/ | 7 | Slash command implementations |
| prompts/ | 3 | Reusable prompt scaffolds |
| resources/ | 3 | MICE-RC checklist, indicator taxonomy, case references |
| user-docs/ | 2 | Getting started, checklist philosophy |
| work-log/ | 2 | Session log template, creation entry |
| planning/ | 1 | Phase-structured plan |

---

**Workspace Status:** READY FOR USE
**Last Updated:** 2026-05-08
**Version:** 1.0
