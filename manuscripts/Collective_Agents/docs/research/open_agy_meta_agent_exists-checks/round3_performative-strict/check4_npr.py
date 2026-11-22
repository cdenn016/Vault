r"""check4: partner randomization N_pr (redrawn every round) for the TDF instance, by exact row propagation.

Every random variable is a row over standardized noises; for one partner sequence the world-conditional covariance
Cov(e(t*) | eta_0..eta_T) is exact.  Annealed second moment (def:col-contrast second-moment convention) as in round-1
attack A8: Sigma = mean_s Cov_s + mixture part (mean_s K_s S K_s^T - Kbar S Kbar^T), with P(seq | eta) ~ P(seq).
Each member reads one relay per round (its attention rate); under N_pr the sender is drawn uniformly from the other 7.
Two conventions for a sender that is not the department mate:
  'zero'  : the receiver's channel model gives it zero gain (instance I*'s convention for other-niche channels);
  'kept'  : the receiver applies its kept relay gain, reading the foreign raw reading as its own eta_{t-1}.
Declared expectations BEFORE running:
  VAL  partners fixed to the mates reproduce the stationary full Sigma of lgx (max abs diff < 1e-6);
  E1   'kept': annealed Pi diffusive with r(C0) far below the window's lower edge 3.8747 (mixture terms dominate);
  E2   'zero': no prediction (the collider's same-department repulsion may make the annealed Pi non-diffusive).
"""
import numpy as np
import lgx
from tdf import tdf_spec, groups

