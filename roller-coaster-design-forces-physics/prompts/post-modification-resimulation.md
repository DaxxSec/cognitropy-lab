# Post-Modification Re-Simulation Review

## Purpose

Use after a track section has been retracked, a train has been swapped, or wheel assemblies changed. Combines `/force-envelope-check`, `/jerk-budget-audit`, and (if relevant) `/restraint-class-decide` into a single re-validation pass.

## Prompt Template

```
A modification has been made to a ride. Walk the new sim/sensor data through the
appropriate decision trees and produce a delta verdict against the pre-modification
baseline.

Modification context:
- **Ride name:** [name]
- **Modification type:** [retrack | train swap | wheel-assembly change | restraint upgrade]
- **Modified elements:** [list of segment ids affected]
- **Pre-mod sim/sensor trace:** [path to CSV]
- **Post-mod sim/sensor trace:** [path to CSV]
- **Frame:** [track | heartline] — must match between pre and post
- **Standard:** [F2291 | EN13814 | in-house]
- **Context:** [why this mod, what failure mode it was meant to address]

Please:
1. Confirm both traces are in the same frame and sample-rate-equivalent.
2. Run /force-envelope-check on the post-mod trace per modified segment.
3. Diff against the pre-mod verdict: which axes / nodes improved, which degraded, which are unchanged.
4. Run /jerk-budget-audit on every transition window that crosses a modified segment boundary.
5. If the modification touched train geometry (seat height, restraint class), re-run /restraint-class-decide.
6. Produce a single delta verdict: "modification CLEARED" / "modification CONDITIONAL" / "modification REJECTED" with the nodes that drove the decision.
```

## Expected Output

- Side-by-side verdict table (pre vs post, per segment, per axis).
- Jerk-audit delta on transition windows.
- Restraint-class delta if applicable.
- Single delta verdict with the node trail.
- Recommendation: green-light, conditional (re-test after Nth modification), or block (revert / further work).
