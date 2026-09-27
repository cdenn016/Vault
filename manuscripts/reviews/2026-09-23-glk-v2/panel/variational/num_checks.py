"""Numerical checks (NumPy/SciPy, CPU) for the variational lens of the GL(K) v2 pair.
Seeded; every printed number is a residual or a reported value."""
import itertools, json, math
import numpy as np
from scipy import integrate, optimize, special, stats

rng = np.random.default_rng(20260923)
R = {}

def spd(n, scale=1.0):
    A = rng.normal(size=(n, n))
    return scale * (A @ A.T / n + 0.3 * np.eye(n))

def kl_gauss(m0, S0, m1, S1):
    k = len(m0); P1 = np.linalg.inv(S1); d = m1 - m0
    return 0.5 * (np.trace(P1 @ S0) + d @ P1 @ d - k + np.linalg.slogdet(S1)[1] - np.linalg.slogdet(S0)[1])

def softmax(x):
    x = np.asarray(x, float); x = x - x.max(); e = np.exp(x); return e / e.sum()

# ---------- N1 mixture free energy (1-D quadrature, no use of the identity) ----------
tau = 1.0
mq, sq = 0.3, 0.7
mk = rng.normal(size=4); sk = rng.uniform(0.4, 1.5, size=4)
pi = rng.dirichlet(np.ones(4)); beta = rng.dirichlet(np.ones(4))
def integrand(y, j):
    lq = stats.norm.logpdf(y, mq, math.sqrt(sq)); lp = stats.norm.logpdf(y, mk[j], math.sqrt(sk[j]))
    return beta[j] * math.exp(lq) * (math.log(beta[j]) + lq - math.log(pi[j]) - lp)
lhs = sum(integrate.quad(integrand, -30, 30, args=(j,), epsabs=1e-13, epsrel=1e-13, limit=400)[0] for j in range(4))
Dj = np.array([kl_gauss(np.array([mq]), np.array([[sq]]), np.array([mk[j]]), np.array([[sk[j]]])) for j in range(4)])
rhs = beta @ Dj + np.sum(beta * np.log(beta / pi))
R["N1_mixture_KL_quadrature_residual"] = abs(lhs - rhs)

# ---------- N2 Gibbs completion, value, envelope (random, several tau) ----------
worst = 0.0; worst_env = 0.0
for t in (0.05, 0.3, 1.0, math.sqrt(32), 17.0):
    for _ in range(200):
        n = rng.integers(2, 9); D = rng.normal(scale=3, size=n); p = rng.dirichlet(np.ones(n)); b = rng.dirichlet(np.ones(n))
        logZ = special.logsumexp(np.log(p) - D / t); bs = np.exp(np.log(p) - D / t - logZ)
        A = b @ D + t * np.sum(b * np.log(b / p)); comp = t * np.sum(b * np.log(b / bs)) - t * logZ
        worst = max(worst, abs(A - comp), abs((bs @ D + t * np.sum(bs * np.log(bs / p))) + t * logZ))
        h = 1e-6; e = np.zeros(n); e[0] = 1
        dval = (-t * special.logsumexp(np.log(p) - (D + h * e) / t) + t * special.logsumexp(np.log(p) - (D - h * e) / t)) / (2 * h)
        worst_env = max(worst_env, abs(dval - bs[0]))
R["N2_gibbs_completion_and_value_max_residual"] = worst
R["N2_envelope_dvalue_dD_minus_beta_max"] = worst_env

# ---------- N3 content-law cancellation (discrete y, z) ----------
ny, nz, nj = 5, 6, 4
pK = rng.dirichlet(np.ones(ny), size=nj); qQ = rng.dirichlet(np.ones(ny)); r = rng.dirichlet(np.ones(nz), size=nj)
p_joint = pi[:, None, None] * pK[:, :, None] * r[:, None, :]
q_joint = beta[:, None, None] * qQ[None, :, None] * r[:, None, :]
KLjoint = np.sum(q_joint * np.log(q_joint / p_joint))
KLrhs = sum(beta[j] * np.sum(qQ * np.log(qQ / pK[j])) for j in range(nj)) + np.sum(beta * np.log(beta / pi))
R["N3_content_cancellation_residual"] = abs(KLjoint - KLrhs)
R["N3_joint_masses"] = [float(p_joint.sum()), float(q_joint.sum())]
z_vals = rng.normal(size=nz)
R["N3_recognition_content_mean_minus_sum_beta_mean_r"] = abs(np.sum(q_joint.sum(axis=1) * z_vals[None, :]) - beta @ (r @ z_vals))

