# Emissions System Troubleshooting Workspace

> Diagnose emissions faults the way a distributed system reaches consensus — corroborate conflicting sensors, tolerate the ones that lie, and only *commit* a root cause the evidence can defend.

## What This Workspace Does

This workspace turns emissions-control diagnosis into a disciplined consensus problem. A modern vehicle's emissions system *is* a small distributed system: O₂/lambda sensors, MAF, MAP, EGR position, fuel-trim feedback, evap pressure, and one or more ECUs all exchange messages over a CAN bus, and they don't always agree. A stored P0420 ("catalyst efficiency below threshold") might mean a dead converter — or it might mean an exhaust leak fooling the downstream O₂ sensor, or a skewed upstream sensor lying about the air/fuel ratio. The loudest code is rarely the root cause.

So instead of reacting to the first DTC, this workspace borrows the **rigor and process of distributed-systems consensus algorithms**. Each sensor and monitor is a *node* that may be faithful, crashed (dead/open-circuit), or **Byzantine** (reporting plausible-but-wrong values). Evidence is *replicated* into a **chain-of-custody ledger** — an append-only, hash-linked log that nothing edits in place. A candidate root cause is a *proposed value*; it is only **committed** when a **quorum** of independent, corroborating evidence agrees and no sensor is still flagged Byzantine. Competing hypotheses ("bad cat" vs "exhaust leak") are a *split-brain* you resolve with one decisive discriminating test before committing.

