r"""L10 (numerics) float64 central finite-difference checks of every transcribable
gradient formula in PIFB2.tex Appendix A (lines 2212-2515).

Scalar under test (PIFB2 2227-2236, belief channel only, uniform support pi):
  S_surr = sum_i alpha_i KL(q_i||p_i) + sum_i sum_{j!=i} beta_ij KL(q_i||Omega_ij q_j),
  beta_ij = softmax_j(-KL_ij / kappa),  Omega_ij = expm(phi_i) expm(-phi_j),  phi_i in gl(K).
Canonical (entropy-retaining) scalar: add kappa * sum_ij beta_ij log beta_ij.
"""
import numpy as np
from scipy.linalg import expm, expm_frechet

rng = np.random.default_rng(20260924)
b0, c0, kappa = 0.7, 1.3, 0.9
H = 1e-6

def spd(K):
    A = rng.standard_normal((K, K)); return A @ A.T + 0.5 * np.eye(K)

def kl(mq, Sq, mp, Sp):
    K = len(mq); Spi = np.linalg.inv(Sp); d = mp - mq
    return 0.5 * (np.linalg.slogdet(Sp)[1] - np.linalg.slogdet(Sq)[1] + np.trace(Spi @ Sq) + d @ Spi @ d - K)

def gens(K):
    G = []
    for a in range(K):
        for b in range(K):
            E = np.zeros((K, K)); E[a, b] = 1.0; G.append(E)
    return G

class State:
    def __init__(s, K, N, scale=0.6):
        s.K, s.N = K, N
        s.mu = [rng.standard_normal(K) for _ in range(N)]
        s.Sig = [spd(K) for _ in range(N)]
        s.phi = [scale * rng.standard_normal((K, K)) for _ in range(N)]
        s.mp = [rng.standard_normal(K) for _ in range(N)]
        s.Sp = [spd(K) for _ in range(N)]
    def copy(s):
        t = State.__new__(State); t.K, t.N = s.K, s.N
        for k in ("mu", "Sig", "phi", "mp", "Sp"):
            setattr(t, k, [x.copy() for x in getattr(s, k)])
        return t

def Om(s, i, j): return expm(s.phi[i]) @ expm(-s.phi[j])

def E(s, i, j):
    O = Om(s, i, j); return kl(s.mu[i], s.Sig[i], O @ s.mu[j], O @ s.Sig[j] @ O.T)

def betas(s):
    B = np.zeros((s.N, s.N)); Em = np.zeros((s.N, s.N))
    for i in range(s.N):
        js = [j for j in range(s.N) if j != i]
        e = np.array([E(s, i, j) for j in js]); Em[i, js] = e
        w = np.exp(-(e - e.min()) / kappa); B[i, js] = w / w.sum()
    return B, Em

def scalar(s, alpha_mode="auto", entropy=False):
    B, Em = betas(s); tot = 0.0
    for i in range(s.N):
        kp = kl(s.mu[i], s.Sig[i], s.mp[i], s.Sp[i]); a = c0 / (b0 + kp)
        tot += a * kp if alpha_mode == "auto" else s._afix[i] * kp
        for j in range(s.N):
            if j != i:
                tot += B[i, j] * Em[i, j]
                if entropy and B[i, j] > 0: tot += kappa * B[i, j] * np.log(B[i, j])
    return tot

def fd(s, f, field, i, D):
    sp, sm = s.copy(), s.copy()
    getattr(sp, field)[i] = getattr(sp, field)[i] + H * D
    getattr(sm, field)[i] = getattr(sm, field)[i] - H * D
    if hasattr(s, "_afix"): sp._afix = sm._afix = s._afix
    return (f(sp) - f(sm)) / (2 * H)

def rel(a, b): return np.linalg.norm(np.ravel(a) - np.ravel(b)) / max(np.linalg.norm(np.ravel(b)), 1e-300)

# ---------- analytic pieces transcribed from the manuscript ----------
def dKL_dmu_recv(s, i, j):  # 2260
    O = Om(s, i, j); A = O @ s.Sig[j] @ O.T; return np.linalg.solve(A, s.mu[i] - O @ s.mu[j])
def dKL_dSig_recv(s, i, j):  # 2307
    O = Om(s, i, j); A = O @ s.Sig[j] @ O.T; return 0.5 * (-np.linalg.inv(s.Sig[i]) + np.linalg.inv(A))
def N_mat(s, i, j):  # bracket of eq:kl_omega_directional (2377)
    O = Om(s, i, j); A = O @ s.Sig[j] @ O.T; L = np.linalg.inv(A); r = s.mu[i] - O @ s.mu[j]
    return np.eye(s.K) - L @ s.Sig[i] - np.outer(L @ r, O @ s.mu[j]) - np.outer(L @ r, r)
def dKL_dOmega(s, i, j):  # eq:kl_omega_unconstrained (2382), both printed forms
    O = Om(s, i, j); A = O @ s.Sig[j] @ O.T; L = np.linalg.inv(A); r = s.mu[i] - O @ s.mu[j]; OiT = np.linalg.inv(O).T
    f1 = N_mat(s, i, j) @ OiT
    f2 = OiT - L @ s.Sig[i] @ OiT - np.outer(L @ r, s.mu[j]) - np.outer(L @ r, r) @ L @ O @ s.Sig[j]
    return f1, f2
