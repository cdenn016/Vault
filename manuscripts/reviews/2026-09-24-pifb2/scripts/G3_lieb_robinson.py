r"""G3: effective light cone of first-order (parabolic-type) linear dynamics on a bounded-degree graph.

Context: PIFB2.tex:1980 says the finite-speed postulate is in tension with first-order
natural-gradient dynamics "whose naive continuum limit is parabolic with infinite signal
speed". L15-2 proposes citing Lieb-Robinson (1972). That paper treats quantum spin
systems; the classical analog for first-order linear dynamics on a graph is elementary:
for L a graph Laplacian with maximal degree Delta,

    |(e^{tL})_{xy}| <= sum_{k >= d(x,y)} (2 Delta t)^k / k!  <=  e^{2 Delta t} (2 Delta t)^d / d!,

because (L^k)_{xy} = 0 for k < d(x,y) and ||L||_inf <= 2 Delta. Hence responses outside the
cone d > e * 2 Delta * t are super-exponentially suppressed: an effective finite speed
exists on any finite-degree agent graph; the infinite speed is a continuum-limit feature.

This script checks the bound on a 1D chain (Delta = 2) for a few (t, d).
"""
from __future__ import annotations

import math

import numpy as np
from scipy.linalg import expm


def main() -> None:
    n = 81
    L = np.zeros((n, n))
    for i in range(n - 1):
        L[i, i + 1] = L[i + 1, i] = 1.0
    L -= np.diag(L.sum(1))  # graph Laplacian (negative semidefinite convention: dq/dt = L q)
    Delta = 2
    x0 = n // 2
    worst = 0.0
    for t in (0.5, 1.0, 2.0, 4.0):
        K = expm(t * L)
        row = []
        for d in (2, 5, 10, 20, 30):
            val = abs(K[x0, x0 + d])
            a = 2 * Delta * t
            tail = sum(math.exp(k * math.log(a) - math.lgamma(k + 1)) for k in range(d, d + 150))
            worst = max(worst, val / tail)
            row.append(f"d={d}: {val:.2e} <= {tail:.2e}")
        print(f"t={t}: " + "; ".join(row))
    print(f"max ratio actual/bound = {worst:.3e} (must be <= 1)")


if __name__ == "__main__":
    main()
