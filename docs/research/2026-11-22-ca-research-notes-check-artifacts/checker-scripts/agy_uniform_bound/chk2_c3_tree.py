"""C3 at m=2 (n=7, 128 profiles): exact matrix-tree check of the C_out factorization, the path-tree ratio identity,
the limit law mu_lambda, with planted-error negative controls. Own code; mpmath, subtraction-free elimination."""
import sys, time
import mpmath as mp
from gear import Model, gth, tree_weight

mp.mp.dps = 34
m, n = 2, 7
h, Delta = mp.mpf("0.9"), mp.mpf("0.1")
E0 = -m * h


def setup(lam, gamma, control=False):
    delta = mp.mpf(lam) / (2 ** m * mp.mpf(gamma))
    M = Model(m, delta, [-h] * n, control=control)
    Phi = [M.Phi(s) for s in range(M.N)]
    P = [s for s in range(M.N) if abs(Phi[s] - E0) < mp.mpf(10) ** -25]
    B = [s for s in range(M.N) if abs(Phi[s] - (E0 + Delta)) < mp.mpf(10) ** -25]
    V0 = set(P) | set(B)
    nb = {a: [a ^ (1 << i) for i in range(n) if (a ^ (1 << i)) in V0] for a in V0}
    ends = [a for a in V0 if len(nb[a]) == 1]
    assert len(ends) == 2 and max(len(v) for v in nb.values()) == 2
    path = [ends[0]]
    prev = None
    while True:
        nx = [b for b in nb[path[-1]] if b != prev]
        if not nx:
            break
        prev = path[-1]
        path.append(nx[0])
    assert len(path) == len(V0) == 13
    mot = set(M.motor)

    def steps(pp):
        sc = [0]
        for a, b in zip(pp[:-1], pp[1:]):
            off = (a & ~b).bit_length() - 1
            on = (b & ~a).bit_length() - 1
            sc.append(sc[-1] + (1 if (off, on) in mot else (-1 if (on, off) in mot else 0)))
        return sc

    if steps(path[::2])[-1] < 0:
        path = path[::-1]
    sc = steps(path[::2])
    return M, delta, Phi, path, sc


def path_tree_weight(q, path, root_pos):
    w = mp.mpf(1)
    for k, a in enumerate(path):
        if k == root_pos:
            continue
        w *= q[a][path[k + 1] if k < root_pos else path[k - 1]]
    return w


