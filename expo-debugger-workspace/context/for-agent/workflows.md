# Debugging Workflows

Detailed step-by-step methodologies for the agent to follow when debugging Expo + Railway apps.

---

## Workflow 1: The Universal Triage Protocol

Use this for ANY error before diving deeper.

### Step 1 — Classify the Error

Determine which layer the error lives in:

| Layer | Signals |
|-------|---------|
| **Build-time** | Error during `expo start`, `eas build`, or `npx expo export` |
| **Runtime — JS** | Red screen, yellow warning, console error in Metro |
| **Runtime — Native** | App crash without JS error, Xcode crash log |
| **Network / API** | HTTP status codes, timeout, CORS, Railway logs |
| **State / Logic** | App doesn't crash but behaves incorrectly |
| **Environment** | Works on one machine / simulator but not another |

### Step 2 — Gather Context

For every bug, collect:

1. **Full error message and stack trace** (not truncated)
2. **What the user was doing** when it happened (reproduction steps)
3. **When it started** (after a package update? code change? deploy?)
4. **Where it happens** (all screens? one screen? only on device?)
5. **Frequency** (every time? intermittent? first-load only?)

### Step 3 — Rate Severity

| Severity | Definition | Response |
|----------|-----------|----------|
| **Critical** | App crashes on launch, data corruption, auth broken | Fix immediately |
| **High** | Core feature broken, blocks user flow | Fix today |
| **Medium** | Feature partially broken, workaround exists | Fix this sprint |
| **Low** | Visual glitch, minor inconvenience | Backlog |

### Step 4 — Hypothesize → Test → Confirm

1. Form 2-3 hypotheses ranked by likelihood
2. For each hypothesis, define a quick test (< 2 min) to confirm/reject
3. Start with the most likely and cheapest-to-test hypothesis
4. Once confirmed, move to the Fix workflow

---

## Workflow 2: React Native / Expo Error Debugging

### Metro Bundler Errors

```
Error sequence:
1. Clear Metro cache: npx expo start --clear
2. Delete node_modules and reinstall: rm -rf node_modules && npm install
3. Check for circular imports (Metro will usually tell you)
4. Check babel.config.js for plugin conflicts
5. Verify expo SDK version matches all expo-* package versions
```

### Red Screen Errors (Runtime JS Crashes)

```
Diagnostic sequence:
1. Read the FULL error message — the first line is the error, everything below is the stack trace
2. Find the FIRST file in the stack trace that's YOUR code (not node_modules)
3. Go to that file and line number
4. Common causes:
   - Accessing a property on undefined/null (add optional chaining or null checks)
   - Missing import or wrong import path
   - Calling a hook outside a component or in wrong order
   - Async/await without error handling
5. If the error is inside node_modules, it's usually a version mismatch
```

### Build Failures (EAS Build)

```
Diagnostic sequence:
1. Read the build logs from the BOTTOM UP — the actual error is usually near the end
2. Check for:
   - Native module version mismatches (especially react-native-reanimated, react-native-screens)
   - Missing native config plugins in app.json
   - iOS-specific: Provisioning profile or signing issues
   - Pod install failures: often version conflicts
3. Compare working build log with failing build log
4. Check Expo SDK upgrade guide if you recently bumped versions
```

### Navigation Errors

```
Common issues:
1. "Navigator was already mounted" — duplicate NavigationContainer
2. "Couldn't find screen" — typo in screen name or missing registration
3. Expo Router: file not in app/ directory or wrong naming convention
4. Params not passing: check if using expo-router Link vs. navigation.navigate
5. Deep linking broken: check scheme in app.json and linking config
```

---

## Workflow 3: Railway Backend Debugging

### API Connection Issues

```
Diagnostic sequence:
1. Verify Railway service is running (check dashboard for green status)
2. Check Railway logs for startup errors
3. Verify the API URL:
   - Railway provides a *.up.railway.app URL
   - Make sure the app is using the PUBLIC URL, not localhost
   - Check if PORT env var is being read correctly (Railway assigns the port)
4. Test the API independently:
   - curl the health endpoint from terminal
   - Use Postman/Insomnia to isolate frontend vs backend issue
5. CORS: If browser/simulator gets CORS error, check backend CORS config
   - Railway doesn't add CORS headers — your server must
```

### Deploy Failures

```
Diagnostic sequence:
1. Check Railway build logs (similar to EAS — read from bottom up)
2. Common causes:
   - Missing start script in package.json
   - Build command fails (TypeScript errors, missing deps)
   - Port binding: Railway uses $PORT env var, not hardcoded ports
   - Memory limits: free tier has constraints
3. Environment variables: verify all required vars are set in Railway dashboard
4. Database connection: check DATABASE_URL format and SSL settings
```

### Database Issues

```
Diagnostic sequence:
1. Can you connect to the database from Railway's built-in data browser?
2. Check DATABASE_URL — Railway auto-sets this but make sure your ORM reads it
3. Common PostgreSQL issues:
   - SSL: Railway requires SSL; add ?sslmode=require to connection string
   - Connection pooling: too many connections from serverless-style deploys
   - Migrations: did they run? Check if tables exist
4. Query issues: log the actual SQL being executed, not just the ORM call
```

---

## Workflow 4: State & Logic Bugs (No Crash, Wrong Behavior)

```
Diagnostic sequence:
1. Define clearly: what SHOULD happen vs what DOES happen
2. Add console.log at key decision points:
   - Before and after state updates
   - Inside useEffect dependencies
   - At API call and response boundaries
3. Check React DevTools:
   - Is the component re-rendering when expected?
   - Is state what you think it is?
4. Common causes:
   - Stale closure in useEffect (missing dependency)
   - State updates are async — reading state immediately after setState
   - Race conditions in async operations
   - Wrong comparison (== vs ===, object reference vs value)
5. For intermittent bugs:
   - Check for race conditions in parallel async calls
   - Check for unhandled promise rejections
   - Look for timing-dependent code (setTimeout, animation callbacks)
```

---

## Workflow 5: Dependency Audit

```
Steps:
1. Run: npx expo-doctor (checks SDK compatibility)
2. Run: npx expo install --check (finds mismatched versions)
3. Check for peer dependency warnings in npm install output
4. Cross-reference major packages against Expo SDK compatibility:
   - react-native-reanimated
   - react-native-gesture-handler
   - react-native-screens
   - react-native-safe-area-context
5. Look for duplicate packages: npm ls <package-name>
6. Check if any packages have been deprecated or renamed
7. Review Expo's "known issues" page for current SDK version
```

---

## Workflow 6: Pre-Build Health Check

Run this before pushing a build to TestFlight or the App Store.

```
Checklist:
1. [ ] `npx expo-doctor` passes with no errors
2. [ ] `npx expo install --check` shows no mismatches
3. [ ] App runs in Expo Go without errors
4. [ ] App runs in development build without errors
5. [ ] All API endpoints respond (hit health check route)
6. [ ] Railway deploy is green and recent
7. [ ] Environment variables match between dev and production
8. [ ] No console.log statements left in production code
9. [ ] Error boundaries are in place for critical screens
10. [ ] Deep links / universal links work correctly
11. [ ] Push notifications work (if applicable)
12. [ ] App handles offline/poor connectivity gracefully
```
