r"""Information-geometry checks for GL(K)_attention_v2.tex and GL(K)_supplementary_v2.tex.

CPU only: numpy / scipy / sympy.  Seeded.  Writes infogeo_checks.json next to this file.
Every residual is reported with a baseline (float64 eps = 2.22e-16 or the magnitude of the
quantity itself).  Section letters match the report.
"""
import json
import math
import os

import numpy as np
import scipy.linalg as sla
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import minimize, minimize_scalar

rng = np.random.default_rng(20260923)
EPS = float(np.finfo(float).eps)
OUT = {"float64_eps": EPS}


def rand_spd(n, cond=20.0):
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    ev = np.exp(rng.uniform(0.0, math.log(cond), n))
    return (Q * ev) @ Q.T


def rand_gl(n, scale=0.8):
    return np.eye(n) + scale * rng.standard_normal((n, n))


def logdet(S):
    s, v = np.linalg.slogdet(S)
    assert s > 0
    return v


def kl_gauss(m0, S0, m1, S1):
    r"""KL(N(m0,S0) || N(m1,S1)) via Cholesky solves."""
    r = m0.shape[0]
    L1 = np.linalg.cholesky(S1)
    L0 = np.linalg.cholesky(S0)
    M = sla.solve_triangular(L1, L0, lower=True)
    w = sla.solve_triangular(L1, m1 - m0, lower=True)
    return 0.5 * (np.sum(M ** 2) + w @ w - r + logdet(S1) - logdet(S0))


def renyi_gauss(m0, S0, m1, S1, al):
    r"""Renyi D_al(N0||N1), blend S_al = (1-al) S0 + al S1 (Burbea 1984; Gil et al. 2013 Table 2)."""
    Sa = (1 - al) * S0 + al * S1
    d = m1 - m0
    return (al / 2) * d @ np.linalg.solve(Sa, d) + (1.0 / (2 * (al - 1))) * (
        (1 - al) * logdet(S0) + al * logdet(S1) - logdet(Sa))


def paper_projected_kl(a, VQ, b, VK):
    r"""Main eq:projected_full_kl, written term by term exactly as printed."""
    r = a.shape[0]
    P = np.linalg.inv(VK)
    return 0.5 * (np.trace(P @ VQ) + a @ P @ a - 2 * a @ P @ b + b @ P @ b - r
                  + logdet(VK) - logdet(VQ))


def softmax(z):
    z = z - np.max(z)
    e = np.exp(z)
    return e / e.sum()


def two_way(Tm):
    r"""Split a pair table T_ij into grand + row + column + interaction; return norm fractions."""
    g = Tm.mean()
    row = Tm.mean(axis=1, keepdims=True) - g
    col = Tm.mean(axis=0, keepdims=True) - g
    inter = Tm - g - row - col
    tot = np.linalg.norm(Tm - g)
    return {"row_frac": float(np.linalg.norm(row * np.ones_like(Tm)) / max(tot, 1e-300)),
            "col_frac": float(np.linalg.norm(col * np.ones_like(Tm)) / max(tot, 1e-300)),
            "interaction_frac": float(np.linalg.norm(inter) / max(tot, 1e-300))}


# ---------------------------------------------------------------- A. eq:glk_invariance
res_kl, res_h, res_r = [], [], []
for _ in range(200):
    K = 4
    m0, m1 = rng.standard_normal(K), rng.standard_normal(K)
    S0, S1 = rand_spd(K), rand_spd(K)
    A = rand_gl(K)
    base = kl_gauss(m0, S0, m1, S1)
    pushed = kl_gauss(A @ m0, A @ S0 @ A.T, A @ m1, A @ S1 @ A.T)
    res_kl.append(abs(pushed - base) / max(1.0, abs(base)))
    h0 = 1 - math.exp(-0.5 * renyi_gauss(m0, S0, m1, S1, 0.5))
    h1 = 1 - math.exp(-0.5 * renyi_gauss(A @ m0, A @ S0 @ A.T, A @ m1, A @ S1 @ A.T, 0.5))
    res_h.append(abs(h1 - h0))
    r0 = renyi_gauss(m0, S0, m1, S1, 0.3)
    r1 = renyi_gauss(A @ m0, A @ S0 @ A.T, A @ m1, A @ S1 @ A.T, 0.3)
    res_r.append(abs(r1 - r0) / max(1.0, abs(r0)))
OUT["A_glk_invariance"] = {"kl_max_rel_residual": max(res_kl), "hellinger_sq_max_abs_residual": max(res_h),
                           "renyi_0.3_max_rel_residual": max(res_r), "trials": 200}

gaps = []
for _ in range(500):
    K, r = 4, 2
    xi_i, xi_j = rng.standard_normal(K), rng.standard_normal(K)
    Ci, Cj = rand_spd(K), rand_spd(K)
    S = rng.standard_normal((r, K))
    full = kl_gauss(xi_i, Ci, xi_j, Cj)
    tied = kl_gauss(S @ xi_i, S @ Ci @ S.T, S @ xi_j, S @ Cj @ S.T)
    gaps.append(tied - full)
