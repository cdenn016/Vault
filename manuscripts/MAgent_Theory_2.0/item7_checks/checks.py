r"""Numerical checks for Item_7_formation_feedback.tex (float64, tiny sizes, single thread).

Per-agent Gibbs-row dynamics with parents created by a wall handoff. Each block prints a residual, an
event list or a root; agreement supports the statements at the tested instances only. Blocks (1)-(5) test
general-law identities on finite alphabets; blocks (6)-(17) use the Gaussian location instance with the declared
selector. Blocks (18)-(20) test the general-law identities and bounds of the derived selector, and blocks (21)-(26)
run the derived selector in the same instance.
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


# Derived selector ------------------------------------------------------------------------------------------
# The structure free energy F(P) of a coarsening P of the current units is the sum over its blocks of the block
# free energy at its Gibbs row (records omitted: they are the same for every P at fixed laws). The derived selector
# selects the blocks of the minimizer of F that persist for a window Tp. Blocks (18)-(20) test general-law
# identities and bounds; blocks (21)-(26) use the Gaussian location instance with the fixed draw y0 of (7)-(10).
import itertools
rngd = np.random.default_rng(20261024)
pp = (1 - ps) / 11                                            # peer prior of the instance


def F_batch(M, Nn, W):
    r"""Structure free energy of B coarsenings (rows): unit means M, sizes Nn (0 marks padding) and within sums of
    squares W, all of shape (B, K). Unit U pays lam/2 W_U - log[(n_U - 1) pp + ps e^{-n_U lam/2 (m_U - g)^2}
    + sum_V n_V pp e^{-n_U lam/2 (m_U - m_V)^2}]."""
    B, K = M.shape; ii = np.arange(K)
    C = lam / 2 * Nn[:, :, None] * (M[:, :, None] - M[:, None, :]) ** 2               # (B, K, K) receiver x source
    with np.errstate(divide="ignore"):
        Lp = np.broadcast_to(np.log(Nn * pp)[:, None, :], (B, K, K)).copy()
        Lp[:, ii, ii] = np.where(Nn > 1, np.log(np.maximum(Nn - 1, 1) * pp), -np.inf)  # own parent
    C[:, ii, ii] = 0.0
    L = np.concatenate([Lp - C, (np.log(ps) - lam / 2 * Nn * (M - g) ** 2)[:, :, None]], 2)
    mx = L.max(2); lse = mx + np.log(np.exp(L - mx[:, :, None]).sum(2))
    return np.where(Nn > 0, lam / 2 * W - lse, 0.0).sum(1)


def block_stats(y, rgs):
    r"""Means, sizes and within sums of squares of the partitions coded by restricted growth strings (B, n)."""
    B, n = rgs.shape; idx = (np.arange(B)[:, None] * n + rgs).ravel()
    Nn = np.bincount(idx, minlength=B * n).reshape(B, n).astype(float)
    S = np.bincount(idx, weights=np.tile(y, B), minlength=B * n).reshape(B, n)
    SS = np.bincount(idx, weights=np.tile(y * y, B), minlength=B * n).reshape(B, n)
    M = np.where(Nn > 0, S / np.maximum(Nn, 1), 0.0)
    return M, Nn, np.maximum(SS - Nn * M * M, 0.0)


def all_rgs(n):
    R = np.zeros((1, 1), np.int64); mx = np.zeros(1, np.int64)
    for k in range(1, n):
        parts, mxs = [], []
        for v in range(k + 1):
            sel = mx + 1 >= v
            parts.append(np.concatenate([R[sel], np.full((sel.sum(), 1), v)], 1)); mxs.append(np.maximum(mx[sel], v))
        R = np.concatenate(parts); mx = np.concatenate(mxs)
    return R


def rgs_blocks(r):
    return sorted(tuple(int(i) for i in np.nonzero(r == b)[0]) for b in range(r.max() + 1) if np.any(r == b))


_ivl = {}
def interval_coarsenings(Ku):
    r"""One-hot assignments E[p, b, u] of the 2^(Ku-1) interval coarsenings of Ku ordered units."""
    if Ku not in _ivl:
        E = np.zeros((2 ** (Ku - 1), Ku, Ku))
        for p, cuts in enumerate(itertools.product([0, 1], repeat=Ku - 1)):
            b = 0; E[p, 0, 0] = 1
            for u in range(1, Ku):
                b += cuts[u - 1]; E[p, b, u] = 1
        _ivl[Ku] = E
    return _ivl[Ku]


def interval_minimizer(y, units):
    r"""Minimizer of F over interval coarsenings of the units (ordered by mean), and the margin to the next one."""
    units = sorted(units, key=lambda u: y[list(u)].mean())
    nu = np.array([len(u) for u in units], float); mu = np.array([y[list(u)].mean() for u in units])
    Wu = np.array([np.sum((y[list(u)] - y[list(u)].mean()) ** 2) for u in units])
    E = interval_coarsenings(len(units)); Nn = E @ nu
    M = np.where(Nn > 0, (E @ (nu * mu)) / np.maximum(Nn, 1), 0.0)
    W = E @ (Wu + nu * mu * mu) - Nn * M * M
    Fv = F_batch(M, Nn, np.maximum(W, 0.0)); o2 = np.argsort(Fv)
    p = o2[0]; blocks = [frozenset().union(*[units[u] for u in np.nonzero(E[p, b])[0]]) for b in range(len(units))
                         if Nn[p, b] > 0]
    return blocks, Fv[o2[1]] - Fv[o2[0]] if len(Fv) > 1 else np.inf


def Fpart(y, blocks):
    rg = np.zeros(len(y), int)
    for b, u in enumerate(blocks): rg[list(u)] = b
    return F_batch(*block_stats(y, rg[None, :]))[0]


class DerivedPop(SharedPop):
    r"""Shared-label flow with the derived selector: a block of the minimizer of F over interval coarsenings of the
    current units is a candidate; it is selected after Tp without interruption. In the null mode a block's shared
    row weighs the evaluator, with the members' self costs added, against the deleted peer costs."""

    def vel(s, y):
        if s.mode == "null":
            Cg = s.lam / 2 * (s.A * s.n[:, None]) @ ((y - s.g) ** 2)
            bG = s.ps * np.exp(-Cg) / (s.ps * np.exp(-Cg) + 1 - s.ps)
            return bG[s.lab] * (s.g - y) + s.rho * (s.o - y)
        return SharedPop.vel(s, y)

    def select(s, y, t):
        best, _ = interval_minimizer(y, s.top); new = [b_ for b_ in best if b_ not in s.top]
        for b_ in list(s.cand):
            if b_ not in new: del s.cand[b_]
        chosen = []
        for b_ in new:
            s.cand.setdefault(b_, t)
            if t - s.cand[b_] >= s.Tp - 1e-9: chosen.append(b_)
        for b_ in chosen:
            mem = [u for u in s.top if u <= b_]
            s.top = [u for u in s.top if not u <= b_] + [b_]; s.level[b_] = 1 + max(s.level[u] for u in mem)
            s.hist.append((round(t, 2), s.level[b_], tuple(sorted(b_)))); del s.cand[b_]
        if chosen: s._refresh()


