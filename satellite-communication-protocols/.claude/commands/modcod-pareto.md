# /modcod-pareto

Build the Pareto frontier over modulation-and-coding choices and pick the cost-benefit-optimal operating point. Climbing the MODCOD table (QPSK → 8PSK → 16/32APSK, lower → higher code rate) buys spectral efficiency but demands more Es/N₀ — the satcom version of opening the aperture for more light while losing depth of field. Adaptive Coding and Modulation (ACM) lets the link **stop down dynamically** as conditions change.

## Inputs

- The DVB-S2X MODCOD table (`context/references.md`): each point's spectral efficiency and required Es/N₀ at the target BER
- The clear-sky and rain-faded Es/N₀ from `/cascade-budget`
- The rain-fade exceedance statistics from `/rain-margin-economics` (how often each Es/N₀ level is available)
- The value model: $/bit or revenue per Mbps, and the cost of an outage minute

## Steps

1. Plot all candidate MODCODs as points: x = required Es/N₀, y = spectral efficiency. The upper-left envelope (most bits/Hz for the least Es/N₀) is the **Pareto frontier**; discard dominated points.
2. Overlay the link's available Es/N₀ distribution (clear-sky down to deep-fade). The highest-efficiency MODCOD whose requirement sits below the available Es/N₀ at a given availability is the feasible operating point there.
3. For a **fixed (CCM)** link: pick the MODCOD that meets the *worst-case* (target-availability) Es/N₀ — conservative, like stopping all the way down for the dimmest scene. Compute its delivered throughput and $/bit.
4. For an **ACM** link: integrate throughput over the Es/N₀ distribution — each condition runs its best feasible MODCOD. Compute the average delivered Mbps and compare $/bit against CCM. ACM's benefit is the area between the staircase and the fixed floor.
5. Recommend the operating point (or ACM ladder) that maximizes value net of cost, and state the spectral-efficiency Strehl it implies for `/shannon-gap`.

## Output

`outputs/links/<mission-id>/modcod-pareto.md` — the frontier plot/table, the chosen CCM point or ACM ladder, delivered throughput and availability, $/bit, and the CCM-vs-ACM verdict.

## Notes

- DVB-S2X with LDPC+BCH operates within ~0.7–1 dB of Shannon at each point — the frontier is dense, so small Es/N₀ shifts can unlock a whole efficiency step. This is why squeezing 0.5 dB out of an aberration can be worth a MODCOD jump.
- ACM almost always beats static margin when fades are infrequent and deep (Ka/Q/V band) — but it needs a return path for CSI feedback and adds scheduler complexity; price that overhead before recommending it.
