r"""Repair of the prediction-noise remark of Proposition S: closed form for V_12.

With prediction noise eps_i ~ N(0, se2) i.i.d. added to m_i(t+1), and lambda = e^{-i w},
h_k = 1/(1 - rho_k lambda), rho_k = c0_k phi_k, sX_k = (K_s+(n_k-1)K_c)^2 R + (n_k-1) K_c^2 Rc,
  V_12 = -kappa1 kappa2 (1/2pi) int |h1 h2|^2 Re[(c0_1 se2 + phi1 sX_1 lambda)(c0_2 se2 + phi2 sX_2 conj(lambda))] / S_o dw,
  S_o = kappa1^2 |h1|^2 (c0_1^2 se2 + sX_1) + kappa2^2 |h2|^2 (c0_2^2 se2 + sX_2) + Q_w,
and Pi^c_ij = -V_12/(det V sqrt(n1 n2)).  At se2 = 0 this is Proposition S.
Declared expectation: the formula matches the direct conditioning value of V_12 to <= 1e-8 relative
on random draws with se2 > 0; negative control: dropping the cross term (the 'only diag(V)' claim,
i.e. V_12 evaluated at se2 = 0) mismatches.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
exec(open("c3b_sign.py").read().split("# S1, S2, N1")[0])
worst = 0.0; worst_nc = np.inf; used = 0
while used < 100:
    p = draw()
    se2 = 10 ** rng.uniform(-2, 1)
    o = cross_and_V(p, se2)
    o0 = cross_and_V(p, 0.0)
    if o is None or o0 is None:
        continue
    used += 1
    n = np.array(p["n"]); phi, kap = rule(p)
    c0 = 1 - p["Ks"] - (n - 1) * p["Kc"]
    sX = (p["Ks"] + (n - 1) * p["Kc"]) ** 2 * p["R"] + (n - 1) * p["Kc"] ** 2 * p["Rc"]
    rho = c0 * phi
    w = 2 * np.pi * np.arange(8192) / 8192
    lam = np.exp(-1j * w)
    h = [1 / (1 - rho[k] * lam) for k in range(2)]
    So = sum(kap[k] ** 2 * np.abs(h[k]) ** 2 * (c0[k] ** 2 * se2 + sX[k]) for k in range(2)) + p["Qw"]
    num = np.abs(h[0] * h[1]) ** 2 * np.real((c0[0] * se2 + phi[0] * sX[0] * lam) * (c0[1] * se2 + phi[1] * sX[1] * np.conj(lam)))
    V12 = -kap[0] * kap[1] * np.mean(num / So)
    V12_direct = o[1][0, 1]
    worst = max(worst, abs(V12 - V12_direct) / max(abs(V12_direct), 1e-300))
    worst_nc = min(worst_nc, abs(o0[1][0, 1] - V12_direct) / abs(V12_direct))
print(f"formula vs direct V_12 with prediction noise: max rel error {worst:.2e} over {used} draws")
print(f"negative control ('only diag(V) changes'): min rel discrepancy {worst_nc:.2e} (expected >> 1e-8)")