def dpop(oo, Tp_, mode):
    return DerivedPop(oo, lam, rho, ps, g, delta, Delta, Tp_, mode=mode)


# (18) Structure free energy, general laws: at its Gibbs row the block free energy of a unit is
#      sum_i KL(q_i||qbar) - T log(pi_A + sum_nu pi_nu e^{-n KL(qbar||nu)/T}); with a moment-projected parent P in an
#      exponential family containing the sources, sum_i KL(q_i||P) - T log(pi_A + sum_nu pi_nu e^{-n KL(P||nu)/T}).
k, n, Tt = 6, 4, 0.7
Q = [simplex(k) for _ in range(n)]; qbar = sum(Q) / n
srcs = [simplex(k) for _ in range(5)]; pri = simplex(6)
def gibbs_fe(prior, cost, T_):
    w = prior * np.exp(-(cost - cost.min()) / T_); b_ = w / w.sum(); return b_ @ cost + T_ * kl(b_, prior)
c_dir = np.array([sum(kl(q, qbar) for q in Q)] + [sum(kl(q, nu) for q in Q) for nu in srcs])
f_form = sum(kl(q, qbar) for q in Q) - Tt * np.log(pri[0] + np.sum(pri[1:] * np.exp(-n * np.array([kl(qbar, nu) for nu in srcs]) / Tt)))
nus = [ef(rngd.standard_normal(2) * np.array([1.0, 0.2])) for _ in range(5)]
Pst = ef(mproj(T.T @ qbar))
c_ef = np.array([sum(kl(q, Pst) for q in Q)] + [sum(kl(q, nu) for q in Q) for nu in nus])
f_ef = sum(kl(q, Pst) for q in Q) - Tt * np.log(pri[0] + np.sum(pri[1:] * np.exp(-n * np.array([kl(Pst, nu) for nu in nus]) / Tt)))
print("(18) |F_U(Gibbs row) - formula|: linear pool", abs(gibbs_fe(pri, c_dir, Tt) - f_form),
      "; moment projection", abs(gibbs_fe(pri, c_ef, Tt) - f_ef))

