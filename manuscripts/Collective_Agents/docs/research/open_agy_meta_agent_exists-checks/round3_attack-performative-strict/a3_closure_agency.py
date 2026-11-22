r"""a3: closure (memory and inference) and agency for the CCP, own code.

Full stationary model, one firm:
  Y_t = [x_t(4), e_b(t)(4), e_s(t)(4), v_b(t-1), v_s(t-1), e_U(t)(2)]  (16)
  xi_t = [w_a, w_b, v_b, v_s, nu_bs, nu_sb, c_b(4), c_s(4)]            (14)
e_j are the members' prior errors, e_U the union-model prior error (both own
sensors, no computation noise).  Coarse variable (candidate's declaration):
y(t) = average of the members' current prior means (eta^a_t, eta^b_t components).

Declared expectations (before running):
 E1 alpha_I (plain average, best constant encoding) = 0.0317, union prior
    covariance diagonal 0.1590878 (candidate).
 E2 stationary unconditional d_M of y about 5e-5 (candidate 5.112e-5).
 E3 the input-conditional forms (law of y given the blanket path) differ from E2;
    I do not know their size in advance; anything above alpha_M = 0.02 fails
    the memory clause at the stated grade under that reading.
 E4 agency (D2, habits fixed N(0,1/30), gamma_C >= 0, belief z_C = average of
    the members' posterior z) about 0.277 (candidate); other declared pooled
    beliefs give different values, possibly below Agency0 = 0.25.
 E5 NEGATIVE CONTROL for the agency code: if the actual law IS a group posterior
    of the class (kappa, s2 replaced by the group posterior's mean and covariance
    at some c), the index must be 1 to 1e-9.
"""
import numpy as np
from scipy.optimize import minimize_scalar
from ccp_lib import *

np.set_printoptions(precision=6, suppress=True, linewidth=140)
p = default_params()
Phi, Qw, Gm = world_mats(p)
filt = member_filters(p)
F = p["F"]
# union filter (2-d, both own sensors)
PU, KU = kalman_ss(F * np.eye(2), Qw, np.eye(2), p["R"] * np.eye(2))
print("union prior covariance P_U^- =\n", PU)

NY, NE = 16, 14
ix = slice(0, 4); ieb = slice(4, 8); ies = slice(8, 12); ivb, ivs = 12, 13; ieU = slice(14, 16)
qv = np.zeros(NE)
Qxi = np.zeros((NE, NE))
Qxi[0:2, 0:2] = Qw
Qxi[2, 2] = Qxi[3, 3] = p["R"]
Qxi[4, 4] = Qxi[5, 5] = p["Rc"]
Qxi[6:14, 6:14] = p["qc"] * np.eye(8)

A = np.zeros((NY, NY)); B = np.zeros((NY, NE))
A[ix, ix] = Phi; B[ix, 0:2] = Gm
# posterior error maps (as functions of [Y; xi]) for later use
Epost = {}
for j, (ie, own_i, lag_i, nu_i, c0) in {"b": (ieb, 2, ivs, 4, 6), "s": (ies, 3, ivb, 5, 10)}.items():
    K, H = filt[j]["K"], filt[j]["H"]
    M = np.eye(4) - K @ H
    EpY = np.zeros((4, NY)); EpX = np.zeros((4, NE))
    EpY[:, ie] = M
    EpX[:, own_i] += K[:, 0]
    EpY[:, lag_i] += K[:, 1]
    EpX[:, nu_i] += K[:, 1]
    Epost[j] = (EpY, EpX)
    A[ie, :] = Phi @ EpY
    B[ie, :] = Phi @ EpX
    B[ie, c0:c0 + 4] += np.eye(4)
    B[ie, 0:2] += -Gm
B[ivb, 2] = 1.0; B[ivs, 3] = 1.0
MU = np.eye(2) - KU
A[ieU, ieU] = F * MU
B[ieU, 2:4] = F * KU
B[ieU, 0:2] += -np.eye(2)
print("spectral radius full model:", max(abs(np.linalg.eigvals(A))))
SY = solve_discrete_lyapunov(A, B @ Qxi @ B.T)

