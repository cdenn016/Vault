r"""Deciding script 1: collective clause at the declared instance I*.

Computes, by exact Gaussian algebra per pair of independent policy paths (shared world path, independent private
noises) and Monte Carlo over the policy paths only:
  Sigma^c_A (second-moment convention of def:col-contrast, 04_collectives.tex:187), its split into
  E[Cov(e|eta,pi)] and the policy-mixture term, compound-symmetry deviation, diffusivity, contrast of every region
  of the 8-agent population (cross-niche block exactly 0, niche B a copy of A by the niche-swap symmetry),
  the clause (c) mechanism medium (MEDIUM: one component, 8 agents) and the clause (c) mean-coupling medium.
Declared expectations (before running): r(A) about 4.3 with jackknife SE below 0.05; Pi^c diffusive with
compound-symmetric blocks; largest contrast of any other region below 2; mechanism baseline about 2.9; mean-coupling
baseline 1 + (6/7)(r(A)-1) about 3.9; both windows nonempty.  NEGATIVE CONTROL: the same pipeline with useless
relays (Rc = 1e6) must give r(A) within 0.02 of 1 and an empty window.
"""
import time
import numpy as np
from lib import Par, sigma_c, compound, contrast, diffusive, region_contrasts
from instance import PAR, MEDIUM, T, BURN, EVERY, M, PROTO


def jack_r(ab: np.ndarray, n: int):
    al, be = ab[:, 0], ab[:, 1]
    K = len(ab)
    r_all = 1 + n * be.mean() / al.mean()
    loo = np.array([1 + n * (be.sum() - be[k]) / (al.sum() - al[k]) for k in range(K)])
    se = np.sqrt((K - 1) / K * np.sum((loo - loo.mean()) ** 2))
    return r_all, se


def population_precision(al: float, be: float, n: int = 4):
    SA = al * np.eye(n) + be * np.ones((n, n))
    S = np.zeros((2 * n, 2 * n)); S[:n, :n] = SA; S[n:, n:] = SA
    return np.linalg.inv(S), S


t0 = time.time()
full = sigma_c(PAR, M("full"), 160, T, BURN, EVERY, seed=101)
rA, seA = jack_r(full["ab"], 4)
S = full["S"]
print("I* =", PAR, " protocol:", PROTO)
print(f"[full] pairs=160, rounds/path={T}, burn={BURN}, eval every {EVERY}; open rate {full['open_rate']:.4f}; "
      f"attention deviation rate {full['dev_rate']:.2e} per member-round")
print("[full] raw Sigma^c_A =\n", np.array2string(S, precision=7))
print(f"[full] compound projection alpha={full['alpha']:.7f} beta={full['beta']:.7f} "
      f"(SE {full['se_alpha']:.1e}, {full['se_beta']:.1e}); max raw deviation from compound "
      f"{np.abs(S - (full['alpha'] * np.eye(4) + full['beta'])).max():.2e}")
print(f"[full] E[Cov(e|eta,pi)]: alpha={full['alpha_priv']:.7f} beta={full['beta_priv']:.7f}; mixture part of beta "
      f"{full['beta'] - full['beta_priv']:.7f}, of alpha {full['alpha'] - full['alpha_priv']:.7f}")
print(f"[full] r(A) = {rA:.4f} +/- {seA:.4f} (jackknife over pairs); r from E[Cov] alone {full['r_priv']:.4f}")
Pi, S8 = population_precision(full["alpha"], full["beta"])
d = diffusive(Pi)
print(f"[full] Pi^c (8x8, blocks compound) diffusive={d[0]} largest offdiag={d[1]:.3e} smallest row sum={d[2]:.4f}")
Pi_raw = np.linalg.inv(np.block([[S, np.zeros((4, 4))], [np.zeros((4, 4)), S]]))
d_raw = diffusive(Pi_raw)
print(f"[full] raw (unsymmetrized) blocks: diffusive={d_raw[0]} largest offdiag={d_raw[1]:.3e} "
      f"smallest row sum={d_raw[2]:.4f}; r(A) raw={contrast(Pi_raw, range(4)):.4f}")
