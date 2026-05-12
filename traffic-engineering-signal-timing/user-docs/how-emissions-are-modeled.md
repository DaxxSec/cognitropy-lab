# How Emissions Are Modeled in This Workspace — Plain-Language Explainer

## TL;DR

Two emission estimators run side-by-side:
- **CMEM** is fast and approximate. It runs inside the optimizer's inner loop so the agent can score thousands of timing candidates per minute.
- **MOVES4** is slow and authoritative. It runs only on the 1–3 final plans and produces the regulatory-grade numbers that go into the report.

This split exists because MOVES is too slow for an inner loop (each project-level run takes minutes) and CMEM is too coarse for a SIP submittal.

## What MOVES Actually Does

EPA's MOtor Vehicle Emission Simulator (MOVES) is the federally-approved mobile-source emission model. It looks at:

1. **Your fleet** — what vehicles, what model years, what fuels (LDV gasoline, LDT gasoline, LDT diesel, transit bus, single-unit truck, combination truck, motorcycle).
2. **Your drive cycle** — how much time spent at each speed, accelerating, braking, idling.
3. **Your environment** — ambient temperature, humidity, fuel formulation.
4. **Your model years** — newer vehicles emit much less per mile than older ones.

It returns mass emissions per pollutant per source-type per "process" (running, start, idle, evap) per link. Re-running these on different timing scenarios reveals how the timing change moved the corridor's emissions inventory.

## What CMEM Does Differently

The Comprehensive Modal Emissions Model (CMEM, UC Riverside) is a second-by-second physics model:

1. Take a single vehicle's speed trace.
2. For each second, classify it as Idle / Accel / Cruise / Decel.
3. Multiply the seconds in each mode by per-second emission rates from a regression model fit to dynamometer data.
4. Sum to a per-vehicle total. Multiply by vehicle count.

Because everything is a fast lookup, CMEM can score a Pareto candidate in milliseconds. It pays for that with less precision around start/evap effects, cold-start chemistry, and recent model-year updates.

## Why Stops Matter So Much

A stopped-and-restarted vehicle costs roughly:
- 0.045 kg CO2 (a passenger car)
- 0.060 g NOx
- 0.005 gallons of fuel

Multiply by ~3,500 stops in a single PM peak hour on a typical urban arterial corridor and you're at:
- 158 kg CO2/peak-hour
- 210 g NOx/peak-hour
- 17.5 gal fuel/peak-hour

Annualize to 250 weekdays and you're at:
- ~40 t CO2/yr per corridor — equivalent to 9 cars taken off the road
- ~52 kg NOx/yr — material on a NAAQS exceedance basis
- ~4,400 gal fuel/yr at modest gas prices

Cutting stops by 20% via better coordination is therefore worth roughly 8 t CO2/yr — and that's just one corridor. The CMAQ math compounds quickly.

## What "Pareto Frontier" Means Here

The optimizer doesn't return one "best" timing plan. It returns a curve. Each point on the curve is a plan where you can't reduce delay without increasing some emission, or vice versa. This shape exists because the levers (cycle, splits, offsets) push these objectives in correlated but not identical directions.

Your job — usually with stakeholder input — is to pick a point on the curve that respects your binding constraint:
- "We must stay under the basin NOx ceiling" → pick the lowest-delay point with NOx ≤ ceiling.
- "We need the CMAQ funding" → pick the point that maximizes CO2 reduction subject to delay not increasing more than 5%.
- "Pedestrian council pushed back on long cycles" → cap cycle ≤ 90 s and pick min-delay within that.

The frontier doesn't make the decision; it makes the decision visible.

## Where the Numbers Come From

| Number | Source |
|--------|--------|
| Saturation flow defaults | HCM 7th Edition, Chapter 19 |
| Webster's optimal cycle | Webster (1958), as adapted in HCM 7 |
| Akcelik delay | Akcelik (1981); HCM 7 Eq. 19-22 |
| MOVES emission rates | EPA MOVES4 (2024 release) |
| CMEM modal rates | Barth et al. (2000), Scora & Barth (2006) |
| Per-stop emission cost | Derived from CMEM modal rates × typical decel-idle-accel profile |
| Eco-target speed offset | Barth & Boriboonsomsin (2009) |
| Social cost of carbon | EPA SC-CO2 (2024 update, ~$190/t-CO2) |

All are cited inline in `context/for-agent/domain-knowledge.md` and `resources/`.

## What This Workspace Does NOT Model

- Cold-start emissions (under MOVES "start process") — not under signal-timing control.
- Evaporative emissions — same; not signal-controlled.
- Brake/tire wear PM2.5 (non-tailpipe) — sensitive to braking events, but the regression coefficients in CMEM cover this only loosely.
- Real-world driver aggressiveness variance — assumes typical-driver acceleration profiles.
- Electric vehicle (EV) tailpipe emissions — EVs contribute ~0 tailpipe but still produce non-tailpipe PM. The fleet mix should reflect local EV penetration.

When precision on any of those matters, escalate to a microsimulation + MOVES4 workflow with a CARB-grade EV adjustment.
