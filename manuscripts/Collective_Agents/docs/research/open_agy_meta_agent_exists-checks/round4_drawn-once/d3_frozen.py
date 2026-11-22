r"""Frozen-feedback null N_fr for the audience P0, exact.

Under N_fr every member keeps its filter (claimed covariances kept, gains of the all-source
filter) but reads the source's broadcast frozen at its round-0 content u_S(0) = eta_0 + v_S(0),
with fresh receiver-specific channel noise each round.  Member error recursion:
  eps(t+1) = M eps(t) + A K[:,0] v_i(t) + A K[:,1] (eta_0 - eta_{t-1} + v_S(0) + nu_i(t)) + xi(t).
Given the world path the eta terms are deterministic.  If v_S(0) is not conditioned on, it is a
static input common to all members; its stationary response is c v_S(0) with
c = [(I - M)^{-1} A K[:,1]]_0.  The source's error does not involve v_S(0) asymptotically, and
no member reads live source data, so S is uncorrelated with the members.

Declared expectations: conditioned on v_S(0), the member covariance is diagonal and r(A) = 1;
unconditioned, the member block is alpha I + beta 11^T with beta = c^2 R_S, so r(A) = 1 + 4 beta/alpha,
expected well above the full model's 5.3849 (the blind P1 computation gave 7.10 for P1).
"""
from __future__ import annotations

import os
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.linalg import solve_discrete_lyapunov

from fixedlib import AF, riccati, contrast

F, Q, R, RS, Rc, qc = 0.9, 0.05, 1.0, 0.01, 0.002, 1e-4
A = AF(F)
H = np.eye(2)
Rm = np.diag([R, RS + Rc])
Pm, Pp = riccati(F, Q, qc, H, Rm)
K = Pp @ H.T @ np.linalg.inv(Rm)
M = A @ Pp @ np.linalg.inv(Pm)
AK = A @ K
W = R * np.outer(AK[:, 0], AK[:, 0]) + Rc * np.outer(AK[:, 1], AK[:, 1]) + qc * np.eye(2)
Spriv = solve_discrete_lyapunov(M, W)
alpha = Spriv[0, 0]
cvec = np.linalg.solve(np.eye(2) - M, AK[:, 1])
c = cvec[0]
beta = c ** 2 * RS
# source block: its own filter, independent of the members under N_fr
HS = np.array([[1.0, 0.0]])
PmS, PpS = riccati(F, Q, qc, HS, np.array([[RS]]))
KS = PpS @ HS.T / RS
MS = A @ PpS @ np.linalg.inv(PmS)
WS = RS * np.outer((A @ KS)[:, 0], (A @ KS)[:, 0]) + qc * np.eye(2)
sS = solve_discrete_lyapunov(MS, WS)[0, 0]
for label, b in (("frozen content conditioned on", 0.0), ("frozen content not conditioned on", beta)):
    Sig = np.zeros((5, 5))
    Sig[0, 0] = sS
    Sig[1:, 1:] = alpha * np.eye(4) + b * np.ones((4, 4))
    Pi = np.linalg.inv(Sig)
    off = Pi[~np.eye(5, dtype=bool)].max()
    rs = Pi.sum(axis=1).min()
    rA = contrast(Pi, [1, 2, 3, 4])
    print(f"N_fr, {label}: member var {alpha + b:.6e}, cov {b:.6e}, corr {b / (alpha + b):.4f};"
          f" max offdiag {off:.3e}, min row sum {rs:.3f}; r(A) = {rA:.4f}")
print(f"closed form 1 + 4 beta/alpha = {1 + 4 * beta / alpha:.4f}; static gain c = {c:.6f}")
