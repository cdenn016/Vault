"""C4 at m=2: limit law P_lambda, cross-ratio identity for independent-block beliefs (generic log-det computation),
TV lower bound R(2 sqrt p - R), and a scope test: a group posterior on the SAME slot model with a weakly
correlated declared belief. Own code."""
import time
import numpy as np
import mpmath as mp
from scipy.optimize import minimize
from gear import Model, gth, build_graph, v_of_I

mp.mp.dps = 30
rng = np.random.default_rng(20261122)
m, n = 2, 7
h, Delta, b = mp.mpf("0.9"), mp.mpf("0.1"), mp.mpf("0.01")
A_, B_, C_, D_ = (1 << 0) | (1 << 4), (1 << 2) | (1 << 4), (1 << 0) | (1 << 6), (1 << 2) | (1 << 6)
bonus = [0, 2, 4, 6]


def checkpoint_model(delta):
    c = [-h] * n
    for u in bonus:
        c[u] = c[u] - b
    c[6] = c[6] + 2 ** m * mp.mpf(delta)
    return Model(m, delta, c)


def stationary(M, gamma):
    q = M.rates(gamma)
    pi, _, _ = gth(q, list(range(M.N)))
    return pi


t0 = time.time()
print("== C4(1): limit law of the 4-checkpoint model, fixed lambda = 4*gamma*delta ==")
store = {}
for lam, gamma in [(1, 180), (1, 1000), (1, 4000), (4, 180), (4, 1000), (4, 4000)]:
    delta = mp.mpf(lam) / (4 * gamma)
    M = checkpoint_model(delta)
    pi = stationary(M, gamma)
    pl = mp.exp(lam) / (2 * (1 + mp.exp(lam)))
    Plam = {A_: mp.mpf(1) / 2 - pl, B_: pl, C_: pl, D_: mp.mpf(1) / 2 - pl}
    tv = mp.fsum(abs(pi[s] - Plam.get(s, 0)) for s in range(M.N)) / 2
    sig = max(abs(M.R(u, s | (1 << u)) - M.R(u, s & ~(1 << u))) for u in range(n) for s in range(M.N))
    div = max(abs(mp.fsum(M.R(u, s ^ (1 << u)) - M.R(u, s) for u in range(n))) for s in range(M.N))
    store[(lam, gamma)] = (M, pi, delta)
    print(f" lam={lam} gamma={gamma:5d} delta={mp.nstr(delta, 4)} sigma_max={mp.nstr(sig, 4)} max|div R|={mp.nstr(div, 2)}: "
          f"P(A,B,C,D)=({mp.nstr(pi[A_], 6)},{mp.nstr(pi[B_], 6)},{mp.nstr(pi[C_], 6)},{mp.nstr(pi[D_], 6)}) "
          f"limit p_lam={mp.nstr(pl, 6)}  TV(Pinf,P_lam)={mp.nstr(tv, 4)}  [{time.time() - t0:.1f}s]")

print("\n== C4(3): fixed delta=2e-5 (< b/(3*2^7)=2.6e-5), gamma -> infinity ==")
for gamma in [10 ** 4, 10 ** 5, 4 * 10 ** 5]:
    delta = mp.mpf("2e-5")
    M = checkpoint_model(delta)
    pi = stationary(M, gamma)
    store[("fix", gamma)] = (M, pi, delta)
    pmin = min(pi[B_], pi[C_])
    print(f" gamma={gamma:7d} (4*gamma*delta={mp.nstr(4 * gamma * delta, 4)}): P(A,B,C,D)=({mp.nstr(pi[A_], 6)},{mp.nstr(pi[B_], 6)},"
          f"{mp.nstr(pi[C_], 6)},{mp.nstr(pi[D_], 6)})  2*sqrt(min(pB,pC))-1={mp.nstr(2 * mp.sqrt(pmin) - 1, 6)}  [{time.time() - t0:.1f}s]")

# ---------------------------------------------------------------------------------------------
# generic Gaussian machinery on the m=2 slot model: 14 coordinates, slot (u,e) = eta_e + unit noise
# ---------------------------------------------------------------------------------------------
_, sizes, offs, edges, motor = build_graph(m)
elist = list(edges)
slots = [[k for k, e in enumerate(elist) if u in e] for u in range(n)]


def info_gen(Sigma, s):
    rows = [k for u in range(n) if (s >> u) & 1 for k in slots[u]]
    if not rows:
        return 0.0
    S = Sigma[np.ix_(rows, rows)]
    return 0.5 * np.linalg.slogdet(np.eye(len(rows)) + S)[1]


def multi_info(Sigma):
    own = [info_gen(Sigma, 1 << u) for u in range(n)]
    return np.array([sum(own[u] for u in range(n) if (s >> u) & 1) - info_gen(Sigma, s) for s in range(1 << n)]), own


print("\n== C4(2): cross-ratio P(A)P(D)/(P(B)P(C)) for Class-2 posteriors, generic log-det computation ==")
worst = 0.0
for trial in range(40):
    var = rng.uniform(0.05, 60.0, size=len(elist))
    Mi, _ = multi_info(np.diag(var))
    f = rng.normal(0, 3, size=n)  # habits and own-policy pragmatic/epistemic terms: free single-site fields
    gC = rng.uniform(0, 30)
    logw = np.array([sum(f[u] for u in range(n) if (s >> u) & 1) for s in range(1 << n)]) - gC * Mi
    cr = logw[A_] + logw[D_] - logw[B_] - logw[C_]
    worst = max(worst, abs(cr))
print(f" 40 random independent-block beliefs (random variances, fields, gamma_C in [0,30]): max |ln cross-ratio| = {worst:.2e}")
Sig = np.diag(np.array([float(v_of_I(1 if edges[e] == 'adj' else 5)) for e in elist]))
vC = np.diag(Sig).copy()


