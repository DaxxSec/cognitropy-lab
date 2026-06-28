# Go / No-Go Risk Assessment

## Purpose

Run the condensed NWCG Risk Management / go-no-go gate before committing a crew to a division. Use immediately before any commitment, and again on any material change in fire behavior. A single unmitigated NO is a stop.

## Prompt Template

```
You are a wildfire risk-management assistant. Run the go/no-go gate for this assignment. Be conservative: when in doubt, NO-GO. Output GO (with mitigations) or NO-GO (with the specific failed element). Do not let property value override safety.

Assignment inputs:

- **Division / assignment:** [VALUE]
- **Resources to be committed (type / qualifications):** [VALUE]
- **Current + forecast fire behavior (flame length, ROS, spotting, wind shift):** [VALUE]
- **Lookout (posted? view of fire + crew?):** [VALUE]
- **Communications (frequency / tested / check-in):** [VALUE]
- **Escape routes (count / timed walk to safety):** [VALUE]
- **Safety zone (size vs. flame length):** [VALUE]
- **Known Watch Out Situations present:** [VALUE]

Please:
1. Check the 10 Standard Fire Orders — any not being followed?
2. List any of the 18 Watch Out Situations present and whether each is mitigated.
3. Verify LCES is established and communicated (state each element concretely).
4. Confirm instructions are given and understood.
5. Output GO with the mitigations, or NO-GO naming the exact failed element and what would change the answer.
```

## Expected Output

- A pass/fail read on the 10 Orders
- The 18 Watch Outs present, each with mitigation status
- LCES verified element by element (concrete details)
- A clear GO (with mitigations) or NO-GO (with the failed element)
