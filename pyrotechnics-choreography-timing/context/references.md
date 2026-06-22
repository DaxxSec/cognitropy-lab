# Pyrotechnics Choreography Timing — Reference Tables

Compact lookup data. All figures are **planning rules-of-thumb**; the AHJ permit, the product data sheet, and the governing NFPA standard always supersede. Verify against the actual device specs before relying on any number.

## Shell Bore → Separation, Apogee, Time-of-Flight (outdoor, NFPA 1123 planning rule-of-thumb)

| Bore | Min spectator distance (≈70 ft/in) | Approx apogee | Approx time-of-flight to break | Approx hang/descent |
|------|-----------------------------------|---------------|--------------------------------|----------------------|
| 3"   | ~210 ft (~64 m)  | ~250 ft  | ~2.3 s | ~3–4 s |
| 4"   | ~280 ft (~85 m)  | ~350 ft  | ~3.0 s | ~4–5 s |
| 5"   | ~350 ft (~107 m) | ~450 ft  | ~3.5 s | ~5 s   |
| 6"   | ~420 ft (~128 m) | ~600 ft  | ~4.0 s | ~6 s   |
| 8"   | ~560 ft (~171 m) | ~800 ft  | ~5.0 s | ~7 s   |
| 10"  | ~700 ft (~213 m) | ~1000 ft | ~5.6 s | ~8 s   |
| 12"  | ~840 ft (~256 m) | ~1200 ft | ~6.2 s | ~9 s   |

> ToF/apogee vary with lift charge, payload, and air density — treat as ±15%. Willows/long-hang shells extend descent by several seconds. Proximate (1126) devices use product-rated distances, **not** this table.

## Effect Class → Timing Profile

| Class | ToF | Live duration | Cueing note |
|---|---|---|---|
| Aerial shell | bore-dependent (above) | break + glitter tail | cue `t_fire = beat − tof` |
| Multishot cake | ~0 to first shot | internal-fused sequence | cue start only; internal timing fixed |
| Comet / single shot | 0.5–2 s | <1 s | crisp music accents |
| Mine / front | ~0 s | 1–3 s | ground-level; near-zero ToF |
| Gerb / fountain | ~0 s | 10–60 s | long-lived; one sustained cue |
| Set piece / lance | ignition spread | 30–120 s | model as one long interval |

## Sync Tolerance Bands (artistic, planning defaults)

| Cue role | Typical τ (sync window) | Rationale |
|---|---|---|
| Hero / downbeat accent | ±50–80 ms | perceptible misalignment threshold |
| Phrase / bar marker | ±150 ms | looser; rhythmic feel |
| Ambient / wash | ±300 ms+ | not beat-locked |

## Firing-System Quick Facts

| Item | Planning note |
|---|---|
| E-match | one-shot; one cue per pin (parallel only within current limit) |
| Module current budget | each module has a max **simultaneous** e-match count — check `K ≤ max_simultaneous` per settle window |
| Time code | SMPTE or internal clock locks pyro/audio/lighting to a shared T0 |
| Continuity test | pre-show check that every channel reads connected — separate from the *timing* model |
| Finale chains | many tubes paralleled on few channels → CURR + CHAN + SEP all bind at once |

## Standards & Regulatory Anchors (U.S.; check local equivalents elsewhere)

- **NFPA 1123** — Code for Fireworks Display (outdoor): siting, spectator separation, conduct of display.
- **NFPA 1126** — Use of Pyrotechnics Before a Proximate Audience (indoor/close): product-rated distances, overhead clearance, indoor air.
- **NFPA 1124** — manufacture/transport/storage (context only; out of scope for this planning workspace).
- **ATF (27 CFR Part 555)** — federal explosives licensing/permits for display operators.
- **DOT / UN classification** — 1.3G (display) vs 1.4G (consumer) shipping class on device sheets.
- **AHJ permit** — the local Authority Having Jurisdiction's conditions; **always the controlling document**.

## Formal-Methods Tool Cheat-Sheet

| Tool | Model fit | Use it for |
|---|---|---|
| **UPPAAL** | timed automata, real-valued clocks | native cue-separation / reuse / runtime as clock invariants; counterexample traces |
| **TLA+ / TLC** | discrete-time state machine + temporal logic | bounded check of the schedule; clear spec language for obligations |
| **Z3 / SMT** | constraints over reals + intervals | encode SEP geometry + time overlap as `unsat ⇒ safe`; min-margin via optimization |
| **NuSMV / nuXmv** | symbolic model checking, LTL/CTL | invariant (DENSITY, CHAN) checks on a discretized timeline |
| **Alloy** | relational, bounded | channel/rack allocation feasibility (CHAN, CURR) as a finite assignment problem |

### STL/MTL operators (for SYNC, RUNTIME, robustness margins)

| Operator | Meaning | Example obligation |
|---|---|---|
| `G φ` (globally) | φ holds at all times | `G (live_pairs ⇒ footprint_disjoint)` (SEP) |
| `F[a,b] φ` (eventually-in) | φ within window [a,b] | hero cue effect within `F[b−τ, b+τ]` of beat (SYNC) |
| `φ U ψ` (until) | φ until ψ | position stays cleared until next fire (REUSE) |
| robustness ρ | signed margin to satisfaction | "+1.4 s slack on the tightest SEP pair" |

## Show-Design & Audio Tooling (for the music map)

- **Finale 3D / FWsim / Visual Show Director / ShowSim** — commercial show designers; export cue lists (confirm fire-vs-effect time column).
- **librosa** `beat_track` / **madmom** `DBNDownBeatTracking` — extract beat & downbeat times for `/beat-sync-check`.
- **DAW marker export** (Reaper/Logic/Ableton) — hand-placed hero-beat markers as CSV.

## Upstream Catalogues & Further Reading

- **NFPA codes portal** — https://www.nfpa.org/ — 1123 / 1126 full text & handbooks.
- **ATF Explosives** — https://www.atf.gov/explosives — licensing, permits, federal rules.
- **UPPAAL** — https://uppaal.org/ — timed-automata model checker + tutorials.
- **Learn TLA+** — https://learntla.com/ — practical temporal specification.
- **Z3 guide** — https://microsoft.github.io/z3guide/ — SMT encoding patterns.
- **PGI (Pyrotechnics Guild International)** — https://www.pgi.org/ — display community, safety culture.
