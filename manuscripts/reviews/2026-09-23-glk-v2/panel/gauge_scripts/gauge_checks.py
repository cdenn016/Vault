r"""Gauge-theory panel checks for GL(K)_attention_v2.tex (sha256 85b3918c...).

CPU-only numpy/scipy (float64). Every check prints a residual or a deliberately
nonzero change; results go to gauge_checks_results.json next to this script.

Conventions follow the manuscript: frames U_i: V -> E_i, reference moments
xi_i = U_i^{-1} mu_i, C_i = U_i^{-1} Sigma_i U_i^{-T}; passive site action
(mu, Sigma, U) -> (g mu, g Sigma g^T, g U); content link L_ij = U_i O T U_j^{-1};
routed link C_ij = U_i A_ij U_j^{-1}, A_ij = sum_h beta_ij^h O_h T_h.
"""
import itertools
import json
import os

import numpy as np
from scipy.linalg import expm, null_space, logm
from scipy.special import erf

rng = np.random.default_rng(20260923)
EPS = np.finfo(float).eps
R = {}


def rand_gl(K, scale=0.5):
    """Random nonorthogonal element of GL^+(K), moderately conditioned."""
    return expm(scale * rng.standard_normal((K, K)))


def rand_spd(K, floor=0.5):
    A = rng.standard_normal((K, K))
    return A @ A.T + floor * np.eye(K)


def blockdiag(*blocks):
    n = sum(b.shape[0] for b in blocks)
    out = np.zeros((n, n))
    s0 = 0
    for b in blocks:
        d = b.shape[0]
        out[s0:s0 + d, s0:s0 + d] = b
        s0 += d
    return out


def kl_gauss(m0, S0, m1, S1):
    """KL(N(m0,S0)||N(m1,S1)) = 1/2[tr(S1^-1 S0) + d^T S1^-1 d - r + ln|S1| - ln|S0|]."""
    r = len(m0)
    S1i = np.linalg.inv(S1)
    d = m1 - m0
    return 0.5 * (np.trace(S1i @ S0) + d @ S1i @ d - r
                  + np.linalg.slogdet(S1)[1] - np.linalg.slogdet(S0)[1])


def softmax(x):
    x = np.asarray(x, float)
    x = x - np.max(x[np.isfinite(x)])
    e = np.exp(x)
    return e / e.sum()


def attention(mu, Sig, U, SQ, SK, T, O, tau, logprior, causal=True):
    """One ideal full-Gaussian attention layer in the manuscript's form."""
    N, K = mu.shape
    H = SQ.shape[0]
    Ui = np.linalg.inv(U)
    xi = np.einsum("nab,nb->na", Ui, mu)
    C = Ui @ Sig @ np.transpose(Ui, (0, 2, 1))
    beta = np.zeros((H, N, N))
    D = np.full((H, N, N), np.nan)
    for h in range(H):
        for i in range(N):
            aq, VQ = SQ[h] @ xi[i], SQ[h] @ C[i] @ SQ[h].T
            logits = np.full(N, -np.inf)
            for j in range(N):
                if causal and j > i:
                    continue
                bk, VK = SK[h] @ xi[j], SK[h] @ C[j] @ SK[h].T
                D[h, i, j] = kl_gauss(aq, VQ, bk, VK)
                logits[j] = -D[h, i, j] / tau + logprior[h, i, j]
            beta[h, i] = softmax(logits)
    A = np.zeros((N, N, K, K))
    for h in range(H):
        A += beta[h][:, :, None, None] * (O[h] @ T[h])[None, None]
    Cl = np.einsum("iab,ijbc,jcd->ijad", U, A, np.linalg.inv(U))
    m = np.einsum("ijab,jb->ia", Cl, mu)
    return dict(beta=beta, D=D, m=m, xi=xi, C=C, A=A, Cl=Cl)


def rec(name, value, note=""):
    v = float(value) if np.ndim(value) == 0 else np.asarray(value).tolist()
    R[name] = {"value": v, "note": note}
    shown = ("%.3e" % v) if isinstance(v, float) else str(v)
    print("%-62s %12s  %s" % (name, shown, note))


