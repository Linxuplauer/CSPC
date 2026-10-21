# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
```

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- I created a repository with a working conda environment.
- I added a Python simulation of radioactive decay, with tests for it.
- I wrote a script that compares the speed of two methods.

**Speed comparison (loop vs NumPy):**
- loop : 0.284 s
- numpy : 0.003 s
- speed-up: 94.67 x faster

**Tests:** yes, all 3 tests pass (`pytest -v`: starts at N0, rejects a negative rate, matches the exponential law).

**Conclusion:**
- In this lab, I learned how to use Git commands in the terminal to commit, make branches, and push my code to GitHub. Creating the conda environment with environment.yml was easy and helped run everything without problems. I also saw that using NumPy is much faster than standard Python loops for heavy simulation tasks.

---

## PW1 - Lab B: Data, Plotting, and Automation

**What I built:**
- `plot.py` reads `decay_observed.csv`, computes the analytical law N0 * exp(-lambda * t) with lambda = 0.3 and N0 = the first observed count, and draws a 1x2 figure with shared axes (observed points on the left, analytical curve on the right), saved as `figure.png`.
- A `Snakefile` with one rule that builds `figure.png` from the CSV by running `plot.py`.

**What the data showed:**
- The observed counts decrease with time and follow the analytical curve closely, with some random noise.

**Snakemake:**
- The pipeline builds `figure.png` from `decay_observed.csv`. When I ran it again with nothing changed, Snakemake reported "Nothing to be done" and did no work.

---

## PW2 - Lab A: Motion from Tracking Data

- **Mean acceleration:** -8.58 m/s² (std 28.7 m/s²), roughly consistent with -g = -9.81 m/s².
- **Why noisy:** Differentiation divides small differences between noisy neighbouring measurements by a small time step (0.1 s), which amplifies the noise, and acceleration needs two derivatives.
- **Integrating back:** Integrating the noisy acceleration twice recovered the position to within 0.78 m, because integration sums values and the random noise largely cancels out.

---

## PW2 - Lab B: Optimization in Chemistry

### Part 2: Optimization methods
- On the easy convex function f(x) = (x-3)^2 + 1, gradient descent, Newton and SLSQP all reach x = 3.
- On g(x) = x^4 - 3x^2 + x + 5 the methods do not always agree.
- From x0 = 0, Newton landed on x = 0.17, which is a maximum (g'' < 0), while gradient descent and SLSQP reached the global minimum at x = -1.30.
- From x0 = 2, all three methods reached the local minimum at x = 1.13.
- Lesson: on a complicated landscape the starting point and the algorithm matter. Newton finds stationary points, not necessarily minima.

### Part 3: Reaction rate
- Fitted rate constant: k = 0.262 (close to the expected 0.25; the data is noisy). Plot: kinetics.png

### Part 4: Equilibrium (H2 + I2 <=> 2 HI, K = 15.6)
- Newton and SLSQP agree: x = 0.664.
- Equilibrium amounts: H2 = 0.336 mol, I2 = 0.336 mol, HI = 1.328 mol. Plot: equilibrium.png

### Part 5 (bonus): Titration
- Equivalence point at 50.00 mL, where the slope of the pH curve is largest. Plot: titration.png

---

## PW3: Data, Distributions, Testing, and Causation

### What I learned

- I learned to use **pandas**: loading a CSV into a DataFrame, filtering rows
  with a condition, and summarising columns with `describe()`.
- I learned to use **matplotlib (`plt`)**: histograms, Q-Q plots, error-bar
  plots and scatter plots.
- I learned about the **pollution index** and how a hidden third variable can
  make a harmless variable look guilty.

### Data

- Heart data: UCI Heart Disease (Cleveland), from Kaggle
  (https://www.kaggle.com/datasets/ritwikb3/heart-disease-cleveland).
  303 patients, 14 columns, no missing values.
- Chemicals data: synthetic, 1000 patients (benzene, cadmium, pollution_index,
  age, malignancy).

Scripts: `session1.py`, `session2.py`, `dataset2.py`.

### Session 1: Distributions and normality

![distributions](PW3/distributions.png)
![qqplots](PW3/qqplots.png)

I checked normality in two ways: graphically (histograms and Q-Q plots) and
numerically (skewness, kurtosis and the Shapiro-Wilk test). All four Shapiro
p-values are below 0.05, but with 303 patients this test reacts even to small
deviations, so I also used the plots and the skewness.

| variable | skew | kurtosis | Shapiro p | verdict |
|---|---|---|---|---|
| age | -0.21 | -0.53 | 0.0061 | approximately normal |
| chol | 1.13 | 4.40 | 0.0000 | not normal |
| trestbps | 0.70 | 0.85 | 0.0000 | not normal |
| thalach | -0.53 | -0.07 | 0.0001 | not normal (mildly) |

- **age:** Almost symmetric (skew -0.21) and the Q-Q dots stay close to the
  line. The small p-value comes from a slightly flat top (kurtosis -0.53).
- **chol:** Strong right skew (1.13) and heavy tail (kurtosis 4.40). The Q-Q
  plot shoots above the line at the top because of an outlier near 560.
- **trestbps:** Right skew (0.70). The values are rounded (120, 130, 140), so
  the Q-Q plot looks like steps, and the upper end bends above the line.
- **thalach:** Left tail (skew -0.53): a few patients reach only 70 to 100.
  The middle of the Q-Q plot is straight, so it is only mildly non-normal.
  I still treat it as not normal, which decides the test in Session 2.

### Session 2: Heart rate in disease vs healthy

I split `thalach` into patients with disease (n = 139) and healthy patients
(n = 164). Because `thalach` is not normal (Session 1), I used the
**Mann-Whitney U test**, which does not assume a normal shape. As a check I
also ran a Welch t-test.

- Mann-Whitney: U = 5806.5, p = 1.9e-13
- Welch t-test: t = -7.86, p = 9.1e-14

**Conclusion:** the groups really differ. Patients with heart disease reach a
lower maximum heart rate.

| group | mean thalach | SEM | 95% CI |
|---|---|---|---|
| disease | 139.3 | 1.92 | +/- 3.8 |
| healthy | 158.4 | 1.50 | +/- 2.9 |

![means](PW3/thalach_means.png)

The error bars do not overlap, so the plot agrees with the test.

### Age and heart rate

Pearson r = -0.394 and Spearman rho = -0.392 (both p < 1e-11).

![age vs thalach](PW3/age_vs_thalach.png)

Older patients tend to reach a lower maximum heart rate. The relationship is
moderate, with a lot of scatter around the line. This shows that the variables
move together, not that age is the only cause.

### Dataset 2: The chemical mystery

**Naive analysis (all 1000 patients).** Correlation with malignancy:
benzene r = 0.385, cadmium r = 0.880. At face value, cadmium looks like the
cause.

**Looking again.** I checked the correlation of each variable with
`pollution_index`: cadmium r = 0.982, benzene r = 0.054, malignancy r = 0.895.
So cadmium almost follows the pollution, and pollution is strongly linked to
malignancy. Pollution could be a third variable behind the cadmium result.

**Test.** I kept only patients with similar pollution and recomputed the
correlations with malignancy:

| patients kept | n | benzene r | cadmium r |
|---|---|---|---|
| all (naive) | 1000 | 0.385 | 0.880 |
| pollution 40 to 60 | 199 | 0.702 | 0.316 |
| pollution 45 to 55 | 94 | 0.658 | -0.04 (p = 0.70) |

![chemicals](PW3/chemicals.png)

**Conclusion.** **Benzene is the real cause of malignancy.** When pollution is
held roughly constant, the benzene association stays strong while the cadmium
association disappears. Cadmium only looked guilty because it rises together
with pollution, and pollution itself raises malignancy (a confounding
variable). In the 40 to 60 window, cadmium is still 0.32 because pollution
still varies inside that window and cadmium follows it. In the narrower
45 to 55 window this effect is gone.