# ---------------- inference clause ----------------
E2 = np.zeros((2, 4)); E2[0, 0] = 1; E2[1, 1] = 1
Pdiff = np.zeros((2, NY)); Pdiff[:, ieb] = 0.5 * E2; Pdiff[:, ies] += 0.5 * E2; Pdiff[:, ieU] = -np.eye(2)
Cd = Pdiff @ SY @ Pdiff.T
aI_plain = 0.5 * np.trace(np.linalg.solve(PU, Cd))
print("E1 alpha_I (plain average, best constant encoding) = %.5f" % aI_plain)
# reverse direction KL(union || encoded) with best constant encoding: same mean term, covariance part min at P=PU
# log-pool of the members' prior beliefs on (eta^a_t, eta^b_t)
Pb = filt["b"]["P"][:2, :2]; Ps = filt["s"]["P"][:2, :2]
P0 = solve_discrete_lyapunov(F * np.eye(2), Qw)
Lb, Ls, L0 = np.linalg.inv(Pb), np.linalg.inv(Ps), np.linalg.inv(P0)
Lpool = Lb + Ls - L0
Wb = np.linalg.solve(Lpool, Lb); Ws = np.linalg.solve(Lpool, Ls); W0 = -np.linalg.solve(Lpool, L0)
# y_LP - x_cur = Wb e_b + Ws e_s + W0 (0 - x_cur) + (Wb+Ws+W0 - I) x_cur ; Wb+Ws+W0 = I
Plp = np.zeros((2, NY)); Plp[:, ieb] = Wb @ E2; Plp[:, ies] = Ws @ E2; Plp[:, 0:2] += -W0; Plp[:, ieU] = -np.eye(2)
aI_lp = 0.5 * np.trace(np.linalg.solve(PU, Plp @ SY @ Plp.T))
print("   alpha_I (prior-corrected log pool of prior beliefs) = %.5f" % aI_lp)
# claimed-covariance encodings
def kl_gauss(m_cov_diff, Penc, PU):
    k = PU.shape[0]
    return 0.5 * (np.trace(np.linalg.solve(PU, Penc)) - k + np.log(np.linalg.det(PU) / np.linalg.det(Penc))
                  + np.trace(np.linalg.solve(PU, m_cov_diff)))
print("   alpha_I (plain average, encoded covariance = average of members' P^-) = %.5f" % kl_gauss(Cd, 0.5 * (Pb + Ps), PU))
print("   alpha_I (log pool, encoded covariance = Lpool^-1) = %.5f" % kl_gauss(Plp @ SY @ Plp.T, np.linalg.inv(Lpool), PU))

# ---------------- memory clause ----------------
Py = np.zeros((2, NY)); Py[:, ix] = E2; Py[:, ieb] += 0.5 * E2; Py[:, ies] += 0.5 * E2


def markov_defect_from_acf(acf, K):
    """acf(k) = Cov(y_{t+k}, y_t) (d x d). I(y_{t+1}; y_{t-K..t-1} | y_t)."""
    d = acf(0).shape[0]
    n = K + 2   # y_{t-K},...,y_t,y_{t+1}
    G = np.zeros((n * d, n * d))
    for a in range(n):
        for b in range(n):
            k = a - b
            G[a*d:(a+1)*d, b*d:(b+1)*d] = acf(k) if k >= 0 else acf(-k).T
    # order: index n-1 = y_{t+1}, n-2 = y_t, 0..n-3 = past
    fut = slice((n - 1) * d, n * d); cur = slice((n - 2) * d, (n - 1) * d); past = slice(0, (n - 2) * d)
    def condvar(tidx, cidx):
        Stt = G[np.ix_(tidx, tidx)]
        if len(cidx) == 0:
            return Stt
        Stc = G[np.ix_(tidx, cidx)]; Scc = G[np.ix_(cidx, cidx)]
        return Stt - Stc @ np.linalg.solve(Scc, Stc.T)
    ti = list(range(fut.start, fut.stop)); ci = list(range(cur.start, cur.stop)); pi_ = list(range(past.start, past.stop))
    v1 = condvar(ti, ci); v2 = condvar(ti, ci + pi_)
    return 0.5 * (np.log(np.linalg.det(v1)) - np.log(np.linalg.det(v2)))


