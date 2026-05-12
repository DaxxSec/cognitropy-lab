# Domain Knowledge — Traffic Signal Timing with Environmental Impact Assessment

## 1. Signal Timing Fundamentals

### Cycle, Splits, Phases, Offsets — The Four Knobs
- **Cycle length (C):** total time for the controller to serve every phase once. Typical urban range 60–120 s; downtown grids may run as low as 50 s; freeway interchanges may run 150–180 s.
- **Phase split (g_i):** time allocated to phase *i* (green + yellow + red clearance). Splits must sum to C in each ring.
- **Offset:** time difference between the start of a coordinated phase at one intersection and the next, used to build a green wave.
- **Phase sequence:** order in which phases are served (lead-lead, lead-lag, lag-lag for left turns).

### NEMA TS-2 Ring-and-Barrier
The standard 8-phase dual-ring layout:

```
Ring 1:   φ1 (NB-LT)  φ2 (SB-TH+RT)   ||   φ3 (EB-LT)  φ4 (WB-TH+RT)
Ring 2:   φ5 (SB-LT)  φ6 (NB-TH+RT)   ||   φ7 (WB-LT)  φ8 (EB-TH+RT)
                              ^barrier^
```

- **Barrier:** point in the cycle where conflicting movements (NS vs EW) are exchanged. Both rings must reach the barrier together.
- **Concurrent phases:** φ1+φ6 (north-south leading lefts), φ2+φ5 (north-south through with leading SB left), etc.
- **Permitted vs. protected:** protected has its own phase; permitted runs on a circular green with FYA (flashing yellow arrow) or solid green.

### Saturation Flow Rate (s)
HCM 7 base saturation flow rate: **s_o = 1900 vphgpl** (vehicles per hour of green per lane). Adjusted via:
```
s = s_o * f_w * f_HV * f_g * f_p * f_bb * f_a * f_LU * f_LT * f_RT * f_Lpb * f_Rpb
```
Where (HCM 7 Eq. 19-8):
- `f_w`: lane width (1.0 at 12 ft, 0.96 at 11 ft, 0.92 at 10 ft)
- `f_HV`: heavy-vehicle adjustment = 100 / (100 + %HV * (E_T - 1)), with E_T = 2.0 typical
- `f_g`: grade = 1 - %grade/200
- `f_p`: parking activity (1.0 if no on-street parking)
- `f_bb`: bus blockage adjustment
- `f_a`: area type (0.90 in CBD)
- `f_LU`: lane utilization
- `f_LT`, `f_RT`: turn-movement adjustments
- `f_Lpb`, `f_Rpb`: pedestrian/bicycle conflict adjustments

### Critical Lane Volume (CLV) and Webster
- **Flow ratio:** y_i = v_i / s_i for each critical lane group
- **Webster's optimal cycle:**
  ```
  C* = (1.5 * L + 5) / (1 - sum(y_i))
  ```
  where L = total lost time per cycle (typically 4 s per critical phase).
- **Akcelik refinement:** for v/c > 0.85, add overflow-delay term to the second term of HCM Eq. 19-22.
- **Practical floor / ceiling:** if `1 - sum(y_i) < 0` the intersection is over capacity — adding cycle won't help; a geometric or demand-management fix is required.

### Levels of Service (HCM 7 Exhibit 19-8)
Based on per-vehicle control delay (s/veh):

| LOS | Delay (s/veh) | Qualitative |
|-----|---------------|-------------|
| A | ≤ 10 | Free flow, very few stops |
| B | 10–20 | Reasonable progression |
| C | 20–35 | Higher delay, more stops |
| D | 35–55 | Noticeable delay, congested |
| E | 55–80 | At capacity, unstable |
| F | > 80 | Over capacity, queue spillback |

## 2. Environmental Impacts of Signal Operations

### Vehicle Emission Mechanisms
- **Cold-start emissions:** dominant for trips < 2 mi; not under signal-timing control.
- **Idle emissions:** stopped at red, ~0.5–1.0 g/s CO, ~0.05 g/s NOx for a typical LDV (varies by model year).
- **Acceleration emissions:** 5–10× cruise rate for NOx; dominant signal-related impact.
- **Cruise emissions:** baseline; minimized when vehicle never has to decelerate-stop-accelerate.

