r"""Attack A9: recompute the inference tolerance alpha_I of PN's closure clause (claimed 5.61e-3 forward, 5.41e-3
reverse) from coefficient rows: expected KL between the declared coarse belief N(mbar_t, P^-_member) and the
union-model predictive law N(m_union_t, P^-_union), the union model being the centralized known-input filter on all
four members' world sensing (prop:agy-pooling / def:agy-closure (ii)).

Declared expectation: E(mbar - m_union)^2 = 1.187e-3 and the two KLs match 5.6079e-3 / 5.4050e-3 to 1e-6.
NEG control: replacing P^-_member by P^-_union in the belief must lower the forward KL (only the mean term remains).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from win import build, kalman_ss

F, Q, R, Rc, b, g, n, T, TS = 0.9, 0.05, 1.0, 0.2, 0.2, 0.05, 4, 70, 40

if __name__ == "__main__":
    mod = build(F, Q, R, Rc, b, g, T, mode="base")
    NT = mod["NT"]
    Pm_c, Pp_c = kalman_ss(F, Q, n / R)
    Kc_ = Pp_c / R
    Pm_m = mod["gains"][3]
    eta = mod["eta"]
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    per = 1 + n + len(pairs)
    mc = np.zeros(NT)
    d2 = None
    for t in range(T):
        if t == TS:
            mbar = (mod["E"][t] + eta[t][None, :]).mean(axis=0)
            d2 = float((mbar - mc) @ (mbar - mc))
        base = 1 + per * t
        ssum = n * eta[t].copy()
        for k in range(n):
            ssum[base + 1 + k] += np.sqrt(R)
        mcp = mc + Kc_ * (ssum - n * mc)
        mc = F * mcp + b * mod["U"][t]
    kl_f = 0.5 * (Pm_m / Pm_c - 1 + np.log(Pm_c / Pm_m) + d2 / Pm_c)
    kl_r = 0.5 * (Pm_c / Pm_m - 1 + np.log(Pm_m / Pm_c) + d2 / Pm_m)
    kl_neg = 0.5 * (d2 / Pm_c)
    print("P^-_member=%.6f P^-_union=%.6f E(mbar-m_union)^2=%.4e  alpha_I forward=%.6e reverse=%.6e  NEG (equal covariances)=%.4e" % (
        Pm_m, Pm_c, d2, kl_f, kl_r, kl_neg))