# (19) Mutual attention bound for two singletons i, j merged into one shared-label unit (linear-pool parent):
#      F_i + F_j - F_ij >= T log(beta_ij beta_ji pi_A / (pi_ij pi_ji)) + max(D_ij, D_ji), pi_A = (pi_ij + pi_ji)/2;
#      an outsider V that attended to i and j now attends to the pool with prior pi_Vi + pi_Vj, and
#      F_V' - F_V <= -T log(1 - beta_V{ij} (1 - e^{-|D_Vi - D_Vj|/(2T)})).
slack_m = slack_o = np.inf
for _ in range(2000):
    kk = 5; T_ = 0.3 + rngd.random(); qi, qj, qv = simplex(kk), simplex(kk), simplex(kk); oth = [simplex(kk) for _ in range(3)]
    pi_i, pi_j, pi_v = simplex(4), simplex(4), simplex(5)
    Di = np.array([kl(qi, qj)] + [kl(qi, x) for x in oth]); Dj = np.array([kl(qj, qi)] + [kl(qj, x) for x in oth])
    Zi, Zj = np.sum(pi_i * np.exp(-Di / T_)), np.sum(pi_j * np.exp(-Dj / T_))
    bij, bji = pi_i[0] * np.exp(-Di[0] / T_) / Zi, pi_j[0] * np.exp(-Dj[0] / T_) / Zj
    qb = (qi + qj) / 2; piA = (pi_i[0] + pi_j[0]) / 2
    Zij = piA * np.exp(-(kl(qi, qb) + kl(qj, qb)) / T_) + np.sum((pi_i[1:] + pi_j[1:]) / 2 * np.exp(-(Di[1:] + Dj[1:]) / T_))
    gain = -T_ * np.log(Zi) - T_ * np.log(Zj) + T_ * np.log(Zij)
    slack_m = min(slack_m, gain - T_ * np.log(bij * bji * piA / (pi_i[0] * pi_j[0])) - max(Di[0], Dj[0]))
    Dv = np.array([kl(qv, qi), kl(qv, qj)] + [kl(qv, x) for x in oth]); Zv = np.sum(pi_v * np.exp(-Dv / T_))
    Zv2 = (pi_v[0] + pi_v[1]) * np.exp(-kl(qv, qb) / T_) + np.sum(pi_v[2:] * np.exp(-Dv[2:] / T_))
    bv = np.sum(pi_v[:2] * np.exp(-Dv[:2] / T_)) / Zv
    slack_o = min(slack_o, -T_ * np.log(1 - bv * (1 - np.exp(-abs(Dv[0] - Dv[1]) / (2 * T_)))) - (T_ * np.log(Zv / Zv2)))
