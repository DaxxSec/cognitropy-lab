# Domain Knowledge — VIP Motorcade Planning & Risk Scoring

## 1. Risk Scoring Methodology — The 5×5 Matrix

### Why a 5×5

The 5×5 matrix (likelihood × impact, each on a 1–5 scale, product 1–25) is the dominant form across ISO 31000, MIL-STD-882E, FEMA HAZUS, and protective-services doctrine because it:

- **Forces discrimination.** A 3×3 collapses too much (every credible hazard ends up "Medium / Medium"). A 7×7 invites false precision (no analyst meaningfully distinguishes 0.42 from 0.46 likelihood).
- **Rolls up cleanly.** Per-segment products plot on a heat-map by class (Low / Moderate / High / Very High / Extreme), giving a readable risk picture at a glance.
- **Is auditable.** Each cell has a written tier definition, and each plot has a written justification — the artefact survives the planner.

### Likelihood (L) — 1 to 5

| L | Tier | Definition (anchored to threat baseline) |
|---|------|------------------------------------------|
| 1 | Rare | No credible actor with intent + capability against this principal in this region; only background-rate hazards. |
| 2 | Unlikely | Actors with intent or capability exist but no specific targeting indicator; hazard is plausible at the rate of public-incident base rates. |
| 3 | Possible | Actors with both intent and capability exist; no specific targeting yet, but principal's profile or movement window matches the actor's pattern. |
| 4 | Likely | Specific targeting indicator (surveillance, threat communication, prior incident) within 90 days, OR principal is in the actor's known operating area during a sensitive window. |
| 5 | Almost Certain | Active, dated, specific threat against this principal or a near-identical principal at this venue/time, OR a recent successful attack of this type at this segment within 30 days. |

### Impact (I) — 1 to 5

| I | Tier | Definition (principal-centric) |
|---|------|--------------------------------|
| 1 | Negligible | Brief delay; no injury; no comms loss; no story. |
| 2 | Minor | Detail-level injury or vehicle damage; principal experiences delay but no harm or photographable disruption. |
| 3 | Significant | Forced abort; minor principal injury; embarrassing visual; press story; protocol breach with the host nation. |
| 4 | Critical | Critical principal injury, principal capture / hostage situation, KIA among detail. |
| 5 | Catastrophic | Principal killed; mass casualty; geopolitical incident. |

### Risk Bands

| Product | Band | Operating Stance |
|---------|------|------------------|
| 1–4 | Low | Acceptable; proceed. Document mitigations performed. |
| 5–9 | Moderate | Acceptable; default ceiling for an approved leg. |
| 10–14 | High | Requires explicit detail-leader sign-off + at least one specific countermeasure on the segment. |
| 15–19 | Very High | Requires written contracting-office sign-off; route should be re-engineered if at all possible. |
| 20–25 | Extreme | Veto. Re-route. |

### Inherent vs Residual

- **Inherent** = score before mitigations.
- **Residual** = score after applying motorcade composition, advance, counter-surveillance, hardening, route choice, timing, and host-nation support.

The detail leader signs off on **residual**, not inherent. Every High+ residual requires a named, *attributable* mitigation listed in the brief.

### Common Abuse Patterns (and How to Resist Them)

1. **The "Center Drift."** Analysts gravitate to L=3, I=3 ("possible / significant") for everything. Resist by demanding a specific anchor for every L≥3 (an actor, a date, an indicator) and every I≥3 (a casualty mechanism).
2. **Mitigation theatre.** Adding a vehicle does not necessarily reduce ambush *likelihood*; it may reduce *impact*. Be precise about which axis a mitigation moves.
3. **Average-down.** Routes are not the average of their segments. Roll-up uses *max residual* + count of High+ as a tail-risk tie-breaker.
4. **Reverse engineering.** "We've decided to take River Road, so let me score the others higher." Score before deciding; if you've already decided, document that this was the case.
5. **Number worship.** A 12 with a clear ambush mitigation is safer than an 8 with no plan. Numbers serve the brief, not the other way around.

## 2. Attack Typology — What You're Scoring Against

| Type | Brief description | Likelihood drivers | Impact drivers | Mitigation primary |
|------|-------------------|--------------------|----------------|--------------------|
| Complex Ambush | Coordinated attack, multiple shooters, often combined with IED/initiator | High-threat post, prior attack signature | Up to catastrophic | Speed-through, hardened vehicle, CAT, alternate timing |
| Single-shot Sniper | Long-range precision shot at predictable point | Public, predictable stops; line-of-sight standoff | Critical+ on principal | Block sightlines, vary stops, screen the principal |
| VBIED / IED | Vehicle-borne or roadside explosive | Predictable route, slow chokepoint | Catastrophic | Route variation, sweep, standoff, route closure |
| Crowd Surge / Crush | Public motorcade meets dense crowd; vehicles trapped | High public profile, parade routing | Significant – Critical | Crowd line-up, advance crowd-density estimate, push-through plan |
| Lone-actor Edged / Firearm | Close-range opportunist, often at venue arrival/departure | Public exposure at fixed point, principal pattern-of-life leak | Critical | Arrival hardening, decoy, dynamic timing |
| Vehicle Ramming | Heavy-vehicle ram at chokepoint or stop | Public stops, narrow streets | Significant – Critical | Hostile-vehicle mitigation (HVM), bollard awareness |
| Kidnap-for-ransom | Force vehicle stop, extract principal | Lat-Am / W-Africa norms, low-profile movement | Critical | Counter-surveillance, hardened, CAT, route variation |
| Disinformation / Spoof Comms | Fake police checkpoint, fake medical event | Host-nation corruption, imitable uniforms | Significant | Host-nation liaison verification, callsign discipline |
| Cyber-physical (GPS spoof, comms jamming) | Disrupt navigation/comms to force divert | High-end actor, electronic-warfare capable | Significant | Map-and-compass fallback, comms diversity |

