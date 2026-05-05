# Getting Started — First Sol Walkthrough

This is the 30-minute walkthrough for a brand-new user. By the end you'll have a sol plan handoff document, even if you've never planned a rover traverse before.

## Prerequisites

- A planning AOI: a HiRISE orthoimage + DEM (or, for analog use, a drone-photogrammetry DEM + orthoimage).
- A rover platform spec (use Curiosity or Perseverance from `resources/flight-rules-quickref.md` if you don't have your own).
- A strategic target: the (lat, lon) you're driving toward.
- Python 3.x with `rasterio`, `numpy`, `scipy`, `networkx` if you want to run the geospatial stack; if not, you can drive the workflow conceptually using JMARS/QGIS for visual review.

## Step 1: Onboard

Run `/onboard`. The agent will interview you about:
- Mission, rover platform, target site
- Dataset paths
- Reviewer panel (in solo mode you play all 5 roles)
- Constraints

This populates `context/` and bootstraps `planning/plan.md`.

## Step 2: Assess Terrain

Run `/terrain-assess` on your planning AOI. The agent will:
1. Compute slope, aspect, roughness from the DEM.
2. Estimate rock abundance from the orthoimage.
3. Classify terrain into the 6 canonical classes.
4. Combine into a composite hazard score.
5. Save the rasters and a visual summary PNG.

Open the PNG and look at it. Does the hazard map reflect what you expect from the orthoimage? If not, the weights or terrain classification need calibration; iterate before continuing.

## Step 3: Compose Candidates

Run `/traverse-compose`. The agent will:
1. Sample candidate waypoints across the AOI.
2. Build a graph of safe segments.
3. Enumerate the top 3–5 candidate progressions toward your strategic target.
4. Write each candidate to `planning/candidates/` as a chord progression.

Review the candidate list. Which one looks best on the map?

## Step 4: Check Cadence

Run `/risk-cadence` on your top pick. The agent will:
1. Walk the chord progression segment by segment.
2. Identify phrases (start-on-stable, end-on-stable subsequences).
3. Flag any unresolved-dissonance stretches or pathologies.
4. Render a tension profile diagram.

If there are HARD FAILs, fix them — usually by going back to `/traverse-compose` with different parameters, or by running `/substitution-search` on the flagged segment.

## Step 5: Substitute (If Needed)

If `/risk-cadence` flagged a HIGH or MEDIUM segment, run `/substitution-search` on it. The agent will:
1. Try a tritone substitution (different terrain, same destination).
2. Try a modal-interchange substitution (borrow from the conservative plan).
3. Try a pivot-recovery substitution (insert a safer intermediate waypoint).
4. Score and rank the substitutes.

Accept the strongest substitute (or none, if the original is still better). Re-run `/risk-cadence` after any substitution.

## Step 6: Peer Review

Run `/peer-review` on the cleared candidate. In solo mode, the agent will walk you through each of the 5 reviewer roles (Driver, Science PI, Mech/Safety, Autonomy, Comms) and force you to argue from each perspective. The output is a decision log saved to `outputs/decision-log/`.

A PASS or STRONG PASS is your green light.

## Step 7: Synthesize the Sol Plan

Run `/sol-plan`. The agent will:
1. Verify the candidate has passed peer review.
2. Build the sol skeleton (housekeeping, science, drive, comms, contingency).
3. Place the drive block, science blocks, comms passes, and contingencies.
4. Honor any dissents from the decision log.
5. Save the final sol plan to `outputs/sol-plans/`.

That document is the handoff to the uplink team (or to the next planner, in analog use).

## Tips for Beginners

- **Use the harmonic vocabulary as a thinking tool, not a goal.** The point isn't to write beautiful chord progressions; the point is to have a vocabulary that makes trade-offs explicit.
- **Solo mode is harder, not easier.** With no live panel, you're at risk of agreeing with yourself. Force yourself to find at least one objection per role.
- **Start with a known-easy traverse.** Pick a strategic target on flat bedrock with no rocky obstacles. Get a clean PASS through the workflow before tackling a hard one.
- **The cadence chord matters more than anything else.** If you can't find a verified safe parking spot at the end, no amount of clever substitutions saves the plan.
- **`/risk-cadence` is fast — run it freely.** It's the cheapest check in the workflow; running it after every substitution is the right amount.
- **Read the decision log later.** A week from now, when you wonder "why did I choose this route?" — the decision log has the answer. That's its purpose.
