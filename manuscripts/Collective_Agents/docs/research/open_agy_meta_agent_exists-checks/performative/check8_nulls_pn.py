r"""Check 8: N_hab and N_pr for the performative niche candidate PN (quenched draws), and the
member-restricted order parameter Omega_int(A | zeta_B) over six rounds.

Full model PN (check 5): r(A) = r(B) = 17.97891, mean-coupling baseline 15.55335, window
(15.55335, 17.97891]; statistic S0 = max significance r(C)/rbar_hom = 1.15597.

Nulls (quenched: partners drawn once; the annealed variants are not computed):
 N_pr : each receiver's 3 partners redrawn uniformly from the other 7 agents; acts unchanged (g=0.15).
        Exact filters give zero gain to relays about the other niche's component.
 N_hab: gamma = 0: attention drawn from uniform habits (same law as N_pr, quenched), acts drawn from
        habits, hence independent of beliefs (g = 0; habit act noise conditioned as broadcast noise
        or absent).
Selector applied to each null draw with the null's own mean-coupling baseline (reading R-own) and with
the full model's baseline held fixed (reading R-fixed).  A draw whose Pi^c is not diffusive has no
contrast (open:col-non-diffusive) and selects no collective.
Declared expectations: (E1) most draws non-diffusive or with no region above the baseline; (E2) the
fraction of draws selecting exactly {A,B} at r0 = 16.8 (window midpoint) is small; (E3) p-value of
the N_pr test with 99 draws is 0.01 if no draw reaches S0.  (E4) Omega_int(A | zeta_B) > 0.
"""
import itertools
import numpy as np
from pc import world_conditional_cov, diffusivity, contrast
from pcg import build

F, Q, R, Rc, b = 0.9, 0.05, 1.0, 0.2, 0.2
n, N = 4, 8
A_, B_ = list(range(4)), list(range(4, 8))
R0_LIST = [15.6, 16.8, 17.97]
RBAR_FULL = 15.55335


def spec_reads(reads, g):
    comp = [0] * n + [1] * n
    Rcd = {(i, j): Rc for i in range(N) for j in reads[i]}
    kn = [set(A_) if i < n else set(B_) for i in range(N)]
    return {"F": [F, F], "Qw": [Q, Q], "comp": comp, "R": [R] * N, "reads": reads, "Rc": Rcd,
            "act": comp[:], "g": [g] * N, "b": b, "known": kn, "mu": [0.0] * N}


REGIONS = [list(C) for m in range(2, N + 1) for C in itertools.combinations(range(N), m)]


def all_contrasts(Pi):
    eps = Pi.sum(axis=1)
    return [(tuple(C), contrast(Pi, C)["r"], eps[C].max() / eps[C].mean()) for C in REGIONS]


def selected(rs, r0, rbar):
    return [C for C, r, het in rs if r >= r0 and r0 > max(het, rbar)]


def stat_and_sel(Pi, rs):
    a = -(Pi - np.diag(np.diag(Pi)))
    rbar = 1 + N * a[np.triu_indices(N, 1)].mean() / Pi.sum(axis=1).mean()
    return max(r for _, r, _ in rs) / rbar, rbar


if __name__ == "__main__":
    rng = np.random.default_rng(7)
    for null, g in [("N_pr", 0.15), ("N_hab", 0.0)]:
        nd = 0; S = []; same = {r0: [0, 0] for r0 in R0_LIST}
        for draw in range(99):
            reads = [list(rng.choice([j for j in range(N) if j != i], size=3, replace=False)) for i in range(N)]
            m = build(spec_reads(reads, g))
            Pi = np.linalg.inv(world_conditional_cov(m["A"], m["Qx"], m["iw"], m["ia"], 60))
            if not diffusivity(Pi, tol=1e-10)["diffusive"]:
                S.append(-np.inf); continue
            nd += 1
            rs = all_contrasts(Pi)
            s, rbar = stat_and_sel(Pi, rs); S.append(s)
            for r0 in R0_LIST:
                same[r0][0] += set(selected(rs, r0, rbar)) == {tuple(A_), tuple(B_)}
                same[r0][1] += set(selected(rs, r0, RBAR_FULL)) == {tuple(A_), tuple(B_)}
        S = np.array(S)
        S0 = 17.97891 / 15.55335
        p = (1 + np.sum(S >= S0)) / (len(S) + 1)
        fin = S[np.isfinite(S)]
        print("%s: diffusive draws %d/99; statistic over diffusive draws: max %.4f median %.4f; S0 = %.4f; p = %.3f" % (
            null, nd, fin.max() if len(fin) else float("nan"), np.median(fin) if len(fin) else float("nan"), S0, p))
        for r0 in R0_LIST:
            print("   r0=%.2f: draws selecting exactly {A,B}: %d (own baseline), %d (full baseline held fixed)" % (r0, same[r0][0], same[r0][1]))

    # Omega_int(A | zeta_B) over rounds 1..6, pair (0,1), conditioning on initial state and world innovations
    m = build(spec_reads([[j for j in (A_ if i < n else B_) if j != i] for i in range(N)], 0.15))
    Am, Qx = m["A"], m["Qx"]
    # recover a factor G with Qx = G G^T split into world (first 2 noise columns) and private parts:
    # rebuild G explicitly from pcg internals by Cholesky of the private part is not unique; instead
    # compute the path covariance due to private noises: total noise covariance minus world part.
    # In pcg the world innovation enters only the eta rows (columns 0,1 of G); private noises enter both.
    # So private covariance = Qx - diag(Q,Q) on the eta block.
    Qpriv = Qx.copy(); Qpriv[0, 0] -= Q; Qpriv[1, 1] -= Q
    T = 6; d = Am.shape[0]
    # path covariance of x_1..x_T driven by private noises only (x_0 and w conditioned => fixed)
    Phi = [np.linalg.matrix_power(Am, k) for k in range(T)]
    C = np.zeros((T * d, T * d))
    for t in range(1, T + 1):
        for s in range(1, T + 1):
            acc = np.zeros((d, d))
            for u in range(0, min(t, s)):
                acc += Phi[t - 1 - u] @ Qpriv @ Phi[s - 1 - u].T
            C[(t - 1) * d:t * d, (s - 1) * d:s * d] = acc
    i0 = [(t * d) + 2 + 0 for t in range(T)]; i1 = [(t * d) + 2 + 1 for t in range(T)]
    S00 = C[np.ix_(i0, i0)]; S11 = C[np.ix_(i1, i1)]; S01 = C[np.ix_(i0, i1)]
    M = np.linalg.solve(S00, S01) @ np.linalg.solve(S11, S01.T)
    I01 = -0.5 * np.log(np.linalg.det(np.eye(T) - M))
    print("Omega_int pair (0,1) over rounds 1..6 given X_sh and zeta_B: %.4f nats" % I01)
    # negative control: pair (0,4) across niches
    i4 = [(t * d) + 2 + 4 for t in range(T)]
    S44 = C[np.ix_(i4, i4)]; S04 = C[np.ix_(i0, i4)]
    M = np.linalg.solve(S00, S04) @ np.linalg.solve(S44, S04.T)
    print("NEG pair (0,4) across niches: %.2e nats" % (-0.5 * np.log(np.linalg.det(np.eye(T) - M))))
