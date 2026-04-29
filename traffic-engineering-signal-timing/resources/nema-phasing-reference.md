# NEMA TS-2 Ring-and-Barrier Reference

> Source: NEMA TS-2 (2021 revision); FHWA Signal Timing Manual 2nd Ed. (2015); ITE Traffic Engineering Handbook 7th Ed.

## Standard 8-Phase Layout

```
                Major Street                    Minor Street
                (NS)                            (EW)
              ┌──────────┐                    ┌──────────┐
Ring 1:       │ φ1 NB-LT │  φ2 SB-TH+RT       │ φ3 EB-LT │  φ4 WB-TH+RT
              │          │                    │          │
Ring 2:       │ φ5 SB-LT │  φ6 NB-TH+RT       │ φ7 WB-LT │  φ8 EB-TH+RT
              └──────────┘                    └──────────┘
                              ^Barrier 1^                       ^Barrier 2^
```

## Phase Definitions
- **Phase 1 (NB-LT):** Northbound left-turn. Protected.
- **Phase 2 (SB-TH+RT):** Southbound through + right.
- **Phase 3 (EB-LT):** Eastbound left-turn. Protected.
- **Phase 4 (WB-TH+RT):** Westbound through + right.
- **Phase 5 (SB-LT):** Southbound left-turn. Protected.
- **Phase 6 (NB-TH+RT):** Northbound through + right.
- **Phase 7 (WB-LT):** Westbound left-turn. Protected.
- **Phase 8 (EB-TH+RT):** Eastbound through + right.

## Compatibility Rules
- Within a ring, phases must run sequentially (no two phases at once).
- Across rings, only "compatible" phase pairs may run concurrently.
- Both rings must reach a barrier together before either can cross to the next pair of phases.

### Compatible Pairs (concurrent)
| Ring 1 | Ring 2 |
|--------|--------|
| φ1 (NB-LT) | φ5 (SB-LT) |
| φ1 (NB-LT) | φ6 (NB-TH+RT) |
| φ2 (SB-TH+RT) | φ5 (SB-LT) |
| φ2 (SB-TH+RT) | φ6 (NB-TH+RT) |
| φ3 (EB-LT) | φ7 (WB-LT) |
| φ3 (EB-LT) | φ8 (EB-TH+RT) |
| φ4 (WB-TH+RT) | φ7 (WB-LT) |
| φ4 (WB-TH+RT) | φ8 (EB-TH+RT) |

## Phase Sequence Variants

### Lead-Lead
Both lefts (φ1 and φ5) start before their through phases.
- Use when left-turn volumes are heavy from both directions.
- Reduces opposing through capacity slightly.

### Lag-Lag
Both lefts run after their through phases.
- Useful with permitted-left flashing yellow arrow upstream.
- Improves coordination on the through movement.

### Lead-Lag (Asymmetric)
One left leads, opposing left lags.
- Common when one direction needs to release a queue first.
- Watch for yellow trap — protect with FYA or split-phase.

### Yellow Trap
A condition in lead-lag or permitted-protected operation where a permitted left-turn driver sees yellow on the through indication, assumes opposing through has yellow too, and turns into oncoming traffic that still has green. Mitigate with **FYA (Flashing Yellow Arrow)** or a **dallas display**.

## Pedestrian Phase Mapping

Pedestrian movements are typically tied to the parallel through phase:
- Ped 2: parallel to φ2 (south side crossing)
- Ped 4: parallel to φ4 (west side crossing)
- Ped 6: parallel to φ6 (north side crossing)
- Ped 8: parallel to φ8 (east side crossing)

The associated through phase must be ≥ walk + flashing-don't-walk + buffer.

## Special Phases
- **Phase 9–16:** Available in 16-phase or "8 + 8" configurations for split-phase intersections, T-intersections, channelized rights with separate signal heads, transit-only phases.
- **Preempt 1–6:** Rail, EVP (Emergency Vehicle Preemption), TSP. Override normal cycle entirely.
- **Overlap A–D:** "Tag along" phases that run concurrently with multiple parent phases (e.g., right-turn overlap with adjacent through + opposing left).

## Common Diagrams

### Standard 8-Phase Sequence (Lead-Lag, NS Coordinated)
```
   |φ1+φ5|--φ2+φ6 (coord)--|------BAR1------|φ3+φ7|--φ4+φ8--|------BAR2------|
        ^lead lefts        ^through                ^lead lefts ^through
```

### Permitted-Protected (FYA)
```
   |φ1 protected NB-LT|--φ2 + permitted NB-LT (FYA)--|---BAR---|...
```

## NTCIP 1202 v03A Reference
Key objects for remote signal management:
- `phaseMin` (1.3.6.1.4.1.1206.4.2.1.1.2.1.4) — minimum green per phase
- `phaseMax1` — maximum green
- `phaseYellowChange` — yellow interval
- `phaseRedClear` — red clearance interval
- `phaseWalk` — walk interval
- `phasePedestrianClear` — flashing-don't-walk interval
- `coordPattern` — active coordination pattern
- `coordCycle` — current cycle length
- `coordOffset` — offset
