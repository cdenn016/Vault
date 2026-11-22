"""A1: exact recomputation of P0's deciding numbers from the specification.

Declared expectations (before running), from the candidate's report:
  sigma=6.07184e-3, c=6.5888e-4, Var e_i=7.5547e-3, beta=4.03044e-3, alpha=3.52426e-3
  Pi^c diffusive; a_AA=58.024, a_SA=5.605; leaks 46.048 (A), 144.707 (S)
  r(A)=5.384864, r(A+S)=2.325959 (best other region)
  mean-coupling baseline 3.8167; M-perm 3.9301
  mate-reading probability ~2.1e-14 per member-round (summed over mates?)
If my numbers differ by more than 1e-4 relative, the candidate's numbers are wrong
or my reading of the specification differs; either is reported.
Negative controls that must FAIL the collective clause:
  NC1: Rc*100 -> r(A) small (candidate: 1.075)
  NC2: v_S conditioned on (R0 reversed) -> Sigma^c of members diagonal, r(A)=1
Unit tests that must PASS: C1 test value r=3 at alpha=1,beta=.5,n=4; diffusive test.
"""
import os
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from alib import (P0Model, contrast, all_regions, diffusive_parts,
                  mean_coupling_baseline, perm_average)

np.set_printoptions(precision=6, suppress=False, linewidth=140)

# ---------- unit tests ----------
S = 1.0 * np.eye(4) + 0.5 * np.ones((4, 4))
print("unit C1: r =", contrast(np.linalg.inv(S), [0, 1, 2, 3]), "(expect 3)")
a, eps, mo, mr = diffusive_parts(np.array([[2., -1.], [-1., 2.]]))
print("unit diffusive: a12 =", a[0, 1], "eps =", eps, "(expect 1, [1,1])")
Sneg = 1.0 * np.eye(4) - 0.1 * np.ones((4, 4))
_, _, mo, mr = diffusive_parts(np.linalg.inv(Sneg))
print("unit neg control beta=-0.1: max offdiag =", mo, "(expect >0, non-diffusive)")

# ---------- P0 ----------
m = P0Model()
print("\nP0 filters")
print("  S   P^- =", m.PmS.ravel(), " K_S =", m.KS.ravel())
print("  mem P^- =", m.Pm.ravel(), " P^+ =", m.Pp.ravel())
print("  mem K (cols own, channel) =", m.Km.ravel())
p, G = m.policy_probs()
print("  EFE:", {k: round(v, 6) for k, v in G.items()})
print("  policy probs:", {k: f"{v:.3e}" for k, v in p.items()})
print("  P(read a mate) per member-round = %.3e ; P(none) = %.3e" % (sum(p[f'm{j}'] for j in range(1, 4)), p['none']))

Sc = m.sigma_c()
sig, c, vi, beta = Sc[0, 0], Sc[0, 1], Sc[1, 1], Sc[1, 2]
print("\nSigma^c entries: sigma=%.6e c=%.6e Var e_i=%.6e beta=%.6e alpha=%.6e" % (sig, c, vi, beta, vi - beta))
print("  exchangeable check (spread of member var, cov):", np.ptp(np.diag(Sc)[1:]), np.ptp(Sc[1:, 1:][np.triu_indices(4, 1)]))
Pi = np.linalg.inv(Sc)
a, eps, mo, mr = diffusive_parts(Pi)
print("Pi^c: max offdiag = %.4e, min row sum = %.4f" % (mo, mr))
print("  a_AA = %.4f, a_SA = %.4f, leak A = %.4f, leak S = %.4f, cut(A) = %.4f" %
      (a[1, 2], a[0, 1], eps[1], eps[0], a[0, 1:].sum()))
regs = all_regions(5)
rs = {tuple(C): contrast(Pi, C) for C in regs}
rA = rs[(1, 2, 3, 4)]
others = sorted(((v, k) for k, v in rs.items() if k != (1, 2, 3, 4)), reverse=True)
print("r(A) = %.6f ; best other: %s r=%.6f ; best containing S: r=%.6f" %
      (rA, others[0][1], others[0][0], max(v for k, v in rs.items() if 0 in k)))
# closed form Prop A
n = 4
al = vi - beta
bp = beta - c * c / sig
print("Prop A closed form r(A) = 1 - c/sig + n beta'/alpha = %.6f" % (1 - c / sig + n * bp / al))
mc = mean_coupling_baseline(Pi)
Sperm = perm_average(Sc)
mp = max(contrast(np.linalg.inv(Sperm), C) for C in regs)
print("baseline mean coupling = %.6f ; M-perm (Sigma averaged over relabelings) = %.6f" % (mc, mp))
print("leak heterogeneity on A: %.6f" % (eps[1:].max() / eps[1:].mean()))

# ---------- negative controls ----------
m2 = P0Model(Rc=0.2)
Pi2 = np.linalg.inv(m2.sigma_c())
_, _, mo2, mr2 = diffusive_parts(Pi2)
print("\nNC1 Rc*100: max offdiag %.3e min rowsum %.3f r(A) = %.4f baseline %.4f" %
      (mo2, mr2, contrast(Pi2, [1, 2, 3, 4]), mean_coupling_baseline(Pi2)))
# NC2: condition on v_S path: remove v_S from noise inputs (set its variance to 0 in the members' channel and in S)
# Conditioning on v_S removes it from every agent's conditional covariance.
m3 = P0Model()
T, W = m3.system(False)
# rebuild W without v_S: recompute by zeroing RS contribution in noise but keeping filters' gains
from scipy.linalg import solve_discrete_lyapunov
RS_saved = m3.RS
m3.RS = 0.0  # only affects noise variance in system(); filter gains were computed in __init__
T3, W3 = m3.system(False)
m3.RS = RS_saved
Z3 = solve_discrete_lyapunov(T3, W3)
idx = [0, 2, 4, 6, 8]
Sc3 = Z3[np.ix_(idx, idx)]
print("NC2 v_S conditioned: offdiag max |Sigma| = %.3e ; r(A) = %.6f" %
      (np.abs(Sc3[~np.eye(5, dtype=bool)]).max(), contrast(np.linalg.inv(Sc3), [1, 2, 3, 4])))
