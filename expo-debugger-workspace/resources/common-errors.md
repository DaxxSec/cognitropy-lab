# Common React Native / Expo Errors — Quick Reference

A catalog of frequently encountered errors with root causes and fixes. The agent should consult this during triage and debugging.

---

## Build & Bundling Errors

### "Unable to resolve module" / "Module not found"

**Root cause**: Import path is wrong, package isn't installed, or Metro cache is stale.
**Fix sequence**:
1. Check the import path for typos (case-sensitive on iOS!)
2. Verify the package is in `package.json` and `node_modules/`
3. If it should be there: `rm -rf node_modules && npm install`
4. Clear Metro cache: `npx expo start --clear`
5. If using path aliases: check `tsconfig.json` paths AND `babel.config.js` module-resolver

### "Invariant Violation: requireNativeComponent"

**Root cause**: A native module is used but not linked, or the wrong version is installed.
**Fix**: `npx expo install <package-name>` to get the Expo-compatible version. If using a dev build, rebuild with `eas build --profile development`.

### "Error: Reanimated 2 failed to create a worklet"

**Root cause**: `react-native-reanimated` babel plugin not configured or wrong version.
**Fix**:
1. Add to `babel.config.js`: `plugins: ['react-native-reanimated/plugin']` (must be LAST plugin)
2. Clear Metro cache: `npx expo start --clear`
3. If still failing, check reanimated version matches Expo SDK

### "SyntaxError: Unexpected token" in Metro

**Root cause**: Code uses syntax that Babel can't transform (optional chaining in dependencies, JSX in .js files, etc.)
**Fix**: Check if the error is in YOUR code or `node_modules`. If node_modules, the package may need to be added to Metro's `transformIgnorePatterns`.

---

## Runtime Errors (Red Screen)

### "TypeError: Cannot read property 'X' of undefined"

**Root cause**: Accessing a property on a variable that is `undefined` or `null`.
**Common scenarios**:
- API response is `undefined` because the request failed silently
- Navigation params not passed correctly
- State hasn't been initialized yet (component renders before data loads)
**Fix**: Add optional chaining (`?.`) and null checks. Handle loading states.

### "TypeError: X is not a function"

**Root cause**: The variable isn't what you think it is.
**Common scenarios**:
- Wrong import (named vs default export mismatch)
- Calling a component as a function instead of rendering it as JSX
- Overwriting a function with a state variable of the same name
**Fix**: Check the import statement. Check `typeof X` to see what it actually is.

### "Too many re-renders. React limits the number of renders"

**Root cause**: State update is happening during render, causing an infinite loop.
**Common scenarios**:
- Calling `setState()` directly in the component body instead of in `useEffect` or an event handler
- `onPress={() => doSomething()}` vs `onPress={doSomething()}` (extra parentheses = called during render)
**Fix**: Move state updates into `useEffect` or event handlers. Remove the `()` from handler assignments.

### "Invalid hook call"

**Root cause**: Hooks called outside a React component, or multiple copies of React in node_modules.
**Fix sequence**:
1. Ensure hooks are at the top level of a component (not in if/else, loops, or callbacks)
2. Check for duplicate React: `npm ls react` (should show only one version)
3. If duplicate: `rm -rf node_modules && npm install`

### "VirtualizedLists should never be nested inside ScrollViews"

**Root cause**: FlatList/SectionList inside a ScrollView causes performance issues.
**Fix**: Use `ListHeaderComponent` and `ListFooterComponent` props on FlatList instead of wrapping in ScrollView.

---

## Navigation Errors

### "No route found for key X"

**Root cause**: Navigating to a screen name that doesn't exist in the navigator.
**Fix**: Check for typos in screen names. Ensure the screen is registered in the correct navigator.

### Expo Router: "Unmatched Route"

**Root cause**: File-based routing can't find a matching file in `app/` directory.
**Fix**: Check file naming convention. `app/index.tsx` = root, `app/settings.tsx` = /settings, `app/(tabs)/` = tab layout.

### "Tried to navigate before navigation was ready"

**Root cause**: Calling `navigation.navigate()` before the navigator has mounted.
**Fix**: Use `navigation.isReady()` check or move navigation calls to `useEffect`.

---

## Network & API Errors

### "Network request failed" / "TypeError: Network request failed"

**Root cause**: Can't reach the server.
**Check sequence**:
1. Is the device/simulator connected to the internet?
2. Is the API URL correct? (not `localhost` if on physical device)
3. Is the Railway service running?
4. Is the URL `https://` (not `http://`)?
5. For iOS Simulator: `localhost` works. For physical device: use the machine's IP or Railway URL.

### "CORS error" / "Access-Control-Allow-Origin"

**Root cause**: Backend doesn't allow requests from the app's origin.
**Fix**: Configure CORS on the Railway backend to allow the app's origin. For development: allow all origins.

### HTTP 401 / 403

**Root cause**: Authentication token is missing, expired, or invalid.
**Check**: Is the token being sent in the Authorization header? Is it expired? Is the backend validating it correctly?

### HTTP 500

**Root cause**: Server-side error. The fix is in the Railway backend.
**Check**: Railway logs for the actual error. The frontend error message is usually generic.

---

## State Management Errors

### Stale State in Closures

**Symptom**: State value is always the old value inside a callback or useEffect.
**Root cause**: JavaScript closures capture the state value at the time the closure was created.
**Fix**: Use `useRef` for values you need to read in callbacks, or add the state variable to the `useEffect` dependency array.

### "Can't perform a React state update on an unmounted component"

**Root cause**: Async operation completes after the component unmounts (navigation away, etc.)
**Fix**: Use an abort controller or cleanup function in `useEffect`:
```javascript
useEffect(() => {
  let cancelled = false;
  fetchData().then(data => {
    if (!cancelled) setData(data);
  });
  return () => { cancelled = true; };
}, []);
```

---

## Expo-Specific Errors

### "Expo Go is not compatible with this SDK version"

**Root cause**: SDK version in app.json doesn't match the Expo Go app version.
**Fix**: Update Expo Go on the device, or downgrade the SDK version in app.json.

### "This app is not allowed to query for scheme: X"

**Root cause**: iOS requires declaring URL schemes in Info.plist for `Linking.canOpenURL`.
**Fix**: Add `ios.infoPlist.LSApplicationQueriesSchemes` to app.json.

### EAS Build: "Provisioning profile doesn't match"

**Root cause**: iOS signing credentials mismatch.
**Fix**: Run `eas credentials` and manage signing. Often: `eas build --clear-cache --platform ios`.

---

## Performance Issues

### Slow FlatList / Choppy Scrolling

**Causes**: Heavy components in list items, missing `keyExtractor`, images not cached.
**Fixes**: Use `React.memo()` on list items, add `keyExtractor`, use `expo-image` with caching, set `windowSize` and `maxToRenderPerBatch`.

### App Startup Slow

**Causes**: Too much work on mount, large bundle, synchronous storage reads.
**Fixes**: Lazy load screens, use code splitting, move storage reads to async, use splash screen to mask load time.
