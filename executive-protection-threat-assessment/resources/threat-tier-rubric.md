# Threat Tier Rubric

The default likelihood × impact scoring rubric for this workspace, with principal-specific tuning slot.

## Likelihood (1–5)

Likelihood is judged as the conservative median of three legs: **Intent**, **Capability**, **Opportunity**. See `context/for-agent/domain-knowledge.md` §1.1.

| Score | Label | Indicators (any of) | Typical evidence grade |
|-------|-------|---------------------|------------------------|
| 1 | Negligible | No documented intent, no capability, no opportunity | C–D |
| 2 | Low | Latent — one leg present, two absent | C |
| 3 | Moderate | Two legs present; the third would have to be acquired | B–C |
| 4 | High | All three legs present, no specific timing indicator | A–B |
| 5 | Imminent | All three legs present plus a specific timing indicator or pre-attack signal in the last 14 days | A |

## Impact (1–5)

Impact is the worst plausible outcome to the principal if the threat manifests. Use the band that best fits.

| Score | Label | Worst-plausible outcome |
|-------|-------|-------------------------|
| 1 | Negligible | Embarrassment / minor reputational, no physical risk |
| 2 | Minor | Disruption to schedule; possible minor injury |
| 3 | Moderate | Schedule loss + minor-to-moderate injury OR significant reputational |
| 4 | Major | Hospitalisation, persistent reputational damage, mission failure |
| 5 | Catastrophic | Life-threatening injury or death, fatal mission failure, geopolitical fallout |

For vehicle-borne rows, **do not score impact qualitatively** — the kinematics workflow returns an AIS band and the table below maps it to the matrix Impact:

| AIS band | Matrix Impact |
|----------|---------------|
| 0–1 | 1 |
| 1–2 | 2 |
| 2–3 | 3 |
| 3–4 | 4 |
| 4–5 | 5 |

## Posture mapping (5×5)

```
Impact →   1   2   3   4   5
        ┌───┬───┬───┬───┬───┐
   L=5  │ Y │ O │ R │ R │ R │
        ├───┼───┼───┼───┼───┤
   L=4  │ G │ Y │ O │ R │ R │
        ├───┼───┼───┼───┼───┤
   L=3  │ G │ Y │ Y │ O │ R │
        ├───┼───┼───┼───┼───┤
   L=2  │ G │ G │ Y │ Y │ O │
        ├───┼───┼───┼───┼───┤
   L=1  │ G │ G │ G │ Y │ Y │
        └───┴───┴───┴───┴───┘
```

- **G — Monitor.** Situational awareness only.
- **Y — Mitigate by procedure.** Adjust route, timing, comms; no equipment uplift.
- **O — Mitigate by countermeasure.** Add formation depth, hardened vehicle, additional advance, LE liaison.
- **R — Avoid or harden.** Cancel/reschedule, or full hardening (armoured platform, alternate-route discipline, explicit LE coverage).

## Evidence grades

| Grade | Definition |
|-------|------------|
| A | Multi-source, two or more independent reliable sources, includes physical/forensic or first-party reporting |
| B | Single reliable source (named LE liaison, vetted intel feed, confirmed first-party) |
| C | Open-source unverified — news report, social media, public filing without independent confirmation |
| D | Speculative — analyst inference without source, hypothesis only |

## Mitigation layers

| Layer | Examples |
|-------|----------|
| Routing | Alternates, randomisation, chokepoint avoidance |
| Timing | Off-peak movement, surprise schedule, early arrival |
| Formation | Vehicle order, lead/follow distance, chase role, flankers |
| Vehicle | Hardening (B4/B6/B7 BR), runflats, ram bumper, tyre-deflation device |
| Medical | TCCC medic, IFAK, hospital pre-coordination |
| LE liaison | Host LE escort, intel exchange, traffic plan |
| Comms | Encrypted comms, code words, EAP/exfil triggers |
| Counter-surveillance | SD assets pre-deployed, pattern analysis on inbound surveillance |
| Counter-tech | Cell awareness, drone detection, RF discipline |

## Default tier targets

For the *default* (non-tuned) rubric, the workspace's tier expectations:

- 60–80% of cells should resolve to Green or Yellow on a normal corporate engagement
- 1–3 Orange cells expected in semi-permissive geographies
- Any Red cell triggers the cancel/reschedule decision unless full mitigation layer is engaged AND posture-driving cell evidence is grade A

## Principal-specific tuning

> Populated by `/onboard` and refreshed at each `/risk-matrix` recalibration. The default rubric above is a starting point; high-profile principals may warrant tighter likelihood thresholds, and low-profile principals may warrant looser ones.

| Principal codename | Tier shift | Rationale | Date set |
|--------------------|-----------|-----------|----------|
| _(populate at onboard)_ | _(e.g. likelihood +1 across categories 1, 2, 5 due to active named threat)_ | _(evidence-anchored)_ | _(ISO date)_ |

## Posture decision aids

- **All Green** → re-collect; almost certainly under-collection
- **>2 Red without grade-A evidence** → almost certainly over-weighting; demand defence per cell
- **One Red with full mitigation layer** → proceed, recalibrate at engagement +24h
- **Mixed Orange with single-layer mitigation** → uplift to two layers before engagement
- **Pre-attack indicator detected** → recalibrate +1 likelihood in relevant rows; if any rises to Red, escalate to detail leader the same day