# ---------------------------------------------------------------- setup
N, K, H, r, s = 5, 6, 2, 2, 2
tau = 1.3
mu = rng.standard_normal((N, K))
Sig = np.stack([rand_spd(K) for _ in range(N)])
U = np.stack([rand_gl(K) for _ in range(N)])
SQ = rng.standard_normal((H, r, K))
SK = rng.standard_normal((H, r, K))
T = rng.standard_normal((H, s, K))
O = rng.standard_normal((H, K, s))
alibi = np.array([[[-(0.5 ** (h + 1)) * (i - j) for j in range(N)] for i in range(N)]
                  for h in range(H)])
base = attention(mu, Sig, U, SQ, SK, T, O, tau, alibi)

print("== 1. passive site action (covariance proposition)")
g = np.stack([rand_gl(K, 0.8) for _ in range(N)])
gi = np.linalg.inv(g)
mu_p = np.einsum("nab,nb->na", g, mu)
Sig_p = g @ Sig @ np.transpose(g, (0, 2, 1))
U_p = g @ U
pas = attention(mu_p, Sig_p, U_p, SQ, SK, T, O, tau, alibi)
rec("1a_max_abs_dbeta_passive", np.max(np.abs(pas["beta"] - base["beta"])))
rec("1b_max_abs_message_law", np.max(np.abs(pas["m"] - np.einsum("nab,nb->na", g, base["m"]))))
rec("1c_max_abs_link_endpoint_law",
    np.max(np.abs(pas["Cl"] - np.einsum("iab,ijbc,jcd->ijad", g, base["Cl"], gi))))
rec("1d_max_cond_g", max(np.linalg.cond(x) for x in g), "nonorthogonal test elements")

print("== 2. unitary gauge g_i = U_i^{-1}: frame-free operator")
gu = np.linalg.inv(U)
uni = attention(np.einsum("nab,nb->na", gu, mu), gu @ Sig @ np.transpose(gu, (0, 2, 1)),
                gu @ U, SQ, SK, T, O, tau, alibi)
frame_free = np.einsum("ijab,jb->ia", base["A"], base["xi"])
rec("2a_max_abs_U_after_unitary_gauge_minus_I", np.max(np.abs(gu @ U - np.eye(K))))
rec("2b_max_abs_unitary_message_minus_frame_free", np.max(np.abs(uni["m"] - frame_free)))
rec("2c_max_abs_dbeta_unitary", np.max(np.abs(uni["beta"] - base["beta"])))
Omega = np.einsum("iab,jbc->ijac", U, np.linalg.inv(U))
dressed = np.einsum("iab,ijbc,jcd->ijad", np.linalg.inv(U), Omega, U)
rec("2d_max_abs_dressed_Omega_minus_I", np.max(np.abs(dressed - np.eye(K))),
    "U_i^-1 Omega_ij U_j = I (pure gauge)")

print("== 3. principal right action on the sections alone is NOT a symmetry")
k = np.stack([rand_gl(K, 0.5) for _ in range(N)])
right = attention(mu, Sig, U @ k, SQ, SK, T, O, tau, alibi)
rec("3a_max_abs_dbeta_per_site_right_action", np.max(np.abs(right["beta"] - base["beta"])),
    "sigma_i -> sigma_i k_i, associated point fixed")
a = rand_gl(K, 0.5)
glob_nc = attention(mu, Sig, U @ a, SQ, SK, T, O, tau, alibi)
glob_c = attention(mu, Sig, U @ a, SQ @ a, SK @ a, T @ a, np.linalg.inv(a) @ O, tau, alibi)
rec("3b_max_abs_dbeta_global_right_uncompensated", np.max(np.abs(glob_nc["beta"] - base["beta"])))
rec("3c_max_abs_dbeta_global_right_compensated", np.max(np.abs(glob_c["beta"] - base["beta"])),
    "S,T,O co-transformed (line 386)")
rec("3d_max_abs_dm_global_right_compensated", np.max(np.abs(glob_c["m"] - base["m"])))

