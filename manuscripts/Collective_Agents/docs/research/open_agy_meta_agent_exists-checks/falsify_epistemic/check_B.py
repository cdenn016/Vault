"""Check B: attacks that need new numbers.

B1  inference clause when the encoded belief must be a function of the declared scalar y alone
    (variance V(y) = 1/E[1/P*|y], the pointwise optimum).  Expected: between the pi-dependent value 0.00765
    and the constant-V value 0.02416; unknown whether below alpha_I = 0.02.
B2  quenched N_pr, 400 fresh draws: expected ~99.6% non-diffusive, max S among diffusive < 5.
B3  investigator's finite-gamma_att sensitivity reproduced (slot law at gamma=4): expected 7.26/11.79/24.39/47.53.
B4  single precision for slots AND attention (def:fw-system has one gamma): table of r(A), mechanism baseline,
    mean-coupling baseline, N_pr annealed, agency index.  Expected: fails at gamma=4; unknown at large gamma.
B5  eta_A-coordinate reading (every agent's error on eta_A; B-agents hold the prior plus computation noise):
    expected r(A) unchanged, mean-coupling baseline collapses toward 1.
"""
import os
for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[k] = "1"
import math
import numpy as np
from fx import *

n, N, kappa = 4, 8, 3
P0, Rs, Rc, gam, s2 = 1.0, 1.0, 0.1, 4.0, 1e-3
out = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    out.append(line)


Gfull = lambda i, x, So: finfo(x / Rs + So / (Rs + Rc), P0)
profs, law, _ = stationary_chain(n, Gfull, gam)

# ---------------- B1 ----------------
def coeffs(p):
    """Coefficient vectors of y (mean of means) and of y - m* on (eta, v_1..n, nu_ik, c_i); full attention."""
    S = p.sum()
    Lam = 1 / P0 + p / Rs + (S - p) / (Rs + Rc)
    Ps = 1 / (1 / P0 + S / Rs)
    nv = 1 + n + n * n + n
    cy = np.zeros(nv)
    cm = np.zeros(nv)
    var = np.concatenate([[P0], np.full(n, Rs), np.full(n * n, Rc), np.full(n, s2)])
    for i in range(n):
        if p[i]:
            cy[0] += (1 / (Lam[i] * Rs)) / n
            cy[1 + i] += (1 / (Lam[i] * Rs)) / n
        for k in range(n):
            if k != i and p[k]:
                w = 1 / (Lam[i] * (Rs + Rc)) / n
                cy[0] += w
                cy[1 + k] += w
                cy[1 + n + i * n + k] += w
        cy[1 + n + n * n + i] += 1 / n
    for k in range(n):
        if p[k]:
            cm[0] += Ps / Rs
            cm[1 + k] += Ps / Rs
    d = cy - cm
    return Ps, float(np.sum(cy ** 2 * var)), float(np.sum(d ** 2 * var)), float(np.mean(1 / Lam))


tab = [(law[k],) + coeffs(p) for k, p in enumerate(profs) if law[k] > 0]
W = np.array([t[0] for t in tab]); PS = np.array([t[1] for t in tab]); VY = np.array([t[2] for t in tab])
VD = np.array([t[3] for t in tab]); PB = np.array([t[4] for t in tab])
mean_part = np.sum(W * 0.5 * VD / PS)
klpb = np.sum(W * 0.5 * (PB / PS - 1 - np.log(PB / PS))) + mean_part
# y | pi ~ N(0, VY): integrate V(y) = 1/E[1/P* | y]
ys = np.linspace(-8, 8, 160001)
dy = ys[1] - ys[0]
dens = np.array([w * np.exp(-ys ** 2 / (2 * v)) / math.sqrt(2 * math.pi * v) for w, v in zip(W, VY)])
post = dens / dens.sum(0)
Vy = 1 / (post / PS[:, None]).sum(0)
klvy = float(np.sum(dens * 0.5 * (Vy[None, :] / PS[:, None] - 1 - np.log(Vy[None, :] / PS[:, None]))) * dy) + mean_part
Vc = 1 / np.sum(W / PS)
klc = np.sum(W * 0.5 * (Vc / PS - 1 - np.log(Vc / PS))) + mean_part
say("B1 mass check", float(dens.sum() * dy), "| alpha_I: N(y,Pbar(pi))", klpb, "| N(y,V(y)) optimum", klvy,
    "| N(y,const V)", klc, "| declared alpha_I 0.02")

