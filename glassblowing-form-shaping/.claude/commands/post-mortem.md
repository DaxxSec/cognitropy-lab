# /post-mortem — Failed Piece Diagnosis

Diagnose a failed piece against the failure-mode taxonomy. Append the diagnosis to the originating batch record so future `/lineage-trace` calls can find it. Update the taxonomy if the diagnosis surfaces a new mode.

## Required Inputs
- Piece ID (or, if no ID, enough description to find the batch record)
- Failure description: what cracked, when, what the fracture surface looks like
- Photo paths if available (the agent doesn't process images, but the user can describe what they see)

## Procedure

### 1. Resolve the Originating Batch
Find the batch record that produced this piece. If the piece has no batch record, that itself is a finding — log it and note that future pieces must be batch-logged before they can be diagnosed.

### 2. Walk the Taxonomy
Use the diagnostic decision tree from `resources/failure-mode-taxonomy.md`:

#### Q1: When did the failure occur?
- **A1.** During working (at the bench): cold check — the piece was worked too cold or had a cold tool contact a hot surface
- **A2.** Immediately on transfer to lehr: thermal shock — sudden ΔT exceeded glass tensile strength
- **A3.** During anneal cycle: anneal crack — cool curve too steep for wall thickness
- **A4.** After lehr cycle complete, within 24h: residual strain — anneal hold was too short, or strain-to-room ramp was too steep
- **A5.** Days to weeks after: COE mismatch (slow cracker) — incompatibility between joined glass families
- **A6.** Months later or seemingly random: storage thermal shock or coldwork-induced surface stress

#### Q2: Where did the crack initiate?
- **B1.** From the punty mark: punty pickup ΔT was too high
- **B2.** At a color/cane interface: COE incompatibility
- **B3.** At the wall thickness inflection: anneal crack (gradient stress at thickness change)
- **B4.** From a surface inclusion or bubble: cord, devit, or contamination
- **B5.** Through the body with no clear initiation: residual strain from anneal hold too short
- **B6.** From a coldwork edge: surface stress concentration

#### Q3: Fracture surface character
- **C1.** Smooth conchoidal: clean glass failure, classic stress crack
- **C2.** Crystalline / cloudy at the surface: devit-driven (devit reduces surface tensile strength)
- **C3.** Branching / radial: high-energy thermal shock (A2 confirmed)
- **C4.** Single straight crack at a feature line: anneal crack (A3 confirmed)

### 3. Combine Q1+Q2+Q3 to a Diagnosis
The taxonomy's decision matrix maps the (When, Where, How) tuple to a primary failure mode plus contributing factors. Common combos:
- (A4, B5, C1) → residual strain from short anneal hold — increase hold by 50% next time at this thickness
- (A3, B3, C4) → anneal crack at thickness change — slow the anneal-to-strain ramp
- (A5, B2, C1) → COE mismatch — pull suspect color lot via `/lineage-trace`
- (A1, B1, C1) → cold punty — pre-heat punty in glory hole next time
- (A6, B6, C1) → coldwork-induced stress — reanneal pieces post-coldwork at anneal point for 30 min

### 4. Write Up the Diagnosis
Save to `outputs/post-mortems/<piece-id>-<date>.md` with:
- The (When, Where, How) tuple
- Primary mode + contributing factors
- Confidence (high if all three Q's converge to one mode; medium if two of three; low if conflicting evidence)
- Recommended corrective action for future pieces of similar geometry / glass family

### 5. Loop Back
- Append the post-mortem link to the originating batch record under a `## Diagnostic Followups` section
- If the same primary mode now appears in N ≥ 3 post-mortems within a 60-day window: trigger a `/lineage-trace` automatically (pass it the piece IDs of the cluster)
- If the diagnosis surfaces a mode not in the taxonomy (rare but possible): add a new node to `resources/failure-mode-taxonomy.md` and version-bump the file

### 6. Output to User
A short summary:
- Diagnosis with confidence
- One concrete change for the next attempt
- Link to the post-mortem file and the originating batch record
