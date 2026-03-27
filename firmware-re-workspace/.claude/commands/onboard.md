# /onboard — Workspace Initialization

Welcome to the Firmware RE Workspace. This command walks you through a setup interview to personalize the workspace for your use case and current target.

## What This Does
- Gathers your profile and experience level
- Documents your toolchain and environment
- Records your current target firmware details
- Sets authorization scope and constraints
- Writes all context to the appropriate files in `context/`

---

## Interview Flow

Conduct this as a conversation. Ask questions in logical groups, wait for answers, then proceed to the next group.

### Group 1: User Profile

Ask the user:
1. What's your name or handle?
2. What's your primary role? (DFIR analyst, security researcher, pentester, hobbyist, student, other)
3. How experienced are you with firmware reverse engineering? (Beginner / Intermediate / Advanced / Expert)
4. What disassemblers do you use? (Ghidra, radare2, Binary Ninja, IDA, other)
5. Are you comfortable with Python scripting for automation?

Save to: `context/role.md`

---

### Group 2: Environment & Toolchain

Ask the user:
1. What OS are you working on? (Linux distro, macOS, Windows WSL2)
2. Do you have binwalk installed? Any other extraction tools (sasquatch, jefferson, ubireader)?
3. Do you have qemu available for emulation?
4. Do you have hardware tools? (JTAG debugger, UART adapter, logic analyzer)
5. What's your primary working directory for firmware files?

Save to: `context/for-agent/environment.md`

Fill in the template fields based on answers. Mark tools as `yes` or `no`.

---

### Group 3: Current Target (Optional — skip if no active target)

Ask the user:
1. Do you have a firmware target you want to start working on right now?
   - If yes, continue below
   - If no, skip to Group 4

2. What device/product is this firmware for?
3. What is the firmware version or filename?
4. Where did you get the firmware? (vendor download, device extraction, evidence seizure, CTF, etc.)
5. What is the SHA256 hash of the firmware file? (run: `sha256sum firmware.bin`)
6. What is the investigation type? (Security research / DFIR / Bug bounty / CTF / Personal)

Save to: `context/project.md`

---

### Group 4: Constraints & Authorization

Ask the user:
1. Are you authorized to analyze this firmware? What is the basis of that authorization?
2. Are there any files, systems, or actions that should be off-limits?
3. Do you have any disclosure obligations? (CVD timeline, internal only, no disclosure)
4. Should I avoid suggesting any specific tools?
5. Are there evidence handling requirements? (e.g., DFIR chain of custody, encryption)

Save to: `context/constraints.md`

---

### Group 5: Preferences

Ask the user:
1. How much detail do you want in explanations? (Terse commands only / Step-by-step guidance / Explain the reasoning)
2. Do you prefer terminal commands, markdown reports, or both?
3. What report format do you prefer for findings? (Markdown / PDF / DOCX)

Save to: `context/role.md` (communication preferences section)

---

## Post-Interview Actions

After collecting all answers:

1. Write all populated files to `context/`
2. Create a first work log entry:
   ```
   work-log/[YYYY-MM-DD].md
   ## Session: [date] — Workspace Onboarded
   ### Summary
   Workspace initialized for [user name/handle].
   Target: [target name or "No active target"]
   Toolchain: [brief summary]
   ```
3. Confirm to the user:
   > "Workspace initialized! Your profile and environment are saved in `context/`.
   > You're ready to start. Try `/analyze-firmware` to begin, or `/toolchain-setup` if you need help getting your tools ready."