acf_a = lambda k: Py @ np.linalg.matrix_power(A, k) @ SY @ Py.T
print("\nE2 d_M (a) stationary unconditional law of y:")
for K in (1, 5, 20, 60):
    print("   history %2d: %.4e" % (K, markov_defect_from_acf(acf_a, K)))

# (b) input-free internal process (law of y given the bi-infinite sensory input path)
Kb, Ks = filt["b"]["K"], filt["s"]["K"]
Mb = np.eye(4) - Kb @ filt["b"]["H"]; Ms = np.eye(4) - Ks @ filt["s"]["H"]
Ai = np.zeros((10, 10))
Ai[0:4, 0:4] = Phi @ Mb; Ai[0:4, 8] = Phi @ Kb[:, 1]
Ai[4:8, 4:8] = Phi @ Ms; Ai[4:8, 9] = Phi @ Ks[:, 1]
Qn = np.diag([p["qc"]] * 8 + [p["Rc"]] * 2)
Si = solve_discrete_lyapunov(Ai, Qn)
Pyi = np.zeros((2, 10)); Pyi[:, 0:4] = 0.5 * E2; Pyi[:, 4:8] = 0.5 * E2
acf_b = lambda k: Pyi @ np.linalg.matrix_power(Ai, k) @ Si @ Pyi.T
print("E3 d_M (b) input-free internal process (stationary law given the whole sensory path):")
for K in (1, 5, 20, 60):
    print("   history %2d: %.4e" % (K, markov_defect_from_acf(acf_b, K)))


# (b'), (c') literal: actual joint stationary law, condition on blanket path from 0 to t
def literal_defect(t, with_acts):
    """I(y_{t+1}; y_{0:t-1} | y_t, s_{0:t} [, u_{0:t}]) in the actual stationary joint law.
    Build the joint Gaussian of the needed variables from [Y_0; xi_0..xi_{t}] with
    acts' private noise eps added."""
    n_eps = 2
    dimU = NY + (NE + n_eps) * (t + 1)
    covU = np.zeros((dimU, dimU)); covU[:NY, :NY] = SY
    for k in range(t + 1):
        o = NY + k * (NE + n_eps)
        covU[o:o + NE, o:o + NE] = Qxi
        covU[o + NE:o + NE + 2, o + NE:o + NE + 2] = p["s2"] * np.eye(2)
    coef = np.zeros((NY, dimU)); coef[:, :NY] = np.eye(NY)
    ys, ss, us = [], [], []
    for k in range(t + 1):
        o = NY + k * (NE + n_eps)
        cx = np.zeros((NE, dimU)); cx[:, o:o + NE] = np.eye(NE)
        ce = np.zeros((2, dimU)); ce[:, o + NE:o + NE + 2] = np.eye(2)
        ys.append(Py @ coef)
        # sensors s_b = eta^a_t + v_b(t), s_s = eta^b_t + v_s(t)
        sb = coef[0] + cx[2]; s_s = coef[1] + cx[3]
        ss += [sb, s_s]
        # acts: u_j = -kappa D (x + e_j^+) + eps_j
        for jj, j in enumerate("bs"):
            EpY, EpX = Epost[j]
            mplus = coef[ix] + EpY @ coef + EpX @ cx
            us.append(-p["kappa"] * D @ mplus + ce[jj])
        coef = A @ coef + B @ cx
    ys.append(Py @ coef)   # y_{t+1}
    fut = ys[t + 1]; cur = ys[t]
    past = np.vstack(ys[:t]) if t > 0 else np.zeros((0, dimU))
    cond0 = np.vstack([cur] + ss + (us if with_acts else []))
    def cv(Tm, Cm):
        Stt = Tm @ covU @ Tm.T
        Stc = Tm @ covU @ Cm.T
        Scc = Cm @ covU @ Cm.T
        return Stt - Stc @ np.linalg.solve(Scc, Stc.T)
    v1 = cv(fut, cond0)
    v2 = cv(fut, np.vstack([cond0, past])) if t > 0 else v1
    return 0.5 * (np.log(np.linalg.det(v1)) - np.log(np.linalg.det(v2)))


