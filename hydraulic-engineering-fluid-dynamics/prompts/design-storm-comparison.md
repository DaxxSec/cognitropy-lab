# Design Storm Comparison — Deterministic vs. Probabilistic

Use this prompt to compare traditional deterministic design storm analysis against probabilistic alternatives for a specific infrastructure element.

## Prompt

I need to size [describe infrastructure: culvert, detention basin, pipe segment, spillway] for the following conditions:
- Location: [city, state or coordinates]
- Contributing drainage area: [acres or km²]
- Current design standard: [e.g., 25-year/24-hour storm, 100-year peak flow]
- Available data: [gauge record length, Atlas 14 availability]

Please:
1. Run the traditional deterministic design calculation using the standard design storm
2. Perform a Bayesian flood frequency analysis to estimate the design flow with uncertainty
3. Compare the two approaches: how different are the design sizes?
4. Calculate the implied reliability of the deterministic design (what's the actual probability of exceedance given parameter uncertainty?)
5. Recommend whether the probabilistic approach changes the design decision
6. Quantify the cost difference if the probabilistic approach suggests a different size
