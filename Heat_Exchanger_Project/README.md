
# Heat Exchanger Performance Analysis Under Fouling Conditions

## Project Overview
This project investigates the effect of fouling resistance on the overall heat-transfer coefficient of a shell-and-tube heat exchanger using Python.

The project uses illustrative simulated operating conditions to demonstrate basic heat-transfer calculations and fouling-resistance analysis.

## Objectives
- Calculate hot-side and cold-side heat duties.
- Calculate the log mean temperature difference (LMTD).
- Estimate the clean overall heat-transfer coefficient.
- Evaluate the effect of fouling resistance on the overall heat-transfer coefficient.
- Visualize results using Python graphs.

## Tools and Libraries
- Python
- Pandas
- Matplotlib
- Engineering calculations based on heat-transfer principles

## Methodology
1. Define fluid properties and operating temperatures.
2. Calculate heat duties and LMTD.
3. Estimate the clean overall heat-transfer coefficient.
4. Apply additional fouling resistance using:

   1/U_f = 1/U_clean + R_f

5. Calculate the percentage reduction in the overall heat-transfer coefficient.
6. Export results to CSV and generate graphs.

## Main Results
The illustrative model estimates a reduction in the overall heat-transfer coefficient from approximately 246.17 to 164.95 W/(m²·K) at a fouling resistance of 0.002 m²·K/W.

This corresponds to a reduction of approximately 32.99%.

## Files
- `heat_exchanger.py` — Python source code
- `fouling_results.csv` — calculated results
- `fouling_analysis.png` — heat-transfer coefficient graph
- `fouling_reduction.png` — percentage reduction graph

## Limitations
The operating conditions and fouling-resistance values are illustrative assumptions, not measured industrial data. The model estimates the effect of added thermal resistance on the overall heat-transfer coefficient; it does not independently predict fouled outlet temperatures or actual plant energy savings.

## Future Improvements
- Validate the model against experimental or published industrial data.
- Include heat exchanger geometry and detailed thermal-resistance calculations.
- Extend the model to predict outlet temperatures under fouled operating conditions.