eps = Pi.sum(1); a = -Pi[0, 1]
print(f"[full] leak eps={eps[0]:.4f} (ratio max/mean on A {eps[:4].max()/eps[:4].mean():.6f}), coupling a={a:.4f}, "
      f"a/eps={a/eps[0]:.4f}, cross coupling {-Pi[0,4]:.1e}")
rc = region_contrasts(Pi)
others = {C: v for C, v in rc.items() if C not in ((0, 1, 2, 3), (4, 5, 6, 7))}
best = max(others, key=others.get)
meet = max(v for C, v in rc.items() if any(c < 4 for c in C) and any(c >= 4 for c in C))
print(f"[full] r(A)={rc[(0,1,2,3)]:.4f}, r(B)={rc[(4,5,6,7)]:.4f}; largest other region {best}: {others[best]:.4f}; "
      f"largest region meeting both niches {meet:.4f}; whole population {rc[tuple(range(8))]:.4f}")
print(f"  time {time.time()-t0:.1f}s", flush=True)

t1 = time.time()
med = sigma_c(MEDIUM, M("full"), 50, T, BURN, EVERY, seed=202)
rM, seM = jack_r(med["ab"], 8)
SM = med["S"]
PiM = np.linalg.inv(med["alpha"] * np.eye(8) + med["beta"] * np.ones((8, 8)))
rcM = region_contrasts(PiM)
bestM = max(rcM, key=rcM.get)
print(f"[mechanism medium] pairs=50; open rate {med['open_rate']:.4f}; deviation rate {med['dev_rate']:.2e}; "
      f"alpha={med['alpha']:.7f} beta={med['beta']:.7f}; raw deviation from compound "
      f"{np.abs(SM - (med['alpha'] * np.eye(8) + med['beta'])).max():.2e}")
print(f"[mechanism medium] whole-medium contrast {rM:.4f} +/- {seM:.4f}; sup over regions {rcM[bestM]:.4f} "
      f"attained by {bestM}; diffusive={diffusive(PiM)[0]}")
print(f"  time {time.time()-t1:.1f}s", flush=True)

# clause (c) mean-coupling medium of the population precision
N = 8
abar = sum(-Pi[i, j] for i in range(N) for j in range(i + 1, N)) / (N * (N - 1) / 2)
ebar = Pi.sum(1).mean()
Pmc = np.diag(np.full(N, ebar)) + abar * (N * np.eye(N) - np.ones((N, N)))
rc_mc = region_contrasts(Pmc)
r_mc = max(rc_mc.values())
print(f"[mean-coupling medium] abar={abar:.4f} ebar={ebar:.4f}: sup over regions {r_mc:.4f} "
      f"(formula 1+N abar/ebar = {1 + N * abar / ebar:.4f}; 1+(6/7)(r(A)-1) = {1 + 6/7*(rA-1):.4f})")
print(f"WINDOW mechanism: ({rM:.4f}, {rA:.4f}]  width {rA - rM:.4f}")
print(f"WINDOW mean-coupling: ({r_mc:.4f}, {rA:.4f}]  width {rA - r_mc:.4f}")
print(f"Selection: other regions <= {others[best]:.4f} < both lower edges: {others[best] < min(rM, r_mc)}")

# negative control: useless relays
neg = sigma_c(PAR.with_(Rc=1e6), M("full"), 6, 250, 60, 5, seed=303)
negM = sigma_c(MEDIUM.with_(Rc=1e6), M("full"), 3, 250, 60, 5, seed=304)
print(f"NEG (Rc=1e6): r(A)={neg['r']:.4f}, medium={negM['r']:.4f} -> window empty: {neg['r'] <= negM['r'] + 1e-9}")
print(f"total time {time.time()-t0:.1f}s")
