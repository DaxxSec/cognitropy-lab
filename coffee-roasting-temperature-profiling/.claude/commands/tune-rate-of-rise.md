# /tune-rate-of-rise

Re-schedule gas, airflow, and drum settings to produce a smooth, continuously declining rate-of-rise without crash or flick — the core of a reproducible profile.

## Inputs

- The current profile/log with its RoR problem (from `/diagnose-roast-curve`).
- The roaster's controllable levers and their granularity (gas steps, fan/damper positions, drum speed if variable).
- Target RoR shape and DTR (from the golden profile or `/design-roast-profile`).

## Steps

1. Read `context/concepts.md` ("Heat-transfer levers", "RoR, crash & flick").
2. Identify *when* the RoR misbehaves: early spike (tipping risk), mid-roast bump, or the post-FC crash/flick zone.
3. For a **crash**: move the pre-FC heat reduction earlier and make it gentler so momentum carries through FC; verify airflow isn't over-scrubbing convective heat.
4. For a **flick**: remove or soften the late heat increase that caused the rebound; smooth the gas step instead of a sharp change.
5. For an **early RoR spike**: lower charge temp or initial gas, or reduce batch size relative to capacity.
6. Propose a revised gas/airflow timeline (set-point + time), predict the new RoR curve, and note what to watch on the next roast.

## Output

`outputs/profiles/<sku-or-lot>-vX.Y-ror-tune-YYYY-MM-DD.md` — the revised lever timeline, predicted RoR curve, the rationale per change, and the success criterion (smooth decline, no crash/flick, DTR in band) to verify with `/match-profile-batch`.

## Notes

- Change one variable at a time across roasts — simultaneous gas + airflow changes make the cause unrecoverable.
- Adding heat *into* a crash causes a flick; anticipate the crash by cutting heat *before* FC, not reacting after.
- Airflow does double duty (heat + chaff/exhaust); raising it to fix heat can scrub aromatics — note the trade-off.