# ---------- N4 shared-latent correction: formula vs independent KKT (Gaussian MAP = conditional mean) ----------
K, rr, s = 4, 2, 3
worst4 = 0.0
for Rcase in ("pd", "psd_singular", "zero"):
    xi = rng.normal(size=K); C = spd(K); SK = rng.normal(size=(rr, K)); T = rng.normal(size=(s, K))
    if Rcase == "pd":
        Rn = spd(rr, 0.5)
    elif Rcase == "psd_singular":
        v = rng.normal(size=(rr, 1)); Rn = v @ v.T
    else:
        Rn = np.zeros((rr, rr))
    y = rng.normal(size=rr)
    formula = T @ xi + T @ C @ SK.T @ np.linalg.solve(SK @ C @ SK.T + Rn, y - SK @ xi)
    # KKT: minimize (x-xi)^T C^-1 (x-xi) + u^T u  s.t.  SK x + Rh u = y, with Rh Rh^T = Rn
    w_, V_ = np.linalg.eigh(Rn); Rh = V_ @ np.diag(np.sqrt(np.clip(w_, 0, None)))
    Ci = np.linalg.inv(C)
    KKT = np.block([[Ci, np.zeros((K, rr)), SK.T], [np.zeros((rr, K)), np.eye(rr), Rh.T], [SK, Rh, np.zeros((rr, rr))]])
    rhs = np.concatenate([Ci @ xi, np.zeros(rr), y])
    sol = np.linalg.solve(KKT, rhs)
    worst4 = max(worst4, float(np.max(np.abs(formula - T @ sol[:K]))))
R["N4_shared_latent_formula_vs_KKT_conditioning_max"] = worst4

# Monte Carlo: recognition Q(j,y,x)=beta_j qQ(y) p(x|y,j) has content mean sum_j beta_j T(xi_j + C_j S^T (V_j+R)^{-1}(a-b_j))
nj4 = 3; a_q = rng.normal(size=rr); VQ = spd(rr, 0.4)
xis = rng.normal(size=(nj4, K)); Cs = [spd(K) for _ in range(nj4)]; Rn = spd(rr, 0.3); b4 = rng.dirichlet(np.ones(nj4))
Nmc = 400000; mc = np.zeros(s); var_bound = 0.0
for j in range(nj4):
    Syy = SK @ Cs[j] @ SK.T + Rn; Gain = Cs[j] @ SK.T @ np.linalg.inv(Syy)
    ys = rng.multivariate_normal(a_q, VQ, size=Nmc)
    condcov = Cs[j] - Gain @ SK @ Cs[j]
    xs = (xis[j] + (ys - SK @ xis[j]) @ Gain.T) + rng.multivariate_normal(np.zeros(K), condcov, size=Nmc)
    vals = xs @ T.T
    mc += b4[j] * vals.mean(axis=0)
    var_bound += (b4[j] ** 2) * vals.var(axis=0).max() / Nmc
closed = sum(b4[j] * (T @ (xis[j] + Cs[j] @ SK.T @ np.linalg.solve(SK @ Cs[j] @ SK.T + Rn, a_q - SK @ xis[j]))) for j in range(nj4))
uncorr = sum(b4[j] * (T @ xis[j]) for j in range(nj4))
R["N4_MC_shared_latent_recognition_mean_minus_closed_form_maxabs"] = float(np.max(np.abs(mc - closed)))
R["N4_MC_3sigma"] = float(3 * math.sqrt(var_bound))
R["N4_shared_latent_minus_uncorrected_mixture_mean_maxabs"] = float(np.max(np.abs(closed - uncorr)))

