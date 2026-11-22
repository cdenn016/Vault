"""Check C: the single-precision repair (one gamma for slots and attention, as def:fw-system has one gamma).

C1  inference clause at single gamma = 40 by Monte Carlo, both readings (variance from the blanket path vs
    constant variance).  Control: at the declared instance (gamma 4, attention top-kappa) the MC must reproduce
    0.00765 (blanket-path variance) and 0.02416 (constant variance) within MC error.
C2  quenched N_pr at gamma = 40, 200 draws.
C3  neighborhood of (P0, Rs, Rc, gamma) = (1, 1, 0.1, 40): 3^4 grid at x0.95/1/1.05, declared r0 = 30;
    expected: mechanism and mean-coupling baselines < 30 <= r(A), nulls < 30, agency >= 0.99.
"""
import os
for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[k] = "1"
import itertools
import math
import numpy as np
from fx import *

n, N, kappa, s2 = 4, 8, 3, 1e-3
out = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    out.append(line)


def mc_inference(P0, Rs, Rc, g_slot, g_att, T, rng):
    Gfull = lambda i, x, So: finfo(x / Rs + So / (Rs + Rc), P0)
    profs, law, _ = stationary_chain(n, Gfull, g_slot)
    Ps_all = 1 / (1 / P0 + profs.sum(1) / Rs)
    Vc = 1 / np.sum(law / Ps_all)
    counts = rng.multinomial(T, law)
    tot_pb = tot_c = 0.0
    sq = []
    for k, p in enumerate(profs):
        m = counts[k]
        if m == 0:
            continue
        S = p.sum()
        eta = rng.normal(0, math.sqrt(P0), m)
        s = eta[:, None] + rng.normal(0, math.sqrt(Rs), (m, n))
        Ps = 1 / (1 / P0 + S / Rs)
        mstar = Ps * (s * p).sum(1) / Rs
        ms = np.zeros((m, n))
        invL = np.zeros((m, n))
        for i in range(n):
            co = [j for j in range(n) if j != i and p[j]]
            js, pj = j_law(p[i], len(co), N - 1, kappa, g_att, P0, Rs, Rc)
            ji = rng.choice(js, size=m, p=pj)
            keys = rng.random((m, len(co))) if co else np.zeros((m, 0))
            order = np.argsort(keys, axis=1)
            acc = p[i] * s[:, i] / Rs
            nh = np.zeros(m)
            for r_, jj in enumerate(co):
                rank = np.argmax(order == r_, axis=1) if co else None
                heard = rank < ji
                acc = acc + heard * (s[:, jj] + rng.normal(0, math.sqrt(Rc), m)) / (Rs + Rc)
                nh += heard
            Lam = 1 / P0 + p[i] / Rs + nh / (Rs + Rc)
            ms[:, i] = acc / Lam + rng.normal(0, math.sqrt(s2), m)
            invL[:, i] = 1 / Lam
        y = ms.mean(1)
        Pb = invL.mean(1)
        d2 = (y - mstar) ** 2
        tot_pb += np.sum(0.5 * (Pb / Ps - 1 - np.log(Pb / Ps) + d2 / Ps))
        tot_c += np.sum(0.5 * (Vc / Ps - 1 - np.log(Vc / Ps) + d2 / Ps))
        sq.append(0.5 * d2 / Ps)
    sq = np.concatenate(sq)
    return tot_pb / T, tot_c / T, float(np.std(sq) / math.sqrt(T))


rng = np.random.default_rng(2026)
a, b, se = mc_inference(1.0, 1.0, 0.1, 4.0, np.inf, 200000, rng)
say("C1 control (gamma 4, top-kappa): blanket-path variance", a, "constant variance", b, "s.e.~", se,
    "| exact 0.00765 / 0.02416")
a, b, se = mc_inference(1.0, 1.0, 0.1, 40.0, 40.0, 200000, rng)
say("C1 single gamma 40: blanket-path variance", a, "constant variance", b, "s.e.~", se, "| alpha_I 0.02")

