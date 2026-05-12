# /onboard — Workspace Initialization

Walk a new user through configuring this workspace for their company, productions, and puppet inventory. Populates `context/project.md`, `context/role.md`, and `context/constraints.md`. Establishes the peer-review roster.

## Required Inputs

None — this is the bootstrap command. The agent prompts for everything.

## Steps

### 1. Identify the Company and Production

Ask:
- Company name?
- Productions currently in scope (one or many)?
- Touring or resident?
- Performance cadence (shows / week)?

Write the answers to `context/project.md` under the **Production / Company** section.

### 2. Build the Puppet Inventory

For each puppet, ask:
- Slug / call-name (kebab-case)
- Type (string-marionette / hand / rod / bunraku / shadow / animatronic / stop-motion)
- Materials (body, limbs, skin / latex, strings)
- Articulation count and rough joint list
- Control rig (airplane / paddle / triple-actor / glove / multi-rod / servo-driven)
- Mass including rigging
- Existing calibration baseline file? (if not, schedule a `/calibration-audit` for after onboard)

Write to `context/project.md` under **Puppet Inventory**. For each puppet, create an empty stub at `outputs/baselines/<slug>.yml` with the comment "awaiting first /calibration-audit".

### 3. Establish the Peer-Review Roster

Critical step — without two distinct-role reviewers, the `/peer-review` command will refuse to run.

Ask:
- Who can review puppeteer-side (timing, phrasing)?
- Who can review rigger-side (mechanism, materials)?
- Who can review dramaturg-side (dramatic intent)?
- Who can review tradition-bearer-side (only if the company works in a living-lineage tradition)?

Each reviewer needs: name, role, default review color (red / blue / purple), contact handle.

Write to `context/project.md` under **Peer-Review Roster**.

### 4. Capture User Role and Communication Preferences

Walk through `context/role.md`:
- Primary role
- Experience on each side (puppetry, detection engineering, peer review, Laban)
- Tradition / school
- Communication preferences (which vocabulary defaults; explanation depth)
- Time budget per session

### 5. Establish Constraints

Walk through `context/constraints.md` confirming the artistic, safety, privacy, and detection-engineering defaults. Modify per company specifics; flag any default the user wants to relax (and note that relaxing the "two distinct-role reviewers" rule is not supported).

### 6. Sanity-Check the Failure-Mode Catalog

Open `resources/puppet-mechanism-failure-modes.md` and walk the user through the tactic × technique grid. Ask:
- "Which tactics apply to your puppets?"
- "Are there tactics or techniques specific to your tradition that are missing?"

Note any gaps; do not edit the catalog unilaterally — gaps become a draft proposal queued for the first `/peer-review` pass.

### 7. Schedule the First Calibration Audit

For each puppet in the inventory, create a stub plan in `planning/<slug>-calibration-baseline.md` for the first `/calibration-audit`. The audit must run before any `/movement-log` is replayable against quantitative rules.

## Output

- Populated `context/project.md`, `context/role.md`, `context/constraints.md`.
- Empty baselines stubbed for each puppet.
- Calibration audit plans queued in `planning/`.
- Confirmation message naming the peer-review roster and the first scheduled audit.

## Failure Modes

- **Single-reviewer roster.** If the user can only name one reviewer, write that fact to `context/project.md` and warn explicitly: `/peer-review` will refuse until a second distinct-role reviewer is named.
- **No baseline calibration possible yet (e.g. puppets are mid-build).** Mark each baseline stub `awaiting puppet completion` and tell the user `/movement-log` and `/detect-anomaly` will run in narrative-only mode until baselines exist.
