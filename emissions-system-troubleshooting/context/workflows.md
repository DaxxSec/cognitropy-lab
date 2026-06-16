# Emissions System Troubleshooting — Workflows and Methodology

Step-by-step procedures the agent runs, tied to today's technique: **evidence chain-of-custody tracking**, framed as a distributed-consensus protocol. `concepts.md` says what the pieces *are*; this file says what the agent *does* with them.

## The Diagnostic Consensus Protocol (master workflow)

**Goal:** reach one committed, defensible root cause from a set of unreliable sensor/monitor inputs, with an unbroken evidence trail.

### Phase 0 — Open the term (`/open-case`)
Capture VIN, vehicle, complaint, mileage, fuel level, and ambient conditions. Initialize the chain-of-custody ledger as entry #0 (genesis), with its own hash. This is the consensus "term" — every later entry belongs to this case and chains from #0.

### Phase 1 — Replicate evidence into the log (`/ingest-scan`, `/log-evidence`)
**Before clearing anything**, pull Mode 02 freeze frame, Mode 03/07/0A DTCs, Mode 06 monitor results, and a Mode 01 live-data baseline; append each as an evidence node. Add hand-collected evidence (smoke test, scope traces, pressures) as it's gathered. Each append carries `prev-hash` so the log is tamper-evident.

### Phase 2 — Detect Byzantine nodes (`/cross-validate-sensors`)
For every sensor whose value you might rely on, find an independent cross-check (table below). A sensor that disagrees with its cross-check is flagged **Byzantine** — its data is quarantined as "evidence about the sensor," not accepted as fact. A sensor with no signal at all is flagged **crashed** and excluded.

### Phase 3 — Propose root cause + classify the DAG (`/classify-faults`)
From the surviving (faithful) evidence, name candidate root causes. Build the DTC causal DAG: identify the **leader** (root) code(s) and mark the rest as **followers** (consequences). Misfire → catalyst/lean/O₂ followers is the canonical pattern.

### Phase 4 — Build quorum (`/build-quorum`)
For the leading candidate, enumerate the *minimum independent corroborating tests* required to commit (its quorum set). Report quorum met, or list what's still missing. No single test is a quorum.

### Phase 5 — Resolve split-brain if needed (`/resolve-split`)
If two candidates both have partial support, do **not** repair both. Design the single decisive discriminating test whose result falsifies one branch; log it; the survivor proceeds.

### Phase 6 — Commit (`/commit-diagnosis`)
Only with quorum satisfied and no open Byzantine flag: append a *committed* diagnosis entry — root cause, supporting entry hashes, confidence, and the repair plan. This is the Raft "commit index" moving forward.

### Phase 7 — Repair and verify replication (`/verify-repair`)
After the repair, re-run the affected monitors to readiness over the OEM drive cycle, confirm the DTC does not return, and confirm trims/sensor behavior returned to band. Append the verification evidence. The fix isn't real until it "replicates."

### Phase 8 — Export custody (`/custody-report`)
Verify the hash chain end-to-end (no gaps, monotonic timestamps), then export the dossier for the owner, warranty, referee, or fleet audit.

## Decision Points (master)
- If a sensor fails cross-validation → flag Byzantine, exclude from quorum, and consider *the sensor* as a candidate root cause.
- If quorum cannot be reached → keep gathering evidence; never commit on a single input.
- If two causes tie → go to `/resolve-split`; do not "parts-cannon."
- If a request is to clear a code without a committed root cause → **refuse** (tampering / clear-to-pass).

## Cross-validation reference (Byzantine detection)

| Sensor / signal | Independent cross-check | "Lying" signature |
|---|---|---|
| MAF | MAP + RPM + VE → expected g/s; throttle-snap response | reads low at high load → false-lean trims |
| Upstream O₂ / wideband | Commanded vs actual λ; propane enrichment response | slow/biased switch → skewed fuel control |
| Downstream O₂ | Should be lazy if cat is good; check for exhaust leak ahead of it | active downstream + good front = leak fooling it, not a dead cat |
| ECT / IAT | Compare to ambient at cold soak; compare to each other | stuck-cold ECT → permanent open-loop enrichment |
| EGR flow (P0401) | Commanded position vs MAP change vs DPFE | code with no MAP response → flow path, not valve |
| Fuel pressure | Live PID vs mechanical gauge | PID disagreeing with gauge = the PID sensor lies |

## Per-DTC workflows

### P0420/P0430 — catalyst efficiency
1. Read **Mode 06** catalyst monitor (don't condemn on the P-code alone).
2. `/cross-validate-sensors`: rule out an **exhaust leak** ahead of the downstream O₂ and a **skewed upstream O₂**.
3. Watch front-vs-rear O₂ correlation at steady cruise — a good cat makes the rear lazy.
4. Quorum to commit "dead cat": Mode 06 fail + rear mirrors front (poor storage) + no exhaust leak + upstream O₂ proven faithful.

### P0171/P0174 — lean (one or both banks)
1. Both banks lean → fault upstream of the bank split (air/fuel global).
2. `/cross-validate-sensors`: MAF vs MAP-derived load (catch low MAF).
3. Quorum: trims + smoke-test for unmetered air + fuel-pressure/volume check. Localize by trim-vs-load pattern (idle-only = vacuum leak).

### P0442/P0455/P0456 — EVAP leak
1. Note fuel level (monitor won't run outside its window) and check the cap first (P0457).
2. Smoke test; log the *specific* leak location (photo).
3. Quorum: smoke-confirmed leak point + post-repair monitor pass. Small/very-small leaks (P0456) often need targeted smoke + soap.

### P0401/P0402/P0404 — EGR
1. Distinguish valve fault from passage restriction (carbon) — commanded position vs actual flow/MAP response.
2. Quorum: actuation test + flow evidence (MAP delta or DPFE) + visual/passage check.

### Diesel P2002 / P20EE — DPF / SCR
1. `/classify-faults`: a clogged DPF is usually a *follower* — find the leader (failed regen, EGR-cooler leak, dosing/DEF-quality fault).
2. Read soot-load estimate, regen history, NOx in/out, DEF quality.
3. Quorum: leader confirmed + downstream effect consistent; commit only the leader as root cause.
