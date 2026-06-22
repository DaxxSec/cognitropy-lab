# Pyrotechnics Choreography Timing Workspace

> Treat a fireworks show like a safety-critical timed system: model the cues, write the safety and music-sync constraints as proof obligations, and *discharge every one* — or get a counterexample.

## What This Workspace Does

A professional fireworks display is a real-time, safety-critical system that happens to be beautiful. Dozens to thousands of cues fire on a sub-second timeline; each aerial shell breaks seconds *after* its e-match fires; fallout drifts on the wind toward a crowd line; firing modules can only sink so much current at once; and the whole thing is supposed to land its accent effects on the beats of a music track. Designers usually reason about all of this informally, in show-design software, by eye. This workspace applies **formal-verification thinking** to that timeline.

The core idea is the **proof obligation**. Every safety rule ("no two live effects closer than their combined fallout radius", "magazine reload interval ≥ 0", "total runtime ≤ track length") and every artistic rule ("the finale's hero shells break within ±80 ms of the downbeat") becomes a named, labeled obligation in a specification catalog. The cue sheet is the model. The verifier walks the catalog and *discharges* each obligation — proving it holds against the schedule, or returning a concrete **counterexample** (which two cues collide, by how much, at what time). Nothing is "probably fine"; it is discharged, open, assumed, or refuted, and the **proof ledger** tracks the status across every revision of the show.

Today's technique is **decision-tree triage workflows**, which shows up in three places: the **weather gate** (a go/no-go tree over wind speed, wind direction vs. fallout geometry, and visibility), the **misfire triage** runbook (no-fire vs. low-break vs. hangfire → wait-time and safing decisions), and **constraint-violation triage** (when a proof fails, a tree decides whether to move the cue, drop the effect, re-rack, or relax the spec). The workspace is for **planning, verification, and documentation** by licensed operators — it never touches device chemistry or manufacture.

## Why This Workspace Exists

The failure modes in display choreography are timing failures: a cue that fires before the previous shell's fallout has cleared, an aerial accent that "looks" on-beat in the software but was never time-of-flight compensated so it actually breaks a half-second late, a finale chain that double-books an e-match channel, a runtime that overruns the music by four seconds. These are exactly the kind of bugs formal methods were invented to catch — interval overlaps, temporal constraints, resource budgets — yet show-design tools verify almost none of them automatically. This workspace codifies the constraints as machine-checkable obligations and the contingencies as explicit decision trees, so a show is *argued* safe and on-time, with a written, re-runnable record, rather than eyeballed.

## Getting Started

### Prerequisites

- A show concept and a **cue list / script** (from Finale 3D, ShowSim, Visual Show Director, FWsim, or a hand-built CSV): per-cue device, position/rack, effect, and nominal fire time.
- The **music track** with a beat/downbeat map (DAW marker export, `librosa`/`madmom` beat times, or hand-tapped markers) if the show is choreographed to music.
- A **site diagram**: firing positions, audience/spectator line, no-fire zones, and prevailing/forecast wind. Distances in feet or meters.
- The applicable **safety framework**: NFPA 1123 (outdoor display) or NFPA 1126 (proximate/indoor), your AHJ permit conditions, and product DOT/bore data sheets.
- *(Optional, for the rigorous path)* a model checker for timed systems — **UPPAAL**, **TLA+/TLC**, or an SMT solver (**Z3**) — if you want machine-checked rather than spreadsheet-checked obligations.

### Quick Start

