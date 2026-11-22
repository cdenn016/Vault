r"""a3b: agency index of the CCP under the declarations that def:agy-group-model
allows, and the sampling spread of the candidate's 300-state declaration.

Declared expectations (before running):
 E1 Monte Carlo simulation of the full model (members' filters on a simulated
    world) reproduces my stationary Var(z_j) = Var(D m_j^+) to |z| < 4.
 E2 with z_C = D y(t+1)/F (coarse state formed at the end of the decision round,
    includes computation noise) the index is within 0.002 of the avg-posterior
    value 0.2654.
 E3 with the group belief a declared function of the start-of-round coarse
    state y(t) the index stays below Agency0 = 0.25 even with a free scale
    lambda on the belief (z_C = lambda D y(t)).
 E4 the candidate's procedure (300 states drawn from the stationary law of the
    act means) has seed-to-seed spread large enough that some draws fall below
    0.25 (fraction reported).
"""
import numpy as np
from scipy.optimize import minimize, minimize_scalar
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import a3_closure_agency as M   # my own model matrices (its prints suppressed)

np.set_printoptions(precision=6, suppress=True)
p, h, kap, s2 = M.p, M.h, M.kap, M.s2
zb, zs, SYX = M.zb, M.zs, M.SYX
NY, NE = M.NY, M.NE

# ---- E1: Monte Carlo of the full model ----
rng = np.random.default_rng(99)
A, B, Qxi = M.A, M.B, M.Qxi
Lq = np.linalg.cholesky(Qxi + 1e-18 * np.eye(NE))
Y = np.zeros(NY)
vals = []
nT, burn = 300000, 1000
for t in range(nT + burn):
    xi = Lq @ rng.standard_normal(NE)
    if t >= burn:
        YX = np.concatenate([Y, xi])
        vals.append([zb @ YX, zs @ YX])
    Y = A @ Y + B @ xi
vals = np.array(vals)
nb = 100
bs = len(vals) // nb
bm = np.array([np.mean(vals[i*bs:(i+1)*bs] ** 2, 0) for i in range(nb)])
V = np.vstack([zb, zs])
ex = np.diag(V @ SYX @ V.T)
print("E1 Var(z_b), Var(z_s): MC", bm.mean(0), " exact", ex, " z", (bm.mean(0) - ex) / (bm.std(0) / np.sqrt(nb)))


def index_general(zc_map, lam_free=False):
    Vv = np.vstack([zb, zs, zc_map])
    Cz = Vv @ SYX @ Vv.T
    Ez2 = Cz[0, 0] + Cz[1, 1]
    klE = (s2 * 2 * h - 2 - 2 * np.log(s2 * h) + h * kap ** 2 * Ez2) / 2

    def klg(c, lam):
        g = lam * c / (h + 2 * c)
        cov_part = s2 * (2 * h + 2 * c) - 2 - 2 * np.log(s2) - np.log(h) - np.log(h + 2 * c)
        E_d2 = kap ** 2 * Ez2 - 2 * kap * g * (Cz[2, 0] + Cz[2, 1]) + 2 * g ** 2 * Cz[2, 2]
        E_s2 = kap ** 2 * (Cz[0, 0] + Cz[1, 1] + 2 * Cz[0, 1]) - 4 * kap * g * (Cz[2, 0] + Cz[2, 1]) + 4 * g ** 2 * Cz[2, 2]
        return 0.5 * (cov_part + h * E_d2 + c * E_s2)
    if lam_free:
        best = np.inf
        for lc0 in (-2, 0, 2, 4):
            for l0 in (0.5, 1, 2, 4):
                r = minimize(lambda v: klg(np.exp(v[0]), v[1]), [lc0, l0], method="Nelder-Mead",
                             options=dict(xatol=1e-9, fatol=1e-12, maxiter=4000))
                best = min(best, r.fun)
        best = min(best, klg(0.0, 1.0))
    else:
        r = minimize_scalar(lambda lc: klg(np.exp(lc), 1.0), bounds=(-12, 12), method="bounded")
        best = min(r.fun, klg(0.0, 1.0))
    return 1 - best / klE


zc_avg = M.zC["avg posterior z"]
zc_y = M.zC["coarse y(t) (prior avg)"]
# y(t+1)/F : D y(t+1) = F * avg D m^+ + avg D c  (c are xi indices 6..9 (c_b), 10..13 (c_s))
zc_next = zc_avg.copy()
zc_next[NY + 6:NY + 10] += 0.5 * M.D / p["F"]
zc_next[NY + 10:NY + 14] += 0.5 * M.D / p["F"]
print("E2 index, z_C = avg posterior z       : %.4f" % index_general(zc_avg))
print("   index, z_C = D y(t+1)/F (end of round): %.4f" % index_general(zc_next))
print("E3 index, z_C = D y(t) (start of round)  : %.4f" % index_general(zc_y))
print("   index, z_C = lambda D y(t), lambda free: %.4f" % index_general(zc_y, lam_free=True))
print("   index, z_C = lambda * avg posterior z, lambda free: %.4f" % index_general(zc_avg, lam_free=True))

# ---- E4: candidate's procedure on my covariance: 300 sampled states of the act means ----
Vv = np.vstack([zb, zs])
Cmu = kap ** 2 * (Vv @ SYX @ Vv.T)


def idx_sample(MU):
    n = 2
    zcs = np.mean(MU / kap, 1)   # z_j = -mu_j/kappa ; zC = mean of z_j ; sign handled below

    def kl(m1, S1, m2, S2):
        S2i = np.linalg.inv(S2); dm = m2 - m1
        return 0.5 * (np.trace(S2i @ S1) + dm @ S2i @ dm - n + np.log(np.linalg.det(S2) / np.linalg.det(S1)))
    den = sum(kl(mu, s2 * np.eye(2), np.zeros(2), np.eye(2) / h) for mu in MU)

    def f(lg):
        c = np.exp(lg)
        Si = np.linalg.inv(h * np.eye(2) + c * np.ones((2, 2)))
        tot = 0.0
        for mu in MU:
            zC = np.mean(-mu / kap)
            tot += kl(mu, s2 * np.eye(2), -c * zC * Si @ np.ones(2), Si)
        return tot
    grid = np.linspace(-6, 8, 57)
    v = [f(x) for x in grid]
    j = int(np.argmin(v))
    r = minimize_scalar(f, bounds=(grid[max(j - 1, 0)], grid[min(j + 1, 56)]), method="bounded")
    return 1 - min(r.fun, v[j]) / den, den / len(MU)


res = []
for seed in range(60):
    MU = np.random.default_rng(1000 + seed).multivariate_normal(np.zeros(2), Cmu, size=300)
    res.append(idx_sample(MU))
res = np.array(res)
print("E4 300-state declarations over 60 seeds: index mean %.4f sd %.4f min %.4f max %.4f; fraction < 0.25: %.2f"
      % (res[:, 0].mean(), res[:, 0].std(), res[:, 0].min(), res[:, 0].max(), np.mean(res[:, 0] < 0.25)))
print("   mean KL(P||E) per state: mean %.3f, min %.3f, max %.3f (candidate's draw: 1.474)" % (res[:, 1].mean(), res[:, 1].min(), res[:, 1].max()))