xi = rng.standard_normal(4)
C = rand_spd(4)
SQ, SK = rng.standard_normal((2, 4)), rng.standard_normal((2, 4))
untied_same_state = kl_gauss(SQ @ xi, SQ @ C @ SQ.T, SK @ xi, SK @ C @ SK.T)
OUT["A2_data_processing"] = {"tied_max_(Dproj-Dfull)": float(max(gaps)), "trials": 500,
                             "untied_D_for_identical_states": float(untied_same_state),
                             "full_state_KL_for_identical_states": 0.0}

# ---------------------------------------------------------------- B. reduced covariance PD
mins = []
for _ in range(200):
    S = rng.standard_normal((3, 6))
    mins.append(np.linalg.eigvalsh(S @ rand_spd(6) @ S.T).min())
OUT["B_projected_pd_min_eig"] = float(min(mins))


# ---------------------------------------------------------------- C. metric complement (prior C1)
def g_orth_complement(U, T, H):
    r"""G-orthogonal complement in E of ker(T U^{-1}) = U ker T, with G = U^{-T} H U^{-1}."""
    NT = sla.null_space(T)
    W = U @ NT
    G = np.linalg.inv(U).T @ H @ np.linalg.inv(U)
    return sla.null_space(W.T @ G)


K, s = 4, 2
U = rand_gl(K)
T = rng.standard_normal((s, K))
H = rand_spd(K)
a = rand_gl(K)
comp = g_orth_complement(U, T, H)
formula = U @ np.linalg.solve(H, T.T)
ang_formula = float(np.max(sla.subspace_angles(comp, formula)))
compp = g_orth_complement(U @ a, T @ a, a.T @ H @ a)
ang_rebase = float(np.max(sla.subspace_angles(comp, compp)))
comp_I = g_orth_complement(U, T, np.eye(K))
comp_I_reset = g_orth_complement(U @ a, T @ a, np.eye(K))
ang_reset = float(np.max(sla.subspace_angles(comp_I, comp_I_reset)))
Sigma = rand_spd(K)
Cref = np.linalg.inv(U) @ Sigma @ np.linalg.inv(U).T
compF = g_orth_complement(U, T, np.linalg.inv(Cref))
formulaF = Sigma @ np.linalg.inv(U).T @ T.T
ang_F = float(np.max(sla.subspace_angles(compF, formulaF)))
Cref_a = np.linalg.inv(a) @ Cref @ np.linalg.inv(a).T
compF_a = g_orth_complement(U @ a, T @ a, np.linalg.inv(Cref_a))
ang_F_rebase = float(np.max(sla.subspace_angles(compF, compF_a)))
g = rand_gl(K)
compF_g = g_orth_complement(g @ U, T, np.linalg.inv(Cref))
ang_F_passive = float(np.max(sla.subspace_angles(g @ compF, compF_g)))
ang_F_vs_euclid = float(np.max(sla.subspace_angles(compF, comp_I)))
OUT["C_metric_complement"] = {
    "general_H_formula_U_Hinv_imTt_max_angle": ang_formula,
    "general_H_rebased_with_Hprime_eq_aT_H_a_max_angle": ang_rebase,
    "H_eq_I_reset_after_nonorthogonal_rebase_max_angle_rad": ang_reset,
    "fisher_H_eq_Cinv_formula_Sigma_Uinv_T_imTt_max_angle": ang_F,
    "fisher_rebase_automatic_max_angle": ang_F_rebase,
    "fisher_passive_covariant_max_angle": ang_F_passive,
    "fisher_vs_euclidean_complement_max_angle_rad": ang_F_vs_euclid,
}

# ---------------------------------------------------------------- D/E. comparison tensor and Gaussian lift
K, r = 5, 2
Ui, Uj = rand_gl(K), rand_gl(K)
SigI, SigJ = rand_spd(K), rand_spd(K)
SQ, SK = rng.standard_normal((r, K)), rng.standard_normal((r, K))
AQ, AK = SQ @ np.linalg.inv(Ui), SK @ np.linalg.inv(Uj)
PK = np.linalg.inv(AK @ SigJ @ AK.T)
B = AQ.T @ PK @ AK
gi, gj = rand_gl(K), rand_gl(K)
AQp, AKp = SQ @ np.linalg.inv(gi @ Ui), SK @ np.linalg.inv(gj @ Uj)
PKp = np.linalg.inv(AKp @ (gj @ SigJ @ gj.T) @ AKp.T)
Bp = AQp.T @ PKp @ AKp
res_B = float(np.max(np.abs(Bp - np.linalg.inv(gi).T @ B @ np.linalg.inv(gj))) / np.max(np.abs(B)))
Ci = np.linalg.inv(Ui) @ SigI @ np.linalg.inv(Ui).T
Cj = np.linalg.inv(Uj) @ SigJ @ np.linalg.inv(Uj).T
VQ, VK = SQ @ Ci @ SQ.T, SK @ Cj @ SK.T
R = Ci @ SQ.T @ np.linalg.inv(VQ)
res_right_inv = float(np.max(np.abs(SQ @ R - np.eye(r))))
res_crosscov = float(np.max(np.abs(Ci @ SQ.T - R @ SQ @ Ci @ SQ.T)) / np.max(np.abs(Ci @ SQ.T)))
y = rng.standard_normal(r)
NS = sla.null_space(SQ)
Cinv = np.linalg.inv(Ci)
gaps = []
for _ in range(200):
    w = NS @ rng.standard_normal(NS.shape[1])
    d0 = R @ y
    gaps.append((d0 + w) @ Cinv @ (d0 + w) - d0 @ Cinv @ d0 - w @ Cinv @ w)