The chain-of-custody discipline (today's engine technique) is what makes the diagnosis *defensible*: every reading, smoke test, and part swap is timestamped, attributed, and hash-linked to the entry before it, so the committed conclusion stands up to a warranty adjudicator, a CARB referee, a fleet compliance auditor, or the next technician who reopens the case.

## Why This Workspace Exists

Emissions diagnosis has a high false-positive rate and an expensive failure mode: parts get "thrown" at codes (a new catalytic converter is hundreds of dollars; a P0420 that was really a $40 exhaust gasket is a classic), and a misdiagnosis that disables a monitor to "make the code go away" crosses into illegal tampering. The cost of being wrong — financially, legally, and environmentally — is exactly the cost that consensus protocols were invented to manage: how do you commit a correct decision when some of your inputs are unreliable or actively wrong? This workspace codifies that answer for the bay: corroborate before you commit, distrust the lying sensor, and keep an evidence trail that proves you did.

## Getting Started

### Prerequisites

- An OBD-II scan tool capable of **Mode 06** (on-board monitor test results) and live data, not just code read/clear — bidirectional/enhanced is strongly preferred (e.g. a J2534 pass-thru + OEM software, or a capable aftermarket tool).
- A **smoke machine** (EVAP/intake leak testing) and a **lab scope** or graphing meter for sensor waveforms.
- Reference data for the specific vehicle: FSM/service info, expected sensor ranges, and the OEM drive-cycle / readiness-monitor procedure.
- Basic gas-analyzer access is a plus for tailpipe corroboration (the ground-truth "external observer").

### Quick Start

1. Clone this workspace and read `CLAUDE.md`, then skim `context/concepts.md` for the fusion model.
2. Run `/open-case` to capture the VIN, complaint, and ambient conditions and open the chain-of-custody ledger (a new consensus "term").
3. Run `/ingest-scan` to pull DTCs, freeze frame, live data, and Mode 06 results into the ledger as evidence nodes.
4. Run `/cross-validate-sensors` to flag any Byzantine (lying) sensors *before* you trust their data, then `/classify-faults` to separate root codes from downstream consequences.
5. Run `/build-quorum` on your leading candidate, `/resolve-split` if two causes are tied, `/commit-diagnosis` when the evidence agrees, repair to spec, and close with `/verify-repair` + `/custody-report`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/open-case` | Open a diagnostic case = new consensus term; capture VIN/complaint/conditions; init the ledger | First, on every new vehicle or new complaint |
| `/ingest-scan` | Pull OBD-II evidence (Mode 01/02/03/06/07/0A) into the ledger as structured nodes | Right after `/open-case`, before forming any theory |
| `/log-evidence` | Append one hand-collected datum (smoke test, scope trace, pressure, part swap, photo) to the hash-linked ledger | Any time you gather evidence outside the scan tool |
| `/cross-validate-sensors` | Cross-check each sensor against a redundant/derivable reference; flag the liars | After `/ingest-scan`, before trusting any single sensor |
| `/classify-faults` | Build the causal DAG of stored DTCs: root (leader) vs downstream (follower) codes | When multiple DTCs are present |
| `/build-quorum` | Assemble the minimum independent corroborating evidence for a candidate root cause | Once you have a leading hypothesis |
| `/resolve-split` | Design the single decisive test that breaks a tie between two competing causes | When two hypotheses both have partial support |
| `/commit-diagnosis` | Commit the root cause to the ledger once quorum holds and no Byzantine flag is open | Only after quorum is satisfied |
| `/verify-repair` | Re-run monitors to readiness, confirm the DTC stays cleared over a drive cycle, trims in band | After the repair, before closing |
| `/custody-report` | Verify ledger integrity and export the full dossier for warranty / CARB referee / fleet audit | To hand off, claim, or archive the case |

## Directory Structure

```
emissions-system-troubleshooting/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke diagnostic-consensus commands
├── context/
│   ├── concepts.md           # Emissions subsystems, DTCs, fuel trims, consensus/Byzantine model, fusion map
│   ├── workflows.md          # The diagnostic consensus protocol + per-DTC decision trees
│   └── references.md         # DTC table, OBD modes, fuel-trim cheat-sheet, drive cycles, consensus reference
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Per-case ledgers, committed diagnoses, custody dossiers
```

## Example Use Cases

### P0420 — catalyst efficiency, or a liar downstream?
A no-driveability-complaint P0420 comes in. Instead of quoting a converter, `/cross-validate-sensors` checks the downstream O₂ for an exhaust leak (false-lean fooling the monitor) and the upstream sensor for a slow/skewed switch; `/build-quorum` won't let you commit "dead cat" until the leak is ruled out and the front/rear O₂ correlation actually shows poor storage. Often saves the customer a converter.

### P0171/P0174 — lean on both banks
Lean trims on *both* banks point upstream of the splits. `/cross-validate-sensors` compares MAF-derived load against MAP/RPM-derived load to catch a MAF reading low (a Byzantine node), and `/build-quorum` corroborates with a smoke test for unmetered air and a fuel-pressure reading before committing.

### EVAP P0442 — small leak, defensible close
A small evap leak with an intermittent code. The smoke test, the specific leak location photo, and a post-repair monitor pass all land in the hash-linked ledger; `/custody-report` produces a dossier that documents the actual leak and the verified fix — useful for a comeback dispute.

### Fleet / warranty / CARB-referee diagnosis
A diagnosis that may be challenged later. The append-only ledger + committed-diagnosis provenance is exactly the artifact a fleet auditor, warranty adjudicator, or referee program needs: who measured what, when, with which tool, and why the conclusion follows.

### Diesel DPF/SCR (P2002 / P20EE)
Soot-load and NOx-efficiency faults where the "obvious" component is rarely the cause; `/classify-faults` separates a clogged DPF (follower) from a failed regen, a leaking EGR cooler, or a dosing fault (leaders), and quorum gates the commit.

## Recommended MCP Servers

- **Filesystem MCP** — read/write the per-case ledgers and custody dossiers under `outputs/cases/` directly.
- **Fetch / web MCP** — pull DTC definitions, TSBs, and OEM drive-cycle procedures for the specific platform during a case.
- **SQLite / database MCP** — keep a queryable index of prior cases and known-good sensor ranges by platform (a "reference collection" of past consensus rounds).

## Legal & Ethical Considerations

- **Anti-tampering is non-negotiable.** Disabling, deleting, masking, or simulating an emissions control or OBD monitor on an on-road vehicle is illegal under the U.S. Clean Air Act §203(a)(3), CARB regulations, and international equivalents (EU/UNECE). This workspace exists to *find and fix* emissions faults, not to defeat them.
- **No "clear-to-pass."** Clearing a DTC to pass an inspection without a committed root cause and a real repair is both fraud and a tamper act — it is refused here. A committed diagnosis must be followed by a verified repair before a case closes.
- **Privacy.** A VIN and location data identify a vehicle and often a person. Treat case ledgers as containing PII; share custody dossiers only with the owner, their authorized repairer, or the relevant adjudicator.

## Technical References

- [SAE J1979 / ISO 15031-5 — OBD-II diagnostic services & PIDs](https://www.sae.org/standards/content/j1979_201702/) — the mode/PID model the scan evidence is built on.
- [SAE J2012 / ISO 15031-6 — DTC definitions](https://www.sae.org/standards/content/j2012_201612/) — the canonical Pxxxx code dictionary.
- [EPA — vehicle tampering & defeat devices (Clean Air Act §203)](https://www.epa.gov/enforcement/air-enforcement) — the legal boundary this workspace respects.
- [Lamport, "The Part-Time Parliament" (Paxos)](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf) — the consensus foundation.
- [Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm" (Raft)](https://raft.github.io/raft.pdf) — leader election + the append-only replicated log this workspace mirrors.
- [Castro & Liskov, "Practical Byzantine Fault Tolerance" (PBFT)](https://pmg.csail.mit.edu/papers/osdi99.pdf) — tolerating nodes that lie, the model for skewed sensors.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
