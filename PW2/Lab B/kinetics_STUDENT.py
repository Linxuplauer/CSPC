"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read data
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t, C = data[:, 0], data[:, 1]
C0 = C[0]

# TODO 2: total error
def total_error(k):
    return np.sum((C - C0 * np.exp(-k[0] * t))**2)

# TODO 3: minimise
res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print("Fitted k:", k_fit)

# TODO 4: plot
plt.plot(t, C, "o", label="data")
plt.plot(t, C0 * np.exp(-k_fit * t), "-", label=f"fit, k={k_fit:.3f}")
plt.xlabel("time")
plt.ylabel("concentration")
plt.legend()
plt.savefig("kinetics.png")