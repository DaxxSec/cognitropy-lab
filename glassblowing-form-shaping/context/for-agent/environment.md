# Studio Environment

This file is populated during `/onboard`. Until then it holds the canonical schema and a worked example so the agent has a reference shape to write into.

## Schema

```
## Studio Identity
- Name: <studio name or "home studio">
- Location: <city / country, indoor / outdoor>
- Footprint: <hot shop area, lampworking bench, cold-shop area>

## Ambient Envelope
- Indoor temperature range (°C): <low / typical / high>
- Indoor humidity range (RH%): <low / typical / high>
- Notable seasonal swings: <free text>

## Hot Shop Equipment
- Furnace: <model, capacity (kg), max T, glass family loaded, fuel>
- Glory hole: <model, max T, typical soak T, fuel, door size>
- Lehr (annealing oven): <model, max T, # programmable segments, programmable ramp/hold/dwell>
- Bench: <jacks, blocks (with material/state), paddles, optic molds, marver dimensions>
- Pyrometer / thermocouple: <yes/no, location, accuracy>

## Lampworking Equipment (if any)
- Torch: <model, fuel mix, surface-mix vs. pre-mix, BTU>
- Garaging kiln: <model, max T>
- Mandrels & bead release: <inventory>

## Cold Shop Equipment (if relevant to post-form work)
- Saws, grinders, polishing wheels: <list>
- Sand blaster: <model, abrasive>
- Diamond pads: <grit progression>

## Documentation Posture
- Single artist or multi-user: <single / multi, with names if multi>
- Existing logs: <none / paper notebook / spreadsheet / other>
- Photo workflow: <none / phone / DSLR / cataloged>
```

## Worked Example (for the agent's reference; replace at /onboard)

```
## Studio Identity
- Name: Northbank Glass
- Location: Seattle, WA, USA — indoor warehouse
- Footprint: 600 sq ft hot shop, separate 80 sq ft cold shop

## Ambient Envelope
- Indoor temperature range (°C): 14 (winter morning) / 22 (typical) / 32 (summer afternoon)
- Indoor humidity range (RH%): 35 (winter) / 55 (typical) / 75 (summer afternoon)
- Notable seasonal swings: summer afternoons add ~10 °C to working time pressure

## Hot Shop Equipment
- Furnace: Wet Dog Glass 400 lb pot, 1190 °C max, loaded with Spectrum System 96
- Glory hole: Steve Stelzer "Big Mike" propane, 1300 °C max, typical soak 1170 °C, 14" door
- Lehr (annealing oven): Olympic 18" cube, controller is Bartlett V6-CF, 8 programmable segments, ramp/hold/dwell each
- Bench: Carlo Dona jacks (24" and 36"), maple blocks (cherry and pear), graphite paddle, three optic molds (12-rib, 18-rib, 24-rib spiral)
- Pyrometer: optical pyrometer pointed at glory hole interior, ±15 °C accuracy

## Lampworking Equipment
- Not present

## Cold Shop Equipment
- Wet belt sander, diamond grit 60–600
- Felt polishing wheel + cerium oxide
- Hand-held diamond pads, 200/400/800/1500 grit

## Documentation Posture
- Multi-user: gaffer + assistant model; gaffer is workspace owner, assistants log under their own name
- Existing logs: paper notebook (sparse); migration to this workspace in progress
- Photo workflow: phone, every finished piece gets a photo into outputs/photos/<piece-id>/
```

## How the Agent Uses This

- **Working time budget** in `/form-sim` reads ambient temp from this file's envelope (or from a today-specific override the user supplies)
- **Cool curve** in `/cool-curve` reads lehr capability (max T, programmable segments) — refuses to recommend a program the lehr can't run
- **Lampworking-only commands** are gated on the lampworking section being populated; if it's empty, the command informs the user gracefully