### Pollutants of Interest
| Pollutant | Source | Control Lever |
|-----------|--------|---------------|
| CO | Incomplete combustion (worst at idle/cold) | Reduce stops, reduce idle time |
| NOx | High-temperature combustion (worst at acceleration) | Smooth flow, eco-driving |
| VOC / HC | Evaporative + tailpipe | Reduce engine-on time |
| PM2.5 (tailpipe) | Diesel + GDI direct injection | Smooth flow, modal cycle |
| PM2.5 (non-tailpipe) | Brake/tire wear, road dust | Reduce braking events |
| CO2 / CO2-eq | Fuel combustion (proportional to fuel use) | Minimize fuel ≈ minimize stops + idle |
| Black carbon | Diesel combustion | Smooth heavy-vehicle flow |
| Noise (Leq) | Engine + tire-road + acceleration | Avoid stop-and-go, manage truck % |

### EPA MOVES4 (2024)
- **Scale:** project, county, national.
- **Inputs:** roadway link geometry, source-type population (LDV/LDT/SU/CombT/Bus/MC × model year × fuel type), drive-schedule (link-average speed + idle/operating fraction), meteorology (T, RH).
- **Outputs:** mass emissions (g/hr) per pollutant per source-type per process (running, start, idle, evap).
- **For signal projects:** use the **project-level** scale with link drive-schedules derived from microsimulation second-by-second speed traces.
- **SIP-grade requirement:** MOVES is the only EPA-approved tool outside California (CARB-approved EMFAC for CA). Always re-run on finalist plans for the official deliverable.

### CMEM (Comprehensive Modal Emissions Model)
- **Resolution:** second-by-second, modal (idle / cruise / accel / decel) by engine load.
- **Speed:** ~1000× faster than MOVES for inner-loop optimization use.
- **Calibration:** 30+ vehicle categories with regression coefficients on tractive power.
- **Use here:** evaluate Pareto candidates fast; finalists go to MOVES.

### Approximate Emission Sensitivity to Signal Decisions
Rules of thumb from FHWA/NCHRP synthesis:

| Change | Typical Delay Δ | Typical CO2 Δ | Typical NOx Δ |
|--------|-----------------|---------------|---------------|
| –10 s cycle (over-cycled corridor) | –8 to –12% | –3 to –6% | –2 to –4% |
| Re-coordinate offsets (was uncoordinated) | –15 to –30% | –10 to –20% | –8 to –15% |
| Add adaptive control (SCATS/SCOOT) | –10 to –20% | –5 to –12% | –4 to –10% |
| Aggressive cycle reduction (under-cycled) | +30%+ | +10 to +20% | +8 to +15% |

These sign-conventions are why **delay reduction is necessary but not sufficient** — over-cycle reduction can paradoxically save delay locally while increasing emissions corridor-wide if it pushes more queues onto cross streets.

## 3. Coordination & Bandwidth

### Time-Space Diagrams
Plot each intersection's coordinated-phase green window on a time × distance diagram. The "band" is the parallelogram of green-on-green time available for a vehicle traveling at the design speed. Bandwidth (BW) is measured in seconds.

### Maximum Bandwidth (Maxband / Multiband)
- **Maxband (Little, 1981):** mixed-integer LP that finds offsets maximizing the smaller of inbound/outbound bands.
- **Multiband (Gartner, 1991):** weights each link's band by directional volume.
- **PASSER, TRANSYT-7F, Synchro CycleLength Optimizer:** practical implementations.

### Eco-Weighted Coordination
Augment the objective:
```
maximize  sum_d  (vol_d * BW_d) - alpha * sum_d (vol_d * stops_d * CO2_per_stop)
```
where `alpha` translates kg-CO2 to seconds of delay (the social cost of carbon). Typical values: USEPA SC-CO2 (2024 update) ~$190/t-CO2, with VOT ~$20/hr → α ≈ 9.5e-3 s/g.

### Design Speed for Green Wave
Field studies (Barth & Boriboonsomsin, 2009) show CO2 minimization on 30–35 mph arterials sits at ~5–7 mph **below** the posted speed because the lower target reduces deceleration severity.

## 4. Pedestrian, Bicycle, and Transit Considerations

### Pedestrian Walk + Clearance
- Walk: 7 s preferred / 4 s minimum (MUTCD 2009 §4E.06)
- Clearance (FDW): crossing distance / walk speed (3.5 ft/s standard, 3.0 ft/s for slower pedestrians)
- Total = walk + FDW. The phase serving the parallel through movement must be at least this long (minus the buffer interval).

### Bicycle Minimum Green
NACTO recommends:
- Minimum green ≥ 7 s + (intersection_width / 14.7 ft/s)
- Bicycle clearance interval if dedicated bike phase

