"""Deciding script 1: unit checks, full model, baselines, agency, inference closure, order parameter.
Each check states its expected outcome before the computed value."""
import itertools, math
import numpy as np
from core import *

np.set_printoptions(precision=6, suppress=True)
n, N, kappa = 4, 8, 3
P0, s, c, gam, s2 = 1.0, 1.0, 0.1, 4.0, 1e-3          # declared instance
rng = np.random.default_rng(20261121)


def att_full(i, p):
    return [(tuple(j for j in range(n) if j != i), 1.0)]


out = []
def say(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

# ---------- A1: lemma C1 (exchangeable block) + negative control ----------
say("A1 expect: Pi formula error < 1e-10, r = 1+n*beta/alpha; control beta<0 gives positive off-diagonal")
for al, be, m in [(1.0, 0.5, 4), (0.3, 2.0, 6)]:
    S = al * np.eye(m) + be * np.ones((m, m)); Pi = np.linalg.inv(S)
    Pf = (np.eye(m) - be / (al + m * be) * np.ones((m, m))) / al
    say("  alpha,beta,m", al, be, m, "| err", np.abs(Pi - Pf).max(), "| coupling", -Pi[0, 1], "vs", be / (al * (al + m * be)),
        "| leak", Pi.sum(1)[0], "vs", 1 / (al + m * be), "| r", contrast(Pi, range(m)), "vs", 1 + m * be / al)
S = 1.0 * np.eye(4) - 0.2 * np.ones((4, 4)); say("  control beta=-0.2: max offdiag of Pi", (np.linalg.inv(S) - np.diag(np.diag(np.linalg.inv(S)))).max(), "diffusive:", diffusive(np.linalg.inv(S))[0])

# ---------- A2: closed form, all slots open, no computation noise ----------
say("A2 expect: |code - (1 + n(n+2rho)/(rho(n-1+rho)))| < 1e-9")
for mm, cc in [(4, 0.1), (5, 0.3)]:
    allopen = np.zeros(2 ** mm); allopen[-1] = 1.0
    att = lambda i, p, mm=mm: [(tuple(j for j in range(mm) if j != i), 1.0)]
    Sg = sigma_c_enum(mm, allopen, att, P0, s, cc, 0.0); rho = cc / s
    say("  n,rho", mm, rho, "| code", contrast(np.linalg.inv(Sg), range(mm)), "| formula", 1 + mm * (mm + 2 * rho) / (rho * (mm - 1 + rho)))

# ---------- A3: capacity formula vs enumeration ----------
say("A3 expect: capacity-analytic Sigma equals enumeration to < 1e-12 (m=6, kappa=2)")
m6, k6 = 6, 2
law6, _ = deliberation_law(m6, k6, P0, s, c, 3.0)
def att_cap(i, p):
    op = [j for j in range(m6) if j != i and p[j]]
    if len(op) <= k6: return [(tuple(op), 1.0)]
    cs = list(itertools.combinations(op, k6)); return [(U, 1.0 / len(cs)) for U in cs]
say("  max diff", np.abs(sigma_c_capacity(m6, law6, k6, P0, s, c, s2) - sigma_c_enum(m6, law6, att_cap, P0, s, c, s2)).max())

# ---------- A4: deliberation chain (P4) vs potential law + negative control ----------
say("A4 expect: chain law = exp(-gamma g(S)) law to < 1e-12, detailed balance < 1e-14; control (heterogeneous own precision) violates both")
law, g = deliberation_law(n, n - 1, P0, s, c, gam)
v, db = chain_law(n, n - 1, P0, s, c, gam)
say("  |chain - formula|", np.abs(v - law).max(), "| detailed balance", db)
v2, db2 = chain_law(n, n - 1, P0, s, c, gam, a_own=[1.0, 1.3, 0.8, 1.0])
say("  control: detailed balance", db2)

# ---------- B: full model ----------
SA = sigma_c_enum(n, law, att_full, P0, s, c, s2)
allopen = np.zeros(2 ** n); allopen[-1] = 1
noise_only = SA - s2 * np.eye(n)
profs = profiles(n)
EP = np.zeros(n); EPP = np.zeros((n, n))
for k, p in enumerate(profs):
    S_ = p.sum(); P = 1 / (1 / P0 + p / s + (S_ - p) / (s + c)); EP += law[k] * P; EPP += law[k] * np.outer(P, P)
mv = (EPP - np.outer(EP, EP)) / P0
say("B  P(S=0..4):", np.round([law[profs.sum(1) == k].sum() for k in range(n + 1)], 4))
say("B  Sigma^c_A diag", SA[0, 0], "offdiag beta", SA[0, 1], "| alpha", SA[0, 0] - SA[0, 1],
    "| beta parts: noise", (noise_only - mv)[0, 1], "mean-variation", mv[0, 1])
say("B  exchangeable spread (max-min of diag, of offdiag):", np.ptp(np.diag(SA)), np.ptp(SA[~np.eye(n, dtype=bool)]))
Pi = np.linalg.inv(block_diag(SA, SA))
d = diffusive(Pi)
say("B  expect diffusive with uniform leak: diffusive", d[0], "max offdiag", d[1], "min rowsum", d[2],
    "| leaks", np.round(Pi.sum(1), 6), "| in-niche coupling", -Pi[0, 1], "| cross coupling", -Pi[0, n])
regs = region_contrasts(Pi)
rA, rB = regs[tuple(range(n))], regs[tuple(range(n, N))]
others = {C: r for C, r in regs.items() if C not in (tuple(range(n)), tuple(range(n, N)))}
Cmax = max(others, key=others.get)
say("B  r(A)", rA, "r(B)", rB, "| max over all other regions", others[Cmax], "at", Cmax,
    "| max over regions meeting both niches", max(r for C, r in regs.items() if min(C) < n <= max(C)))
say("B  closed form check 1+n*beta/alpha:", 1 + n * SA[0, 1] / (SA[0, 0] - SA[0, 1]))

# ---------- A5: Monte Carlo check of Sigma^c incl. mean-variation term ----------
say("A5 expect: MC estimate of E[Cov(e|eta)] within 4 s.e. of Sigma^c; control without mean-variation term fails")
T = 200000
k = rng.choice(len(profs), size=T, p=law); p = profs[k].astype(float)
eta = rng.normal(0, np.sqrt(P0), T); o = eta[:, None] + rng.normal(0, np.sqrt(s), (T, n))
nu = rng.normal(0, np.sqrt(c), (T, n, n))
e = np.zeros((T, n))
for i in range(n):
    Sm = p.sum(1) - p[:, i]; Pi_ = 1 / (1 / P0 + p[:, i] / s + Sm / (s + c))
    tot = p[:, i] * o[:, i] / s + sum(p[:, j] * (o[:, j] + nu[:, i, j]) / (s + c) for j in range(n) if j != i)
    e[:, i] = Pi_ * tot + rng.normal(0, np.sqrt(s2), T) - eta
M2 = e.T @ e / T - np.outer(EP, EP) / P0
se = np.sqrt(np.var(e[:, 0] * e[:, 1]) / T)
say("  MC offdiag", M2[0, 1], "exact", SA[0, 1], "s.e.", se, "| MC diag", M2[0, 0], "exact", SA[0, 0],
    "| control exact-without-mv offdiag", (SA - mv)[0, 1], "z", (M2[0, 1] - (SA - mv)[0, 1]) / se)

# ---------- C: baselines ----------
lawN, gN = deliberation_law(N, kappa, P0, s, c, gam)
SH = sigma_c_capacity(N, lawN, kappa, P0, s, c, s2)
PiH = np.linalg.inv(SH); dH = diffusive(PiH)
regH = region_contrasts(PiH); CH = max(regH, key=regH.get)
r_mech = regH[CH]
a = -(Pi - np.diag(np.diag(Pi))); abar = a[np.triu_indices(N, 1)].mean(); ebar = Pi.sum(1).mean()
r_mean = 1 + N * abar / ebar
say("C  (c)-mechanism medium: diffusive", dH[0], "| sup region contrast", r_mech, "attained by size", len(CH),
    "| size-n value", regH[tuple(range(n))])
say("C  (c)-mean coupling / (b) complete graph: abar", abar, "ebar", ebar, "baseline", r_mean)
say("C  (b) niche graph declared: baseline = clique contrast", rA, "-> window empty (trap)")
eps_ratio = Pi.sum(1)[:n].max() / Pi.sum(1)[:n].mean()
lo = max(r_mech, eps_ratio, others[Cmax])
say("C  window (c)-mechanism: (", lo, ",", rA, "]  width", rA - lo, "| (c)-mean: (", max(r_mean, eps_ratio), ",", rA, "]")

# ---------- D: agency ----------
ag, gC, klmin, den, klf = agency_index(law, n, P0, s)
say("D  expect index in (0,1]: Agency", ag, "| fitted gamma_C", gC, "| KL_min", klmin, "| KL(P||E)", den,
    "| habit-only KL", klf(0.0))
lp = lambda q: np.log(law[int("".join(map(str, q)), 2)])
lor = lp((1, 1, 0, 0)) + lp((0, 0, 0, 0)) - lp((1, 0, 0, 0)) - lp((0, 1, 0, 0))
say("D  log odds ratio of members 1,2 (others closed); expect < 0 (redundancy):", lor)

# ---------- E: inference closure ----------
say("E  alpha_I (encoded N(mbar,Pbar)) =", inference_kl(n, law, P0, s, c, s2))

# ---------- F: order parameter ----------
Sg = sigma_c_enum(n, allopen, att_full, P0, s, c, s2); rho12 = Sg[0, 1] / Sg[0, 0]
say("F  beta > 0 implies Omega_int(A|zeta_B) > 0; Gaussian pair MI given eta at all-open profile:", -0.5 * np.log(1 - rho12 ** 2))
open("main_out.txt", "w").write("\n".join(out) + "\n")