print("E3 d_M literal, actual joint law, conditioning on the blanket path from 0 to t:")
for t in (1, 2, 5, 10, 20, 40):
    print("   t=%2d  sensors only: %.4e   sensors+acts: %.4e" % (t, literal_defect(t, False), literal_defect(t, True)))

# ---------------- agency ----------------
h = 30.0
kap, s2 = p["kappa"], p["s2"]
ZY = np.zeros((NY, 0))
# z_j = D m_j^+ = D x + D e_j^+ ; as a map on [Y; xi]
SYX = np.zeros((NY + NE, NY + NE)); SYX[:NY, :NY] = SY; SYX[NY:, NY:] = Qxi


def zmap(j):
    EpY, EpX = Epost[j]
    r = np.zeros(NY + NE)
    r[:NY] = D @ EpY
    r[0:4] += D
    r[NY:] = D @ EpX
    return r


zb, zs = zmap("b"), zmap("s")
# candidate pooled beliefs for the group model
zC = {}
zC["avg posterior z"] = 0.5 * (zb + zs)
r = np.zeros(NY + NE); r[0:4] += D; r[4:8] += 0.5 * D; r[8:12] += 0.5 * D   # D y(t), prior average
zC["coarse y(t) (prior avg)"] = r
r = np.zeros(NY + NE); r[0:2] += np.array([1., -1.]); r[ieU.start:ieU.stop] += np.array([1., -1.]) @ MU
r[NY + 2:NY + 4] += np.array([1., -1.]) @ KU                                # union posterior at t
zC["union posterior"] = r
# log pool of the members' posteriors on the current components
Pbp = (np.eye(4) - Kb @ filt["b"]["H"]) @ filt["b"]["P"]; Psp = (np.eye(4) - Ks @ filt["s"]["H"]) @ filt["s"]["P"]
Lbp, Lsp = np.linalg.inv(Pbp[:2, :2]), np.linalg.inv(Psp[:2, :2])
Lpp = Lbp + Lsp - L0
Wbp = np.linalg.solve(Lpp, Lbp); Wsp = np.linalg.solve(Lpp, Lsp)
EbY, EbX = Epost["b"]; EsY, EsX = Epost["s"]
r = np.zeros(NY + NE)
D2 = np.array([1., -1.])
r[0:2] += D2                         # (Wb+Ws+W0) x_cur = x_cur ... plus W0(0 - x) handled below
r[:NY] += D2 @ (Wbp @ E2 @ EbY + Wsp @ E2 @ EsY); r[NY:] += D2 @ (Wbp @ E2 @ EbX + Wsp @ E2 @ EsX)
W0p = -np.linalg.solve(Lpp, L0)
r[0:2] += -D2 @ W0p                  # m_LP - x = Wb e_b + Ws e_s - W0 x
zC["log pool posterior"] = r


def index_for(zc, kapA=kap, s2A=s2, verbose=False):
    V = np.vstack([zb, zs, zc])
    Cz = V @ SYX @ V.T                       # cov of (z_b, z_s, z_C)
    Ez2 = Cz[0, 0] + Cz[1, 1]
    klE = (s2A * 2 * h - 2 - 2 * np.log(s2A * h) + h * kapA ** 2 * Ez2) / 2

    def klg(c):
        g = c / (h + 2 * c)
        cov_part = s2A * (2 * h + 2 * c) - 2 - 2 * np.log(s2A) - np.log(h) - np.log(h + 2 * c)
        E_d2 = kapA ** 2 * Ez2 - 2 * kapA * g * (Cz[2, 0] + Cz[2, 1]) + 2 * g ** 2 * Cz[2, 2]
        E_s2 = kapA ** 2 * (Cz[0, 0] + Cz[1, 1] + 2 * Cz[0, 1]) - 4 * kapA * g * (Cz[2, 0] + Cz[2, 1]) + 4 * g ** 2 * Cz[2, 2]
        return 0.5 * (cov_part + h * E_d2 + c * E_s2)
    res = minimize_scalar(lambda lc: klg(np.exp(lc)), bounds=(-12, 12), method="bounded")
    c_opt = np.exp(res.x)
    best = min(res.fun, klg(0.0))
    if verbose:
        print("     cov(zb,zs,zC)=", Cz.ravel(), " c_opt=%.3f" % c_opt)
    return 1 - best / klE, klE, c_opt, Cz


