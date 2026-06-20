# /threat-stream-synthesis

Synthesize the protective intelligence feed (DS Watch, OSAC, host-nation MOI liaison, embassy reporting, open-source HUMINT) into a daily TBA-format brief during pre-trip and visit windows.

## Inputs

- **DS Watch / equivalent state-actor feed** for the relevant jurisdictions.
- **OSAC reporting** for in-country regional environment.
- **Host-nation MOI liaison** updates (formal channel via embassy liaison).
- **Embassy reporting** — DCM weekly + crisis-specific cable traffic.
- **Open-source feeds** — Twitter/X, Telegram channels, host-nation media, sectarian/political-faction channels relevant to threat picture.
- **Trip-specific filters** — protectee identity, jurisdictions, venues, dates.

## Steps

1. Read `context/concepts.md` "Threat taxonomy" + `context/workflows.md` "Threat-stream synthesis".
2. Pull current-day reporting from each source; deduplicate against prior days.
3. Classify each new item:
   - **Direct** — specific threat against protectee or trip
   - **Indirect** — generalised threat affecting jurisdiction in trip window (civil unrest, regional conflict, political crisis)
   - **Environmental** — context that could escalate (election cycle, anniversary, sectarian tension flare)
   - **Tactical** — TTP shifts (new IED design, new attack pattern, new VBIED profile)
4. Score each item:
   - **Specificity** — generic / regional / venue-specific / protectee-specific
   - **Credibility** — single-source / multi-source / corroborated
   - **Recency** — current / past 24h / past week / older
5. Aggregate to trip-tier impact assessment:
   - Does this raise trip threat tier? Lower it? Steady?
   - Does this trigger contingency-tree revision?
   - Does this trigger motorcade-config revision?
6. Write the daily TBA brief — Threat Bulletin Assessment — to `outputs/threat-streams/<trip-id>/<YYYY-MM-DD>-TBA.md`.
7. Brief detail leader + RSO within 12 hours of synthesis.

## Output

A markdown TBA brief at `outputs/threat-streams/<trip-id>/<YYYY-MM-DD>-TBA.md` containing: date, sources reviewed, new items by class, tier impact assessment, contingency / motorcade impact, named POCs for follow-up, source list with classification handling notes.

## Decision points

- **If new direct threat surfaces** → escalate immediately to detail leader + RSO; do not wait for next scheduled brief.
- **If a source goes silent during an active feed window** → flag as possible coverage gap; reach out via alternate channel before assuming "no news = good news".
- **If multi-source corroboration is missing for high-impact reporting** → caveat appropriately; don't drive trip-config changes off single-source thinly.

## Notes

- TBA cadence is daily during pre-trip (T-14 to T-0) and twice-daily during visit; surge cadence on threat shifts.
- Source list inside the TBA must respect originator-control rules; document classification handling.
- Open-source feeds are signal-rich but noise-heavy; corroborate before action.
- Don't confuse "no negative reporting" with "all clear" — the absence of reporting may itself be a reporting gap.
