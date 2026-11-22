"""Verification suite for open:lrn-noncentral (Exact second moment E[psi psi^T]).

Covers claims C1-C5 with two independent computational channels per claim and
planted-error negative controls. Fixed seed, deterministic, single-threaded.
"""
from __future__ import annotations

import math
import numpy as np
from scipy import integrate, special

SEED = 20261122
RNG = np.random.default_rng(SEED)

# Exact 6-point probabilists' Gauss-Hermite nodes/weights (exact for poly deg <= 11)
_GH_X, _GH_W = np.polynomial.hermite_e.hermegauss(6)
_GH_W = _GH_W / math.sqrt(2.0 * math.pi)
_E1, _E2 = np.meshgrid(_GH_X, _GH_X, indexing="ij")
_GH_PTS = np.stack([_E1.ravel(), _E2.ravel()], axis=1)  # (36, 2)
_GH_WTS = (_GH_W[:, None] * _GH_W[None, :]).ravel()     # (36,)


def f_alpha(alpha: float, lam: float) -> float:
    """f_alpha(lam) = int_0^1 (1-v)^(alpha-1) exp(-lam*v) dv = (1/alpha) 1F1(1; alpha+1; -lam)."""
    assert alpha > 0.0 and lam >= 0.0
    return float(special.hyp1f1(1.0, alpha + 1.0, -lam) / alpha)


def rc1_isotropic_closed(K: int, H: np.ndarray, m_i: np.ndarray, u0: float, Rc0: float, sigma_H: float) -> float:
    """Exact closed form (Claim C3b) for r_c=1, P = p*I_K, K >= 3."""
    assert K >= 3 and H.shape == (1, K) and m_i.shape == (K,) and sigma_H > 0.0 and Rc0 >= 0.0
    H_norm = float(np.linalg.norm(H))
    assert H_norm > 0.0
    lam = H_norm**2 / (2.0 * sigma_H**2)
    Hm = float(H[0] @ m_i)
    m_par = Hm / H_norm
    m_perp_sq = float(np.dot(m_i, m_i) - m_par**2)

    f0 = f_alpha(K / 2.0 - 1.0, lam)
    f1 = (1.0 - (K / 2.0 - 1.0) * f0) / lam
    f2 = (1.0 - (K / 2.0) * f1) / lam

    cR = 0.5 * lam * ((K - 1) * f1 - (K - 3) * f0)
    cu = cR - 2.0 * lam * f1 + 1.0
    c_par = 0.25 * (K**2 - 1) * (f1 - f2)
    c_perp = 0.25 * (K + 1) * f2 - 0.25 * (K - 1) * f1
    c_par_u = 0.25 * (K - 1) * (K - 2) * (f1 - f0)
    return float(cR * Rc0 + cu * u0**2 + c_par * Hm**2 + c_perp * (H_norm**2) * m_perp_sq + 2.0 * c_par_u * Hm * u0)


def rc1_schwinger_1d(P: np.ndarray, H: np.ndarray, m_i: np.ndarray, u0: float, Rc0: float, sigma_H: float) -> tuple[float, float]:
    """Exact 1D Schwinger-Laplace integral (Claim C3a) for r_c=1, general P > 0, K >= 3."""
    K = P.shape[0]
    assert K >= 3 and P.shape == (K, K) and H.shape == (1, K) and sigma_H > 0.0 and Rc0 >= 0.0
    eigvals, eigvecs = np.linalg.eigh(P)
    assert np.all(eigvals > 0.0), "P must be SPD"
    P_sqrt = eigvecs @ np.diag(np.sqrt(eigvals)) @ eigvecs.T
    P_inv_sqrt = eigvecs @ np.diag(1.0 / np.sqrt(eigvals)) @ eigvecs.T
    s = (sigma_H**2) * eigvals
    h = eigvecs.T @ (P_sqrt @ H[0])
    z = eigvecs.T @ (P_inv_sqrt @ m_i)
    c0 = float(H[0] @ m_i - u0)

    def integrand(t: float) -> float:
        inv_d = 1.0 / (1.0 + 2.0 * t * s)
        Z = float(np.prod(np.sqrt(inv_d)) * math.exp(-t * float(np.sum((h**2) * inv_d))))
        mu_t = h * inv_d
        sig_t = s * inv_d
        mX = float(np.sum(h * mu_t))
        mY = float(np.sum(z * mu_t))
        vXX = float(np.sum((h**2) * sig_t))
        vXY = float(np.sum(h * z * sig_t))
        vYY = float(np.sum((z**2) * sig_t))
        EX = mX
        EXY = mX * mY + vXY
        EX2 = mX**2 + vXX
        EX2Y = (mX**2) * mY + vXX * mY + 2.0 * mX * vXY
        EX2Y2 = (mX**2 + vXX) * (mY**2 + vYY) + 2.0 * (vXY**2) + 4.0 * mX * mY * vXY
        return Z * (2.0 * c0 * (u0 * EX - EXY) + t * ((u0**2 + Rc0) * EX2 - 2.0 * u0 * EX2Y + EX2Y2))

    q_val, q_err = integrate.quad(integrand, 0.0, np.inf, epsabs=1e-13, epsrel=1e-13, limit=250)
    return float(c0**2 + q_val), float(q_err)


def prop_expansion_bracket(P: np.ndarray, H: np.ndarray, m_i: np.ndarray, u: np.ndarray, Rc: np.ndarray) -> np.ndarray:
    """Second-order bracket from prop:lrn-understanding-expansion."""
    S0 = H @ P @ H.T
    S0_inv = np.linalg.inv(S0)
    O0 = P @ H.T @ S0_inv
    P0_plus = P - O0 @ H @ P
    mbar0 = m_i + O0 @ (u - H @ m_i)
    E_mhat0_sq = float(np.dot(mbar0, mbar0) + np.trace(O0 @ Rc @ O0.T))
    rc = H.shape[0]
    trP0 = float(np.trace(P0_plus))
    OTO = O0.T @ O0
    return E_mhat0_sq * np.eye(rc) - trP0 * (Rc @ S0_inv + S0_inv @ Rc) + (Rc @ OTO + OTO @ Rc)