print("== 4. treatise typing: u_i = sigma_0 U_i^{-1}; right action on u_i = passive action")
N0 = rand_gl(K)
e = rng.standard_normal(K)
Ui0 = U[0]
u0 = N0 @ np.linalg.inv(Ui0)
mu_loc = np.linalg.solve(u0, e)
z = np.linalg.solve(N0, e)
rec("4a_ref_coords_equal_Uinv_mu", np.max(np.abs(z - np.linalg.solve(Ui0, mu_loc))))
aa = rand_gl(K, 0.6)
u0p = u0 @ aa
mu_locp = np.linalg.solve(u0p, e)
Ui0p = np.linalg.inv(np.linalg.solve(N0, u0p))
gpass = np.linalg.inv(aa)
rec("4b_mu_transforms_as_g_mu_with_g=a^-1", np.max(np.abs(mu_locp - gpass @ mu_loc)))
rec("4c_U_transforms_as_g_U_with_g=a^-1", np.max(np.abs(Ui0p - gpass @ Ui0)))

print("== 5. loop traces of routed links are frame-free words in the routing weights")
Nl = 4
bw = rng.uniform(0.05, 1.0, size=(H, Nl, Nl))
M = O @ T
Al = np.einsum("hij,hab->ijab", bw, M)
Ul = np.stack([rand_gl(K) for _ in range(Nl)])
Cl = np.einsum("iab,ijbc,jcd->ijad", Ul, Al, np.linalg.inv(Ul))
worst_frame, worst_poly = 0.0, 0.0
for L in (2, 3, 4):
    for walk in itertools.product(range(Nl), repeat=L):
        cyc = list(walk) + [walk[0]]
        edges = list(zip(cyc[:-1], cyc[1:]))
        P = np.eye(K)
        PA = np.eye(K)
        for (x, y) in edges:
            P = P @ Cl[x, y]
            PA = PA @ Al[x, y]
        poly = 0.0
        for word in itertools.product(range(H), repeat=L):
            coef = np.prod([bw[hh, x, y] for hh, (x, y) in zip(word, edges)])
            Mw = np.eye(K)
            for hh in word:
                Mw = Mw @ M[hh]
            poly += coef * np.trace(Mw)
        worst_frame = max(worst_frame, abs(np.trace(P) - np.trace(PA)) / max(1.0, abs(np.trace(PA))))
        worst_poly = max(worst_poly, abs(np.trace(PA) - poly) / max(1.0, abs(poly)))
rec("5a_max_rel_trace_framed_minus_frame_free", worst_frame)
rec("5b_max_rel_trace_minus_word_polynomial", worst_poly, "sum_words prod beta Tr(M...M)")
one = np.einsum("ij,ab->ijab", bw[0], M[0])
Cone = np.einsum("iab,ijbc,jcd->ijad", Ul, one, np.linalg.inv(Ul))
tri = np.trace(Cone[0, 1] @ Cone[1, 2] @ Cone[2, 0])
rec("5c_single_head_triangle_minus_weights_times_TrM3",
    abs(tri - bw[0, 0, 1] * bw[0, 1, 2] * bw[0, 2, 0] * np.trace(M[0] @ M[0] @ M[0])) / abs(tri))
Nd, count = 6, 0
for L in range(2, 6):
    for walk in itertools.product(range(Nd), repeat=L):
        cyc = list(walk) + [walk[0]]
        if all(y <= x for x, y in zip(cyc[:-1], cyc[1:])) and len(set(walk)) > 1:
            count += 1
rec("5d_causal_closed_walks_distinct_vertices_N6_len2to5", count, "only self-loop walks exist")

print("== 6. comparison-space GL(r) redundancy (lead L5)")
h0 = 0
Aco = rand_gl(r, 0.9)
x_i, C_i = base["xi"][3], base["C"][3]
x_j, C_j = base["xi"][1], base["C"][1]


def Dpair(Sq, Sk):
    return kl_gauss(Sq @ x_i, Sq @ C_i @ Sq.T, Sk @ x_j, Sk @ C_j @ Sk.T)


