# /triage — Error Triage & Root Cause Analysis

Quickly classify an error, identify the root cause, and determine severity.

## Instructions

Ask the user to paste:
1. The **full error message and stack trace**
2. **What they were doing** when it happened
3. **When it started** (after an update? out of nowhere?)

## Analysis Steps

### 1. Classify the Error Layer

Determine which layer the bug lives in:
- **Build-time**: Metro bundler, EAS Build, Babel, TypeScript
- **Runtime JS**: Red screen, uncaught exception, component error
- **Runtime Native**: App crash without JS error, Xcode log needed
- **Network/API**: HTTP errors, timeouts, CORS, Railway issues
- **State/Logic**: No crash, but wrong behavior
- **Environment**: Platform-specific or machine-specific

### 2. Read the Stack Trace

- Identify the **first line of the user's own code** in the stack trace
- Note the file path and line number
- If all lines are in `node_modules`, this is likely a dependency issue

### 3. Determine Root Cause

Cross-reference with `resources/common-errors.md` for known patterns.

Form 2-3 hypotheses ranked by probability. For each:
- State the hypothesis clearly
- Explain why you think this could be the cause
- Describe a quick test (< 2 min) to confirm or rule it out

### 4. Rate Severity

| Severity | Criteria |
|----------|----------|
| **CRITICAL** | App won't launch, data loss risk, security issue |
| **HIGH** | Core feature broken, no workaround, blocks users |
| **MEDIUM** | Feature impacted but workaround exists |
| **LOW** | Visual/cosmetic, minor inconvenience |

### 5. Output Format

```
## Triage Report

**Error**: [one-line summary]
**Layer**: [Build / Runtime JS / Runtime Native / Network / State / Environment]
**Severity**: [CRITICAL / HIGH / MEDIUM / LOW]

### Root Cause
[Plain-language explanation of why this is happening]

### Most Likely Hypothesis
[Description and quick test to confirm]

### Alternative Hypotheses
[Other possibilities if the first doesn't pan out]

### Recommended Next Step
[Either a quick fix if obvious, or suggest running /debug for a full session]
```

Log the triage to `work-log/`.
