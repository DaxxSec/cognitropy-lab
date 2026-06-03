# Cost & Yield Memo

## Purpose

Communicate the cost and yield impact of a build or a defect to the F&B cost controller — numbers-first, so a quality decision can be made on economics as well as craft.

## Prompt Template

```
You are a viennoiserie lamination agent writing a cost & yield memo for the F&B cost controller.

Source:
- **Product & batch:** [PRODUCT, batch size]
- **Build / defect:** [outputs/codex-...md and/or outputs/rootcause-...md]
- **Inputs cost:** [butter cost/kg, flour cost/kg, butter % of formula]
- **Outcome:** [units good / downgraded / rejected]

Please produce a memo that:
1. Leads with the headline number (cost per good unit, or waste cost of the defect).
2. Breaks down butter cost share (usually the dominant input in lamination).
3. States yield: good units vs theoretical, and the waste % with its cause.
4. Recommends one action with its financial effect (e.g. "AOP butter +X/kg but cuts reject rate from Y% to Z%").
5. Keeps it to numbers the controller needs — no craft jargon.
```

## Expected Output

- A headline cost/yield number first, then a short breakdown table.
- Waste % tied to its root cause (cites the rootcause artifact).
- One costed recommendation with the net financial effect.
