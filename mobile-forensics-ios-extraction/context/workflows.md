# Mobile Forensics — iOS Extraction — Workflows and Methodology

Procedures and decision trees the agent runs. Concepts (`concepts.md`) say *what things are*; this file says *what to do with them*. The through-line is today's technique — **structured hypothesis testing** — applied to both acquisition (which method?) and analysis (which explanation?).

## Workflow 1: Seizure-to-report acquisition lifecycle

**Goal:** acquire an iOS device defensibly while preserving its perishable state.

### Phases

1. **Authorise & document** — confirm warrant/consent/ownership; record legal scope. Out-of-scope data is not yours to extract.
2. **Isolate** (`/isolate-evidence`) — place in a Faraday bag/enclosure with power; if isolation is impossible, enable Airplane Mode only as a documented last resort. Capture any reachable pairing/lockdown record from a seized host *now* (it can bypass USB Restricted Mode and unlock backups).
3. **Identify** (`/identify-device`) — model, SoC, iOS version; derive method eligibility (checkm8? agent-only?).
4. **Assess lock state** (`/assess-lock-state`) — BFU or AFU; passcode known/unknown. This sets the ceiling on what is extractable and how urgent the next step is.
5. **Plan** (`/plan-extraction`) — choose the least-invasive method that answers the question within authority. Prefer encrypted backup over unencrypted when only logical is available; prefer FFS/agent in AFU when sandbox/system data is needed.
6. **Acquire** — execute the chosen method; never reboot an AFU device. Log every action with timestamps.
7. **Verify** (`/verify-extraction`) — hash the image; cross-validate with a second tool; check completeness against the keybag (which classes unwrapped).
8. **Analyse** — parse artifacts, run the ACH loop (Workflow 2), carve deleted data (`/carve-sqlite`), build the timeline (`/reconstruct-timeline`).
9. **Report** (`/draft-examination-report`) — findings, confidence, refuted alternatives, methodology, chain of custody.

### Decision Points

- If **AFU**: treat as time-critical; keep powered + isolated; pursue FFS/agent before any state loss.
- If **BFU + unknown passcode**: expect Class D only; document the limitation; consider checkm8 (A5–A11) for what little is reachable, or hold pending lawful passcode access.
- If **checkm8-eligible (A5–A11)**: a BootROM acquisition is available regardless of patch level — but still cannot defeat passcode-derived keys on BFU without brute force.
- If **A12+ and BFU**: most paths are blocked; escalate to specialist/commercial capability rather than rebooting to "try."

## Workflow 2: The ACH examination loop (structured hypothesis testing)

**Goal:** reach a conclusion that survives disconfirmation, not one that merely accumulates support.

### Steps

1. **Frame the question** (`/frame-hypotheses`) — state the precise investigative question (e.g. "Were the disputed messages sent from this device on 2026-06-26?").
2. **Enumerate hypotheses** — build a mutually-exclusive, collectively-exhaustive set. Always include the *null* / innocent / "evidence was fabricated or synced from elsewhere" hypotheses.
3. **Inventory evidence** — list every relevant artifact, plus assumptions and notable *absences* (an expected log that is missing is evidence).
4. **Score diagnosticity** (`/build-diagnosticity-matrix`) — mark each (evidence × hypothesis) cell Consistent / Inconsistent / N-A. Down-weight evidence consistent with all hypotheses; up-weight evidence inconsistent with some.
5. **Rank by disconfirmation** — order hypotheses by the weight of *inconsistent* evidence against each. The least-disconfirmed survives.
6. **Sensitivity check** — identify the 1–3 evidence items the conclusion hinges on. For each, ask: if it were misdated, a tool artifact, or planted, does the ranking flip? Flag the dependency.
7. **Conclude with confidence** — state the surviving hypothesis, a calibrated confidence, and the alternatives ruled out plus the evidence that ruled them out.

### Decision Points

- If two hypotheses are **near-tied** after scoring: the data is under-diagnostic. Identify what artifact *would* discriminate them and go collect/carve it (`/carve-sqlite`, `/reconstruct-timeline`) before concluding.
- If the conclusion depends on **one fragile artifact**: lower confidence and seek a corroborating, independent source.
- If new evidence arrives: re-score the matrix — never bolt a finding on without re-running diagnosticity.

## Workflow 3: Deleted-record recovery and timeline fusion

**Goal:** recover what was removed and place events on one clock.

1. **Carve** (`/carve-sqlite`) — for each target DB, pull `-wal`, `-shm`, and rollback journal; recover rows from the WAL not yet checkpointed, from freelist pages, and from unallocated. Distinguish *deleted-but-recoverable* from *never-existed*.
2. **Normalise time** — convert every source to UTC, accounting for Unix vs Mac-absolute (2001 epoch) vs Core Data timestamps; record the conversion used.
3. **Fuse** (`/reconstruct-timeline`) — merge `KnowledgeC` usage, `powerlog` charge/screen events, `CallHistory`, and `sms.db` into a single ordered timeline; flag gaps and overlaps.
4. **Feed the matrix** — every recovered row and timeline interval becomes evidence in Workflow 2, scored for diagnosticity rather than assumed probative.

### Decision Points

- If WAL and main DB **disagree**: the WAL is usually more recent; note both and which checkpoint state each reflects.
- If a recovered row has **no corroborating artifact**: treat as low-weight until a second source supports it.
