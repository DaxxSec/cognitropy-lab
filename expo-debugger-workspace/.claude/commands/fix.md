# /fix — Generate a Complete Fix

When the bug is understood and you just need the code changes. Produces copy-paste-ready fixes.

## Instructions

### Input Required

Ask for:
1. Which bug are we fixing? (reference a previous triage, or describe it)
2. The current code that has the bug (paste the file or relevant section)
3. What it should be doing instead

### Fix Output Format

For each file that needs changes:

```
## Fix: [brief description]

### File: [path/to/file.tsx]

**What's wrong**: [one sentence]
**Why**: [one sentence root cause]

#### Current Code (lines X-Y):
[show the buggy code block]

#### Fixed Code:
[show the complete fixed code block — enough context that it can be pasted directly]

#### What Changed:
- [bullet point each change and why]
```

### Rules for Fixes

1. **Show complete functions/components**, not just the changed line — context prevents paste errors
2. **Include all imports** if adding new ones
3. **Preserve existing code style** (semicolons, quotes, spacing)
4. If the fix requires installing a package, state the exact command: `npx expo install <package>`
5. If the fix requires an environment variable, state exactly where to set it
6. If the fix touches more than 3 files, present a summary plan first and confirm before showing all changes

### Verification

After the fix code, always include:

```
## Verify the Fix

1. [Step to confirm the fix works — e.g., "Run `npx expo start --clear` and navigate to the Settings screen"]
2. [What you should see — e.g., "The profile image should load without a red screen error"]
3. [Optional regression check — e.g., "Also confirm the home screen still loads correctly"]
```

### Save to Outputs

Save the fix to `outputs/` as `fix-YYYY-MM-DD-[brief-name].md` for reference.
Log the fix to `work-log/`.
