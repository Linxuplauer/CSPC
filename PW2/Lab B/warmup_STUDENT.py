"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A
x0 = 0.0
x = x0  
for _ in range(1000):
    x = x - 0.1 * df(x)
print("GD:", x)
print("Newton:", newton(df, x0, fprime=d2f))
print("SLSQP:", minimize(f, x0, method="SLSQP").x[0])

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: 
for x0 in [0.0, 2.0]:
    x = x0
    for _ in range(5000):
        x = x - 0.01 * dg(x)
    xn = newton(dg, x0, fprime=d2g)
    xs = minimize(g, x0, method="SLSQP").x[0]
    print(f"x0={x0}: GD={x:.3f}  Newton={xn:.3f} (g''={d2g(xn):.2f})  SLSQP={xs:.3f}")