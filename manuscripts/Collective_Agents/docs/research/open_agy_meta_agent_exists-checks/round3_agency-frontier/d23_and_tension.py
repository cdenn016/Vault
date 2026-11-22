r"""Deciding run 7: restricted-support designs D2, D3; the flooding-memory tension in Rs; H_mon checks.

D2: D1 with the attention support {{mate}, {o1}} (|S| = 2).  D3: n = 4 niches of two (N = 8), kappa_msg = 3,
support {{3 mates}, {3 channels of the other niche}} (|S| = 2), m = 8 private slots, Rs = 10.
N_pr under a restricted support is computed in both readings of 'redrawn uniformly': over all N-1 others
(r_att = kappa_msg channels) and over the potential partners of the declared support (D2: mate or o1 w.p. 1/2, which
equals the habit law's attention, i.e. N_hab's attention with EFE slots).
Declared expectations (before running): D2 N_hab below 2.21 (slot-neutral rho(0.5)) because half-open slots add own
precision; D2 N_pr(all) 1.76, N_pr(potential) about 2.2 (thin margin to 2.493); D3: r(A) 8.63, b 4.754, N_hab
below 3.07, N_pr(all) 2.93; inference about 0.058, d_M about 7e-5.
Tension: rho_flood(1) (n=2, m=8) falls and the worst single-round d_cl rises as Rs falls; expect no Rs with both
rho_flood(1) < 2.493 and worst d_cl < 0.02.
H_mon: moving habit mass from c=0 to partial c (n=3: c=1; n=4: c=1, 2) at pi in {0.3, 0.7} raises N_hab contrast.
NEGATIVE CONTROL: D2 with N_pr over potential partners and EFE slots must sit within 3 SE of the slot-neutral
rho(0.5) = 2.212 when slots are removed (m = 0).
"""
import time
import itertools
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from flib import (Par, exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact, closure_numbers, steady_prior,
                  member_mats, dcl_step)
from design import make_design

t0 = time.time()
D2, _ = make_design(types=((0, 1), (1, 1)))
oh = mc(D2, "hab", K=1500, T=400, burn=80, seed=8101)
rh, sh, _, _ = r_and_se(oh, 2)
op = mc(D2, "pr", K=1500, T=400, burn=80, seed=8102, r_att=1)
rp, sp, _, _ = r_and_se(op, 2)
# N_pr over potential partners: attention mate w.p. 1/2 each round, slots by EFE -> emulate with 'pr' on a
# population whose only other channel is o1 (n_zero = 1)
op2 = mc(D2.with_(n_zero=1), "pr", K=1500, T=400, burn=80, seed=8103, r_att=1)
rp2, sp2, _, _ = r_and_se(op2, 2)
op3 = mc(D2.with_(n_zero=1, m=0), "pr", K=1500, T=400, burn=80, seed=8104, r_att=1)
rp3, sp3, _, _ = r_and_se(op3, 2)
print(f"D2 (n=2, |S|=2, m=8, Rs=10, psi {D2.psi:.4f}): N_hab {rh:.4f}+-{sh:.4f}; N_pr(all others) {rp:.4f}+-{sp:.4f}; "
      f"N_pr(potential partners) {rp2:.4f}+-{sp2:.4f}; NEG same with m=0 {rp3:.4f}+-{sp3:.4f} (expect 2.212 within 3 SE); "
      f"window (2.4932, 4.3452]  ({time.time()-t0:.0f}s)")
# D3
base = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=10.0, psi=0.0, gamma=400.0, qc=1e-4, n=4, n_zero=4, m=8,
           types=((0, 1), (3, 1)))
from d1_agency import design as mkdesign  # noqa: E402  (psi = g_max + 0.06 over c in 0..3)
D3 = mkdesign(4, ((0, 1), (3, 1)), 8)
att = ~np.eye(4, dtype=bool)
rf = r_ab(4, *compound(exact_sigma_c(D3, att, np.zeros(4, dtype=int))[0]))
b = medium_exact(D3, N=8, c=3)[2]
oh3 = mc(D3, "hab", K=800, T=400, burn=80, seed=8201)
rh3, sh3, _, _ = r_and_se(oh3, 4)
op3 = mc(D3, "pr", K=800, T=400, burn=80, seed=8202, r_att=3)
rp3, sp3, _, _ = r_and_se(op3, 4)
dcl, dM, _ = closure_numbers(D3, c=3, k=0, n=4)
of3 = mc(D3, "full", K=600, T=400, burn=80, seed=8203, want_inf=True)
rf3, sf3, _, _ = r_and_se(of3, 4)
I = of3.inf
vst = 1.0 / (I["invU"] / I["n"])
best = 0.5 * (vst * I["invU"] / I["n"] - 1 - np.log(vst) + I["lnU"] / I["n"] + I["q"] / I["n"])
print(f"D3 (n=4, |S|=2, m=8, Rs=10, psi {D3.psi:.4f}): r(A) exact {rf:.4f}, MC {rf3:.4f}+-{sf3:.4f}; medium {b:.4f}; "
      f"N_hab {rh3:.4f}+-{sh3:.4f}; N_pr(all) {rp3:.4f}+-{sp3:.4f}; d_cl {dcl:.2e}, d_M {dM:.2e}; inference {best:.4f}  "
      f"({time.time()-t0:.0f}s)")
# tension scan
for Rs in (1.0, 2.0, 3.0, 5.0):
    p, _ = make_design(Rs=Rs, types=((0, 1), (1, 1)))
    o = mc(p, "hab", K=600, T=400, burn=80, seed=8300 + int(Rs), att_law=np.array([0.0, 1.0]))
    r, s, _, _ = r_and_se(o, 2)
    Pm = steady_prior(p, 1, 0)
    M, _, _, k_rel, _ = member_mats(p, Pm, 1, 0)
    A = np.kron(np.eye(2), M)
    Qn = np.kron(np.eye(2), p.Rc * np.outer(k_rel, k_rel) + p.qc * np.eye(2))
    Sig = solve_discrete_lyapunov(A, Qn)
    worst = max(dcl_step(p, [Pm, Pm], cs, ks, Sig, 2) for cs in itertools.product((0, 1), repeat=2)
                for ks in itertools.product(range(p.m + 1), repeat=2))
    print(f"tension Rs={Rs}: rho_flood(1) {r:.4f}+-{s:.4f} (b 2.4932); worst single-round d_cl {worst:.4f}")
print(f"({time.time()-t0:.0f}s)")
# H_mon checks
for n, pi in ((3, 0.3), (3, 0.7), (4, 0.3), (4, 0.7)):
    tps = tuple((c, 1) for c in range(n))
    par = Par(Rc=0.1, qc=1e-4, n=n, n_zero=n, m=0, types=tps)
    res = []
    for c in range(n - 1):
        law = np.zeros(n); law[c] = 1 - pi; law[n - 1] = pi
        o = mc(par, "hab", K=500, T=300, burn=60, seed=8400 + 10 * n + c + int(10 * pi), att_law=law)
        r, s, _, _ = r_and_se(o, n)
        res.append(f"rest on c={c}: {r:.3f}+-{s:.3f}")
    print(f"H_mon n={n} pi={pi}: " + "; ".join(res))
print(f"total {time.time()-t0:.1f}s")