print("(19) min slack over 2000 draws: member bound", slack_m, "; outsider bound", slack_o, "(both must be >= 0)")

# (20) Gaussian location: F_batch equals the sum of unit free energies computed from explicit Gibbs rows, and for
#      the partition into singletons it is the sum of the agents' current free energies (records omitted).
def F_direct(y, blocks):
    tot = 0.0
    for a_, u in enumerate(blocks):
        yu = y[list(u)]; mu_ = yu.mean(); pr, co = [ps], [lam / 2 * np.sum((yu - g) ** 2)]
        if len(u) > 1: pr.append((len(u) - 1) * pp); co.append(lam / 2 * np.sum((yu - mu_) ** 2))
        for b_, v_ in enumerate(blocks):
            if b_ != a_: pr.append(len(v_) * pp); co.append(lam / 2 * np.sum((yu - y[list(v_)].mean()) ** 2))
        tot += gibbs_fe(np.array(pr), np.array(co), 1.0)
    return tot
res = []
for _ in range(5):
    rg = rngd.integers(0, 5, 12); bl = [frozenset(np.nonzero(rg == b_)[0].tolist()) for b_ in range(5) if np.any(rg == b_)]
    res.append(abs(F_direct(y0, bl) - Fpart(y0, bl)))
Dm = lam / 2 * (y0[:, None] - y0[None, :]) ** 2; np.fill_diagonal(Dm, lam / 2 * (y0 - g) ** 2)
prm = np.full((12, 12), pp); np.fill_diagonal(prm, ps)
F_ind = sum(gibbs_fe(prm[i], Dm[i], 1.0) for i in range(12))
print("(20) max |F_batch - explicit Gibbs rows| over 5 random partitions =", max(res),
      "; |F(singletons) - sum_i F_i| =", abs(Fpart(y0, [frozenset([i]) for i in range(12)]) - F_ind))

# (21) The instance at t = 0 (fixed draw). Mutual attention within the groups exceeds the peer prior, so merging
#      lowers the free energy; the minimizer of F over all 4,213,597 partitions of the twelve agents is the four groups.
Wr = prm * np.exp(-(Dm - Dm.min(1, keepdims=True))); Wr /= Wr.sum(1, keepdims=True)
print("(21) beta_01 beta_10 =", round(Wr[0, 1] * Wr[1, 0], 4), ", beta_12 beta_21 =", round(Wr[1, 2] * Wr[2, 1], 4),
      ", beta_23 beta_32 =", round(Wr[2, 3] * Wr[3, 2], 5), "; peer prior pp =", round(pp, 4))
sing = [frozenset([i]) for i in range(12)]
pair = [frozenset([0, 1])] + [frozenset([i]) for i in range(2, 12)]
F_pair_unit = gibbs_fe(np.array([ps, pp] + [pp] * 10), np.array([lam / 2 * np.sum((y0[:2] - g) ** 2),
                       lam / 2 * np.sum((y0[:2] - y0[:2].mean()) ** 2)] + [lam / 2 * np.sum((y0[:2] - y0[j]) ** 2) for j in range(2, 12)]), 1.0)
gain_mem = gibbs_fe(prm[0], Dm[0], 1.0) + gibbs_fe(prm[1], Dm[1], 1.0) - F_pair_unit
bound_mem = np.log(Wr[0, 1] * Wr[1, 0] / pp) + max(Dm[0, 1], Dm[1, 0])
gain_pop = Fpart(y0, sing) - Fpart(y0, pair)
print("    merging agents 0 and 1: members' gain", round(gain_mem, 4), ">= bound", round(bound_mem, 4),
      "; outsiders' change", round(gain_mem - gain_pop, 4), "; gain of F", round(gain_pop, 4))
