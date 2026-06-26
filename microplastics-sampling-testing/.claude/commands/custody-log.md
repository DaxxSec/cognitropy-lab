# /custody-log

Open or append a tamper-evident chain-of-custody record. Borrowed directly from evidence handling: every sample is sealed, signed, and logged at each transfer so its result is defensible if it ever reaches a regulator or a courtroom.

## Inputs

- Sample ID (from the deployment plan).
- Event type: `collect`, `transfer`, `store`, `subsample`, `analyze`, `archive`, `dispose`.
- Actor (collector/handler), timestamp, location.
- For `collect`: seal ID, container type (glass/metal only — note any unavoidable plastic and why), matrix, volume/mass, in-situ conditions.
- For `transfer`/`store`: from→to custodian, storage condition (e.g. 4 °C dark, frozen), new seal ID if resealed.

## Steps

1. If no record exists for the Sample ID, create one with the `collect` event as the root; otherwise append.
2. Validate the custody chain is **unbroken**: each new event's "from" custodian must equal the previous event's holder, and timestamps must be monotonic. Flag any gap or backdated entry loudly — a broken chain downgrades the sample to *research-only, not defensible*.
3. Record the **seal state** at every transfer (intact / broken / reapplied). A broken seal between collection and analysis is a custody failure; note it rather than hiding it.
4. Log storage conditions and elapsed holding time; flag if holding time exceeds the method's limit (some matrices degrade, biofilms grow, fibers settle).
5. On `analyze`/`subsample`, link the custody record to the run ID used by `/screen-sample` and `/polymer-id` so the result traces back to an intact chain.

## Output

A custody record under `outputs/custody/<sample-id>.md`: append-only event log (timestamp, actor, event, from→to, seal state, conditions), a chain-integrity verdict (intact / broken-at-step-N), and the holding-time check. Never edit prior events — corrections are new events.