print("\nAgency index (D2 actual law, habits fixed N(0,1/30), gamma_C >= 0):")
for name, zc in zC.items():
    idx, klE, c_opt, Cz = index_for(zc)
    print("   belief %-26s index = %.4f   E KL(P||E) = %.4f   c_opt = %.3f" % (name, idx, klE, c_opt))
# E5 negative control: actual law replaced by group posterior at c=25 with zC = avg posterior z
cg = 25.0
kg = cg / (h + 2 * cg)
# group posterior: mean -kg zC (1,1), cov (hI + c 11^T)^-1 is not isotropic, so emulate with a direct check:
def index_exact_group(c):
    V = np.vstack([zb, zs, zC["avg posterior z"]])
    Cz = V @ SYX @ V.T
    Sg = np.linalg.inv(h * np.eye(2) + c * np.ones((2, 2)))
    def kl(Sa, Sb_, dcov):
        return 0.5 * (np.trace(np.linalg.solve(Sb_, Sa)) - 2 + np.log(np.linalg.det(Sb_) / np.linalg.det(Sa)) + dcov)
    # actual law = group posterior at c; model at c' : mean diff = (g(c')-g(c)) zC (1,1)
    def klg(c2):
        Sg2 = np.linalg.inv(h * np.eye(2) + c2 * np.ones((2, 2)))
        g1, g2 = c / (h + 2 * c), c2 / (h + 2 * c2)
        Lg2 = np.linalg.inv(Sg2)
        return kl(Sg, Sg2, (g2 - g1) ** 2 * Cz[2, 2] * np.ones(2) @ Lg2 @ np.ones(2))
    klE = kl(Sg, np.eye(2) / h, (c / (h + 2 * c)) ** 2 * Cz[2, 2] * 2 * h)
    res = minimize_scalar(lambda lc: klg(np.exp(lc)), bounds=(-12, 12), method="bounded")
    return 1 - res.fun / klE
print("E5 negative control (actual law = group posterior at c=25): index = %.10f" % index_exact_group(25.0))


# E5b: brute-force check of index_for's closed-form algebra by sampling decision
# states and using the generic Gaussian KL formula on a grid of c.
rng = np.random.default_rng(11)
V = np.vstack([zb, zs, zC["avg posterior z"]])
Cz = V @ SYX @ V.T
Lc = np.linalg.cholesky(Cz + 1e-15 * np.eye(3))
smp = (Lc @ rng.standard_normal((3, 20000))).T


def kl_full(m1, S1, m2, S2):
    d = m2 - m1
    return 0.5 * (np.trace(np.linalg.solve(S2, S1)) - 2 + np.log(np.linalg.det(S2) / np.linalg.det(S1)) + d @ np.linalg.solve(S2, d))


def mc_index(cgrid):
    S1 = s2 * np.eye(2)
    klE = np.mean([kl_full(-kap * z[:2], S1, np.zeros(2), np.eye(2) / h) for z in smp[:4000]])
    best = np.inf
    for c in cgrid:
        Sg = np.linalg.inv(h * np.eye(2) + c * np.ones((2, 2)))
        g = c / (h + 2 * c)
        v = np.mean([kl_full(-kap * z[:2], S1, -g * z[2] * np.ones(2), Sg) for z in smp[:4000]])
        best = min(best, v)
    return 1 - best / klE


idx_cf = index_for(zC["avg posterior z"])[0]
idx_mc = mc_index(np.linspace(0, 80, 161))
print("E5b closed form %.4f vs brute-force MC (4000 states, c grid step 0.5) %.4f" % (idx_cf, idx_mc))