# ---------- N5 ELBO identity (discrete latent, correlated Q) ----------
nzz = 6; pz = rng.dirichlet(np.ones(nzz))
lik1 = rng.dirichlet(np.ones(3), size=nzz); lik2 = rng.dirichlet(np.ones(4), size=nzz)
o1, o2 = 1, 2
joint_o = pz * lik1[:, o1] * lik2[:, o2]
logpo = math.log(joint_o.sum()); post = joint_o / joint_o.sum()
Qz = rng.dirichlet(np.ones(nzz))
L = np.sum(Qz * (np.log(joint_o) - np.log(Qz))); KLq = np.sum(Qz * np.log(Qz / post))
R["N5_ELBO_identity_residual"] = abs(logpo - (L + KLq))
mass = sum(pz[z] * lik1[z, a] * lik2[z, c] for z in range(nzz) for a in range(3) for c in range(4))
R["N5_total_mass_minus_1"] = abs(mass - 1)

# ---------- N6 Bernoulli compatibility record model ----------
def bernoulli_model(tau, nz=4, cyclic=True, cost="kl_nonneg", cap=None):
    N = 3
    S = {0: [1, 2], 1: [0, 2], 2: [0, 1]} if cyclic else {0: [0], 1: [0, 1], 2: [0, 1, 2]}
    pz = rng.dirichlet(np.ones(nz))
    pis = {i: rng.dirichlet(np.ones(len(S[i]))) for i in range(N)}
    if cost == "kl_nonneg":
        Dz = {i: rng.gamma(2.0, 2.0, size=(nz, len(S[i]))) for i in range(N)}
    else:
        Dz = {i: rng.normal(scale=4.0, size=(nz, len(S[i]))) for i in range(N)}
    if cap is not None:
        Dz = {i: np.clip(Dz[i], 0.0, cap) for i in range(N)}
    shift = {i: (Dz[i].min(axis=1, keepdims=True) if cost != "kl_nonneg" else 0.0) for i in range(N)}
    P1 = {i: np.exp(-(Dz[i] - shift[i]) / tau) for i in range(N)}
    return N, S, pz, pis, Dz, P1

out6 = {}
for tau in (0.25, 1.0, math.sqrt(32), 10.0):
    for cost, cap in (("kl_nonneg", None), ("kl_nonneg", 3.0), ("real", None)):
        N, S, pz, pis, Dz, P1 = bernoulli_model(tau, cost=cost, cap=cap)
        assert all((P1[i] > 0).all() and (P1[i] <= 1 + 1e-15).all() for i in range(N))
        labs = [range(len(S[i])) for i in range(N)]
        mass = 0.0
        for z in range(len(pz)):
            for J in itertools.product(*labs):
                w = pz[z] * np.prod([pis[i][J[i]] for i in range(N)])
                for o in itertools.product((0, 1), repeat=N):
                    rec = np.prod([P1[i][z, J[i]] if o[i] == 1 else (1 - P1[i][z, J[i]]) for i in range(N)])
                    mass += w * rec
        worst_post = 0.0
        for z in range(len(pz)):
            wts = {}
            for J in itertools.product(*labs):
                wts[J] = np.prod([pis[i][J[i]] * P1[i][z, J[i]] for i in range(N)])
            tot = sum(wts.values())
            for J, wv in wts.items():
                prod_rows = np.prod([softmax(np.log(pis[i]) - Dz[i][z] / tau)[J[i]] for i in range(N)])
                worst_post = max(worst_post, abs(wv / tot - prod_rows))
        Qz = rng.dirichlet(np.ones(len(pz))); betas = {i: rng.dirichlet(np.ones(len(S[i]))) for i in range(N)}
        def Ffull(bdict):
            tot = 0.0; lp = []
            for z in range(len(pz)):
                for J in itertools.product(*labs):
                    qv = Qz[z] * np.prod([bdict[i][J[i]] for i in range(N)])
                    logp = math.log(pz[z]) + sum(math.log(pis[i][J[i]]) + math.log(P1[i][z, J[i]]) for i in range(N))
                    tot += qv * (math.log(qv) - logp); lp.append(logp)
            return tot, special.logsumexp(lp)
        F, logpo6 = Ffull(betas)
        dec = np.sum(Qz * np.log(Qz / pz))
        for i in range(N):
            ED = Qz @ Dz[i]
            dec += np.sum(betas[i] * np.log(betas[i] / pis[i])) + betas[i] @ ED / tau
            if cost != "kl_nonneg":
                dec -= Qz @ (Dz[i].min(axis=1)) / tau
        opt = optimize.minimize(lambda th: Ffull({0: softmax(th), 1: betas[1], 2: betas[2]})[0], np.zeros(len(S[0])), method="BFGS", options={"gtol": 1e-12})
        b_formula = softmax(np.log(pis[0]) - (Qz @ Dz[0]) / tau)
        b_avg_pointwise = sum(Qz[z] * softmax(np.log(pis[0]) - Dz[0][z] / tau) for z in range(len(pz)))
        out6[f"tau={tau:.4g},cost={cost},cap={cap}"] = {
            "mass_minus_1": abs(mass - 1),
            "cond_posterior_vs_product_gibbs_max": worst_post,
            "F_minus_decomposition": abs(F - dec),
            "F_plus_log_p(o)_nonneg": F + logpo6,
            "coord_opt_numeric_minus_formula_max": float(np.max(np.abs(softmax(opt.x) - b_formula))),
            "TV(recog_opt,E_Qz_pointwise_posterior)": float(0.5 * np.abs(b_formula - b_avg_pointwise).sum()),
        }