Each one has its own characteristic indicators and mitigations. The agent's `/contingency-plan` walks the operator through them.

## 3. Route Survey — What Makes a Segment a Segment

A segment is a stretch of route with **uniform exposure characteristics**. It changes when any of these change:

- Roadway geometry (lane count, divided/undivided)
- Speed regime (highway / urban / parking-deck)
- Building density / line-of-sight (urban canyon, open boulevard, suburban)
- Choke condition (single lane, bottleneck, controlled intersection)
- Jurisdictional boundary (county line, host-nation district)
- Ingress/egress availability (alternate exits per minute of route)

Typical urban motorcades produce 15–35 segments for a 20-minute leg. Each segment is geocoded (start lat/long, end lat/long), photographed (offline, kept private), and tagged with the dominant hazards from §2.

## 4. Motorcade Composition Doctrine

Composition is decided *before* the route, but it changes the *impact* score across many hazards.

### Standard Compositions

- **3-vehicle (corporate / Tier 3):** Lead — Principal — Follow.
- **5-vehicle (diplomatic / Tier 2):** Lead — Pilot — Principal (limousine) — Follow — Tail.
- **7+ vehicle (high-threat / Tier 1):** Adds a Counter-Assault Team (CAT) vehicle, a Hazardous Materials / EOD scout, and frequently a press / staff vehicle.

### Pilot vs. Lead

- **Lead** opens the route, watches for forward indicators. Stays ~10–15 s ahead of principal.
- **Pilot** runs further ahead, identifies route conditions, calls back diversions. Used in Tier 1 / Tier 2.

### Counter-Assault Team

- A separate vehicle with detail capable of dismounting and *fixing* an ambush so the principal motorcade can break contact and run. CAT is not part of the principal's escort; its mission is to enable departure, not defend in place.

### Spacing

- Tight (1–2 car lengths) in dense urban; speed reduces but cohesion increases.
- Open (5+ lengths) on highway; lets the lead/follow react without ricocheting into the principal car.

## 5. Timing & Predictability

Predictability is itself a hazard: an actor can plan around a known schedule.

- **Vary departures** by a randomized window (e.g. ±15 min). The agent's `/movement-brief` will produce briefing artefacts in *relative* time so the same brief works across the window.
- **Vary routes** between primary, alternate, and previously-unused — never run the same primary three days in a row for a sustained-engagement principal.
- **Vary stops** — even a 30-second curb stop is a high-impact opportunity if it's predictable.

## 6. Doctrine Citations Worth Knowing

- **U.S. State Department Diplomatic Security (DS) High-Threat Protection (HTP)** — the dominant U.S. methodology for Tier 1 work in non-permissive environments. Public summary: motorcade composition, advance work, comms.
- **U.S. Secret Service Protective Methodology** — emphasizes "concentric rings of protection" and precise advance work. Source for line-of-sight, stand-off, and crowd-line concepts.
- **NPSA UK (formerly CPNI)** — strong public guidance on hostile vehicle mitigation (HVM), reconnaissance indicators, and crowded-place protection.
- **ASIS International PSC.1 Executive Protection Standard** — corporate-EP risk management framework; aligns with ISO 31000.
- **ISO 31000:2018** — generic risk-management standard, source of the "establish context → identify → analyse → evaluate → treat → monitor & review" cycle the workflows follow.
- **MIL-STD-882E** — DoD system-safety risk matrix; the ancestor of the modern 5×5.
- **FEMA HAZUS / NIMS ICS** — for understanding incident-command interfaces with host-nation responders during a contingency.

The agent cites these inline in briefs and after-action reports so the doctrinal anchor is preserved.

## 7. Failure Modes the Agent Watches For

- **Single-route plans.** Refuse to score a candidate "primary" without an alternate and abort also on the table.
- **Mitigation double-counting.** A single advance team cannot be credited as a mitigation on every segment of a 30-segment route. Track which mitigation is *actually* present on each segment.
- **Stale baseline.** Threat baselines older than 14 days require a `/threat-baseline --refresh` before the matrix is trusted.
- **Pattern-of-life drift.** If the principal's actual movement is converging toward a routine the workspace was meant to vary, flag it in `/after-action`.
- **Brief bloat.** A T-2 movement brief no driver actually reads is worse than no brief. The agent enforces a 1-page driver brief alongside the full operational order.
