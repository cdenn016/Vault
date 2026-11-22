r"""Attack run a1: recompute D1's deciding contrast numbers with independent code.

Declared expectations (from the candidate's report, to be confirmed or refuted):
  alpha 0.0134391, beta 0.0224783, r(A) 4.345220; diffusive; cross-niche block 0; spanning regions <= 1.
  mechanism medium (one component, N = 4, random single partner each round) 2.493156; mean-coupling 3.2301.
  g_max 0.00702, psi 0.06702, attention EFE gap 0.04837, slot gap 0.06094, P(mate) = 1 - 1.18e-8.
  N_lp (dead relays) r = 1 exactly.
NEGATIVE CONTROLS (must fail / must behave as stated):
  (i) Rc = 1e6: r(A) -> 1 and the window is degenerate (the collective clause must fail);
  (ii) dead relays: Sigma^c diagonal, r = 1;
  (iii) MC with independent worlds per replica must give a much larger r (estimator conditions on the world);
  (iv) MC of the full model must agree with the exact value within 3 SE.
"""
import time
import numpy as np
from mylib import Par, steady, gains, sigma_c_pattern, contrast, diffusive, all_regions, medium_exact, info_x, efe, \
    lbin, mc

t0 = time.time()
par = Par()
# ---- psi and EFE gaps
gmax = 0.0
for c in (0, 1):
    Pm = steady(par, c, 0)
    for cc in (0, 1):
        gmax = max(gmax, info_x(par, Pm, cc, 1) - info_x(par, Pm, cc, 0))
print(f"g_max {gmax:.6f}; psi declared {par.psi:.8f}; g_max + 0.06 = {gmax + 0.06:.8f}")
Pm = steady(par, 1, 0)
print(f"stationary prior P^- = {Pm.round(6).tolist()}")
att_gap = efe(par, Pm, 0, 0) - efe(par, Pm, 1, 0)
slot_gap = efe(par, Pm, 1, 1) - efe(par, Pm, 1, 0)
lb = lbin(par.m)
W = np.array([[np.log(3) + lb[k] - par.gamma * efe(par, Pm, 0, k) for k in range(par.m + 1)],
              [np.log(1) + lb[k] - par.gamma * efe(par, Pm, 1, k) for k in range(par.m + 1)]])
W -= W.max(); Pw = np.exp(W); Pw /= Pw.sum()
print(f"attention gap {att_gap:.5f}; slot gap {slot_gap:.5f}; P(mate) = 1 - {1 - Pw[1].sum():.3e}; "
      f"P(any slot open) = {1 - Pw[:, 0].sum():.3e}")
# ---- exact Sigma^c for D1 (two niches: 0<->1, 2<->3), all regions
Sc, _ = sigma_c_pattern(par, [1, 0, 3, 2], [0, 0, 0, 0])
Pi = np.linalg.inv(Sc)
al = Sc[0, 0] - Sc[0, 1]; be = Sc[0, 1]
print(f"alpha {al:.7f} beta {be:.7f}; cross-niche cov {Sc[0, 2]:.2e}; 1 + 2 beta/alpha = {1 + 2 * be / al:.6f}")
dif = diffusive(Pi)
eps = Pi.sum(1)
print(f"diffusive {dif}; coupling {-Pi[0, 1]:.4f} leak {eps[0]:.4f}")
reg = all_regions(Pi)
for C, r in sorted(reg.items(), key=lambda z: -z[1]):
    print(f"   region {C}: r = {r:.6f}")
rA = reg[(0, 1)]
# ---- mechanism medium
Sm = medium_exact(par, 4)
Pim = np.linalg.inv(Sm)
regm = all_regions(Pim)
b_mech = max(regm.values())
print(f"mechanism medium: Sigma diag {Sm[0, 0]:.7f} off {Sm[0, 1]:.7f} (max off-diag spread {np.ptp(Sm[~np.eye(4, dtype=bool)]):.1e});"
      f" sup over regions {b_mech:.6f}; whole {regm[(0, 1, 2, 3)]:.6f}; diffusive {diffusive(Pim)[0]}")
# ---- mean coupling, clause (c)
a = -Pi.copy(); np.fill_diagonal(a, 0.0)
abar = a[np.triu_indices(4, 1)].mean(); ebar = eps.mean()
Pih = np.diag(np.full(4, ebar)) + (np.diag(np.full(4, 3 * abar)) - (abar * (np.ones((4, 4)) - np.eye(4))))
b_mc = max(all_regions(Pih).values())
print(f"mean coupling: abar {abar:.5f} ebar {ebar:.5f} sup {b_mc:.6f} (formula 1+(2/3)(r-1) = {1 + 2 / 3 * (rA - 1):.6f})")
print(f"window mechanism ({b_mech:.4f}, {rA:.4f}], mean coupling ({b_mc:.4f}, {rA:.4f}]; r0 = 3.7 admissible: "
      f"{b_mech < 3.7 <= rA and b_mc < 3.7 <= rA}")
# ---- N_lp: dead relays
Sd, _ = sigma_c_pattern(par, [1, 0, 3, 2], [0, 0, 0, 0], dead=True)
print(f"NEG(ii) N_lp dead relays: off-diagonal max |cov| {np.max(np.abs(Sd - np.diag(np.diag(Sd)))):.2e}; "
      f"r(A) = {contrast(np.linalg.inv(Sd), (0, 1)):.6f}")
# ---- control (i)
p6 = par.w(Rc=1e6)
Sx, _ = sigma_c_pattern(p6, [1, 0, 3, 2], [0, 0, 0, 0])
print(f"NEG(i) Rc=1e6: r(A) {contrast(np.linalg.inv(Sx), (0, 1)):.6f}, medium "
      f"{max(all_regions(np.linalg.inv(medium_exact(p6, 4))).values()):.6f}")
print(f"  ({time.time() - t0:.1f}s)")
# ---- MC checks
o = mc(par, "full", B=3000, T=500, burn=100, seed=11)
print(f"NEG(iv) MC full model: r {o['r']:.4f} +- {o['se']:.4f} (z vs exact {(o['r'] - rA) / o['se']:+.2f}); "
      f"open {o['open_rate']:.2e}; c rate {o['c_rate']:.6f}  ({time.time() - t0:.1f}s)")
o = mc(par, "full", B=1500, T=300, burn=100, seed=12, indep_world=True)
print(f"NEG(iii) MC independent worlds: r {o['r']:.2f} (must be far above {rA:.2f})  ({time.time() - t0:.1f}s)")
o = mc(par, "full", B=1500, T=300, burn=100, seed=13, dead=True)
print(f"NEG(ii') MC dead relays: r {o['r']:.4f} +- {o['se']:.4f}  ({time.time() - t0:.1f}s)")
