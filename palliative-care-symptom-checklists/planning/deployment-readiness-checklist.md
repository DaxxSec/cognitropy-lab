# Deployment Readiness Checklist

Work through this list before any real-patient use. All items must be checked.

## Licensing and legal
- [ ] IPOS license registered with Cicely Saunders Institute (if IPOS will be used)
- [ ] All other instrument license terms reviewed and met
- [ ] Instrument versions documented in `resources/instruments.md`

## Privacy and security
- [ ] Workspace deployed inside organization's compliant environment
- [ ] No PHI written to disk (spot check `outputs/` and `work-log/`)
- [ ] No outbound network calls carry PHI
- [ ] Access controls on the deployment environment verified
- [ ] Compliance officer sign-off on PHI handling

## Clinical governance
- [ ] Medical director sign-off on escalation thresholds
- [ ] Nursing lead sign-off on workflow fit
- [ ] Pilot (3 clinicians, 3 fictitious cases) completed
- [ ] Draft-note acceptance rate ≥ 80%
- [ ] Scoring validation: 100% agreement with hand-calculation

## Training and change management
- [ ] Team training session held
- [ ] Quick-reference card produced (one page, per-instrument)
- [ ] Escalation policy distributed (how to act on flags)
- [ ] Feedback channel established (where clinicians report issues)

## Operational
- [ ] Session-log review cadence established (weekly)
- [ ] Threshold re-review cadence established (every 180 days, or sooner if clinical policy changes)
- [ ] Version of this workspace tagged
