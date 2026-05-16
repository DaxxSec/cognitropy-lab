# Injury-Risk Briefing

## Purpose

Use after `/injury-posterior` has been run for a test, to produce a one-page analyst-facing briefing that turns the posterior into a defensible narrative — without ever collapsing the credibility interval into a point estimate.

## Prompt Template

```
You are a senior crash-test biomechanics analyst writing a one-page injury-risk briefing for the lab's chief engineer. The briefing must lead with posterior credibility intervals, not point estimates.

Test:
- **Test ID:** [TEST_ID]
- **Vehicle:** [YEAR_MAKE_MODEL]
- **Test mode:** [FRONTAL_RIGID | ODB | MPDB | SMALL_OVERLAP | SIDE_POLE | OBLIQUE | OTHER]
- **Occupant position:** [DRIVER | FRONT_PASSENGER | REAR_LEFT | REAR_RIGHT | OTHER]
- **Dummy:** [HYBRID_III_50M | THOR_50M | HYBRID_III_5F | OTHER] — serial [SERIAL]
- **Posteriors file:** [PATH_TO_outputs/<test-id>/posteriors/<occupant>/summary.md]

Please:
1. For each body region (head, neck, chest, pelvis, femur), state the posterior P(AIS 3+) as median [5th, 95th] — never as a single number.
2. Identify the body region with the highest P(AIS 3+) and explain in two sentences what the kinematics imply about the injury mechanism (refer to `/restraint-likelihood` output if available).
3. Flag any region whose 5–95 credibility interval crosses the regulatory threshold of P(AIS 3+) ≤ 0.20 — this is a "tight pass" that should not be over-claimed.
4. Recommend one concrete next action: publish, retest, re-elicit dummy prior, or hold for analyst review.
```

## Expected Output

- Five posterior intervals (head / neck / chest / pelvis / femur) reported as median [5th, 95th].
- One named "worst body region" with a two-sentence mechanism narrative.
- A flag list of any tight-pass regions.
- A single concrete next action.
- No body region reported as a point estimate anywhere in the briefing.
