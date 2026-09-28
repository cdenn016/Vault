r"""Sanity checks for the Stage 4 first-contrast activation note (not proofs).

1. Geometry of the matching sheet S^(0): residuals in (z_+, z_1, z_2, z_3) coordinates.
2. Constants used in the written bounds (uniform 12-ball marginals).
3. Margins of the two deterministic activation-time inequalities (t_1 and s_flat).
4. Noise-free Monte Carlo of the first qualifying completion time tau and of
   m = E[ z(tau)^T K_Z z(tau) ] / T over seeds uniform in the ball of radius rho,
   to observe the eps^{-5} scaling claimed for the first-completion activation.
"""
from __future__ import annotations

import json
import math

import numpy as np
from scipy import integrate, special

rho = 1.0 / 100.0
out: dict = {}

# ---------------------------------------------------------------- 1. geometry
def covectors() -> tuple[np.ndarray, np.ndarray]:
    """Rows a^b_i, a^m_i of r^b_i = k_{i+1}-k_i-w_i, r^m_i = m_{i+1}-m_i-w_i; x=(k,m,w)."""
    ab = np.zeros((4, 12)); am = np.zeros((4, 12))
    for i in range(4):
        j = (i + 1) % 4
        ab[i, j] += 1; ab[i, i] -= 1; ab[i, 8 + i] -= 1
        am[i, 4 + j] += 1; am[i, 4 + i] -= 1; am[i, 8 + i] -= 1
    return ab, am

ab, am = covectors()
e, f = 0, 2  # selected edges of S^(0)
H = 2 * sum(np.outer(ab[g], ab[g]) + np.outer(am[g], am[g]) for g in (e, f))
D = np.zeros((4, 12)); D[:, 0:4] = np.eye(4); D[:, 4:8] = -np.eye(4)  # k - m
Rev = 2 * D.T @ D
npl = {g: (ab[g] + am[g]) / (2 * math.sqrt(2)) for g in (e, f)}
nmi = {g: (ab[g] - am[g]) / 2 for g in (e, f)}
u_plus = (npl[e] + npl[f]) / math.sqrt(2)
F = np.stack([(npl[e] - npl[f]) / math.sqrt(2), nmi[e], nmi[f]])  # hidden basis rows
x_circ = np.concatenate([np.zeros(8), np.ones(4)])
rng = np.random.default_rng(0)
xs = rng.standard_normal((50, 12))
zp = xs @ u_plus; z = xs @ F.T
res_err = max(
    np.abs(xs @ ab[e] - (zp + z[:, 0] + z[:, 1])).max(),
    np.abs(xs @ am[e] - (zp + z[:, 0] - z[:, 1])).max(),
    np.abs(xs @ ab[f] - (zp - z[:, 0] + z[:, 2])).max(),
    np.abs(xs @ am[f] - (zp - z[:, 0] - z[:, 2])).max(),
)
Tsym = 1e-3
K = H + Tsym * (np.eye(12) + Rev)
out["geometry"] = {
    "residual_identity_max_err": float(res_err),
    "hidden_proj_x_circ": (F @ x_circ).tolist(),
    "z_plus_x_circ": float(u_plus @ x_circ),
    "K_on_hidden_minus_diag": float(np.abs(F @ K @ F.T - np.diag([8 + Tsym, 4 + 5 * Tsym, 4 + 5 * Tsym])).max()),
    "K_u_plus_eigen_err": float(np.abs(K @ u_plus - (8 + Tsym) * u_plus).max()),
    "hidden_retained_block_err": float(np.abs(F @ K @ (np.eye(12) - F.T @ F)).max()),
}

# ---------------------------------------------------------------- 2. constants
c12 = special.gamma(7) / (math.sqrt(math.pi) * special.gamma(6.5))
I_half = integrate.quad(lambda y: (1 - y * y) ** 5, 0.5, 1)[0]
emin = (6 / math.pi) * (math.pi - 2) / 84  # E_unif[min(u2^2,u3^2)]/rho^2
out["constants"] = {
    "c12_one_coord_density_at_0_times_rho": c12,
    "E_unif_u_k^2_over_rho^2": 1 / 14,
    "E_unif_min_u2u3_sq_over_rho^2": emin,
    "int_{-1/4}^{1/4}(1-x^2)^{13/2}_lower_ratio": integrate.quad(lambda x: (1 - x * x) ** 6.5, -0.25, 0.25)[0] / 0.5,
    "(15/16)^{13/2}": (15 / 16) ** 6.5,
    "e^-9.2": math.exp(-9.2),
    "e^-8": math.exp(-8),
}