nd, nf = 2, 2
F, Q, R, Rc, qc, QZ, h, beta, sa2 = 0.9, 0.05, 1.0, 0.1, 1e-4, 0.05, 1.0, 1.0, 0.01
KAP = 0.68
N = 2 * nd * nf
Kc = 3 * nf
spec = tdf_spec(nd, nf, Rc=Rc, kappa=KAP)
mod = lgx.build(spec, "full")
Kg = mod["gains"][0]["K"]  # identical for every member (same R, Rc, one relay)
AF = np.array([[F, 0.0], [1.0, 0.0]])
comp = [a["k"] for a in spec["agents"]]
kap = [a["kappa"] for a in spec["agents"]]
mate = {i: spec["agents"][i]["senders"][0] for i in range(N)}
firm_of = [i // (2 * nd) for i in range(N)]


def simulate(seq: np.ndarray, T: int, tstar: int, mode: str):
    per = Kc + N + N + 2 * N + N
    ncol = Kc + per * T
    col = 0
    eta = np.zeros((Kc, ncol))
    for k in range(Kc):
        var = Q / (1 - F * F) if k % 3 != 2 else QZ
        eta[k, col] = np.sqrt(var)
        col += 1
    lag = np.zeros((Kc, ncol))
    m = np.zeros((N, 2, ncol))           # prior means (rows); start at 0
    vlag = np.zeros((N, ncol))
    H = [eta.copy()]
    E = None
    for t in range(T):
        base = Kc + per * t
        w = lambda k: base + k
        v = lambda j: base + Kc + j
        nu = lambda i: base + Kc + N + i
        qn = lambda i, c: base + Kc + 2 * N + 2 * i + c
        an = lambda i: base + Kc + 4 * N + i
        if t == tstar:
            E = np.array([m[i, 0] - eta[comp[i]] for i in range(N)])
        mp = np.zeros((N, 2, ncol))
        for i in range(N):
            k = comp[i]
            s = eta[k].copy(); s[v(i)] += np.sqrt(R)
            p = seq[t, i]
            innov0 = s - m[i, 0]
            if p == mate[i]:
                y = lag[k] + vlag[p]; y = y.copy(); y[nu(i)] += np.sqrt(Rc)
                mp[i] = m[i] + np.outer(Kg[:, 0], innov0) + np.outer(Kg[:, 1], y - m[i, 1])
            elif mode == "kept":
                y = lag[comp[p]] + vlag[p]; y = y.copy(); y[nu(i)] += np.sqrt(Rc)
                mp[i] = m[i] + np.outer(Kg[:, 0], innov0) + np.outer(Kg[:, 1], y - m[i, 1])
            else:
                mp[i] = m[i] + np.outer(Kg[:, 0], innov0)
        u = np.zeros((N, ncol))
        for i in range(N):
            u[i] = -kap[i] * mp[i, 0]
            u[i, an(i)] += np.sqrt(sa2)
        new = np.zeros((Kc, ncol))
        for f in range(nf):
            for k in (3 * f, 3 * f + 1):
                new[k] = F * eta[k]; new[k, w(k)] += np.sqrt(Q)
            z = 3 * f + 2
            new[z] = h * (eta[3 * f] - eta[3 * f + 1]) + beta * sum(u[i] for i in range(N) if firm_of[i] == f)
            new[z, w(z)] += np.sqrt(QZ)
        for i in range(N):
            m[i] = AF @ mp[i]
            m[i, 0, qn(i, 0)] += np.sqrt(qc); m[i, 1, qn(i, 1)] += np.sqrt(qc)
        vlag = np.zeros((N, ncol))
        for j in range(N):
            vlag[j, v(j)] = np.sqrt(R)
        lag = eta
        eta = new
        H.append(eta.copy())
    Hm = np.vstack(H)
    G = Hm @ Hm.T
    CE = E @ Hm.T
    Ks = np.linalg.solve(G, CE.T).T
    return E @ E.T - Ks @ CE.T, Ks, G


def annealed(mode: str, nseq: int, T: int, tstar: int, seed: int):
    rng = np.random.default_rng(seed)
    covs, Ks, Gs = [], [], []
    for _ in range(nseq):
        seq = np.zeros((T, N), dtype=int)
        for i in range(N):
            others = np.array([j for j in range(N) if j != i])
            seq[:, i] = rng.choice(others, size=T)
        c, k, g = simulate(seq, T, tstar, mode)
        covs.append(c); Ks.append(k); Gs.append(g)
    Sg = np.mean(Gs, axis=0)
    Kb = np.mean(Ks, axis=0)
    mix = np.mean([k @ Sg @ k.T for k in Ks], axis=0) - Kb @ Sg @ Kb.T
    Cb = np.mean(covs, axis=0)
    return 0.5 * (Cb + Cb.T), 0.5 * (mix + mix.T)


def report(name, S):
    P = np.linalg.inv(S)
    d = lgx.diffusivity(P)
    Gd = groups(nd, nf)
    line = f"{name}: diffusive={d['diffusive']} (max off {d['max_off']:+.3f}, min row {d['min_row']:.3f})"
    if d["diffusive"]:
        top = lgx.all_regions(P, top=3)
        line += (f"; r(C0)={lgx.contrast(P, Gd['C0'])['r']:.4f} r(B0)={lgx.contrast(P, Gd['B0'])['r']:.4f}; "
                 f"top {[(round(r, 3), C) for r, C, _ in top]}")
    else:
        off = P - np.diag(np.diag(P))
        i, j = np.unravel_index(np.argmax(off), off.shape)
        line += f"; largest positive entry at ({i},{j})"
    print(line)
    return P


if __name__ == "__main__":
    T, tstar = 70, 45
    seq = np.array([[mate[i] for i in range(N)]] * T)
    c, _, _ = simulate(seq, T, tstar, "zero")
    S_ref = lgx.sigma_c(spec, "full", 60)
    print(f"VAL fixed mates: max|row-propagation - lgx stationary| = {np.max(np.abs(c - S_ref)):.2e}")
    for mode, seed in (("zero", 1), ("kept", 2)):
        Sa, mix = annealed(mode, 150, T, tstar, seed)
        print(f"[{mode}] mean diag {np.mean(np.diag(Sa)):.5f}, mixture part diag {np.mean(np.diag(mix)):.5f}")
        report(f"N_pr annealed '{mode}' (cov part + mixture)", Sa + mix)
        Sb, mixb = annealed(mode, 150, T, tstar, seed + 10)
        report(f"N_pr annealed '{mode}' replicate", Sb + mixb)