# C2 quenched N_pr at gamma 40
Gfull = lambda i, x, So: finfo(x / 1.0 + So / 1.1, 1.0)
profs, law40, _ = stationary_chain(n, Gfull, 40.0)
nd, Ss = 0, []
for l in range(200):
    T_ = [rng.choice([j for j in range(N) if j != i], size=kappa, replace=False) for i in range(N)]
    blocks = []
    for base in (0, n):
        U = [[int(j) - base for j in T_[base + i] if base <= j < base + n] for i in range(n)]
        blocks.append(sigma_c_fixedU(n, law40, U, 1.0, 1.0, 0.1, s2))
    Pi = np.linalg.inv(blockdiag(*blocks))
    if not is_diffusive(Pi)[0]:
        nd += 1
        continue
    Ss.append(min(contrast(Pi, range(n)), contrast(Pi, range(n, N))))
say("C2 gamma 40 quenched N_pr: non-diffusive", nd, "of 200 | diffusive S", np.round(sorted(Ss), 3))

# C3 neighborhood grid
rows = []
for fP, fs, fc, fg in itertools.product((0.95, 1.0, 1.05), repeat=4):
    P0, Rs, Rc, g1 = 1.0 * fP, 1.0 * fs, 0.1 * fc, 40.0 * fg
    Gf = lambda i, x, So: finfo(x / Rs + So / (Rs + Rc), P0)
    Gm = lambda i, x, So: finfo(x / Rs + min(kappa, So) / (Rs + Rc), P0)
    pr, lw, _ = stationary_chain(n, Gf, g1)
    SA = sigma_c(n, lw, N - 1, kappa, g1, P0, Rs, Rc, s2)
    Pi = np.linalg.inv(blockdiag(SA, SA))
    dif = is_diffusive(Pi)[0] and SA[0, 1] > 0
    rA = contrast(Pi, range(n))
    rsub = contrast(Pi, range(n - 1))
    prN, lwN, _ = stationary_chain(N, Gm, g1)
    PiH = np.linalg.inv(sigma_c(N, lwN, N - 1, kappa, g1, P0, Rs, Rc, s2))
    rmech = contrast(PiH, range(N)) if is_diffusive(PiH)[0] else np.inf
    A_ = -(Pi - np.diag(np.diag(Pi)))
    rmean = 1 + N * A_[np.triu_indices(N, 1)].mean() / Pi.sum(1).mean()
    Sp = sigma_c(n, lw, N - 1, kappa, 0.0, P0, Rs, Rc, s2)
    rpr = contrast(np.linalg.inv(blockdiag(Sp, Sp)), range(n))
    Sh = sigma_c(n, np.full(2 ** n, 2.0 ** -n), N - 1, kappa, 0.0, P0, Rs, Rc, s2)
    rh = contrast(np.linalg.inv(blockdiag(Sh, Sh)), range(n))
    ag = agency(lw, pr, P0, Rs)[0]
    rows.append((dif, rA, rsub, rmech, rmean, rpr, rh, ag))
R = np.array(rows, float)
names = ["diffusive", "r(A)", "r_sub", "mech", "mean", "N_pr ann", "N_hab", "Agency"]
for k, nm in enumerate(names):
    say(f"C3 {nm:10s} min {R[:, k].min():.6g} max {R[:, k].max():.6g}")
r0 = 30.0
ok_mech = np.sum((np.maximum.reduce([R[:, 2], R[:, 3], R[:, 5], R[:, 6]]) < r0) & (R[:, 1] >= r0))
ok_mean = np.sum((np.maximum.reduce([R[:, 2], R[:, 4], R[:, 5], R[:, 6]]) < r0) & (R[:, 1] >= r0))
say("C3 r0 = 30 admissible and A selected: mechanism", ok_mech, "/81 | mean coupling", ok_mean, "/81")
open("check_C_out.txt", "w").write("\n".join(out) + "\n")