D0 = Dpair(SQ[h0], SK[h0])
rec("6a_KL_cogredient_ASQ_ASK_residual", abs(Dpair(Aco @ SQ[h0], Aco @ SK[h0]) - D0))
rec("6b_KL_dilation_cSQ_cSK_c37_residual", abs(Dpair(37 * SQ[h0], 37 * SK[h0]) - D0))
Ainvt = np.linalg.inv(Aco).T
rec("6c_KL_contragredient_change", abs(Dpair(Aco @ SQ[h0], Ainvt @ SK[h0]) - D0), "not a KL redundancy")
dot0 = (SQ[h0] @ x_i) @ (SK[h0] @ x_j)
rec("6d_dot_contragredient_residual", abs((Aco @ SQ[h0] @ x_i) @ (Ainvt @ SK[h0] @ x_j) - dot0))
rec("6e_dot_cogredient_change", abs((Aco @ SQ[h0] @ x_i) @ (Aco @ SK[h0] @ x_j) - dot0))
VQ, VK = SQ[h0] @ C_i @ SQ[h0].T, SK[h0] @ C_j @ SK[h0].T
VQa, VKa = Aco @ VQ @ Aco.T, Aco @ VK @ Aco.T
ge0 = np.sort(np.linalg.eigvals(np.linalg.solve(VK, VQ)).real)
ge1 = np.sort(np.linalg.eigvals(np.linalg.solve(VKa, VQa)).real)
rec("6f_generalized_eigs_VKinvVQ_residual", np.max(np.abs(ge0 - ge1)), "invariant datum")
rec("6g_cond_VK_before", np.linalg.cond(VK))
rec("6h_cond_VK_after_A", np.linalg.cond(VKa), "gauge-dependent")
rec("6i_sigma_min_SK_before", np.linalg.svd(SK[h0], compute_uv=False).min())
rec("6j_sigma_min_ASK_after", np.linalg.svd(Aco @ SK[h0], compute_uv=False).min(), "gauge-dependent")
w_, V_ = np.linalg.eigh(VK)
Awh = V_ @ np.diag(1.0 / np.sqrt(w_)) @ V_.T
rec("6k_cond_VK_in_whitened_gauge", np.linalg.cond(Awh @ VK @ Awh.T))
rec("6l_KL_in_whitened_gauge_residual", abs(Dpair(Awh @ SQ[h0], Awh @ SK[h0]) - D0))
S1 = SQ[h0]
Dt = kl_gauss(S1 @ x_i, S1 @ C_i @ S1.T, S1 @ x_j, S1 @ C_j @ S1.T)
S2 = Aco @ S1
Dt2 = kl_gauss(S2 @ x_i, S2 @ C_i @ S2.T, S2 @ x_j, S2 @ C_j @ S2.T)
rec("6m_tied_same_rowspace_residual", abs(Dt - Dt2), "Grassmannian dependence")
Bc = rand_gl(s, 0.9)
rec("6n_content_BT_OBinv_residual", np.max(np.abs((O[0] @ np.linalg.inv(Bc)) @ (Bc @ T[0]) - O[0] @ T[0])))

print("== 7. Schur: equivariant interfaces for a product of GL(d_b) are block scalars")
dims = [3, 3]
Kb = sum(dims)


def rand_block(dims_):
    return blockdiag(*[rand_gl(d, 0.7) for d in dims_])


gens = [rand_block(dims) for _ in range(4)]
rows = [np.kron(np.eye(Kb), gk) - np.kron(gk.T, np.eye(Kb)) for gk in gens]
rec("7a_dim_commutant_End_G_V", null_space(np.vstack(rows)).shape[1], "= B (block scalars)")
rows = [np.kron(gk.T, np.eye(3)) - np.kron(np.eye(Kb), gk[:3, :3]) for gk in gens]
rec("7b_dim_Hom_G_V_to_V1", null_space(np.vstack(rows)).shape[1], "only c * pr_1")
rows = [np.kron(gk[:3, :3].T, np.eye(3)) - np.kron(np.eye(3), gk[3:, 3:]) for gk in gens]
rec("7c_dim_Hom_G_V1_to_V2", null_space(np.vstack(rows)).shape[1], "inequivalent blocks")
gensK = [rand_gl(Kb) for _ in range(3)]
rows = [np.kron(np.eye(Kb), gk) - np.kron(gk.T, np.eye(Kb)) for gk in gensK]
rec("7d_dim_commutant_GLK", null_space(np.vstack(rows)).shape[1], "= 1 (R*I)")

