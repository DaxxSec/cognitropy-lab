# /health-check — Pre-Build Health Check

Run through a systematic check of the app across all common issue categories. Use before pushing a build to TestFlight or whenever things feel shaky.

## Instructions

Work through each category. For each, either ask the user to run a command or ask about the current state. Report findings as PASS / WARN / FAIL.

### 1. Expo Doctor

Ask the user to run:
```bash
npx expo-doctor
```
Review output for warnings or errors.

### 2. Dependency Compatibility

Ask the user to run:
```bash
npx expo install --check
```
Flag any mismatched versions. Suggest fixes with `npx expo install --fix`.

### 3. TypeScript / Linting

Ask the user to run:
```bash
npx tsc --noEmit
```
Review type errors. Categorize by severity.

### 4. Metro Bundler

Ask the user to start the app with a clean cache:
```bash
npx expo start --clear
```
Note any warnings in the Metro output.

### 5. API Connectivity

Ask the user to verify:
- Can the app reach the Railway backend?
- Does the health check endpoint respond?
- Are all environment variables set for the current environment?

### 6. Navigation

Check for:
- Any screens that error on load
- Deep link configuration (if applicable)
- Tab/stack navigator nesting issues

### 7. Error Handling

Review:
- Are there Error Boundaries around critical screens?
- Are API calls wrapped in try/catch?
- Are loading and error states handled in the UI?

### 8. Performance Quick Look

Check for obvious issues:
- Large images not optimized
- Unnecessary re-renders (React DevTools profiler)
- Memory leaks from uncleared subscriptions/timers

## Output Format

```
## Health Check Report — [Date]

| Category | Status | Notes |
|----------|--------|-------|
| Expo Doctor | PASS/WARN/FAIL | [details] |
| Dependencies | PASS/WARN/FAIL | [details] |
| TypeScript | PASS/WARN/FAIL | [details] |
| Metro Bundler | PASS/WARN/FAIL | [details] |
| API Connectivity | PASS/WARN/FAIL | [details] |
| Navigation | PASS/WARN/FAIL | [details] |
| Error Handling | PASS/WARN/FAIL | [details] |
| Performance | PASS/WARN/FAIL | [details] |

### Action Items (prioritized)
1. [FAIL items first]
2. [WARN items second]
3. [Improvement suggestions]
```

Save report to `outputs/health-check-YYYY-MM-DD.md`.
