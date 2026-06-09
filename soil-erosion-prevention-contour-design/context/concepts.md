# Soil Erosion Prevention (Contour Design) — Core Concepts

Background the agent reads before acting. Optimised for fast recall. This workspace frames erosion control through **capacity planning**: storms and sediment are *demand*, structures are *capacity*, and good design keeps utilization < 1 with headroom across the service life.

## Water erosion processes

Erosion by water is a sequence of detachment → transport → deposition, manifesting as escalating forms:

- **Splash** — raindrop impact detaches particles; the first energy input, mitigated by canopy and residue cover.
- **Sheet erosion** — thin, near-uniform removal of topsoil across a slope; invisible until it isn't.
- **Rill erosion** — concentrated flow cuts small channels (< ~30 cm) that tillage can erase; the workhorse term in RUSLE.
- **Interrill** — the splash + sheet contribution feeding rills; RUSLE models interrill + rill together.
- **Ephemeral gully** — recurring concentrated-flow channels in swales; *not* well captured by RUSLE.
- **Classic gully** — permanent incised channels; an engineering (check-dam / grade-control) problem, not a tillage one.
- **Streambank / tunnel (piping)** — channel and subsurface forms outside the contour-design scope but worth flagging.

Contour design intervenes by **shortening effective slope length**, **reducing slope-driven flow velocity**, and **providing controlled conveyance and storage** for the runoff that does form.

## RUSLE — the erosion-rate model

**A = R · K · LS · C · P** — the (Revised) Universal Soil Loss Equation predicts average annual sheet-and-rill soil loss per unit area.

| Factor | Meaning | Driver | Reduced by |
|--------|---------|--------|-----------|
| **R** | Rainfall–runoff erosivity (energy × max 30-min intensity, EI₃₀) | Climate | (not a design lever) |
| **K** | Soil erodibility (t·ac·hr per hundreds of ft·tonf·in, US units) | Texture, OM, structure, permeability | OM building, structure |
| **LS** | Slope-length × slope-steepness topographic factor | Terrain | **contour/terrace shortening of L; grading of S** |
| **C** | Cover–management ratio (0–1, bare fallow = 1) | Crop, residue, canopy | residue, cover crops, no-till |
| **P** | Support-practice ratio (0–1, up-and-down slope = 1) | Practice | **contouring, strip cropping, terracing** |

Two of five factors (LS, P) are exactly what contour design manipulates; C is agronomy; R and K are largely given. **RUSLE2** (the current USDA process-form model) supersedes the lookup-table USLE and handles time-varying cover, deposition, and complex slopes — prefer it where available.

**MUSLE** replaces R with a runoff-energy term (Qₚ-based) to estimate *single-storm sediment yield* for basin sizing: `Sediment = 11.8·(Q·qₚ)^0.56·K·LS·C·P` (metric tonnes).

## Soil-loss tolerance T — the capacity budget

**T** is the maximum erosion rate (t/ac/yr, typically 1–5; or t/ha/yr ~2–11) a soil can sustain while maintaining productivity, set per soil mapping unit (NRCS). It is the **budget against which RUSLE A is the draw**:

- **A ≤ T** → within capacity; design adequate.
- **A > T** → over-utilized; add or strengthen support practices (lower P), increase cover (lower C), or shorten slope length (lower LS via terraces).
- **Utilization (soil) = A / T.** Track it like a utilization ratio — the goal is ≤ 1.0 with margin, not "as low as possible at any cost."

## Runoff hydrology — the demand signal

- **Design storm** — a rainfall depth/intensity tied to a **return period** (recurrence interval, e.g. 10-yr, 25-yr, 100-yr) and duration, read from **IDF curves** (Intensity–Duration–Frequency). The return period is the service-level target.
- **Rational method:** `Qₚ = C·i·A` (peak runoff = runoff coefficient × rainfall intensity at time-of-concentration × drainage area). Valid for small areas (≲ ~80–200 ac). `C` here is the *rational runoff coefficient* (0–1), **not** RUSLE's cover factor.
- **NRCS Curve Number (CN) method:** `Q = (P − 0.2S)² / (P + 0.8S)`, `S = 1000/CN − 10` (inches). Better for larger areas and ungauged sites; CN from soil hydrologic group × cover.
- **Time of concentration (Tc)** — the time for runoff to travel from the hydraulically most-distant point to the outlet; sets the design intensity `i`. Contouring lengthens Tc (good — lowers peak).
- **Infiltration capacity** — the max rate soil can absorb water (**Horton:** `f(t)=f_c+(f_0−f_c)e^{−kt}`; **Green-Ampt** for physically-based fronts). Runoff (Hortonian/infiltration-excess) is generated when **rainfall intensity > infiltration capacity** — directly a demand-vs-capacity comparison at the soil surface.

## The capacity-planning analogy (this workspace's spine)

| Capacity-planning concept | Erosion-control mapping |
|---------------------------|--------------------------|
| Demand / load | Design-storm peak runoff Qₚ; storm sediment yield; annual soil loss A |
| Capacity | Channel conveyance Q_cap (Manning); basin/terrace storage volume; soil-loss tolerance T |
| Utilization (= demand/capacity) | Qₚ/Q_cap (hydraulic); A/T (soil); stored-sediment/storage-volume (basin) |
| Headroom / safety margin | Freeboard (channel depth above design WSE); (T − A) margin; spare storage |
| Service level / SLA | Design return period (overtopping accepted above it) |
| Bottleneck | The reach or structure with the highest utilization — fails first |
| Demand forecasting | IDF curves, climate-intensification scaling of design storms |
| Capacity drawdown over time | Sediment accumulation reducing live storage; vegetation/cover degradation |
| Capacity refresh / replenishment | Basin cleanout, channel re-grading, revegetation (maintenance cadence) |
| Queueing / buffering | Detention storage attenuating peak before discharge |