print("== 8. diagonal storage is a gauge slice (every orbit meets Sigma = I)")
Sfull = rand_spd(K)
Lc = np.linalg.cholesky(Sfull)
gfix = np.linalg.inv(Lc)
U0 = rand_gl(K)
m0 = rng.standard_normal(K)
xi_a = np.linalg.solve(U0, m0)
C_a = np.linalg.solve(U0, Sfull) @ np.linalg.inv(U0).T
U1 = gfix @ U0
xi_b = np.linalg.solve(U1, gfix @ m0)
C_b = np.linalg.solve(U1, gfix @ Sfull @ gfix.T) @ np.linalg.inv(U1).T
rec("8a_gauge_fixed_Sigma_minus_I", np.max(np.abs(gfix @ Sfull @ gfix.T - np.eye(K))))
rec("8b_xi_residual", np.max(np.abs(xi_a - xi_b)))
rec("8c_C_residual", np.max(np.abs(C_a - C_b)))
Dg = np.diag(rng.uniform(0.2, 3.0, K))
Cdiag = np.linalg.solve(U0, Dg) @ np.linalg.inv(U0).T
U2 = np.diag(1.0 / np.sqrt(np.diag(Dg))) @ U0
Cid = np.linalg.inv(U2) @ np.linalg.inv(U2).T
rec("8d_D_U_vs_I_DinvsqrtU_C_residual", np.max(np.abs(Cdiag - Cid)))

print("== 9. off-block complement m of gl(K) under block-diagonal h")


def proj_h(X, dims_):
    out = np.zeros_like(X)
    s0 = 0
    for d in dims_:
        out[s0:s0 + d, s0:s0 + d] = X[s0:s0 + d, s0:s0 + d]
        s0 += d
    return out


for dims9 in ([2, 2], [1, 1, 1], [2, 1, 1]):
    Kd = sum(dims9)
    worst_hm, worst_Ad, mm_m = 0.0, 0.0, 0.0
    for _ in range(20):
        X = rng.standard_normal((Kd, Kd))
        Xm = X - proj_h(X, dims9)
        Y = proj_h(rng.standard_normal((Kd, Kd)), dims9)
        Z = rng.standard_normal((Kd, Kd))
        Zm = Z - proj_h(Z, dims9)
        gb = blockdiag(*[rand_gl(d, 0.7) for d in dims9])
        worst_hm = max(worst_hm, np.max(np.abs(proj_h(Y @ Xm - Xm @ Y, dims9))))
        worst_Ad = max(worst_Ad, np.max(np.abs(proj_h(gb @ Xm @ np.linalg.inv(gb), dims9))))
        br = Xm @ Zm - Zm @ Xm
        mm_m = max(mm_m, np.max(np.abs(br - proj_h(br, dims9))))
    tag = "x".join(str(d) for d in dims9)
    rec("9_dims" + tag + "_bracket_h_m_hpart", worst_hm)
    rec("9_dims" + tag + "_Ad_g_m_hpart", worst_Ad)
    rec("9_dims" + tag + "_bracket_m_m_mpart", mm_m, "0 => symmetric pair")

print("== 10. RoPE intertwining and anisotropic comparison covariance")


def rot(t):
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])


th = 0.37
SQr = np.hstack([np.eye(2), np.zeros((2, 2))])
Rpos = [rot(i * th) for i in range(6)]
Pblk = [rand_gl(2) for _ in range(6)]
Uinv_pos = [blockdiag(Rpos[i], Pblk[i]) for i in range(6)]
rec("10a_SQ_Uinv_minus_R_SQ", max(np.max(np.abs(SQr @ Uinv_pos[i] - Rpos[i] @ SQr)) for i in range(6)))
Xtok = [rand_gl(4, 0.4) for _ in range(2)]
lit = max(np.max(np.abs(SQr @ Uinv_pos[i] @ np.linalg.inv(Xtok[t]) - Rpos[i] @ SQr))
          for i in range(6) for t in range(2))