R["N6_bernoulli_record"] = out6

# ---------- N7 mixture-of-channels transition kernel, vector case ----------
K, H, nS = 3, 2, 3   # sources: 0 = receiver itself (causal self edge), 1, 2
mus = rng.normal(size=(nS, K)); Sigs = [spd(K) for _ in range(nS)]; Qi = spd(K, 0.2)
Ls = {(h, j): np.outer(rng.normal(size=K), rng.normal(size=K)) for h in range(H) for j in range(nS)}
betas7 = [rng.dirichlet(np.ones(nS)) for _ in range(H)]

def kernel_moments(mus, Sigs, Ls, Qi):
    mm = np.zeros(K); m2 = np.zeros((K, K))
    for J in itertools.product(range(nS), repeat=H):
        w = np.prod([betas7[h][J[h]] for h in range(H)])
        A = {j: (np.eye(K) if j == 0 else np.zeros((K, K))) for j in range(nS)}
        for h in range(H):
            A[J[h]] = A[J[h]] + Ls[(h, J[h])]
        m = sum(A[j] @ mus[j] for j in range(nS)); Cv = Qi + sum(A[j] @ Sigs[j] @ A[j].T for j in range(nS))
        mm += w * m; m2 += w * (Cv + np.outer(m, m))
    return mm, m2 - np.outer(mm, mm)

mix_m, mix_C = kernel_moments(mus, Sigs, Ls, Qi)
att_mean = mus[0] + sum(betas7[h][j] * Ls[(h, j)] @ mus[j] for h in range(H) for j in range(nS))
closed = Qi + Sigs[0].copy()
for h in range(H):
    closed += betas7[h][0] * (Ls[(h, 0)] @ Sigs[0] + Sigs[0] @ Ls[(h, 0)].T)
for j in range(nS):
    for h in range(H):
        for hp in range(H):
            coef = betas7[h][j] if h == hp else betas7[h][j] * betas7[hp][j]
            closed += coef * Ls[(h, j)] @ Sigs[j] @ Ls[(hp, j)].T
for h in range(H):
    mh = sum(betas7[h][j] * Ls[(h, j)] @ mus[j] for j in range(nS))
    closed += sum(betas7[h][j] * np.outer(Ls[(h, j)] @ mus[j], Ls[(h, j)] @ mus[j]) for j in range(nS)) - np.outer(mh, mh)
