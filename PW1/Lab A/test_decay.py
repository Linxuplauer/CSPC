import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    N0, lam, dt, steps = 10000, 0.4, 0.05, 200
    runs = [simulate(N0, lam, dt=dt, steps=steps, seed=s) for s in range(100)]
    avg = np.mean(runs, axis=0)

    t = np.arange(steps + 1) * dt
    expected = N0 * np.exp(-lam * t)

    assert avg == pytest.approx(expected, rel=0.05)