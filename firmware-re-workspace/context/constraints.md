# Constraints & Preferences
<!-- Populated by /onboard -->

## Legal & Authorization
- **Authorization Type:** [written consent / vendor program / own device / DFIR legal hold / CTF]
- **Scope Statement:** [describe exactly what you're authorized to analyze]
- **Jurisdiction:** [country/region — affects DMCA, CFAA applicability]
- **Out of Scope:** [explicitly list what you should NOT analyze or touch]

## Tool Preferences
- **Primary Disassembler:** [Ghidra / radare2 / Binary Ninja / IDA / other]
- **Preferred Scripting:** [Python / Bash / other]
- **Emulation Available:** [yes/no — qemu-user-static, qemu-system, unicorn]
- **Hardware Tools Available:** [JTAG debugger, UART adapter, logic analyzer, etc.]
- **Avoid Tools:** [any tools you don't want suggested]

## Output Preferences
- **Report Format:** [Markdown / PDF / DOCX]
- **Finding Severity Scale:** [CVSS / custom / qualitative]
- **Evidence Handling:** [should outputs be kept local? encryption required?]

## Analysis Constraints
- **Time Box:** [time limit per session, if any]
- **Depth:** [quick triage / thorough analysis / exhaustive research]
- **Disclosure Intent:** [CVD / public / internal only / no disclosure]

## Safety Rails
- Do not execute extracted binaries without explicit permission
- Flag any findings that suggest malware or implants before proceeding
- Do not transmit firmware images or extracted files to external services
- Always document chain of custody if this is a DFIR investigation