# ---------------- B2 ----------------
rng = np.random.default_rng(99)
nd, Ss = 0, []
for l in range(400):
    T = [rng.choice([j for j in range(N) if j != i], size=kappa, replace=False) for i in range(N)]
    blocks = []
    for base in (0, n):
        U = [[int(j) - base for j in T[base + i] if base <= j < base + n] for i in range(n)]
        blocks.append(sigma_c_fixedU(n, law, U, P0, Rs, Rc, s2))
    Pi = np.linalg.inv(blockdiag(*blocks))
    if not is_diffusive(Pi)[0]:
        nd += 1
        continue
    Ss.append(min(contrast(Pi, range(n)), contrast(Pi, range(n, N))))
# control: the full model's attention passed through the fixed-U routine must reproduce r(A)=54.086
Uf = [[j for j in range(n) if j != i] for i in range(n)]
Sf = sigma_c_fixedU(n, law, Uf, P0, Rs, Rc, s2)
say("B2 control fixed-U full attention r(A)", contrast(np.linalg.inv(blockdiag(Sf, Sf)), range(n)),
    "| quenched draws 400, non-diffusive", nd, "| diffusive S values", np.round(sorted(Ss), 3))

# ---------------- B3 ----------------
for ga in (5.0, 10.0, 20.0, 40.0):
    SA = sigma_c(n, law, N - 1, kappa, ga, P0, Rs, Rc, s2)
    say("B3 slot gamma 4, gamma_att", ga, "r(A)", contrast(np.linalg.inv(blockdiag(SA, SA)), range(n)))

# ---------------- B4 ----------------
Gmed = lambda i, x, So: finfo(x / Rs + min(kappa, So) / (Rs + Rc), P0)
say("B4 single gamma: gamma | P(S=4) | r(A) | mech sup | mean-coupling | N_pr ann | N_hab | Agency | gammaC")
for g1 in (4.0, 10.0, 20.0, 30.0, 40.0, 60.0, 100.0):
    pr, lw, _ = stationary_chain(n, Gfull, g1)
    SA = sigma_c(n, lw, N - 1, kappa, g1, P0, Rs, Rc, s2)
    Pi = np.linalg.inv(blockdiag(SA, SA))
    rA = contrast(Pi, range(n))
    oth = max(contrast(Pi, C) for C in all_regions(N) if C not in (tuple(range(n)), tuple(range(n, N))))
    prN, lwN, _ = stationary_chain(N, Gmed, g1)
    SH = sigma_c(N, lwN, N - 1, kappa, g1, P0, Rs, Rc, s2)
    PiH = np.linalg.inv(SH)
    dH = is_diffusive(PiH)[0]
    rmech = max(contrast(PiH, C) for C in all_regions(N)) if dH else float("nan")
    A_ = -(Pi - np.diag(np.diag(Pi)))
    rmean = 1 + N * A_[np.triu_indices(N, 1)].mean() / Pi.sum(1).mean()
    Sp = sigma_c(n, lw, N - 1, kappa, 0.0, P0, Rs, Rc, s2)
    rpr = contrast(np.linalg.inv(blockdiag(Sp, Sp)), range(n))
    Sh = sigma_c(n, np.full(2 ** n, 2.0 ** -n), N - 1, kappa, 0.0, P0, Rs, Rc, s2)
    rh = contrast(np.linalg.inv(blockdiag(Sh, Sh)), range(n))
    ag, gC, _, _ = agency(lw, pr, P0, Rs)
    say("B4", g1, "|", round(float(lw[pr.sum(1) == 4].sum()), 4), "|", round(rA, 3), "(other max", round(oth, 3),
        ") |", round(rmech, 3), "(diffusive", dH, ") |", round(rmean, 3), "|", round(rpr, 3), "|", round(rh, 3), "|",
        round(ag, 6), "|", round(gC, 2))

# ---------------- B5 ----------------
SA = sigma_c(n, law, N - 1, kappa, np.inf, P0, Rs, Rc, s2)
Pi_eA = np.linalg.inv(blockdiag(SA, s2 * np.eye(n)))
A_ = -(Pi_eA - np.diag(np.diag(Pi_eA)))
rmeanA = 1 + N * A_[np.triu_indices(N, 1)].mean() / Pi_eA.sum(1).mean()
say("B5 eta_A coordinate: diffusive", is_diffusive(Pi_eA)[0], "| r(A)", contrast(Pi_eA, range(n)),
    "| max other region", max(contrast(Pi_eA, C) for C in all_regions(N) if C != tuple(range(n))),
    "| leak ratio on A", Pi_eA.sum(1)[:n].max() / Pi_eA.sum(1)[:n].mean(), "| mean-coupling baseline", rmeanA)
open("check_B_out.txt", "w").write("\n".join(out) + "\n")
