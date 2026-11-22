r"""Check 6: worst per-step closure defect over relay-count sequences, for the scalar collective average (P1) that
repairs the declaration clause, and for the constructor's R^2 average (P2).  Reading R-mem: alpha_M must bound d_M,
and d_M <= d_cl per step, so a sup of d_cl over reachable sequences below alpha_M = 0.02 suffices.

Searches (members' P^- propagated exactly along each sequence, Sigma = Cov(x | blanket path) from the stationary
symmetric state): (a) X sustained 30 rounds then Y, X over the 35 sorted relay-count vectors, Y over all 256, open
counts 0, 2, 4; (b) X/Y alternating for 20 rounds, open count 0; (c) 1500 random sequences of 30 rounds (relay
counts uniform on 0..3, open count uniform on 0..4).
Declared expectations (before running): P2 sup about 1e-2 (constructor 1.0e-2); P1 sup between 1.35e-2 (single-
round worst, check 3) and 0.02.  If P1 exceeds 0.02 somewhere, the repaired declaration needs alpha_M above 0.02
under the sup reading (not under the stationary reading, where d_M(P1) is about 1e-4).
NEGATIVE CONTROL: the all-symmetric sequence (3,3,3,3) must give P2 = 0 and P1 equal to check 3's 2.7e-3 level.
"""
import time
import itertools
import numpy as np
from core import Par

t0 = time.time()
PAR = Par()
n, F = 4, PAR.F
AF = np.array([[F, 0.0], [1.0, 0.0]])
P1 = np.zeros((1, 8)); P1[0, 0::2] = 0.25
P2 = np.kron(np.ones((1, n)) / n, np.eye(2))
QW = np.diag([PAR.Q, 0.0]) + PAR.qc * np.eye(2)


def member(Pm, nopen, m):
    D = np.diag([1 / PAR.R + nopen / PAR.Rs, m / (PAR.R + PAR.Rc)])
    Pp = np.linalg.inv(np.linalg.inv(Pm) + D)
    Ai = AF @ Pp @ np.linalg.inv(Pm)
    krel = Pp[:, 1] / (PAR.R + PAR.Rc)
    Qi = AF @ (m * PAR.Rc * np.outer(krel, krel)) @ AF.T + PAR.qc * np.eye(2)
    return Ai, Qi, AF @ Pp @ AF.T + QW


def step(Pms, nopen, ms):
    A = np.zeros((8, 8)); Qn = np.zeros((8, 8)); new = []
    for i in range(n):
        Ai, Qi, Pn = member(Pms[i], nopen, ms[i])
        A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Ai; Qn[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Qi; new.append(Pn)
    return A, Qn, new


def dcl(P, A, Qn, Sig):
    PS = P @ Sig
    Sxy = Sig - PS.T @ np.linalg.solve(PS @ P.T, PS)
    M = P @ A @ Sxy @ A.T @ P.T
    return 0.5 * np.log(np.linalg.det(np.eye(P.shape[0]) + np.linalg.solve(P @ Qn @ P.T, M)))


def run_seq(Pms, Sig, seq):
    b1 = b2 = 0.0
    for nopen, ms in seq:
        A, Qn, Pn = step(Pms, nopen, ms)
        b1 = max(b1, dcl(P1, A, Qn, Sig)); b2 = max(b2, dcl(P2, A, Qn, Sig))
        Sig = A @ Sig @ A.T + Qn; Pms = Pn
    return b1, b2, Pms, Sig


def sym_state(nopen):
    Pm = np.diag([0.12, 0.09])
    for _ in range(3000):
        Pm = member(Pm, nopen, 3)[2]
    Pms = [Pm.copy() for _ in range(n)]
    Sig = np.zeros((8, 8))
    A, Qn, _ = step(Pms, nopen, [3] * n)
    for _ in range(400):
        Sig = A @ Sig @ A.T + Qn
    return Pms, Sig


best1 = (0.0, None); best2 = (0.0, None)
sorted_X = [x for x in itertools.product(range(4), repeat=n) if list(x) == sorted(x)]
allY = list(itertools.product(range(4), repeat=n))
for nopen in (0, 2, 4):
    Pms0, Sig0 = sym_state(nopen)
    c1, c2, _, _ = run_seq(Pms0, Sig0, [(nopen, (3, 3, 3, 3))] * 10)
    print(f"NEG symmetric sequence, nopen={nopen}: P1 {c1:.3e}, P2 {c2:.1e}")
    for X in sorted_X:
        _, _, PmsX, SigX = run_seq(Pms0, Sig0, [(nopen, X)] * 30)
        for Y in allY:
            A, Qn, _ = step(PmsX, nopen, Y)
            v1, v2 = dcl(P1, A, Qn, SigX), dcl(P2, A, Qn, SigX)
            if v1 > best1[0]: best1 = (v1, ("sustain-then", nopen, X, Y))
            if v2 > best2[0]: best2 = (v2, ("sustain-then", nopen, X, Y))
    print(f"(a) nopen={nopen} done: P1 sup so far {best1[0]:.4e} {best1[1]}; P2 sup {best2[0]:.4e} {best2[1]}  "
          f"({time.time()-t0:.0f}s)", flush=True)
Pms0, Sig0 = sym_state(0)
for X in sorted_X:
    for Y in allY:
        v1, v2, _, _ = run_seq(Pms0, Sig0, [(0, X), (0, Y)] * 10)
        if v1 > best1[0]: best1 = (v1, ("alternate", 0, X, Y))
        if v2 > best2[0]: best2 = (v2, ("alternate", 0, X, Y))
print(f"(b) alternating, nopen=0: P1 sup {best1[0]:.4e} {best1[1]}; P2 sup {best2[0]:.4e} {best2[1]}  "
      f"({time.time()-t0:.0f}s)", flush=True)
rng = np.random.default_rng(6101)
Pms2, Sig2 = sym_state(2)
for k in range(1500):
    seq = [(int(rng.integers(5)), tuple(rng.integers(4, size=n))) for _ in range(30)]
    v1, v2, _, _ = run_seq(Pms2, Sig2, seq)
    if v1 > best1[0]: best1 = (v1, ("random", k))
    if v2 > best2[0]: best2 = (v2, ("random", k))
print(f"(c) after random sequences: P1 sup {best1[0]:.4e} {best1[1]}; P2 sup {best2[0]:.4e} {best2[1]}")
print(f"total {time.time()-t0:.1f}s")
