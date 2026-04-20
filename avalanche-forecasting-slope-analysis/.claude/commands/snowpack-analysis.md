---
description: Interpret stability tests and stratigraphy data, update the persistent weak layer tracker.
---

# /snowpack-analysis

## Inputs

The user will provide one or more observations with:
- Location (zone, elevation, aspect, slope angle)
- HS (total snow height), HST (new snow), slab properties (density, hardness)
- Test results: CT / ECT / PST / RB with failure depth, failure character, propagation/arrest
- Notes on suspect layer (grain type, hardness, depth from surface)
- Optional: snow profile in CAAML / Snowpilot JSON

## Steps

1. Parse test results. Convert to standard notation (ECTP/ECTN/ECTX, CT sudden planar, PST END/ARR/SF).
2. Identify the weak layer(s) involved. Flag whether it's a known tracked PWL or a new one.
3. Rate stability contribution:
   - ECTP <= 15 + sudden planar -> HIGH propagation concern
   - ECTP 16-30 sudden -> MODERATE concern
   - ECTN / ECTX -> low concern from this test alone; pool with other evidence
   - PST < 50/100 END -> propagation likely
4. Update `work-log/pwl-tracker.md` - one row per weak layer with depth, grain type, aspect/elevation representativeness, today's evidence.
5. Recommend problem-type implications for next forecast:
   - New PWL signal -> upgrade / add persistent slab problem
   - Healing evidence (quiet, ECTX for 7+ consecutive days across reps) -> candidate for downgrade but require human sign-off
6. Record spatial variability caveat: single pit \!= the zone.

## Output

- Updated PWL tracker row(s)
- Bullet summary of stability contribution
- Problem-type delta recommendation (no auto-apply)