def dOm_dphi_recv(s, i, j, G): return expm_frechet(s.phi[i], G, compute_expm=False) @ expm(-s.phi[j])  # 2367
def dKL_dphi_recv(s, i, j, G):  # chain rule 2372
    return np.trace(dOm_dphi_recv(s, i, j, G).T @ dKL_dOmega(s, i, j)[0])
def dE_dmu_send(s, l, i):  # 2435
    O = Om(s, l, i); return np.linalg.inv(s.Sig[i]) @ np.linalg.solve(O, O @ s.mu[i] - s.mu[l])
def dE_dSig_send(s, l, i):  # 2436
    O = Om(s, l, i); Lt = np.linalg.inv(O @ s.Sig[i] @ O.T); d = O @ s.mu[i] - s.mu[l]
    return 0.5 * O.T @ (Lt - Lt @ (s.Sig[l] + np.outer(d, d)) @ Lt) @ O
def dE_dphi_send_exact(s, l, i, G):  # 2453-2457
    O = Om(s, l, i); Ja = expm_frechet(-s.phi[i], G, compute_expm=False)
    return -np.trace(Ja.T @ expm(s.phi[l]).T @ N_mat(s, l, i) @ np.linalg.inv(O).T)
def dE_dphi_send_abelian(s, l, i, G):  # eq:sender_phi_gradient 2447
    O = Om(s, l, i); return -np.trace(G.T @ (O.T @ N_mat(s, l, i) @ np.linalg.inv(O).T))

def total_grad(s, field, i, alpha_eff, responses=True):
    """Receiver (2279/2312/2410) + sender (eq:sender_autograd 2470) assembled."""
    B, Em = betas(s); K = s.K
    if field == "mu":
        self_g = np.linalg.solve(s.Sp[i], s.mu[i] - s.mp[i]); recv = lambda j: dKL_dmu_recv(s, i, j); send = lambda l: dE_dmu_send(s, l, i)
    elif field == "Sig":
        self_g = 0.5 * (-np.linalg.inv(s.Sig[i]) + np.linalg.inv(s.Sp[i])); recv = lambda j: dKL_dSig_recv(s, i, j); send = lambda l: dE_dSig_send(s, l, i)
    else:
        Gs = gens(K); self_g = np.zeros((K, K))
        recv = lambda j: np.array([dKL_dphi_recv(s, i, j, G) for G in Gs]).reshape(K, K)
        send = lambda l: np.array([dE_dphi_send_exact(s, l, i, G) for G in Gs]).reshape(K, K)
    g = alpha_eff * self_g
    js = [j for j in range(s.N) if j != i]
    rbar = sum(B[i, j] * Em[i, j] for j in js)
    for j in js:
        g = g + B[i, j] * recv(j) * ((1 - Em[i, j] / kappa) if responses else 1.0)
    if responses:
        g = g + (rbar / kappa) * sum(B[i, k] * recv(k) for k in js)  # R_mu
    for l in js:
        lbar = sum(B[l, m] * Em[l, m] for m in range(s.N) if m != l)
        g = g + B[l, i] * send(l) * ((1 - Em[l, i] / kappa) if responses else 1.0)
        if responses: g = g + (lbar / kappa) * B[l, i] * send(l)  # R_mu^(s)
    return g

def fd_field(s, f, field, i):
    K = s.K
    if field == "mu":
        return np.array([fd(s, f, "mu", i, np.eye(K)[a]) for a in range(K)])
    if field == "phi":
        return np.array([fd(s, f, "phi", i, G) for G in gens(K)]).reshape(K, K)
    G = np.zeros((K, K))  # symmetric gradient from symmetric directions
    for a in range(K):
        for b in range(a, K):
            Dm = np.zeros((K, K)); Dm[a, b] = 1; Dm[b, a] = 1
            v = fd(s, f, "Sig", i, Dm)
            if a == b: G[a, a] = v
            else: G[a, b] = G[b, a] = v / 2
    return G

out = {}
def rec(name, val):
    assert np.isfinite(val), name
    out[name] = max(out.get(name, 0.0), val)

