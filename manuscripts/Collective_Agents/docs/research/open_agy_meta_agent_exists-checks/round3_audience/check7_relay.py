r"""Check 7: relay variant P1 of the audience (kmsg = 2: each member reads the source and, by expected free energy,
one more channel; every other parameter as P0), which makes the members interact with one another.

Computed: full-model Sigma^c (exact pair algebra over Monte Carlo policy paths; the mate choice is random and the
gains switch between 'source only' and 'source + mate'); contrast, regions, the source's coupling; mean-coupling and
M-perm baselines (exact from Sigma^c), M-F medium with kmsg = 2 (sampled Monte Carlo); N_hab, N_pr (2 partners
redrawn every round); member-restricted order parameter Omega_int(A | zeta_S) through the members' covariance with
the source's private inputs conditioned on; agency under the full-policy reading (11 policies per member, 14641
profiles, class G2); memory and inference (fixed-state brackets).

Declared expectations before running: Pi^c diffusive; r(A) between 5.4 and 7; source still out of the block;
N_hab, N_pr below 2.5 and below every baseline; Omega covariance positive (> 1e-6) while the same computation for P0
gives 0 to 1e-15 (NEGATIVE CONTROL); full-policy agency between 0.99 and 1; d_M and inference KL below 0.03.
"""
import itertools
import time
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
import sim
from aud import Par, riccati_fixed, b_of, diffusive, contrast, all_regions, mean_coupling_baseline, type_law, \
    sigma_mc, symmetrize_audience, posterior, A_F, info

t0 = time.time()
par = Par(kmsg=2)
A = tuple(range(1, par.N))


def exch(S):
    N = S.shape[0]
    d = np.trace(S) / N
    o = (S.sum() - np.trace(S)) / (N * (N - 1))
    return d - o, o


def rep(Sm, label):
    Pi = np.linalg.inv(Sm)
    dif = diffusive(Pi)
    tab = {C: contrast(Pi, C) for C in all_regions(par.N)}
    oth = max((v, k) for k, v in tab.items() if k != A)
    print(f"[{label}] diffusive {dif[0]} (max off {dif[1]:.2e}, min row {dif[2]:.2e}); r(A) {tab[A]:.4f}; best other "
          f"{oth[0]:.4f} {oth[1]}; couplings: pair {-Pi[1,2]:.3f}, source {-Pi[0,1]:.3f}")
    return Pi, tab


# full model
x = sigma_mc(par, "full", npairs=120, T=300, burn=80, every=2, seed=701)
Ss = np.array([symmetrize_audience(s) for s in x["S_pairs"]])
Sm = Ss.mean(0)
Pi, tab = rep(Sm, "P1 full (exact pair MC)")
rb = np.array([contrast(np.linalg.inv(Ss[b::20].mean(0)), A) for b in range(20)])
print(f"   r(A) SE {rb.std(ddof=1)/np.sqrt(20):.4f}; 'source only' rounds fraction {x['dev_rate']:.3f}; "
      f"mixture part of cov(i,j) {(Sm - symmetrize_audience(x['Priv']))[1,2]:.2e}")
o = sim.run(par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma, K=3000, T=300, burn=80,
            seed=702, mode="full")
rep(symmetrize_audience(o["S"]), "P1 full (sampled-noise cross-check)")
mcb = mean_coupling_baseline(Pi)[0]
al, be = exch(Sm)
mperm = 1 + par.N * be / al
oF = sim.run(par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma, K=2500, T=300, burn=80,
             seed=703, mode="full", src=False, Rmed=par.R)
a2, b2 = exch(oF["S"])
print(f"baselines: mean coupling {mcb:.4f}; M-perm {mperm:.4f}; M-F (kmsg=2) {1 + par.N * b2 / a2:.4f}  ({time.time()-t0:.0f}s)")

for mode in ("hab", "pr"):
    xn = sigma_mc(par, mode, npairs=120, T=300, burn=80, every=2, seed=710 + len(mode))
    Sn = np.array([symmetrize_audience(s) for s in xn["S_pairs"]])
    rep(Sn.mean(0), f"P1 null {mode}")
print(f"({time.time()-t0:.0f}s)")