res_min = float(max(abs(x) for x in gaps))
L_fisher = SigI @ B
L_cmp = Ui @ R @ SK @ np.linalg.inv(Uj)
res_Lf = float(np.max(np.abs(L_fisher - Ui @ Ci @ SQ.T @ np.linalg.inv(VK) @ SK @ np.linalg.inv(Uj))))
diff_lift = float(np.linalg.norm(L_fisher - L_cmp) / np.linalg.norm(L_cmp))
VK_eq = SQ @ Ci @ SQ.T
L_f_eq = Ui @ Ci @ SQ.T @ np.linalg.inv(VK_eq) @ SQ @ np.linalg.inv(Uj)
L_c_eq = Ui @ Ci @ SQ.T @ np.linalg.inv(VQ) @ SQ @ np.linalg.inv(Uj)
OUT["D_E_tensor_and_lift"] = {"B_law_rel_residual": res_B, "lift_right_inverse_residual": res_right_inv,
                              "lift_crosscov_rel_residual": res_crosscov,
                              "lift_min_norm_cross_term_max_abs": res_min,
                              "Sigma_B_formula_residual": res_Lf,
                              "rel_diff_SigmaB_vs_Gaussian_lift_generic": diff_lift,
                              "rel_diff_when_VQ_equals_VK": float(np.linalg.norm(L_f_eq - L_c_eq) / np.linalg.norm(L_c_eq))}

# ---------------------------------------------------------------- F. block KL additivity
m_q, m_p = rng.standard_normal(5), rng.standard_normal(5)
Sq = sla.block_diag(rand_spd(2), rand_spd(3))
Sp = sla.block_diag(rand_spd(2), rand_spd(3))
full = kl_gauss(m_q, Sq, m_p, Sp)
blocks = (kl_gauss(m_q[:2], Sq[:2, :2], m_p[:2], Sp[:2, :2]) + kl_gauss(m_q[2:], Sq[2:, 2:], m_p[2:], Sp[2:, 2:]))
c = 0.6
ce = kl_gauss(np.zeros(2), np.array([[1, c], [c, 1.0]]), np.zeros(2), np.eye(2))
OUT["F_block_additivity"] = {"residual": abs(full - blocks), "counterexample_c_0.6": ce,
                             "paper_value_minus_half_log_1_minus_c2": -0.5 * math.log(1 - c * c)}

# ---------------------------------------------------------------- G. dilation, isotropic form, (V*, tau) redundancy
mu, Sg, Uu = rng.standard_normal(4), rand_spd(4), rand_gl(4)
cdil = -2.7
xi0, C0 = np.linalg.solve(Uu, mu), np.linalg.inv(Uu) @ Sg @ np.linalg.inv(Uu).T
xi1 = np.linalg.solve(cdil * Uu, cdil * mu)
C1 = np.linalg.inv(cdil * Uu) @ (cdil ** 2 * Sg) @ np.linalg.inv(cdil * Uu).T
res_dil = float(max(np.max(np.abs(xi1 - xi0)), np.max(np.abs(C1 - C0))))
a_, b_ = rng.standard_normal(3), rng.standard_normal(3)
s2 = 2.3
res_iso = abs(kl_gauss(a_, s2 * np.eye(3), b_, s2 * np.eye(3)) - np.sum((a_ - b_) ** 2) / (2 * s2))
N, r = 6, 3
Vs = rand_spd(r)
aa = rng.standard_normal((N, r)); bb = rng.standard_normal((N, r))
VQs = [rand_spd(r) for _ in range(N)]


def routing(Vstar, tau, VQlist):
    D = np.array([[kl_gauss(aa[i], VQlist[i], bb[j], Vstar) for j in range(N)] for i in range(N)])
    return np.array([softmax(-D[i] / tau) for i in range(N)])


cc = 3.7
r1 = routing(Vs, 1.3, VQs)
r2 = routing(cc * Vs, 1.3 / cc, [cc * v for v in VQs])
r3 = routing(cc * Vs, 1.3 / cc, VQs)
OUT["G_dilation_isotropic_redundancy"] = {"passive_dilation_residual": res_dil, "isotropic_form_residual": res_iso,
                                          "routing_cVstar_tau_over_c_minus_base_max": float(np.max(np.abs(r2 - r1))),
                                          "routing_query_cov_unscaled_max": float(np.max(np.abs(r3 - r1)))}

