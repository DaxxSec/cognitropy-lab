# Diplomatic Security Advance Planning — Workflows and Methodology

Step-by-step procedures the agent uses for advance planning, surveys, contingency activation, and post-trip review. Each workflow maps to one or more bespoke commands in `.claude/commands/`.

## Workflow 1: Pre-Trip Advance (T-30 → T-0)

**Goal:** Take a protectee visit from initial notification to ready-for-arrival posture, with every artifact signed off.

### Steps

1. **T-30: Strategic kickoff** — receive trip notification; establish embassy DCM + host-nation liaison; activate intel feed; draft itinerary.
2. **T-21: Threat picture lock-in (initial)** — first `/threat-stream-synthesis` brief; establish trip threat tier per jurisdiction.
3. **T-14: Tactical advance begins** — venue list locked; run `/venue-survey-checklist` for each venue; queue in-person surveys.
4. **T-14: Route candidates identified** — run `/route-recon-report` for primary + alternates per increment.
5. **T-10: Coordination matrix** — run `/jurisdiction-coord-matrix`; engage host-nation POCs; confirm coordination commitments.
6. **T-7: Motorcade configs** — run `/motorcade-config` per increment; review with detail leader.
7. **T-7: Contingency tree** — run `/contingency-tree`; walk through with detail.
8. **T-5: Comms audit** — run `/comms-redundancy-audit`; test dead-zone mitigations in person.
9. **T-3: Rehearsal** — full team walkthrough of contingency branches; motorcade rehearsal on primary route.
10. **T-2: Final threat picture** — `/threat-stream-synthesis` final pre-arrival; re-tier if needed; revise motorcade / contingency if tier changed.
11. **T-1: Detail handover** — outgoing advance team hands off to detail; deviation log opened.
12. **T-0: Activation** — protectee arrives; detail operates; advance closes.

### Decision points

- **If threat tier escalates** at any phase → re-engage motorcade + contingency + comms with new tier; do not silently absorb.
- **If a venue can't be surveyed in person before trip** → flag as elevated risk; either restructure, virtual-survey + remote-eyes verify, or cancel increment.
- **If host-nation will not commit to requested coordination** → escalate via DCM; document gap; consider trip restructure.

---

## Workflow 2: Venue Site Survey (In Person)

**Goal:** Produce a signed-off venue survey checklist tied to venue type and threat tier.

### Steps

1. Read venue-type-specific section of `context/concepts.md` "Venue-survey methodology".
2. Arrive at venue with checklist (from `/venue-survey-checklist`).
3. Walk the venue with venue POC; observe + document each checklist item.
4. Photo-document vulnerability-relevant items (sightlines, standoff distances, evac routes).
5. Identify deviations from protocol expectation; document with proposed mitigation.
6. Sign off checklist with advance agent + venue POC + (later) RSO.
7. Upload to trip artifacts directory.

### Decision points

- **If venue refuses photo documentation** → escalate to RSO; venue may need to be removed from increment.
- **If venue's standoff distance falls below protocol minimum** → motorcade staging adjustment OR venue alternative OR increment cancellation.

---

## Workflow 3: Route Reconnaissance (In Person)

**Goal:** Drive primary + alternates at multiple times of day; document chokepoints, hospital pre-positioning, IED-hide assessment.

### Steps

1. From `/route-recon-report` template, drive primary at peak, off-peak, overnight.
2. Drive Alt-A at peak (when primary is most likely to fail).
3. Drive Alt-B once for baseline; cross-check satellite imagery for validation.
4. Per drive, document chokepoints (timestamps, photos, alternate-availability times).
5. Coordinate with host-nation police for traffic plan agreement on primary.
6. Coordinate with EMS for pre-positioning at primary's worst-case segment.
7. Coordinate with primary hospital for trauma-protocol activation availability.

### Decision points

- **If chokepoint mitigation isn't available** on a route → motorcade config compensates OR route is dropped.
- **If hospital pre-positioning time is unacceptable** → request air-EMS standby OR co-locate medical asset in motorcade OR consider route restructure.

---

## Workflow 4: Threat-Stream Synthesis (Daily)

**Goal:** Daily TBA brief for the detail leader + RSO, every day during pre-trip and visit.

### Steps

1. Per `/threat-stream-synthesis`, pull all sources daily.
2. Classify + score each new item (specificity, credibility, recency).
3. Aggregate to trip-tier impact assessment.
4. Brief detail leader + RSO within 12 hours of synthesis.
5. Archive TBA to trip artifacts directory.

### Decision points

- **If direct threat surfaces** → immediate escalation (do not wait for next scheduled brief).
- **If a source goes silent during active feed window** → flag possible coverage gap; reach via alternate channel.
- **If multi-source corroboration is missing on high-impact item** → caveat appropriately; don't drive trip-config changes off single-source.

---

## Workflow 5: Contingency Activation (Real-Time, In-Trip)

**Goal:** Execute the documented contingency tree when a triggering event occurs.

### Steps

1. Trigger observed (medical, hostile, civil disturbance, vehicle failure, comms loss).
2. Detail leader announces trigger condition on primary comms; team acknowledges per role.
3. Immediate actions (first 30 seconds) executed per branch — formation change, evac route, comms escalation.
4. Decision authority determines continue vs. abort trip.
5. Short-term actions (1-5 min) executed — host-nation notification, embassy notification, family notification.
6. Sustained actions executed (beyond 5 min) — incident management, additional asset request, threat-tier escalation.
7. Document the activation in the deviation log + post-event narrative.

### Decision points

- **If real-time conditions don't match any tree branch exactly** → detail leader judgement, documented for AAR.
- **If decision authority is unclear (RSO away, detail leader injured)** → pre-designated succession kicks in; do not improvise.

---

## Workflow 6: Post-Trip AAR (Within 72 Hours)

**Goal:** Document what worked, what didn't, and what protocol revisions follow. Feed findings into the practice's protocol library.

(Full steps in `/aar-debrief`.)

### Cross-trip patterns shared by all AAR work

- AAR is candid by design — protect openness by separating from performance-review channels.
- Pattern findings across trips matter more than per-incident findings.
- Protocol revisions must be specific, actionable, accountable.
- Within 72 hours is non-negotiable — memory fades fast.
