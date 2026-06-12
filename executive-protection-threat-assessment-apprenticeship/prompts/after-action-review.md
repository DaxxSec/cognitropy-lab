# After-Action Review (AAR)

## Purpose

Run a structured AAR after a live operation or a drill, extracting both operational lessons (sustain/improve) and individual competency observations that feed the apprenticeship portfolio.

## Prompt Template

```
You are facilitating an after-action review for an executive-protection operation or drill.

I have the following inputs:

- **Operation / drill:** [WHAT, WHEN, WHERE, WHO WAS ON THE DETAIL]
- **Plan / intent:** [WHAT WAS SUPPOSED TO HAPPEN]
- **What actually happened:** [TIMELINE + ANY INCIDENTS]
- **Apprentices involved + EPAs exercised:** [NAMES, EPA-N]

Please:
1. Compare intent vs reality and explain the deltas (root cause, not blame).
2. List what to SUSTAIN and what to IMPROVE, each with an owner.
3. For each apprentice, record competency observations against the EPA(s) they exercised — at what entrustment level did they actually perform?
4. Recommend follow-up taskings or sign-offs (hand to /competency-signoff or /apprentice-tasking).
```

## Expected Output

- An AAR record: intent-vs-reality deltas with root causes, sustain/improve lists with owners.
- Per-apprentice competency observations tied to specific EPAs and entrustment levels.
- Explicit hand-offs into the progression loop (sign-offs / taskings).
- Repair-over-blame tone; mistakes are data.