# ---------------------------------------------------------------- H. eq:projected_full_kl
res = []
for _ in range(300):
    r = 4
    a_, b_ = rng.standard_normal(r), rng.standard_normal(r)
    VQ_, VK_ = rand_spd(r, 100), rand_spd(r, 100)
    kk = kl_gauss(a_, VQ_, b_, VK_)
    res.append(abs(paper_projected_kl(a_, VQ_, b_, VK_) - kk) / max(1.0, kk))
a1, a2, b1, b2, p11, p12, p22 = sp.symbols("a1 a2 b1 b2 p11 p12 p22", real=True)
Psym = sp.Matrix([[p11, p12], [p12, p22]])
av, bv = sp.Matrix([a1, a2]), sp.Matrix([b1, b2])
expand_res = sp.simplify(((av - bv).T * Psym * (av - bv))[0] - ((av.T * Psym * av)[0] - 2 * (av.T * Psym * bv)[0] + (bv.T * Psym * bv)[0]))
OUT["H_projected_full_kl"] = {"max_rel_residual_vs_cholesky_KL": float(max(res)), "trials": 300,
                              "sympy_quadratic_expansion_residual": str(expand_res)}


# ---------------------------------------------------------------- I. term classification (row / source / pair)
def term_tables(A_, B_, VQl, VKl):
    n = len(A_)
    out = {k: np.zeros((n, n)) for k in ("trace", "query_quad", "cross", "key_quad", "logdet_K", "logdet_Q")}
    for i in range(n):
        for j in range(n):
            P = np.linalg.inv(VKl[j])
            out["trace"][i, j] = 0.5 * np.trace(P @ VQl[i])
            out["query_quad"][i, j] = 0.5 * A_[i] @ P @ A_[i]
            out["cross"][i, j] = -A_[i] @ P @ B_[j]
            out["key_quad"][i, j] = 0.5 * B_[j] @ P @ B_[j]
            out["logdet_K"][i, j] = 0.5 * logdet(VKl[j])
            out["logdet_Q"][i, j] = -0.5 * logdet(VQl[i])
    return out


N, r = 12, 3
A_ = rng.standard_normal((N, r)); B_ = rng.standard_normal((N, r))
VQl = [rand_spd(r, 30) for _ in range(N)]; VKl = [rand_spd(r, 30) for _ in range(N)]
gen = {k: two_way(v) for k, v in term_tables(A_, B_, VQl, VKl).items()}
Vst = rand_spd(r, 30)
shared = {k: two_way(v) for k, v in term_tables(A_, B_, VQl, [Vst] * N).items()}
OUT["I_term_classification"] = {"general_covariances": gen, "shared_key_covariance": shared}

# ---------------------------------------------------------------- J. whitening proposition + O(r) freedom
N, r = 7, 3
Vst = rand_spd(r, 50)
A_ = rng.standard_normal((N, r)); B_ = rng.standard_normal((N, r))
VQl = [rand_spd(r) for _ in range(N)]
tau = 1.7
logpi = np.log(rng.dirichlet(np.ones(N)))
W = np.real(sla.fractional_matrix_power(Vst, -0.5))
qv, kv = A_ @ W.T, B_ @ W.T
Om, _ = np.linalg.qr(rng.standard_normal((r, r)))
worst, worstO = 0.0, 0.0
for i in range(N):
    D = np.array([kl_gauss(A_[i], VQl[i], B_[j], Vst) for j in range(N)])
    beta = softmax(-D / tau + logpi)
    pred = softmax(kv @ qv[i] / tau - np.sum(kv ** 2, 1) / (2 * tau) + logpi)
    predO = softmax((kv @ Om.T) @ (Om @ qv[i]) / tau - np.sum((kv @ Om.T) ** 2, 1) / (2 * tau) + logpi)
    worst = max(worst, float(np.max(np.abs(beta - pred))))
    worstO = max(worstO, float(np.max(np.abs(beta - predO))))
OUT["J_whitening"] = {"routing_residual": worst, "orthogonal_rewhitening_residual": worstO}


# ---------------------------------------------------------------- K. exponential-family pairing identity
def nat(m, V):
    P = np.linalg.inv(V)
    return P @ m, -0.5 * P


def expt(m, V):
    return m, V + np.outer(m, m)


def A_logpart(m, V):
    r = m.shape[0]
    return 0.5 * m @ np.linalg.solve(V, m) + 0.5 * logdet(V) + 0.5 * r * math.log(2 * math.pi)


def neg_entropy(m, V):
    r = m.shape[0]
    return -0.5 * (logdet(V) + r * math.log(2 * math.pi * math.e))


def pair(th, et):
    return th[0] @ et[0] + np.sum(th[1] * et[1])