rec("10b_literal_identity_with_token_factor_violation", lit, "positional-factor condition suffices")
Vs = rand_spd(2)
Vq = rand_spd(2)
a_ = rng.standard_normal(2)
b_ = rng.standard_normal(2)
cross_rot = a_ @ Rpos[1].T @ np.linalg.inv(Rpos[4] @ Vs @ Rpos[4].T) @ Rpos[4] @ b_
w2, V2 = np.linalg.eigh(Vs)
Vmh = V2 @ np.diag(1.0 / np.sqrt(w2)) @ V2.T
cross_white = (Rpos[1] @ Vmh @ a_) @ (Rpos[4] @ Vmh @ b_)
rec("10c_cross_pushforward_minus_whitened_rotary_aniso", abs(cross_rot - cross_white))
tr_terms = {}
for (i, j) in [(4, 1), (5, 2), (3, 3), (5, 0)]:
    Pj = np.linalg.inv(Rpos[j] @ Vs @ Rpos[j].T)
    tr_terms["%d-%d" % (i, j)] = float(np.trace(Pj @ Rpos[i] @ Vq @ Rpos[i].T))
rec("10d_trace_term_41_minus_52", abs(tr_terms["4-1"] - tr_terms["5-2"]), "depends on i-j only")
rec("10e_trace_term_41_minus_33", abs(tr_terms["4-1"] - tr_terms["3-3"]), "relative-position bias")

print("== 11. non-flat edge connection on the causal DAG (inverse reverse edges)")
Kn, Nn = 3, 6
Vrel = [np.eye(Kn)] + [rand_gl(Kn, 0.5) for _ in range(Nn - 1)]
Un = [rand_gl(Kn) for _ in range(Nn)]
Theta = {(i, j): Un[i] @ Vrel[i - j] @ np.linalg.inv(Un[j]) for i in range(Nn) for j in range(i + 1)}
gn = [rand_gl(Kn, 0.8) for _ in range(Nn)]
ThetaG = {(i, j): gn[i] @ Theta[(i, j)] @ np.linalg.inv(gn[j]) for (i, j) in Theta}
worst_dev, worst_spec = 0.0, 0.0
for trip in itertools.combinations(range(Nn), 3):
    i, j, k2 = sorted(trip, reverse=True)
    hol = Theta[(i, j)] @ Theta[(j, k2)] @ np.linalg.inv(Theta[(i, k2)])
    holg = ThetaG[(i, j)] @ ThetaG[(j, k2)] @ np.linalg.inv(ThetaG[(i, k2)])
    ev = np.sort_complex(np.linalg.eigvals(hol))
    evg = np.sort_complex(np.linalg.eigvals(holg))
    worst_dev = max(worst_dev, np.max(np.abs(ev - 1)))
    worst_spec = max(worst_spec, np.max(np.abs(ev - evg)))
rec("11a_max_abs_eig_hol_minus_1_learned_offset_links", worst_dev, "genuine curvature")
rec("11b_max_spectrum_change_under_gauge", worst_spec, "gauge invariant")
J = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0.0]])
Vrope = [expm(d * 0.3 * J) for d in range(Nn)]
worst_rope = 0.0
for trip in itertools.combinations(range(Nn), 3):
    i, j, k2 = sorted(trip, reverse=True)
    hol = Vrope[i - j] @ Vrope[j - k2] @ np.linalg.inv(Vrope[i - k2])
    worst_rope = max(worst_rope, np.max(np.abs(hol - np.eye(Kn))))
rec("11c_RoPE_type_offset_links_holonomy_minus_I", worst_rope, "one-parameter group => flat")

print("== 12. sharpness and temperature degeneracy (shared isotropic covariance)")
aa_ = rng.standard_normal((5, 2))
qq = rng.standard_normal(2)
lg1 = [-np.sum((qq - b) ** 2) / (2 * 0.7 * 1.9) for b in aa_]
lg2 = [-np.sum((qq - b) ** 2) / (2 * (0.7 * 3.0) * (1.9 / 3.0)) for b in aa_]
rec("12a_beta_sigma2_tau_minus_beta_3sigma2_tau3", np.max(np.abs(softmax(lg1) - softmax(lg2))))

