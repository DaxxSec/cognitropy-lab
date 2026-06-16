# Emissions System Troubleshooting — Reference Tables

Lookup data the agent reaches for during a case. Compact by design — defer to OEM service info and the standards for fuller specs.

## DTC quick table (common emissions codes)

| DTC | Meaning | First-look diagnostic |
|---|---|---|
| P0420 / P0430 | Catalyst efficiency below threshold (B1/B2) | Mode 06 cat monitor; front-vs-rear O₂; rule out exhaust leak |
| P0171 / P0174 | System too lean (B1/B2) | LTFT pattern; MAF-vs-MAP; smoke test; fuel pressure |
| P0172 / P0175 | System too rich (B1/B2) | Negative trims; fuel pressure; leaking injector; MAF high |
| P0101 | MAF range/performance | MAF g/s vs expected from VE/MAP |
| P0131–P0167 | O₂/A-F sensor (low/high/slow/heater) | Switch rate, λ command-vs-actual, heater circuit |
| P0401 / P0402 / P0404 | EGR insufficient / excessive / range | Commanded vs actual flow; MAP response; carbon |
| P0440 / P0442 / P0455 / P0456 | EVAP general / small / large / very-small leak | Cap first; smoke test; fuel-level window |
| P0457 | EVAP leak — loose/missing cap | Inspect & reseat cap; re-run monitor |
| P0410 | Secondary air injection | Pump/valve actuation; flow |
| P0300+P03xx | Random / cylinder-specific misfire | Often the **leader** behind cat/lean/O₂ followers |
| P2002 | DPF efficiency below threshold (diesel) | Soot load; regen history; ΔP |
| P20EE | SCR NOx catalyst efficiency (diesel) | NOx in/out; DEF quality & dosing |

## OBD-II service modes (evidence sources)

| Mode | Content | Use as evidence |
|---|---|---|
| 01 | Live data / current PIDs | Baseline trims, sensor values, load |
| 02 | Freeze frame | Conditions at the moment the DTC set — log before clearing |
| 03 | Stored DTCs | Confirmed faults |
| 06 | On-board monitor test results (TID/MID) | Numbers behind P0420 etc. |
| 07 | Pending DTCs | Faults seen once, not yet matured |
| 0A | Permanent DTCs | Can't be cleared by battery pull — the system's "committed" failures |

## Fuel-trim interpretation cheat-sheet

| Observation | Reading | Likely direction |
|---|---|---|
| LTFT > +10% | ECU adding fuel | Lean: unmetered air / low fuel delivery / MAF reads low |
| LTFT < −10% | ECU pulling fuel | Rich: high fuel pressure / leaking injector / MAF reads high |
| Lean at idle only | Trim drops with load | Vacuum/intake leak |
| Lean across all loads | Flat positive trim | Fueling or MAF (global) |
| Rich at idle only | Negative idle trim | Leaking injector / dripping |
| Normal band | ±5% | No fueling root cause |

- Stoichiometric λ=1 ≈ 14.7:1 AFR (gasoline). Closed-loop targets λ=1; open-loop (cold/WOT) ignores O₂.

## Readiness monitors & drive cycle

- Continuous monitors: misfire, fuel system, comprehensive components (run whenever conditions allow).
- Non-continuous: catalyst, EVAP, O₂, O₂ heater, EGR, secondary air — each has an *enabling-conditions window* (temp, speed, fuel level, soak time).
- After a repair, a generic drive cycle: cold start → idle → steady cruise 25–40 mph → highway cruise → decel → repeat; many monitors need a full warm/cool cycle. Always prefer the **OEM-specific** drive cycle.
- EVAP monitors typically need fuel level ~15–85% and a cold soak — note this before chasing an "intermittent" evap code.

## Consensus-algorithm reference (imported model)

| Concept | Rule of thumb |
|---|---|
| Quorum (majority) | Need > N/2 independent witnesses to commit |
| Byzantine tolerance (PBFT) | `3f+1` nodes tolerate `f` liars → cross-check, don't trust one |
| Crash vs Byzantine | Dead (no signal) is easy; alive-and-wrong is the danger |
| Leader / log / commit | Raft: one leader, append-only log, commit on quorum ack |
| Split-brain | Two leaders → need a witness/fence to break the tie |
| Log matching | Each entry consistent with predecessor → hash-link the ledger |

## Upstream Catalogues & Standards

- **SAE J1979 / ISO 15031-5** — https://www.sae.org/standards/content/j1979_201702/ — OBD-II services & PIDs.
- **SAE J2012 / ISO 15031-6** — https://www.sae.org/standards/content/j2012_201612/ — DTC definitions dictionary.
- **ISO 15765 (CAN diagnostics)** — https://www.iso.org/standard/66574.html — the bus the nodes talk over.
- **EPA air enforcement / anti-tampering** — https://www.epa.gov/enforcement/air-enforcement — the legal boundary.
- **CARB OBD-II program** — https://ww2.arb.ca.gov/our-work/programs/on-board-diagnostics-program — monitor requirements & referee.
- **Raft (raft.github.io)** — https://raft.github.io/ — append-only log + leader election reference.

## Tooling cheat-sheet

- Bidirectional/enhanced scan tool with **Mode 06** + live graphing (J2534 pass-thru + OEM SW preferred).
- Smoke machine (EVAP/intake), lab scope or graphing meter, fuel-pressure gauge, gas analyzer (tailpipe ground-truth).