resF, resR = [], []
for _ in range(200):
    r = 3
    a_, b_ = rng.standard_normal(r), rng.standard_normal(r)
    VQ_, VK_ = rand_spd(r), rand_spd(r)
    fwd = A_logpart(b_, VK_) + neg_entropy(a_, VQ_) - pair(nat(b_, VK_), expt(a_, VQ_))
    resF.append(abs(fwd - kl_gauss(a_, VQ_, b_, VK_)))
    rev = A_logpart(a_, VQ_) + neg_entropy(b_, VK_) - pair(nat(a_, VQ_), expt(b_, VK_))
    resR.append(abs(rev - kl_gauss(b_, VK_, a_, VQ_)))
OUT["K_exp_family_pairing"] = {"forward_KL_q_p_eq_A_thp_plus_Astar_etaq_minus_pair_max_residual": max(resF),
                               "reverse_KL_p_q_max_residual": max(resR)}

# ---------------------------------------------------------------- L. reverse joint KL gives prior-only routing
N, r = 5, 2
pi = rng.dirichlet(np.ones(N))
mq, Vq = rng.standard_normal(r), rand_spd(r)
mk = rng.standard_normal((N, r)); Vk = [rand_spd(r) for _ in range(N)]


def rev_joint(beta):
    return float(np.sum(pi * np.log(pi / beta)) + sum(pi[j] * kl_gauss(mk[j], Vk[j], mq, Vq) for j in range(N)))


def fwd_joint(beta):
    return float(np.sum(beta * np.log(beta / pi)) + sum(beta[j] * kl_gauss(mq, Vq, mk[j], Vk[j]) for j in range(N)))


opt_rev = minimize(lambda z: rev_joint(softmax(z)), np.zeros(N), method="BFGS", options={"gtol": 1e-10})
opt_fwd = minimize(lambda z: fwd_joint(softmax(z)), np.zeros(N), method="BFGS", options={"gtol": 1e-10})
Dfw = np.array([kl_gauss(mq, Vq, mk[j], Vk[j]) for j in range(N)])
OUT["L_joint_direction"] = {
    "reverse_joint_argmin_minus_prior_max": float(np.max(np.abs(softmax(opt_rev.x) - pi))),
    "forward_joint_argmin_minus_gibbs_max": float(np.max(np.abs(softmax(opt_fwd.x) - softmax(np.log(pi) - Dfw)))),
    "gibbs_minus_prior_max_nontrivial": float(np.max(np.abs(softmax(np.log(pi) - Dfw) - pi)))}

# ---------------------------------------------------------------- M. reverse / Jeffreys / Bhattacharyya under shared KEY covariance
N, r = 10, 3
A_ = rng.standard_normal((N, r)); B_ = rng.standard_normal((N, r))
VQl = [rand_spd(r, 30) for _ in range(N)]
Vst = rand_spd(r, 30)
P = np.linalg.inv(Vst)
fwd = np.array([[kl_gauss(A_[i], VQl[i], B_[j], Vst) + A_[i] @ P @ B_[j] for j in range(N)] for i in range(N)])
rev = np.array([[kl_gauss(B_[j], Vst, A_[i], VQl[i]) + A_[i] @ np.linalg.solve(VQl[i], B_[j]) for j in range(N)] for i in range(N)])
jef = np.array([[kl_gauss(A_[i], VQl[i], B_[j], Vst) + kl_gauss(B_[j], Vst, A_[i], VQl[i])
                 + A_[i] @ (P + np.linalg.inv(VQl[i])) @ B_[j] for j in range(N)] for i in range(N)])
bha = np.array([[renyi_gauss(A_[i], VQl[i], B_[j], Vst, 0.5) for j in range(N)] for i in range(N)])
Vq_sh = rand_spd(r, 30)
VKl = [rand_spd(r, 30) for _ in range(N)]
rev_sq = np.array([[kl_gauss(B_[j], VKl[j], A_[i], Vq_sh) + A_[i] @ np.linalg.solve(Vq_sh, B_[j]) for j in range(N)] for i in range(N)])
fwd_sq = np.array([[kl_gauss(A_[i], Vq_sh, B_[j], VKl[j]) for j in range(N)] for i in range(N)])
OUT["M_direction_reductions"] = {
    "forward_sharedK_minus_dot_interaction_frac": two_way(fwd)["interaction_frac"],
    "reverse_sharedK_minus_querymetric_dot_interaction_frac": two_way(rev)["interaction_frac"],
    "jeffreys_sharedK_minus_dot_interaction_frac": two_way(jef)["interaction_frac"],
    "bhattacharyya_sharedK_interaction_frac_raw": two_way(bha)["interaction_frac"],
    "reverse_sharedQ_minus_dot_interaction_frac": two_way(rev_sq)["interaction_frac"],
    "forward_sharedQ_interaction_frac_raw": two_way(fwd_sq)["interaction_frac"]}


# ---------------------------------------------------------------- N. RoPE on full Gaussian pushforwards
def rope(pos, freqs):
    blocks = []
    for f in freqs:
        th = pos * f
        blocks.append(np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]]))
    return sla.block_diag(*blocks)