print("== 13. comparison tensor and metric laws")
i1, j1 = 3, 1
AQ = SQ[0] @ np.linalg.inv(U[i1])
AK = SK[0] @ np.linalg.inv(U[j1])
B = AQ.T @ np.linalg.inv(AK @ Sig[j1] @ AK.T) @ AK
AQp = SQ[0] @ np.linalg.inv(U_p[i1])
AKp = SK[0] @ np.linalg.inv(U_p[j1])
Bp = AQp.T @ np.linalg.inv(AKp @ Sig_p[j1] @ AKp.T) @ AKp
rec("13a_Bprime_minus_ginvT_B_ginv", np.max(np.abs(Bp - np.linalg.inv(g[i1]).T @ B @ gi[j1])))
Gm = np.linalg.inv(U[i1]).T @ np.linalg.inv(U[i1])
Gmp = np.linalg.inv(U_p[i1]).T @ np.linalg.inv(U_p[i1])
rec("13b_GinvB_link_law", np.max(np.abs(np.linalg.solve(Gmp, Bp) - g[i1] @ np.linalg.solve(Gm, B) @ gi[j1])))
rec("13c_SigmaB_link_law", np.max(np.abs(Sig_p[i1] @ Bp - g[i1] @ Sig[i1] @ B @ gi[j1])))
rec("13d_invariant_scalar_muBmu", abs(mu_p[i1] @ Bp @ mu_p[j1] - mu[i1] @ B @ mu[j1]))

print("== 14. Culver: products of two real exponentials leave the image of exp")
J2 = np.array([[0, -1.0], [1, 0]])
Mc = expm(np.pi * J2) @ expm(np.diag([0.0, np.log(2.0)]))
rec("14a_expm_piJ_expm_diag0ln2_minus_diag_m1m2", np.max(np.abs(Mc - np.diag([-1.0, -2.0]))))
Lg = logm(np.diag([-1.0, -2.0]).astype(complex))
rec("14b_max_abs_Im_logm_diag_m1m2", np.max(np.abs(Lg.imag)), "principal log is complex")

print("== 15. four functional roles of frames in a tiny reported-type model")
Nt, Kt, Ht, rt, Lt, Vt, Hid = 5, 6, 2, 2, 2, 7, 8
dims_t = [3, 3]
mu_tab = rng.standard_normal((Vt, Kt))
sig_tab = rng.uniform(0.3, 2.0, (Vt, Kt))
Xtab = [blockdiag(*[rng.standard_normal((3, 3)) * 0.4 for _ in dims_t]) for _ in range(Vt)]
Ypos = [blockdiag(*[rng.standard_normal((3, 3)) * 0.3 for _ in dims_t]) for _ in range(Nt)]
toks = rng.integers(0, Vt, Nt)
Uf = np.stack([expm(Xtab[t]) @ expm(Ypos[i]) for i, t in enumerate(toks)])
layers = []
for _ in range(Lt):
    layers.append(dict(SQ=rng.standard_normal((Ht, rt, Kt)), SK=rng.standard_normal((Ht, rt, Kt)),
                       T=rng.standard_normal((Ht, rt, Kt)) * 0.5, O=rng.standard_normal((Ht, Kt, rt)) * 0.5,
                       W1=rng.standard_normal((Hid, Kt)) * 0.4, b1=rng.standard_normal(Hid) * 0.1,
                       W2=rng.standard_normal((Kt, Hid)) * 0.4, b2=rng.standard_normal(Kt) * 0.1))
gam, bet = rng.uniform(0.5, 1.5, Kt), rng.standard_normal(Kt) * 0.1
Wout, bout = rng.standard_normal((Vt, Kt)), rng.standard_normal(Vt)
alibi_t = np.array([[[-(0.5 ** (h + 1)) * (i - j) for j in range(Nt)] for i in range(Nt)]
                    for h in range(Ht)])


def LN(x, eps_=1e-6):
    c = x - x.mean(-1, keepdims=True)
    return gam * c / np.sqrt((c ** 2).mean(-1, keepdims=True) + eps_) + bet


def gelu(x):
    return 0.5 * x * (1 + erf(x / np.sqrt(2)))


def mlp(u, P):
    return u + gelu(u @ P["W1"].T + P["b1"]) @ P["W2"].T + P["b2"]


