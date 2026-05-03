# /batch-log — Open or Update a Session Batch Record

Open a structured batch record for the current studio session. Modeled directly on the soil-microbiome plot intervention card schema (see `resources/batch-record-card.md`). Every studio session must have one record; every action that touches glass appends to that record.

## Required Inputs
- Date (defaults to today)
- Session sequence letter if multiple sessions occur the same day (`A`, `B`, `C`…)
- Artist name (defaults to onboarded user; required if studio is multi-user)

## Procedure

### 1. Resolve or Create the Batch Record
Path: `work-log/<YYYY-MM-DD><seq>.md` (e.g. `work-log/2026-05-03A.md`).
- If the file exists, open it for append
- If not, create it from the canonical template in `resources/batch-record-card.md`

### 2. Header Block
Populate (or confirm if existing):
- **Batch ID:** `<date>-<seq>` (e.g. `2026-05-03-A`)
- **Artist:** name
- **Glass family:** the primary COE family for this session (one only — incompatible families do not co-occur in a session)
- **Studio:** location identifier
- **Pre-session glory hole soak:** measured °C
- **Pre-session lehr program loaded:** program ID or summary
- **Pre-session ambient:** °C / RH

### 3. Inputs (Lineage Block)
For each material entering the session, capture:
- Glass cullet/billet melt ID (or "fresh from supplier batch <ID>")
- Each color rod lot, supplier, color name, COE
- Any prior-session leftover stock used (with originating batch ID — this is the lineage edge)

### 4. Planned Forms
List the forms planned for the session, each as:
- Form name + spec file path (`planning/form-<slug>-v<n>.md`)
- Sim verdict (green/yellow/red)
- Scenario test summary (e.g. "7/7 green" or "1 yellow: gather over-mass — accepted")
- Refuse to log a planned form whose sim verdict is red without an explicit user override (and log the override prominently)

### 5. In-Session Append
As the session proceeds, the user (or an assistant prompted by the agent) appends one entry per significant event:
- **Gather n** at HH:MM, mass estimate
- **Operation** (marver / jack / block / optic / transfer) at HH:MM, observed result
- **Reheat** at HH:MM, glory hole reading if available
- **Lehr load** at HH:MM, lehr program confirmed
- **Anomaly** — any deviation from plan (color flake, cord, surface bubble, partial collapse)

### 6. Outcome Block (Closeout)
At session end:
- **Pieces produced:** list with form name, mass, finished/abandoned state, lehr position
- **Lehr program actually run:** confirm matches planned, note any controller deviations
- **Cleanup notes:** broken color rods left over (return to inventory, log lot for next session)
- **Successional follow-ups scheduled:** 24h post-anneal inspection, 30d shelf check (these become rows in the day's record, with placeholder lines to be filled in later)

### 7. Cross-Linking
- Update `cognitropy-history.json` style ledger: append the batch ID to a session index in `work-log/INDEX.md` if it exists (create if missing), so `/lineage-trace` can find it without filesystem scanning
- For each piece produced, add a one-line entry to `outputs/pieces/<piece-id>.md` that links back to the batch record

### 8. Successional Follow-Up Pass
When the user runs `/batch-log` for a date that has open follow-ups from earlier records, surface those follow-ups first and prompt for completion before opening today's session record.

## Output
A single, append-only markdown record per session, structured so that 12 months from now `/lineage-trace` can answer "which batches used color rod lot R-2026-04-Effetre-Cobalt?" with a grep.
