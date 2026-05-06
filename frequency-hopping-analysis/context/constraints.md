# Boundaries & Constraints

> Populated by `/onboard`. The agent treats every section here as a hard constraint.

## Authorisation Scope

- **Target system:** _____
- **Authorisation document on file:** (path / link)
- **Authorising party:** (legal name + role)
- **Scope of authorisation:**
  - [ ] Receive only (passive monitoring)
  - [ ] Demodulation of cleartext payload
  - [ ] Decryption of payload (with key provided by authoriser)
  - [ ] Active probing / replay (RARE — almost never enabled for FHSS work)
  - [ ] Transmission on target band (RARE — requires licensing)
- **Frequency range authorised:** _____
- **Time window authorised:** _____
- **Geographic location of authorised work:** _____

## Hard Prohibitions (default — only override with explicit written authorisation)

- **No transmission** on the target system or any band protected by licensing rules.
- **No follower jamming, sweep jamming, or any active interference.**
- **No replay attacks** — captured FHSS traffic is not retransmitted under any circumstances.
- **No payload decryption attempts** without explicit cryptographic authorisation.
- **No reception** of cellular bands, public-safety encrypted channels, or other Wiretap-Act-protected systems.
- **No exfiltration** of recovered hop sequences or sensitive captures outside this workspace until findings have been responsibly disclosed to vendor / CERT.

## Jurisdictional Notes

- US: 47 CFR Part 15 (consumer ISM), 47 USC §605 (general radio surveillance prohibition), 18 USC §2511 (Wiretap Act).
- EU: Radio Equipment Directive 2014/53/EU; member-state surveillance laws vary.
- UK: Wireless Telegraphy Act 2006 — receiving is generally OK in ISM, but recovering content from non-public services is illegal.

If you are unsure which regime applies, the agent must halt the analysis and ask before proceeding.

## Reporting Constraints

- All findings get a Bayesian posterior with credibility interval — no point estimates.
- All captures referenced in reports must include SigMF metadata.
- Vulnerability findings are embargoed until vendor + CERT acknowledgement (90-day default per CERT/CC).

## Resource Constraints

- Storage budget: _____ TB
- Compute budget: _____ (cores, GPUs)
- Time budget: _____ (deadline for findings)
