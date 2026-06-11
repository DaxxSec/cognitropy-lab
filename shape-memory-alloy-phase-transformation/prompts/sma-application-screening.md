# SMA Application Screening

## Purpose

Decide whether a shape memory alloy is the right material for a proposed application — on functional grounds *and* environmental grounds together — before committing to a design.

## Prompt Template

```
You are a materials selection engineer screening shape memory alloys against an application,
weighing functional fit and environmental cost in the same pass.

The application is:

- **Function needed:** [actuation / superelastic / damping / constrained-recovery coupling]
- **Operating temperature range:** [e.g. -10 °C to 60 °C]
- **Stroke / strain and force required:** [values]
- **Cycle-life requirement:** [e.g. 10^5 actuations / 4×10^8 fatigue cycles]
- **Constraints:** [biomedical / cost ceiling / weight / space / regulatory]
- **Conventional alternative today:** [solenoid / motor / bimetal / spring / none]

Please:
1. Judge functional fit: is the operating band compatible with an achievable Af window, stroke, and fatigue life? Name the candidate alloy family.
2. Identify the binding constraint (often the Ni-tuning tolerance, the fatigue requirement, or the temperature window).
3. Sketch the environmental case: embodied-energy premium vs. the conventional alternative, use-phase energy, end-of-life recyclability, and Ni-release risk if there's human contact.
4. Give a go / no-go with reasoning, and if no-go, name the better material.
```

## Expected Output

- A functional fit verdict with the candidate alloy family and the binding constraint named.
- A first-order environmental comparison against the conventional alternative (embodied + use-phase + EOL).
- A clear go / no-go recommendation with the decisive factor stated, and an alternative if SMA loses.
- A list of the next commands to run (e.g. `/composition-temperature-tune`, `/use-phase-energy-balance`) to firm up the screen.
