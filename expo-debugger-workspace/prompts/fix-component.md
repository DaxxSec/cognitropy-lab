# Prompt Template: Fix a Broken Component

Use this when a specific screen or component isn't working correctly.

---

## Prompt

```
This component in my Expo app isn't working correctly:

**File:** [path to the file, e.g., app/screens/ProfileScreen.tsx]

**Current code:**
[paste the full component code]

**Expected behavior:**
[what it should do]

**Actual behavior:**
[what it actually does — include any errors if present]

**Related files** (if relevant):
- API call: [path to API service file]
- Navigation: [how the user gets to this screen]
- State: [where the data comes from — context, props, API]

Please:
1. Identify every bug in this component
2. For each bug, explain the root cause
3. Provide the complete fixed component code (not just diffs)
4. List any changes needed in other files
5. Tell me how to test that each fix works
```
