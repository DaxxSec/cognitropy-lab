# Prompt — Studio Environment Envelope Capture

Use at the start of every working session, especially when something feels different (hotter than usual, humid, draughty). The captured envelope feeds into `/form-sim`'s working-time budget and into `/post-mortem` if today's pieces fail later for environmental reasons.

## Inputs to Provide
- Current studio ambient temperature (°C)
- Current studio relative humidity (%)
- Glory hole soak temperature (measured if pyrometer present, estimated otherwise)
- Lehr starting temperature
- Time of day, weather note (rainstorm, heat wave, cold snap)
- Any non-routine condition (door open for delivery, ventilation upgraded, new fan running)

## Suggested Conversation Opening

> Capturing studio envelope before today's session. Ambient is <T> °C / <RH>%. Glory hole at <T> °C. Lehr program <ID> loaded, currently at <T> °C. <Any weather note>. <Any non-routine notes>.
>
> Please put this in today's batch record header and call out anything in this envelope that should affect the working-time budget for my planned forms.

## What the Agent Will Do

1. Open or update the day's batch record header with the envelope values
2. Compare the envelope to the studio's typical envelope from `context/for-agent/environment.md`:
   - **Within typical range:** no special action; sim defaults apply
   - **Above typical (hotter day):** working time budget tightens — the gather radiates faster into a hot ambient. Recommend marvering for slightly less time, or reheats sooner.
   - **Below typical (cold day):** working time budget loosens slightly — gather holds heat longer. But cold tools become a bigger risk; recommend pre-heating jacks/punties.
   - **High humidity:** flag any wet-block or water-cooled tool work — water flashing into steam at hot glass surface accelerates surface ΔT
3. If the glory hole is reading lower than the studio's typical soak, flag it — gather temperature out of the hole sets the entire working-time budget. A 50 °C low soak shaves significant time off every gather.
4. If the lehr starting temperature differs from the planned program's loading temperature by > 30 °C, recommend either pre-warming the lehr or adjusting the load procedure (slower door cycle)

## Why This Prompt Exists

Most "weird session" failures correlate with envelope changes the artist didn't notice in the moment. A summer afternoon with the door open shaves working time across every gather. A cold morning where the lehr hadn't fully pre-warmed loads pieces into a steeper thermal gradient. Capturing the envelope explicitly turns these from invisible variables into recorded ones, available for `/post-mortem` later.

## Output

Updated batch record header, plus any envelope-driven warnings for today's planned forms (e.g., "Form-1 sim assumed 60 s working time per heat at typical ambient; today's hot ambient suggests budgeting 50 s — please reheat one operation earlier than the spec calls for").
