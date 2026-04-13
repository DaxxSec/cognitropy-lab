# Creation Report: railway-signaling-systems

**Created:** 2026-04-13
**Day Number:** 19
**Domain:** Railway Signaling Systems (Engineering & Technical)
**Technique:** Apprenticeship Progression Tracking
**Crossover:** No

---

## Why This Domain

Railway signaling is an under-represented discipline in AI-assisted learning tools. It is highly specialized, deeply safety-critical, and governed by a tightly controlled professional licensing framework (the IRSE scheme in the UK). Apprentices in this field spend 4+ years working toward NVQ Level 3/4 and IRSE licences, often without access to on-demand expert mentorship between shifts.

The domain sits at the intersection of electrical engineering, software safety, control systems theory, and operational railway practice — making it ideal for an agent workspace that can synthesize technical depth with structured learning guidance.

## Why This Technique

Apprenticeship progression tracking is a natural fit for a domain with:
- A formal, published competency framework (IRSE Licences, NVQ standards)
- Clear level-gating — some concepts genuinely should not be attempted before others
- A long learning arc (4–7 years from new entrant to Proficient level)
- Assessment requirements at multiple milestones

The workspace models five progression levels (Foundation → Expert) and the agent calibrates explanation depth, assessment difficulty, and safety emphasis based on the learner's documented level.

## Design Decisions

- **Safety-first framing throughout:** Railway signaling kills people when it fails. The CLAUDE.md explicitly instructs the agent to never simplify away safety context. Every concept explanation must acknowledge its safety-critical implications.
- **Historical incident analysis command (`/incident`):** Learning from real failures is a core pillar of engineering education. Ladbroke Grove (1999, 31 deaths), Potters Bar (2002), and Grayrigg (2007) are included as canonical case studies.
- **Standards-anchored content:** Rather than vague references to "industry standards," the domain knowledge file names specific documents (IEC 62279, EN 50128, NR/SP/SIG series, ERA ETCS Subsets) so learners can find primary sources.
- **ETCS/ERTMS included:** Modern railway hiring increasingly requires ETCS knowledge. Including Level 1/2/3 application modes future-proofs the workspace.
- **Competency table in README:** The progression levels are visible at-a-glance so a new user can immediately locate themselves on the map.

## Persona: Signal Mentor

The agent persona was named Signal Mentor to reflect its role as an experienced practitioner guiding a less experienced one — the essence of the apprenticeship model. It does not pretend to be a colleague or peer; it positions itself as a knowledgeable mentor who has seen systems fail and knows why the rules exist.

## Connection to Cognitropy Engine

- **Seed date:** 2026-04-13 (Day 19)
- **Engine selection:** Primary category Engineering & Technical, domain Railway Signaling Systems
- **Technique applied:** Apprenticeship progression tracking shapes the entire workspace structure — competency levels, the `/progress` command, quiz difficulty calibration, and the onboarding flow all derive from this technique

---

*Cognitropy Lab — one domain per day, every day*