freqs = [1.0, 0.1, 0.01]
r = 6
aq, bk = rng.standard_normal(r), rng.standard_normal(r)
VQ_, VK_ = rand_spd(r, 50), rand_spd(r, 50)


def rot_kl(i, j):
    Ri, Rj = rope(i, freqs), rope(j, freqs)
    return kl_gauss(Ri @ aq, Ri @ VQ_ @ Ri.T, Rj @ bk, Rj @ VK_ @ Rj.T)


def rot_kl_mean_only(i, j):
    Ri, Rj = rope(i, freqs), rope(j, freqs)
    return kl_gauss(Ri @ aq, VQ_, Rj @ bk, VK_)


shift_full = max(abs(rot_kl(i + 17, j + 17) - rot_kl(i, j)) for i in range(5) for j in range(5))
shift_mean = max(abs(rot_kl_mean_only(i + 17, j + 17) - rot_kl_mean_only(i, j)) for i in range(5) for j in range(5))
lam = rng.uniform(0.5, 3, 3)
Vcomm = np.diag(np.repeat(lam, 2))
Rt = rope(5, freqs)
OUT["N_rope"] = {"full_pushforward_relative_position_max_residual": shift_full,
                 "mean_only_rotation_anisotropic_shift_violation": shift_mean,
                 "blockwise_isotropic_Vstar_commutes_residual": float(np.max(np.abs(Rt @ Vcomm @ Rt.T - Vcomm))),
                 "generic_Vstar_commutator_size": float(np.max(np.abs(Rt @ VK_ @ Rt.T - VK_)))}

# ---------------------------------------------------------------- O. mixture covariance
n, dim = 4, 3
beta = rng.dirichlet(np.ones(n)); v = rng.standard_normal((n, dim)); Wl = [rand_spd(dim) for _ in range(n)]
vbar = beta @ v
second = sum(beta[j] * (Wl[j] + np.outer(v[j], v[j])) for j in range(n))
cov_direct = second - np.outer(vbar, vbar)
cov_paper = sum(beta[j] * (Wl[j] + np.outer(v[j] - vbar, v[j] - vbar)) for j in range(n))
OUT["O_mixture_covariance_residual"] = float(np.max(np.abs(cov_direct - cov_paper)))

# ---------------------------------------------------------------- P. decoder: e-mixture (Gibbs) vs m-mixture (predictive)
sd = 2.0


def gpdf(x, m, s):
    return math.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))


def p1(x):
    return 1.0 / (1.0 + math.exp(2 - 2 * x))


def logp(v, x):
    z = 2 - 2 * x
    return -np.logaddexp(0, z) if v == 1 else -np.logaddexp(0, -z)


El = [quad(lambda x: gpdf(x, 0, sd) * logp(v, x), -60, 60, limit=200)[0] for v in (0, 1)]
rho = softmax(np.array(El))
pbar1 = quad(lambda x: gpdf(x, 0, sd) * p1(x), -60, 60, limit=200)[0]


def exp_rev_kl(t):
    return quad(lambda x: gpdf(x, 0, sd) * ((1 - t) * (math.log(1 - t) - logp(0, x)) + t * (math.log(t) - logp(1, x))), -60, 60, limit=200)[0]


def exp_fwd_kl(t):
    return quad(lambda x: gpdf(x, 0, sd) * ((1 - p1(x)) * (logp(0, x) - math.log(1 - t)) + p1(x) * (logp(1, x) - math.log(t))), -60, 60, limit=200)[0]


tr_ = minimize_scalar(exp_rev_kl, bounds=(1e-6, 1 - 1e-6), method="bounded", options={"xatol": 1e-12})
tf_ = minimize_scalar(exp_fwd_kl, bounds=(1e-6, 1 - 1e-6), method="bounded", options={"xatol": 1e-12})
OUT["P_decoder_e_vs_m"] = {"gibbs_rho1": float(rho[1]), "paper_1_over_1_plus_e2": 1 / (1 + math.e ** 2), "pbar1": pbar1,
                           "argmin_E_q_KL_r_to_pX": tr_.x, "argmin_E_q_KL_pX_to_r": tf_.x}

# ---------------------------------------------------------------- Q. supplement B.1 population residual
K = 3
Gam = rand_spd(2 * K, 40)
Sig_i, Sig_j, G_ij, G_ji = Gam[:K, :K], Gam[K:, K:], Gam[:K, K:], Gam[K:, :K]
Lk = rng.standard_normal((K, K)); Lk[:, -1] = 0.0
Tm = np.hstack([np.eye(K), -Lk])
V_direct = Tm @ Gam @ Tm.T
V_paper = Sig_i + Lk @ Sig_j @ Lk.T - G_ij @ Lk.T - Lk @ G_ji
mu_all = rng.standard_normal(2 * K); ebar = Tm @ mu_all
Rr = rand_spd(K)
cost_direct = np.trace(np.linalg.solve(Rr, V_direct + np.outer(ebar, ebar)))
cost_paper = ebar @ np.linalg.solve(Rr, ebar) + np.trace(np.linalg.solve(Rr, V_paper))
cc = 0.35
OUT["Q_population"] = {"V_residual": float(np.max(np.abs(V_direct - V_paper))), "cost_residual": float(abs(cost_direct - cost_paper)),
                       "scalar_example_2_1_minus_c": 2 * (1 - cc), "scalar_direct": 1 + 1 - 2 * cc}