R["N7_mixture_mean_minus_attention_residual_max"] = float(np.max(np.abs(mix_m - att_mean)))
R["N7_mixture_cov_minus_closed_form_max"] = float(np.max(np.abs(mix_C - closed)))
R["N7_eigs(moment_matched_minus_passthrough)"] = [float(x) for x in np.linalg.eigvalsh(mix_C - Sigs[0])]
gs = [np.eye(K) + 0.5 * rng.normal(size=(K, K)) for _ in range(nS)]
mus_g = np.array([gs[j] @ mus[j] for j in range(nS)]); Sigs_g = [gs[j] @ Sigs[j] @ gs[j].T for j in range(nS)]
Ls_g = {(h, j): gs[0] @ Ls[(h, j)] @ np.linalg.inv(gs[j]) for h in range(H) for j in range(nS)}
Qi_g = gs[0] @ Qi @ gs[0].T
mm_g, C_g = kernel_moments(mus_g, Sigs_g, Ls_g, Qi_g)
R["N7_passive_covariance_mean_max"] = float(np.max(np.abs(mm_g - gs[0] @ mix_m)))
R["N7_passive_covariance_cov_max"] = float(np.max(np.abs(C_g - gs[0] @ mix_C @ gs[0].T)))
Wj = [spd(K) for _ in range(nS)]; vj = rng.normal(size=(nS, K)); bb = rng.dirichlet(np.ones(nS)); vbar = bb @ vj
paper = sum(bb[j] * (Wj[j] + np.outer(vj[j] - vbar, vj[j] - vbar)) for j in range(nS))
direct = sum(bb[j] * (Wj[j] + np.outer(vj[j], vj[j])) for j in range(nS)) - np.outer(vbar, vbar)
R["N7_paper_line1069_mixture_cov_residual"] = float(np.max(np.abs(paper - direct)))

# ---------- N8 linear decoder as Gibbs readout of shared-covariance templates ----------
Vv, K8 = 7, 4
W = rng.normal(size=(Vv, K8)); bo = rng.normal(size=Vv); kappa = 0.7; puni = rng.dirichlet(np.ones(Vv))
Sstar = spd(K8)
mu_v = (Sstar @ W.T).T
log_omega = bo + kappa * np.log(puni) + 0.5 * np.einsum("vk,kl,vl->v", W, Sstar, W)
log_omega -= special.logsumexp(log_omega)
worst8 = 0.0
for _ in range(50):
    m = rng.normal(size=K8) * 3; Sq = spd(K8, rng.uniform(0.1, 5))
    gibbs = softmax(log_omega - np.array([kl_gauss(m, Sq, mu_v[v], Sstar) for v in range(Vv)]))
    lin = softmax(W @ m + bo + kappa * np.log(puni))
    worst8 = max(worst8, float(np.max(np.abs(gibbs - lin))))
R["N8_linear_decoder_equals_shared_cov_gibbs_readout_max"] = worst8

# ---------- N9 Gibbs readout vs predictive average; Jensen ordering ----------
KL0 = kl_gauss(np.array([0.0]), np.array([[4.0]]), np.array([0.0]), np.array([[1.0]]))
KL1 = kl_gauss(np.array([0.0]), np.array([[4.0]]), np.array([2.0]), np.array([[1.0]]))
rho = softmax([-KL0, -KL1])
pbar1 = integrate.quad(lambda x: stats.norm.pdf(x, 0, 2) / (1 + math.exp(2 - 2 * x)), -40, 40, epsabs=1e-14)[0]
def elogp(v):
    sgn = 1.0 if v == 1 else -1.0
    return integrate.quad(lambda x: stats.norm.pdf(x, 0, 2) * (-np.logaddexp(0.0, sgn * (2 - 2 * x))), -40, 40, epsabs=1e-14)[0]
elog = [elogp(0), elogp(1)]
R["N9_rho1_pbar1"] = [float(rho[1]), pbar1]
R["N9_log_rho_minus_Elog_p(v|X)"] = [float(math.log(rho[v]) - elog[v]) for v in (0, 1)]
R["N9_log_pbar_minus_Elog_p(v|X)"] = [float(math.log([1 - pbar1, pbar1][v]) - elog[v]) for v in (0, 1)]

# ---------- N10 R5 counterexample and exclusivity counterexample ----------
pJ = np.array([[0.45, 0.05], [0.05, 0.45]]); b2 = np.array([0.9, 0.1])
b1 = softmax(np.array([b2 @ np.log(pJ[0]), b2 @ np.log(pJ[1])]))
R["N10_R5_correlated_prior_coordinate"] = [float(x) for x in b1]
g = np.array([0.8, 0.2]); Dz = np.array([0.4, 1.3]); pi2 = np.array([0.5, 0.5])
R["N10_extra_label_factor_row"] = [float(x) for x in softmax(np.log(pi2) - Dz + np.log(g))]
R["N10_exclusive_row"] = [float(x) for x in softmax(np.log(pi2) - Dz)]

print(json.dumps(R, indent=1, default=float))
