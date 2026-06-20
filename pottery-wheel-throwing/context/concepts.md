# Pottery Wheel Throwing — Core Concepts

Background the agent reads before acting on studio-flow, kiln, or footprint tasks. Three lenses braided together: the **craft** (throwing), the **method** (traffic signal timing), and the **technique** (environmental impact assessment). Optimised for fast recall.

## The throwing-to-fired-ware pipeline

A piece passes through serial stages, each with a characteristic duration and a different process type (continuous skilled labor vs. passive wait vs. batch firing):

| Stage | What happens | Process type | Typical time (mug-scale) |
|---|---|---|---|
| Wedging / prep | De-air and homogenize clay | Setup / changeover (lost time) | 2–5 min/batch |
| Centering | Cone the clay true on the wheel | Skilled, serial | 1–3 min |
| Opening + pulling | Open the floor, pull the walls up | Skilled, serial | 3–8 min |
| Shaping + finishing | Form, rib, trim foot lip, wire off | Skilled, serial | 2–5 min |
| Drying to leather-hard | Stiffen enough to handle/trim | Passive wait (queue) | 6–24 h |
| Trimming | Turn the foot, refine profile | Skilled, serial | 2–6 min |
| Drying to bone-dry | Drive off remaining water | Passive wait (queue) | 1–7 days |
| **Bisque firing** | First firing, ~cone 06–04 | **Batch server** | 8–12 h + cool |
| Glazing | Dip/spray/brush glaze | Skilled, serial | 1–4 min |
| **Glaze firing** | Final firing, cone 6 (mid) or 10 (high) | **Batch server** | 8–14 h + cool |

The two **batch servers** (the kilns) are the crux. Everything upstream is either skilled serial work (rate-limited by the potter) or passive drying (rate-limited by physics and humidity). The kiln is rate-limited by *capacity per cycle × cycles per period* — which is precisely a signalized server.

## The traffic-signal-timing mapping (the method)

This is the workspace's engine. Each traffic concept has an exact studio analog:

| Traffic signal timing | Pottery studio analog |
|---|---|
| Signalized intersection | A processing stage (wheel bank, drying area, kiln) |
| Signal cycle | One production cycle (throw → dry → trim → bisque → glaze → glaze-fire) |
| Movement / approach | A product line competing for shared capacity |
| Green time (g) | Active time/capacity given to a line or firing type |
| Phase split | How total capacity is divided among competing lines |
| Lost time (L) | Wedging, wheel cleanup, kiln load/unload, changeover |
| Saturation flow rate (s) | Max pieces/hour a stage clears under ideal, uninterrupted conditions |
| Capacity (c = s·g/C) | Practical throughput of a stage given its share of the cycle |
| Degree of saturation (X = v/c) | Demand ÷ capacity; X > 1 means a backlog grows every cycle |
| Queue / stopped delay | Greenware waiting for the kiln; pots waiting to be trimmed |
| Offset | Time lag between when one stage finishes and the next begins |
| Coordination / "green wave" | Tuning offsets so a batch never waits between stages |
| Level of Service (LOS A–F) | A grade for how congested the pipeline is |
| Actuated control | Demand-responsive firing: fire when the kiln is full, not on a fixed clock |
| Oversaturation | The bottleneck stage (nearly always the kiln) where demand exceeds capacity |

### Webster's optimal cycle length

