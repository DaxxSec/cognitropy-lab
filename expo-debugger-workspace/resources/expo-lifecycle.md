# Expo App Lifecycle & Build Pipeline Reference

Understanding the Expo development and build lifecycle helps diagnose where bugs originate.

---

## Development Modes

### Expo Go
- Quick prototyping, no native code changes
- Limitations: can't use custom native modules, limited background tasks
- When it breaks: usually SDK version mismatch or unsupported module

### Development Build
- Custom native runtime built with `eas build --profile development`
- Supports all native modules and config plugins
- When it breaks: native module version mismatch, missing config plugin

### Production Build
- Final build for TestFlight / App Store
- Built with `eas build --profile production`
- When it breaks: different env vars, optimizations expose hidden bugs, missing assets

## The Build Pipeline

```
Source Code
    ↓
Metro Bundler (transpiles JS/TS → bundle.js)
    ↓
Expo Config (app.json / app.config.js → native project config)
    ↓
Config Plugins (modify native iOS/Android projects)
    ↓
EAS Build (cloud build → .ipa / .apk)
    ↓
EAS Submit (upload to TestFlight / Play Console)
```

**Where errors happen at each stage:**
- Metro: import errors, syntax errors, babel config issues
- Config: missing permissions, wrong bundle ID, bad splash/icon
- Config Plugins: native dependency not configured properly
- EAS Build: pod install failures, signing issues, native compilation errors
- EAS Submit: metadata issues, provisioning profile problems

## Key Configuration Files

### app.json / app.config.js
- App name, slug, version, SDK version
- iOS bundle identifier and Android package name
- Permissions, splash screen, icon
- Config plugins
- EAS project ID

### babel.config.js
- Presets: `babel-preset-expo` (always required)
- Plugins: reanimated plugin must be LAST
- Module resolver for path aliases

### metro.config.js
- Usually not needed for basic Expo apps
- Required for: SVG support, monorepo setups, custom asset extensions
- Common issue: overriding without extending default config

### tsconfig.json
- Strict mode settings
- Path aliases (must match babel module-resolver)
- Base URL for imports

### eas.json
- Build profiles (development, preview, production)
- Build configuration (node version, env vars, distribution)
- Submit configuration

## React Native Component Lifecycle

```
Component Mount:
  1. Constructor / initial state (useState initial value)
  2. First render
  3. DOM update
  4. useEffect runs (after paint)
  5. useLayoutEffect runs (before paint — use sparingly)

Component Update:
  1. Props or state change triggers re-render
  2. New render output computed
  3. DOM diffed and updated
  4. useEffect cleanup runs (for previous deps)
  5. useEffect runs (with new deps)

Component Unmount:
  1. useEffect cleanup runs
  2. Component removed from tree
```

**Common lifecycle bugs:**
- Fetching data without cleanup → memory leak / state update on unmounted component
- Missing `useEffect` dependency → stale data
- Too many dependencies in `useEffect` → infinite re-render loop
- Work in render body → performance issues / too many re-renders

## Expo SDK Upgrade Checklist

When upgrading Expo SDK versions:

1. Read the official upgrade guide for the target version
2. Update `expo` package: `npx expo install expo@latest`
3. Update all `expo-*` packages: `npx expo install --fix`
4. Run `npx expo-doctor` to find remaining issues
5. Check `react-native` version compatibility
6. Check `react-native-reanimated` compatibility
7. Clear all caches: `rm -rf node_modules && npm install && npx expo start --clear`
8. Test in Expo Go first, then development build
9. Test production build before submitting

## Debugging Tools

### React Native Debugger
- Shake device / Cmd+D in simulator → "Debug Remote JS"
- Use Chrome DevTools for breakpoints and network inspection
- Note: Hermes debugger is different from Chrome debugger

### Expo Dev Tools
- Press `?` in Metro terminal for all options
- `r` = reload, `m` = toggle menu, `j` = open debugger
- Shake device for dev menu on physical device

### Flipper (optional)
- Network inspector, layout inspector, React DevTools
- Requires setup for Expo managed workflow

### Console Logging Best Practices
- Use structured logging: `console.log('[Screen] action:', data)`
- Log API requests and responses during debugging
- Remove or gate console.logs before production builds
- Use `__DEV__` flag: `if (__DEV__) console.log(...)`
