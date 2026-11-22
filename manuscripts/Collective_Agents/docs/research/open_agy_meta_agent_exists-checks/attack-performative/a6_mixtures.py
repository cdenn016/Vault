r"""Attack A6: independent recomputation of the two numbers that decide PN's every-constant differ clause against
N_hab under the M1 baseline: the annealed habit-null contrast (investigator: 4.409, Monte Carlo) and the mechanism
baseline M1 (investigator: 5.0754, Gaussian second-moment approximation of the collider).

Method (not Monte Carlo over noises): sample attention sequences a; for each, error rows over standardized noises are
propagated exactly with the members' exact time-varying Kalman gains; then
   Sigma^c = E_eta Cov(e | eta) = E_a Cov(e | eta, a) + E_a[K_a S_eta K_a^T] - Kbar S_eta Kbar^T,
with K_a = Cov(e, eta | a) Cov(eta | a)^{-1} and S_eta = E_a Cov(eta | a).  This is exact for N_hab (no act feedback,
so eta is exogenous and P(a | eta) = P(a)); for M1 (acts on the common component) it replaces P(a | eta) by P(a).
Prior errors obey e_i(t+1) = F e_i^+(t) - w_t whatever the acts, and U enters only the world path.

Declared expectations: N_hab annealed in [4.3, 4.5]; M1 in [5.0, 5.15]; NEG controls: attention fixed on all three
niche-mates without acts must give 28.5 (+-0.05); M1 without acts must give the investigator's no-act value 6.8586
(+-0.05).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

F, Q, R, Rc, b = 0.9, 0.05, 1.0, 0.2, 0.2


def run(mode: str, g: float, nsamp: int, T: int = 60, ts: int = 45, seed: int = 0) -> float:
    rng = np.random.default_rng(seed)
    if mode == "M1":
        N, comp = 8, [0] * 8
        members = list(range(8))
    else:
        N, comp = 8, [0] * 4 + [1] * 4
        members = list(range(4))  # niche A; B is independent and uninformative for A
    pairs = [(i, j) for i in range(N) for j in range(N) if i != j]
    pidx = {p: q for q, p in enumerate(pairs)}
    per = 1 + N + len(pairs)
    NT = 1 + per * T
    sig0 = np.sqrt(Q / (1 - F * F))
    covs, Ks_list, Seta_list = [], [], []
    for s in range(nsamp):
        eta = np.zeros((T + 1, NT))
        eta[0, 0] = sig0
        e = {i: np.zeros(NT) for i in members}
        for i in members:
            e[i][0] = -sig0  # m_i(0) = 0
        Pm = {i: Q / (1 - F * F) for i in members}
        Erows = None
        for t in range(T):
            base = 1 + per * t
            if t == ts:
                Erows = np.array([e[i] for i in members])
            ep = {}
            for i in members:
                if mode == "fixed":
                    part = [j for j in members if j != i]
                else:
                    others = [j for j in range(N) if j != i]
                    part = list(rng.choice(others, size=3, replace=False))
                inf = [j for j in part if comp[j] == comp[i]]
                Pp = 1.0 / (1.0 / Pm[i] + 1.0 / R + len(inf) / (R + Rc))
                Ks, Kc = Pp / R, Pp / (R + Rc)
                row = (1 - Ks - len(inf) * Kc) * e[i]
                row[base + 1 + i] += Ks * np.sqrt(R)
                for j in inf:
                    row[base + 1 + j] += Kc * np.sqrt(R)
                    row[base + 1 + N + pidx[(i, j)]] += Kc * np.sqrt(Rc)
                ep[i] = row
                Pm[i] = F * F * Pp + Q
            # acts: U = -g sum_i (eta + e_i^+) over acting members on this component
            U = -g * sum(eta[t] + ep[i] for i in members)
            eta[t + 1] = F * eta[t] + b * U
            eta[t + 1][base] += np.sqrt(Q)
            for i in members:
                e[i] = F * ep[i]
                e[i][base] -= np.sqrt(Q)
        H = eta
        G = H @ H.T
        C_eh = Erows @ H.T
        Ka = np.linalg.solve(G, C_eh.T).T
        cov_cond = Erows @ Erows.T - Ka @ C_eh.T
        covs.append(cov_cond)
        Ks_list.append(Ka)
        Seta_list.append(G)
    S_eta = np.mean(Seta_list, axis=0)
    Kbar = np.mean(Ks_list, axis=0)
    mix = np.mean([K @ S_eta @ K.T for K in Ks_list], axis=0) - Kbar @ S_eta @ Kbar.T
    Sig = np.mean(covs, axis=0) + mix
    n = len(members)
    diag = np.mean(np.diag(Sig))
    off = (Sig.sum() - np.trace(Sig)) / (n * (n - 1))
    alpha = diag - off
    v = alpha + n * off
    Pi = np.linalg.inv(0.5 * (Sig + Sig.T))
    offd = Pi - np.diag(np.diag(Pi))
    return v / alpha, float(offd.max()), float(Pi.sum(axis=1).min()), float(np.trace(mix) / np.trace(Sig))


if __name__ == "__main__":
    r, mo, mr, fr = run("fixed", 0.0, 1)
    print("NEG fixed attention, no acts: r=%.4f (expect 28.5) max_off=%.2e min_row=%.3f" % (r, mo, mr))
    for seed in [1, 2]:
        r, mo, mr, fr = run("hab", 0.0, 1500, seed=seed)
        print("N_hab annealed (exact mixture second moment), seed %d: r=%.4f  max_off=%.2e min_row=%.3f  mixture-mean share %.3f" % (
            seed, r, mo, mr, fr))
    r, mo, mr, fr = run("M1", 0.0, 400, seed=3)
    print("NEG M1 without acts: r=%.4f (investigator no-act 6.8586)" % r)
    for seed in [4, 5]:
        r, mo, mr, fr = run("M1", 0.05, 400, seed=seed)
        print("M1 with acts g=0.05 (P(a|eta)~P(a)), seed %d: r=%.4f max_off=%.2e min_row=%.3f mixture-mean share %.4f" % (
            seed, r, mo, mr, fr))
    for seed in [6]:
        r, mo, mr, fr = run("hab", 0.05, 1500, seed=seed)
        print("N_pr annealed with acts g=0.05 (P(a|eta)~P(a)), seed %d: r=%.4f" % (seed, r))
