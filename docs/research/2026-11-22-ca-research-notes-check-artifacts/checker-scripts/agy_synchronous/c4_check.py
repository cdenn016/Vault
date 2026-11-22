"""Independent check of C4 (conj_agy_synchronous.md) and of the manuscript form ex:agy-synchronous-cycle.
Own implementation following the manuscript's formulas (s05_agency.tex / app05_agency.tex), random parameters,
gamma_C != gamma, pragmatic terms in the reversed-cycle model, extremes, and planted controls.
Also: Gaussian residual covariance identity quoted in the note's Scope section.
"""
from itertools import product
import numpy as np

rng = np.random.default_rng(23)
states = list(product(range(3), repeat=3))


def post(G, E, gamma):
    lp = -gamma * G + np.log(E[0])[:, None, None] + np.log(E[1])[None, :, None] + np.log(E[2])[None, None, :]
    P = np.exp(lp - lp.max())
    return P / P.sum()


def sync_stat(G, E, gamma):
    P = post(G, E, gamma)
    K = [P / P.sum(axis=i, keepdims=True) for i in range(3)]
    T = np.zeros((27, 27))
    for a, s in enumerate(states):
        for b, t in enumerate(states):
            pr = 1.0
            for i in range(3):
                u = list(s)
                u[i] = t[i]
                pr *= K[i][tuple(u)]
            T[a, b] = pr
    A = np.vstack([T.T - np.eye(27), np.ones(27)])
    rhs = np.zeros(28)
    rhs[-1] = 1
    return np.linalg.lstsq(A, rhs, rcond=None)[0].reshape(3, 3, 3)


def G_from_slots(reads, snr, psi):
    """reads[i][a] = coordinate index read by member i's policy a (a=1,2); snr[coordinate]; first principles logdet"""
    G = np.zeros((3, 3, 3))
    for s in states:
        Lam = np.ones(3)
        cost = 0.0
        for i, a in enumerate(s):
            if a:
                Lam[reads[i][a]] += snr[reads[i][a]]
                cost += psi[i][a]
        G[s] = -0.5 * np.log(Lam).sum() + cost
    return G


def snr_for(I):
    R = np.exp(2 * I)
    return (R - 1) + np.sqrt((R - 1) ** 2 + (R - 1))


def run(h2, E, psi, gamma, gC, variant="correct"):
    # clockwise: policy 1 of member i reads eta_i, policy 2 reads eta_{i+1}
    reads = [{1: i, 2: (i + 1) % 3} for i in range(3)]
    G = G_from_slots(reads, h2, psi)
    ps = sync_stat(G, E, gamma)
    I = [0.5 * np.log((1 + x) ** 2 / (1 + 2 * x)) for x in h2]
    g = [[0.0, G[tuple(1 if j == i else 0 for j in range(3))], G[tuple(2 if j == i else 0 for j in range(3))]] for i in range(3)]
    w = [[E[i][a] * np.exp(-gamma * g[i][a]) for a in range(3)] for i in range(3)]
    al = [np.exp(-gamma * x) for x in I]

    def Z(k, pi_i, pi_ip1):      # k = i+2 ; manuscript formula
        i = (k + 1) % 3
        return w[k][0] + w[k][1] * al[k] ** (pi_ip1 == 2) + w[k][2] * al[i] ** (pi_i == 1)

    Jt = []
    for i in range(3):
        k = (i + 2) % 3
        Jt.append(-np.log(Z(k, 1, 2) * Z(k, 0, 0) / (Z(k, 1, 0) * Z(k, 0, 2))))
    ht = [[np.log(w[i][0]),
           np.log(w[i][1]) + np.log(Z((i + 2) % 3, 1, 0) / Z((i + 2) % 3, 0, 0)),
           np.log(w[i][2]) + np.log(Z((i + 1) % 3, 0, 2) / Z((i + 1) % 3, 0, 0))] for i in range(3)]
    # reversed cycle: coordinate e=(i,i+1) read by policy 1 of member i and policy 2 of member i+1
    if variant == "correct":
        reads_t = [{1: i, 2: (i - 1) % 3} for i in range(3)]
    else:  # planted: pair policy 1 of member i with policy 1 of member i+1
        reads_t = [{1: i, 2: (i + 1) % 3} for i in range(3)]
    st = [snr_for(Jt[e] / gC) for e in range(3)]
    psi_t = [[0.0, 0.5 * np.log(2 * np.pi * np.e * (1 + st[reads_t[i][1]])), 0.5 * np.log(2 * np.pi * np.e * (1 + st[reads_t[i][2]]))] for i in range(3)]
    Gt = G_from_slots(reads_t, st, psi_t)
    Et = []
    for i in range(3):
        e = np.array([np.exp(ht[i][a] + gC * Gt[tuple(a if j == i else 0 for j in range(3))]) for a in range(3)])
        Et.append(e / e.sum())
    Pt = post(Gt, Et, gC)
    L = np.log(ps)
    lor = L[1, 0, 2] + L[0, 0, 0] - L[1, 0, 0] - L[0, 0, 2]
    red_t = Gt[1, 2, 0] - Gt[1, 0, 0] - Gt[0, 2, 0] + Gt[0, 0, 0]
    best_same = min(0.5 * np.abs(ps - post(G, E, gp)).sum() for gp in np.linspace(0.0, 3 * gamma, 301))
    return dict(tv=0.5 * np.abs(ps - Pt).sum(), lor=lor, I0=I[0], Jt=Jt, red_t=red_t, Jt0_over_gC=Jt[0] / gC,
                tv_same=0.5 * np.abs(ps - post(G, E, gamma)).sum(), best_same=best_same, minEt=min(e.min() for e in Et))


