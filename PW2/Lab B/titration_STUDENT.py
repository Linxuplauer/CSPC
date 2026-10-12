"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read data
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V, pH = data[:, 0], data[:, 1]

# TODO 2: slope and equivalence point
slope = np.gradient(pH, V)
i = np.argmax(slope)
V_eq = V[i]
print(f"Equivalence point: {V_eq:.2f} mL")

# TODO 3: two plots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(V, pH)
ax1.axvline(V_eq, color="r", linestyle=":", label=f"V_eq = {V_eq:.1f} mL")
ax1.set_xlabel("volume of base (mL)")
ax1.set_ylabel("pH")
ax1.legend()

ax2.plot(V, slope)
ax2.axvline(V_eq, color="r", linestyle=":")
ax2.set_xlabel("volume of base (mL)")
ax2.set_ylabel("slope dpH/dV")

plt.tight_layout()
plt.savefig("titration.png")