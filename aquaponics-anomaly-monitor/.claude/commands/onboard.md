# /onboard — Workspace Initialization

You are initializing the Aquaponics Anomaly Monitor workspace for a new operator's specific system.

## Step 1: Introduction
Welcome the operator. Explain that you'll ask a series of questions to understand their system so you can provide accurate, calibrated monitoring and analysis.

## Step 2: System Profile Interview
Ask these questions in a natural, conversational flow (not a rigid questionnaire):

1. What species of fish are you raising, how many, and roughly what size/weight are they?
2. What is your total fish tank volume? (liters or gallons)
3. What are your plant beds — type (DWC, media bed, NFT), area, and what crops?
4. What kind of biofilter do you have and how old is it? Has it ever been crashed or treated with medications?
5. What sensors do you have available? (pH probe, test kits, DO meter, temperature, EC/TDS?)
6. Are you on city water? If so, do you know if they use chlorine or chloramine?
7. Any recent events — new fish, disease treatment, equipment problems, partial water changes?
8. What motivated you to start using this workspace — is there an active problem or are you setting up for routine monitoring?

## Step 3: Document the System
Write the operator's answers into `context/project.md`, filling in the template fields.

## Step 4: Initial Baselines
Based on the fish species identified, pull the appropriate thresholds from `resources/species-profiles.md` and populate the baseline table in `context/project.md` with conservative starting values. Note that these are textbook defaults — run `/baseline` after 7 days of stable readings to get system-specific values.

## Step 5: Quick First Scan (Optional)
Ask: "Do you have a set of current readings you'd like to run through the anomaly scanner right now?"
If yes, proceed to `/scan` workflow.

## Step 6: Orientation
Briefly explain the available commands and what each is for. Point to `README.md` for full reference.

## Completion
Confirm workspace is ready. Remind operator to update `context/role.md` with their experience level and communication preferences.
