# /onboard — Initialize Wireless Protocol RE Workspace

Welcome to the Wireless Protocol Reverse Engineering workspace. I'll gather your setup details to customize this environment.

## Interview Flow

### 1. Hardware Profile
Ask the user:
- What SDR hardware do you have? (HackRF One, RTL-SDR v3, USRP, LimeSDR, other)
- What antennas are available? (wideband, directional, frequency-specific)
- Do you have a Faraday cage or RF-isolated test environment?

Save responses to `context/for-agent/environment.md`.

### 2. Target Profile
Ask the user:
- What device(s) or signal(s) are you trying to reverse engineer?
- What frequency range(s) are you interested in?
- Do you have physical access to the target device?
- What's your legal authorization for this analysis?

Save responses to `context/project.md`.

### 3. Experience & Tools
Ask the user:
- Experience level with SDR and protocol analysis? (beginner/intermediate/advanced)
- Software already installed? (GNU Radio, URH, Inspectrum, rtl_433, etc.)
- What OS are you running?
- Comfortable with Python scripting for custom decoders?

Save responses to `context/role.md` and `context/for-agent/environment.md`.

### 4. Goals & Constraints
Ask the user:
- What does success look like? (full protocol spec, replay capability, documentation, vulnerability assessment)
- Any time constraints or deadlines?
- Storage capacity for IQ captures?
- Processing power available?

Save responses to `context/project.md` and `context/constraints.md`.

## Post-Onboard Actions
1. Recommend optimal SDR settings for their target frequency
2. Suggest a capture plan based on their hardware capabilities
3. Create an initial analysis plan in `planning/plan.md`
4. Log the onboarding session in `work-log/`
