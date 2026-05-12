# /onboard — Initialize Glassblowing Form Shaping Workspace

Welcome. I'll walk you through capturing the studio profile, the glass families you work in, your equipment specs, and the form vocabulary you operate in. The output of this command becomes the baseline that every subsequent `/form-sim`, `/cool-curve`, and `/batch-log` reasons against.

## Interview Flow

### 1. Studio Profile
Ask the user:
- Studio name (or "home studio") and rough physical footprint
- Indoor ambient temperature range (summer high / winter low) — affects working time
- Average relative humidity (matters for cold work and storage, less for hot)
- Hours per week of bench time you typically get
- Solo work, paired (gaffer + assistant), or full team?

Save responses to `context/project.md` (project framing) and `context/for-agent/environment.md` (ambient envelope).

### 2. Glass Families in Use
Ask the user:
- Which COE families do you work in? (Bullseye 90, System 96, Effetre/Moretti 104, Schott Borosilicate 33, other)
- For each family: typical sources/suppliers and the cullet vs. billet vs. rod mix you use
- Any historical incompatibility incidents with specific suppliers? Note them — they go into `resources/failure-mode-taxonomy.md` as a known-bad pairing
- Color palette you most often work in (frit, rod, powder)

Save the COE family list to `context/constraints.md` (these become the COE compatibility guardrails) and supplier history to `resources/glass-viscosity-reference.md` (append).

### 3. Equipment Specifications
Ask the user, capturing each precisely:
- **Glory hole**: max temperature, typical soak temperature, fuel (propane / natural gas / electric), door size constraints
- **Furnace** (if you have one): capacity, melt temperature, glass family loaded
- **Lehr (annealing oven)**: model, max temperature, programmable segments? how many? typical anneal point used (480 °C for soda-lime, 565 °C for borosilicate)
- **Bench**: jacks, blocks (wood blocks soaked in water?), paddles, optic molds available
- **Pyrometer or thermocouple** in glory hole? (changes how precisely we can budget working time)

Save to `context/for-agent/environment.md` as the equipment block.

### 4. Form Vocabulary & Goals
Ask the user:
- What forms do you primarily make? (vessels, sculptural, lighting components, beads, paperweights, plates, goblets…)
- Any specific upcoming pieces or commissions to plan for?
- New techniques you want to learn this quarter (these become the candidates for `/form-sim` first-pass simulation)
- Failure modes that have plagued you historically? (anneal cracks, cord, stuck punties, devit, color mismatch)

Save to `context/project.md` (target form vocabulary, near-term goals) and `context/role.md` (artist's experience, problem areas).

### 5. Documentation Posture
Ask the user:
- Do you currently keep any session log? (notebook, spreadsheet, photos)
- Comfortable letting the agent enforce a structured batch record per session, or want it as an opt-in?
- Are you the only person who works in this studio, or do others (apprentices, renters, classes) also work here? (multi-user studios need batch IDs that include who worked the session)

Save to `context/constraints.md` and `context/role.md`.

## Post-Onboard Actions

1. Write `context/project.md`, `context/role.md`, and `context/constraints.md` from the interview.
2. Populate `context/for-agent/environment.md` with the equipment block and ambient envelope.
3. Pre-flight `resources/glass-viscosity-reference.md` against the user's stated COE families — strip any irrelevant rows so the reference reads cleanly for the studio.
4. Write `planning/plan.md` with the user's stated near-term forms as the initial backlog, each entry stubbed to `pending /form-sim`.
5. Open today's batch record in `work-log/<YYYY-MM-DD>.md` even if no glass is being worked — it's the onboarding session itself, and that's part of the lineage.
6. Print a one-screen summary back to the user: "Here's what I captured, here are the guardrails I'll enforce, here's what to do next."
