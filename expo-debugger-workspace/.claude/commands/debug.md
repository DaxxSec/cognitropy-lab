# /debug — Full Interactive Debugging Session

A structured, step-by-step debugging session for a specific bug. More thorough than `/triage` — this walks through diagnosis to resolution.

## Instructions

If the bug hasn't been triaged yet, run the triage protocol from `context/for-agent/workflows.md` first.

### Phase 1: Reproduce

1. Ask the user to describe exact reproduction steps
2. Clarify: Does it happen every time or intermittently?
3. Clarify: Does it happen in Expo Go, dev build, production, or all?
4. Ask to see the relevant code files (component, screen, API call, etc.)

### Phase 2: Isolate

Guide the user through narrowing down the cause:

1. **Binary search the code**: Comment out half the component. Does the error persist?
2. **Check recent changes**: `git diff` or `git log --oneline -10` — what changed recently?
3. **Test dependencies**: Does the error happen with a fresh `node_modules`? (`rm -rf node_modules && npm install`)
4. **Test environment**: Does it happen on a different simulator/device?

### Phase 3: Diagnose

Based on isolation results:

1. Identify the exact line(s) causing the issue
2. Explain WHY the code is failing (not just what's wrong)
3. Reference similar patterns from `resources/common-errors.md` if applicable
4. Check if this is a known issue with the specific package version

### Phase 4: Fix

1. Present the fix as a complete code block showing the full file context (not just the changed line)
2. Explain what the fix does and why it works
3. Flag any potential side effects
4. Provide a verification step: "After applying this fix, you should see [X]"

### Phase 5: Prevent

1. Explain the pattern that caused this bug
2. Suggest a practice or check that would catch this earlier
3. If relevant, suggest adding an error boundary, type check, or validation

## Session Logging

Log the full session to `work-log/` including:
- Date
- Bug description
- Root cause
- Fix applied
- Prevention recommendation
