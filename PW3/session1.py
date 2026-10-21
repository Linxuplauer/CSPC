import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")
df = df.rename(columns={"condition": "target"})
print(df.shape)
print(df.head())

cols = ["age", "chol", "trestbps", "thalach"]
X = df[cols]
print(X.describe())

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, c in zip(axes.flat, cols):
    ax.hist(X[c], bins=20, edgecolor="black")
    ax.set_title(c)
    ax.set_xlabel(c)
    ax.set_ylabel("number of patients")
plt.tight_layout()
plt.savefig("distributions.png", dpi=150)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, c in zip(axes.flat, cols):
    stats.probplot(X[c], dist="norm", plot=ax)
    ax.set_title(f"Q-Q plot: {c}")
plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)

print(f"\n{'var':10s} {'skew':>7s} {'kurt':>7s} {'Shapiro W':>10s} {'p-value':>10s}")
for c in cols:
    W, p = stats.shapiro(X[c])
    print(f"{c:10s} {stats.skew(X[c]):7.2f} {stats.kurtosis(X[c]):7.2f} {W:10.3f} {p:10.4f}")