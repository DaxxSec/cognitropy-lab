# /onboard — Initialise Executive Protection Threat Assessment Workspace

Welcome. I'll gather the principal profile, engagement scope, detail composition, authorities, and ethical fence-line, and write them into the `context/` files. After this, the matrix and pre-engagement workflows are useable.

**Discipline note.** Real names, addresses, plates, and family identities never get persisted to this repository. Use a stable codename (e.g. `PRINCIPAL-ECHO`) and store the codename↔identity mapping in your access-controlled HR/protective system, not here.

## Inputs gathered through interview

### 1. Principal profile (→ `context/project.md`)
- Codename for the principal (assigned by you)
- Public profile sensitivity (low / moderate / high / extreme)
- Industry / role context — what makes them a target
- Family or accompanying parties to consider; do they have separate threat profiles?
- Known prior incidents in the last 24 months (date / type / outcome / case ref)
- Standing open threats believed live

### 2. Engagement / itinerary in scope (→ `context/project.md`)
- Engagement window (start / end / timezone)
- Geography (country, region, city, neighbourhood, permissiveness rating)
- Movement profile (static / single-leg motorcade / multi-leg / mixed)
- Public exposure (closed / semi-public / public / press)
- Local liaison contact, if any

### 3. Detail composition (→ `context/for-agent/environment.md`)
- Headcount and shift pattern
- Medical capability (TCCC / EMT / paramedic / none)
- Counter-surveillance assets
- Comms platform (encrypted / cellular / SatCom)
- Vehicle inventory: for each vehicle — class, curb mass, hardening level, runflats, special features, driver, EVOC level

### 4. Authorities & legal framing (→ `context/project.md` and `context/constraints.md`)
- Lawful basis for protection (contractual / in-house / statutory) and jurisdiction
- Use-of-force authority of the detail (citizen-arrest only / sworn / armed status)
- Vehicle authority (civilian / police escort / lane authority / emergency-vehicle privileges)
- Information-handling authority and applicable data-protection regime

### 5. Detail leader / analyst role (→ `context/role.md`)
- Your role on the detail and years of experience
- Specialisations and accreditations
- Decision authority (cancel / change formation / engage LE)
- Tooling fluency (mapping, matrix authoring, crash kinematics, spreadsheets, Python)
- Output preferences (verbosity, recommendation style, pace)

### 6. Threat environment snapshot (→ `context/project.md`)
- Macro political/security baseline
- Sector-specific threat picture
- Named actors / groups with known interest, evidence-graded
- Capability inventory of likely adversaries (vehicle classes, weapons, surveillance)
- Recent incident base-rate in this geography or against similar principals

## Procedure

1. **Refuse if scope is offensive.** If during the interview the user describes targeting an individual rather than protecting one, refuse, log the refusal in `work-log/<date>.md`, and stop.
2. **Walk the six sections above as a structured interview.** One section at a time; confirm each before moving on.
3. **Write to disk** as you go — do not batch. Each section's responses populate the correct file.
4. **Calibrate the rubric** — read `resources/threat-tier-rubric.md`. Ask whether the principal's class warrants the default tuning or a tighter / looser scale. Save tuning notes to a new `### Principal-specific tuning` section in the rubric.
5. **Summarise** — produce a one-page summary covering: codename, engagement, posture posture-defaults, detail capability, authorities. Save to `outputs/<codename>-onboard-summary.md`.
6. **Recommend next step** — if engagement is < 14 days away → `/risk-matrix` then `/threat-assessment`. If > 14 days → `/risk-matrix` only, with a note to revisit at T-7d.
7. **Log** the onboarding session in `work-log/<YYYY-MM-DD>.md` with: who onboarded, codename, engagement reference, time spent.

## Output

- `context/project.md` populated
- `context/role.md` populated
- `context/constraints.md` reviewed and any principal-specific additions noted
- `context/for-agent/environment.md` populated
- `resources/threat-tier-rubric.md` tuned
- `outputs/<codename>-onboard-summary.md` produced
- `work-log/<date>.md` updated