# member-restricted order parameter: covariance of members' errors with the source's private inputs conditioned on
for p_, lab in ((par, "P1"), (Par(), "NEG P0")):
    xo = sigma_mc(p_, "full", npairs=30, T=200, burn=60, every=2, seed=720, excl_src=True)
    Pv = symmetrize_audience(xo["Priv"])
    print(f"[{lab}] E[Cov(e_i, e_j | X_sh, zeta_S, routing)] = {Pv[1,2]:.3e} (var {Pv[1,1]:.3e}); "
          f"=> Omega_int(A | zeta_S) {'> 0' if Pv[1,2] > 1e-9 else '= 0'}")

# agency, full-policy reading: 11 policies per member
sets = [()] + [(j,) for j in range(4)] + list(itertools.combinations(range(4), 2))   # 0 = source, 1..3 = mates
E1 = np.full(len(sets), 1.0 / len(sets))
hasS = np.array([1 if 0 in s else 0 for s in sets])
nm = np.array([sum(1 for j in s if j != 0) for s in sets])


def member_law(Pm):
    G = np.array([-info(Pm, 1 / par.R, b_of(par, hasS[k], nm[k])) for k in range(len(sets))])
    lw = np.log(E1) - par.gamma * G
    lw -= lw.max()
    q = np.exp(lw)
    return q / q.sum()


profs = np.array(list(itertools.product(range(len(sets)), repeat=par.n)))
kS = hasS[profs].sum(1)
lnE = np.log(E1)[profs].sum(1)
res = []
for lab, (s, m) in (("state S+m", (1, 1)), ("state S", (1, 0))):
    Pm, _ = riccati_fixed(par, 1 / par.R, b_of(par, s, m))
    q = member_law(Pm)
    lnP = np.log(q)[profs].sum(1)
    P = np.exp(lnP)
    Vu = Pm[1, 1] + par.RS
    GC = -0.5 * np.log1p(np.arange(par.n + 1) * Vu / par.Rc)
    den = float(np.sum(P * (lnP - lnE)))
    best = (den, 0.0)
    for gC in np.concatenate([[0.0], np.geomspace(1e-2, 1e5, 600)]):
        lw = lnE - gC * GC[kS]
        mx = lw.max()
        v = float(np.sum(P * (lnP - (lw - (mx + np.log(np.exp(lw - mx).sum()))))))
        if v < best[0]:
            best = (v, gC)
    res.append((den, best[0]))
    print(f"agency at {lab}: member law on (S), (S,m_j) = {q[1]:.4f}, {q[5]:.4f} x3; KL(P||E) {den:.4f}; "
          f"inf KL(P||P_g) {best[0]:.5f} at gamma_C {best[1]:.3g}; index {1 - best[0]/den:.5f}")
fr = x["dev_rate"]
den = (1 - fr) * res[0][0] + fr * res[1][0]
num = (1 - fr) * res[0][1] + fr * res[1][1]
print(f"two declared decision states weighted by frequency: index >= {1 - num/den:.5f} (separate gamma_C per state is "
      f"not allowed, so this is an upper bound; the single-state values bracket it)")

# memory and inference at the fixed 'S+m' state (bracket)
Pm, Pp = riccati_fixed(par, 1 / par.R, b_of(par, 1, 1))
M = A_F(par.F) @ Pp @ np.linalg.inv(Pm)
k_rel = Pp[:, 1] / (par.R + par.Rc)
Qn = par.qc * np.eye(2) + par.Rc * A_F(par.F) @ np.outer(k_rel, k_rel) @ A_F(par.F).T
S1 = solve_discrete_lyapunov(M, Qn)
c = np.array([1.0, 0.0])
ac = []
Pk = S1.copy()
for k in range(62):
    ac.append(float(c @ Pk @ c)); Pk = M @ Pk
def cv(m):
    T = np.array([[ac[abs(i - j)] for j in range(m + 1)] for i in range(m + 1)])
    return T[m, m] - T[:m, m] @ np.linalg.solve(T[:m, :m], T[:m, m])
print(f"memory at the 'S+m' state (relay noise internal): d_M = {0.5*np.log(cv(1)/cv(60)):.4f}  ({time.time()-t0:.0f}s)")