print("random instances (gamma_C != gamma, random SNRs, habits, costs)")
worst = 0.0
for tr in range(12):
    h2 = rng.uniform(0.2, 6.0, size=3)
    E = [rng.dirichlet(np.ones(3) * 2) for _ in range(3)]
    psi = [[0.0] + list(rng.uniform(-0.6, 0.6, size=2)) for _ in range(3)]
    gamma = float(rng.uniform(0.1, 6.0))
    gC = float(rng.uniform(0.1, 6.0))
    r = run(h2, E, psi, gamma, gC)
    worst = max(worst, r["tv"])
    assert min(r["Jt"]) > 0 and r["minEt"] > 0
    if tr < 4:
        print(f"  gamma={gamma:.3f} gamma_C={gC:.3f}: TV(P_sync, reversed posterior)={r['tv']:.2e}  cond. LOR(pi0=1,pi2=2|pi1=0)={r['lor']:+.1e} vs -gamma*I0={-gamma * r['I0']:+.4f}  "
              f"reversed redundancy {r['red_t']:.6f} = J~/gamma_C {r['Jt0_over_gC']:.6f}  TV to P_C(gamma)={r['tv_same']:.4f}  min over gamma' in [0,3gamma] of TV to P_C(gamma';E,G_C)={r['best_same']:.2e}")
print(f"  max TV over 12 instances = {worst:.2e}")
assert worst < 1e-12
h2 = np.array([1.5 ** 2, 2.0 ** 2, 1.2 ** 2])
E = [np.array([0.20, 0.35, 0.45]), np.array([0.30, 0.40, 0.30]), np.array([0.25, 0.25, 0.50])]
psi = [[0.0, 0.3, -0.2], [0.0, 0.1, 0.4], [0.0, -0.1, 0.2]]
print("extremes on the note's instance (h=(1.5,2.0,1.2))")
for gamma, gC in [(1e-3, 1.0), (0.2, 0.2), (1.0, 5.0), (5.0, 0.05), (30.0, 1.0)]:
    r = run(h2, E, psi, gamma, gC)
    print(f"  gamma={gamma:<6g} gamma_C={gC:<5g}: TV={r['tv']:.2e}  J~=({r['Jt'][0]:.3e},{r['Jt'][1]:.3e},{r['Jt'][2]:.3e})  TV to P_C(gamma)={r['tv_same']:.6f}")
r = run(h2, E, psi, 1.0, 1.0, variant="planted")
print(f"planted control (reversed model pairs policy 1 with policy 1): TV = {r['tv']:.3e}")
# equal parameters
r = run(np.array([1.0, 1.0, 1.0]), [np.ones(3) / 3] * 3, [[0.0, 0.0, 0.0]] * 3, 1.0, 1.0)
print(f"symmetric instance (all SNR 1, uniform habits, zero costs): TV={r['tv']:.2e}, J~={r['Jt'][0]:.6f}")

# Gaussian remark in the Scope section: Cov(Y)-Cov(X) = D^-1 (Lam - D) D^-1
M = rng.normal(size=(4, 4))
Lam = M @ M.T + 4 * np.eye(4)
D = np.diag(np.diag(Lam))
Sig = np.linalg.inv(Lam)
Aop = -np.linalg.inv(D) @ (Lam - D)
CovY = Aop @ Sig @ Aop.T + np.linalg.inv(D)
print("Gaussian parallel-Gibbs remark: max|Cov(Y)-Cov(X) - D^-1(Lam-D)D^-1| =", f"{np.abs(CovY - Sig - np.linalg.inv(D) @ (Lam - D) @ np.linalg.inv(D)).max():.2e}")
print("done")