def model(mu0_, Sig0_, Uf_, canonical=False):
    mu_l = mu0_.copy()
    for P in layers:
        att = attention(mu_l, Sig0_, Uf_, P["SQ"], P["SK"], P["T"], P["O"], 1.1, alibi_t)
        mu_att = mu_l + att["m"]
        if canonical:
            xi_att = np.einsum("nab,nb->na", np.linalg.inv(Uf_), mu_att)
            mu_l = np.einsum("nab,nb->na", Uf_, mlp(LN(xi_att), P))
        else:
            mu_l = mlp(LN(mu_att), P)
    if canonical:
        return np.einsum("nab,nb->na", np.linalg.inv(Uf_), mu_l) @ Wout.T + bout
    return mu_l @ Wout.T + bout


def model_unitary(xi0_, C0_, Uf_):
    """Same logits written only through xi0, static C, conjugated LN+MLP, decoder W U."""
    xi_l = xi0_.copy()
    Iden = np.stack([np.eye(Kt)] * Nt)
    for P in layers:
        att = attention(xi_l, C0_, Iden, P["SQ"], P["SK"], P["T"], P["O"], 1.1, alibi_t)
        mu_att = np.einsum("nab,nb->na", Uf_, xi_l + att["m"])
        xi_l = np.einsum("nab,nb->na", np.linalg.inv(Uf_), mlp(LN(mu_att), P))
    return np.einsum("va,nab,nb->nv", Wout, Uf_, xi_l) + bout


mu0 = mu_tab[toks]
Sig0 = np.stack([np.diag(sig_tab[t]) for t in toks])
logits = model(mu0, Sig0, Uf)
xi0 = np.einsum("nab,nb->na", np.linalg.inv(Uf), mu0)
C0 = np.linalg.inv(Uf) @ Sig0 @ np.transpose(np.linalg.inv(Uf), (0, 2, 1))
rec("15a_logits_frame_model_minus_unitary_gauge_rewrite",
    np.max(np.abs(logits - model_unitary(xi0, C0, Uf))), "four roles only")
rec("15a2_logit_scale", np.max(np.abs(logits)))
gp = np.stack([blockdiag(*[rand_gl(3, 0.6) for _ in dims_t]) for _ in range(Nt)])
mu0p = np.einsum("nab,nb->na", gp, mu0)
Sig0p = gp @ Sig0 @ np.transpose(gp, (0, 2, 1))
Ufp = gp @ Uf
rec("15b_reported_model_logit_change_under_passive_g",
    np.max(np.abs(model(mu0p, Sig0p, Ufp) - logits)), "coordinate LN MLP decoder break covariance")
lc = model(mu0, Sig0, Uf, canonical=True)
rec("15c_canonical_model_logit_change_under_passive_g",
    np.max(np.abs(model(mu0p, Sig0p, Ufp, canonical=True) - lc)), "left (local) covariant")
ab = blockdiag(*[rand_gl(3, 0.5) for _ in dims_t])
saved = [dict(P) for P in layers]
for P in layers:
    P["SQ"], P["SK"], P["T"], P["O"] = P["SQ"] @ ab, P["SK"] @ ab, P["T"] @ ab, np.linalg.inv(ab) @ P["O"]
Ufa = Uf @ ab
rec("15d_reported_model_logit_change_under_global_ref_change",
    np.max(np.abs(model(mu0, Sig0, Ufa) - logits)), "right (global) redundancy")
rec("15e_canonical_model_logit_change_under_global_ref_change",
    np.max(np.abs(model(mu0, Sig0, Ufa, canonical=True) - lc)), "canonical model fixes reference frame")
for P, Sv in zip(layers, saved):
    P.update(Sv)
Cstatic = [np.linalg.inv(Uf) @ Sig0 @ np.transpose(np.linalg.inv(Uf), (0, 2, 1)) for _ in range(Lt)]
rec("15f_C_layer0_minus_layer1_under_passthrough", np.max(np.abs(Cstatic[0] - Cstatic[1])),
    "C depends only on token and position")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gauge_checks_results.json")
with open(out_path, "w") as fh:
    json.dump(R, fh, indent=1)
print("float64 eps", EPS)
print("wrote", out_path)
