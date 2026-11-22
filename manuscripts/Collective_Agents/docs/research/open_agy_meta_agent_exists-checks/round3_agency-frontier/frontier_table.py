r"""Deciding run 9: frontier table Agency0_max against the levers (Rc = 0.1, noise as I*).

For each (n, K): r_full (exact), b(kappa_msg = n-1), b(kappa_msg = n) (window check), rho(pi) on a grid
(slot-neutral MC), pi* = rho^{-1}(b), and p_full* = the least attention concentration with r(A) > b (in the
slot-neutral class p_full* = pi*, because the full model's slots are closed and N_hab's are absent).
Index formulas (C12 identity with zero slot misfit, verified to 4 digits in d1_agency):
  deterministic attention, uniform habits on |S| sets:   A(m) = m ln2 / (m ln2 + ln|S|),  |S| >= ceil(1/pi*)
  deterministic attention, best non-uniform habits:      A(m) = m ln2 / (m ln2 + ln(1/pi*))      (Theorem A bound)
  soft attention P(x*) = p, uniform |S|:                 A(m) = m ln2 / (m ln2 + d(p || 1/|S|)),  r(A) = rho(p) > b
Minimal m for Agency0 in {0.5, 0.8, 0.9}.
Declared expectations: window open for kappa_msg = n-1 at every (n, K); closed for kappa_msg = n at n = 2;
ceil(1/pi*) = 2 except n = 2, K = 4 (pi* < 1/2 -> 3).
NEGATIVE CONTROL: the formula at the canonical n=4 support and m=1 must give 1/7 (d1_agency NEG (a)).
"""
import time
from math import ceil, log
import numpy as np
from flib import Par, exact_sigma_c, compound, r_ab, mc, r_and_se, medium_exact

t0 = time.time()


def dkl(p, q):
    p = min(max(p, 1e-15), 1 - 1e-15)
    return p * log(p / q) + (1 - p) * log((1 - p) / (1 - q))


def mmin(a0, kla):
    return int(np.ceil(a0 / (1 - a0) * kla / log(2) - 1e-12))


pis = np.array([0.0, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
print("n K | r_full  b(k=n-1)  b(k=n) | pi*   ceil(1/pi*) ln(1/pi*) | min m for Agency0 0.5/0.8/0.9: "
      "uniform |S|=ceil(1/pi*) ; Theorem-A bound ; canonical |S_k|")
for n in (2, 3, 4):
    par = Par(Rc=0.1, qc=1e-4, n=n, n_zero=n, m=0, types=((0, 1), (n - 1, 1)))
    att = ~np.eye(n, dtype=bool)
    rf = r_ab(n, *compound(exact_sigma_c(par, att, np.zeros(n, dtype=int))[0]))
    rho = [1.0]
    for pi in pis[1:-1]:
        o = mc(par, "hab", K=600, T=300, burn=60, seed=int(12000 + 100 * n + 100 * pi), att_law=np.array([1 - pi, pi]))
        rho.append(r_and_se(o, n)[0])
    rho.append(rf)
    rho = np.array(rho)
    for K in (2, 3, 4):
        N = K * n
        b = medium_exact(par, N=N, c=n - 1)[2]
        bk = medium_exact(par, N=N, c=n)[2] if n < N - 1 else float("nan")
        j = int(np.searchsorted(rho, b))
        ps = pis[j - 1] + (pis[j] - pis[j - 1]) * (b - rho[j - 1]) / (rho[j] - rho[j - 1])
        S_u = ceil(1 / ps - 1e-12)
        # canonical support size for kappa_msg = n-1 among N-1 channels
        from math import comb
        S_c = sum(comb(N - 1, c) for c in range(n))
        row = []
        for kla in (log(S_u), log(1 / ps), log(S_c)):
            row.append("/".join(str(mmin(a, kla)) for a in (0.5, 0.8, 0.9)))
        print(f"{n} {K} | {rf:.3f}  {b:.3f}  {bk:.3f}{' (closed)' if bk >= rf else ''} | {ps:.3f} {S_u} {log(1/ps):.3f} | "
              f"{row[0]} ; {row[1]} ; {row[2]} (|S_k|={S_c})")
    if n == 2:
        print("  soft attention, n=2, K=2, |S|=2 (b = 2.493, mean-coupling baseline 1+(2/3)(r-1)):")
        for p in (0.6, 0.7, 0.8, 0.9, 1.0):
            r = float(np.interp(p, pis, rho))
            kla = dkl(p, 0.5)
            print(f"    P(x*)={p}: r(A)~{r:.3f} (margin over b {r-2.493:+.3f}; mean-coupling baseline "
                  f"{1+(2/3)*(r-1):.3f}); KL_a/member {kla:.4f}; Agency(m=1) {log(2)/(log(2)+kla):.4f}, "
                  f"(m=8) {8*log(2)/(8*log(2)+kla):.4f}")
    print(f"  ({time.time()-t0:.0f}s)")
print(f"NEG canonical n=4 support, m=1: {log(2)/(log(2)+log(64)):.4f} (must be 1/7 = 0.1429)")