def run(lam, gamma, control=False, verbose=True):
    M, delta, Phi, path, sc = setup(lam, gamma, control)
    q = M.rates(gamma)
    V0 = path
    V1 = [s for s in range(M.N) if s not in set(V0)]
    order = V0 + V1
    pi, piv, red = gth(q, order, n_keep=len(V0))
    Cout = mp.mpf(1)
    for s in V1:
        Cout *= piv[s]
    # censored chain on V0 (indices follow 'path'); W(x) = Cout * Wtilde(x)
    idx = list(range(len(V0)))
    rho, Wt = [], []
    for k in range(0, len(path), 2):
        wt = tree_weight(red, idx, k)
        Wt.append(wt)
        rho.append(wt / path_tree_weight(q, path, k))
    # consistency: stationary law from GTH equals Cout*Wtilde normalised (matrix-tree theorem)
    Ps = [pi[path[k]] for k in range(0, len(path), 2)]
    mctt_err = max(abs((Wt[i] / Wt[0]) / (Ps[i] / Ps[0]) - 1) for i in range(len(Ps)))
    # path-tree ratio identity
    w0 = path_tree_weight(q, path, 0)
    ident = [mp.log(path_tree_weight(q, path, 2 * i) / w0) - 2 * mp.mpf(lam) * sc[i] / 2 ** m for i in range(len(sc))]
    wrong = [mp.log(path_tree_weight(q, path, 2 * i) / w0) - mp.mpf(lam) * sc[i] / 2 ** m for i in range(len(sc))]
    bound = (2 * n) ** len(V0) * mp.exp(-mp.mpf(gamma) * (Delta - (6 * 2 ** m - 8) * delta))
    massP = mp.fsum(Ps)
    mu = [mp.exp(2 * mp.mpf(lam) * s / 2 ** m) for s in sc]
    Zm = mp.fsum(mu)
    mu = [x / Zm for x in mu]
    tv_mu = (mp.fsum(abs(Ps[i] - mu[i]) for i in range(len(mu))) + (1 - massP)) / 2
    Pphi = [mp.exp(-mp.mpf(gamma) * (Phi[s] - E0)) for s in range(M.N)]
    Zp = mp.fsum(Pphi)
    tv_phi = mp.fsum(abs(pi[s] - Pphi[s] / Zp) for s in range(M.N)) / 2
    lr = mp.log((pi[path[-1]] / (Pphi[path[-1]] / Zp)) / (pi[path[0]] / (Pphi[path[0]] / Zp)))
    maxlog = max(abs(mp.log(pi[s] / (Pphi[s] / Zp))) for s in range(M.N))
    # R sanity
    sig = max(abs(M.R(u, s | (1 << u)) - M.R(u, s & ~(1 << u))) for u in range(n) for s in range(M.N))
    if verbose:
        print(f"lam={lam} gamma={gamma} delta={mp.nstr(delta, 6)} sigma_max(LG)={mp.nstr(sig, 6)} control={control}")
        print("   s along P_2:", sc)
        print("   rho(x)-1 = W(x)/(C_out w_path(x)) - 1 over x in P_2:", [mp.nstr(r - 1, 4) for r in rho])
        print(f"   min(rho-1)={mp.nstr(min(rho) - 1, 4)} (must be >=0)   proved upper bound on rho-1: {mp.nstr(bound, 4)}   within bound: {all(r - 1 <= bound for r in rho)}")
        print(f"   matrix-tree vs GTH stationary law (ratios on P_2), max rel err: {mp.nstr(mctt_err, 3)}")
        print(f"   path-tree identity ln[w(v_k)/w(v_0)] - 2 lam s_k/2^m, max abs: {mp.nstr(max(abs(x) for x in ident), 3)}"
              f"   [planted wrong exponent lam s_k/2^m: max abs {mp.nstr(max(abs(x) for x in wrong), 6)}]")
        print(f"   mass(P_2)={mp.nstr(massP, 10)}  TV(Pinf, mu_lam)={mp.nstr(tv_mu, 6)}  ln-ratio(vL,v0)={mp.nstr(lr, 12)} (2 lam={2 * lam})"
              f"  TV(Pinf,P_Phi)={mp.nstr(tv_phi, 8)}  max|ln(Pinf/P_Phi)|={mp.nstr(maxlog, 8)}  2(|A|-1) g s={mp.nstr(2 * 127 * mp.mpf(gamma) * delta, 6)}")
    return dict(rho=rho, ident=ident, lr=lr, tv_phi=tv_phi, tv_mu=tv_mu, maxlog=maxlog, Cout=Cout, q=q, path=path, red=red, piv=piv, Wt=Wt)


t0 = time.time()
print("== exact factorization, identity and limit law at m=2 ==")
for lam, gamma in [(1, 40), (1, 120), (4, 120), (4, 600), (1, 2000)]:
    r = run(lam, gamma)
    assert min(r["rho"]) >= 1 - mp.mpf(10) ** -25
    assert max(abs(x) for x in r["ident"]) < mp.mpf(10) ** -25
    print(f"   [elapsed {time.time() - t0:.1f}s]")

print("\n== negative controls ==")
# (a) potential perturbation (+d,+d): identity with 2 lam s/2^m must fail, ln ratio ~ 0
r = run(4, 120, control=True, verbose=False)
print(f" (a) potential control (+d,+d), lam=4, gamma=120: max|identity residual|={mp.nstr(max(abs(x) for x in r['ident']), 6)} (identity fails), "
      f"ln-ratio(vL,v0)={mp.nstr(r['lr'], 6)}, TV(Pinf,P_Phi)={mp.nstr(r['tv_phi'], 6)}")
# (b) wrong split: forests of V1 u B_2 rooted in P_2 used as 'C_out' with the same path tree weight -> ratio not 1
r = run(4, 120, verbose=False)
q, path = r["q"], r["path"]
Pset = path[::2]
rest = [s for s in range(128) if s not in set(Pset)]
_, piv2, _ = gth(q, Pset + rest, n_keep=len(Pset))
Cbad = mp.mpf(1)
for s in rest:
    Cbad *= piv2[s]
W0 = r["Cout"] * r["Wt"][0]


def pw(q, path, root_pos):
    w = mp.mpf(1)
    for k, a in enumerate(path):
        if k != root_pos:
            w *= q[a][path[k + 1] if k < root_pos else path[k - 1]]
    return w


print(f" (b) planted wrong split (C_out over V1 u B_2): W(v0)/(C_bad w_path(v0)) = {mp.nstr(W0 / (Cbad * pw(q, path, 0)), 8)} (not 1)")
print(f"total {time.time() - t0:.1f}s")
