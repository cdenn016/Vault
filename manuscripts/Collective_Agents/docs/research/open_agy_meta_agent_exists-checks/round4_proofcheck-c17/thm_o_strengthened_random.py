r"""Random finite test of Theorem O under STRENGTHENED hypotheses (joint S_n-equivariance of (A, E, S_C),
i.i.d. private inputs, so the joint law of (z, xi) is exchangeable), n = 3 members with d = 2 local states,
2 private inputs per member, 2 scalar non-members independent of C (O1), scalar world,
tilde-y loading kappa_z (x) p on z_C and kappa_xi (x) m on xi_C with W = span{v}, dim W = 1 < n-1 = 2.
Sigma^c = S Cov(z_tau | tilde-y_{0..Tt}) S^T (Lemma M), Sigma^eff = S Cov(z_tau) S^T, z_0 = 0, finite window.
Checks: f in D_C, f perp v is an eigenvector of both with the same eigenvalue; when Pi^c diffusive,
xi_in <= 1/alpha = xi_in^eff and xi_out >= xi_out^eff. Finite test only; not a proof.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

rng = np.random.default_rng(2026)
n, d, dxi, nR = 3, 2, 2, 2
nz = n * d + nR
nxi = n * dxi + nR
Tt, tau = 50, 35
one = np.ones(n); J = np.outer(one, one)

def equiv(M0, M1):
    return np.kron(np.eye(n), M0) + np.kron(J - np.eye(n), M1)

def rates(Pi, C):
    N = Pi.shape[0]; C = list(C); k = len(C)
    eps = Pi.sum(1); a = -(Pi - np.diag(np.diag(Pi)))
    LC = np.zeros((k, k))
    for x, i in enumerate(C):
        for y, j in enumerate(C):
            if i != j:
                LC[x, y] = -a[i, j]; LC[x, x] += a[i, j]
    Q = np.diag(eps[C]) + LC
    U = np.linalg.svd(np.ones((k, 1)))[0][:, 1:]
    xin = np.min(np.linalg.eigvalsh(U.T @ Q @ U))
    phi = np.zeros(N); phi[C] = 1 / np.sqrt(k)
    return xin, phi @ Pi @ phi

def diffusive(Pi, tol=1e-10):
    off = Pi - np.diag(np.diag(Pi))
    return bool(np.all(off <= tol) and np.all(Pi.sum(1) >= -tol))

stats = dict(draws=0, eig_err=0.0, both_diff=0, viol_in=0, viol_out=0, pic_diff_eff_not=0, min_gap_in=np.inf)
for draw in range(300):
    A = np.zeros((nz, nz)); E = np.zeros((nz, nxi))
    A0 = np.diag(rng.uniform(0, 1, d)); A[:n*d, :n*d] = equiv(A0, rng.uniform(0, 0.5) * A0)
    A[n*d:, n*d:] = np.diag(rng.uniform(-0.8, 0.8, nR))
    A *= 0.7 / max(np.max(np.abs(np.linalg.eigvals(A))), 1e-9)
    E0 = np.abs(rng.normal(size=(d, dxi))); E[:n*d, :n*dxi] = equiv(E0, rng.uniform(0, 1) * E0)
    E[n*d:, n*dxi:] = np.diag(rng.uniform(0.5, 1.5, nR))
    s = np.abs(rng.normal(size=d))
    S = np.zeros((n + nR, nz)); S[:n, :n*d] = np.kron(np.eye(n), s); S[n:, n*d:] = np.eye(nR)
    v = np.array([1.0, -1.0, 0.0]) / np.sqrt(2)                  # W = span{v}
    kz = one + 0.3 * rng.normal() * v; kx = one + 0.3 * rng.normal() * v
    p = rng.normal(size=d); m = rng.normal(size=dxi)
    Lz = np.concatenate([np.kron(kz, p), np.zeros(nR)])  # 1 x nz
    Lx = np.concatenate([np.kron(kx, m), np.zeros(nR)])  # 1 x nxi
    qnu, qw = rng.uniform(0.1, 1), rng.uniform(0.1, 1)
    # linear maps on noise vector: per step [xi (nxi), nu (1), w (1)]
    per = nxi + 2; Ntot = per * (Tt + 1)
    z = np.zeros((nz, Ntot)); Z = []; Y = []
    for t in range(Tt + 1):
        Xi = np.zeros((nxi, Ntot)); Xi[:, t*per:t*per+nxi] = np.eye(nxi)
        Nu = np.zeros((1, Ntot)); Nu[0, t*per+nxi] = np.sqrt(qnu)
        Wn = np.zeros((1, Ntot)); Wn[0, t*per+nxi+1] = np.sqrt(qw)
        Z.append(z)
        Y.append(Lz @ z + Lx @ Xi + Nu + Wn)
        z = A @ z + E @ Xi
    Ly = np.vstack(Y); Lt = S @ Z[tau]
    Seff = Lt @ Lt.T
    Sxy = Lt @ Ly.T
    Sc = Seff - Sxy @ np.linalg.solve(Ly @ Ly.T, Sxy.T)
    f = np.zeros(n + nR); f[:n] = np.array([1.0, 1.0, -2.0]) / np.sqrt(6)   # in D_C, perp v
    alpha = f @ Seff @ f
    err = max(np.max(np.abs(Seff @ f - alpha * f)), np.max(np.abs(Sc @ f - alpha * f)))
    stats["eig_err"] = max(stats["eig_err"], err); stats["draws"] += 1
    Pc, Pe = np.linalg.inv(Sc), np.linalg.inv(Seff)
    dc, de = diffusive(Pc), diffusive(Pe)
    if dc and not de:
        stats["pic_diff_eff_not"] += 1
    if dc and de:
        stats["both_diff"] += 1
        xin, xout = rates(Pc, range(n)); xine, xoute = rates(Pe, range(n))
        stats["min_gap_in"] = min(stats["min_gap_in"], xine - xin)
        stats["max_rel_excess_in"] = max(stats.get("max_rel_excess_in", -np.inf), (xin - xine) / xine)
        stats["max_rel_err_eff_eq_1_over_alpha"] = max(stats.get("max_rel_err_eff_eq_1_over_alpha", 0.0), abs(xine * alpha - 1))
        stats["max_rel_excess_out"] = max(stats.get("max_rel_excess_out", -np.inf), (xoute - xout) / xoute)
        if xin > xine * (1 + 1e-6) or abs(xine * alpha - 1) > 1e-6:
            stats["viol_in"] += 1
        if xout < xoute * (1 - 1e-6):
            stats["viol_out"] += 1
print(stats)
