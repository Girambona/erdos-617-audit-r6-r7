"""Independent reimplementation of Sneiderman's coloured-core ladder and recursive edge floors
(Erdos Problem 617; consolidated draft section 3 = r7-r8/main.tex section 2), written from the
manuscript text, not from the author's code.

  p(a, n)        Turan floor: minimum edges of an n-vertex graph with independence number <= a
  thresholds(r)  T_s(r) from equations (8)-(10) of r7-r8/main.tex
  make(r)        returns (T, B) with B(a, m) the recursive lower bound B_r(a, m) of Prop. 2.4
  margins(r)     the margins B_r(r-1-j, r^2-d-jr) - E_{r,d,j} of the margin table

Usage:  python3 ladder.py 7        (prints thresholds, margin table and the r = 7 input floors)
Keep r small (r <= 9); the recursion is memoised but grows quickly with r.
"""
import sys
from functools import lru_cache
from math import comb, inf

def p(a, n):
    q, b = divmod(n, a)
    return a * comb(q, 2) + q * b

def thresholds(r):
    T = {2: 0}
    s = 3
    while True:
        A = (s + 1) * r - 2 * s - T[s - 1] + 1
        Bh = r * s * (s + T[s - 1] - 2) - 2 * (r - 1) * (s - 1)
        if A <= 0:
            break
        v = max(1, Bh // A + 1)
        if v >= r:
            break
        T[s] = v
        s += 1
    return T

def make(r, use_kp_equality=True):
    """use_kp_equality=False drops the '+1' of the third line of Q_r (the only place where the
    Kang-Pikhurko equality characterization enters). Used for Observation 2."""
    T = thresholds(r)
    D = lambda n: comb(n, 2) - (r - 1) * p(r, n)
    def Q(a, n):
        if n <= a * (r - 1):
            return p(a, n)
        if n <= a * r:
            return p(a, n) + n // a - 1
        return p(a, n) + n // a - (0 if use_kp_equality else 1)
    def C(d):
        if d < r - 1:
            return comb(d + 1, 2)
        if d == r - 1:
            return comb(r, 2) + 1
        return d + -(-((r + 2) * comb(d, 2)) // r)
    @lru_cache(None)
    def B(a, n):
        if a == 0:
            return 0 if n == 0 else inf
        if a == 1:
            return comb(n, 2) if n <= r - 1 else inf
        if a in T and n >= a * r + T[a]:
            return inf
        best = inf
        for d in range(0, n):
            sub = B(a - 1, n - 1 - d)
            if sub == inf:
                continue
            best = min(best, max(sub + C(d), -(-(n * d) // 2)))
        if best == inf:
            return inf
        b = max(Q(a, n), best)
        return inf if b > D(n) else b
    return T, B

def margins(r, use_kp_equality=True):
    T, B = make(r, use_kp_equality)
    M = r * (r * r + 1) // 2
    rows = {}
    for d in range(0, r):
        row = []
        for j in range(0, r - 4):
            E = M - d - comb(d, 2) - j * comb(r, 2)
            b = B(r - 1 - j, r * r - d - j * r)
            row.append(inf if b == inf else b - E)
        rows[d] = row
    return T, rows

if __name__ == '__main__':
    for r in map(int, sys.argv[1:] or ['7']):
        T, rows = margins(r)
        print(f"r = {r}: thresholds T_s = {T}")
        print("margins B - E (columns j = 0 .. r-5):")
        for d, row in rows.items():
            print(f"  d = {d}: " + ' '.join('inf' if x == inf else str(x) for x in row))
        if r == 7:
            _, B = make(7)
            for a, m in [(3, 20), (3, 21), (5, 37), (5, 38), (5, 39)]:
                print(f"  P_{a}({m}) >= B_7({a},{m}) = {B(a, m)}")
