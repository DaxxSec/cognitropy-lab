# Prompt — Color Incompatibility Pretest

Use when introducing a new color rod lot into the studio's rotation, or when proposing a combination of glasses that the compatibility matrix flags as `PRETEST` (e.g., Effetre 104 + Reichenbach RW104).

## Inputs to Provide
- Proposed color rod(s): supplier, lot ID, color name, nominal COE
- Base glass: family, melt batch ID
- Form context — is this a "color applied to surface" combination (low risk if compatible) or "color cased into body" (higher consequence on incompatibility)?

## Suggested Conversation Opening

> I want to introduce <supplier> <color> rod, lot <lot-id>, into rotation. Nominal COE <n>. I plan to use it with <base glass family> melt <batch ID>. The first piece I'm thinking is <form description>.
>
> The compatibility matrix in resources/glass-viscosity-reference.md says <OK/PRETEST/BLOCK> for this pair. Please walk me through the pretest protocol if it's PRETEST, or document the assumption if it's OK and the lot is new to the studio.

## What the Agent Will Do

### If matrix says BLOCK
- Refuse to proceed. Explain the COE delta and the slow-cracker risk.
- Suggest alternative colors from the same family that achieve a similar visual.

### If matrix says PRETEST
1. Open the test record at `outputs/compatibility-tests/<base-family>-<color-supplier>-<color-lot>.md`
2. Walk through the standard protocol:
   - Make a small (~2 cm) fused strip of the two glasses in direct contact
   - Anneal under the standard program for the base family
   - After cool, inspect under crossed polarizers
   - **No fringes:** mark `compatible-this-lot` and proceed; record the lot pair as OK in the studio's append section of the compatibility matrix
   - **Fringes visible:** mark `incompatible-this-lot`, treat as BLOCK for this lot, contact supplier with photo, log to `resources/failure-mode-taxonomy.md` known-bad pairings
3. Schedule a 90-day successional follow-up on the test piece (compatibility issues sometimes only manifest with thermal cycling)

### If matrix says OK
- Confirm the lot is being entered into inventory with full traceability (supplier + lot ID labeled on the rod bundle)
- Suggest a single small test piece as the lot's "first fire" — even with full compatibility, lot variation can surface other surprises (color shift, devit propensity, working temp variation)

## Why This Prompt Exists

Compatibility failures are the worst category of glass failure: they look fine, the piece survives anneal, and weeks later it cracks at the color interface. The pretest takes 30 minutes and prevents months of mystery cracking. Skipping the pretest because "it should be compatible" is the failure mode this prompt is here to prevent.

## Output

A complete entry in `outputs/compatibility-tests/<base-family>-<color-supplier>-<color-lot>.md` with the test result, photos if any, and the lot's status (`compatible-this-lot` / `incompatible-this-lot` / `pending-90d-followup`).
