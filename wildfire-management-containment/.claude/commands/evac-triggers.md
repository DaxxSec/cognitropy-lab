# /evac-triggers — Staged Ready/Set/Go Evacuation Triggers

Convert projected fire arrival time into staged, geographic evacuation trigger points (Ready / Set / Go) for each protective-action zone, so the AHJ gets a recommendation before the window closes.

## Inputs

- Protective-action zones and their populations (note vulnerable populations: schools, care facilities, livestock)
- Projected fire arrival time at each zone (from `/spread-projection`)
- Egress routes and their capacity / time-of-day constraints
- Required clearance time per zone (evacuation duration estimate)

## Steps

1. For each zone, take the projected arrival time and the zone's required clearance time (population ÷ road capacity, adjusted for night/visibility).
2. Define **geographic + temporal triggers**: a named ridge/road the fire reaching = the trigger, sized so the stage fires before arrival by the clearance margin.
3. Walk Decision Tree 4: **READY** (notify, prepare) → **SET** (voluntary; vulnerable populations + livestock leave; stage resources) → **GO** (recommend mandatory order to AHJ now).
4. Check egress integrity: if the only route is threatened or arrival precedes clearance time → escalate the trigger earlier, and if egress is already compromised, recommend **shelter-in-place / refuge area** rather than putting evacuees on a burning road.
5. Identify who issues the order (sheriff/AHJ) and the notification mechanism (WEA, reverse-911, door-to-door, sirens).
6. Note re-evaluation triggers (wind shift, faster ROS, new spot fires across an egress route).

## Output

An evacuation-trigger plan to `outputs/evac-triggers-<date>.md`: per-zone READY/SET/GO triggers (geographic feature + clock time), clearance-time basis, egress integrity assessment, shelter-in-place fallback, and the issuing authority. Framed as a recommendation to the AHJ.

## Notes

- The evacuation **order** is a law-enforcement/AHJ legal function — this command recommends triggers, it does not order.
- Lead time must exceed evacuation duration. Late is the failure mode that kills; when in doubt, trigger earlier.
- Build in the worst credible wind-shift case; an envelope that "probably" misses the town is not a basis for delaying SET.
