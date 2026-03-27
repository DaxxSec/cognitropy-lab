# /tune-diff — Tune Version Comparison

Compare two tune states to understand what changed, why it matters, and whether the changes move the calibration toward or away from safety limits.

---

## When to Use This Command
- Your tuner sent a revised map and you want to understand what changed
- You made changes to your own calibration and want to document the delta
- You're investigating whether a problem appeared after a tune revision
- Building a history of tune evolution for your build records

---

## How to Provide Tune Data

**Option A — Describe the differences verbally:**
"The previous tune had 18° timing at 5500 RPM / 100 kPa. The new tune shows 20° at the same cell."

**Option B — Paste table data for both versions:**
Paste the old table, then the new table. Label them clearly.

**Option C — File-based (with filesystem MCP):**
Provide paths to both tune files or ROM images. The agent will read and compare them.

**Option D — Describe context only:**
"My tuner increased boost target from 17psi to 19psi and bumped fueling in the top-end. What should I watch for?"

---

## What Gets Analyzed

For each reported change:

1. **What the parameter controls** — plain language explanation of the table/map function
2. **Direction of change** — more aggressive (toward limits) or more conservative
3. **Magnitude** — small tweak vs. significant change
4. **Effect on safety** — does this move closer to any hard limits in constraints.md?
5. **Effect on performance** — expected impact on power, drivability, fuel economy
6. **Interaction effects** — does this change interact with other parameters? (e.g., timing advance + boost increase = compounded knock risk)

---

## Output Format

**Revision Summary:**
| Parameter | Old Value | New Value | Change | Assessment |
|-----------|-----------|-----------|--------|------------|
| Ignition @ 5500/100kPa | 18° | 20° | +2° | Monitor for knock |
| Boost target peak | 17 psi | 19 psi | +2 psi | Verify injector headroom |
| WOT fueling target | 11.5 AFR | 11.2 AFR | Richer | Safer margin |

**Overall Assessment:**
[Safe / Marginal / Flags for concern — with reasoning]

**Changes That Approach Hard Limits:**
[Explicitly flag any change that brings a parameter within 10% of a constraints.md hard limit]

**Recommended Monitoring:**
[What to watch on the first pull after these changes]

**Tune History Entry:**
[Ready-to-paste summary for saving in work-log/]

---

## Saving the Diff

After analysis, offer to save the comparison to:
`outputs/tune-diff-YYYY-MM-DD-[descriptor].md`

This creates a permanent record of the calibration evolution for the build.