RG = all_rgs(12); best_f, best_r, second = np.inf, None, np.inf
for c0 in range(0, len(RG), 20000):
    fv = F_batch(*block_stats(y0, RG[c0:c0 + 20000])); j = int(np.argmin(fv)); fs = np.sort(fv)
    if fv[j] < best_f: second = min(best_f, fs[1]); best_f, best_r = fv[j], RG[c0 + j]
    else: second = min(second, fs[0])
print(f"    {len(RG)} partitions; minimizer {rgs_blocks(best_r)}, F = {best_f:.4f}, margin to the next {second - best_f:.4f}")

# (22) Minimizer of F along the flow with individual rows (no handoffs), the gap of the left groups, and the null box.
du_ = sorted(brentq(Fd, a_, b_, args=(3 * lam / 2,)) for a_, b_ in ((0.5, 1.0), (1.0, 1.1)))[0]
yv = y0.copy(); tv = 0.0; prev = None; t_cross = None; switch = []
Pind = SharedPop(o, lam, rho, ps, g, delta, Delta, Tp, mode="off")
snap = {}; mg_early = np.inf
while tv < 2.2 - 1e-9:
    bl, mg = interval_minimizer(yv, sing); key = sorted(tuple(sorted(u)) for u in bl if len(u) > 1)
    if key != prev: switch.append((round(tv, 2), key, round(float(mg), 4))); prev = key
    if tv <= 1.3 + 1e-9: mg_early = min(mg_early, mg)
    if t_cross is None and yv[3:6].mean() - yv[:3].mean() < du_ - 0.005: t_cross = round(tv, 2)
    for tt in (0.5, 1.0, 1.7, 1.78, 2.0):
        if abs(tv - tt) < 5e-3: snap[tt] = yv.copy()
    yv = rk(Pind.vel, yv, 0.01, 1); tv += 0.01
print("(22) interval minimizer along the flow with individual rows (time, blocks, margin to the next):", switch)
print("     smallest margin of the four-group minimizer on [0, 1.3] =", round(float(mg_early), 4))
print("     left gap below d_u - 0.005 =", round(du_ - 0.005, 4), "from t =", t_cross)
R6 = all_rgs(6); side = np.array([np.concatenate([a_, b_ + 6]) for a_ in R6 for b_ in R6])
for tt, ys in sorted(snap.items()):
    fv = F_batch(*block_stats(ys, side)); bi, _ = interval_minimizer(ys, sing)
    print(f"     t = {tt}: minimizer over the {len(side)} side-respecting partitions {rgs_blocks(side[np.argmin(fv)])}"
          f" agrees with the interval minimizer: {rgs_blocks(side[np.argmin(fv)]) == sorted(tuple(sorted(u)) for u in bi)}")