def exact_ET_rc2_batch(Hbar: np.ndarray, zbar: np.ndarray, u: np.ndarray, Rc: np.ndarray, mus: np.ndarray, Sigs: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Vectorized exact polynomial expectation under P_T for r_c=2 over a batch of B matrices T.
    mus: (B, K, 2), Sigs: (B, K, 2, 2).
    """
    B, K, _ = mus.shape
    has_z = bool(np.any(zbar != 0.0))
    b_max = 3 if has_z else 1

    # Single-column exact moments via 36-pt 2D Gauss-Hermite (exact for poly deg <= 11)
    def single_col(k: int) -> dict:
        h_k = Hbar[:, k]
        z_k = float(zbar[k])
        mu_k = mus[:, k, :]      # (B, 2)
        Sig_k = Sigs[:, k, :, :] # (B, 2, 2)
        l00 = np.sqrt(Sig_k[:, 0, 0])
        l10 = Sig_k[:, 1, 0] / l00
        l11 = np.sqrt(np.maximum(Sig_k[:, 1, 1] - l10 * l10, 0.0))
        # G: (B, 36, 2)
        g0 = mu_k[:, None, 0] + l00[:, None] * _GH_PTS[None, :, 0]
        g1 = mu_k[:, None, 1] + l10[:, None] * _GH_PTS[None, :, 0] + l11[:, None] * _GH_PTS[None, :, 1]
        G = np.stack([g0, g1], axis=-1) # (B, 36, 2)

        Ak = (h_k[None, None, :, None] * G[:, :, None, :]).reshape(B, 36, 4)
        Sk = np.stack([g0 * g0, g0 * g1, g1 * g1], axis=-1)  # (B, 36, 3)
        pA = [np.ones((B, 36, 1)), Ak, (Ak[:, :, :, None] * Ak[:, :, None, :]).reshape(B, 36, 16)]
        pS = [np.ones((B, 36, 1)), Sk, (Sk[:, :, :, None] * Sk[:, :, None, :]).reshape(B, 36, 9)]
        if has_z:
            qk = z_k * G
            pq = [np.ones((B, 36, 1)), qk, (qk[:, :, :, None] * qk[:, :, None, :]).reshape(B, 36, 4)]
        else:
            pq = [np.ones((B, 36, 1))]

        mk = {}
        for a in range(3):
            for b in range(b_max):
                for c in range(3):
                    val = np.einsum("n,bni,bnj,bnk->bijk", _GH_WTS, pA[a], pq[b], pS[c])
                    mk[(a, b, c)] = val.reshape((B,) + (4,) * a + (2,) * b + (3,) * c)
        return mk

    def convolve(M1: dict, M2: dict) -> dict:
        out = {}
        for a in range(3):
            for b in range(b_max):
                for c in range(3):
                    acc = np.zeros((B,) + (4,) * a + (2,) * b + (3,) * c)
                    for a1 in range(a + 1):
                        a2 = a - a1
                        for b1 in range(b + 1):
                            b2 = b - b1
                            for c1 in range(c + 1):
                                c2 = c - c1
                                t1 = M1[(a1, b1, c1)]
                                t2 = M2[(a2, b2, c2)]
                                r1 = a1 + b1 + c1
                                r2 = a2 + b2 + c2
                                # Batched outer product along axis 0
                                prod = t1.reshape(t1.shape + (1,) * r2) * t2.reshape((B,) + (1,) * r1 + t2.shape[1:])
                                off = 1 + r1
                                perm = (
                                    [0]
                                    + list(range(1, 1 + a1))
                                    + list(range(off, off + a2))
                                    + list(range(1 + a1, 1 + a1 + b1))
                                    + list(range(off + a2, off + a2 + b2))
                                    + list(range(1 + a1 + b1, 1 + r1))
                                    + list(range(off + a2 + b2, off + r2))
                                )
                                term = np.transpose(prod, perm)
                                if a1 == 1 and a2 == 1:
                                    term = term + np.swapaxes(term, 1, 2)
                                if b1 == 1 and b2 == 1:
                                    term = term + np.swapaxes(term, 1 + a, 2 + a)
                                if c1 == 1 and c2 == 1:
                                    term = term + np.swapaxes(term, 1 + a + b, 2 + a + b)
                                acc += term
                    out[(a, b, c)] = acc
        return out

    M = single_col(0)
    for k in range(1, K):
        M = convolve(M, single_col(k))

    adj_map = np.zeros((2, 2, 3))
    adj_map[0, 0, 2] = 1.0
    adj_map[0, 1, 1] = -1.0
    adj_map[1, 0, 1] = -1.0
    adj_map[1, 1, 0] = 1.0

    MAS = M[(1, 0, 1)].reshape(B, 2, 2, 3)
    E1 = np.einsum("bijc,jkc,k->bi", MAS, adj_map, u, optimize=True)
    R_uu = Rc + np.outer(u, u)
    MAASS = M[(2, 0, 2)].reshape(B, 2, 2, 2, 2, 3, 3)
    E2 = np.einsum("bijnmcd,jkc,kl,lmd->bin", MAASS, adj_map, R_uu, adj_map, optimize=True)

    if has_z:
        MAqS = M[(1, 1, 1)].reshape(B, 2, 2, 2, 3)
        E1 = E1 - np.einsum("bijkc,jkc->bi", MAqS, adj_map, optimize=True)
        MAAqSS = M[(2, 1, 2)].reshape(B, 2, 2, 2, 2, 2, 3, 3)
        E2_uq = np.einsum("bijnmlcd,jkc,k,lmd->bin", MAAqSS, adj_map, u, adj_map, optimize=True)
        E2_qu = np.einsum("bijnmkcd,jkc,l,lmd->bin", MAAqSS, adj_map, u, adj_map, optimize=True)
        MAAqqSS = M[(2, 2, 2)].reshape(B, 2, 2, 2, 2, 2, 2, 3, 3)
        E2_qq = np.einsum("bijnmklcd,jkc,lmd->bin", MAAqqSS, adj_map, adj_map, optimize=True)
        E2 = E2 - E2_uq - E2_qu + E2_qq
    return E1, E2


def rc2_matrix_laplace(
    P: np.ndarray, H: np.ndarray, m_i: np.ndarray, u: np.ndarray, Rc: np.ndarray, sigma_H: float, n_r: int = 16, n_th: int = 16, gamma2_factor: float = 1.0
) -> np.ndarray:
    """Exact 3D Matrix-Laplace integral (Claim C2) for r_c=2, general P > 0, K >= 4.
    Uses compactified trigonometric spectral coordinates:
      T = Q(theta) diag(t1, t2) Q(theta)^T, 0 < t2 < t1 < inf, theta in [0, pi),
      dT = (t1 - t2) dt1 dt2 dtheta,
      v1 = sin^2(a1), v2 = v1 * sin^2(a2), t_j = v_j / (2 * s_bar * (1 - v_j)).
    """
    K = P.shape[0]
    assert K >= 4 and H.shape == (2, K) and sigma_H > 0.0
    eigvals, eigvecs = np.linalg.eigh(P)
    assert np.all(eigvals > 0.0)
    P_sqrt = eigvecs @ np.diag(np.sqrt(eigvals)) @ eigvecs.T
    P_inv_sqrt = eigvecs @ np.diag(1.0 / np.sqrt(eigvals)) @ eigvecs.T
    s_k = (sigma_H**2) * eigvals
    s_bar = float(np.mean(s_k))
    Hbar = H @ P_sqrt @ eigvecs
    zbar = eigvecs.T @ (P_inv_sqrt @ m_i)
    c0 = H @ m_i - u

    xs, ws = np.polynomial.legendre.leggauss(n_r)
    alphas = 0.25 * math.pi * (xs + 1.0)
    walphas = 0.25 * math.pi * ws
    thetas = (np.arange(n_th) + 0.5) * (math.pi / n_th)
    w_th = math.pi / n_th
    c_th = np.cos(thetas)
    s_th = np.sin(thetas)
    c2_th = c_th * c_th
    s2_th = s_th * s_th
    cs_th = c_th * s_th

    int_E1 = np.zeros(2)
    int_E2 = np.zeros((2, 2))

    # For each i (a1), batch over (j, l) of size n_r * n_th
    a2_grid, th_idx_grid = np.meshgrid(np.arange(n_r), np.arange(n_th), indexing="ij")
    a2_idx = a2_grid.ravel()
    th_idx = th_idx_grid.ravel()
    B_sz = a2_idx.size

    sin2_a2 = np.sin(alphas[a2_idx]) ** 2
    dsin2_a2 = np.sin(2.0 * alphas[a2_idx])
    wa2_flat = walphas[a2_idx]
    c2_flat = c2_th[th_idx]
    s2_flat = s2_th[th_idx]
    cs_flat = cs_th[th_idx]

    for i in range(n_r):
        a1 = alphas[i]
        v1 = math.sin(a1) ** 2
        dv1 = math.sin(2.0 * a1)
        t1 = v1 / (2.0 * s_bar * (1.0 - v1))
        dt1 = dv1 / (2.0 * s_bar * (1.0 - v1) ** 2)

        v2 = v1 * sin2_a2
        dv2 = v1 * dsin2_a2
        t2 = v2 / (2.0 * s_bar * (1.0 - v2))
        dt2 = dv2 / (2.0 * s_bar * (1.0 - v2) ** 2)

        wt_dT = (walphas[i] * dt1) * (wa2_flat * dt2) * w_th * (t1 - t2)
        detT_sqrt = np.sqrt(t1 * t2)

        t00 = t1 * c2_flat + t2 * s2_flat
        t01 = (t1 - t2) * cs_flat
        t11 = t1 * s2_flat + t2 * c2_flat

        logZ = np.zeros(B_sz)
        mus = np.zeros((B_sz, K, 2))
        Sigs = np.zeros((B_sz, K, 2, 2))
        for k in range(K):
            sk = s_k[k]
            m00 = 1.0 + 2.0 * sk * t00
            m01 = 2.0 * sk * t01
            m11 = 1.0 + 2.0 * sk * t11
            detM = m00 * m11 - m01 * m01
            inv00 = m11 / detM
            inv01 = -m01 / detM
            inv11 = m00 / detM
            hk0, hk1 = Hbar[0, k], Hbar[1, k]
            mu0 = inv00 * hk0 + inv01 * hk1
            mu1 = inv01 * hk0 + inv11 * hk1
            q_val = hk0 * (t00 * mu0 + t01 * mu1) + hk1 * (t01 * mu0 + t11 * mu1)
            logZ += -0.5 * np.log(detM) - q_val
            mus[:, k, 0] = mu0
            mus[:, k, 1] = mu1
            Sigs[:, k, 0, 0] = sk * inv00
            Sigs[:, k, 0, 1] = sk * inv01
            Sigs[:, k, 1, 0] = sk * inv01
            Sigs[:, k, 1, 1] = sk * inv11

        Z = np.exp(logZ)
        E1_T, E2_T = exact_ET_rc2_batch(Hbar, zbar, u, Rc, mus, Sigs)
        # m1=1: (det T)^(-1/2) / Gamma_2(1) = 1 / (pi * sqrt(det T))
        # m2=2: (det T)^(+1/2) / Gamma_2(2) = 2 * sqrt(det T) / pi
        w1 = wt_dT * (1.0 / (math.pi * detT_sqrt)) * Z
        w2 = wt_dT * (2.0 * detT_sqrt / (math.pi * gamma2_factor)) * Z
        int_E1 += np.einsum("b,bi->i", w1, E1_T)
        int_E2 += np.einsum("b,bij->ij", w2, E2_T)

    return np.outer(c0, c0) + np.outer(c0, int_E1) + np.outer(int_E1, c0) + int_E2


def mc_direct(P: np.ndarray, H: np.ndarray, m_i: np.ndarray, u: np.ndarray, Rc: np.ndarray, sigma_H: float, n_draws: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Brute-force MC directly from definitions (nu integrated analytically in closed form)."""
    rc, K = H.shape
    W = rng.standard_normal((n_draws, rc, K))
    Hhat = H[None, :, :] + sigma_H * W
    HhatP = np.einsum("mik,kl->mil", Hhat, P)
    S = np.einsum("mik,mjk->mij", HhatP, Hhat)
    S_inv = np.linalg.inv(S)
    O = np.einsum("mki,mij->mkj", HhatP.transpose(0, 2, 1), S_inv)
    HO = np.einsum("ij,mjk->mik", H, O)
    Hhat_m = np.einsum("mik,k->mi", Hhat, m_i)
    psi0 = (H @ m_i - u)[None, :] + np.einsum("mij,mj->mi", HO, u[None, :] - Hhat_m)
    samples = psi0[:, :, None] * psi0[:, None, :] + np.einsum("mij,jk,mlk->mil", HO, Rc, HO)
    mean = np.mean(samples, axis=0)
    se = np.std(samples, axis=0, ddof=1) / math.sqrt(n_draws)
    return mean, se


def run_check_1_conventions() -> None:
    print("=== CHECK 1: Convention lock test values ===")
    g2_1 = math.sqrt(math.pi) * math.gamma(1.0) * math.gamma(0.5)
    g2_2 = math.sqrt(math.pi) * math.gamma(2.0) * math.gamma(1.5)
    assert abs(g2_1 - math.pi) < 1e-15
    assert abs(g2_2 - 0.5 * math.pi) < 1e-15
    f1_1 = f_alpha(1.0, 1.0)
    f05_1 = f_alpha(0.5, 1.0)
    assert abs(f1_1 - (1.0 - math.exp(-1.0))) < 1e-15
    assert abs(f05_1 - 2.0 * float(special.dawsn(1.0))) < 1e-15
    # Verify prop:lrn-understanding-expansion bracket at r_c=1, P=pI, K=4: R_c coeff = 5-2K = -3
    B = prop_expansion_bracket(2.5 * np.eye(4), np.array([[1.0, 0.0, 0.0, 0.0]]), np.zeros(4), np.zeros(1), np.array([[1.0]]))
    assert abs(B[0, 0] - (-3.0)) < 1e-15
    print(f"  PASS: Gamma_2(1)={g2_1:.12f}, Gamma_2(2)={g2_2:.12f}, f_1(1)={f1_1:.12f}, f_1/2(1)={f05_1:.12f}, B_Rc(K=4)={B[0,0]:.1f}")


def run_check_2_stein_C1() -> None:
    print("\n=== CHECK 2 (Claim C1): Exact general-P Stein identity & non-perturbative E[psi psi^T] ===")
    # Held-out generic non-diagonal anisotropic instance (K=6, r_c=2, d=5 => finite 4th moment)
    K, rc = 6, 2
    H = np.array([[0.9, -0.7, 0.4, 1.1, -0.3, 0.6], [-0.5, 0.8, 1.2, -0.4, 0.7, -0.2]])
    L = np.array([
        [1.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.3, 0.9, 0.0, 0.0, 0.0, 0.0],
        [-0.2, 0.4, 1.4, 0.0, 0.0, 0.0],
        [0.1, -0.3, 0.2, 0.8, 0.0, 0.0],
        [0.2, 0.1, -0.2, 0.3, 1.3, 0.0],
        [-0.1, 0.2, 0.1, -0.2, 0.2, 1.0],
    ])
    P = L @ L.T
    m_i = np.array([0.4, -0.8, 0.5, 0.7, -0.6, 0.3])
    u = np.array([-0.6, 0.9])
    Rc = np.array([[0.35, -0.09], [-0.09, 0.28]])
    sigma_H = 0.6

    n_draws = 250000
    W = RNG.standard_normal((n_draws, rc, K))
    Hhat = H[None, :, :] + sigma_H * W
    HhatP = np.einsum("mik,kl->mil", Hhat, P)
    S = np.einsum("mik,mjk->mij", HhatP, Hhat)
    S_inv = np.linalg.inv(S)
    O = np.einsum("mki,mij->mkj", HhatP.transpose(0, 2, 1), S_inv)
    HO = np.einsum("ij,mjk->mik", H, O)
    trP_plus = float(np.trace(P)) - np.einsum("mkj,mjk->m", O, HhatP)
    OTO = np.einsum("mki,mkj->mij", O, O)

    lhs_samples = np.eye(rc)[None, :, :] - HO
    rhs_samples = (sigma_H**2) * (trP_plus[:, None, None] * S_inv - OTO)
    diff_samples = lhs_samples - rhs_samples
    diff_mean = np.mean(diff_samples, axis=0)
    diff_se = np.std(diff_samples, axis=0, ddof=1) / math.sqrt(n_draws)
    max_z = float(np.max(np.abs(diff_mean / diff_se)))
    sym_gap = float(np.max(np.abs(np.mean(HO, axis=0) - np.mean(HO, axis=0).T)))
    assert max_z < 3.5, f"Stein identity failed: max_z={max_z}"

    # Full Stein representation vs direct E[psi psi^T]
    Hhat_m = np.einsum("mik,k->mi", Hhat, m_i)
    mhat0 = m_i[None, :] + np.einsum("mki,mi->mk", O, u[None, :] - Hhat_m)
    psi0 = np.einsum("ik,mk->mi", H, mhat0) - u[None, :]
    direct_s = psi0[:, :, None] * psi0[:, None, :] + np.einsum("mij,jk,mlk->mil", HO, Rc, HO)
    Wm0 = np.einsum("mik,mk->mi", W, mhat0)
    WO = np.einsum("mik,mkj->mij", W, O)
    Wm_s = Wm0[:, :, None] * Wm0[:, None, :] + np.einsum("mij,jk,mlk->mil", WO, Rc, WO)
    RcSinv = np.einsum("ij,mjk->mik", Rc, S_inv)
    RcOTO = np.einsum("ij,mjk->mik", Rc, OTO)
    stein_s = Rc[None, :, :] + (sigma_H**2) * (
        Wm_s - trP_plus[:, None, None] * (RcSinv + RcSinv.transpose(0, 2, 1)) + (RcOTO + RcOTO.transpose(0, 2, 1))
    )
    full_diff = direct_s - stein_s
    full_z = float(np.max(np.abs(np.mean(full_diff, axis=0) / (np.std(full_diff, axis=0, ddof=1) / math.sqrt(n_draws)))))
    assert full_z < 3.5, f"Full Stein representation failed: full_z={full_z}"

    # Planted-error negative control: flip -O^T O to +O^T O
    wrong_rhs = (sigma_H**2) * (trP_plus[:, None, None] * S_inv + OTO)
    wrong_gap = float(np.max(np.abs(np.mean(lhs_samples - wrong_rhs, axis=0))))
    assert wrong_gap > 0.05, f"Negative control failed to separate: {wrong_gap}"
    print(f"  PASS: Stein identity max |z|={max_z:.2f}, max |E[HO]-E[HO]^T|={sym_gap:.2e}, full E[psi psi^T] Stein max |z|={full_z:.2f}")
    print(f"  NEG-CTRL PASS (flipped sign of O^T O): max entry gap={wrong_gap:.4f} > 0.05")


def run_check_3_matrix_laplace_C2() -> None:
    print("\n=== CHECK 3 (Claim C2): Full r_c=2 Matrix-Laplace integral (general anisotropic P) ===")
    # Instance A: K=6, r_c=2 (d=5, finite 4th moment -> valid CLT SEs), held-out generic anisotropic P
    K, rc = 6, 2
    H = np.array([[0.9, -0.7, 0.4, 1.1, -0.3, 0.6], [-0.5, 0.8, 1.2, -0.4, 0.7, -0.2]])
    L = np.array([
        [1.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.3, 0.9, 0.0, 0.0, 0.0, 0.0],
        [-0.2, 0.4, 1.4, 0.0, 0.0, 0.0],
        [0.1, -0.3, 0.2, 0.8, 0.0, 0.0],
        [0.2, 0.1, -0.2, 0.3, 1.3, 0.0],
        [-0.1, 0.2, 0.1, -0.2, 0.2, 1.0],
    ])
    P = L @ L.T
    m_i = np.array([0.4, -0.8, 0.5, 0.7, -0.6, 0.3])
    u = np.array([-0.6, 0.9])
    Rc = np.array([[0.35, -0.09], [-0.09, 0.28]])
    sigma_H = 0.6

    E_lap_16 = rc2_matrix_laplace(P, H, m_i, u, Rc, sigma_H, n_r=14, n_th=14)
    E_lap_20 = rc2_matrix_laplace(P, H, m_i, u, Rc, sigma_H, n_r=18, n_th=18)
    quad_conv = float(np.max(np.abs(E_lap_20 - E_lap_16)))
    E_mc, se_mc = mc_direct(P, H, m_i, u, Rc, sigma_H, n_draws=300000, rng=RNG)
    max_z = float(np.max(np.abs((E_mc - E_lap_20) / se_mc)))
    assert quad_conv < 1e-6, f"Quadrature did not converge: {quad_conv}"
    assert max_z < 3.5, f"Matrix-Laplace vs MC mismatch: max_z={max_z}"

    # Instance B: Edge case K=4, r_c=2 (K = r_c + 2, d=3)
    H4 = H[:, :4]
    P4 = P[:4, :4]
    m4 = m_i[:4]
    E4_lap_16 = rc2_matrix_laplace(P4, H4, m4, u, Rc, sigma_H=0.65, n_r=14, n_th=14)
    E4_lap_20 = rc2_matrix_laplace(P4, H4, m4, u, Rc, sigma_H=0.65, n_r=18, n_th=18)
    E4_mc, _ = mc_direct(P4, H4, m4, u, Rc, sigma_H=0.65, n_draws=300000, rng=RNG)
    edge_rel = float(np.max(np.abs(E4_mc - E4_lap_20)) / np.max(np.abs(E4_lap_20)))
    assert edge_rel < 0.03, f"Edge K=4, r_c=2 mismatch: rel={edge_rel}"

    # Planted-error negative control: drop factor of 2 in Gamma_2(2) = pi/2 -> pi
    E_wrong = rc2_matrix_laplace(P, H, m_i, u, Rc, sigma_H, n_r=14, n_th=14, gamma2_factor=2.0)
    wrong_gap = float(np.max(np.abs(E_wrong - E_lap_20)))
    assert wrong_gap > 0.2, f"Negative control failed: {wrong_gap}"
    print(f"  PASS (K=6, r_c=2): quad conv (14 vs 18)={quad_conv:.2e}, max |z| vs MC={max_z:.2f}")
    print(f"    Matrix-Laplace = {np.round(E_lap_20, 6).tolist()}")
    print(f"    Monte Carlo    = {np.round(E_mc, 6).tolist()} (se <= {float(np.max(se_mc)):.4e})")
    print(f"  PASS (edge K=4, r_c=2): quad conv={float(np.max(np.abs(E4_lap_20 - E4_lap_16))):.2e}, rel diff vs MC={edge_rel:.4f}")
    print(f"    Matrix-Laplace = {np.round(E4_lap_20, 6).tolist()}, MC = {np.round(E4_mc, 6).tolist()}")
    print(f"  NEG-CTRL PASS (Gamma_2(2) wrong by 2x): max entry gap={wrong_gap:.4f} > 0.2")


def run_check_4_rc1_C3() -> None:
    print("\n=== CHECK 4 (Claim C3): Exact r_c=1 closed forms (isotropic 1F1/elementary & anisotropic 1D Schwinger) ===")
    # Part A: Isotropic P = p*I_K for K = 3 (edge, Dawson), 4 (elementary), 5 (odd), 6 (even)
    for K in [3, 4, 5, 6]:
        H = np.array([[(1.1 - 0.25 * k) * ((-1) ** k) for k in range(K)]])
        p = 1.9
        P = p * np.eye(K)
        m_i = np.array([0.6 - 0.3 * k for k in range(K)])
        u0, Rc0, sigma_H = -0.75, 0.42, 0.58
        val_closed = rc1_isotropic_closed(K, H, m_i, u0, Rc0, sigma_H)
        val_quad, q_err = rc1_schwinger_1d(P, H, m_i, u0, Rc0, sigma_H)
        diff = abs(val_closed - val_quad)
        assert diff < 1e-12, f"K={K} closed vs Schwinger mismatch: {diff}"

        # Check explicit K=3 Dawson and K=4 elementary specialization formulas directly
        lam = float(np.sum(H**2)) / (2.0 * sigma_H**2)
        if K == 3:
            cR_dawson = 1.0 - float(special.dawsn(math.sqrt(lam))) / math.sqrt(lam)
            cu_dawson = float(special.dawsn(math.sqrt(lam))) / math.sqrt(lam)
            assert abs(cR_dawson + cu_dawson - 1.0) < 1e-15
            v_pure_Rc = rc1_isotropic_closed(3, H, np.zeros(3), 0.0, Rc0, sigma_H)
            assert abs(v_pure_Rc - Rc0 * cR_dawson) < 1e-14
        if K == 4:
            cR_elem = 1.0 + 0.5 * math.exp(-lam) - 1.5 * (1.0 - math.exp(-lam)) / lam
            cu_elem = 0.5 * math.exp(-lam) + 0.5 * (1.0 - math.exp(-lam)) / lam
            v_pure = rc1_isotropic_closed(4, H, np.zeros(4), u0, Rc0, sigma_H)
            assert abs(v_pure - (Rc0 * cR_elem + u0**2 * cu_elem)) < 1e-14

        extra = ""
        if K >= 5:
            mc_m, mc_se = mc_direct(P, H, m_i, np.array([u0]), np.array([[Rc0]]), sigma_H, n_draws=250000, rng=RNG)
            z = float((mc_m[0, 0] - val_closed) / mc_se[0, 0])
            assert abs(z) < 3.5, f"K={K} MC z={z}"
            extra = f", MC={mc_m[0,0]:.6f}+/-{mc_se[0,0]:.4e} (z={z:+.2f})"
        print(f"  PASS (isotropic K={K}): closed={val_closed:.12f}, Schwinger={val_quad:.12f}, diff={diff:.2e}{extra}")

    # Part B: General anisotropic P > 0 at K=3 (edge) and K=5 (finite 4th moment)
    for K in [3, 5]:
        H = np.array([[0.8, -0.5, 1.2, -0.4, 0.7][:K]])
        A = np.diag(np.linspace(0.7, 2.1, K)) + 0.25 * np.eye(K, k=1)
        P = A @ A.T
        m_i = np.array([0.7, -0.5, 0.9, -0.3, 0.4][:K])
        u0, Rc0, sigma_H = 0.65, 0.35, 0.55
        val_quad, q_err = rc1_schwinger_1d(P, H, m_i, u0, Rc0, sigma_H)
        val_wrong_iso = rc1_isotropic_closed(K, H, m_i, u0, Rc0, sigma_H)
        assert abs(val_quad - val_wrong_iso) > 0.02, "Anisotropic instance did not separate from isotropic formula"
        mc_m, mc_se = mc_direct(P, H, m_i, np.array([u0]), np.array([[Rc0]]), sigma_H, n_draws=250000, rng=RNG)
        if K == 5:
            z = float((mc_m[0, 0] - val_quad) / mc_se[0, 0])
            assert abs(z) < 3.5
            print(f"  PASS (anisotropic K=5): Schwinger={val_quad:.8f} (err={q_err:.1e}), MC={mc_m[0,0]:.8f}+/-{mc_se[0,0]:.4e} (z={z:+.2f}), iso_wrong={val_wrong_iso:.6f}")
        else:
            rel = abs(mc_m[0, 0] - val_quad) / val_quad
            assert rel < 0.03
            print(f"  PASS (anisotropic edge K=3): Schwinger={val_quad:.8f} (err={q_err:.1e}), MC={mc_m[0,0]:.8f} (rel={rel:.4f}), iso_wrong={val_wrong_iso:.6f}")

    # Planted-error negative control: flip sign of c_{par,u} at K=4
    H4 = np.array([[1.1, -0.85, 0.6, -0.35]])
    m4 = np.array([0.6, 0.3, 0.0, -0.3])
    val_true = rc1_isotropic_closed(4, H4, m4, -0.75, 0.42, 0.58)
    lam = float(np.sum(H4**2)) / (2.0 * 0.58**2)
    f0 = f_alpha(1.0, lam)
    f1 = (1.0 - f0) / lam
    c_par_u = 0.25 * 3 * 2 * (f1 - f0)
    Hm = float(H4[0] @ m4)
    val_flipped = val_true - 4.0 * c_par_u * Hm * (-0.75)
    assert abs(val_flipped - val_true) > 0.01
    print(f"  NEG-CTRL PASS (flipped c_par_u sign at K=4): gap={abs(val_flipped - val_true):.5f} > 0.01")


def run_check_5_obstructions_C4() -> None:
    print("\n=== CHECK 5 (Claim C4): Exact r_c=2 K=4 Shi(lam) identity & Carlson elliptic integral ===")
    # Part A: E[(GG^T)^-1]_11 for r_c=2, K=4, Omega = 2*lam*I_2
    for lam in [0.3, 1.0, 1.7, 3.5]:
        shi, _ = special.shichi(lam)
        val_shi = (1.0 - math.exp(-2.0 * lam)) / (4.0 * lam) + ((1.0 + lam) / (2.0 * lam)) * math.exp(-lam) * float(shi)
        # Independent channel: Schur Poisson-2F2 series
        val_schur = 0.0
        for n2 in range(120):
            w2 = math.exp(-lam + n2 * math.log(lam) - math.lgamma(n2 + 1))
            if w2 < 1e-18:
                continue
            a, b, c = 1.5 + n2, 1.5, 2.0 + n2
            t, s = 1.0, 1.0
            for n1 in range(1, 120):
                t *= (-lam) * (a + n1 - 1.0) / ((b + n1 - 1.0) * (c + n1 - 1.0))
                s += t
                if abs(t) < 1e-16:
                    break
            val_schur += w2 * s
        diff = abs(val_shi - val_schur)
        assert diff < 1e-14, f"Shi vs Schur mismatch at lam={lam}: {diff}"
        print(f"  PASS (r_c=2, K=4, lam={lam}): Shi={val_shi:.15f}, Schur={val_schur:.15f}, diff={diff:.2e}")

    # Third independent channel at lam=1.7: verify M(e1,0)+M(e2,0)-M(0,I2) = I2 - 2 E[HO] = (2*val_shi - 1)*I2 via Matrix-Laplace!
    lam = 1.7
    sigma_H = 1.0
    s_val = math.sqrt(2.0 * lam)
    H = np.array([[s_val, 0.0, 0.0, 0.0], [0.0, s_val, 0.0, 0.0]])
    P = np.eye(4)
    z0 = np.zeros(4)
    M_e1 = rc2_matrix_laplace(P, H, z0, np.array([1.0, 0.0]), np.zeros((2, 2)), sigma_H, n_r=18, n_th=16)
    M_e2 = rc2_matrix_laplace(P, H, z0, np.array([0.0, 1.0]), np.zeros((2, 2)), sigma_H, n_r=18, n_th=16)
    M_I2 = rc2_matrix_laplace(P, H, z0, np.zeros(2), np.eye(2), sigma_H, n_r=18, n_th=16)
    diff_comb = M_e1 + M_e2 - M_I2
    shi, _ = special.shichi(lam)
    gamma_lam = (1.0 - math.exp(-2.0 * lam)) / (4.0 * lam) + ((1.0 + lam) / (2.0 * lam)) * math.exp(-lam) * float(shi)
    expected_comb = (2.0 * gamma_lam - 1.0) * np.eye(2)
    comb_err = float(np.max(np.abs(diff_comb - expected_comb)))
    assert comb_err < 1e-8, f"Linear combination identity failed: {comb_err}"
    print(f"  PASS (3rd channel, Matrix-Laplace linear-combination identity at lam=1.7): max diff={comb_err:.2e}")

    # Planted-error negative control: replace Shi(lam) with sinh(lam)/lam
    wrong_shi = (1.0 - math.exp(-2.0 * lam)) / (4.0 * lam) + ((1.0 + lam) / (2.0 * lam)) * math.exp(-lam) * (math.sinh(lam) / lam)
    assert abs(wrong_shi - gamma_lam) > 0.05
    print(f"  NEG-CTRL PASS (Shi -> sinh/lam): gap={abs(wrong_shi - gamma_lam):.5f} > 0.05")

    # Part B: Carlson elliptic integral at r_c=1, K=3, sigma_H -> inf, anisotropic P = diag(p1, p2, p3)
    for (p1, p2, p3) in [(1.7, 0.9, 2.5), (1.0, 0.3, 4.0), (2.0, 2.0, 2.0)]:
        val_int, _ = integrate.quad(
            lambda t: (p1**2) * t / (((1.0 + 2.0 * t * p1) ** 1.5) * math.sqrt((1.0 + 2.0 * t * p2) * (1.0 + 2.0 * t * p3))),
            0.0,
            np.inf,
            epsabs=1e-13,
            epsrel=1e-13,
        )
        val_carlson = (0.5 / math.sqrt(p1 * p2 * p3)) * (
            p1 * float(special.elliprf(1.0 / p1, 1.0 / p2, 1.0 / p3)) - float(special.elliprd(1.0 / p2, 1.0 / p3, 1.0 / p1)) / 3.0
        )
        diff = abs(val_int - val_carlson)
        assert diff < 1e-13
        if p1 == p2 == p3:
            assert abs(val_carlson - 1.0 / 3.0) < 1e-14
        print(f"  PASS (Carlson elliptic P=diag({p1},{p2},{p3})): int={val_int:.14f}, Carlson={val_carlson:.14f}, diff={diff:.2e}")


def run_check_6_asymptotics_and_divergence_C5() -> None:
    print("\n=== CHECK 6 (Claim C5): sigma_H->0 vs prop:lrn-understanding-expansion, sigma_H->inf, K<=r_c+1 divergence ===")
    # Part A: sigma_H -> 0 (exact vs prop:lrn-understanding-expansion AND exact sigma_H^4 coefficient)
    for K in [3, 4, 5]:
        H = np.array([[1.2, -0.6, 0.8, -0.4, 0.5][:K]])
        P = 1.5 * np.eye(K)
        m_i = np.array([0.7, -0.5, 0.9, -0.3, 0.6][:K])
        u0, Rc0 = 0.85, 0.35
        B = prop_expansion_bracket(P, H, m_i, np.array([u0]), np.array([[Rc0]]))[0, 0]
        H_sq = float(np.sum(H**2))
        Hm = float(H[0] @ m_i)
        m_perp_sq = float(np.dot(m_i, m_i) - (Hm**2) / H_sq)
        # Exact sigma_H^4 coefficient from symbolic expansion
        c4_exact = (
            (K - 4) * (3 * K - 8) * Rc0
            + ((K - 4) ** 2) * (u0**2)
            + (K**2 - 1) * (Hm**2)
            - (2 * K - 1) * H_sq * m_perp_sq
            - 2.0 * (K - 1) * (K - 2) * Hm * u0
        ) / (H_sq**2)

        rems = []
        for sH in [0.04, 0.02, 0.01]:
            ex = rc1_isotropic_closed(K, H, m_i, u0, Rc0, sH)
            rem = ex - (Rc0 + (sH**2) * B)
            rems.append(rem)
        ratio_4_2 = rems[0] / rems[1]
        ratio_2_1 = rems[1] / rems[2]
        c4_num = rems[2] / (0.01**4)
        rel_c4 = abs(c4_num - c4_exact) / abs(c4_exact)
        assert abs(ratio_2_1 - 16.0) < 0.2, f"Remainder not O(sigma_H^4): ratio={ratio_2_1}"
        assert rel_c4 < 1e-3, f"sigma_H^4 coeff mismatch: {c4_num} vs {c4_exact}"
        print(f"  PASS (sigma_H->0, iso K={K}): rem ratios={ratio_4_2:.3f}, {ratio_2_1:.3f} (vs 16), c4_num={c4_num:.6f} vs exact={c4_exact:.6f} (rel={rel_c4:.2e})")

    # Anisotropic P > 0 at K=3: Schwinger 1D vs prop:lrn-understanding-expansion
    H3 = np.array([[1.1, -0.6, 0.8]])
    A3 = np.array([[1.2, 0.3, -0.2], [0.3, 0.7, 0.4], [-0.2, 0.4, 2.1]])
    P3 = A3 @ A3.T
    m3 = np.array([0.7, -0.4, 0.9])
    u3, Rc3 = 0.85, 0.30
    B3 = prop_expansion_bracket(P3, H3, m3, np.array([u3]), np.array([[Rc3]]))[0, 0]
    rems_aniso = [rc1_schwinger_1d(P3, H3, m3, u3, Rc3, sH)[0] - (Rc3 + (sH**2) * B3) for sH in [0.04, 0.02, 0.01]]
    ratio_aniso = rems_aniso[1] / rems_aniso[2]
    assert abs(ratio_aniso - 16.0) < 0.2
    # Negative control: drop noise-correlation terms -> only first term E||mhat0||^2
    S0 = H3 @ P3 @ H3.T
    O0 = P3 @ H3.T @ np.linalg.inv(S0)
    mbar0 = m3 + O0 @ (np.array([u3]) - H3 @ m3)
    B3_wrong = float(np.dot(mbar0, mbar0) + np.trace(O0 @ np.array([[Rc3]]) @ O0.T))
    rems_wrong = [rc1_schwinger_1d(P3, H3, m3, u3, Rc3, sH)[0] - (Rc3 + (sH**2) * B3_wrong) for sH in [0.04, 0.02, 0.01]]
    ratio_wrong = rems_wrong[1] / rems_wrong[2]
    assert abs(ratio_wrong - 4.0) < 0.2, f"Neg-ctrl ratio expected ~4, got {ratio_wrong}"
    print(f"  PASS (sigma_H->0, aniso K=3): rem ratio={ratio_aniso:.3f} (vs 16)")
    print(f"  NEG-CTRL PASS (drop noise-corr terms): rem ratio={ratio_wrong:.3f} (~4, O(sigma_H^2) residual!)")

    # Moderate sigma_H comparison: exact vs prop:lrn-understanding-expansion vs eq:lrn-understanding-bound
    print("  Moderate-sigma_H comparison (anisotropic K=3, r_c=1):")
    eigP = np.linalg.eigvalsh(P3)
    kappaP = float(eigP[-1] / eigP[0])
    H3_sq = float(np.sum(H3**2))
    m3_sq = float(np.sum(m3**2))
    for sH in [0.2, 0.5, 1.0, 2.0]:
        ex, _ = rc1_schwinger_1d(P3, H3, m3, u3, Rc3, sH)
        exp2 = Rc3 + (sH**2) * B3
        bnd = 3.0 * H3_sq * kappaP * (m3_sq + (u3**2 + Rc3) / ((sH**2) * (3 - 1 - 1))) + 3.0 * (u3**2)
        print(f"    sigma_H={sH:.1f}: exact={ex:.6f}, 2nd-order={exp2:.6f}, bound={bnd:.2f}")

    # Part B: sigma_H -> inf exact limit & O(sigma_H^-2) noise term at (K=6, r_c=2, P=I)
    K, rc = 6, 2
    H6 = np.array([[0.9, -0.7, 0.4, 1.1, -0.3, 0.6], [-0.5, 0.8, 1.2, -0.4, 0.7, -0.2]])
    m6 = np.array([0.4, -0.8, 0.5, 0.7, -0.6, 0.3])
    u6 = np.array([-0.6, 0.9])
    Rc6 = np.array([[0.35, -0.09], [-0.09, 0.28]])
    n = K - rc
    Hm6 = H6 @ m6
    E_inf = (
        np.outer(u6, u6)
        - (n / K) * (np.outer(Hm6, u6) + np.outer(u6, Hm6))
        + (n * rc / (K * (K - 1) * (K + 2))) * float(np.dot(m6, m6)) * (H6 @ H6.T)
        + (n * ((n + 1) * K - 2) / (K * (K - 1) * (K + 2))) * np.outer(Hm6, Hm6)
    )
    E_big, se_big = mc_direct(np.eye(K), H6, m6, u6, Rc6, sigma_H=300.0, n_draws=300000, rng=RNG)
    z_inf = float(np.max(np.abs((E_big - E_inf) / se_big)))
    assert z_inf < 3.5
    # Noise leading term at m=0, u=0, sigma_H=30
    s_big = 30.0
    E_noise_mc, se_noise = mc_direct(np.eye(K), H6, np.zeros(K), np.zeros(rc), Rc6, sigma_H=s_big, n_draws=300000, rng=RNG)
    E_noise_lead = (float(np.trace(Rc6)) / ((s_big**2) * K * (K - rc - 1))) * (H6 @ H6.T)
    rel_noise = float(np.max(np.abs(E_noise_mc - E_noise_lead)) / np.max(np.abs(E_noise_lead)))
    assert rel_noise < 0.02
    print(f"  PASS (sigma_H->inf, K=6, r_c=2, P=I): limit max |z|={z_inf:.2f}; O(sigma_H^-2) noise rel diff={rel_noise:.4f}")

    # Part C: K <= r_c + 1 divergence (K=2, r_c=1) vs y=0 finiteness
    H2 = np.array([[1.2, -0.7]])
    P2 = np.array([[1.5, 0.3], [0.3, 0.9]])
    m2 = np.array([0.8, -0.5])
    sigma2 = 0.6
    eig2, vec2 = np.linalg.eigh(P2)
    s2 = (sigma2**2) * eig2
    h2 = vec2.T @ (vec2 @ np.diag(np.sqrt(eig2)) @ vec2.T @ H2[0])
    z2 = vec2.T @ (vec2 @ np.diag(1.0 / np.sqrt(eig2)) @ vec2.T @ m2)

    def schwinger_integrand_k2(t: float, u0: float, Rc0: float) -> float:
        inv_d = 1.0 / (1.0 + 2.0 * t * s2)
        Z = float(np.prod(np.sqrt(inv_d)) * math.exp(-t * float(np.sum((h2**2) * inv_d))))
        mu_t = h2 * inv_d
        sig_t = s2 * inv_d
        mX = float(np.sum(h2 * mu_t))
        mY = float(np.sum(z2 * mu_t))
        vXX = float(np.sum((h2**2) * sig_t))
        vXY = float(np.sum(h2 * z2 * sig_t))
        vYY = float(np.sum((z2**2) * sig_t))
        c0 = float(H2[0] @ m2 - u0)
        EX, EXY = mX, mX * mY + vXY
        EX2 = mX**2 + vXX
        EX2Y = (mX**2) * mY + vXX * mY + 2.0 * mX * vXY
        EX2Y2 = (mX**2 + vXX) * (mY**2 + vYY) + 2.0 * (vXY**2) + 4.0 * mX * mY * vXY
        return Z * (2.0 * c0 * (u0 * EX - EXY) + t * ((u0**2 + Rc0) * EX2 - 2.0 * u0 * EX2Y + EX2Y2))

    # Asymptotic tail t * integrand(t) -> (u0^2 + Rc0) * ||h2||^2 * exp(-0.5 * sum(h2^2/s2)) / (4 * sqrt(s2[0]*s2[1])) > 0
    asymp_coeff = (0.5**2 + 0.3) * float(np.sum(h2**2)) * math.exp(-0.5 * float(np.sum((h2**2) / s2))) / (4.0 * math.sqrt(s2[0] * s2[1]))
    tail_val = 1e6 * schwinger_integrand_k2(1e6, 0.5, 0.3)
    assert abs(tail_val - asymp_coeff) / asymp_coeff < 1e-4
    # When y = 0 identically (u0=0, Rc0=0), integral converges and matches MC!
    q_y0, _ = integrate.quad(lambda t: schwinger_integrand_k2(t, 0.0, 0.0), 0.0, np.inf, epsabs=1e-12, epsrel=1e-12)
    ex_y0 = float((H2[0] @ m2) ** 2) + q_y0
    mc_y0, se_y0 = mc_direct(P2, H2, m2, np.zeros(1), np.zeros((1, 1)), sigma2, n_draws=200000, rng=RNG)
    z_y0 = float((mc_y0[0, 0] - ex_y0) / se_y0[0, 0])
    assert abs(z_y0) < 3.5
    print(f"  PASS (K=2, r_c=1 divergence): t*integrand(1e6)={tail_val:.8f} vs exact log-pole coeff={asymp_coeff:.8f} (1/t divergence)")
    print(f"  PASS (K=2, r_c=1, y=0 finite): Schwinger={ex_y0:.8f}, MC={mc_y0[0,0]:.8f}+/-{se_y0[0,0]:.4e} (z={z_y0:+.2f})")


if __name__ == "__main__":
    run_check_1_conventions()
    run_check_2_stein_C1()
    run_check_3_matrix_laplace_C2()
    run_check_4_rc1_C3()
    run_check_5_obstructions_C4()
    run_check_6_asymptotics_and_divergence_C5()
    print("\nALL 6 VERIFICATION CHECKS AND ALL NEGATIVE CONTROLS PASSED.")
