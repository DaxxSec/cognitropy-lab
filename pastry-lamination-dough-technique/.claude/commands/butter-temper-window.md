# /butter-temper-window

Match butter plasticity to dough consistency and compute the working temper window — the "material analysis" of the laminate's two substrates, like assessing parchment and ink before reading a manuscript.

## Inputs

- Butter fat % (from spec sheet or `/provenance-trace`).
- Détrempe target temperature and hydration.
- Kitchen ambient temperature and humidity.

## Steps

1. Look up the butter's plasticity range from fat % (higher fat → wider, more forgiving window; see `context/references.md`).
2. Compute the **overlap window** where butter and dough are at matched consistency (typically butter 13–16 °C, dough 12–15 °C).
3. Adjust for **ambient**: a warm kitchen narrows the safe window and shortens working time before re-chill.
4. State the **lock-in target temps**, the **maximum working time** before butter softens past the window, and the **re-chill trigger**.
5. Flag any mismatch that makes clean lamination unlikely with the current lot (e.g. low-fat butter in a warm room) and recommend a substitution or schedule change.

## Output

A temper window note at `outputs/temper-<butter-lot>-<date>.md`: the overlap window, lock-in targets, working-time limit, re-chill trigger, and any mismatch warning.

## Notes

- European/AOP *beurre de tourage* (~84% fat) gives the widest, most error-tolerant window; standard 80% butter cracks colder and bleeds warmer.
- The window is the single best predictor of welding/bleed faults — compute it before lock-in, not after a failure.
