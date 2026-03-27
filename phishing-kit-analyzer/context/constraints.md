# Constraints & Boundaries

> This file is populated during `/onboard`. Below are placeholders.

## Hard Constraints
- **No code execution** — all analysis is static; never run kit code
- **Evidence preservation** — never modify original kit files
- **PII handling** — harvested credentials found in kits must be handled per org policy
- **Classification** — outputs may be TLP-marked; respect sharing boundaries

## Analyst Preferences
<!-- Populated during onboard -->
- Preferred output format: <!-- STIX 2.1 / CSV / JSON / Markdown -->
- Report verbosity: <!-- Executive summary / Technical detail / Full teardown -->
- IOC confidence tagging: <!-- Yes/No, and what scale? -->
- Attribution threshold: <!-- How confident before you'll name an actor? -->

## Environment Constraints
<!-- Populated during onboard -->
- Air-gapped analysis: <!-- Yes/No -->
- Can access VirusTotal: <!-- Yes/No -->
- Can access URLScan: <!-- Yes/No -->
- Can push to MISP: <!-- Yes/No -->
- TLP default for outputs: <!-- WHITE / GREEN / AMBER / RED -->
