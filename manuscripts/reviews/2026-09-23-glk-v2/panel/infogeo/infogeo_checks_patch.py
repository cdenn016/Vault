r"""Patch checks: well-conditioned invariance residuals with baselines, Bhattacharyya remainder,
representative dependence of the reported singular-value / condition diagnostics."""
import json, math, os
import numpy as np
import scipy.linalg as sla

rng = np.random.default_rng(7)
EPS = float(np.finfo(float).eps)


def rand_spd(n, cond=20.0):
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    ev = np.exp(rng.uniform(0.0, math.log(cond), n))
    return (Q * ev) @ Q.T


def rand_gl_cond(n, cond):
    Q1, _ = np.linalg.qr(rng.standard_normal((n, n)))
    Q2, _ = np.linalg.qr(rng.standard_normal((n, n)))
    sv = np.exp(np.linspace(0, math.log(cond), n))
    return Q1 @ np.diag(sv) @ Q2


def logdet(S):
    s, v = np.linalg.slogdet(S)
    return v


def kl_gauss(m0, S0, m1, S1):
    r = m0.shape[0]
    L1 = np.linalg.cholesky(S1); L0 = np.linalg.cholesky(S0)
    M = sla.solve_triangular(L1, L0, lower=True)
    w = sla.solve_triangular(L1, m1 - m0, lower=True)
    return 0.5 * (np.sum(M ** 2) + w @ w - r + logdet(S1) - logdet(S0))


def renyi_gauss(m0, S0, m1, S1, al):
    Sa = (1 - al) * S0 + al * S1
    d = m1 - m0
    return (al / 2) * d @ np.linalg.solve(Sa, d) + (1.0 / (2 * (al - 1))) * ((1 - al) * logdet(S0) + al * logdet(S1) - logdet(Sa))


out = {}
for cond in (10.0, 1e3):
    res = []
    for _ in range(200):
        K = 4
        m0, m1 = rng.standard_normal(K), rng.standard_normal(K)
        S0, S1 = rand_spd(K), rand_spd(K)
        A = rand_gl_cond(K, cond)
        base = kl_gauss(m0, S0, m1, S1)
        res.append(abs(kl_gauss(A @ m0, A @ S0 @ A.T, A @ m1, A @ S1 @ A.T) - base) / max(1.0, base))
    out[f"KL_invariance_cond(A)={cond:g}"] = {"max_rel_residual": max(res), "baseline_cond^2_eps": cond ** 2 * EPS}
Uu = rand_gl_cond(4, 10.0); mu = rng.standard_normal(4); Sg = rand_spd(4); c = -2.7
xi0, C0 = np.linalg.solve(Uu, mu), np.linalg.solve(Uu, np.linalg.solve(Uu, Sg).T)
xi1 = np.linalg.solve(c * Uu, c * mu); C1 = np.linalg.solve(c * Uu, np.linalg.solve(c * Uu, c * c * Sg).T)
out["passive_dilation_rel_residual"] = float(max(np.max(np.abs(xi1 - xi0)) / np.max(np.abs(xi0)), np.max(np.abs(C1 - C0)) / np.max(np.abs(C0))))


def two_way(Tm):
    g = Tm.mean(); row = Tm.mean(1, keepdims=True) - g; col = Tm.mean(0, keepdims=True) - g
    inter = Tm - g - row - col
    return float(np.linalg.norm(inter) / np.linalg.norm(Tm - g))


N, r = 10, 3
A_ = rng.standard_normal((N, r)); B_ = rng.standard_normal((N, r))
VQl = [rand_spd(r, 30) for _ in range(N)]; Vst = rand_spd(r, 30)
bha = np.array([[renyi_gauss(A_[i], VQl[i], B_[j], Vst, 0.5)
                 + 0.5 * A_[i] @ np.linalg.solve(0.5 * (VQl[i] + Vst), B_[j]) for j in range(N)] for i in range(N)])
out["bhattacharyya_sharedK_minus_rowmetric_dot_interaction_frac"] = two_way(bha)

# representative dependence of the paper's raw-map diagnostics (common left action on S_Q, S_K)
K, r = 8, 3
SQ, SK = rng.standard_normal((r, K)), rng.standard_normal((r, K))
Ci, Cj = rand_spd(K, 30), rand_spd(K, 30)
xi_i, xi_j = rng.standard_normal(K), rng.standard_normal(K)
D0 = kl_gauss(SQ @ xi_i, SQ @ Ci @ SQ.T, SK @ xi_j, SK @ Cj @ SK.T)
rows = []
for name, A in (("identity", np.eye(r)), ("scale_x40", 40 * np.eye(r)), ("scale_x0.025", 0.025 * np.eye(r)),
                ("diag_1_1_40", np.diag([1.0, 1.0, 40.0])), ("orthogonal", np.linalg.qr(rng.standard_normal((r, r)))[0])):
    sq, sk = A @ SQ, A @ SK
    VK = sk @ Cj @ sk.T; VQ = sq @ Ci @ sq.T
    rows.append({"A": name, "D_ij": kl_gauss(sq @ xi_i, VQ, sk @ xi_j, VK) - D0,
                 "min_sv_SQ": float(np.linalg.svd(sq, compute_uv=False).min()),
                 "min_sv_SK": float(np.linalg.svd(sk, compute_uv=False).min()),
                 "cond_VK": float(np.linalg.cond(VK)), "cond_VQ": float(np.linalg.cond(VQ)),
                 "relative_spectrum_VK^-1VQ": np.sort(np.real(np.linalg.eigvals(np.linalg.solve(VK, VQ)))).tolist()})
out["representative_dependence"] = rows
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "infogeo_checks_patch.json")
json.dump(out, open(path, "w"), indent=1, default=float)
print(json.dumps(out, indent=1, default=float))
