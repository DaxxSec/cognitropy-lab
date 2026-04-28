# /threat-baseline — Build Threat Actor & Capability Baseline

Produce the documented threat baseline that anchors every Likelihood score in this workspace.

## Required Inputs
- Principal profile (from `context/project.md`)
- Movement window (start, end, plus a -30 d look-back / +7 d look-ahead horizon)
- AOR — host nation / city / district
- Authorized intel inputs (open-source by default; classified feeds only if the user explicitly states authorization)

## Procedure

### 1. Frame the Horizon
Window start − 30 d → window end + 7 d. Document the exact ISO range in the baseline file. Anything older than 30 d is *context*, not *targeting*.

### 2. Enumerate Candidate Threat Actors
For each of these classes, ask "is there a credible actor *against this principal in this AOR* in this horizon?" — yes / no / unsure:

- State-nexus (foreign intelligence service / state-sponsored)
- Organized criminal (kidnap-for-ransom, narco, crime family)
- Ideological / political (insurgency, extremist movement, lone-wolf network)
- Issue-driven activist (protest disruption, doxx-and-confront)
- Lone actor (stalker, mentally-disordered offender, opportunist)
- Insider (disaffected staff, contractor with access)

Drop `no` rows; keep `yes` and `unsure`.

### 3. Score Intent and Capability
For each kept actor:

- **Intent (1–5):** Has the actor stated, demonstrated, or strongly implied targeting *this* principal class? 1 = no signal; 5 = explicit, dated targeting.
- **Capability (1–5):** Can the actor deliver against the protective posture? 1 = no relevant capability; 5 = recent demonstrated success against a similar-tier principal.

Set base likelihood for any related hazard at `min(intent, capability)` unless §4 evidence pushes it higher.

### 4. Catalog Targeting Indicators
Within the horizon — list each indicator with date, source, and confidence:

- Surveillance attempts (physical, electronic, social)
- Threat communications received by the principal or their organization
- Similar-profile incidents in the AOR
- Leaked schedule fragments (open or known-leaked)
- Third-party warnings (host-nation police, embassy, OSINT analyst)

Each indicator either pegs likelihood higher for one or more hazards, or is filed as context.

### 5. AOR Conditions
- Public events overlapping the window (protests, anniversaries, elections).
- Ongoing security incidents in the AOR (active conflict, recent terror attack, civil unrest).
- Host-nation security posture changes (heightened alert, route closures, force levels).

### 6. Output
Write `outputs/threat-baseline-<YYYY-MM-DD>.md` containing:
- Horizon dates
- Actor table with Intent, Capability, derived base-likelihood
- Indicator log with date, source, confidence, hazard mapped
- AOR conditions summary
- Per-hazard recommended likelihood ceiling for the next scoring run
- Validity expiry date (default = today + 14 d, or window-end + 7 d, whichever sooner)

Log a short summary in `work-log/<YYYY-MM-DD>-threat-baseline.md`.

## Decision Rules

- If no candidate actor reaches Intent ≥ 3 and Capability ≥ 3: cap likelihood at 3 across the matrix and flag the run as "low-anchor."
- If any actor reaches Intent ≥ 4 *and* Capability ≥ 4 against this principal class: every segment with matching exposure must score L ≥ 4 unless explicitly mitigated.
- If a specific, dated targeting indicator exists for this movement window: the related hazard's likelihood is L = 5 until mitigations bring residual into spec.

## Refusal Conditions

- Refuse to baseline against a principal the user is not contracted to protect.
- Refuse to scrape closed government systems or social media at scale.
- Refuse to attribute a threat to an actor without an evidence chain documented in the indicator log.
