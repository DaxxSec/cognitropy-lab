# Emissions System Troubleshooting — Core Concepts

Background the agent should read before acting on tasks in this domain. Optimised for fast recall, not exhaustive theory. The organizing idea: **a vehicle's emissions system is a small distributed system of sensors and ECUs, and root-cause diagnosis is a consensus problem over unreliable nodes, recorded in a tamper-evident evidence log.**

## The emissions control system as a distributed system

The closed-loop fuel/emissions system is a set of communicating nodes:

- **ECU/PCM** — the coordinator; runs closed-loop fuel control and the OBD monitors.
- **Upstream O₂ / wideband (A/F) sensors** (B1S1, B2S1) — primary fuel-control feedback; switch ~0.1–0.9 V (narrowband) or report λ directly (wideband).
- **Downstream O₂ sensors** (B1S2, B2S2) — *catalyst monitor* feedback; should be lazy/steady when the cat stores oxygen well.
- **MAF / MAP / IAT / ECT / TPS / CKP / CMP** — load and state inputs.
- **EGR position, evap purge/vent solenoids, secondary-air, DPF ΔP, NOx, DEF-quality** sensors/actuators on the emissions periphery.

They exchange messages over **CAN** (ISO 15765). Like any distributed system, the nodes can disagree, lag, or be wrong, and the coordinator must still decide. That decision-making — under unreliable inputs — is what consensus algorithms formalize.

## OBD-II: the message log you start from

OBD-II exposes diagnostic *services* (modes). These are your raw evidence feed:

- **Mode 01** — live data (current PIDs: fuel trims, sensor voltages, load, RPM).
- **Mode 02** — *freeze frame*: the snapshot of conditions captured when a DTC set. The single most under-used piece of evidence — it tells you the operating point at the moment of failure.
- **Mode 03 / 07 / 0A** — stored / pending / permanent DTCs. Permanent codes (0A) cannot be cleared by a battery pull and only self-clear after the monitor re-passes — they are the system's "committed" failures.
- **Mode 06** — on-board monitor test results (TID/MID + raw value vs min/max limits). This is the numeric backbone behind a P0420 etc.; read it *before* condemning a part.
- **Readiness monitors** — flags showing which self-tests have run since the last clear.

## DTC families (what the codes actually mean)

- **Catalyst** — `P0420`/`P0430` (efficiency below threshold, bank 1/2). Diagnosed by front-vs-rear O₂ correlation, *not* by the code alone.
- **Fuel trim / mixture** — `P0171`/`P0174` (lean B1/B2), `P0172`/`P0175` (rich). The master signal: see fuel trims below.
- **O₂ / A-F sensor** — `P013x`/`P014x` (heater, slow response, range).
- **EGR** — `P0401` (insufficient flow), `P0402` (excessive), `P0404` (range/performance).
- **EVAP** — `P0440` (general), `P0442` (small leak), `P0455` (large leak), `P0456` (very small leak), `P0457` (loose/missing cap).
- **Secondary air** — `P0410`.
- **Diesel** — `P2002` (DPF efficiency), `P20EE` (SCR NOx efficiency), `P2459` (regen frequency), DEF-quality/dosing codes.

## Fuel trims — the system's "vote count"

Short-term (STFT) and long-term (LTFT) fuel trim are the ECU's *running correction* to hit stoichiometric λ=1 (≈14.7:1 for gasoline). They are the most honest aggregate signal in the system:

- **Positive trim (e.g. LTFT +15%)** = ECU adding fuel = it sees **lean** → unmetered air (vacuum/intake leak), low fuel pressure/delivery, or a **MAF reading low**.
- **Negative trim (e.g. LTFT −12%)** = ECU pulling fuel = it sees **rich** → high fuel pressure, leaking injector, or a **MAF reading high**.
- **Trim vs load/RPM pattern** localizes the fault: lean at idle only → vacuum leak; lean across all loads → fueling/MAF; rich only at idle → leaking injector. Trims around ±5% are normal; ±10% is suspect; ±25% is a hard fault (and many ECUs cap correction there).

## Consensus & fault models (the imported rigor)

