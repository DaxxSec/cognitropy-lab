# /water-quality — Water Quality Analysis & Anomaly Detection

Analyze water quality data, compare against regulatory thresholds, calculate trophic state, and flag anomalies.

## Procedure

1. Ask the user to provide data in one of these formats:
   - Paste raw data (CSV, table, or list format)
   - Describe the parameters and values verbally
   - Reference a file in the workspace

2. **Data Validation** (Workflow 3, Step 1):
   - Check for impossible values
   - Compare field duplicates (RPD <20%)
   - Verify calibration drift is acceptable
   - Flag any holding time violations

3. **Threshold Comparison** (Workflow 3, Step 2):
   - Compare against EPA National Recommended Water Quality Criteria
   - Apply state-specific standards if user has specified jurisdiction
   - Distinguish acute vs. chronic thresholds
   - Flag recreational water quality exceedances (E. coli, cyanotoxins)

4. **Trophic State Assessment** (Workflow 3, Step 3):
   - Calculate Carlson's TSI for Secchi depth, chlorophyll-a, and total phosphorus
   - Classify trophic state
   - Analyze TSI divergences to identify limiting factors

5. **Anomaly Detection** (Workflow 3, Step 4):
   - Sudden DO crashes
   - Chlorophyll-a spikes
   - Conductivity anomalies
   - pH excursions
   - Temperature inversions
   - Any cyanotoxin detection

6. **Safety Implications** (Workflow 3, Step 6):
   - Flag any water quality results that affect field safety
   - Recommend PPE changes or sampling restrictions as needed
   - If microcystin detected, trigger HAB awareness

7. Generate analysis report and save to `outputs/wq-analysis-[SITE]-[DATE].md`
