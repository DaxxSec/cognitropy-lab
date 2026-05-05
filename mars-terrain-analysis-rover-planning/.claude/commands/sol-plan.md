# /sol-plan — Synthesize the Final Sol Plan

Combine the reviewed traverse with the science block, comms passes, and contingencies into the final uplink-ready sol plan.

## Required Inputs

- A candidate that has PASSED `/peer-review` (decision log path)
- Sol number, sol date, sol-relative comms-pass schedule
- Science block draft from the science team (or a placeholder for the SOWG to fill)
- Energy budget (RTG output if RTG; predicted insolation if solar)
- Any active dissents from the decision log that affect the plan

## Procedure

### 1. Verify Eligibility

Refuse to proceed unless:
- A `/peer-review` decision log exists for the candidate with decision = PASS or STRONG PASS
- The candidate has not been modified since the decision log was written (verify by hash)
- Comms passes are scheduled for the sol (no plans without at least one downlink window)

### 2. Build the Sol Skeleton

A standard sol plan has these blocks; each block has a start time (sol-local, expressed as Local True Solar Time for solar rovers or as elapsed-from-sol-start for RTG):

```
sol-N plan
├── Pre-drive housekeeping  (engineering checkout, mast unstow if needed)
├── Pre-drive science       (mast cameras, opportunistic ChemCam/SuperCam, environmental monitoring)
├── Drive block             (the reviewed traverse)
├── Post-drive imaging      (mandatory hazcam / navcam panorama for next-sol planning)
├── Post-drive science      (contact science if rover came to rest at a science target)
├── Comms passes            (downlink to MRO/Odyssey/MAVEN/TGO; uplink window if planned)
├── Overnight thermal       (passive cooling; heater management)
└── Pre-handoff state       (final pose, mechanism state, energy state for sol-N+1 planner)
```

### 3. Place the Drive Block

- Insert the reviewed traverse as the drive block.
- Compute drive-end time from segment drive-time estimates.
- Reserve a buffer (default: +20% of the drive block duration) for stop-and-think pauses, hazcam pauses, or AutoNav corrections.

### 4. Place Science Blocks

- Pre-drive science: typically opportunistic, low-cost observations.
- Post-drive science: high-cost (drilling, contact instruments) only if reviewed and approved separately.
- Honor any **dissent-derived recommendations** from the decision log (e.g., the science dissent recommending a 30-min SuperCam raster at WP-3 — schedule it during a planned drive pause).

### 5. Place Comms Passes

- Each pass has a start time, an orbiter (relay), and an estimated data volume.
- Verify the rover is in line-of-sight to the relay during the pass; if not, escalate (this is a flight-rule violation that should have been caught at `/peer-review`).
- Verify the data-volume budget: total downlink ≥ total observation data volume.
- Plan the uplink window for sol-N+1's plan (if not already planned).

### 6. Build the Contingency Block

Every sol plan has at least one contingency:

| Trigger | Action |
|---------|--------|
| Drive aborts on hazcam reject | Stop, snap full panorama, downlink, await sol-N+1 plan |
| Slope exceeded mid-segment | Stop, log telemetry, downlink |
| Mechanism fault | Safe pose, downlink, await intervention |
| Comms-pass missed | Buffer downlink to next pass; do not retry science to free memory |

Pull contingencies from the dissents and from the candidate's flagged segments.

### 7. Render the Sol Plan

Save to `outputs/sol-plans/<sol>-<YYYY-MM-DD>.md` in the canonical format:

```markdown
# Sol <N> Plan — <YYYY-MM-DD>

**Approved by:** see decision log <path>
**Rover platform:** <platform>
**Strategic target:** <target name>
**Data-volume budget:** <bits>

## Timeline

| LTST | Block | Detail |
|------|-------|--------|
| 09:30 | Pre-drive housekeeping | Mast unstow; HGA stow check |
| 10:00 | Pre-drive science | Navcam 360°; SuperCam mast LIBS opportunistic targets |
| 10:45 | Drive block | Sol-<N> reviewed traverse, candidate <id>, decision log <path> |
|       |   ├ WP-0 → WP-1 | 6.2 m, bedrock-flat → bedrock-inclined (ii chord) |
|       |   ├ WP-1 → WP-2 | 8.1 m, contoured around ripple field (tritone sub from rev2) |
|       |   ├ ... | ... |
|       |   └ WP-N park | bedrock-flat-strategic, cadence (I) |
| 13:30 | Drive-end imaging | Full hazcam + navcam panorama for sol-<N+1> planning |
| 14:00 | Post-drive science | SuperCam raster on layered outcrop (per science dissent) |
| 16:30 | MRO downlink pass | ~250 Mbit |
| 22:00 | Mars Odyssey relay pass | ~50 Mbit |

## Contingencies
- **Drive abort:** stop, full panorama, await sol-<N+1>
- **Slope exceeded at WP-3:** safe pose, log telemetry, downlink
- **Comms pass missed:** buffer to TGO 04:00 LTST sol-<N+1>

## Open Items / Dissents Carried
- Science PI dissent: WP-3 SuperCam raster scheduled for 14:00 — confirm fits data-volume budget.

## Handoff State (Predicted)
- End-of-sol position: WP-N (lat, lon)
- Heading: <deg>
- Mechanism: nominal
- Energy: <%>
- Memory: <% used>

## Provenance
- Candidate: <path to candidate file>
- Cadence report: <path>
- Decision log: <path>
- Hazard map: <path>
```

### 8. Cross-Link All Artifacts

Update `planning/plan.md` with a "Sol N planned" entry pointing to:
- The candidate file
- The cadence report
- The decision log
- The final sol plan

### 9. Log to Work-Log

`work-log/<YYYY-MM-DD>.md`: brief summary of the sol-plan synthesis, any deviations from the decision-log dissents, and explicit confirmation that the data-volume budget was honored.

### 10. Hand Off

Print:
- The sol-plan path
- The handoff state for the next planner
- Any items the uplink team needs to confirm (data volume, mast unstow timing, contingency triggers)

## Output

The final sol plan in `outputs/sol-plans/`, plus updates to `planning/plan.md` and `work-log/`. This is the artifact handed to the uplink team.
