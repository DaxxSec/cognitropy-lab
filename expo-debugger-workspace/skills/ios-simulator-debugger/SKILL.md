---
name: ios-simulator-debugger
description: >
  Autonomous visual debugging and testing for React Native / Expo apps running in the iOS Simulator.
  Uses computer-use to screenshot the simulator, tap through every screen, reproduce bugs, read
  error messages, fix code, and retest — all end-to-end with minimal user intervention.
  Use this skill whenever someone asks you to test their app, debug their app, find bugs, fix
  crashes, QA an Expo or React Native project, do a test pass, check if things work on the
  simulator, or anything that involves visually interacting with a mobile app in the iOS Simulator.
  Also trigger when the user shares a React Native / Expo project and wants help getting it
  working, or when they mention red screens, white screens, crashes, or broken navigation.
  Even if they just say "my app is broken" or "can you test this" — use this skill.
---

# iOS Simulator Debugger

You are an autonomous QA engineer and debugger for React Native / Expo apps. You test apps by
visually interacting with the iOS Simulator via computer-use, systematically working through every
screen and component, identifying bugs, fixing code, and retesting until the app is stable.

## How This Works

You have two superpowers working together:

1. **Computer-use** — You can see the iOS Simulator screen, tap on elements (clicks register as
   touches), scroll, and read whatever's visible. You can also see the terminal running Metro
   bundler and read error output.

2. **Filesystem access** — You can read and edit the project's source code directly, run CLI
   commands in the sandbox, and persist test results between sessions.

The iOS Simulator treats your clicks as finger taps. That's all you need to test a touch-screen
app. You don't need to type into the terminal (which is restricted to click-tier) — the user
starts the dev server with one command and you handle the rest.

## The Testing Methodology

### Phase 1: Reconnaissance — Map the App

Before touching the simulator, understand what you're testing.

**Read the codebase and build a component map.** Look at:
- `app/` or `src/` directory structure (screens, components, navigation)
- Navigation config (Expo Router file structure, or React Navigation setup)
- API endpoints and data flows
- Key features and user flows

**Produce a structured app map.** This is your test plan's foundation. Organize it as a hierarchy:

```
App
├── Auth Flow
│   ├── Login Screen
│   │   ├── Email input
│   │   ├── Password input
│   │   ├── Login button → navigates to Home
│   │   └── Sign Up link → navigates to Register
│   └── Register Screen
│       ├── Form fields
│       └── Submit → creates account → navigates to Home
├── Main Tab Navigator
│   ├── Home Tab
│   │   ├── Header with user greeting
│   │   ├── Feed list (scrollable)
│   │   └── Pull-to-refresh
│   ├── Search Tab
│   │   ├── Search input
│   │   └── Results list
│   └── Profile Tab
│       ├── User info display
│       ├── Edit Profile button
│       └── Logout button
└── Modals / Overlays
    ├── Settings modal
    └── Error alerts
```

Save this map to `test-results/app-map.md` in the project directory. This becomes the checklist
you work through during testing.

### Phase 2: Build the Test Plan

From the app map, create a prioritized test plan. Focus on:

1. **Critical paths first** — Can the user sign in? Can they perform the app's core action?
2. **Navigation completeness** — Can you reach every screen? Does back navigation work?
3. **Data operations** — Do creates, reads, updates, deletes actually work?
4. **Edge cases** — Empty states, error handling, offline behavior
5. **Component interactions** — Do buttons respond? Do forms submit? Do lists scroll?

Save the test plan to `test-results/test-plan.md`.

**Do NOT test visual design** unless the user specifically asks you to compare against a provided
mockup. Focus on: does the backend work, do database operations succeed, and do UI components
function correctly when tapped.

### Phase 3: Execute — Test in the Simulator

**Prerequisites the user handles:**
- Start the Expo dev server (`npx expo start`)
- Open the iOS Simulator with the app loaded
- Grant you computer-use access to the Simulator app

**Your testing loop:**

1. **Request access** to the Simulator application via `request_access`
2. **Screenshot** the simulator to see the current state
3. **Orient yourself** — What screen are you on? What's visible?
4. **Work through the test plan systematically:**
   - Screenshot before each action
   - Tap the target element
   - Screenshot after to verify the result
   - Log what happened (pass/fail/unexpected behavior)
5. **Watch for errors at every step:**
   - Red screen = JS runtime crash (read the error message and stack trace)
   - Yellow warning box = non-fatal warning (note it, keep going)
   - White/blank screen = render failure or navigation error
   - Infinite spinner = API call hanging or promise not resolving
   - Nothing happens on tap = event handler missing or broken
   - Layout broken = style issue (note it, keep going unless it blocks testing)
6. **Check the terminal** periodically — screenshot the Metro bundler window to catch
   console errors, network failures, or build warnings that don't show up in the app

**Triage during testing:**

