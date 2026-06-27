# Mobile Forensics — iOS Extraction Workspace

> A Claude Agent workspace for acquiring and analysing iOS devices the disciplined way: pick the right extraction method for the hardware and lock state, then reason about the evidence with structured hypothesis testing instead of confirmation bias.

## What This Workspace Does

iPhone and iPad examinations have two hard problems. The first is **acquisition**: on a modern device, what you can extract is dictated by the SoC generation, the iOS version, the Data Protection encryption classes, and — decisively — whether the phone was seized **Before First Unlock (BFU)** or **After First Unlock (AFU)**. The second is **interpretation**: a phone yields tens of thousands of artifacts, and it is dangerously easy to anchor on the first explanation that fits and cherry-pick supporting rows from `sms.db`.

This workspace addresses both. It encodes the acquisition decision tree (logical → full-file-system → agent-based → checkm8) as bespoke commands that start from a device fingerprint and a lock-state assessment, and it makes **Analysis of Competing Hypotheses (ACH)** the default reasoning method: enumerate every plausible explanation up front, score each artifact by how well it *discriminates* between hypotheses, and rank explanations by the disconfirming evidence they survive. The engine seeded this build with the technique *structured hypothesis testing*, which is exactly the ACH loop the commands implement.

The output is a reproducible examination: an acquisition plan tied to the device's real capabilities, a diagnosticity matrix that shows which artifacts mattered and why, a fused activity timeline, integrity verification against the keybag, and a court-ready report that states confidence and the alternatives that were ruled out.

## Why This Workspace Exists

Mobile forensics fails in two recognisable ways. Technically, examiners over-collect or pick a method the device can't support — attempting a full file system extraction on a BFU A15 phone, or rebooting an AFU device and losing everything that was decryptable. Analytically, reports assert a single narrative without showing the competing explanations that were considered. Both are avoidable with structure. This workspace codifies the method so the examiner spends judgment on the evidence, not on remembering which iPhone supports checkm8 or how to lay out an ACH matrix.

## Getting Started

### Prerequisites

- A **legal basis** for examination — warrant, documented consent, or ownership. Record it before touching the device.
- A forensic acquisition tool. Open/free: `libimobiledevice` (`idevice_id`, `ideviceinfo`, `idevicebackup2`), `checkra1n`/`palera1n` (checkm8 devices), `iLEAPP` for parsing. Commercial: Cellebrite UFED/Premium, Magnet GrayKey, ELCOMSOFT iOS Forensic Toolkit, Magnet AXIOM.
- A **Faraday bag or RF-shielded enclosure** and a charged power source inside isolation.
- A SQLite browser/CLI (`sqlite3`, `DB Browser for SQLite`) for artifact and WAL inspection.
- A write-once evidence store and a hashing tool (`sha256sum`).

### Quick Start

