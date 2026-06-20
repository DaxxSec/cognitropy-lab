# Studio Throughput Diagnosis

## Purpose

Use when a studio "feels backed up" and you need to locate the real bottleneck with the traffic signal-timing lens before spending money or changing the schedule.

## Prompt Template

```
You are a ceramics-studio operations analyst applying traffic-engineering signal-timing methodology. Treat each stage as a signalized server and find the controlling bottleneck.

My studio:
- **Wheels:** [NUMBER] | typical throw time per piece: [MINUTES]
- **Drying capacity:** [PIECES] holding, [HOURS] to leather-hard, [HOURS] to bone-dry
- **Trimming:** [STATIONS] benches | [MINUTES] per piece
- **Kiln(s):** [MODEL, CU FT] | pieces per firing: [BISQUE COUNT] bisque, [GLAZE COUNT] glaze | cycle hours: [HOURS]
- **Demand:** [PIECES] per [week/month]
- **Symptom:** [WHERE GREENWARE PILES UP]

Please:
1. Estimate the saturation flow rate and degree of saturation (X) for each stage.
2. Identify the bottleneck and state by how much its X exceeds the others.
3. Confirm whether the math agrees with the observed pile-up.
4. Recommend the next command to run (load density, phase split, or a capacity decision).
```

## Expected Output

- A per-stage saturation-flow / capacity / X table.
- The named bottleneck with a quantified margin.
- A reconciliation against the observed symptom.
- A routing recommendation to the right command.
