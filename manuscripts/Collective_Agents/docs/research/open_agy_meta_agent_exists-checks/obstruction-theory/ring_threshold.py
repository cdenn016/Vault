"""Lazy-ring consensus output Y = W X + delta, Sigma_X = I, delta ~ N(0, tau I):
smallest tau* such that Pi_Y = (W^2 + tau I)^{-1} is diffusive for all tau >= tau* (scan), n = 3..10.
EXPECTED: n=3 -> tau* = 0 (W exchangeable, invertible); n=4 -> tau* = 1/2 (closed form)."""
import numpy as np
from common import is_diffusive
def lazy_ring(n, w=0.25):
    W = (1 - 2 * w) * np.eye(n)
    for i in range(n):
        W[i, (i + 1) % n] += w; W[i, (i - 1) % n] += w
    return W
taus = np.concatenate([[1e-9], np.logspace(-6, 1, 1401)])
for n in range(3, 11):
    W = lazy_ring(n)
    ok = [all(is_diffusive(np.linalg.inv(W @ W + t * np.eye(n)))[:2]) for t in taus]
    # tau* = smallest grid tau from which all larger grid taus are diffusive
    idx = len(ok)
    for i in range(len(ok) - 1, -1, -1):
        if ok[i]: idx = i
        else: break
    ts = taus[idx] if idx < len(ok) else np.inf
    print(f"n={n:2d}: min|eig W|={np.abs(np.linalg.eigvalsh(W)).min():.4f}, diffusive at tau=1e-9: {ok[0]}, tau* ~ {ts:.4g}")
