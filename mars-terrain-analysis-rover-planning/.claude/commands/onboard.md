# /onboard — Initialize Mars Terrain Analysis & Rover Planning Workspace

Welcome. I'll gather your mission setup, rover platform, terrain dataset, and reviewer panel so subsequent commands have the right context.

## Interview Flow

### 1. Mission Profile

Ask the user:
- What is the project? (real mission name, analog field test name, concept study, educational exercise)
- What rover platform? (Mars 2020 Perseverance, MSL Curiosity, MER, Rosalind Franklin, custom analog)
- What mission phase? (surface ops, traverse-to-target, sample campaign, extended mission)
- Where on Mars (or analog Earth site)? Lat/lon or feature name.

Save responses to `context/project.md`.

### 2. Strategic Targets

Ask the user:
- What is the current strategic target the rover is driving toward?
- How many sols ahead are you planning? (1-sol tactical / 3–5 sol look-ahead / 10+ sol long-range)
- Are there secondary opportunistic targets?

Save responses to `context/project.md`.

### 3. Terrain Datasets

Ask the user:
- Which orbital products do you have? (HiRISE orthoimage IDs, HiRISE DEMs, CTX coverage, MOLA, project-internal products)
- What resolution is appropriate for current planning? (HiRISE for tactical, CTX for look-ahead)
- Where do the files live on disk?

Save responses to `context/for-agent/environment.md`.

### 4. Rover Platform Specs

Ask the user (or look up from `resources/flight-rules-quickref.md`):
- Wheel diameter and ground clearance
- Max drivable slope (operational, not design)
- Max vehicle tilt
- Drive distance budget per sol
- Solar or RTG power
- AutoNav availability and capability for this rover/FSW version

Save responses to `context/for-agent/environment.md` and confirm against `context/constraints.md` hard flight rules.

### 5. Reviewer Panel

Ask the user:
- Who plays each of the 5 reviewer roles for `/peer-review`?
  - Rover Driver
  - Science PI
  - Mechanical / Safety
  - Autonomy Lead
  - Uplink / Comms Lead
- How are reviewers contacted? (sync meeting, async PR comments, Slack, email)
- For solo / educational use: confirm the planner will play all 5 roles and argue from each perspective.

Save responses to `context/project.md` (panel) and `context/for-agent/environment.md` (channel).

### 6. User Role & Communication Style

Ask the user:
- What is your role? (planner of record, advisor, analog test lead, student)
- Have you used the harmonic framework before, or is this your first exposure?
- Do you prefer the harmonic vocabulary used throughout, or kept on request?
- Comfort level with rover platform mobility specs?

Save responses to `context/role.md`.

### 7. Constraints & Scope

Ask the user:
- Are there planetary-protection Special Regions in the planning area?
- Any embargoed datasets to mark as internal-only?
- Any project-specific flight rules beyond the platform defaults?
- Anything explicitly out of scope (e.g., "don't propose any plan that requires drilling")?

Save responses to `context/constraints.md`.

## Post-Onboard Actions

1. Initialize `planning/plan.md` with the strategic target, current rover position, and sol-N goal.
2. Drop a starter entry in `work-log/<YYYY-MM-DD>.md` summarizing the onboarding.
3. If the rover platform is one of the supported ones, recommend they review `resources/flight-rules-quickref.md` for the correct hard limits.
4. Recommend the first command after onboarding is `/terrain-assess` on the current planning tile.

## Output

Confirm to the user the configuration captured, and list the files updated. Do not proceed to traverse composition until the user confirms the onboarding summary.