# ---------------------------------------------------------------- 3. margins
marg = {}
for eps in (1e-2, 1e-3, 1e-4, 1e-6):
    T = eps ** 8
    l1, l2 = 8 + T, 4 + 5 * T
    t1 = 0.5 * math.log(1 / eps) - 0.25 * math.log(50)
    sfl = 0.25 * math.log(1 / eps) + 0.15
    gen = (1 + math.sqrt(2) * rho) * math.exp(-l1 * t1) + rho * math.exp(-l2 * t1) + eps ** 2 / 8
    rare = (1 + math.sqrt(2) * rho) * math.exp(-l1 * sfl) + eps * math.exp(-l2 * sfl) + eps ** 2 / 8
    tstar = 2 * math.log(1 / eps) + 1
    marg[f"{eps:g}"] = {"t1": t1, "s_flat": sfl, "generic_bound/eps^2": gen / eps ** 2,
                        "rare_bound/eps^2": rare / eps ** 2, "t1+1<=t*": t1 + 1 <= tstar,
                        "p_hat": 73728 * eps ** 4 * tstar + 18 * tstar * math.exp(-1 / T) if T > 0 else None}
out["margins"] = marg

# ---------------------------------------------------------------- 4. Monte Carlo
def sample_ball(n: int, dim: int = 12) -> np.ndarray:
    g = rng.standard_normal((n, dim))
    g /= np.linalg.norm(g, axis=1, keepdims=True)
    r = rng.random(n) ** (1 / dim)
    return rho * g * r[:, None]

def first_completion(eps: float, u: np.ndarray, dt: float = 2e-3):
    """Noise-free first qualifying completion time for blocks {0,1},{2,3}; returns tau, z(tau)."""
    T = eps ** 8
    l1, l2 = 8 + T, 4 + 5 * T
    t1 = 0.5 * math.log(1 / eps) - 0.25 * math.log(50)
    tg = np.arange(0.0, t1 + 1.6, dt)
    E1 = np.exp(-l1 * tg)[None, :]; E2 = np.exp(-l2 * tg)[None, :]
    up, u1, u2, u3 = (u[:, k:k + 1] for k in range(4))
    zp = (-1 + up) * E1; z1 = u1 * E1; z2 = u2 * E2; z3 = u3 * E2
    thr_b, thr_m = math.sqrt(2) * eps ** 2, eps ** 2
    bad01 = (np.abs(zp + z1 + z2) > thr_b) | (np.abs(zp + z1 - z2) > thr_m)
    bad23 = (np.abs(zp - z1 + z3) > thr_b) | (np.abs(zp - z1 - z3) > thr_m)
    n1 = int(round(1 / dt))
    taus = []
    for bad in (bad01, bad23):
        c = np.concatenate([np.zeros((bad.shape[0], 1)), np.cumsum(bad, axis=1)], axis=1)
        win = c[:, n1 + 1:] - c[:, :-n1 - 1]  # bad count on grid window [i, i+n1]
        ok = win == 0
        idx = np.where(ok.any(axis=1), ok.argmax(axis=1), -1)
        taus.append(np.where(idx >= 0, tg[np.clip(idx, 0, None)] + n1 * dt, np.inf))
    tau = np.minimum(taus[0], taus[1])
    zt = np.stack([u1[:, 0] * np.exp(-l1 * tau), u2[:, 0] * np.exp(-l2 * tau), u3[:, 0] * np.exp(-l2 * tau)], axis=1)
    return tau, zt, t1

mc = {}
for eps in (1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5):
    T = eps ** 8
    lam = np.array([8 + T, 4 + 5 * T, 4 + 5 * T])
    ntot, chunk = 200_000, 4_000
    stats = []; taumax = 0.0; taumin = np.inf
    for _ in range(ntot // chunk):
        u = sample_ball(chunk)
        tau, zt, t1 = first_completion(eps, u)
        assert np.isfinite(tau).all()
        taumax = max(taumax, float(tau.max())); taumin = min(taumin, float(tau.min()))
        q = (zt ** 2 * lam).sum(axis=1) / T  # displacement part of z^T K_Z z / T
        vmin = np.minimum(np.abs(u[:, 2]), np.abs(u[:, 3]))
        stats.append(np.stack([q, vmin], axis=1))
    s = np.concatenate(stats)
    q, vmin = s[:, 0], s[:, 1]
    m = q.mean() + 3.0
    rare = vmin <= eps
    mc[f"{eps:g}"] = {
        "tau_max": taumax, "tau_bound_t1+1": t1 + 1, "tau_min": taumin,
        "tau_min_pred_(1/4)log(1/eps)+1": 0.25 * math.log(1 / eps) + 1,
        "m_mean": float(m), "m*eps^4": float(m * eps ** 4), "m*eps^5": float(m * eps ** 5),
        "rare_fraction": float(rare.mean()), "rare_share_of_q": float(q[rare].sum() / q.sum()),
        "q_std_err_rel": float(q.std() / math.sqrt(len(q)) / q.mean()),
    }
out["montecarlo_uniform_ball_noise_free"] = mc
print(json.dumps(out, indent=1))
