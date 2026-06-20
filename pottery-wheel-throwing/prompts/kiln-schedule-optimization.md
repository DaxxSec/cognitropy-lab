# Kiln Schedule Optimization

## Purpose

Use to turn a product mix and a kiln into an optimized firing schedule — phase split plus green-wave coordination — that keeps every firing full and meets lead times.

## Prompt Template

```
You are scheduling firings for a production pottery studio. Treat the kiln as a signalized batch server: allocate its limited firing slots ("green time") across product lines and bisque/glaze phases, and coordinate upstream offsets so batches arrive as slots open.

Inputs:
- **Kiln:** [MODEL, CU FT] | firings available per [week/month]: [NUMBER]
- **Bisque capacity:** [PIECES] | **glaze capacity:** [PIECES] (no-contact)
- **Product lines:** [LINE A: demand, lead time], [LINE B: ...], [LINE C: ...]
- **Constraint:** [SHIP DATES / STANDING ORDERS]

Please:
1. Compute each line's critical flow ratio and split firing slots proportionally.
2. Keep every firing at high utilization — flag any plan that fires partial loads.
3. Produce a dated firing calendar with the throwing start date (offset) for each batch.
4. Note the per-piece firing-energy implication of the chosen utilization.
```

## Expected Output

- Firing-slot allocation per line and phase, with utilization per firing.
- A dated calendar of throw → bisque → glaze → glaze-fire offsets.
- Any starved line or partial-load firing flagged.
- The energy-per-piece consequence of the schedule.
