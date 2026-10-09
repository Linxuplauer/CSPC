
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
