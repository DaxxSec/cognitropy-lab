# /incident — Historical Incident Analysis

Usage: `/incident [incident name or brief description]`

Examples:
- `/incident Ladbroke Grove 1999`
- `/incident Potters Bar 2002`
- `/incident Grayrigg 2007`
- `/incident Quintinshill 1915`
- `/incident SPAD at a junction — driver failed to acknowledge AWS`

## Incident Analysis Protocol

This command is for learning from real and hypothetical signaling failures. The goal is not to assign blame but to extract engineering and organizational lessons.

## Analysis Structure

1. **Incident Summary:** What happened, when, where, and the immediate consequences.

2. **Signaling Chain of Events:** Walk through the signaling state at each stage — what was the signal aspect, what did the interlocking allow, what train detection showed.

3. **Contributory Factors:**
   - Equipment factors (was there a signaling failure, and if so, was it a design flaw, maintenance gap, or wear-out?)
   - Human factors (driver, signaller, maintainer — what did they know, what did they do?)
   - Organizational factors (management pressure, maintenance backlog, training gaps)
   - Standards/regulatory factors (were the rules followed? were the rules adequate?)

4. **What Signaling Changes Resulted?** (Rule changes, technical requirements, new equipment mandated)

5. **Calibrated Lesson for Learner's Level:**
   - L1: "The fundamental lesson here for anyone starting in the industry is..."
   - L2–L3: "From a maintenance and fault-finding perspective, this incident shows..."
   - L4–L5: "From a design and safety case perspective, the key engineering lesson is..."

## Important Framing Note

Always frame incidents as learning opportunities, not entertainment. These events caused deaths. Present the analysis with the appropriate weight — acknowledge the human cost, then extract the technical and organizational lessons methodically.

Encourage the learner to think: "What would I have done differently at each stage, given what was known at the time?"
