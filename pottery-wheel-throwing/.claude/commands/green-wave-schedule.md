# /green-wave-schedule

Coordinate the offsets between stages so a batch of pieces flows wheel → leather-hard → trim → bone-dry → bisque → glaze → glaze-fire without queueing — the studio's "green wave."

## Inputs

- The batch (count + form) to schedule.
- Stage durations including the passive drying waits (leather-hard, bone-dry) from `context/references.md` or measured logs.
- Kiln firing slots available (dates/times) from `/kiln-phase-split`.
- The required finish/ship date.

## Steps

1. Lay the stages on a timeline back-to-front from the firing slots: a glaze firing on day D requires glazed ware on day D, which requires bisque-fired ware before that, etc.
2. Set each **offset** = the lead time so the batch arrives at each stage exactly when that stage is free — pieces should not sit bone-dry waiting weeks for a kiln slot (damage risk) nor arrive before the prior stage finished.
3. Resolve collisions: if two batches want the same kiln slot, stagger throwing start dates (adjust the upstream offset) rather than firing partial loads.
4. Verify drying waits are respected, not compressed — forcing leather-hard early causes S-cracks and warping (a quality failure that wastes all upstream work *and* its embodied footprint).
5. Emit a dated production calendar; mark the firing days as the fixed "green phases" everything else coordinates around.

## Output

`outputs/green-wave-YYYY-MM-DD.md`: a per-batch timeline (throw date → each stage offset → firing slot → finish), collisions resolved, and the total pipeline lead time.

## Notes

- The kiln slots are the fixed points; coordinate *to* them, like timing side streets to a coordinated arterial.
- Greenware queued bone-dry for too long is both a damage risk and wasted embodied energy if it cracks — minimizing that wait is a footprint move, not just a throughput one.
