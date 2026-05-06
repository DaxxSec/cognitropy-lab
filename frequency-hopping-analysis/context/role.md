# Your Role

> Populated by `/onboard`. Until then, this is a prompt for the user, not a description of the agent.

## RF Background

- Years of SDR experience
- Have you previously dehopped a hopping signal? With what tool (gr-bluetooth, custom scripts, URH, ubertooth)?
- Comfort with channelisation, polyphase filterbanks, instantaneous-frequency analysis

## Bayesian / Statistical Background

- Comfort with conjugate priors, posterior predictives, MCMC
- PyMC, Stan, NumPyro experience
- Comfort with HMM / Viterbi inference (the dehopper is a hidden-state HMM)

## Domain

- Why do you care about this hopping signal?  (Research / authorised pen-test / coursework / hobby identification)
- Public-band interest (Bluetooth, IoT, ISM) vs. authorised-range tactical work

## Output Preferences

- Do you need plots saved to `outputs/` or only numeric posteriors?
- Reproducibility: SigMF metadata for every capture? Pickle-checkpointed posteriors?
- Reporting style: terse engineer (numbers + CIs), narrative writeup, or court-admissible chain-of-custody?
