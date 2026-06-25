# /rtos-vs-baremetal

Decide the scheduling architecture — superloop, cooperative scheduler, or preemptive RTOS — by weighing what the workload's real timing needs cost against what each model buys, because an RTOS is a purchase, not a default.

## Inputs

- The task list with each task's period, deadline, and worst-case execution time
- Concurrency/priority needs (any genuinely independent, priority-ordered timing?)
- Available RAM/flash headroom and team familiarity with an RTOS

## Steps

1. Characterize timing: is it **soft** (a superloop tolerates jitter) or **hard** (deadlines that must be met under load)?
2. Count truly **concurrent, priority-ordered** activities — one or two interrupt-driven events rarely need an RTOS.
3. Price each model: superloop (~free), cooperative (small), preemptive RTOS (few KB RAM/flash + context-switch + race surface + learning curve).
4. Match the cheapest model that meets the timing; reserve the RTOS for genuine concurrency with priorities.
5. If RTOS, size the **per-task stacks** and account them in the RAM budget (`/budget-flash-ram`).

## Output

`outputs/projects/<name>/scheduling-decision.md` — the timing characterization, the model chosen, what it costs (RAM/flash/complexity) and what it buys, and the rejected alternatives.

## Notes

- A superloop with well-prioritized interrupts handles a surprising amount; don't buy an RTOS to blink an LED.
- The RTOS's hidden cost is the **race-condition surface** (mutexes, priority inversion) — that complexity is part of the price.