mgs = []; ok = True
for _ in range(200):
    yb = o + 0.005 * (2 * rngd.random(12) - 1); bi, mg = interval_minimizer(yb, sing); mgs.append(mg)
    ok &= sorted(tuple(sorted(u)) for u in bi) == [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
print("     null box |y_i - o_i| <= 0.005, 200 states: minimizer is the four groups at all:", ok,
      "; smallest margin", round(min(mgs), 4))

# (23) Derived-selector histories on the fixed draw for three windows; null and feedback-off controls.
for Tp_ in (0.5, 1.25, 2.0):
    row_ = []
    for mode in ("full", "null") + (("off",) if Tp_ == 1.25 else ()):
        Pd = dpop(o, Tp_, mode); yf = Pd.run(y0, 300.0 if mode != "null" else 100.0)
        row_.append((mode, short(Pd), round(float(yf[3:6].mean() - yf[:3].mean()), 4)))
    print(f"(23) Tp = {Tp_}:", row_)

# (24) Robustness on the admitted class, Tp = 1.25: partition sequences without event times.
seqs = set(); t2s = []
for _ in range(12):
    yy = o + 0.005 * (2 * rngd.random(12) - 1)
    Pf = dpop(o, 1.25, "full"); Pf.run(yy, 300.0); Pz = dpop(o, 1.25, "null"); Pz.run(yy, 60.0)
    seqs.add((tuple(sorted((h[1], h[2]) for h in Pf.hist)), tuple(sorted((h[1], h[2]) for h in Pz.hist))))
    t2s += [h[0] for h in Pf.hist if h[1] == 2]
print("(24) distinct (shared-label, null) partition sequences over 12 draws:", len(seqs))
for s_ in seqs: print("     ", s_)
print("     union times in [%.2f, %.2f]" % (min(t2s), max(t2s)))

# (25) Union radius. For two synchronized parents of size n at gap d, with the evaluator and far units dropped,
#      F(separate) - F(union) = Gamma_n(d) = -log pp + log(2n-1) - 2 log(n-1 + n e^{-n lam d^2/2}) - n lam d^2/4.
def Gam(d, nn=3):
    return -np.log(pp) + np.log(2 * nn - 1) - 2 * np.log(nn - 1 + nn * np.exp(-nn * lam * d * d / 2)) - nn * lam * d * d / 4
for nn in (2, 3, 4, 6):
    ds = np.linspace(1e-4, 3.0, 300001); v_ = Gam(ds, nn)
    zs = [brentq(Gam, ds[j], ds[j + 1], args=(nn,)) for j in range(len(ds) - 1) if v_[j] * v_[j + 1] < 0]
    print(f"(25) n = {nn}: zeros of Gamma_n on (0, 3] {np.round(zs, 4)}, Gamma_n(0) = -log((2n-1) pp) = {Gam(0.0, nn):.4f}")
dst = brentq(Gam, 0.5, 1.0); errs = []
for d in np.linspace(0.05, 1.2, 24):
    for cL in (-2.5, -2.3, -2.7):                       # parent means stay in [-3.3, -1.7]
        m4 = np.array([cL - d / 2, cL + d / 2, 2.4, 2.6])[None, :]
        Fsep = F_batch(m4, np.full((1, 4), 3.0), np.zeros((1, 4)))[0]
        Fun = F_batch(np.array([[cL, 2.4, 2.6]]), np.array([[6.0, 3.0, 3.0]]), np.array([[1.5 * d * d, 0, 0]]))[0]
        errs.append(abs(Fsep - Fun - Gam(d)))
print("     d_* =", round(dst, 5), "; max |F(sep) - F(union) - Gamma_3| over 72 configurations in range =", max(errs),
      "; d_m < d_* < d_u - 0.005:", roots["exact Bayes"][0] < dst < du_ - 0.005 if "roots" in globals() else None)

# (26) Counterfactual first-stage handoffs under the derived selector (Tp = 1.25): shift L1 and L2 apart after stage 1.
for mode, shifts in (("full", (-0.15, -0.05, 0.0, 0.025, 0.05, 0.1, 0.25)), ("off", (0.0, 0.1, 0.25, 0.4))):
    Pb = dpop(o, 1.25, mode); yb = Pb.run(y0, 1.35); out = []
    for s_ in shifts:
        Qc = copy.deepcopy(Pb); yc = yb.copy(); yc[[0, 1, 2]] -= s_; yc[[3, 4, 5]] += s_
        yf = Qc.run(yc, 2000.0); un = [h[0] for h in Qc.hist if h[1] == 2 and min(h[2]) == 0]
        out.append((round(float(yc[3:6].mean() - yc[:3].mean()), 3), un[0] if un else None,
                    round(float(yf[3:6].mean() - yf[:3].mean()), 4)))
    print(f"(26) {mode}: first stage {short(Pb)}; (gap at handoff, union time, final gap)", out)
