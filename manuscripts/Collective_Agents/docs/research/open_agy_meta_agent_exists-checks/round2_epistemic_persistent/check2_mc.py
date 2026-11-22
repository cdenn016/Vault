r"""Check 2: two-replica Monte Carlo with sampled Gaussians (actual filters on sampled data) against the exact
pair-moment algebra, on the same pairs of policy paths.

For each pair of independent policy paths, G Gaussian draws of (shared world path; independent private noises of
the two replicas); the members run their Kalman filters on the sampled data; Sigma^c is estimated by
1/2 E[(e^1 - e^2)(e^1 - e^2)^T] at the evaluation times.
Declared expectations (before running):
 (a) at I*, the MC estimates of alpha and beta agree with the exact pair moments of the same policy pairs within
     3 standard errors;
 (b) at a high-mixture variant (Rs = 0.3, psi = 0.06, other parameters of I*), the policy-mixture part of beta is
     resolvable: MC agrees with the exact Sigma^c within 3 SE and disagrees with E[Cov(e|eta,pi)] alone by more than
     3 SE (NEGATIVE CONTROL: the estimator without the mixture term must fail);
 (c) NEGATIVE CONTROL: an exact computation that treats the relayed sensing noise as fresh noise (no sharing)
     must disagree with the MC beta by more than 10 SE.
"""
import time
import numpy as np
from lib import Par, simulate_policy_path, pair_moments, posterior, A_F, compound
from instance import PAR


def mc_pair(par: Par, pa, pb, t_eval, G: int, rng):
    n = par.n
    Tn = pa.Pm.shape[0]
    Af = A_F(par.F)
    V0 = par.Q / (1 - par.F ** 2)
    eta_prev = rng.normal(0, np.sqrt(V0), G)
    eta = par.F * eta_prev + rng.normal(0, np.sqrt(par.Q), G)  # x_0 = (eta_0, eta_{-1}) stationary
    m = [np.zeros((n, 2, G)), np.zeros((n, 2, G))]
    vprev = [rng.normal(0, np.sqrt(par.R), (n, G)), rng.normal(0, np.sqrt(par.R), (n, G))]
    acc = np.zeros((n, n)); cnt = 0
    paths = (pa, pb)
    t_set = set(t_eval)
    for t in range(Tn):
        if t in t_set:
            d = m[0][:, 0, :] - m[1][:, 0, :]        # e^1 - e^2 = m^1 - m^2 (eta cancels)
            acc += 0.5 * (d @ d.T) / G
            cnt += 1
        newm = []
        vnow = []
        for r in (0, 1):
            pth = paths[r]
            v = rng.normal(0, np.sqrt(par.R), (n, G))
            vnow.append(v)
            mr = np.zeros((n, 2, G))
            nopen = int(pth.slots[t].sum())
            for i in range(n):
                Pm = pth.Pm[t, i]
                mts = pth.mates[t][i]
                a = 1 / par.R + nopen / (par.Rs + par.Rsh)
                b = len(mts) / (par.R + par.Rc)
                Pp = posterior(Pm, a, b)
                Im = np.linalg.inv(Pm)
                h0 = (eta + v[i]) / par.R                                # own sensor
                for k in range(n):
                    if pth.slots[t, k]:
                        h0 = h0 + (eta + rng.normal(0, np.sqrt(par.Rs), G)) / (par.Rs + par.Rsh)
                h1 = np.zeros(G)
                for j in mts:
                    h1 = h1 + (eta_prev + vprev[r][j] + rng.normal(0, np.sqrt(par.Rc), G)) / (par.R + par.Rc)
                info = Im @ m[r][i] + np.vstack([h0, h1])
                mplus = Pp @ info
                mr[i] = Af @ mplus + rng.normal(0, np.sqrt(par.qc), (2, G))
            newm.append(mr)
        w = rng.normal(0, np.sqrt(par.Q), G)
        eta_prev, eta = eta, par.F * eta + w
        m = newm
        vprev = vnow
    return acc / cnt


def run(par: Par, npairs: int, G: int, seed: int, label: str, fresh_control=False):
    rng = np.random.default_rng(seed)
    t_eval = list(range(80, 300, 4))
    mc_ab, ex_ab, pv_ab = [], [], []
    for k in range(npairs):
        pa = simulate_policy_path(par, 300, rng, "full")
        pb = simulate_policy_path(par, 300, rng, "full")
        ex = pair_moments(par, pa, pb, t_eval)
        S_ex = np.mean([e[0] for e in ex], axis=0)
        S_pv = np.mean([0.5 * (e[1] + e[2]) for e in ex], axis=0)
        S_mc = mc_pair(par, pa, pb, t_eval, G, rng)
        mc_ab.append(compound(S_mc)); ex_ab.append(compound(S_ex)); pv_ab.append(compound(S_pv))
    mc_ab, ex_ab, pv_ab = map(np.array, (mc_ab, ex_ab, pv_ab))
    diff = mc_ab - ex_ab
    se = diff.std(0, ddof=1) / np.sqrt(npairs)
    z = diff.mean(0) / se
    dpv = mc_ab - pv_ab
    sepv = dpv.std(0, ddof=1) / np.sqrt(npairs)
    print(f"[{label}] {npairs} policy pairs x {G} Gaussian draws: exact alpha,beta = {ex_ab.mean(0)}, "
          f"MC = {mc_ab.mean(0)}; z(MC - exact) = {np.round(z, 2)}")
    print(f"[{label}] E[Cov(e|eta,pi)] only: alpha,beta = {pv_ab.mean(0)}; z(MC - E[Cov] only) = "
          f"{np.round(dpv.mean(0) / sepv, 2)}; mixture part of beta (exact) {ex_ab[:, 1].mean() - pv_ab[:, 1].mean():.3e}")
    return mc_ab, ex_ab, pv_ab


t0 = time.time()
mc, ex, pv = run(PAR, 24, 300, 8101, "I*")
print(f"  t={time.time()-t0:.0f}s", flush=True)
run(PAR.with_(Rs=0.3, psi=0.06), 24, 300, 8102, "high-mixture variant")
print(f"  t={time.time()-t0:.0f}s", flush=True)
# (c) NEG: exact algebra with the relayed sensing noise treated as fresh (no sharing): beta of that computation
from lib import sigma_c
neg = sigma_c(PAR, "full", 10, 300, 80, 4, seed=8103, fresh_relays=True)
se_b = (mc[:, 1] - ex[:, 1]).std(ddof=1) / np.sqrt(len(mc))
print(f"(c) NEG: no-sharing computation beta = {neg['beta']:.3e} vs MC beta {mc[:, 1].mean():.3e}; "
      f"difference / SE = {(mc[:, 1].mean() - neg['beta']) / se_b:.1f}")
print(f"total {time.time()-t0:.1f}s")
