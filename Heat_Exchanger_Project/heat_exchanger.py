
import math
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# HEAT EXCHANGER PERFORMANCE ANALYSIS
# Illustrative simulated data
# ==========================================

# 1. Fluid properties and operating conditions
cp_hot = 4180
cp_cold = 4180

m_hot = 1.2
m_cold = 1.0

T_hot_in = 90.0
T_hot_out = 65.0
T_cold_in = 20.0
T_cold_out = 50.0

area = 12.0

# 2. Calculate heat duties
Q_hot = m_hot * cp_hot * (T_hot_in - T_hot_out)
Q_cold = m_cold * cp_cold * (T_cold_out - T_cold_in)
Q_average = (Q_hot + Q_cold) / 2

# 3. Calculate LMTD for countercurrent flow
delta_T1 = T_hot_in - T_cold_out
delta_T2 = T_hot_out - T_cold_in

if delta_T1 <= 0 or delta_T2 <= 0:
    raise ValueError("Invalid terminal temperature differences.")

if math.isclose(delta_T1, delta_T2):
    LMTD = delta_T1
else:
    LMTD = (
        (delta_T1 - delta_T2)
        / math.log(delta_T1 / delta_T2)
    )

# 4. Calculate clean overall heat-transfer coefficient
U_clean = Q_average / (area * LMTD)

# 5. Define illustrative fouling resistance values
# Units: m^2.K/W
fouling_resistances = [0.0, 0.0005, 0.0010, 0.0020]

# 6. Calculate performance for each scenario
results = []

for Rf in fouling_resistances:

    # Added fouling resistance on a consistent area basis
    U_fouled = 1 / ((1 / U_clean) + Rf)

    # Percentage reduction relative to the clean coefficient
    reduction = (U_clean - U_fouled) / U_clean * 100

    results.append({
        "Fouling Resistance (m2.K/W)": Rf,
        "Overall U (W/m2.K)": U_fouled,
        "Reduction in U (%)": reduction
    })

# 7. Create a results table
df = pd.DataFrame(results)

print("\nHEAT EXCHANGER BASELINE")
print("-" * 40)
print(f"Hot-side duty: {Q_hot / 1000:.2f} kW")
print(f"Cold-side duty: {Q_cold / 1000:.2f} kW")
print(f"LMTD: {LMTD:.2f} K")
print(f"Clean overall U: {U_clean:.2f} W/(m2.K)")

print("\nFOULING ANALYSIS")
print(df.round(3).to_string(index=False))

# 8. Save results to CSV
df.to_csv("fouling_results.csv", index=False)
print("\nSaved results to fouling_results.csv")

# 9. Plot overall heat-transfer coefficient

# 9. Plot overall heat-transfer coefficient
plt.figure(figsize=(9, 5.5))

plt.plot(
    df["Fouling Resistance (m2.K/W)"],
    df["Overall U (W/m2.K)"],
    marker="o",
    linewidth=2,
    markersize=7,
    label="Overall heat-transfer coefficient"
)

plt.xlabel("Fouling Resistance (m²·K/W)", fontsize=11)
plt.ylabel("Overall Heat-Transfer Coefficient (W/m²·K)", fontsize=11)

plt.title(
    "Effect of Fouling Resistance on Heat Exchanger Performance",
    fontsize=13
)

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("fouling_analysis.png", dpi=300)
plt.show()

# 10. Plot percentage reduction in U
plt.figure(figsize=(9, 5.5))

plt.plot(
    df["Fouling Resistance (m2.K/W)"],
    df["Reduction in U (%)"],
    marker="o",
    linewidth=2,
    markersize=7,
    label="Reduction in U"
)

plt.xlabel("Fouling Resistance (m²·K/W)", fontsize=11)
plt.ylabel("Reduction in Overall U (%)", fontsize=11)
plt.title("Percentage Loss in Heat-Transfer Performance", fontsize=13)

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("fouling_reduction.png", dpi=300)
plt.show()

print("Saved graph to fouling_reduction.png")


# 11. Generate an automated engineering summary

worst_case = df.loc[df["Reduction in U (%)"].idxmax()]

print("\nENGINEERING SUMMARY")
print("-" * 40)

print(
    f"Clean heat-transfer coefficient: "
    f"{U_clean:.2f} W/(m2.K)"
)

print(
    f"Maximum fouling resistance studied: "
    f"{worst_case['Fouling Resistance (m2.K/W)']:.4f} m2.K/W"
)

print(
    f"Heat-transfer coefficient at this condition: "
    f"{worst_case['Overall U (W/m2.K)']:.2f} W/(m2.K)"
)

print(
    f"Reduction in overall U: "
    f"{worst_case['Reduction in U (%)']:.2f}%"
)

print(
    "\nNote: Results are based on illustrative simulated "
    "conditions, not measured industrial data."
)


