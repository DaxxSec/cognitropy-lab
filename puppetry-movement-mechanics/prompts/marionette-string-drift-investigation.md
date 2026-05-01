# Prompt — Marionette String-Drift Tour Investigation

A reusable investigation prompt for tracking a suspected string-drift pattern across a multi-month touring run. Use this prompt to drive a structured `/detect-anomaly --backtest` + `/calibration-audit` review across an entire tour's logs.

## When to Use

- A puppeteer suspects a particular control surface has drifted noticeably over the run
- The tour is mid-run and you want to decide whether to tune now or wait
- You're authoring the company's "starter rule set" for the next tour and want to mine this tour's data

## Prompt Body

> You are investigating string-drift on `<puppet-slug>` over the period `<start-date>` to `<end-date>`. The suspected drift is on `<string-id>`. Your task:
>
> 1. **Collect the corpus.** List every `work-log/<date>.md` between the start and end dates. Identify which logs touch the named puppet.
>
> 2. **Recover the calibration trajectory.** List every `outputs/audits/<date>-<puppet>.md` between those dates. Extract the per-audit measurement of `<string-id>`. Plot or tabulate the trajectory.
>
> 3. **Replay the active rule set.** Run `/detect-anomaly --all-active` against the corpus, filtered to events touching the named puppet. Note any rule that fires more than three times.
>
> 4. **Inspect the firings.** For each frequently-firing rule, walk one or two firings to confirm they are real anomalies and not false-positives.
>
> 5. **Distinguish the drift profile.** Decide which of the following profiles fits:
>    - **Linear** — drift is roughly proportional to days-in-tour. Likely Spectra creep; expect drift to stabilize after the first ~2 weeks then re-accelerate after a tightening.
>    - **Step** — drift jumped at a specific date. Cause is usually a travel event (new venue, transport shock) or a humidity change; cross-reference travel logs.
>    - **Sawtooth** — drift accumulates between adjustments. This is the desired profile for a maintained rig; flag if amplitude is growing.
>    - **Hysteretic** — drift oscillates with humidity / temperature. String material is hygroscopic; consider switching to Spectra if currently polyester.
>
> 6. **Decide the action.**
>    - Linear, low slope → continue monitoring; tune at the next scheduled stop.
>    - Step → investigate the named travel event; consider re-baselining after tour stabilizes.
>    - Sawtooth, growing amplitude → mechanism wear (anchor wearing); maintenance recommended at next break.
>    - Hysteretic → consider material change; flag for next show's pre-build.
>
> 7. **Output.** Write the investigation to `outputs/reports/<date>-<puppet>-string-drift-investigation.md` with the trajectory table, profile classification, and recommended action. Run `/peer-review` against the report — minimum reviewers: rigger + puppeteer.

## Why This Prompt Exists

String-drift investigation is one of the most common ad-hoc tasks on a long tour and is exactly the activity the company's institutional memory loses when a senior puppeteer leaves. A formalized investigation produces a written, reviewable artifact that can train the next person.

## Reference

- Bell, John — *American Puppet Modernism* (2008) for tour-logistics narratives
- Cordwainer, Kelly — *The Marionette Master's Manual* (self-published, 2014) — practical reference for rig adjustment
- Spectra technical data sheets (DSM Dyneema, available from the manufacturer) — for creep curves
