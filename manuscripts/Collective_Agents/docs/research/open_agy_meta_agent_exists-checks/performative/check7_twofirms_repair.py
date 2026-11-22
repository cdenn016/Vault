r"""Check 7: repairing ex:met-two-firms inside its own model class (consensus filter on contributions,
bounded model, act noise 0.01, computation noise 1e-3, latency of eq:met-firms).

Variants (all n_c = 1, bounded model for both firms):
 V0: the declared example (R = (0.5,1,2,4 | 1,1,2,2), lazy ring)            -> non-diffusive (reproduced in check 6)
 V1: homogeneous R = 1, complete-graph consensus W = (1-w)I + w/(n-1)(J-I), w = 0.5 (nonsingular),
     only C1's acts enter the price (C2 acts on a variable outside the conditioned world? no: C2's
     acts enter nothing)                                                     -> expect cross = 0; within C1 diffusive?
 V2: as V1 but both firms' acts enter the price                              -> expect cross > 0 (C3 regime)
 V3: as V1 but with the singular lazy ring                                   -> expect within-firm positive entries
 V4: as V1 with heterogeneous R of the example                               -> report
Declared expectations: V1 diffusive with r(C1) > 1 (exchangeable block, collective mode enlarged by the
shared stored act noise); V2 and V3 non-diffusive; cross entries of V1 vanish.
For diffusive variants: contrast of C1 and C2, mean-coupling baseline (clause (c)), r_sub.
"""
import itertools
import numpy as np
from pc import world_conditional_cov, diffusivity, riccati_scalar, contrast


def build(nc, R, Wr, load=(0.2, 0.2), gu=(0.15, 0.15)):
    f, bp, Qw = 0.9, 0.2, 0.05
    R = np.asarray(R, float)
    firm = [0] * 4 + [1] * 4
    Ls = [sum(1 / R[:4]), sum(1 / R[4:])]
    Pb = [riccati_scalar(f, 0.1, Ls[k])[1] for k in range(2)]
    Wn = np.linalg.matrix_power(Wr, nc)
    W = np.zeros((8, 8)); W[:4, :4] = Wn; W[4:, 4:] = Wn
    n = 4
    ip = 0; iX = list(range(1, 9)); iu = list(range(9, 17)); iy = list(range(17, 25)); ie = list(range(25, 33))
    A = np.zeros((33, 33)); G = np.zeros((33, 33))
    A[ip, ip] = f; G[ip, 0] = np.sqrt(Qw)
    for j in range(8):
        A[ip, iu[j]] = load[firm[j]]
    for i in range(8):
        k = firm[i]
        A[iX[i], ip] = 1.0; G[iX[i], 1 + i] = np.sqrt(R[i])
        A[iu[i], ie[i]] = -gu[k]; G[iu[i], 9 + i] = np.sqrt(0.01)
        for j in range(8):
            if firm[j] == k:
                A[iy[i], iu[j]] = 1.0
        G[iy[i], 17 + i] = np.sqrt(1e-3)
        coef = f * Pb[k] * n * W[i] / R
        A[ie[i], ie[i]] = f * (1 - Pb[k] * Ls[k])
        for j in range(8):
            A[ie[i], iX[j]] += coef[j]
        A[ie[i], iy[i]] += bp
        G[ie[i], 25 + i] = np.sqrt(1e-3)
    return A, G @ G.T, [ip], ie


def analyze(label, A, Qx, iw, ia):
    Pi = np.linalg.inv(world_conditional_cov(A, Qx, iw, ia, 60))
    dif = diffusivity(Pi)
    C1, C2 = list(range(4)), list(range(4, 8))
    cross = Pi[np.ix_(C1, C2)]
    off = Pi - np.diag(np.diag(Pi))
    s = "%-4s max offdiag=%.4g (within C1 %.4g, C2 %.4g)  cross in [%.3e, %.3e]  min rowsum=%.4g  diffusive=%s" % (
        label, dif["max_offdiag"], off[np.ix_(C1, C1)].max(), off[np.ix_(C2, C2)].max(), cross.min(), cross.max(),
        dif["min_rowsum"], dif["diffusive"])
    print(s)
    if dif["diffusive"]:
        a = -off
        abar = a[np.triu_indices(8, 1)].mean(); epsbar = Pi.sum(axis=1).mean()
        rbar = 1 + 8 * abar / epsbar
        rs = {C: contrast(Pi, list(C))["r"] for m in range(2, 9) for C in itertools.combinations(range(8), m)}
        top = sorted(rs.items(), key=lambda kv: -kv[1])[:4]
        eps = Pi.sum(axis=1)
        print("     r(C1)=%.5f r(C2)=%.5f  rbar_hom(mean coupling)=%.5f  eps_max/eps_mean(C1)=%.5f  top regions: %s" % (
            rs[tuple(C1)], rs[tuple(C2)], rbar, eps[C1].max() / eps[C1].mean(), [(C, round(r, 4)) for C, r in top]))
    return Pi


if __name__ == "__main__":
    S = np.roll(np.eye(4), 1, axis=1)
    lazy = 0.5 * np.eye(4) + 0.25 * (S + S.T)
    w = 0.5
    comp = (1 - w) * np.eye(4) + w / 3 * (np.ones((4, 4)) - np.eye(4))
    print("eig(lazy ring) =", np.round(np.linalg.eigvalsh(lazy), 6), " eig(complete, w=0.5) =", np.round(np.linalg.eigvalsh(comp), 6))
    Rex = [0.5, 1, 2, 4, 1, 1, 2, 2]
    analyze("V0", *build(1, Rex, lazy))
    analyze("V1", *build(1, [1] * 8, comp, load=(0.2, 0.0)))
    analyze("V2", *build(1, [1] * 8, comp, load=(0.2, 0.2)))
    analyze("V3", *build(1, [1] * 8, lazy, load=(0.2, 0.0)))
    analyze("V4", *build(1, Rex, comp, load=(0.2, 0.0)))
    for nc in (0, 2, 4):
        analyze("V1n%d" % nc, *build(nc, [1] * 8, comp, load=(0.2, 0.0)))
