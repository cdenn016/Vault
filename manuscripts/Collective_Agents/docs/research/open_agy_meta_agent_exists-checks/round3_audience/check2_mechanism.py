r"""Check 2: clause (c) mechanism baselines (04_collectives.tex:202) for instance P0, under declared media.

  M-F    N = 5 agents of the audience type (own sensor R, broadcast, capacity kmsg = 1, EFE attention, gamma = 40):
         the exchangeable state of the attention mechanism without a distinguished source.
  M-S    as M-F with every sensor of the source type (RS).
  M-perm the full model's Sigma^c averaged over relabelings (second moment over a uniformly random source position);
         exchangeable in law.  The whole-medium contrast is 1 + N beta/alpha by C1.
  M-sym  the population's types kept and attention in its uniform state (= N_pr every round): reported in check 1.
Baseline = sup over regions of the medium; for an exchangeable (compound-symmetric) precision it is attained by the
whole medium (lem:col-uniform-leak; C1), and the script also enumerates all regions.

Declared expectations before running: M-F baseline below 1.6; M-S baseline below 3.0; M-perm baseline below the
mean-coupling baseline 3.817 (averaging covariances before inverting dilutes the block).
NEGATIVE CONTROL: M-F with Rc = 1e6 (channels useless) must give a baseline within 0.02 of 1.
"""
import time
import numpy as np
import sim
from aud import Par, riccati_fixed, b_of, stationary_fixed, coords, contrast, all_regions

t0 = time.time()
par = Par()


def exch(S):
    N = S.shape[0]
    d = np.trace(S) / N
    o = (S.sum() - np.trace(S)) / (N * (N - 1))
    return d - o, o


def medium(Rmed, label, Rc=None, seed=0):
    o = sim.run(par.F, par.Q, par.R, par.RS, par.Rc if Rc is None else Rc, par.qc, par.n, par.kmsg, par.gamma,
                K=2500, T=300, burn=80, seed=seed, mode="full", src=False, Rmed=Rmed)
    al, be = exch(o["S"])
    ab = np.array([exch(s) for s in o["S_b"]])
    rb = 1 + par.N * ab[:, 1] / ab[:, 0]
    N = par.N
    Sm = (al) * np.eye(N) + be * np.ones((N, N))
    Pi = np.linalg.inv(Sm)
    best = max(contrast(Pi, C) for C in all_regions(N))
    print(f"[{label}] alpha {al:.4e} beta {be:.4e}; whole-medium contrast 1+N beta/alpha = {1 + N * be / al:.4f} "
          f"+- {rb.std(ddof=1)/np.sqrt(len(rb)):.4f}; enumerated sup {best:.4f}; channels read per agent {o['read_tot']:.3f}")
    return best


bF = medium(par.R, "M-F (audience type)", seed=31)
bS = medium(par.RS, "M-S (source type)", seed=32)
# M-perm: exact
Pm_S, _ = riccati_fixed(par, 1.0 / par.RS, 0.0)
Pm_A, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
Pm = np.array([Pm_S] + [Pm_A] * par.n)
S, _, _ = stationary_fixed(par, [tuple()] + [(0,)] * par.n, Pm)
Sc = coords(par, S)
al, be = exch(Sc)
print(f"[M-perm (exact)] alpha {al:.4e} beta {be:.4e}; whole-medium contrast {1 + par.N * be / al:.4f}")
medium(par.R, "NEG M-F with Rc = 1e6", Rc=1e6, seed=33)
print(f"({time.time() - t0:.0f}s)")
