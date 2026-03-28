# /firmware-check — Firmware & CVE Assessment

Assess firmware currency and identify known vulnerabilities in deployed devices.

## Steps
1. Collect device list from asset inventory (or gather device info now):
   - Manufacturer, model, firmware version for each device
   - Flag any devices with "Unknown" firmware version

2. For each device, perform CVE correlation:
   - Search CISA ICS-CERT advisories: https://www.cisa.gov/ics-advisories
   - Cross-reference CISA KEV list for known exploited vulnerabilities
   - Note CVSS scores and exploitability
   - Check if CVE is exploitable from network (vs. physical access)

3. Flag critical CVEs:
   - CVSS ≥ 9.0: Document as Critical finding
   - CVSS 7.0-8.9: Document as High finding
   - Any CVE on CISA KEV list: Escalate to Critical regardless of CVSS
   - Unitronics CVE-2023-6448 specifically — widely exploited in OT ransomware

4. If firmware binary is provided:
   - Guide through binwalk extraction
   - Search for hardcoded credentials
   - Check embedded component versions
   - Identify exposed network endpoints
   - Generate YARA/string indicators if malicious content suspected

5. Produce firmware/CVE findings report:
   - Device-by-device vulnerability summary
   - Prioritized patch recommendations with biological maintenance window guidance
   - For unpatched legacy devices: compensating controls (network isolation, monitoring)
   - Save to `outputs/firmware-cve-[date].md`

Reference: `context/for-agent/workflows.md` — Workflow 5
