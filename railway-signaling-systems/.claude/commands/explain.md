# /explain — Deep-Dive Technical Explanation

Usage: `/explain [topic]`

Examples:
- `/explain track circuits`
- `/explain approach locking`
- `/explain ETCS Level 2`
- `/explain SIL 4 requirements`
- `/explain axle counter reset procedure`

## Explanation Protocol

1. **Read context:** Check `context/role.md` for current level. Calibrate depth accordingly.

2. **Safety flag first:** If the topic has safety-critical implications, state them at the outset:
   > ⚠️ *Safety context: [brief statement of why this matters for safety]*

3. **Explain in three layers:**
   - **What it is** (1–2 sentences, plain language)
   - **How it works** (technical depth calibrated to learner level)
   - **Why it matters / failure modes** (what goes wrong and what the consequences are)

4. **Use analogies** where appropriate (especially L1–L2), but always return to the railway-specific framing.

5. **Reference relevant standards:** Name the document(s) the learner should consult for authoritative detail.

6. **Offer follow-up:** "Want me to quiz you on this, or is there a related concept you want to go deeper on?"

## Depth Calibration Guide
- **L1:** Plain language, domestic analogies, no relay theory
- **L2:** Technical terminology, basic circuit concepts, introduce standards references
- **L3:** Full technical depth, circuit logic, failure analysis, specific standard clauses
- **L4–L5:** Design implications, standards interpretation, trade-offs, safety case considerations