| Severity | What It Looks Like | Action |
|----------|-------------------|--------|
| **Blocking** | App crashes, red screen, can't proceed to next screen | Stop. Fix it now. Retest. |
| **Non-blocking** | Yellow warning, minor glitch, wrong data displayed | Log it. Continue testing. Fix later. |
| **Needs user input** | Auth credentials needed, third-party service config, major refactor required | Log it. Ask user. Continue what you can. |

### Phase 4: Fix

After completing (or getting blocked on) the test plan:

1. **Review all logged issues** from Phase 3
2. **Fix non-blocking bugs** in order of severity (highest first)
3. **For each fix:**
   - Read the relevant source file(s)
   - Identify the root cause (don't just patch symptoms)
   - Make the code change
   - Explain what was wrong and why the fix works

**Guardrails:**
- **Never refactor or make major architectural changes without user approval.** If a fix
  requires restructuring navigation, changing the data model, swapping a library, or touching
  more than 5 files — stop and add it to the report for user review.
- **Never change environment variables, API keys, or backend configuration** without asking.
- **Keep fixes minimal and targeted.** Fix the bug, don't redesign the feature.

### Phase 5: Retest

After applying fixes:

1. The app should hot-reload automatically (Expo fast refresh)
2. Screenshot the simulator to verify the app reloaded
3. Re-run the specific test cases that failed
4. Verify the fixes work
5. Check for regressions — make sure you didn't break something that was working

If new bugs surface during retesting, triage and fix them following the same rules.

### Phase 6: Report

Save a comprehensive test report to `test-results/test-report-YYYY-MM-DD.md`:

```markdown
# Test Report — [Date]

## Summary
- Total screens tested: X
- Total components tested: X
- Bugs found: X (Y critical, Z non-blocking)
- Bugs fixed: X
- Bugs needing user input: X

## Test Results by Screen

### [Screen Name]
- **Status:** Pass / Fail / Partial
- **Components tested:** [list]
- **Issues found:**
  - [Issue description] — [Fixed / Needs User Input / Logged]

## Bugs Fixed
| # | Description | Root Cause | Fix Applied | Files Changed |
|---|-------------|-----------|-------------|---------------|
| 1 | ... | ... | ... | ... |

## Needs User Input
| # | Description | Why User Input Is Needed | Suggested Options |
|---|-------------|------------------------|-------------------|
| 1 | ... | ... | ... |

## Remaining Known Issues
| # | Description | Severity | Notes |
|---|-------------|----------|-------|
| 1 | ... | ... | ... |

## Next Steps
[What should happen next — retesting after user decisions, areas not yet tested, etc.]
```

Present this report to the user when testing is complete.

## Session Continuity

Previous test results matter. Before starting a new test session:

1. **Check for existing test results** in `test-results/`
2. **Read the most recent test report** — What was found? What was fixed? What needed user input?
3. **Ask the user** if they've addressed the items that needed their input
4. **Reference the previous app map** — Has the app changed? Update the map if needed.
5. **Focus the new session** on: retesting previous fixes, testing areas flagged as needing
   user input (if resolved), and testing any new features or changes

Never start from scratch if previous results exist. Build on them.

## Common Expo / React Native Patterns

See `references/common-issues.md` for a catalog of error patterns you'll encounter in the
simulator and their typical root causes. Consult it when you see an error you need to diagnose.

## Computer-Use Tips for the iOS Simulator

- **Tapping:** A regular `left_click` at the right coordinates registers as a finger tap
- **Scrolling:** Use `scroll` with direction `up` or `down` to scroll lists
- **Text input:** Tap a text field first, then use `type` to enter text (the simulator accepts
  keyboard input when a field is focused)
- **Back navigation:** Tap the back button in the nav bar, or swipe from left edge using
  `left_click_drag` from x=0 to x=150 at the vertical center
- **Pull to refresh:** `left_click_drag` from center-top to center-bottom of a scrollable list
- **Modals/alerts:** Check for overlay elements before tapping through them
- **Screenshot the terminal:** The Metro bundler terminal is a separate window — screenshot it
  separately from the simulator to read console output
- **Zoom in:** Use the `zoom` action to read small text in error messages or stack traces
- **Wait for loads:** After tapping a button that triggers an API call, `wait` 2-3 seconds
  before screenshotting to let the response come back

## Log Monitoring

Whenever you're able to see the terminal running Metro bundler or Expo:

- **Red text** = errors (read carefully)
- **Yellow text** = warnings (note them)
- **Network request logs** = check for failed API calls (4xx, 5xx status codes)
- **"Invariant Violation"** = React component error (usually a hook or render issue)
- **"TypeError: undefined is not an object"** = null reference (needs optional chaining or guard)
- **"Network request failed"** = API unreachable (check URL, CORS, Railway status)

If you can't see the terminal, that's OK — the simulator red/yellow screens capture most critical
errors. But if you can see it, always check it between screens.
