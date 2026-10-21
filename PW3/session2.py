# PW3 - Session 2 (heart data): compare groups, uncertainty, correlation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")
df = df.rename(columns={"condition": "target"})

# ------------------------------------------------------------
# TASK 4a: do disease patients reach a different max heart rate?
# ------------------------------------------------------------
disease = df[df["target"] == 1]["thalach"]    # group 1: heart disease
healthy = df[df["target"] == 0]["thalach"]    # group 0: healthy

print("n disease:", len(disease), " n healthy:", len(healthy))

# Session 1: thalach is NOT normal -> use Mann-Whitney U
U, p_mw = stats.mannwhitneyu(disease, healthy)
print("Mann-Whitney U =", U, " p-value =", p_mw)

# Cross-check with Welch t-test
t, p_t = stats.ttest_ind(disease, healthy, equal_var=False)
print("Welch t =", round(t, 2), " p-value =", p_t)

# ------------------------------------------------------------
# TASK 4b: mean +/- uncertainty on the mean
# ------------------------------------------------------------
means, sems = [], []
for name, g in [("disease", disease), ("healthy", healthy)]:
    m = g.mean()
    sem = g.std(ddof=1) / np.sqrt(len(g))     # standard error of the mean
    means.append(m)
    sems.append(sem)
    print(name, "mean =", round(m, 1), " SEM =", round(sem, 2),
          " 95% CI = +/-", round(1.96 * sem, 1))

plt.figure(figsize=(5, 5))
plt.errorbar(["disease", "healthy"], means, yerr=[1.96 * s for s in sems],
             fmt="o", capsize=8, markersize=8)
plt.ylabel("mean max heart rate (thalach)")
plt.title("Mean thalach with 95% confidence interval")
plt.tight_layout()
plt.savefig("thalach_means.png", dpi=150)

# ------------------------------------------------------------
# TASK 5: do age and thalach move together?
# ------------------------------------------------------------
r, p_r = stats.pearsonr(df["age"], df["thalach"])
rho, p_rho = stats.spearmanr(df["age"], df["thalach"])
print("Pearson r =", round(r, 3), " p =", p_r)
print("Spearman rho =", round(rho, 3), " p =", p_rho)

plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6)
slope, intercept = np.polyfit(df["age"], df["thalach"], 1)   # best straight line
x = np.array([df["age"].min(), df["age"].max()])
plt.plot(x, slope * x + intercept, color="red")
plt.xlabel("age")
plt.ylabel("max heart rate (thalach)")
plt.title("age vs thalach")
plt.tight_layout()
plt.savefig("age_vs_thalach.png", dpi=150)
