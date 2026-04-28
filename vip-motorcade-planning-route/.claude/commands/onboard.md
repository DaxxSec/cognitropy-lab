# /onboard — Initialize VIP Motorcade Planning Workspace

Welcome. I will collect the minimum context needed to score routes correctly. Answer in shorthand; we'll refine as movements happen.

## Interview Flow

### 1. Principal & Threat Tier
Ask the user:
- Codename / placeholder for the principal (do not give me a true name; use `[PRINCIPAL]` or a callsign).
- Threat tier: 1 (head-of-state / high-threat post), 2 (senior diplomatic / public figure / corporate), or 3 (routine corporate executive)?
- Health / mobility considerations that affect MEDEVAC planning?
- Family / household members included in the motorcade scope?

Save responses to `context/project.md` (Principal Profile section).

### 2. Movement Window
Ask the user:
- Start and end of the movement window (relative time is fine: "T-0 = Mon 0900 local").
- Anchor venues — give placeholder names (`[VENUE_A]`, `[VENUE_B]`) and the rough geography.
- How many distinct legs in the window?
- Crowd / public exposure expected at any leg?

Save to `context/project.md` (Movement Window section).

### 3. Jurisdictions & Authorities
Ask the user:
- Host nation / state / municipality.
- What legal framework does the detail operate under? (DSS / USSS / RCMP-PPS / private contract / other)
- Weapons carry posture — open / concealed / unarmed — confirm legality for this jurisdiction.
- Liaison contacts on file (police, traffic, hospital, embassy / RSO if applicable).

Save to `context/project.md` (Jurisdictions section). Sensitive contact details go to `outputs/liaison-contacts.md` flagged `confidential-do-not-sync`.

### 4. Motorcade Resources
Ask the user:
- Vehicle count + role assignment (Lead / Pilot / Principal / Follow / Tail / CAT / Staff / Press).
- Vehicle hardening (B6 / B7 / unarmored / mixed)?
- Comms suite — primary, fallback, satellite if applicable.
- Driver tier — trained protective drivers, vetted hires, mixed?
- Advance team size and lead time.
- Counter-surveillance present? Static / mobile / contracted?

Save to `context/project.md` (Motorcade Resources section).

### 5. Operator Profile
Ask the user:
- Position (detail leader / advance lead / planning cell / EP contractor / unit type)
- Years in protective ops, movements led, formal training (DSS HTP, USSS PCDP, BFC, etc.)
- Prior risk-matrix / ISO 31000 / HAZOP exposure
- Preferred prompting depth — verbose vs terse

Save to `context/role.md`.

### 6. Constraints & Posture
Ask the user:
- Default residual-risk ceiling for an approved leg (default Moderate ≤9; some details run High ≤14 with sign-off).
- Minimum motorcade composition the contracting office insists on.
- Sanitization / OPSEC level for artefacts in this workspace (default: hard-sanitize, no real PII).

Save to `context/constraints.md`.

## Post-Onboard Actions

1. Pre-fill `planning/comparison-weights.md` with the README's default weights and flag where the user's answers suggest tuning (e.g. corporate Lat-Am tour shifts profile/deniability higher).
2. Recommend whether `/threat-baseline` should run first against open sources (Tier 2/3) or against unit intel feeds (Tier 1) — and stop if the unit hasn't authorized the latter.
3. Create `planning/plan.md` capturing the movement window, principal placeholder, list of legs to score, and target T-2 brief deadline.
4. Log onboarding in `work-log/<YYYY-MM-DD>-onboard.md`.
5. Print the residual-risk ceiling and minimum composition once at the top of every subsequent session as a posture reminder.