### Transit Signal Priority (TSP)
- **Green extension:** stretch active green up to a configured limit (often 5–10 s) when an approaching transit vehicle is detected.
- **Early green:** serve coordinated phase early when transit is queued, transferring time from cross-street.
- **NTCIP 1211 v02:** standard for SP messaging.
- **Emissions trade-off:** bus saves engine-on time and avoids deceleration cycle (~5 kg CO2/event for a 40-ft diesel bus); cross-street vehicles incur added stops. Net is usually positive when bus is loaded but must be modeled per corridor.

## 5. Adaptive Signal Control

| System | Vendor / Origin | Approach | Maturity |
|--------|-----------------|----------|----------|
| SCOOT | TRL (UK) | Cycle-by-cycle split + offset tuning from upstream loop | Mature, 1980s |
| SCATS | RMS NSW (AU) | Library plan selection + fine adjustment | Mature, 1980s |
| ACS-Lite | FHWA / Siemens | Time-of-day plan tuning, requires existing coordination | US-focused |
| InSync | Rhythm Eng. (Cubic) | Cycle-free, demand-responsive | 2010s |
| Surtrac | CMU spinout | Decentralized scheduling, AI-based | 2010s, smaller deployments |
| MaxView/Centracs | Q-Free / Econolite | Centralized adaptive overlays | Vendor-specific |

Signal timing remains valuable even with adaptive — the underlying time-of-day plan is the floor the adaptive algorithm modulates around.

## 6. Performance Measures / ATSPM

ATSPM (Automated Traffic Signal Performance Measures) — UDOT origin, now widely deployed.

### Core Metrics
- **Purdue Coordination Diagram (PCD):** scatterplot of arrival time vs. green start; shows platoon arrival on green.
- **Approach Volume:** ATSPM-derived volumes from detector events.
- **Split Monitor:** programmed vs. actual phase duration distribution.
- **Yellow + Red Actuations:** safety surrogate (red-light running).
- **Pedestrian Delay:** time from pedestrian call to walk indication.
- **Arrivals on Green (AOG):** primary coordination quality KPI; aim for > 80% on coordinated phases.

### High-Resolution Event Logs (10-Hz)
NEMA / NTCIP event codes used by ATSPM:
- 0–10: phase begin/end events
- 21–24: pedestrian events
- 81–82: detector on/off
- 90–91: split monitoring

## 7. Common Failure Modes / Pitfalls

1. **Over-cycling.** Long cycles "look efficient" because they reduce lost time, but inflate per-vehicle delay and pedestrian frustration. Watch v/c — if all v/c < 0.7 and cycle > 110 s, shrink the cycle.
2. **Coordinating where you shouldn't.** Coordination needs adjacent intersections within ~0.5 mi and similar cycle length. Forcing coordination across a discontinuity yields negative emissions impact.
3. **Permitted lefts that should be protected.** High left-turn volume + sight distance issues = crashes and emissions both worsen. Run the HCM 7 left-turn warrant.
4. **Stripping pedestrian time to hit a delay number.** Statutory minimums; also creates ADA liability.
5. **Reporting MOVES at network average speed.** MOVES is sensitive to drive cycle, not just average — use link-level second-by-second.
6. **Forgetting evap / cold start.** These are large but not under signal control. Don't let them drown the running-emissions delta in your report.
7. **Year-stale MOVES inputs.** Source-type populations and rates update each MOVES release; using MOVES2014 in 2026 understates LDV NOx by ~20%.
8. **Ignoring saturation under-flow.** Bottleneck downstream = your beautiful green wave is delivering vehicles into a queue. Always check downstream capacity before sizing offsets.

## 8. Standards & Regulatory Reference

- **HCM 7th Edition (TRB, 2022)** — Chapter 19 (signalized) and Chapter 23 (corridor)
- **MUTCD (FHWA, 2023 Edition)** — Chapter 4 Highway Traffic Signals
- **ITE Traffic Engineering Handbook, 7th Ed.** — practitioner reference
- **FHWA Signal Timing Manual, 2nd Ed. (2015)** — methodology
- **NEMA TS-2 (2021 revision)** — controller hardware/firmware
- **NTCIP 1202 v03A (2019)** — actuated controller objects (ASC)
- **NTCIP 1211 v02** — Signal Control & Prioritization (SCP)
- **EPA MOVES4 (2024)** — mobile-source emissions model (federal)
- **CARB EMFAC2021** — California-only equivalent
- **40 CFR Part 93 Subpart B** — transportation conformity
- **23 CFR 771.117(c)(28)** — NEPA Categorical Exclusion for ITS/operations
- **AASHTO Green Book (7th Ed.)** — geometry context
- **NACTO Urban Street Design Guide** — multimodal context
