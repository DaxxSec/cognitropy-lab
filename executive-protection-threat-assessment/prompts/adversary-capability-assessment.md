# Adversary Capability Assessment Prompt

## Purpose
Profile a named adversary (group or individual) for inclusion in the engagement matrix's "intent + capability + opportunity" scoring. Lawful-collection only; no targeting language; no mischaracterisation of non-violent activity as threat-of-violence.

## Prompt Template

I need to score the threat from the following named adversary in the active engagement matrix:

- **Adversary identifier (codename or group abbreviation):** [...]
- **Type:** [criminal / activist with documented violent history / terrorist designation / ideologically-motivated lone actor / state-affiliated / other]
- **Why we're scoring them:** [specific public statement, prior incident pattern, named threat, sector exposure, etc.]
- **Geography of operation:** [...]
- **Available reporting in last 24 months:** [paste sources or attach]

Please walk through the adversary capability assessment:

1. **Intent grading**
   - What documented public statements, manifestos, or claimed actions tie this adversary to the principal or principal's class?
   - Score Intent 1–5 against the rubric in `domain-knowledge.md` §1.2
   - Cite evidence (source, grade A/B/C/D)

2. **Capability inventory**
   - Vehicles previously used or accessed (attacker classes, per `crash-energy-reference.md`)
   - Weapons or weapon-equivalents previously used
   - Surveillance / technical capability (drone, RF, cyber)
   - Funding indicators
   - Operational tradecraft level (single attempt / sustained pattern / coordinated)

3. **Opportunity for this engagement**
   - Geographic overlap (do they operate where the engagement is?)
   - Schedule visibility (could they access the principal's itinerary?)
   - Access to the venue or route
   - Surveillance / pre-attack indicators detected in the last 14 days

4. **Composite likelihood score**
   - Conservative median of Intent / Capability / Opportunity
   - Map to the matrix's Vehicle-borne, Targeted physical, IED, Surveillance, and Cyber rows
   - Update the engagement matrix only if scores rise; recalibration mode only

5. **Crash-kinematics implication**
   - If the Capability inventory includes a documented vehicle class, hand off to `/crash-kinematics` with that class as the credible attacker for the engagement's most exposed leg

6. **Hard constraints — must respect**
   - Do not characterise lawful protest, journalism, or political opposition as a threat without specific evidence-A linkage to a credible threat-of-violence narrative
   - No purchased data of dubious provenance
   - No unlawful surveillance methods used in collection

## Expected Output

- Adversary profile (codename, type, geography, reporting summary)
- Intent / Capability / Opportunity scores with cell traces and evidence grades
- Updated matrix cells (only those that rose)
- Kinematics handoff package if applicable
- Refusals logged with reasoning if any element of the request triggered a constraint

Save to `outputs/<engagement-id>-adversary-<adversary-id>.md`.
