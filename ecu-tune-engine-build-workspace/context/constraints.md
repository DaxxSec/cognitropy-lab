# Constraints, Safety Limits & Preferences

> Populated by /onboard and updated as the build evolves. The agent MUST enforce these constraints — never recommend exceeding hard limits.

---

## Safety Limits (HARD — Never Exceed)

| Parameter | Safe Max | Current Target | Notes |
|-----------|----------|----------------|-------|
| Boost (peak) | [XX psi] | [XX psi] | |
| Boost (sustained) | [XX psi] | [XX psi] | |
| AFR (WOT, NA) | [X.X:1 lean limit] | [X.X:1] | |
| AFR (WOT, boosted) | [X.X:1 lean limit] | [X.X:1] | |
| Knock retard (acceptable) | [X degrees] | [X degrees] | |
| Coolant temp (WOT) | [XX°C / XX°F] | | |
| Oil temp (WOT) | [XX°C / XX°F] | | |
| IAT (WOT) | [XX°C / XX°F] | | |
| Redline | [XXXX RPM] | | |
| Max throttle below [X°C] oil temp | [XX%] | | Warm-up limit |

---

## Fuel Constraints
- **Maximum safe fuel on this pump/injectors:** [describe limit]
- **E85 capable:** [Yes / No / Partial flex]
- **Fuel quality at primary location:** [brand, octane, ethanol %, station]
- **Race gas availability:** [Yes / No / Occasionally]

---

## Physical / Hardware Limits
- **Transmission torque limit:** [lb-ft / Nm — if known]
- **Axle torque limit:** [lb-ft / Nm — if applicable]
- **Clutch slip threshold:** [describe when it starts slipping]
- **Tire traction limit:** [tires / expected wheelspin point]

---

## Budget Constraints
- **Remaining mod budget:** [approximate]
- **Max spend per dyno session:** [approximate]
- **OEM preference for reliability parts:** [Yes / No — (e.g., prefer OEM head gaskets)]

---

## Preferences
- **Street-legal requirement:** [Yes / No / Not concerned]
- **Emissions compliance required:** [Yes / No / State-specific]
- **Noise restrictions (neighbors/track):** [specify if applicable]
- **Preferred parts brands:** [list any strong preferences or brands to avoid]
- **Parts sourcing preference:** [Local / Online / Mix — preferred vendors]

---

## Off-Limit Modifications (User Has Decided Against)
- [e.g., No port injection — keeping setup simple]
- [e.g., No water-meth injection]
- [e.g., No engine swap — staying with OEM platform]

---

## Legal / Regulatory Notes
- **Registration jurisdiction:** [State / Province / Country]
- **Any current smog/inspection requirements:** [describe]
- **Track rules if applicable:** [rollcage, fire suppression, helmet — list]

---

## Agent Behavior Rules (Enforce Always)
1. Flag ANY recommendation that approaches a hard limit above before confirming it
2. If AFR or knock data is absent from a datalog review, explicitly note the gap
3. Do not recommend increasing boost without confirming injector headroom first
4. Always recommend conservative timing advance changes (≤1° at a time in critical areas)
5. For diagnosis tasks, always list "lean condition" as a differential before recommending power increases
