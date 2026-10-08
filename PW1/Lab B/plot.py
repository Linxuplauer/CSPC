import numpy as np
import matplotlib.pyplot as plt
LAMBDA = 0.3
# TODO 1
t, observed = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1, unpack=True)
# TODO 2
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)
# TODO 3
fig, (ax_obs, ax_ana) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))
ax_obs.scatter(t, observed, s=15)
ax_obs.set_title("Observed data")
ax_obs.set_xlabel("Time")
ax_obs.set_ylabel("Count")
ax_ana.plot(t, analytical)
ax_ana.set_title("Analytical")
ax_ana.set_xlabel("Time")
ax_ana.set_ylabel("Count")
fig.tight_layout()
# TODO 4
fig.savefig("figure.png", dpi=150)