if __name__ == "__main__":
    for K in (2, 3):
        for trial in range(3):
            s = State(K, 3)
            i, j = 0, 1
            f_pair = lambda t: E(t, i, j)
            rec("dKL/dmu_i receiver (2260)", rel(dKL_dmu_recv(s, i, j), fd_field(s, f_pair, "mu", i)))
            rec("dKL/dSigma_i receiver (2307)", rel(dKL_dSig_recv(s, i, j), fd_field(s, f_pair, "Sig", i)))
            f_send = lambda t: E(t, j, i)
            rec("dE_li/dmu_i sender (2435)", rel(dE_dmu_send(s, j, i), fd_field(s, f_send, "mu", i)))
            rec("dE_li/dSigma_i sender (2436)", rel(dE_dSig_send(s, j, i), fd_field(s, f_send, "Sig", i)))
            O = Om(s, i, j); f1, f2 = dKL_dOmega(s, i, j)
            def KLofO(Ox): return kl(s.mu[i], s.Sig[i], Ox @ s.mu[j], Ox @ s.Sig[j] @ Ox.T)
            gO = np.array([(KLofO(O + H * Gm) - KLofO(O - H * Gm)) / (2 * H) for Gm in gens(K)]).reshape(K, K)
            rec("dKL/dOmega = N Omega^{-T} (2382 first form)", rel(f1, gO))
            rec("dKL/dOmega expanded (2382 second form)", rel(f2, gO))
            X = rng.standard_normal((K, K))
            dX = (KLofO(expm(H * X) @ O) - KLofO(expm(-H * X) @ O)) / (2 * H)
            rec("directional d_X KL = tr(X^T N) (2377)", abs(np.trace(X.T @ N_mat(s, i, j)) - dX) / abs(dX))
            xs, ws = np.polynomial.legendre.leggauss(40); xs = 0.5 * (xs + 1); ws = 0.5 * ws
            Ga = gens(K)[1]
            quad = sum(w * expm((1 - x) * s.phi[i]) @ Ga @ expm(x * s.phi[i]) for x, w in zip(xs, ws)) @ expm(-s.phi[j])
            fdO = (expm(s.phi[i] + H * Ga) - expm(s.phi[i] - H * Ga)) / (2 * H) @ expm(-s.phi[j])
            rec("Frechet dOmega/dphi_i receiver integral (2367)", rel(quad, fdO))
            quads = -expm(s.phi[j]) @ sum(w * expm(-(1 - x) * s.phi[i]) @ Ga @ expm(-x * s.phi[i]) for x, w in zip(xs, ws))
            fdOs = expm(s.phi[j]) @ (expm(-(s.phi[i] + H * Ga)) - expm(-(s.phi[i] - H * Ga))) / (2 * H)
            rec("Frechet dOmega_li/dphi_i sender integral (2442)", rel(quads, fdOs))
            g_r = np.array([dKL_dphi_recv(s, i, j, G) for G in gens(K)]).reshape(K, K)
            rec("dKL_ij/dphi_i receiver exact (2372+2382)", rel(g_r, fd_field(s, f_pair, "phi", i)))
            g_s = np.array([dE_dphi_send_exact(s, j, i, G) for G in gens(K)]).reshape(K, K)
            rec("dE_li/dphi_i sender exact (2453-2457)", rel(g_s, fd_field(s, f_send, "phi", i)))
            kp = kl(s.mu[i], s.Sig[i], s.mp[i], s.Sp[i]); astar = c0 / (b0 + kp)
            f_auto = lambda t: scalar(t, "auto")
            s._afix = [c0 / (b0 + kl(s.mu[k], s.Sig[k], s.mp[k], s.Sp[k])) for k in range(s.N)]
            f_fix = lambda t: scalar(t, "fix")
            f_ent = lambda t: scalar(t, "fix", entropy=True)
            for field in ("mu", "Sig", "phi"):
                rec(f"total surrogate grad {field}, alpha autograd (alpha_eff=a*^2 b0/c0; 2279/2312/2410 + 2470)",
                    rel(total_grad(s, field, i, astar ** 2 * b0 / c0), fd_field(s, f_auto, field, i)))
                rec(f"total surrogate grad {field}, alpha frozen (alpha_eff=a*)",
                    rel(total_grad(s, field, i, astar), fd_field(s, f_fix, field, i)))
                rec(f"canonical energy+entropy grad {field} = sum beta grad E, no response (2239/2489)",
                    rel(total_grad(s, field, i, astar, responses=False), fd_field(s, f_ent, field, i)))
                gfull = total_grad(s, field, i, astar ** 2 * b0 / c0)
                # size of the sender block dropped by a receiver-only field (2286, 2430)
                B, Em = betas(s)
    print("max relative error over K in {2,3}, 3 random draws each, N=3 agents, float64, central FD h=1e-6:")
    for k, v in out.items():
        print(f"  {v:.2e}  {k}")
    print()
    for sc in (1e-3, 1e-2, 1e-1, 0.5, 1.0):
        errs_r, errs_s, nphi = [], [], []
        for trial in range(20):
            s = State(3, 3, scale=sc); nphi.append(np.linalg.norm(s.phi[0]))
            for G in gens(3):
                ex = dOm_dphi_recv(s, 0, 1, G); ab = G @ Om(s, 0, 1); errs_r.append(rel(ab, ex))
            gs_e = np.array([dE_dphi_send_exact(s, 1, 0, G) for G in gens(3)]); gs_a = np.array([dE_dphi_send_abelian(s, 1, 0, G) for G in gens(3)])
            errs_s.append(rel(gs_a, gs_e))
        print(f"abelian approx (2370/2447), median |phi_i|_F={np.median(nphi):.3g}: dOmega/dphi median rel err {np.median(errs_r):.2e} (max {np.max(errs_r):.2e}); sender phi-gradient vector median rel err {np.median(errs_s):.2e}")
