# Common iOS Simulator Issues — Expo / React Native

Quick-reference catalog of error patterns you'll encounter when testing in the simulator.
Organized by what you'll SEE, not by technical category — because you're diagnosing visually.

---

## Red Screen Errors (App Crashes)

### "TypeError: undefined is not an object (evaluating 'X.Y')"
**What you see:** Red screen with this error message
**Root cause:** Trying to access a property on something that's null or undefined
**Common triggers:** API response hasn't loaded yet, missing navigation params, optional data field
**Fix pattern:** Add optional chaining (`obj?.property`) or null guards (`if (obj) {...}`)

### "Invariant Violation: Rendered more hooks than during the previous render"
**What you see:** Red screen, often on navigation
**Root cause:** Conditional hook calls — a `useState` or `useEffect` inside an `if` block
**Fix pattern:** Move all hooks to the top of the component, before any conditionals

### "Invariant Violation: Text strings must be rendered within a <Text> component"
**What you see:** Red screen pointing to a JSX return
**Root cause:** Bare string or expression outside of `<Text>` tags in JSX
**Fix pattern:** Wrap the string in `<Text>` or check for accidental whitespace between components

### "Maximum update depth exceeded"
**What you see:** Red screen, app becomes unresponsive before crashing
**Root cause:** Infinite re-render loop — usually a `useEffect` that sets state in its own dependency
**Fix pattern:** Check `useEffect` dependency arrays. Remove the state variable causing the loop.

### "Cannot read property 'navigate' of undefined"
**What you see:** Red screen when trying to navigate
**Root cause:** `navigation` prop not available — component isn't inside a navigator
**Fix pattern:** Use `useNavigation()` hook instead of props, or ensure component is a screen

---

## White / Blank Screen

### App loads but shows nothing
**Possible causes (check in order):**
1. JS bundle failed to load — check Metro terminal for errors
2. Root component returns null — check conditional rendering logic
3. Navigation container issue — no initial route defined
4. Splash screen stuck — `SplashScreen.hideAsync()` never called
5. Auth check blocking render — async auth state hasn't resolved

### Screen navigates to but is blank
**Possible causes:**
1. Component renders `null` due to loading state that never resolves
2. Data fetch fails silently — no error handling on the fetch call
3. SafeAreaView with wrong flex — content renders but is off-screen
4. Wrong background color — content is there but same color as background

---

## Infinite Loading / Spinner

### Spinner never stops
**Check in order:**
1. API endpoint reachable? (Check Railway deploy status)
2. API URL correct? (Not `localhost` — must be the Railway public URL)
3. Network error caught but not shown to user?
4. Response format mismatch? (API returns different shape than expected)
5. CORS blocking the request? (Check terminal for CORS errors)

### Loading indicator appears then nothing happens
**Usually:** The API call completed but the response handling has a bug
**Check:** Console logs around the `.then()` or `await` that processes the response

---

## Navigation Problems

### Tapping a button does nothing (no navigation)
**Possible causes:**
1. `onPress` handler missing or misspelled (`onpress` vs `onPress`)
2. Navigation action references wrong screen name (typo)
3. Touchable component wrapping issue — inner element swallowing the press
4. Button disabled state — check if there's a conditional disable

### Screen flickers / navigates then immediately goes back
**Root cause:** Usually a `useEffect` on the target screen that triggers navigation back
**Check:** Effects that run on mount and check some condition (auth, data) then navigate away

### Tab bar or bottom nav not showing
**Common causes:**
1. `tabBarStyle: { display: 'none' }` set somewhere
2. Screen is in a nested stack that hides the tab bar
3. Tab component import error

---

## API / Network Issues

### "Network request failed"
**If testing on simulator:**
1. Check the API URL — `localhost` won't work from the simulator for a remote backend
2. Check Railway service status — is it deployed and running?
3. Check for CORS — the browser/simulator may block cross-origin requests
4. Check SSL — Railway requires HTTPS

### Data doesn't save / changes disappear
**Check:**
1. POST/PUT request actually firing? (Watch Metro console for network logs)
2. Request body formatted correctly? (JSON.stringify issues)
3. Auth token being sent? (Check headers)
4. Railway database actually receiving writes? (Check Railway logs)

### Data loads but is wrong or stale
**Check:**
1. Caching — is there a local cache (AsyncStorage) serving old data?
2. Query parameters — is the right filter/ID being sent?
3. State update — is the component re-rendering after new data arrives?

---

## Build / Metro Errors (Visible in Terminal)

### "Unable to resolve module"
**Cause:** Import path is wrong or package isn't installed
**Fix:** Check the import path, run `npx expo install <package>` if missing

### "Module not found: Can't resolve"
**Cause:** Same as above but from webpack/metro resolution
**Fix:** Check for typos in import, verify file exists at that path

### "Requiring unknown module"
**Cause:** Circular dependency or module resolution failure
**Fix:** Check for circular imports between files, restructure if needed

---

## Simulator-Specific Gotchas

### App works in Expo Go but crashes in dev build
**Cause:** Native module not configured — needs a config plugin in app.json
**Fix:** Check which native modules the crash references, add config plugins

### Touch doesn't register on some elements
**Possible causes:**
1. Element is behind another (invisible) view — check z-index
2. `pointerEvents="none"` on a parent container
3. `TouchableOpacity` vs `Pressable` — try switching
4. Absolute positioning placing the hit target elsewhere

### Keyboard covers input field
**Fix:** Use `KeyboardAvoidingView` or `ScrollView` with `keyboardShouldPersistTaps="handled"`

### Status bar overlaps content
**Fix:** Use `SafeAreaView` from `react-native-safe-area-context` (not the one from `react-native`)
