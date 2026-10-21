import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("chemicals_cancer.csv")
print(df.shape)
print(df.head())

print("\nNAIVE correlation with malignancy (all patients)")
for chem in ["benzene", "cadmium"]:
    r, p = stats.pearsonr(df[chem], df["malignancy"])
    print(chem, "r =", round(r, 3), " p =", p)

print("\nCorrelation of each variable with pollution_index")
for col in ["benzene", "cadmium", "malignancy"]:
    r, p = stats.pearsonr(df[col], df["pollution_index"])
    print(col, "r =", round(r, 3))

for low, high in [(40, 60), (45, 55)]:
    similar = df[(df["pollution_index"] > low) & (df["pollution_index"] < high)]
    print("\nPollution between", low, "and", high, "-> patients kept:", len(similar))
    for chem in ["benzene", "cadmium"]:
        r, p = stats.pearsonr(similar[chem], similar["malignancy"])
        print("  ", chem, "r =", round(r, 3), " p =", round(p, 4))

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for col, chem in enumerate(["benzene", "cadmium"]):
    axes[0, col].scatter(df[chem], df["malignancy"], alpha=0.4, s=10)
    axes[0, col].set_title(chem + ": all patients")
    axes[1, col].scatter(similar[chem], similar["malignancy"], alpha=0.5, s=10)
    axes[1, col].set_title(chem + ": pollution 45-55 only")
    axes[1, col].set_xlabel(chem)
    axes[0, col].set_ylabel("malignancy")
    axes[1, col].set_ylabel("malignancy")
plt.tight_layout()
plt.savefig("chemicals.png", dpi=150)