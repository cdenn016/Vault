r"""Scope follow-up for C3c: a non-acting agent d that reads members of U1 only (and senses eta).
Declared expectation (reconstruction): the U1-U2 block of the POPULATION precision is
kappa bhat_1 bhat_2^T + L_1^T R^{-1} L_2 with L_2 parallel to bhat_2 (group 2 sees group 1 only
through bhat_2), so the block stays rank one, v bhat_2^T, but its left factor v is no longer
parallel to bhat_1 and can have entries of either sign.
Control: d reads nobody (pure sensor): v parallel to bhat_1, all entries positive.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
exec(open("c3c_eigen.py").read().split("e1_rank = e1_kappa = 0.0")[0])
for mode in ["reads U1 only (positive weights)", "reads U1 only (mixed-sign weights)", "pure sensor"]:
    worst = 0.0; dev = 0.0; neg = 0; used = 0
    while used < 60:
        g1 = eigen_group(3); g2 = eigen_group(3)
        A = np.zeros((7, 7)); A[:3, :3] = g1[0]; A[3:6, 3:6] = g2[0]; A[6, 6] = rng.uniform(0, 0.8)
        if mode.startswith("reads U1 only (positive"):
            A[6, 0] = rng.exponential(1.5); A[6, 1] = rng.exponential(0.2)
        elif mode.startswith("reads U1 only (mixed"):
            A[6, 0] = rng.exponential(1.5); A[6, 1] = -rng.exponential(1.5)
        Q = blockdiag(g1[1], g2[1], np.array([[rng.exponential(0.5) + 0.05]]))
        mags = rng.exponential(0.6, 2) + 0.1
        b = np.concatenate([mags[0] * g1[2], mags[1] * g2[2], [0.0]])
        k = rng.standard_normal(7) * 0.3
        F, q = rng.uniform(-0.9, 0.9), rng.exponential(0.5) + 0.05
        S = direct_conditional(A, k, b, F, Q, q)
        if S is None:
            continue
        used += 1
        blk = np.linalg.inv(S)[:3, 3:6]
        U, s, Vt = np.linalg.svd(blk)
        worst = max(worst, s[1] / s[0])
        dev = max(dev, 1 - abs(U[:, 0] @ g1[2]))
        neg += int(np.min(blk) < 0)
    print(f"{mode}: max sigma2/sigma1 {worst:.2e}; max 1-|<left factor, bhat_1>| {dev:.2e}; draws with a negative cross entry {neg}/{used}")
