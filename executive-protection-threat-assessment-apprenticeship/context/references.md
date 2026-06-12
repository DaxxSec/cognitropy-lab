# References — Lookup Tables & Cheat-Sheets

Compact lookup data for EP threat assessment and apprenticeship tracking. Prose lives in `concepts.md`.

---

## Threat / risk tier rubric

| Tier | Label | Likelihood × Impact | Posture |
|---|---|---|---|
| **T1** | Routine | Low likelihood, moderate impact | Baseline detail, standard advances |
| **T2** | Elevated | Credible actor without imminent capability/opportunity | Add surveillance detection, tighten advances |
| **T3** | High | Capable + intent, opportunity emerging | Counter-surveillance, route hardening, LE liaison |
| **T4** | Imminent | Capable + intent + opportunity, indicators of mobilisation | Movement restriction, protective intelligence surge, LE handoff |

Calibrate against ISO 31000 likelihood × consequence; resist "everything is high."

## Capability × Intent × Opportunity scoring

| Factor | 1 (low) | 3 (moderate) | 5 (high) |
|---|---|---|---|
| **Capability** | No means/skill | Some access to weapons/skill | Trained, armed, resourced |
| **Intent** | None expressed | Grievance + ideation | Research/preparation behaviours observed |
| **Opportunity** | No access/knowledge | Knows some routine | Detailed pattern-of-life + proximity |

Threat ≈ (Intent × Capability), escalated by Opportunity. A high-intent/low-capability actor is a *howler*; watch for capability acquisition.

## Hostile planning cycle → interdiction

| Phase | Detection signature | Cheapest interdiction |
|---|---|---|
| Initial surveillance | Casing, photography of security, probing questions | Surveillance detection, pattern variation |
| Final target selection | Repeated presence (TEDD) | Counter-surveillance, deterrent visibility |
| Pre-attack surveillance | Fixed observation posts, dry-run timing | SDR, LE referral — **highest leverage** |
| Rehearsal | Probing access, testing response | Harden access, change posture |
| Execution | — | Cover & evacuate (get off the X) |

## TRAP-18 proximal warning behaviours (quick lens)

Pathway · Fixation · Identification · Novel aggression · Energy burst · Leakage · Last resort · Directly communicated threat. *(Distal characteristics inform but don't trigger.)*

## Advance-survey checklist (EPA-1)

- [ ] Arrival/departure points (APOD) & embus/debus screening
- [ ] Primary / alternate / emergency routes
- [ ] Safe haven / hold room (< 30s from principal)
- [ ] Nearest Level I/II trauma center + time-distance
- [ ] Command post & comms plan
- [ ] Access control / magnetometer plan
- [ ] CPTED walk + CARVER of single points of failure
- [ ] Site-specific EAP (AOP, medical, fire, evac)
- [ ] Vulnerability register with owners

## Trauma-center note

Level I = full-spectrum, surgeon in-house 24/7; Level II = comprehensive, may transfer complex cases. Advance medical plans target the nearest **Level I or II**; record drive-time on the primary and an alternate route.

---

## Dreyfus ladder ↔ EP role

| Stage | Role |
|---|---|
| Novice | Protective Agent Trainee |
| Advanced beginner | Shift / Post Agent |
| Competent | Advance Agent |
| Proficient | Detail Leader |
| Expert | Detail Commander / Program Lead |

## EPA roster ↔ command

| EPA | Activity | Command |
|---|---|---|
| EPA-1 | Advance survey | `/advance-survey` |
| EPA-2 | Protectee risk profile | `/protectee-risk-profile` |
| EPA-3 | Adversary assessment | `/adversary-assessment` |
| EPA-4 | Route analysis | `/route-threat-analysis` |
| EPA-5 | Surveillance-detection plan | `/surveillance-detection-plan` |
| EPA-6 | Attack-cycle interdiction | `/attack-cycle-map` |
| EPA-7 | Emergency action plan | `/eap-builder` |
| EPA-8 | Protective-intelligence watch | `/adversary-assessment` + `/attack-cycle-map` |

## Entrustment scale (quick)

1 Observe only · 2 Direct supervision · 3 Indirect supervision · 4 Unsupervised · 5 Supervise others.
**Rule:** raise a level only on ≥2 independent WBA observations; never on tenure alone.

## Miller's pyramid (assessment target)

Knows → Knows how → Shows how → **Does** (live, supervised — the `/competency-signoff` target).

## Roster record template (`outputs/roster.md`)

```
### <Apprentice name> — stage: <Dreyfus role>
| EPA | Entrustment (1-5) | Evidence count | Notes |
|-----|-------------------|----------------|-------|
| EPA-1 | 3 | 4 | indirect supv; one live advance |
| EPA-2 | 4 | 5 | unsupervised |
| ...   |   |   |       |
Weakest EPA: EPA-6 (1, 1) → next deliberate-practice target
```

---

## External references

- U.S. Secret Service NTAC — Protective Intelligence & Threat Assessment: https://www.secretservice.gov/protection/ntac
- Fein & Vossekuil, *Protective Intelligence and Threat Assessment Investigations* (NIJ): https://www.ojp.gov/pdffiles/179981.pdf
- ten Cate, Entrustable Professional Activities (Academic Medicine / PMC): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3613304/
- Meloy, TRAP-18: https://www.gifrinc.com/trap-18/
- Calhoun & Weston, *Contemporary Threat Management* (hunters vs howlers): https://www.specializedtraining.com/
- ASIS International (Protection of Assets, risk standards): https://www.asisonline.org/
- ISO 31000 risk management: https://www.iso.org/iso-31000-risk-management.html
- Dreyfus model of skill acquisition: https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition
