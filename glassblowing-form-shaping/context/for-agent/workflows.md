# Core Workflows — Glassblowing Form Shaping

Four workflows cover the full life cycle: pre-session simulation, in-session logging, post-session closeout, and post-mortem. Each one names the commands and files involved so the agent can execute them without re-deriving the structure.

## Workflow 1: Pre-Session Form Simulation

**Goal:** before any glass is fired, produce a feasibility verdict, working-time budget, gravity-sag check, COE compatibility check, and recommended cool curve for every form planned today.

### Steps
1. **Open today's batch record skeleton** — `/batch-log` creates `work-log/<YYYY-MM-DD>A.md` if it doesn't exist
2. **For each planned form:**
   1. Capture geometry (mass, max wall thickness, max horizontal reach, distinct features)
   2. Run `/form-sim` — produces verdict + form spec at `planning/form-<slug>-v<n>.md`
   3. If verdict is yellow or red, decide: rework geometry, accept risk explicitly, or remove from today's plan
   4. Run `/scenario-test` against the form spec — produces scenario-test report
   5. If any scenario is red, treat as a hard block unless user explicitly overrides (logged)
3. **Append planned forms to the batch record** — under "Planned Forms" with sim verdict + scenario summary
4. **Pre-flight environment** — measure & log studio ambient °C / RH and glory hole soak temp into the batch record's environmental envelope
5. **Pre-flight lehr** — confirm the lehr program loaded matches the recommended cool curve from `/form-sim` for the largest planned piece; if not, adjust before any work starts

### Decision Points
- **Mixed-COE day:** if today's planned forms span more than one COE family, split into two sessions with separate batch records (no co-occurrence in a single record)
- **Apprentice involved:** if the artist on the bench isn't the workspace owner, create the batch record under the apprentice's name and require sim sign-off from the supervisor before the bench work starts
- **Rushed session:** if pre-flight is being skipped due to time pressure, log the skip in the batch record under a "PRE-FLIGHT SKIPPED" header — this is a finding worth surfacing in retrospectives

## Workflow 2: In-Session Logging

**Goal:** capture every meaningful event during the session as an append-only entry in the day's batch record. Future post-mortems and lineage traces depend on this granularity.

### Steps
1. **Inputs unboxed and entered** — every color rod or new cullet/billet that touches the bench gets logged with lot ID, supplier, color name, COE, and (if applicable) prior-batch leftover linkage
2. **Per-piece, per-gather:** log gather number, time, mass estimate, and which planned form it's for
3. **Per-operation:** log operation type (marver/jack/block/optic/transfer), time, observed result (success / partial / aborted)
4. **Reheats:** log reheat number, time, glory hole reading at reheat (if pyrometer present)
5. **Anomalies:** any deviation from plan — color flake, cord, surface bubble, partial collapse, dropped piece, unscheduled cool — gets its own anomaly entry with timestamp and brief description
6. **Lehr loads:** when each piece goes into the lehr, log time, lehr program ID, and confirm the program matches the planned cool curve
7. **Mid-session re-runs:** if a planned form is abandoned and replaced with a different one, the new form must go through `/form-sim` before being attempted (no improvising past the simulator)

### Decision Points
- **Glory hole crash mid-session:** invoke scenario 1 from `/scenario-test`'s catalog in real time; the in-progress piece is parked in lehr if possible, anomaly logged, recovery decision noted
- **COE compatibility surprise:** if a rod lot is discovered to be from a different COE family than expected, the affected pieces are flagged in the batch record for 90-day successional follow-up (slow-cracker risk)

## Workflow 3: Post-Session Closeout

**Goal:** seal the day's batch record with outcomes, schedule successional follow-ups, and update inventory.

### Steps
1. **Outcomes block:** for each piece produced, record final state (finished / abandoned), mass, geometry confirmation against form spec, lehr position
2. **Lehr program confirmation:** confirm the program actually run matches the planned program; note any controller deviation as an anomaly
3. **Inventory delta:** update the running inventory of color rod lots — what was consumed, what's leftover, what should be returned to stock with explicit lot tagging so it can be lineage-traced if it's used in a future session
4. **Successional follow-ups scheduled:** for every piece, add placeholder rows to the batch record:
   - 24h post-anneal inspection
   - 7d shelf check
   - 30d crack survey (mode 4: residual strain — usually shows by 30d)
   - 90d crack survey (mode 5: COE mismatch slow cracker — can take this long)
5. **Cross-link pieces:** for each finished piece, create or update `outputs/pieces/<piece-id>.md` with form spec link, batch record link, and the scheduled follow-up dates
6. **Update history index:** append the batch ID to `work-log/INDEX.md`
7. **Studio shutdown:** confirm glory hole shut down, lehr program running unattended (with checkback time), and any remaining lit torches extinguished — log shutdown time

### Decision Points
- **Follow-ups overdue:** if today's closeout shows yesterday's 24h inspection wasn't done, surface it before closing today; closing on top of a missed follow-up is bad data hygiene
- **Anomaly count high:** if today's record has > 3 anomalies, prompt for a quick reflection note — what's different about today vs. baseline?

## Workflow 4: Failure Diagnosis (Post-Mortem)

**Goal:** when a piece fails, diagnose the failure, append the finding to the batch record, and update the taxonomy or trigger a lineage trace if the failure is part of a cluster.

### Steps
1. **Trigger:** any time a follow-up inspection finds a crack, devit, or color anomaly, or any time the user reports a failure outside scheduled follow-ups
2. **Run `/post-mortem`** with the piece ID — walks the (When, Where, How) decision tree from `resources/failure-mode-taxonomy.md`
3. **Diagnosis confidence:** if all three Q's converge to one mode → high confidence; two of three → medium; conflicting → low (and log as a research case in `outputs/post-mortems/research-cases/`)
4. **Loop back to batch record:** append a `## Diagnostic Followups` entry to the originating batch record with the diagnosis, confidence, and corrective action
5. **Cluster check:** if this is the third failure of the same primary mode in the last 60 days, automatically trigger `/lineage-trace` on the cluster (Mode B, failure-anchored)
6. **Taxonomy update:** if the diagnosis surfaces a mode not in the taxonomy, append a new node to `resources/failure-mode-taxonomy.md` with version bump
7. **Corrective action backlog:** add an entry to `planning/plan.md` for the next session — concrete change to test (longer hold, slower ramp, alternate rod lot, different punty technique)

### Decision Points
- **Storage thermal shock:** if a piece cracked in storage with no prior failures and no known cause, check if the storage area was exposed to a temperature swing; this is mode 6 territory and may indicate an environmental issue, not a glass issue
- **Repeated failure mode:** if the same primary mode keeps appearing despite corrective actions, escalate to a controlled experiment — same form, same artist, isolated variable test, at least three replicates

## Workflow Cross-References

| Workflow | Calls these commands | Reads these resources |
|----------|---------------------|------------------------|
| 1 — Pre-session sim | `/batch-log`, `/form-sim`, `/scenario-test` | `resources/glass-viscosity-reference.md`, `resources/failure-mode-taxonomy.md` |
| 2 — In-session logging | `/batch-log` (append) | `resources/batch-record-card.md` |
| 3 — Post-session closeout | `/batch-log` (close) | `outputs/pieces/`, `work-log/INDEX.md` |
| 4 — Post-mortem | `/post-mortem`, `/lineage-trace` | `resources/failure-mode-taxonomy.md` |
