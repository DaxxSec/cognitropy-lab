# Workflows — Running Assessments as Graded Apprenticeship Artifacts

The technique that shapes this workspace is **apprenticeship progression tracking**: every operational workflow below is run *by a named apprentice* and produces evidence that flows into the progression loop in §4.

---

## 1. The dual-purpose assessment loop (the master workflow)

```
                ┌─────────────────────────────────────┐
                │  /apprentice-tasking                 │
                │  (assign next EPA at edge of ability)│
                └───────────────┬─────────────────────┘
                                ▼
        ┌──────────────────────────────────────────────┐
        │  Operational command (EPA-1…7)                │
        │  apprentice authors the assessment under      │
        │  the entrustment level they currently hold    │
        └───────────────┬──────────────────────────────┘
                        ▼
        ┌──────────────────────────────────────────────┐
        │  /competency-signoff                          │
        │  grade artifact vs rubric → log WBA evidence  │
        └───────────────┬──────────────────────────────┘
                        ▼
        ┌──────────────────────────────────────────────┐
        │  /progression-review (at cadence)             │
        │  update ladder + entrustment, find weakest EPA│
        └───────────────┬──────────────────────────────┘
                        └───────────► back to /apprentice-tasking
```

The operational quality of the artifact is graded first; the development signal is a by-product that never distorts the operational grade.

---

## 2. Protective-intelligence & threat-assessment methodology

### 2.1 Establish the baseline (`/protectee-risk-profile`)
1. Inventory **exposure factors**: public profile, wealth/visibility, controversy, prior incidents, family, residences, travel, digital footprint, predictable patterns.
2. Map the **threat landscape**: who would target this principal and why (grievance, ideology, extortion, IPV/insider, fixation, opportunistic).
3. Combine into a **risk tier** (see `references.md` rubric) with explicit justification.
4. Output drives every downstream command (what to advance, which actors to assess).

### 2.2 Work up an actor (`/adversary-assessment`)
1. Score **capability** (means, skills, access to weapons), **intent** (stated, inferred, trajectory along the path to intended violence), **opportunity** (proximity, knowledge of routine).
2. Apply BTAM lenses (TRAP-18 proximal behaviours, hunter vs howler, leakage).
3. Classify and recommend management (monitor / interview / law-enforcement referral / hardening).

### 2.3 Locate interdiction (`/attack-cycle-map`)
1. Place the actor on the **hostile planning cycle** (concepts §1.3) using observed indicators.
2. For each remaining phase, list the **detection signature** and the **cheapest protective interdiction**.
3. Recommend the highest-leverage window (usually pre-attack surveillance).

### 2.4 Harden the ground (`/advance-survey`, `/route-threat-analysis`, `/surveillance-detection-plan`)
- **Advance**: CPTED walk → CARVER the site from the adversary's view → fix safe haven, medical, command post, EAP hooks → derive *decisions*, not just an inventory.
- **Route**: primary/alternate/emergency routes; mark choke points, ambush geometry, AOP drill points, timing windows; never present a single-route plan.
- **SDR**: design a route that forces a follower to commit; build the pre-attack-indicator watch list (TEDD); define what a "hit" triggers.

### 2.5 Plan for failure (`/eap-builder`)
1. For the scenario (AOP, medical, fire, vehicle), write **immediate actions** in get-off-the-X order.
2. Assign roles, triggers, rally points, comms, and the nearest trauma center.
3. Table-top it; the rehearsal doubles as a WBA of junior agents' immediate-action competency.

---

## 3. Advance-survey decision tree (worked detail for EPA-1)

```
Arrive at site
  → Is there a defensible safe haven within 30s of the principal's position?
       no → flag CRITICAL vulnerability; design a hold room or reconsider the venue
       yes → continue
  → Is the nearest Level I/II trauma center > 20 min by primary route?
       yes → pre-stage medical / alternate; note in EAP
       no → record time-distance; continue
  → Are arrival/departure points observable from uncontrolled public space?
       yes → screen, vary timing, add counter-surveillance at embus/debus
       no → continue
  → CARVER the site: any single point whose loss = mission failure?
       yes → mitigate or add redundancy
  → Produce: routes (primary/alt/emergency), safe haven, medical, command post,
    access plan, site EAP, and a vulnerability register with owners.
```

---

## 4. The progression workflow

### 4.1 Grading an artifact (`/competency-signoff`)
1. Identify the **EPA(s)** the artifact evidences and the **Miller level** it reaches (knows-how / shows-how / does).
2. Score against the rubric dimensions (completeness, threat reasoning, decisions-derived, reproducibility, communication).
3. Assign an **entrustment observation** for this instance (1–5) with a one-line justification.
4. Append a dated, signed evidence record to the apprentice's portfolio in `outputs/`.

### 4.2 Reviewing progression (`/progression-review`)
1. Aggregate portfolio evidence per EPA; require **multiple independent observations** before raising an entrustment level (no single-artifact promotions).
2. Update the apprentice's **Dreyfus stage** when the pattern across EPAs supports it.
3. Identify the **weakest EPA** (lowest entrustment or thinnest evidence) — the deliberate-practice target.
4. Record explicit **entrustment decisions** with rationale; flag any EPA where live-operation use should still be bounded.

### 4.3 Tasking deliberate practice (`/apprentice-tasking`)
1. Take the weakest EPA from the review.
2. Choose a real or scenario assignment that exercises *exactly* that competency, one entrustment level above where they are comfortable (the edge of ability).
3. Set the scaffolding to remove (cognitive-apprenticeship fade) and the specific feedback target.
4. Assign supervisor, due date, and the WBA that will close the loop.

---

## 5. Cadence

| Activity | Trigger / cadence |
|---|---|
| `/protectee-risk-profile` | Engagement start; material change in principal's profile |
| Operational EPA commands | Per movement / per threat as it arises |
| `/competency-signoff` | Immediately after each artifact is produced |
| `/progression-review` | Monthly, or before any entrustment-level change |
| `/apprentice-tasking` | After each progression review |
| AAR (prompt) | After every live operation and every drill |
