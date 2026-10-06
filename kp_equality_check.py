"""Observation 2: at r = 7 the Kang-Pikhurko equality characterization is not load-bearing.
Recomputes every B_7(a, m) (a <= 6, m <= 49) and the margin table with and without the '+1'
of the third line of Q_r, and reports any difference.   Usage: python3 kp_equality_check.py"""
from ladder import make, margins

r = 7
_, B1 = make(r, True)
_, B0 = make(r, False)
diff = [(a, m, B1(a, m), B0(a, m)) for a in range(2, r) for m in range(0, r * r + 1) if B1(a, m) != B0(a, m)]
print(f"B_7(a, m) values that change (a <= 6, m <= 49): {diff if diff else 'none'}")
print("margin table identical:", margins(r, True) == margins(r, False))
print("input floors without equality case:", [B0(a, m) for a, m in [(3, 20), (3, 21), (5, 37), (5, 38), (5, 39)]])