# ---------------------------------------------------------------- R. supplement B.2 LayerNorm
def LN(x, eps):
    Kk = x.shape[-1]
    P0x = x - x.mean(-1, keepdims=True)
    return P0x / np.sqrt((P0x ** 2).sum(-1, keepdims=True) / Kk + eps)


X2 = rng.multivariate_normal(np.zeros(2), rand_spd(2), size=20000)
atoms = np.unique(np.round(LN(X2, 0.0), 12), axis=0)
X8 = rng.multivariate_normal(rng.standard_normal(8), rand_spd(8), size=20000)
Y8 = LN(X8, 1e-3)
OUT["R_layernorm"] = {"K2_eps0_distinct_outputs": atoms.tolist(),
                      "K8_eps_pos_max_abs_coordinate_sum": float(np.max(np.abs(Y8.sum(-1)))),
                      "K8_eps_pos_max_norm_sq": float(np.max((Y8 ** 2).sum(-1))), "bound_K": 8}

# ---------------------------------------------------------------- S. L7 sharp softmax perturbation bound
x, t = sp.symbols("x t", positive=True)
f = x * (1 - x) * (t - 1) / (1 + x * (t - 1))
crit = sp.solve(sp.Eq(sp.diff(f, x), 0), x)
xstar = 1 / (1 + sp.sqrt(t))
fstar_t = sp.simplify(f.subs(x, xstar))
e_s = sp.symbols("epsilon", positive=True)
tanh_res = sp.simplify((fstar_t.subs(t, sp.exp(2 * e_s)) - sp.tanh(e_s / 2)).rewrite(sp.exp))
second = sp.simplify(sp.diff(f, x, 2).subs(x, xstar))
ratio_max, ratio_paper = 0.0, 0.0
for _ in range(20000):
    n = int(rng.integers(2, 20)); e_ = float(rng.uniform(0.01, 3.0))
    p_ = rng.dirichlet(np.ones(n) * rng.uniform(0.2, 3)); dl = rng.uniform(-e_, e_, n)
    if rng.random() < 0.5:
        dl = np.where(rng.random(n) < 0.5, e_, -e_)
    b_ = p_ * np.exp(dl); b_ /= b_.sum()
    l1 = np.abs(b_ - p_).sum()
    ratio_max = max(ratio_max, l1 / (2 * math.tanh(e_ / 2)))
    ratio_paper = max(ratio_paper, l1 / (math.exp(2 * e_) - 1))
e_ = 0.7
p2 = np.array([1 / (1 + math.exp(e_)), math.exp(e_) / (1 + math.exp(e_))])
b2 = p2 * np.exp([e_, -e_]); b2 /= b2.sum()
OUT["S_L7_bound"] = {"sympy_critical_points": [str(c_) for c_ in crit], "sympy_f_at_xstar": str(fstar_t),
                     "sympy_f_at_xstar_minus_tanh_eps_over_2": str(tanh_res),
                     "sympy_second_derivative_at_xstar": str(second),
                     "random_max_L1_over_2tanh": ratio_max, "random_max_L1_over_paper_bound": ratio_paper,
                     "two_point_eps0.7_L1": float(np.abs(b2 - p2).sum()), "2tanh_0.35": 2 * math.tanh(0.35),
                     "paper_e1.4_minus_1": math.exp(1.4) - 1}

# ---------------------------------------------------------------- T. L5: cogredient GL(r) redundancy, moment map, conditioning
K, r, N = 6, 2, 5
Xi = rng.standard_normal((N, K)); Cs = [rand_spd(K, 30) for _ in range(N)]
SQ0, SK0 = rng.standard_normal((r, K)), rng.standard_normal((r, K))
tau = 1.1
targets = rng.integers(0, N, N)


def Dmat(SQ, SK):
    return np.array([[kl_gauss(SQ @ Xi[i], SQ @ Cs[i] @ SQ.T, SK @ Xi[j], SK @ Cs[j] @ SK.T) for j in range(N)] for i in range(N)])


def loss(SQ, SK):
    D = Dmat(SQ, SK)
    val = 0.0
    for i in range(N):
        z = -D[i] / tau
        val += -(z[targets[i]] - np.log(np.exp(z - z.max()).sum()) - z.max())
    return val


Ag = rand_gl(r, 1.5)
D0 = Dmat(SQ0, SK0)
res_cog = float(np.max(np.abs(Dmat(Ag @ SQ0, Ag @ SK0) - D0)) / np.max(np.abs(D0)))
res_contra = float(np.max(np.abs(Dmat(Ag @ SQ0, np.linalg.inv(Ag).T @ SK0) - D0)) / np.max(np.abs(D0)))
dot0 = (Xi @ SQ0.T) @ (Xi @ SK0.T).T
dot_contra = (Xi @ (Ag @ SQ0).T) @ (Xi @ (np.linalg.inv(Ag).T @ SK0).T).T
dot_cog = (Xi @ (Ag @ SQ0).T) @ (Xi @ (Ag @ SK0).T).T


