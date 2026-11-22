r"""Check 0: validation of the two implementations against each other, with negative controls.

Declared expectations before running:
  (a) aud.py pair-moment algebra on deterministic 'fixedS' paths reproduces the exact Lyapunov Sigma^c to <1e-12
      after burn-in;
  (b) sim.py sampled-noise Monte Carlo ('fixedS') agrees with the exact values within 3 standard errors;
  (c) sim.py 'full' (EFE attention at gamma = 40) agrees with 'fixedS' (attention deviations ~1e-14);
  (d) the habit null by aud.py exact pair algebra and by sim.py Monte Carlo agree within 3 standard errors;
  NEGATIVE CONTROLS (must fail to look like the full model):
  (e) independent worlds per replica inflate the audience covariance by far more than 10 standard errors;
  (f) channels that deliver pure noise ('dead') give an audience covariance within 3 SE of 0.
"""
import time
import numpy as np
from aud import Par, riccati_fixed, b_of, stationary_fixed, coords, simulate_path, pair_moments, sigma_mc, \
    symmetrize_audience
import sim

t0 = time.time()
par = Par()
Pm_S, _ = riccati_fixed(par, 1.0 / par.RS, 0.0)
Pm_A, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
Pm = np.array([Pm_S] + [Pm_A] * par.n)
att = [tuple()] + [(0,)] * par.n
S, _, _ = stationary_fixed(par, att, Pm)
Sc = coords(par, S)
print("exact Sigma^c (fixedS):", np.round(Sc, 8).tolist())

rng = np.random.default_rng(1)
pa = simulate_path(par, 300, rng, "fixedS")
pb = simulate_path(par, 300, rng, "fixedS")
res = pair_moments(par, pa, pb, [299])
print(f"(a) pair algebra vs Lyapunov at t=299: max abs diff {np.max(np.abs(res[0][0] - Sc)):.3e}")


def summarize(o, n):
    Sb = np.array([symmetrize_audience(x) for x in o["S_b"]])
    vals = np.array([[x[0, 0], x[0, 1], x[1, 1], x[1, 2]] for x in Sb])
    m = vals.mean(0)
    se = vals.std(0, ddof=1) / np.sqrt(len(vals))
    return m, se


o = sim.run(par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma, K=3000, T=300, burn=60,
            seed=11, mode="fixedS")
m, se = summarize(o, par.n)
ex = np.array([Sc[0, 0], Sc[0, 1], Sc[1, 1], Sc[1, 2]])
print(f"(b) sim fixedS [varS, cov(S,i), var i, cov(i,j)] = {np.round(m, 7)} +- {np.round(se, 7)}; z = {np.round((m - ex) / se, 2)}")
o = sim.run(par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma, K=3000, T=300, burn=60,
            seed=12, mode="full")
m2, se2 = summarize(o, par.n)
print(f"(c) sim full = {np.round(m2, 7)} +- {np.round(se2, 7)}; z vs exact = {np.round((m2 - ex) / se2, 2)}; "
      f"read_src {o['read_src']:.6f}, read_tot {o['read_tot']:.6f}")

hx = sigma_mc(par, "hab", npairs=120, T=300, burn=80, every=2, seed=21)
Sh = np.array([symmetrize_audience(x) for x in hx["S_pairs"]])
vh = np.array([[x[0, 0], x[0, 1], x[1, 1], x[1, 2]] for x in Sh])
mh, seh = vh.mean(0), vh.std(0, ddof=1) / np.sqrt(len(vh))
o = sim.run(par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma, K=3000, T=300, burn=80,
            seed=22, mode="hab")
m3, se3 = summarize(o, par.n)
print(f"(d) habit null: exact-pair MC {np.round(mh, 7)} +- {np.round(seh, 7)}")
print(f"               sim MC        {np.round(m3, 7)} +- {np.round(se3, 7)}; z = {np.round((mh - m3) / np.sqrt(seh**2 + se3**2), 2)}")

o = sim.run(par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma, K=1500, T=300, burn=60,
            seed=13, mode="fixedS", shared=False)
m4, se4 = summarize(o, par.n)
print(f"(e) NEG independent worlds: cov(i,j) {m4[3]:.6e} vs exact {ex[3]:.6e}: excess {(m4[3]-ex[3])/se4[3]:.1f} SE")
o = sim.run(par.F, par.Q, par.R, par.RS, par.Rc, par.qc, par.n, par.kmsg, par.gamma, K=1500, T=300, burn=60,
            seed=14, mode="dead")
m5, se5 = summarize(o, par.n)
print(f"(f) NEG dead channels: cov(i,j) {m5[3]:.3e} +- {se5[3]:.3e}; cov(S,i) {m5[1]:.3e} +- {se5[1]:.3e}")
print(f"({time.time() - t0:.0f}s)")
