
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
```
```

# PW1 - Lab A: Reproducible Foundations

 ==============What I built:
 i created a repository with a working conda environment.
 i add a Python simulation for radioactive decay and test for it.
 I write a script to compare the speed of two methods.

==============Speed comparison (loop vs NumPy):
-loop : 0.284 s
-numpy : 0.003 s
  -speed-up: 94.67 x faster

=============Tests: all passing?
 - Some problems but it was ok
 - 
===============Conclusion:

-In this lab, I learned how to use Git commands in the terminal to commit, make branches, and push my code to GitHub. Creating the conda environment with environment.yml was easy and helped run everything without problems. I also saw that using NumPy is much faster than standard Python loops for heavy simulation tasks.

## PW2 — Lab A

- **Mean acceleration:** -8.58 m/s² (std 28.7 m/s²), roughly consistent with -g = -9.81 m/s².
- **Why noisy:** Differentiation divides small differences between noisy neighbouring measurements by a small time step (0.1 s), which amplifies the noise, and acceleration needs two derivatives.
- **Integrating back:** Integrating the noisy acceleration twice recovered the position to within 0.78 m, because integration sums values and the random noise largely cancels out.

-HP-ProBook-4-G1i-16-inch-Notebook-AI-PC:~/CSPC/PW2/Lab B$ python titration_STUDENT.py
Equivalence point: 50.00 mL
(cspc) ilkin@ilkin-HP-ProBook-4-G1i-16-inch-Notebook-AI-PC:~/CSPC/PW2/Lab B$ 





## PW2 --- Lab B

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