- **Consensus problem** — get a set of nodes to *agree* on one value (here: one root cause) despite some being unreliable. Properties to want: **agreement** (one committed cause), **validity** (it's supported by real evidence), **termination** (you actually decide).
- **Quorum** — a decision needs a majority of *independent* witnesses, not one loud one. Replicated systems commit a value only after a quorum acknowledges; you commit a root cause only after a quorum of independent corroborating tests agrees.
- **Crash (fail-stop) fault** — a node that's simply *dead*: open-circuit sensor, no signal, default substitution. Easy to detect, easy to exclude.
- **Byzantine fault** — a node that's *alive and lying*: a skewed O₂ sensor, a contaminated MAF reading 20% low, a downstream O₂ fooled by an exhaust leak. The dangerous case — it provides plausible evidence that points the wrong way. PBFT tolerates `f` Byzantine nodes with `3f+1` total; the diagnostic analog is **physical cross-validation** — never accept a sensor's value without an independent check.
- **Leader vs follower** — in a multi-DTC set, one fault is usually the *leader* (root) and the rest are *followers* (downstream consequences it triggered). A misfire (leader) can set a catalyst code, a lean code, and an O₂ code (followers).
- **Split-brain** — two plausible root causes both have partial support and the system can't tell which is "primary." Resolve with a **witness / tiebreaker**: one decisive test that falsifies one branch.
- **Append-only replicated log** — Raft/Paxos commit decisions onto an ordered log that is never rewritten. Your **chain-of-custody ledger** is exactly this log; the *log-matching* property (each entry consistent with its predecessor) is enforced by hash-linking each evidence entry to the prior one's hash.

## Chain-of-custody / evidence integrity (today's technique)

Every datum in a case is an *evidence entry* with: **what** (the reading/test), **value/result**, **when** (timestamp), **who** (collector/tool), **where/how** (conditions, location), and **prev-hash** (the hash of the previous entry). Append-only, never edited; a correction is a *new* entry citing the one it supersedes. This buys three things: **tamper-evidence** (a broken hash chain is visible), **provenance** (the committed diagnosis traces to its supporting entries), and **reproducibility** (another tech replays the log and reaches the same commit). It is what makes a diagnosis defensible to a warranty adjudicator, a CARB referee, or a fleet auditor.

## Fusion mapping (consensus concept → emissions-diagnosis analog)

| Consensus / distributed-systems concept | Emissions-diagnosis analog |
|---|---|
| Node | Sensor / monitor / evidence source |
| Crash (fail-stop) fault | Dead sensor — open circuit, no signal, default substitution |
| Byzantine fault | Skewed/lying sensor — biased O₂, low-reading MAF, leak-fooled downstream O₂ |
| Proposed value | Candidate root cause |
| Quorum | Minimum set of independent corroborating tests before committing |
| Committed value | Confirmed, defensible root-cause diagnosis |
| Append-only replicated log | Chain-of-custody evidence ledger |
| Log-matching / hash chain | Each evidence entry hash-linked to the previous (tamper-evidence) |
| Leader | Root DTC / primary fault |
| Followers | Downstream-consequence DTCs |
| Term / epoch | Diagnostic case ID |
| Split-brain | Two competing root causes with partial support |
| Witness / fencing | The single decisive discriminating test |
| Re-replication / apply | Repair to spec + drive-cycle verification |

## Common Failure Modes

- **Condemning on the loudest code** — quoting a converter for a P0420 that is actually an exhaust leak or a skewed upstream O₂. The classic Byzantine trap.
- **Trusting a single sensor as ground truth** — a MAF reading low *looks* like a fueling/air problem; without the MAP cross-check it's accepted as fact and the real (sensor) fault is missed.
- **Clearing codes to "test"** before logging freeze frame / Mode 06 — destroys the freeze-frame evidence (the snapshot at failure) and resets readiness; log before you clear.
- **No quorum, premature commit** — committing on one passing/failing test; the fault returns and the case "comes back."
- **Unresolved split-brain** — repairing both candidates ("parts cannon") instead of designing one discriminating test.
- **Broken custody** — editing a logged reading in place, or not recording conditions, so the diagnosis can't be defended or reproduced.

## Operating Constraints

- **Anti-tampering law (hard):** never disable, delete, mask, or simulate an emissions control or OBD monitor on a road vehicle (Clean Air Act §203, CARB, EU/UNECE). Diagnose and repair to spec only.
- **Evidence is physical and time-stamped:** trims, monitor results, and leak tests depend on operating conditions (temp, load, fuel level for evap) — record them or the evidence is not reproducible.
- **A committed diagnosis implies a repair plan + verification** — no "diagnosis" closes a case without a planned fix and a drive-cycle confirmation.