def num_grad(fun, X, h=1e-6):
    G = np.zeros_like(X)
    for idx in np.ndindex(X.shape):
        Xp, Xm = X.copy(), X.copy(); Xp[idx] += h; Xm[idx] -= h
        G[idx] = (fun(Xp) - fun(Xm)) / (2 * h)
    return G


GQ = num_grad(lambda M: loss(M, SK0), SQ0)
GK = num_grad(lambda M: loss(SQ0, M), SK0)
Mmap = GQ @ SQ0.T + GK @ SK0.T
mm_rel = float(np.max(np.abs(Mmap)) / np.max(np.abs(GQ @ SQ0.T)))


def run(update, eta, steps):
    SQ, SK = SQ0.copy(), SK0.copy()
    Q0 = SQ @ SQ.T + SK @ SK.T
    L0 = loss(SQ, SK)
    for _ in range(steps):
        gq = num_grad(lambda M: loss(M, SK), SQ, 1e-6)
        gk = num_grad(lambda M: loss(SQ, M), SK, 1e-6)
        dq, dk = update(gq, gk)
        SQ, SK = SQ - eta * dq, SK - eta * dk
    Q1 = SQ @ SQ.T + SK @ SK.T
    return (float(np.linalg.norm(Q1 - Q0) / np.linalg.norm(Q0)), float(L0 - loss(SQ, SK)),
            float(np.sqrt(np.trace(Q1) / np.trace(Q0))))


gd_1 = run(lambda gq, gk: (gq, gk), 2e-3, 100)
gd_2 = run(lambda gq, gk: (gq, gk), 1e-3, 200)
sgn = run(lambda gq, gk: (np.sign(gq), np.sign(gk)), 2e-2, 100)
Ad = np.diag([1.0, 40.0])
VK0 = SK0 @ Cs[0] @ SK0.T; VQ0 = SQ0 @ Cs[1] @ SQ0.T
VKa = (Ad @ SK0) @ Cs[0] @ (Ad @ SK0).T; VQa = (Ad @ SQ0) @ Cs[1] @ (Ad @ SQ0).T
rel0 = np.sort(np.real(np.linalg.eigvals(np.linalg.solve(VK0, VQ0))))
rela = np.sort(np.real(np.linalg.eigvals(np.linalg.solve(VKa, VQa))))
OUT["T_L5_redundancy"] = {
    "D_cogredient_rel_residual": res_cog,
    "D_contragredient_rel_change": res_contra,
    "dot_contragredient_rel_residual": float(np.max(np.abs(dot_contra - dot0)) / np.max(np.abs(dot0))),
    "dot_cogredient_rel_change": float(np.max(np.abs(dot_cog - dot0)) / np.max(np.abs(dot0))),
    "moment_map_rel_to_GQ_SQt": mm_rel,
    "trace_moment_map": float(np.trace(Mmap)),
    "GD_eta2e-3_100steps_relQdrift_lossdrop_normratio": gd_1,
    "GD_eta1e-3_200steps_relQdrift_lossdrop_normratio": gd_2,
    "signGD_eta2e-2_100steps_relQdrift_lossdrop_normratio": sgn,
    "cond_VK_before": float(np.linalg.cond(VK0)), "cond_VK_after_diag_1_40": float(np.linalg.cond(VKa)),
    "min_sv_SK_before": float(np.linalg.svd(SK0, compute_uv=False).min()),
    "min_sv_SK_after": float(np.linalg.svd(Ad @ SK0, compute_uv=False).min()),
    "relative_spectrum_rel_residual": float(np.max(np.abs(rel0 - rela)) / np.max(np.abs(rel0)))}

# ---------------------------------------------------------------- U. query uncertainty in Gibbs vs predictive source weights
bks = np.array([0.0, 2.0])
aq1 = 0.5


def gibbs(vq):
    return softmax(np.array([-kl_gauss(np.array([aq1]), np.array([[vq]]), np.array([b]), np.eye(1)) for b in bks]))


def predictive(vq):
    f0 = quad(lambda yy: gpdf(yy, aq1, math.sqrt(vq)) * softmax(np.array([-(yy - b) ** 2 / 2 for b in bks]))[0], -80, 80, limit=400)[0]
    return np.array([f0, 1 - f0])


UQ = {}
for vq in (0.01, 1.0, 10.0, 100.0):
    UQ["v_q=" + str(vq)] = {"gibbs": gibbs(vq).tolist(), "posterior_predictive": predictive(vq).tolist()}
OUT["U_query_uncertainty"] = UQ

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "infogeo_checks.json")
with open(path, "w", encoding="utf-8") as fh:
    json.dump(OUT, fh, indent=1, default=float)
print(json.dumps(OUT, indent=1, default=float))
