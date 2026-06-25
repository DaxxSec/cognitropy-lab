# Build-vs-Buy Decision Brief

## Purpose

Produce a total-cost-of-ownership comparison for a stack component across commercial, open-source, and in-house options — with license obligations and certification risk priced in, not assumed away.

## Prompt Template

```
You are deciding build vs buy for an embedded stack component on total cost of ownership.

I have a component decision:

- **Component + hard requirements:** [E.G. BLE STACK, MUST BE QUALIFIED]
- **Volume / lifetime:** [UNITS/YEAR, YEARS]
- **Commercial option(s) + license terms + price:** [PER-UNIT / ONE-TIME]
- **Open-source option(s) + license + upstream health:** [GPL/MIT/BSD/APACHE, ACTIVITY]
- **In-house effort estimate:** [ENGINEERING MONTHS + MAINTENANCE]

Please:
1. State the hard bar and which options can actually meet it.
2. Build the TCO for each option (buy price + integration + maintenance + license + certification risk) over the lifetime at volume.
3. Flag license obligations explicitly (especially copyleft in a closed product).
4. Recommend one option with the TCO math and the obligations being accepted.
```

## Expected Output

- The hard-bar feasibility screen
- A TCO comparison across all three paths at the real volume
- An explicit license-obligation analysis
- A recommendation with the math and accepted obligations shown