This is the lens applied throughout: never report a raw size without its utilization and headroom, and never accept a design without naming the bottleneck and the residual (above-design) risk.

## Contour-based support practices

- **Contour cultivation** — tillage and planting on the contour; small ridges intercept and slow flow. P ≈ 0.5–0.9 depending on slope. Effective only up to a slope-dependent critical row length before overtopping.
- **Contour strip cropping** — alternating contour strips of row crop and close-growing/sod crops; the sod strips filter and slow flow from the row strips. P lower than contouring alone (~0.25–0.5).
- **Terraces** — earthen embankments/channels on/near the contour that intercept runoff and shorten slope length:
  - *Broadbase (graded/level)* — farmable front and back slopes; agricultural terraces.
  - *Channel (Nichols)* — channel excavated, ridge downslope.
  - *Bench terraces* — stepped level platforms on steep land (common in rice/horticulture); near-level risers.
  - *Grade*: **level terraces** store and infiltrate (humid-to-subhumid, permeable soils); **graded terraces** carry water at a safe non-erosive grade (0.1–0.6%) to a stable outlet.
- **Diversions** — channels across a slope to intercept upslope runoff and route it away from the work area to a stable outlet.
- **Grassed waterways** — vegetated channels in natural drainageways that convey concentrated flow non-erosively (vegetation raises permissible velocity and Manning's n).
- **Key-line / contour bunds** — pattern cultivation and bunding (common in drylands/Keyline design) to spread and store water on ridges.

## Hydraulic capacity fundamentals

- **Manning's equation** (channel conveyance capacity): `Q = (k/n)·A·R^(2/3)·S^(1/2)` — `k`=1.49 (US, ft) or 1.0 (SI, m); `n`=roughness; `A`=flow area; `R`=hydraulic radius (A/wetted perimeter); `S`=channel slope. This is the supply side of `Qₚ/Q_cap`.
- **Permissible (non-erosive) velocity** — max mean velocity a lining tolerates without scour (bare soil ~0.6–1.5 m/s; good grass cover 1.5–2.4 m/s; riprap higher). The capacity is *velocity-limited*, not just area-limited.
- **Tractive force (shear)** — `τ = γ·R·S`; the more rigorous scour check vs the channel's permissible shear; preferred for vegetated/riprap design.
- **Freeboard** — vertical distance from design water surface to top of bank; the explicit hydraulic headroom (commonly 0.15–0.3 m or per standard).
- **Cross-sections** — parabolic (natural grassed waterways), trapezoidal (constructed), triangular (small diversions).

## Sediment storage & trap structures

- **Sediment basin / detention** — impoundment that ponds runoff so particles settle; sized on **trap efficiency** (Brune curve: f(capacity/inflow ratio) and particle settling velocity vs detention time). Live storage **draws down** as sediment accumulates → finite design life → cleanout cadence.
- **Check dams** — small barriers across a gully/channel that reduce effective bed grade, dissipate energy, and trap sediment. Series spacing by the **head-to-toe rule**: the crest of the downstream dam is at the elevation of the toe of the next dam upstream when the channel re-grades to the stable (non-erosive) slope. `Spacing ≈ H / (S_existing − S_stable)`.
- **Stilling / outlet protection** — energy dissipation below drops and pipe outlets to prevent scour migration.

## Common Failure Modes

- **Up-and-down-slope rows on graded land** — the canonical worst case (P = 1.0); contouring is the cheapest single intervention.
- **Overtopping at a higher-than-design storm** — not a defect if the return period was stated; *is* a defect if undocumented or if no safe overflow path exists.
- **Velocity exceedance in a "big enough" channel** — area capacity met but mean velocity over permissible → scour; always run the velocity/shear check, not just `Q`.
- **Ignoring ephemeral-gully and concentrated flow** — RUSLE A looks fine while a swale gullies; field-verify flow paths.
- **Terrace channel with reverse/flat spots** — ponding, breaching; survey grade continuity.
- **Unmaintained sediment basin** — storage silts to zero, trap efficiency collapses, downstream loading spikes; the capacity-refresh schedule is part of the design, not an afterthought.
- **Mixing the two "C"s** — RUSLE cover-management C vs rational runoff coefficient C are different numbers; label every C.
- **Single-equation overconfidence** — RUSLE is average-annual, empirical, sheet-and-rill only; do not use it to size a structure (use runoff/sediment-yield methods) or to assess gullies.

## Operating Constraints

- Erosion/sediment-control structures that impound or discharge water may be subject to local stormwater, dam-safety, and wetland/clean-water permitting — flag for jurisdictional review.
- Cost-share and standards alignment (e.g. NRCS conservation practice standards) often condition funding; design to the applicable practice standard.
- Constructed water-control structures should carry a licensed engineer's review/stamp where required by jurisdiction; this workspace produces analysis and preliminary sizing, not stamped final designs.
