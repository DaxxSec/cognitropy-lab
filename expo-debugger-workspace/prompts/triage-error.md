# Prompt Template: Quick Error Triage

Use this template when you have an error and want a fast diagnosis.

---

## Prompt

```
I'm getting this error in my Expo app:

**Error message:**
[paste the full error message here]

**Stack trace:**
[paste the full stack trace here]

**What I was doing:**
[describe what action triggered the error]

**When it started:**
[after a package update? code change? randomly?]

**Environment:**
- Testing in: [Expo Go / Dev Build / Production]
- Platform: [iOS Simulator / Physical iPhone / Android]

Please:
1. Classify which layer this error is in (build, runtime JS, native, network, state, environment)
2. Rate severity (Critical / High / Medium / Low)
3. Explain the root cause in plain language
4. Give me the fix as a complete code block I can paste
5. Tell me how to verify the fix worked
```