def correlated(rho):
    S = Sig.copy()
    for (ea, eb) in [((0, 1), (4, 5)), ((2, 3), (5, 6))]:
        i, j = elist.index(ea), elist.index(eb)
        S[i, j] = S[j, i] = rho * np.sqrt(S[i, i] * S[j, j])
    return S


Mi_c, _ = multi_info(correlated(0.5))
print(f" control, correlated belief rho=0.5 on (eta_01,eta_45),(eta_23,eta_56): M(A),M(B),M(C),M(D) = "
      f"{Mi_c[A_]:.5f},{Mi_c[B_]:.2e},{Mi_c[C_]:.2e},{Mi_c[D_]:.5f} -> ln cross-ratio = -gamma_C*{Mi_c[A_] + Mi_c[D_] - Mi_c[B_] - Mi_c[C_]:.5f} (nonzero)")

print("\n== C4 Step 3: min TV(P_lam, Q) subject to Q(A)Q(D) >= kappa Q(B)Q(C), numerical minimisation vs R(2 sqrt p - R) ==")


def min_tv(p, kappa, trials=60):
    P = np.array([0.5 - p, p, p, 0.5 - p, 0.0])  # A,B,C,D,rest
    best = 1.0

    def obj(z):
        qv = np.exp(z - z.max())
        qv /= qv.sum()
        pen = max(0.0, np.log(kappa) + np.log(qv[1]) + np.log(qv[2]) - np.log(qv[0]) - np.log(qv[3]))
        return 0.5 * np.abs(P - qv).sum() + 10.0 * pen

    for _ in range(trials):
        z0 = rng.normal(0, 2, size=5)
        res = minimize(obj, z0, method="Nelder-Mead", options={"xatol": 1e-11, "fatol": 1e-13, "maxiter": 6000})
        best = min(best, res.fun)
    return best


for lam, kappa in [(1.0, 1.0), (4.0, 1.0), (12.0, 1.0), (4.0, 0.8), (4.0, 0.5), (1.0, 0.9)]:
    p = np.exp(lam) / (2 * (1 + np.exp(lam)))
    Rr = kappa ** -0.25
    claim = Rr * (2 * np.sqrt(p) - Rr) if Rr <= 2 * np.sqrt(p) else float("nan")
    num = min_tv(p, kappa)
    print(f" lam={lam:5.1f} kappa={kappa:.2f} R={Rr:.4f}: claimed lower bound={claim:.6f}  numerical min TV={num:.6f}  "
          f"violation={num < claim - 1e-6}  planted wrong bound 2sqrt(p)-0.5={2 * np.sqrt(p) - 0.5:.4f} violated={num < 2 * np.sqrt(p) - 0.5}")

print("\n== Scope test: same slot model, weakly CORRELATED declared belief q_C', product habits, precision gamma_C ==")


def J_of_rho(rho):
    return multi_info(correlated(rho))[0][A_]


def solve_rho(target):
    lo, hi = 0.0, 0.9
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if J_of_rho(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def scope(M, pi, delta, gamma, K, label):
    target = float(2 ** m * delta) / K
    rho = solve_rho(target)
    Sc = correlated(rho)
    Mi, own = multi_info(Sc)
    gC = K * gamma
    # single-site fields (free product habits absorb them): -gamma*(own costs without the tilt)
    cost = [float(-h - (b if u in bonus else 0)) for u in range(n)]
    logw = [mp.mpf(-gamma) * mp.fsum(mp.mpf(cost[u]) for u in range(n) if (s >> u) & 1) - mp.mpf(gC) * mp.mpf(float(Mi[s])) for s in range(1 << n)]
    mx = max(logw)
    w = [mp.exp(x - mx) for x in logw]
    Z = mp.fsum(w)
    Q = [x / Z for x in w]
    tv = mp.fsum(abs(pi[s] - Q[s]) for s in range(1 << n)) / 2
    # sigma_max(q_C'): members' beliefs are the model's diagonal q_u; declared belief is Sc
    sig = 0.0
    for u in range(n):
        for s in range(1 << n):
            if (s >> u) & 1:
                continue
            s1 = s | (1 << u)
            red_u = float(M.info(u, 1 << u) + M.info(u, s) - M.info(u, s1))
            red_c = own[u] + info_gen(Sc, s) - info_gen(Sc, s1)
            sig = max(sig, abs(red_u - red_c))
    pmin = min(pi[B_], pi[C_])
    print(f" {label}: gamma={gamma} delta={mp.nstr(delta, 4)} gamma_C={K}*gamma rho={rho:.5f} M'(A)={Mi[A_]:.3e} M'(D)={Mi[D_]:.3e} M'(B)={Mi[B_]:.1e} M'(C)={Mi[C_]:.1e}")
    print(f"     sigma_max(q_C')={sig:.4e} = {sig / float(delta):.3f}*delta ; gamma_C*sigma_max(q_C')={gC * sig:.3f} ; "
          f"TV(Pinf, Q)={mp.nstr(tv, 5)}  vs independent-block lower bound 2sqrt(min(pB,pC))-1={mp.nstr(2 * mp.sqrt(pmin) - 1, 5)}")


for key, K in [(("fix", 10 ** 5), 1), (("fix", 4 * 10 ** 5), 1), ((4, 1000), 1), ((4, 4000), 1), ((4, 4000), 20), ((1, 4000), 20)]:
    M, pi, delta = store[key]
    gamma = key[1]
    scope(M, pi, delta, gamma, K, f"regime {key}")
print(f"total {time.time() - t0:.1f}s")
