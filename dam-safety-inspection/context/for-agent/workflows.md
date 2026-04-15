# Workflows

## Workflow 1: Pre-Inspection Preparation

### Trigger
User needs to prepare for an upcoming dam inspection.

### Steps
1. **Gather Dam Profile**: Ask for dam name, type, height, length, year built, hazard classification, regulatory jurisdiction, and spillway type.
2. **Identify Dam Type**: Select appropriate inspection protocol (embankment vs. concrete vs. other).
3. **Review Prior Findings**: Ask if previous inspection reports or known deficiencies exist.
4. **Generate Checklist**: Produce dam-type-specific inspection checklist covering all structural features.
5. **Prepare Data Request**: List the instrumentation data needed for pre-inspection trend review.
6. **Compile Package**: Assemble checklist, data request, and any reference materials into an inspection preparation package.

## Workflow 2: Instrumentation Data Analysis

### Trigger
User provides CSV or tabular instrumentation data for analysis.

### Steps
1. **Data Ingestion**: Parse the provided data; identify instrument types, measurement units, and time range.
2. **Quality Check**: Screen for missing values, stuck readings, out-of-range values, timestamp gaps.
3. **Establish Baselines**: Calculate historical statistics (mean, σ, percentiles) for each instrument.
4. **Seasonal Adjustment**: If reservoir level or temperature data is available, compute correlation and regress out expected seasonal behavior.
5. **Anomaly Screening**: Apply statistical methods (Z-score, CUSUM, trend analysis) to the adjusted data.
6. **Threshold Check**: Compare current readings against action/alert/failure thresholds if defined.
7. **Cross-Reference**: Check if anomalies correlate across related instruments (e.g., multiple piezometers in same zone).
8. **Classify Findings**: Rate each anomaly by severity and confidence.
9. **Generate Report**: Produce an anomaly analysis report with findings, visualizations, and recommended actions.

## Workflow 3: Condition Assessment Reporting

### Trigger
User has completed an inspection and needs to produce a formal condition assessment report.

### Steps
1. **Collect Findings**: Gather visual inspection observations, photographs (descriptions), and instrumentation data.
2. **Organize by Feature**: Sort findings into dam structural features (crest, slopes, spillway, outlet, abutments, toe, instrumentation).
3. **Rate Each Feature**: Assign condition ratings using FEMA standard scale.
4. **Screen Failure Modes**: For each deficiency, identify which potential failure modes it relates to.
5. **Develop Recommendations**: Prioritize recommendations by urgency and safety significance.
6. **Draft Report**: Produce a structured condition assessment following the standard template.
7. **Review Checklist**: Verify report completeness against regulatory requirements.

## Workflow 4: Emergency Action Plan Review

### Trigger
User needs to review or update a dam's Emergency Action Plan.

### Steps
1. **EAP Components Check**: Verify the plan includes all required sections (notification flowchart, inundation maps, responsible personnel, evacuation zones).
2. **Contact Verification**: Flag any contact information that should be verified as current.
3. **Scenario Coverage**: Check that the plan addresses both sunny-day (e.g., piping) and flood-induced failure scenarios.
4. **Notification Timing**: Evaluate whether notification procedures allow adequate warning time based on dam breach wave travel time.
5. **Gap Analysis**: Identify missing or inadequate elements.
6. **Recommendations**: Produce prioritized list of EAP improvements needed.

## Workflow 5: Post-Event Rapid Assessment

### Trigger
A significant event has occurred (earthquake, extreme flood, severe storm) and the dam needs rapid evaluation.

### Steps
1. **Event Characterization**: Determine event type, magnitude, and proximity to the dam.
2. **Screening Criteria**: Compare event parameters against dam design assumptions (e.g., PGA vs. design earthquake, flood peak vs. spillway capacity).
3. **Immediate Data Pull**: Identify which instrumentation data to prioritize reviewing.
4. **Rapid Analysis**: Run anomaly detection focused on pre-event vs. post-event comparison.
5. **Safety Assessment**: Classify the situation as: (a) no concern, (b) increased monitoring recommended, (c) special inspection required, or (d) emergency response required.
6. **Documentation**: Generate a rapid assessment memo suitable for regulatory notification if required.
