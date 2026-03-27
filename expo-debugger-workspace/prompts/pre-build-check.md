# Prompt Template: Pre-Build Checklist

Use this before running `eas build` to catch issues early.

---

## Prompt

```
I'm about to run an EAS Build for my Expo app. Please help me check everything is ready.

**Build target:**
- Platform: [iOS / Android / Both]
- Profile: [development / preview / production]
- Distribution: [TestFlight / App Store / Internal]

**Recent changes since last successful build:**
[list what you changed — packages updated, new screens, config changes]

**Please check:**
1. Review my package.json dependencies for version conflicts
2. Verify my app.json / app.config.js has all required fields
3. Check that my eas.json build profile is correctly configured
4. Confirm my Railway backend env vars match what the app expects
5. Flag any common issues that could cause the build to fail
6. Suggest a quick local test I should run before triggering the cloud build

**My package.json:**
[paste it]

**My app.json:**
[paste it]

**My eas.json:**
[paste it]
```
