# /build-vs-buy-stack

Evaluate commercial vs open-source vs in-house for a stack component (BLE, filesystem, TLS, GUI, RTOS) on true total cost of ownership — with the software license treated as a real cost, not a footnote.

## Inputs

- The component's requirements and the certification/security bar it must clear
- Candidate options: commercial (license terms), open-source (license + upstream health), in-house (effort estimate)
- Expected production volume and product lifetime

## Steps

1. Define the **hard bar** (e.g. certified BLE stack, FIPS crypto) — options that can't meet it are out regardless of price.
2. Cost **buy**: per-unit or one-time license, integration hours, support contract, redistribution terms.
3. Cost **open-source**: integration + maintenance hours, **license obligation** (GPL copyleft vs MIT/BSD/Apache permissive), upstream activity.
4. Cost **in-house**: engineering months + ongoing maintenance + the risk it misses a hard requirement.
5. Compare **TCO over the product's life at the real volume**; record the decision and the license terms explicitly.

## Output

`outputs/projects/<name>/build-vs-buy-<component>.md` — the TCO comparison, the license analysis, the recommendation, and the obligations the team is accepting.

## Notes

- A GPL component in a closed-source product is a "can't ship as-is" cost — surface it; don't let "free" hide the obligation.
- For crypto/radio/safety components, bias toward **proven/certified**; rolling your own is rarely cheapest once risk is priced.
