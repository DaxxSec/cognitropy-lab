# Roast Profile Development

## Purpose

Use at the start of a new lot to go from green-lot data and a target roast level to a candidate roast curve and a sample-roast plan — before committing production. Pairs with `/design-roast-profile` and Workflow A.

## Prompt Template

```
You are a roast-development agent in the coffee-roasting-temperature-profiling workspace.
Read context/concepts.md and context/workflows.md (Workflow A) first.

I want to develop a roast profile for a green lot:

- **Green lot ID / origin:** [VALUE — country, region, farm/station, importer]
- **Processing & screen:** [e.g. washed, SC 15/16]
- **Moisture % / water activity:** [VALUE — note source]
- **Crop year:** [current / past]
- **Roaster + capacity + last calibration:** [VALUE]
- **Charge weight:** [VALUE]
- **Target roast level & intent:** [e.g. light-medium, filter, clarity-forward]
- **Constraints:** [e.g. total time ≤ 11:00]

Please:
1. Confirm the green is in spec (aw, moisture) and note any handling flags.
2. Propose charge temp, expected turning point, drying/Maillard/development phase targets, RoR shape, FC timing, and a DTR target.
3. Give a gas/airflow plan that anticipates the post-FC crash.
4. State the expected weight-loss band so /calc-roast-loss can check it.
5. Lay out a 2–4 sample-roast iteration plan and what to adjust between roasts.
```

## Expected Output

- An in-spec/flag verdict on the green.
- A candidate target curve (markers + times + RoR shape + DTR) tied to the lot ID and a profile version.
- A gas/airflow plan with the pre-FC heat-reduction logic.
- The expected weight-loss band and a sample-roast iteration plan toward a cup-approved golden profile.
