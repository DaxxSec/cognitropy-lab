# /deps — Dependency Audit

Check for version conflicts, deprecated packages, and known compatibility issues across the React Native / Expo / Railway stack.

## Instructions

Ask the user to provide:
1. Their `package.json` (paste it or share the file)
2. Output of `npx expo-doctor` (if they can run it)
3. Output of `npx expo install --check` (if they can run it)

## Audit Steps

### 1. Expo SDK Compatibility

Check that all `expo-*` packages match the installed Expo SDK version.
- Run `npx expo install --check` to identify mismatches
- Cross-reference with Expo's compatibility table for the current SDK version
- Flag any packages that are ahead of or behind the SDK

### 2. React Native Core Packages

These packages are tightly coupled and must be compatible:
- `react-native`
- `react-native-reanimated`
- `react-native-gesture-handler`
- `react-native-screens`
- `react-native-safe-area-context`
- `@react-navigation/*` or `expo-router`

Check versions against Expo's recommended versions for the current SDK.

### 3. Duplicate Packages

Look for multiple versions of the same package:
```bash
npm ls react-native-reanimated
npm ls react-native-screens
```

Duplicates cause subtle crashes and "hook" errors.

### 4. Deprecated Packages

Flag any packages that are:
- No longer maintained
- Renamed (e.g., old Expo packages that moved to `expo-*`)
- Replaced by built-in Expo modules

### 5. Known Issue Packages

Check for packages with known issues in the current Expo SDK:
- react-native-reanimated worklet issues
- react-native-svg version mismatches
- AsyncStorage migration to @react-native-async-storage
- Moment.js (suggest date-fns or dayjs for bundle size)

### 6. Peer Dependency Warnings

Review `npm install` output for peer dependency warnings.
- These are often the silent cause of runtime errors
- Suggest resolution for each warning

## Output Format

```
## Dependency Audit Report — [Date]

### Summary
- Total packages: [X]
- Issues found: [X]
- Critical: [X] | Warning: [X] | Info: [X]

### Critical Issues
[Issues that will likely cause crashes or build failures]

### Warnings
[Issues that may cause problems or are not best practice]

### Recommendations
[Suggested package updates, replacements, or removals]

### Fix Commands
[Exact npm/expo install commands to resolve all issues]
```

Save report to `outputs/deps-audit-YYYY-MM-DD.md`.
