r"""Deciding script D1: collective clause of I** (def:col-collective 04_collectives.tex:214-221) for one protocol.

Exact Gaussian algebra per pair of independent policy paths (shared world, independent private inputs), Monte Carlo
over 160 pairs; second-moment convention Sigma^c = E[Cov(e(t)|eta)] (def:col-contrast :187).
Declared expectations (before running), from the exploration at the same parameters:
  r(A) in [8.3, 8.6] with jackknife SE < 0.03; compound projection beta > 0, so Pi^c diffusive (C1);
  raw Sigma^c_A within 5 SE of compound symmetry (exchangeability in law), mixture part of beta below 1e-4;
  other regions: max (1+3b)/(1+b) about 2.3, regions meeting both niches <= 1 (closed forms checked);
  mechanism medium (8 agents) 5.8 to 6.3; mean-coupling baseline 1 + (6/7)(r(A)-1) about 7.4;
  declared r0 = 7.9 inside both windows.
  NEGATIVE CONTROL: Rc = 1e6 (useless relays) gives r(A) within 0.05 of 1 and an empty window.
"""
import time
import numpy as np
from lib3 import sigma_c, compound, contrast, is_diffusive, region_contrasts, population_precision, \
    mean_coupling_baseline
from instance3 import PAR, MEDIUM, T, BURN, EVERY, R0, PROTO

t0 = time.time()
f = sigma_c(PAR, 160, T, BURN, EVERY, seed=101)
S = f["S"]
al, be = f["alpha"], f["beta"]
b = be / al
print("I** =", PAR)
print(f"[A] pairs=160, T={T}, burn={BURN}, every {EVERY}; open rate {f['open_rate']:.4f}; "
      f"attention deficit rate {f['dev_rate']:.2e} per member-round")
print("[A] raw Sigma^c_A =\n", np.array2string(S, precision=8))
dev = S - (al * np.eye(4) + be)
print(f"[A] compound projection alpha={al:.8f} (SE {f['se_alpha']:.1e}) beta={be:.8f} (SE {f['se_beta']:.1e}); "
      f"max |raw - compound| = {np.abs(dev).max():.2e} = {np.abs(dev).max()/f['se_beta']:.2f} x SE(beta)")
print(f"[A] E[Cov(e|eta,pi)]: alpha={f['alpha_priv']:.8f} beta={f['beta_priv']:.8f}; mixture part of beta "
      f"{be - f['beta_priv']:.2e}, of alpha {al - f['alpha_priv']:.2e}")
print(f"[A] r(A) = {f['r']:.4f} +/- {f['se_r']:.4f} (jackknife over pairs); r from E[Cov] only {f['r_priv']:.4f}")
Pi, S8 = population_precision(al, be)
d = is_diffusive(Pi)
print(f"[A] Pi^c (8x8) diffusive={d[0]}, largest off-diagonal {d[1]:.3e}, smallest row sum {d[2]:.4f}; "
      f"coupling a={-Pi[0,1]:.4f} leak eps={Pi.sum(1)[0]:.4f} a/eps={-Pi[0,1]/Pi.sum(1)[0]:.4f} (= beta/alpha {b:.4f})")
rc = region_contrasts(Pi)
others = {C: v for C, v in rc.items() if C not in ((0, 1, 2, 3), (4, 5, 6, 7))}
best = max(others, key=others.get)
meet = max(v for C, v in rc.items() if any(c < 4 for c in C) and any(c >= 4 for c in C))
print(f"[A] r(A)={rc[(0,1,2,3)]:.4f} r(B)={rc[(4,5,6,7)]:.4f}; largest other region {best}: {others[best]:.4f} "
      f"(closed form (1+3b)/(1+b) = {(1+3*b)/(1+b):.4f}); largest region meeting both niches {meet:.6f}")
print(f"  time {time.time()-t0:.0f}s", flush=True)
t1 = time.time()
m = sigma_c(MEDIUM, 50, T, BURN, EVERY, seed=202)
SM = m["S"]
PiM = np.linalg.inv(m["alpha"] * np.eye(8) + m["beta"] * np.ones((8, 8)))
rcM = region_contrasts(PiM)
bM = max(rcM, key=rcM.get)
print(f"[medium] pairs=50; open rate {m['open_rate']:.4f}; alpha={m['alpha']:.8f} beta={m['beta']:.8f}; "
      f"max |raw - compound| {np.abs(SM - (m['alpha']*np.eye(8)+m['beta'])).max():.2e}; "
      f"whole-medium contrast {m['r']:.4f} +/- {m['se_r']:.4f}; sup over regions {rcM[bM]:.4f} at {bM}; "
      f"diffusive {is_diffusive(PiM)[0]}  ({time.time()-t1:.0f}s)", flush=True)
mc_sup, mc_formula = mean_coupling_baseline(Pi)
print(f"[mean coupling] sup over regions {mc_sup:.4f}; formula 1+N abar/ebar {mc_formula:.4f}; "
      f"1+(6/7)(r(A)-1) {1+6/7*(f['r']-1):.4f}")
print(f"WINDOW mechanism: ({m['r']:.4f}, {f['r']:.4f}]  r0={R0}: inside {m['r'] < R0 <= f['r']}; margins "
      f"r(A)-r0 {f['r']-R0:.4f}, r0-medium {R0-m['r']:.4f}")
print(f"WINDOW mean-coupling: ({mc_sup:.4f}, {f['r']:.4f}]  r0={R0}: inside {mc_sup < R0 <= f['r']}; margins "
      f"r(A)-r0 {f['r']-R0:.4f}, r0-baseline {R0-mc_sup:.4f}")
print(f"Selection at r0: other regions <= {others[best]:.4f} < r0: {others[best] < R0}; leak ratio on A "
      f"{Pi.sum(1)[:4].max()/Pi.sum(1)[:4].mean():.6f} < r0")
neg = sigma_c(PAR.with_(Rc=1e6), 6, 250, 60, 5, seed=303)
negM = sigma_c(MEDIUM.with_(Rc=1e6), 3, 250, 60, 5, seed=304)
print(f"NEG (Rc=1e6): r(A)={neg['r']:.4f}, medium={negM['r']:.4f}; window empty: {neg['r'] <= max(negM['r'], 1+6/7*(neg['r']-1)) + 1e-9 or neg['r'] < 1.05}")
np.savez(f"d1_{PROTO}.npz", S=S, al=al, be=be, r=f["r"], se_r=f["se_r"], rM=m["r"], seM=m["se_r"], mc=mc_sup,
         ab=f["ab"], abM=m["ab"])
print(f"total {time.time()-t0:.0f}s")