1. Clone this workspace and drop your cue list, beat map, and site diagram into `context/` (or `outputs/raw/`).
2. Run `/cue-sheet-build` to normalize everything into the canonical timed cue model (fire time, break time, position, fallout radius, channel).
3. Run `/timing-spec` to generate the proof-obligation catalog for your safety framework and artistic goals.
4. Run `/verify-schedule` to discharge the catalog against the cue sheet; review the counterexamples it returns.
5. Triage failures with `/misfire-triage` / `/weather-gate` for contingencies and the constraint-violation tree for proof failures, then re-verify and snapshot the result with `/proof-ledger`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/cue-sheet-build` | Normalize a script + music map into the canonical timed cue model | First, before any verification — establishes the single source of truth |
| `/timing-spec` | Author the proof-obligation catalog (safety + artistic constraints, each labeled) | After the cue sheet exists; whenever the safety framework or artistic goals change |
| `/verify-schedule` | Discharge every obligation against the schedule; emit status + counterexample traces | After any cue-sheet edit; as the gate before sign-off |
| `/separation-proof` | Prove no two live effects violate spatial safety distance (geometry × time-overlap) | When the layout is dense or positions/wind change |
| `/rack-allocation` | Map effects to mortars/racks/firing-module channels; prove electrical feasibility | During hardware planning and before the finale chain is finalized |
| `/beat-sync-check` | Verify hero cues land within tolerance of beats, time-of-flight compensated | For music-choreographed segments and accent moments |
| `/misfire-triage` | Build the misfire / dud / hangfire decision-tree runbook | Before show day, as the operator's live contingency card |
| `/weather-gate` | Build the go/no-go weather decision tree from wind/fallout/visibility thresholds | During permitting and on show day at the weather call |
| `/proof-ledger` | Maintain the obligation ledger across revisions (discharged/open/assumed/refuted) | Every time the show changes — to keep the audit trail current |

## Directory Structure

```
pyrotechnics-choreography-timing/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 9 bespoke domain commands
├── context/
│   ├── concepts.md           # Effect taxonomy, time-of-flight, safety distances, formal-methods vocabulary
│   ├── workflows.md          # The verify loop + the three triage decision trees
│   └── references.md         # Bore→radius/ToF tables, NFPA/ATF standards, tool cheat-sheet
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Cue sheets, spec catalogs, verification reports, ledgers
```

## Example Use Cases

### Verifying a music-synchronized finale
A 90-second finale choreographed to a track has 200 cues. `/cue-sheet-build` ingests the export, `/beat-sync-check` confirms the 12 hero shells break within ±80 ms of their downbeats after time-of-flight compensation, and `/verify-schedule` proves no two finale racks fire within their combined fallout radius while still in the air.

### Proving a dense site is separation-safe under a wind shift
The site is tight and the forecast has the wind veering toward the crowd. `/separation-proof` re-runs the fallout geometry for the worst-case wind vector and returns a counterexample showing two comet positions whose drifted fallout overlaps the spectator line — before anything is loaded.

### Building the operator's live contingency card
`/misfire-triage` produces a one-page decision tree (no-fire → 5-minute wait → safing; low-break → hold downstream chain; hangfire → never approach, electrically safe the module) and `/weather-gate` produces the show-day go/no-go thresholds, both saved to `outputs/` for the shooter's clipboard.

## Recommended MCP Servers

- **Filesystem MCP** — read cue-list exports, beat-map CSVs, and site diagrams from disk and write verification reports back to `outputs/`.
- **Git MCP** — track each show revision so the proof ledger diffs cleanly and discharged obligations are tied to a specific cue-sheet commit.
- *(Optional)* a **shell/exec MCP** — to invoke an external model checker (UPPAAL/TLC) or an SMT solver (Z3) on the generated model and parse its counterexamples back into the ledger.

## Legal & Ethical Considerations

- **Licensed, permitted operation only.** This workspace assumes a licensed display operator (e.g. ATF Type 54 license/permit holder where applicable) firing commercially-manufactured devices under a permit issued by the Authority Having Jurisdiction. It is a planning and documentation aid, not an authorization to fire.
- **No formulation or manufacture.** Nothing here addresses energetic-material chemistry, device construction, or modification — and the agent will refuse such requests. The scope is timing, geometry, firing-system logistics, and verification.
- **Safety standards are the floor, not the ceiling.** NFPA 1123/1126 minimum distances and your permit conditions govern. A discharged obligation in this workspace is a *modeling* result; it never overrides the on-site judgment of the licensed operator or the AHJ.
- **Crowd safety dominates artistic intent.** When a separation, fallout, or weather obligation conflicts with a choreographic goal, the safety obligation wins and the cue is moved or cut.

## Technical References

- [NFPA 1123 — Code for Fireworks Display](https://www.nfpa.org/codes-and-standards/nfpa-1123-standard-development/1123) — outdoor display siting, separation, and operation.
- [NFPA 1126 — Pyrotechnics Before a Proximate Audience](https://www.nfpa.org/codes-and-standards/nfpa-1126-standard-development/1126) — indoor / close-proximity displays.
- [ATF — Explosives & Fireworks](https://www.atf.gov/explosives) — federal licensing/permit framework for display operators (U.S.).
- [UPPAAL — model checker for real-time systems](https://uppaal.org/) — timed automata; natural fit for cue-separation and runtime obligations.
- [TLA+ / TLC](https://lamport.azurewebsites.net/tla/tla.html) — temporal specification and bounded checking of the schedule model.
- [Signal Temporal Logic (STL) — overview](https://en.wikipedia.org/wiki/Signal_temporal_logic) — quantitative timed specs with robustness margins, useful for beat-sync tolerances.
- [librosa beat tracking](https://librosa.org/doc/latest/generated/librosa.beat.beat_track.html) / [madmom](https://github.com/CPJKU/madmom) — extract beat/downbeat times for the music map.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
