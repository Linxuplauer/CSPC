"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: imbalance function (zero at equilibrium)
def k_imbalance(x):
    return (2*x)**2 / ((a-x)*(b-x)) - K

# TODO 2: method 1, Newton (root-finding)
x_newton = newton(k_imbalance, 0.5)

# TODO 3: method 2, SLSQP (minimize imbalance^2)
res = minimize(lambda x: k_imbalance(x[0])**2, [0.5],
               method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]

print("Newton:", x_newton)
print("SLSQP :", x_slsqp)

# TODO 4: amounts and plot
x_eq = x_newton
print(f"H2 = {a-x_eq:.3f}, I2 = {b-x_eq:.3f}, HI = {2*x_eq:.3f}")

xs = np.linspace(0, 0.99, 200)
plt.plot(xs, a-xs, label="H2")
plt.plot(xs, b-xs, "--", label="I2")
plt.plot(xs, 2*xs, label="HI")
plt.axvline(x_eq, color="k", linestyle=":", label=f"equilibrium x={x_eq:.3f}")
plt.xlabel("extent x (mol)")
plt.ylabel("amount (mol)")
plt.legend()
plt.savefig("equilibrium.png")