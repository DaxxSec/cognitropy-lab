# Split-Brain Discriminator

## Purpose

When two candidate root causes both have partial support, design the single decisive test that falsifies one — instead of replacing both ("parts cannon").

## Prompt Template

```
You are an emissions root-cause adjudicator facing a split-brain. Design a discriminating test; do not commit either hypothesis yet.

I have two competing causes:

- **Hypothesis A:** [e.g. "catalytic converter is dead"] — supported by [EVIDENCE]
- **Hypothesis B:** [e.g. "exhaust leak ahead of the rear O₂"] — supported by [EVIDENCE]
- **Vehicle:** [YEAR/MAKE/MODEL/ENGINE]
- **Tools available:** [LIST]

Please:
1. State the prediction each hypothesis makes that the other does NOT.
2. Propose the single cheapest, most reversible test whose result differs between A and B.
3. Give the predicted result under A vs under B.
4. State which hypothesis the actual result would falsify, and what to do if the test is ambiguous.
```

## Expected Output

- The distinguishing prediction for each hypothesis
- One decisive discriminating test with its A-vs-B predicted results
- The falsification rule (which result kills which branch) and a fallback test if ambiguous
