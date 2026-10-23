r"""Numerical checks for Item_7_formation_feedback.tex (float64, tiny sizes, single thread).

Per-agent Gibbs-row dynamics with parents created by a wall handoff. Each block prints a residual, an
event list or a root; agreement supports the statements at the tested instances only. Blocks (1)-(5) test
general-law identities on finite alphabets; blocks (6)-(13) use the Gaussian location instance.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import copy
import numpy as np
from scipy.optimize import brentq

rng = np.random.default_rng(20261023)


def simplex(n):
    p = rng.random(n) + 0.05
    return p / p.sum()


def kl(p, q):
    return float(np.sum(p * np.log(p / q)))


def gibbs(prior, cost):
    w = prior * np.exp(-(cost - cost.min()))
    return w / w.sum()


# (1) Shared label, general laws: sum_i KL(q_i||nu) = sum_i KL(q_i||qbar) + n KL(qbar||nu), so the shared row
#     is the Gibbs row of n KL(qbar||nu) and depends on the block only through its linear pool qbar.
k, n = 6, 4
Q = [simplex(k) for _ in range(n)]; qbar = sum(Q) / n
srcs = [simplex(k) for _ in range(5)]; pri = simplex(5)
res = max(abs(sum(kl(q, nu) for q in Q) - sum(kl(q, qbar) for q in Q) - n * kl(qbar, nu)) for nu in srcs)
print("(1a) |compensation identity residual| =", res)
row = gibbs(pri, np.array([sum(kl(q, nu) for q in Q) for nu in srcs]))
row_pool = gibbs(pri, np.array([n * kl(qbar, nu) for nu in srcs]))
eps = 0.02 * (rng.random(k) - 0.5); eps -= eps.mean()           # same pool, different members
Q2 = [Q[0] + eps, Q[1] - eps] + Q[2:]
row2 = gibbs(pri, np.array([sum(kl(q, nu) for q in Q2) for nu in srcs]))
print("(1b) |shared row - pooled row at temperature 1/n|, |row change at fixed pool| =",
      np.abs(row - row_pool).max(), np.abs(row - row2).max())
# exponential-family sources on {0..k-1} with t(x) = (x, x^2): rows depend only on mean parameters (Pythagoras).
xs = np.arange(k, dtype=float); T = np.stack([xs, xs ** 2], 1)
def ef(th):
    a = T @ th; a -= a.max(); p = np.exp(a); return p / p.sum()
def mproj(mu):
    th = np.zeros(2)
    for _ in range(200):
        p = ef(th); m = T.T @ p; C = (T * p[:, None]).T @ T - np.outer(m, m)
        th = th + np.linalg.solve(C + 1e-12 * np.eye(2), mu - m)
    return th
mubar = T.T @ qbar; ths = mproj(mubar); pstar = ef(ths)
nus = [ef(rng.standard_normal(2) * np.array([1.0, 0.2])) for _ in range(4)]
pyth = max(abs(kl(qbar, nu) - kl(qbar, pstar) - kl(pstar, nu)) for nu in nus)
print("(1c) |KL(qbar||p) - KL(qbar||p*) - KL(p*||p)| over family sources =", pyth, "; |E_p* t - mubar| =",
      np.abs(T.T @ pstar - mubar).max())

# (2) Attention capture: an added source with prior share a gives rows beta'_j = (1 - beta'_A) beta_j; at agreement
#     the row part of the force is multiplied by 1 - beta'_A and a fixed record force is unchanged.
k = 5; q = simplex(k); nus = [simplex(k) for _ in range(4)]; pri = simplex(4); a = 0.3
cost = np.array([kl(q, nu) for nu in nus]); b = gibbs(pri, cost)
bp = gibbs(np.concatenate([(1 - a) * pri, [a]]), np.concatenate([cost, [0.0]]))
print("(2a) |beta'_j - (1 - beta'_A) beta_j| =", np.abs(bp[:-1] - (1 - bp[-1]) * b).max())
loglik = np.log(simplex(k))                                   # record log likelihood in k
def fisher_vel(h, q): return -q * (h - q @ h)
h_rows = np.log(q) - sum(bj * np.log(nu) for bj, nu in zip(b, nus))
h_rows_p = np.log(q) - sum(bj * np.log(nu) for bj, nu in zip(bp[:-1], nus)) - bp[-1] * np.log(q)   # parent law = q
v = fisher_vel(h_rows - loglik, q); vp = fisher_vel(h_rows_p - loglik, q)
vpred = (1 - bp[-1]) * fisher_vel(h_rows, q) + fisher_vel(-loglik, q)
print("(2b) |v' - [(1 - beta'_A) v_rows + v_record]| =", np.abs(vp - vpred).max(),
      "; |v' - (1 - beta'_A) v| =", np.abs(vp - (1 - bp[-1]) * v).max(), "(nonzero with records)")

# (3) Global joint, Gaussian location, natural-gradient flow. (3a) A declared star (parent with its own state and
#     prior, Item 3) exerts no force on the block momentum sum_i P_i y_i + P_A y_A at any configuration. (3b) With a
#     pooled parent (top-down cost tau/2 sum_i (y_i - ybar)^2) and mean-field bridges the block sums close and their
#     trajectories do not depend on tau; with sparse bridges they do.
def rk(f, x, dt, ns):
    for _ in range(ns):
        k1 = f(x); k2 = f(x + dt / 2 * k1); k3 = f(x + dt / 2 * k2); k4 = f(x + dt * k3)
        x = x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return x
def star_flow(tau, P, a_, W, I, PA, aA):
    def f(z):
        y, yA = z[:-1], z[-1]
        gr = P * (y - a_) + W.sum(1) * y - W @ y
        gr[I] += tau * (y[I] - yA)
        gA = PA * (yA - aA) + tau * np.sum(yA - y[I])
        return -np.concatenate([gr / P, [gA / PA]])
    return f
def pooled_flow(tau, a_, W, I):
    def f(y):
        gr = (y - a_) + W.sum(1) * y - W @ y
        gr[I] += tau * (y[I] - y[I].mean())
        return -gr
    return f
nA = 6; I = [0, 1, 2]; J = [3, 4, 5]; P = 1 + rng.random(nA); a_ = rng.standard_normal(nA); PA, aA = 0.7, 0.3
Win = np.zeros((nA, nA))
for blk in (I, J):
    for i in blk:
        for j in blk:
            if i != j: Win[i, j] = 1.0
Wmf = Win.copy(); Wmf[np.ix_(I, J)] = 0.2; Wmf[np.ix_(J, I)] = 0.2      # complete bipartite, equal weights
Wsp = Win.copy(); Wsp[2, 3] = Wsp[3, 2] = 0.6; Wsp[1, 4] = Wsp[4, 1] = 0.6
z = np.concatenate([rng.standard_normal(nA), [0.1]])
rates = [np.sum(np.concatenate([P[I], [PA]]) * star_flow(t_, P, a_, Wsp, I, PA, aA)(z)[I + [nA]])
         for t_ in (0.0, 3.0, 30.0)]
print("(3a) d/dt (sum P_i y_i + P_A y_A) at tau = 0, 3, 30:", np.round(rates, 12))
yI = rng.standard_normal(nA)
for name, W in (("mean-field", Wmf), ("sparse", Wsp)):
    zz = [rk(pooled_flow(t_, a_, W, I), yI.copy(), 0.01, 300) for t_ in (0.0, 10.0)]
    print(f"(3b) {name} bridges, pooled parent: |block sums(tau=0) - block sums(tau=10)| at t=3 =",
          max(abs(zz[0][I].sum() - zz[1][I].sum()), abs(zz[0][J].sum() - zz[1][J].sum())))
zs = [rk(star_flow(t_, np.ones(nA), a_, Wmf, I, PA, aA), z.copy(), 0.01, 300) for t_ in (0.0, 10.0)]
print("(3c) mean-field bridges, own-state star: |block J sum(tau=0) - block J sum(tau=10)| at t=3 =",
      abs(zs[0][J].sum() - zs[1][J].sum()))

# (4) Bernoulli: the m-projection pool of a shared-label block is not exactly inherited. Same pool, same rows,
#     different pooled velocity (source natural parameter 1, no records): 0.25 versus about 0.160.
def pool_vel(p, lsrc=1.0):
    l = np.log(p / (1 - p)); return np.mean(p * (1 - p) * (lsrc - l))
print("(4) d/dt pbar at p = (0.5, 0.5) and (0.2, 0.8):", pool_vel(np.array([0.5, 0.5])), pool_vel(np.array([0.2, 0.8])))

# (5) Characterization step: exact closure for every source state needs (1/n) sum_i Var(theta_i) to be a function of
#     the pooled mean; for Bernoulli it is not (two members, pooled mean 0.5).
print("(5) mean Bernoulli variance at p = (0.5, 0.5), (0.2, 0.8):", np.mean([0.25, 0.25]), np.mean([0.16, 0.16]))


# Gaussian location instance -------------------------------------------------------------------------------
def comps(adj):
    m = adj.shape[0]; lab = -np.ones(m, int); c = 0
    for s in range(m):
        if lab[s] >= 0: continue
        st = [s]; lab[s] = c
        while st:
            u = st.pop()
            for v_ in np.nonzero(adj[u])[0]:
                if lab[v_] < 0: lab[v_] = c; st.append(v_)
        c += 1
    return [frozenset(np.nonzero(lab == j)[0].tolist()) for j in range(c)]


class SharedPop:
    r"""Per-agent Gibbs flow, 1D Gaussian location (precision lam): records o with weight rho, evaluator
    N(g, 1/lam) as self source with prior ps, peer priors pp. A selected block shares one source label: its
    row is the Gibbs row of n^power lam/2 (m - m_src)^2 over {evaluator, own parent, other units}, with
    member-mass priors; power 1 is exact Bayes, power 0 the tempered label. mode 'full', 'off' (passive
    parents, members keep individual rows) or 'null' (peer costs deleted)."""

    def __init__(s, o, lam, rho, ps, g, delta, Delta, Tp, mode="full", power=1.0, maxlev=6):
        s.o = np.asarray(o, float); s.N = len(o); s.lam, s.rho, s.ps, s.g = lam, rho, ps, g
        s.pp = (1 - ps) / (s.N - 1); s.delta, s.Delta, s.Tp = delta, Delta, Tp
        s.mode, s.power, s.maxlev = mode, power, maxlev
        s.top = [frozenset([i]) for i in range(s.N)]; s.level = {u: 0 for u in s.top}
        s.cand = {}; s.hist = []; s.t = 0.0; s._refresh()

    def _refresh(s):
        s.K = len(s.top); s.lab = np.empty(s.N, int)
        for j, u in enumerate(s.top):
            for i in u: s.lab[i] = j
        s.n = np.array([len(u) for u in s.top], float)
        s.A = np.zeros((s.K, s.N))
        for j, u in enumerate(s.top): s.A[j, list(u)] = 1.0 / len(u)

    def vel(s, y):
        lam, rho, g = s.lam, s.rho, s.g
        if s.mode == "null":
            Dii = lam / 2 * (y - g) ** 2
            b0 = s.ps * np.exp(-Dii) / (s.ps * np.exp(-Dii) + 1 - s.ps)
            return b0 * (g - y) + rho * (s.o - y)
        if s.mode == "off" or s.K == s.N:
            D = lam / 2 * (y[:, None] - y[None, :]) ** 2; np.fill_diagonal(D, lam / 2 * (y - g) ** 2)
            pri = np.full((s.N, s.N), s.pp); np.fill_diagonal(pri, s.ps)
            W = pri * np.exp(-(D - D.min(1, keepdims=True))); W /= W.sum(1, keepdims=True)
            src = np.tile(y, (s.N, 1)); np.fill_diagonal(src, g)
            return (W * src).sum(1) - y + rho * (s.o - y)
        m = s.A @ y
        return s.unit_target(m)[s.lab] - y + rho * (s.o - y)

    def unit_target(s, m):
        r"""Row-averaged source mean of each unit: sum_nu beta_{U nu} m_nu (rows sum to one)."""
        fac = (s.n ** s.power)[:, None] * s.lam / 2
        Cu = fac * (m[:, None] - m[None, :]) ** 2; Cg = fac[:, 0] * (m - s.g) ** 2
        Pu = np.tile(s.n * s.pp, (s.K, 1)); np.fill_diagonal(Pu, (s.n - 1) * s.pp)
        cmin = np.minimum(Cu.min(1), Cg)
        Wu = Pu * np.exp(-(Cu - cmin[:, None])); Wg = s.ps * np.exp(-(Cg - cmin))
        return (Wu @ m + Wg * s.g) / (Wu.sum(1) + Wg)

    def parent_vel(s, m):
        return s.unit_target(m) - m + s.rho * (s.A @ s.o - m)

    def select(s, y, t):
        m = s.A @ y; D = s.lam / 2 * (m[:, None] - m[None, :]) ** 2; found = []
        for c in comps(D < s.delta):
            if len(c) < 2: continue
            out = [j for j in range(s.K) if j not in c]
            if all(D[i, j] > s.Delta for i in c for j in out):
                found.append((frozenset().union(*[s.top[i] for i in c]), tuple(sorted(c))))
        now = {b_ for b_, _ in found}
        for b_ in list(s.cand):
            if b_ not in now: del s.cand[b_]
        for b_, c in found:
            if b_ not in s.cand: s.cand[b_] = t
            if t - s.cand[b_] >= s.Tp:
                lev = 1 + max(s.level[s.top[i]] for i in c)
                if lev > s.maxlev: continue
                mem = [s.top[i] for i in c]
                s.top = [u for u in s.top if u not in mem] + [b_]; s.level[b_] = lev
                s.hist.append((round(t, 2), lev, tuple(sorted(b_)))); del s.cand[b_]; s._refresh()
                return

    def run(s, y0, Tend, dt=0.05):
        y = np.array(y0, float)
        while s.t < Tend - 1e-12:
            k1 = s.vel(y); k2 = s.vel(y + dt / 2 * k1); k3 = s.vel(y + dt / 2 * k2); k4 = s.vel(y + dt * k3)
            y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); s.t += dt
            s.select(y, s.t)
        return y


def records(gap, spread=0.15, c=2.5, per=3):
    offs = np.linspace(-spread, spread, per)
    return np.array([cc + oo for cc in (-c - gap / 2, -c + gap / 2, c - gap / 2, c + gap / 2) for oo in offs])


lam, rho, ps, g, delta, Delta, Tp = 6.0, 0.005, 0.05, 0.0, 0.05, 0.5, 2.0
o = records(1.1); y0 = o + 0.005 * (2 * rng.random(len(o)) - 1)
short = lambda P: [(h[0], h[1], len(h[2])) for h in P.hist]

# (6) Tempered label is feedback-neutral on internally synchronized configurations; exact Bayes is not.
P = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode="full", power=1.0)
P.top = [frozenset(range(3 * b_, 3 * b_ + 3)) for b_ in range(4)]; P._refresh()
ys = (P.A.T @ np.array([-3.0, -2.0, 2.1, 3.05]))                  # synchronized blocks
Poff = copy.deepcopy(P); Poff.mode = "off"; Ptmp = copy.deepcopy(P); Ptmp.power = 0.0
print("(6) |v_tempered - v_off|, |v_exactBayes - v_off| at a synchronized configuration =",
      np.abs(Ptmp.vel(ys) - Poff.vel(ys)).max(), np.abs(P.vel(ys) - Poff.vel(ys)).max())

# (7) Exact inheritance: block means of the 12-agent flow follow the 4-unit parent flow; deviations relax
#     autonomously to rho/(1+rho) (o_i - obar_I).
P = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode="full")
y1 = P.run(y0, 2.6, dt=0.01)
m1 = P.A @ y1; ob = P.A @ o
yT = rk(P.vel, y1.copy(), 0.01, 2000); mT = rk(P.parent_vel, m1.copy(), 0.01, 2000)
pred_inf = rho / (1 + rho) * (o - ob[P.lab])
pred = pred_inf + np.exp(-(1 + rho) * 20.0) * ((y1 - m1[P.lab]) - pred_inf)
print("(7) units", [tuple(sorted(u)) for u in P.top], ": |A y(20) - m(20)| =", np.abs(P.A @ yT - mT).max(),
      "; |deviation - formula| =", np.abs(yT - (P.A @ yT)[P.lab] - pred).max())

# (8) Null control, feedback-off control, exact-Bayes and tempered shared labels on the same admitted state.
for mode, pw in (("null", 1.0), ("off", 1.0), ("full", 1.0), ("full", 0.0)):
    Pm = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode=mode, power=pw); yf = Pm.run(y0, 400.0)
    print(f"(8) {mode:4s} power {pw}: events {short(Pm)}")
Pn = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode="null"); yn = rk(Pn.vel, y0.copy(), 0.05, 20000)
Dn = lam / 2 * np.diff(np.sort(yn)) ** 2
print("    null at t = 1000: max |y - o| =", np.abs(yn - o).max(), "; min adjacent divergence =", Dn.min(),
      "(selection needs < delta = 0.05)")

# (9) Reduced gap equation for two equal blocks (n = 3): d' = rho (gap - d) - 2 w_n(d) d,
#     w_n(d) = n e^{-a d^2} / ((n - 1) + n e^{-a d^2}), a = n lam/2 (exact Bayes) or lam/2 (tempered, off at sync).
def Fd(d, a_coef, gap=1.1, nn=3):
    e = nn * np.exp(-a_coef * d * d); return rho * (gap - d) - 2 * e / ((nn - 1) + e) * d
roots = {}
for name, ac in (("exact Bayes", 3 * lam / 2), ("tempered", lam / 2)):
    ds = np.linspace(1e-5, 1.1, 400001); vv = Fd(ds, ac)
    rts = [brentq(Fd, ds[j], ds[j + 1], args=(ac,)) for j in range(len(ds) - 1) if vv[j] * vv[j + 1] < 0]
    roots[name] = rts
    print(f"(9) {name}: roots {np.round(rts, 5)}, slopes",
          np.round([(Fd(r + 1e-7, ac) - Fd(r - 1e-7, ac)) / 2e-7 for r in rts], 5))
iL1, iL2 = P.top.index(frozenset([0, 1, 2])), P.top.index(frozenset([3, 4, 5]))
d1 = m1[iL2] - m1[iL1]
print("    actual gap after stage 1, d(2.6) =", d1, "< d_u =", roots["exact Bayes"][1])
# neglected terms in the reduced equation: evaluator and far-unit weights of the L-side units at stage 1
fac = P.n[:, None] * lam / 2
print("    largest neglected weight (evaluator, R-side units) for L units:",
      max(ps * np.exp(-fac[i, 0] * m1[i] ** 2) / ((P.n[i] - 1) * P.pp) for i in (iL1, iL2)),
      max(np.exp(-fac[i, 0] * (m1[i] - m1[j]) ** 2) * P.n[j] / (P.n[i] - 1)
          for i in (iL1, iL2) for j in range(P.K) if j not in (iL1, iL2)))

# (10) Counterfactual first-stage handoffs: shift L1 and L2 apart by s each after stage 1.
for mode in ("full", "off"):
    Pb = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode=mode); yb = Pb.run(y0, 2.6, dt=0.05)
    out = []
    for s_ in (0.0, 0.1, 0.15, 0.25, 0.4):
        Qc = copy.deepcopy(Pb); yc = yb.copy(); yc[[0, 1, 2]] -= s_; yc[[3, 4, 5]] += s_
        yf = Qc.run(yc, 4000.0)
        un = [h[0] for h in Qc.hist if h[1] == 2 and min(h[2]) == 0]
        out.append((s_, round(float(yc[3:6].mean() - yc[:3].mean()), 3), un[0] if un else None,
                    round(float(yf[3:6].mean() - yf[:3].mean()), 4)))
    print(f"(10) {mode}: (shift, gap at handoff, union time, final gap)", out)

# (11) Window in the record gap (rho = 0.005): stage-1 structure and unions.
for gp in (1.0, 1.1, 1.2, 1.3):
    oo = records(gp); yy = oo + 0.005 * (2 * rng.random(len(oo)) - 1); row_ = []
    for mode in ("off", "full"):
        Pw = SharedPop(oo, lam, rho, ps, g, delta, Delta, Tp, mode=mode); Pw.run(yy, 1500.0); row_.append((mode, short(Pw)))
    print(f"(11) gap {gp}:", row_)

# (12) Robustness on the admitted class |y_i(0) - o_i| < 0.005: partition sequences without event times.
seqs = set(); t1s, t2s = [], []
for _ in range(12):
    yy = o + 0.005 * (2 * rng.random(len(o)) - 1)
    Pr = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode="full"); Pr.run(yy, 400.0)
    Pz = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode="null"); Pz.run(yy, 400.0)
    t1s += [h[0] for h in Pr.hist if h[1] == 1]; t2s += [h[0] for h in Pr.hist if h[1] == 2]
    seqs.add((tuple(sorted((h[1], h[2]) for h in Pr.hist)), len(Pz.hist)))   # blocks per level; order of near-simultaneous events ignored
print("(12) distinct (selected blocks by level, number of null events) over 12 draws:", len(seqs))
for s_ in seqs: print("     ", s_)
print("     first-stage times in [%.2f, %.2f], union times in [%.2f, %.2f]" % (min(t1s), max(t1s), min(t2s), max(t2s)))

# (13) Capture distance d_u versus block size n (rho = 0.005, gap = 1.1, exact Bayes).
for nn in (2, 3, 4, 6):
    ds = np.linspace(1e-5, 1.1, 200001); ac = nn * lam / 2; vv = Fd(ds, ac, nn=nn)
    rts = [brentq(Fd, ds[j], ds[j + 1], args=(ac, 1.1, nn)) for j in range(len(ds) - 1) if vv[j] * vv[j + 1] < 0]
    print(f"(13) n = {nn}: roots {np.round(rts, 4)}")

# (14) Depth one at gap 1.2: the handoff gap lies above the middle root, so the parents converge to the separated
#      stable root (a genuine equilibrium held by the records) and never unite.
for gp in (1.1, 1.2, 1.3):
    oo = records(gp); yy = oo + 0.005 * (2 * rng.random(len(oo)) - 1)
    Pg = SharedPop(oo, lam, rho, ps, g, delta, Delta, Tp, mode="full"); yg = Pg.run(yy, 2.6, dt=0.01)
    mg = Pg.A @ yg; iA, iB = Pg.top.index(frozenset([0, 1, 2])), Pg.top.index(frozenset([3, 4, 5]))
    ds = np.linspace(1e-5, gp, 400001); ac = 3 * lam / 2; vv = Fd(ds, ac, gap=gp)
    rts = [brentq(Fd, ds[j], ds[j + 1], args=(ac, gp)) for j in range(len(ds) - 1) if vv[j] * vv[j + 1] < 0]
    yl = Pg.run(yg, 3000.0, dt=0.05); ml = Pg.A @ yl
    print(f"(14) gap {gp}: roots {np.round(rts, 4)}, handoff gap d(2.6) = {mg[iB] - mg[iA]:.4f}, "
          f"events {short(Pg)}, gap at t=3000: {yl[3:6].mean() - yl[:3].mean():.4f}")

# (15) Parent as an added attention source (no records; each agent's evaluator target eta_i sits in its row).
#      Each member adds its pooled parent with prior share a; the selected blocks agree for a = 0, 0.3, 0.6 and
#      only the second-stage event times change.
def attn_run(eta, a, T_end=300.0, dt=0.02, lam_=6.0, ps_=0.05, dc=0.05, dw=1.0, tp=2.0):
    N = len(eta); pri = np.full((N, N), (1 - ps_) / (N - 1)); np.fill_diagonal(pri, ps_)
    parents, cand, hist, t = [], {}, [], 0.0
    def vel(y):
        D = lam_ / 2 * (y[:, None] - y[None, :]) ** 2; np.fill_diagonal(D, lam_ / 2 * (y - eta) ** 2)
        src = np.tile(y, (N, 1)); np.fill_diagonal(src, eta); v_ = np.zeros(N)
        anc = [[] for _ in range(N)]
        for _, mem in sorted(parents, key=lambda p_: p_[0]):
            mm = y[list(mem)].mean()
            for i in mem: anc[i].append(mm)
        for i in range(N):
            w_, s_, pi_ = D[i], src[i], pri[i]
            if anc[i]:
                kk = len(anc[i]); ma = np.array(anc[i])
                pi_ = np.concatenate([pi_ * (1 - a) ** kk, [a * (1 - a) ** (kk - 1 - l) for l in range(kk)]])
                w_ = np.concatenate([w_, lam_ / 2 * (y[i] - ma) ** 2]); s_ = np.concatenate([s_, ma])
            ww = pi_ * np.exp(-(w_ - w_.min())); ww /= ww.sum(); v_[i] = ww @ (s_ - y[i])
        return v_
    y = eta + 0.0
    while t < T_end - 1e-12:
        k1 = vel(y); k2 = vel(y + dt / 2 * k1); k3 = vel(y + dt / 2 * k2); k4 = vel(y + dt * k3)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t += dt
        mems = [m_ for _, m_ in parents]; tops = [m_ for m_ in mems if not any(m_ < o_ for o_ in mems)]
        cov = set().union(*tops) if tops else set()
        units = tops + [frozenset([i]) for i in range(N) if i not in cov]
        mu = np.array([y[list(u)].mean() for u in units]); Du = lam_ / 2 * (mu[:, None] - mu[None, :]) ** 2
        found = []
        for c in comps(Du < dc):
            if len(c) < 2: continue
            out = [j for j in range(len(units)) if j not in c]
            if all(Du[i, j] > dw for i in c for j in out): found.append(frozenset().union(*[units[i] for i in c]))
        for b_ in list(cand):
            if b_ not in found: del cand[b_]
        for b_ in found:
            cand.setdefault(b_, t)
            if t - cand[b_] >= tp and b_ not in mems:
                lev = 1 + max([l_ for l_, m_ in parents if m_ < b_], default=0)
                parents.append((lev, b_)); hist.append((round(t, 2), lev, tuple(sorted(b_))))
    return hist
eta = np.array([c_ + o_ for c_ in (-3.2, -1.8, 1.8, 3.2) for o_ in (-0.3, 0.0, 0.3)])
for a in (0.0, 0.3, 0.6):
    h_ = attn_run(eta, a)
    print(f"(15) attention source, a = {a}: blocks {sorted((l_, b_) for _, l_, b_ in h_)} ; times {[x_[0] for x_ in h_]}")

# (16) Sign margins of the gap equation used for the counterfactual corollary (n = 3, gap 1.1): F < 0 on
#      [0.1291, d_u - 0.005], F > 0 on [d_u + 0.005, d_s - 0.005], F < 0 on [d_s + 0.005, 1.6]; compare with the
#      bound 1e-10 on the neglected terms.
dm, du, dsep = roots["exact Bayes"]
ac = 3 * lam / 2
I1 = np.linspace(np.sqrt(2 * delta / lam), du - 0.005, 200001); I2 = np.linspace(du + 0.005, dsep - 0.005, 200001)
I3 = np.linspace(dsep + 0.005, 1.6, 200001)
print("(16) max F on [0.129, d_u-0.005] =", Fd(I1, ac).max(), "; min F on [d_u+0.005, d_s-0.005] =", Fd(I2, ac).min(),
      "; max F on [d_s+0.005, 1.6] =", Fd(I3, ac).max())

# (17) Margins of the first-stage selections along the fixed-draw trajectory. A group is a candidate when its coherence
#      graph is connected (bottleneck: the largest edge of its minimum spanning tree is below delta_c) and every
#      member is walled from every agent outside it (agent-level distances bound the unit-level ones from below).
#      For each group: entry time t_c of the candidate condition, slope of the bottleneck margin there, and the
#      smallest bottleneck and wall margins over [t_c + 0.05, t_c + tau_p].
Pm = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode="full"); yv = y0.copy(); dtm = 0.005; traj = []
while Pm.t < 2.45:
    k1 = Pm.vel(yv); k2 = Pm.vel(yv + dtm / 2 * k1); k3 = Pm.vel(yv + dtm / 2 * k2); k4 = Pm.vel(yv + dtm * k3)
    yv = yv + dtm / 6 * (k1 + 2 * k2 + 2 * k3 + k4); Pm.t += dtm; Pm.select(yv, Pm.t); traj.append((Pm.t, yv.copy()))
for gi in [list(range(3 * b_, 3 * b_ + 3)) for b_ in range(4)]:
    out = [j for j in range(12) if j not in gi]
    def marg(yv_):
        D_ = lam / 2 * (yv_[:, None] - yv_[None, :]) ** 2
        internal = sorted(D_[i, j] for i in gi for j in gi if i < j)          # 3 members: MST bottleneck = 2nd smallest
        return delta - internal[1], min(D_[i, j] for i in gi for j in out) - Delta
    ts = np.array([t_ for t_, _ in traj]); ms = np.array([marg(y_) for _, y_ in traj])
    k_c = int(np.argmax((ms[:, 0] > 0) & (ms[:, 1] > 0))); tc = ts[k_c]
    slope = (ms[k_c + 1, 0] - ms[k_c - 1, 0]) / (2 * dtm)
    win = ms[(ts >= tc + 0.05) & (ts <= tc + Tp)]
    print(f"(17) group {gi}: t_c = {tc:.3f}, entry slope of bottleneck margin = {slope:.4f}, "
          f"min bottleneck margin = {win[:, 0].min():.4f}, min wall margin = {win[:, 1].min():.4f} over [t_c+0.05, t_c+2]")
print("     handoffs:", short(Pm))
