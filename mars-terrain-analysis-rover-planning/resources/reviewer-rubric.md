# Peer Review Rubric

The 5-axis × 5-role scoring rubric used by `/peer-review`. Each reviewer scores the candidate on each axis 1–5; primary-axis scores carry hard-fail authority for that role.

---

## Axes

### Feasibility — "Can we drive this as planned?"
- **5 — Excellent.** Drivable end-to-end; no segment requires unusual maneuver; AutoNav handles everything in spec.
- **4 — Good.** Drivable; one or two segments require manual driver intervention (mid-drive imaging, careful approach).
- **3 — Acceptable.** Drivable but tight margins; a slip or hazcam reject mid-drive likely truncates the sol.
- **2 — Marginal.** Drivable only with optimistic assumptions about terrain stability or rover state.
- **1 — Unacceptable (HARD FAIL when scored by Driver).** Plan exceeds operational drive limits or assumes capabilities the rover doesn't have.

### Science Return — "What science does this sol deliver?"
- **5 — Excellent.** Strategic target progress + opportunistic science block + post-drive contact science.
- **4 — Good.** Strategic target progress + opportunistic science.
- **3 — Acceptable.** Either strategic progress *or* a strong science block; not both.
- **2 — Marginal.** Limited science; the sol is mostly a positioning move.
- **1 — Unacceptable (HARD FAIL when scored by Science PI).** Trades all science for marginal positioning, or trades all positioning for marginal science.

### Risk Profile — "What can go wrong, how bad is it?"
- **5 — Excellent.** All segments low-hazard; cadence on a verified parking spot; no half-dim chords; comms-pass coverage redundant.
- **4 — Good.** One acceptable risky segment; clear contingency for it; cadence safe.
- **3 — Acceptable.** Multiple risky segments but each with a contingency; cadence safe.
- **2 — Marginal.** Risky segments without clear contingency; cadence safe but tight.
- **1 — Unacceptable (HARD FAIL when scored by Mech/Safety, Driver, or Autonomy).** Cadence not safe, sustained dissonance, or any forbidden-terrain pixel touched.

### Comms Alignment — "Do passes line up with planned events?"
- **5 — Excellent.** Downlink covers all data products with margin; uplink window is well-positioned for sol-N+1.
- **4 — Good.** Downlink covers all data products; modest data-volume margin.
- **3 — Acceptable.** Downlink fits if no anomalies inflate data volume.
- **2 — Marginal.** Downlink barely fits; a science block re-take would not.
- **1 — Unacceptable (HARD FAIL when scored by Comms Lead).** Plan strands the rover beyond next pass, or planned data exceeds downlink budget.

### Contingency Coverage — "Is there a recovery plan if anything goes wrong?"
- **5 — Excellent.** Every flagged risk has a named contingency; rover has a safe-pose fallback at every segment end.
- **4 — Good.** Major flagged risks have contingencies; some minor ones are implicit.
- **3 — Acceptable.** A drive-abort contingency exists; finer-grained contingencies are unspecified.
- **2 — Marginal.** Drive-abort contingency only — no specific contingencies for flagged risks.
- **1 — Unacceptable.** No contingency specified for any flagged risk.

---

## Roles and Primary Axes

| Role | Primary axes (hard-fail authority) | Secondary axes (score-only) |
|------|-----------------------------------|---------------------------|
| **Rover Driver** | Feasibility, Risk | Comms, Contingency, Science |
| **Science PI** | Science | Feasibility, Risk, Comms, Contingency |
| **Mechanical / Safety** | Risk, Contingency | Feasibility, Science, Comms |
| **Autonomy Lead** | Feasibility (autonomy-specific), Risk | Science, Comms, Contingency |
| **Uplink / Comms Lead** | Comms | Feasibility, Science, Risk, Contingency |

---

## Quorum and Decision Rules

- **Quorum:** at least 4 of 5 reviewers participated.
- **Hard fail:** any reviewer scored 1 on a primary axis. Hard fail blocks approval regardless of average.
- **STRONG PASS:** quorum + no hard fails + average ≥ 4.5 + no individual axis score below 3.
- **PASS:** quorum + no hard fails + average ≥ 3.5.
- **REVISE:** quorum + no hard fails + average 2.5–3.5.
- **REJECT:** any hard fail OR average < 2.5 OR quorum not met.

---

## Dissent Capture (Mandatory)

Any reviewer outvoted on the decision must record their dissent verbatim, in the form:

```
DISSENT
Reviewer role: <role>
Position against: <APPROVAL | REJECTION>
Concern (verbatim):
> <the reviewer's actual concern in their own words>

What would change my position:
> <the specific change that would bring this reviewer to the panel's position>
```

Dissents are not averaged into the score. They are appended to the decision log. Future post-mortems read them first.

---

## Solo-Mode Adaptation

In educational / single-planner use, the planner plays each role in sequence:

1. For each role, write down: "If I were this role, what would I object to in this candidate?" Force at least one objection per role.
2. For each role, write down: "If I were this role, what would I defend?" Force at least one defense per role.
3. Score from each role's perspective using the same 1–5 scale.
4. Apply the same hard-fail and quorum rules (in solo mode, "quorum" means the planner walked through all 5 roles).
5. Capture dissents the same way.

Solo mode is not a relaxation of the rubric — it is more rigorous, because a single planner is at risk of self-confirming. The role-switching exercise is what catches that.
