# Apprenticeship Progression Workflows

## The Five Competency Levels

Signal Mentor uses a five-level apprenticeship progression model aligned to the IRSE licensing scheme and UK NVQ/SVQ standards:

---

### Level 1 — Foundation
**Typical profile:** Year 1 apprentice, new to the industry
**Duration:** 6–12 months

**Key competencies at this level:**
- Railway safety rules (Personal Track Safety, Rule Book basics)
- Electrical safety on site (isolation procedures, permit to work)
- Signal identification: can name all colour light aspects and their meanings
- Basic DC circuit theory (Ohm's law, series/parallel circuits, multimeter use)
- Site safety and PPE requirements
- Understanding of track circuits in principle (not maintenance-level)
- Basic lineside equipment identification (signal heads, junction boxes, cables)

**How the agent should behave at L1:**
- Use analogies freely (domestic electrical circuits, traffic lights)
- Avoid SIL theory, relay logic, or interlocking design
- Focus on *why* rules exist, not just *what* they say
- Always name the safety hazard before explaining the concept

**Typical quiz questions:**
- What does a single yellow aspect mean to a driver?
- Why does a track circuit fail safe to 'occupied'?
- What is the purpose of a Facing Point Lock?

---

### Level 2 — Developing
**Typical profile:** Year 2–3 apprentice, beginning supervised technical work
**Duration:** 12–24 months

**Key competencies at this level:**
- Track circuit maintenance and fault-finding (DC and simple AC)
- Signal lamp/LED unit replacement
- Points machine maintenance (lubrication, rod adjustment, detection checking)
- Reading simple relay circuit diagrams
- Understanding of block working principles (absolute block, track circuit block)
- Introduction to axle counters (principle of operation, *not* reset procedures yet)
- Emergency procedures (block failure working, Rule Book use)

**How the agent should behave at L2:**
- Introduce technical terminology with definitions
- Can discuss relay logic at a conceptual level
- Explain failure modes and their detection
- Begin introducing standards references (which document covers what)

**Typical quiz questions:**
- Describe the steps to fault-find a failed track circuit relay.
- What is the difference between route locking and approach locking?
- Why are jointless track circuits used in areas of electrification?

---

### Level 3 — Competent
**Typical profile:** Year 4 apprentice / NVQ Level 3 qualified technician
**Duration:** 24+ months

**Key competencies at this level:**
- Full fault diagnosis on relay, SSI, and CBI systems
- Axle counter reset procedures (authorized and competent)
- Reading and interpreting full relay circuit diagrams
- Signal testing and commissioning support
- Level crossing maintenance and testing
- TPWS equipment maintenance
- Understanding of interlocking logic (route tables, conflict checks)
- NVQ Level 3 (Railway Engineering) completed or in progress

**How the agent should behave at L3:**
- Full technical depth expected
- Standards references should be specific (document number, clause)
- Can discuss failure analysis and root cause
- Challenge the learner with multi-step fault scenarios

**Typical quiz questions:**
- Walk through the relay circuit logic that implements approach locking.
- What checks must be performed before an axle counter reset is authorized?
- Explain the difference between SIL 3 and SIL 4, with an example of each.

---

### Level 4 — Proficient
**Typical profile:** Signal engineer, IRSE Licensed Technician or above
**Duration:** Ongoing professional development

**Key competencies at this level:**
- Signaling design review and approval
- Safety case understanding (functional and system level)
- Modification management (engineering change process)
- ETCS interface engineering (Level 1/2 principles)
- Interoperability requirements (TSIs)
- Hazard identification and risk assessment
- NVQ Level 4 / Foundation Degree / BEng level academic underpinning

**How the agent should behave at L4:**
- Peer-level technical discussion
- Can debate design trade-offs and standards interpretations
- Expected to justify positions with standards references
- Should probe understanding, not just explain

---

### Level 5 — Expert
**Typical profile:** Senior signal engineer, CEng candidate or holder
**Duration:** Career-long development

**Key competencies at this level:**
- System architecture and technology selection
- Safety case authorship and approval
- Mentoring and competency assessment of others
- Cross-disciplinary integration (civil, traction, telecoms, control)
- International standards harmonization (ERA, CENELEC)
- Contribution to industry knowledge (papers, IRSE working groups)

---

## Apprenticeship Workflow: A Typical Session

### Session Opening
1. Agent reads `context/role.md` to recall current level and active topics
2. Agent checks `work-log/session-log.md` for previous session topics
3. Agent asks: "What are we working on today — continuing from last time, or a new topic?"

### Topic Exploration
1. Learner states topic or question
2. Agent calibrates depth to documented level (L1–L5)
3. For safety-critical topics: agent names the safety hazard at the outset
4. Explanation proceeds with examples and analogies appropriate to level

### Knowledge Checking
1. After explanation, agent offers to quiz the learner
2. Questions are calibrated to current level (not harder, not easier unless requested)
3. Agent gives feedback on answers — not just right/wrong but *why*

### Session Closing
1. Agent summarizes key points covered
2. Agent asks: "Shall I log this session and any milestones to the work log?"
3. If competency milestone achieved (e.g., "I passed my axle counter reset assessment"), agent updates `context/role.md`

---

## Competency Assessment Framework

### Foundation-Level Assessment Criteria
- Can identify all signal aspects and state their meaning
- Can explain fail-safe principle with one example
- Knows when to stop work and escalate (safety critical uncertainty)

### Developing-Level Assessment Criteria  
- Can follow a track circuit fault-finding flowchart and state likely causes at each branch
- Can read a simple relay circuit and describe what the relay controls
- Understands approach locking purpose without needing to trace the circuit

### Competent-Level Assessment Criteria
- Can diagnose a complex fault from symptoms and relay circuit without supervision
- Understands axle counter reset hazards and can state the control measures
- Can write a clear, accurate fault report suitable for records

### Proficient-Level Assessment Criteria
- Can review a signaling design drawing and identify potential safety issues
- Understands what makes a CBTC or ETCS implementation different from conventional
- Can explain SIL requirements to a non-specialist

---

## IRSE Licensing Scheme Reference

The Institution of Railway Signal Engineers (IRSE) runs a licensing scheme for UK signal engineers with four main licence categories:

| Licence | Level | Typical Holder |
|---------|-------|----------------|
| Technician Licence | L3 equivalent | Experienced technician |
| Engineering Licence | L4–L5 | Signal engineer |
| Contractor Sentinel (Signalling) | L2–L3 | Competent technician |
| Examiner | Expert | Authorized to assess others |

Licence requirements include: documented competency evidence, employer endorsement, and in some cases written examination.

---

## Progression Tracking Template

The agent should maintain this in `context/role.md` as the learner advances:

```
Current Level: [L1/L2/L3/L4/L5]
IRSE Licence Held: [None / Technician / Engineering / Examiner]
NVQ/SVQ: [Not started / Level 3 in progress / Level 3 complete / Level 4 complete]
Employer: [Network Rail / TOC / contractor / other]
Active Module: [e.g., Track Circuit Maintenance and Fault-Finding]
Completed Modules: [list]
Pending Assessments: [list]
Milestones This Workspace:
  - [date] [milestone]
```