For a signal (and, here, for a studio's batch cadence):

```
C₀ = (1.5·L + 5) / (1 − Y)
```

- `C₀` = optimal cycle length (seconds for a signal; here, the natural unit is a *firing cycle* or a *production day*).
- `L` = total lost time per cycle (sum of changeover/load/unload times not doing productive work).
- `Y` = Σ yᵢ = sum of the *critical flow ratios* across competing movements, where `yᵢ = qᵢ / sᵢ` (demand ÷ saturation flow for line i).
- Valid only while `Y < 1`. If `Y ≥ 1` the system is oversaturated and no cycle length helps — you must add capacity (a second kiln) or shed demand.

The studio translation: when changeover time (`L`) is high — a kiln that takes hours to load and unload — longer cycles (bigger, less frequent firings) are optimal, because the fixed lost time is amortized over more work. This is *the same reason* big infrequent firings cut per-piece energy.

### Saturation flow and delay

- **Saturation flow rate** `s`: the HCM baseline for traffic is ~1900 passenger cars / hour of green / lane, adjusted by factors. The studio analog is measured directly — e.g. "this kiln fires 30 mugs per 20-hour cycle ⇒ s ≈ 1.5 mugs/h of firing capacity."
- **Webster's average delay per arrival** (lightly loaded, isolated server):

```
d = C(1−λ)² / [2(1−λ·X)]  +  X² / [2q(1−X)]
```

where `λ = g/C` (green ratio), `X = v/c` (degree of saturation), `q` = arrival rate. The first term is uniform delay, the second is overflow delay that blows up as `X → 1`. The studio reading: as the kiln approaches saturation, the *wait* for greenware grows nonlinearly — the last 10% of utilization costs the most delay.

## The kiln as a signalized batch server (the keystone)

A kiln does not process continuously; it accumulates a queue (a kiln-load of greenware) and discharges it in one firing "green phase." Key parameters:

- **Service capacity per cycle** = pieces that fit (see `/kiln-load-density`). This is the studio's saturation flow.
- **Cycle time** = load + ramp + soak + cool + unload. Cooling is unproductive lost time but unavoidable.
- **Utilization** = average load ÷ maximum load. A half-full firing runs the cycle at 50% utilization for ~100% of the energy.

Because the kiln dominates both throughput (it is the slowest server) and footprint (it is the energy sink), **load density is the master variable**. Raising it raises capacity *and* lowers per-piece energy with a single action — the convergence this workspace is built around.

## Environmental impact assessment for ceramics (the technique)

Per ISO 14040/14044, an EIA/LCA needs a **functional unit** ("one finished 350 ml mug, food-safe") and a **system boundary** (cradle-to-gate = raw clay extraction → finished ware at the studio door; gate-to-gate = studio operations only). The inventory (LCI) for studio ceramics:

| Flow | Where it enters | Typical share of cradle-to-gate energy |
|---|---|---|
| **Firing energy** | Bisque + glaze firings | **~60–90 %** (the hotspot) |
| Clay body | Mass thrown minus reclaim losses | material + embodied extraction energy |
| Water | Throwing, glazing, cleanup | local, but matters in water-stressed regions |
| Glaze materials | Dipping/spraying losses + toxicity | small mass, high hazard weight |
| Transport | Materials in, ware out | varies; often secondary to firing |

**The dominant finding for nearly every studio ceramics LCA is the same: the kiln is the footprint.** Therefore environmental optimization and throughput optimization share a lever (kiln load density and fewer, fuller firings) — they are not in tension.

### Aleatoric vs. addressable impact

- **Addressable** — load density, firing schedule, electric vs. gas, off-peak firing, glaze choice, reclaim rate. These respond to the methods in `workflows.md`.
- **Structural** — grid CO₂e intensity, the thermodynamic minimum to vitrify clay, cone temperature required by the body. These bound what optimization can achieve; name them so claims stay honest.

## Common Failure Modes

**Craft / process:**
- **S-cracks** — uncentered or under-compressed floor; cracks in the base after drying.
- **Off-center trimming** — re-centering error at the trimming stage wastes the foot.
- **Over/underfiring** — wrong cone or ramp; underfired ware is porous and unsafe for food.
- **Glaze defects** — crawling, pinholing, shivering, crazing; often a glaze-fit or application-thickness issue.

**Flow / scheduling:**
- **Misdiagnosed bottleneck** — adding wheels when the kiln is the constraint (the most common and most expensive mistake; `/bottleneck-delay-analysis` exists to prevent it).
- **Firing half-empty kilns** — running the cycle at low utilization to "keep things moving" — destroys both throughput and footprint.
- **Uncoordinated offsets** — a batch finishes throwing days before the kiln has a slot, so greenware queues and risks damage.

**Footprint:**
- **Boundary creep / unit drift** — comparing a gate-to-gate number to a cradle-to-gate one, or changing the functional unit mid-assessment, making claims meaningless.
- **Ignoring glaze hazard mass** — treating a 2 % cadmium stain as negligible because its mass is small, while it dominates the toxicity dimension.

## Operating Constraints

- **Cone temperatures** (Orton, self-supporting, 108 °F/hr final ramp): cone 06 ≈ 999 °C, cone 04 ≈ 1060 °C, cone 6 ≈ 1222 °C, cone 10 ≈ 1285 °C. Heat-work (time × temperature), not just peak temperature, sets the cone.
- **Respirable crystalline silica** — OSHA PEL 50 µg/m³ (8-hr TWA), action level 25 µg/m³. Governs any dry-handling or sweeping recommendation.
- **Food-contact leaching** — FDA action levels for leachable lead/cadmium on foodware; verify by ASTM C738 acid-leach test, never by recipe inspection alone.
- **Waste water** — glaze slurry carries heavy metals; many municipalities prohibit drain disposal. Reclaim or settle-and-haul.
