# /crash-report — Crash Log Analysis

Analyze a crash log, stack trace, or error report end-to-end. Handles both JavaScript and native crashes.

## Instructions

Ask the user to paste one of:
- A React Native red screen error (screenshot or text)
- A Metro bundler error
- An Xcode crash log
- An EAS Build failure log
- A console error from the browser debugger

## Analysis Protocol

### 1. Identify Crash Type

| Type | How to Recognize |
|------|-----------------|
| **JS Exception** | `TypeError`, `ReferenceError`, `SyntaxError`, etc. |
| **Native Crash** | SIGABRT, EXC_BAD_ACCESS, Xcode crash log format |
| **OOM (Out of Memory)** | `Jetsam` in crash log, or app just disappears |
| **Bundle Error** | Metro fails to bundle, SyntaxError before app loads |
| **Build Failure** | Error during `eas build`, pod install, or Xcode build phase |

### 2. Parse the Stack Trace

For JS exceptions:
1. Find the error message (first line)
2. Walk the stack trace top-to-bottom
3. Highlight the **first frame that's in the user's code** (not node_modules)
4. Note the file, function, line, and column
5. If all frames are in node_modules, identify which package is crashing

For native crashes:
1. Find the crash reason (e.g., `SIGABRT`, `EXC_BAD_ACCESS`)
2. Look for the thread that crashed (marked with `Crashed:`)
3. Look for any React Native or app-specific frames
4. Check if it corresponds to a known native module issue

### 3. Root Cause Analysis

Present findings as:
```
## Crash Analysis

**Crash Type**: [JS Exception / Native / OOM / Bundle / Build]
**Error**: [exact error message]
**Location**: [file:line in user's code, or package name if in node_modules]

### What Happened
[Plain language explanation of the crash chain]

### Root Cause
[The actual underlying issue]

### Fix
[Complete code fix or configuration change]

### How to Verify
[Steps to confirm the crash is resolved]
```

### 4. Recurring Crash Pattern

If this crash has happened before (check `work-log/`):
- Reference the previous occurrence
- Check if the previous fix was incomplete
- Suggest a more robust prevention strategy

Log to `work-log/`.
