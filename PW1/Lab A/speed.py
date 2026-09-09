import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

t0 = time.perf_counter()
simulate_loop(N0, lam)
loop_time = time.perf_counter() - t0

t0 = time.perf_counter()
simulate(N0, lam)
numpy_time = time.perf_counter() - t0

speedup = loop_time / numpy_time

print(f"Loop time : {loop_time:.4f} s")
print(f"NumPy time: {numpy_time:.4f} s")
print(f"Speed-up  : {speedup:.2f}x faster")
