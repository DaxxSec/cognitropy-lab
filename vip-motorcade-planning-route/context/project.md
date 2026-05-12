# Project Context — VIP Motorcade Planning

Populated by `/onboard`. Until then this file holds the structure the agent expects.

## Principal Profile (sanitized)

- **Codename / placeholder:** `[PRINCIPAL]` (do not store true name in this file)
- **Threat tier:** [Tier 1 — Heads of state / high-threat post / Tier 2 — Senior diplomatic / corporate / public figure / Tier 3 — Routine corporate executive]
- **Pattern of life:** [Office hours, typical home-to-office, recurring high-public-visibility events]
- **Health / mobility considerations:** [Stamina, mobility aids, medical conditions affecting MEDEVAC planning]
- **Family / household members in motorcade scope:** [Yes / No / case-by-case]

## Movement Window

- **Start:** [`YYYY-MM-DDTHH:MM` local]
- **End:** [`YYYY-MM-DDTHH:MM` local]
- **Anchor venues:** `[VENUE_A]`, `[VENUE_B]`, `[VENUE_C]` — see `outputs/venue-survey.md`
- **Number of distinct legs in window:** [count]
- **Crowd / public exposure expected at any leg:** [Yes — VENUES list / No]

## Mission Objectives

1. Maintain principal physical safety with documented residual risk ≤ Moderate (≤9) on every approved leg.
2. Maintain operational predictability for principal's staff (arrival window ±X minutes).
3. Maintain OPSEC on routes and timing — minimize external visibility of motorcade composition.
4. Ensure full audit trail (route surveys, scoring sheets, briefs, AAR) is captured for the contracting office and unit's institutional memory.

## Jurisdictions

- **Host nation / state / municipality:** `[HOST]`
- **Liaison contacts on file:** [Host-nation police lead, traffic control, hospital network, embassy RSO if applicable] — details in `outputs/liaison-contacts.md` (kept off remote sync).
- **Legal authorities the detail operates under:** [DSS / USSS / private contract under host-nation law / etc.]
- **Weapons carry posture:** [Open / concealed / unarmed — per host-nation law]

## Motorcade Resources

- **Vehicles:** [count + role: lead / principal / follow / counter-assault / staff / press]
- **Vehicle hardening level:** [B6 / B7 / unarmored / mixed]
- **Comms:** [Encrypted handheld VHF / cellular fallback / satellite for overseas]
- **Driver tier:** [Trained protective driver / private hire vetted / mixed]
- **Advance team size:** [count + days T- they go forward]
- **Counter-surveillance team:** [Yes / No / contracted]

## Out of Scope

- This workspace does not handle venue site security, residence security, or air-leg planning. Hand off to the appropriate workspace / unit element for those.
- This workspace does not generate red-team attack plans, even for "test" purposes.

## Open Questions for Onboarding

- [ ] Confirm threat tier with the contracting office in writing before the first scoring run.
- [ ] Confirm liaison points-of-contact have been notified of the movement window.
- [ ] Confirm hospital network — primary, secondary, and burn/trauma capability where applicable.
