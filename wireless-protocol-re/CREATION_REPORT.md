# Wireless Protocol Reverse Engineering Workspace — Creation Report

**Date Created:** 2026-04-12
**Template:** `wireless-protocol-re` v1.0
**Category:** RF/SDR/Signals
**Technique:** Resource Optimization Algorithms

## Purpose

This workspace provides a structured environment for reverse engineering unknown or proprietary wireless protocols using SDR hardware. It applies resource optimization algorithms — weighted spectrum scheduling, multi-armed bandit dwell time optimization, priority queuing, and DAG-based pipeline scheduling — to make the RE process more efficient and systematic.

The domain is a natural fit for the Cognitropy Lab: wireless protocol RE sits at the intersection of RF engineering, digital signal processing, security research, and algorithmic optimization. The optimization angle transforms what is typically an ad-hoc exploration process into a structured, measurable workflow.

## Workspace Contents

### Core Documentation (3 files)
1. **CLAUDE.md** — Agent role, commands, foundational instructions
2. **README.md** — Comprehensive guide with getting started, command reference, use cases
3. **CREATION_REPORT.md** — This file

### Context & Agent Knowledge (7 files)
4. **context/project.md** — Target device/signal definition template
5. **context/role.md** — User role and experience template
6. **context/constraints.md** — Legal, ethical, and technical boundaries
7. **context/for-agent/domain-knowledge.md** — Full RE methodology, modulation schemes, ISM bands, 5 optimization algorithms, CRC reference table
8. **context/for-agent/workflows.md** — 4 core workflows with decision trees
9. **context/for-agent/environment.md** — SDR hardware and software setup template
10. **context/for-agent/tools.md** — Tool configurations, command references, databases

### Command Implementations (7 files)
11. **.claude/commands/onboard.md** — Interactive hardware/target/goal setup
12. **.claude/commands/capture-plan.md** — Resource-optimized RF capture planning
13. **.claude/commands/decode-signal.md** — Step-by-step signal decoding walkthrough
14. **.claude/commands/protocol-map.md** — Protocol state machine construction
15. **.claude/commands/spectrum-sweep.md** — Optimized spectrum survey with priority scoring
16. **.claude/commands/compare-known.md** — Known protocol database comparison with similarity scoring
17. **.claude/commands/report-findings.md** — Structured RE findings report generation

### Prompts (3 files)
18. **prompts/unknown-signal-analysis.md** — Template for analyzing unknown captured signals
19. **prompts/ism-device-survey.md** — Template for systematic ISM band device surveys
20. **prompts/capture-session-setup.md** — Quick capture session configuration template

### Reference Materials (3 files)
21. **resources/known-protocol-signatures.md** — Protocol fingerprints for 315/433/868/915/2400 MHz bands
22. **resources/sdr-settings-reference.md** — HackRF/RTL-SDR specs, settings, storage calcs, antenna guide
23. **resources/crc-bruteforce-guide.md** — CRC identification methodology with tools and code examples

### User Documentation (2 files)
24. **user-docs/getting-started.md** — Quick start guide for new users
25. **user-docs/optimization-explained.md** — Plain-language explanation of optimization algorithms

### Working Directories (2 files)
26. **work-log/session-log.md** — Capture and analysis session logging template
27. **planning/.gitkeep** — Directory for active analysis plans

## Key Features

### 1. Resource Optimization Algorithms
Five distinct optimization approaches codified in the domain knowledge:
- Weighted interval scheduling for spectrum coverage
- Epsilon-greedy multi-armed bandit for dwell time
- Dynamic scoring priority queue for signal triage
- Triggered capture with compression for storage optimization
- DAG-based task scheduling for parallel analysis pipelines

### 2. Comprehensive Protocol Database
Known protocol signatures covering 315 MHz, 433 MHz, 868/915 MHz, and 2.4 GHz bands with modulation, data rate, preamble, and sync word details.

### 3. CRC Identification Toolkit
Step-by-step CRC bruteforce methodology with common polynomials, automated tool guidance (reveng, crcmod, CyberChef), and edge case documentation.

### 4. Full RE Pipeline Coverage
From wideband spectrum survey through signal characterization, demodulation, bit recovery, frame analysis, state machine mapping, to formal reporting.

### 5. Hardware-Specific Guidance
Tailored SDR settings, gain configurations, sample rate recommendations, and capture commands for HackRF One and RTL-SDR v3.

## Design Decisions

- **Optimization-first approach:** The technique assignment was "resource optimization algorithms," so optimization is woven into every workflow rather than being a bolt-on feature
- **Practical over theoretical:** CRC bruteforce guide includes actual code snippets and tool commands, not just algorithm descriptions
- **Hardware-agnostic with specifics:** Templates accept any SDR, but reference materials provide concrete settings for the two most common platforms
- **Legal compliance built in:** Constraints and ethical guidelines are prominent, not afterthoughts

## Files Created

Total: **27+ files** across **10 directories**

| Directory | Files | Purpose |
|-----------|-------|---------|
| Root | 3 | Core documentation |
| context/ | 3 | Project, role, constraints |
| context/for-agent/ | 4 | Domain knowledge, workflows, environment, tools |
| .claude/commands/ | 7 | Slash command implementations |
| prompts/ | 3 | Reusable prompt templates |
| resources/ | 3 | Protocol signatures, SDR reference, CRC guide |
| user-docs/ | 2 | Getting started, optimization explanation |
| work-log/ | 1 | Session logging template |
| planning/ | 1 | Active plans directory |
| outputs/ | 1 | Generated artifacts directory |

---

**Workspace Status:** READY FOR USE
**Last Updated:** 2026-04-12
**Version:** 1.0