1. Clone this workspace and confirm your legal authority is documented.
2. Run `/isolate-evidence` the moment the device is in hand — RF isolation and pairing-record capture are time-critical.
3. Run `/identify-device` then `/assess-lock-state` to fingerprint the hardware and pin BFU vs AFU.
4. Run `/plan-extraction` to choose the method that the device + state + authority actually permit, then acquire and `/verify-extraction`.
5. Run `/frame-hypotheses` on the investigative question and `/build-diagnosticity-matrix` to drive the analysis; finish with `/reconstruct-timeline` and `/draft-examination-report`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/identify-device` | Fingerprint model, SoC, iOS version; map to viable methods | First, once the device is identified and isolated |
| `/assess-lock-state` | Classify BFU vs AFU; enumerate what's decryptable now | Immediately after seizure, before any reboot |
| `/isolate-evidence` | RF isolation + lockdown/pairing-record capture protocol | At the scene, before transport |
| `/plan-extraction` | Choose logical / FFS / agent / checkm8 method | After device + lock state are known |
| `/frame-hypotheses` | Build mutually-exclusive, exhaustive competing hypotheses | When the investigative question is set |
| `/build-diagnosticity-matrix` | Score artifacts × hypotheses; rank by disconfirmation | After artifacts are extracted and parsed |
| `/carve-sqlite` | Recover deleted rows from WAL/journal/freelist/unallocated | When messages/calls/records appear deleted |
| `/reconstruct-timeline` | Fuse KnowledgeC/powerlog/biome/sms/calls into one timeline | To establish pattern-of-life or sequence of events |
| `/verify-extraction` | Hash + dual-tool + keybag completeness check | After every acquisition; before analysis |
| `/draft-examination-report` | Court-ready report with confidence and refuted alternatives | At the end of the examination |

## Directory Structure

```
mobile-forensics-ios-extraction/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke iOS-forensics commands
├── context/
│   ├── concepts.md           # Data Protection, BFU/AFU, extraction taxonomy, ACH
│   ├── workflows.md          # Acquisition lifecycle + ACH examination loop
│   └── references.md         # SoC/checkm8 table, artifact paths, DP classes, links
├── prompts/                  # Reusable ACH + reporting prompt templates
└── outputs/                  # Plans, matrices, timelines, reports
```

## Example Use Cases

### Choosing a method without bricking the evidence
A phone arrives powered on and unlocked-since-boot. `/assess-lock-state` flags it as AFU, `/identify-device` shows an A13 on iOS 16, and `/plan-extraction` recommends an agent-based full file system extraction *now* — explicitly warning that a reboot drops it to BFU and forfeits most user data.

### Testing competing explanations for a deleted thread
Messages are missing from `sms.db`. `/carve-sqlite` recovers rows from the WAL and freelist; `/frame-hypotheses` lays out "user deleted," "auto-expire (disappearing messages)," "never existed / fabricated," and "sync artifact," and `/build-diagnosticity-matrix` shows which recovered timestamps actually discriminate between them.

### Pattern-of-life reconstruction
`/reconstruct-timeline` fuses `KnowledgeC.db` app-usage, `powerlog` charge/unlock events, and `CallHistory` to show whether the device was in active use during a window of interest — and the timeline itself becomes evidence in the matrix.

### Defensible reporting
`/draft-examination-report` produces a report that states each finding's confidence, lists the alternative hypotheses considered and the evidence that refuted them, and pins tool versions and hashes for reproducibility.

## Recommended MCP Servers

- **Filesystem MCP** — read extracted artifact trees and write outputs/reports under the examiner's control.
- **SQLite MCP** — query `sms.db`, `KnowledgeC.db`, `Photos.sqlite`, and inspect WAL/journal pages directly.
- **Sequential-thinking / reasoning MCP** — useful scaffolding for working through the ACH diagnosticity matrix step by step.

## Legal & Ethical Considerations

- **Authority is mandatory.** Examine a device only under a warrant, documented consent, or clear ownership. Note the legal basis in the report.
- **Self-incrimination and compelled passcodes** are jurisdiction-specific (e.g., the US Fifth Amendment debate over passcodes vs. biometrics). Do not assume you can compel an unlock.
- **Minimisation.** Extract and retain only what the authority covers; iOS backups contain Health, location, and third-party data far beyond most scopes.
- **No real PII in this repo.** All examples here are synthetic. Keep case data in a controlled evidence store, not in the workspace.

## Technical References

- [Apple Platform Security Guide](https://support.apple.com/guide/security/welcome/web) — authoritative on Data Protection classes, the Secure Enclave, and keybags.
- [NIST SP 800-101r1 — Guidelines on Mobile Device Forensics](https://csrc.nist.gov/pubs/sp/800/101/r1/final) — acquisition methodology and validation.
- [Heuer, *Psychology of Intelligence Analysis* (Ch. 8, ACH)](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/) — the Analysis of Competing Hypotheses method.
- [checkm8 / checkra1n](https://checkra.in/) — BootROM exploit context for A5–A11 devices.
- [iLEAPP — iOS Logs, Events, And Plists Parser](https://github.com/abrignoni/iLEAPP) — open-source artifact parser.
- [libimobiledevice](https://libimobiledevice.org/) — open-source iOS communication and backup tooling.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
