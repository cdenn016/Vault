r"""A6 (attack): inference clause of def:agy-closure (05_agency.tex:21) for the declared coarse variable
y = (1/4) sum_i m^-_{i,0}(t), against the union-model predictive belief N(u, U) of eta_t (exact Bayes filter on eta
with all members' own sensors and open private sensors through round t-1, no relay delay, no computation noise).
Exact second moments per policy path (joint covariance of the members' errors, carried noises and the union error,
world innovation included), averaged over stationary times and 40 paths per protocol.
KL forms: best constant encoding s* = 1/E[1/U]: 1/2[E(D/U) + ln E(1/U) + E ln U]; reverse with best s:
1/2[ln(E U + E D) - E ln U]; with D = E(y - u)^2 given the path.
Declared expectations: best constant about 0.0593 (real) and 0.0594 (frozen), below alpha_I = 0.09.
NEGATIVE CONTROL: a single member's prior mean in place of the average must give a larger defect (about 0.094).
FALSIFIER of the candidate: best-constant defect > 0.09.
"""
import sys, time
import numpy as np
from mylib import Cfg, simulate, round_mats

t0 = time.time()
for proto in ("real", "frozen"):
    c = Cfg(proto=proto)
    rng = np.random.default_rng(71 if proto == "real" else 72)
    n = 4
    acc = dict(DU=[], iU=[], lU=[], U=[], D=[], DU1=[])
    for path_k in range(40):
        pth = simulate(c, 400, rng, "full")
        V0 = c.Q / (1 - c.F ** 2)
        d = 2 * n + 2 * n + 1
        iU = 2 * n + 2 * n
        # initial: eps_i(0) = -x_0 (prior means 0), e_U(0) = -eta_0
        L = np.zeros((d, 2))
        for i in range(n):
            L[2 * i:2 * i + 2] = -np.eye(2)
        L[iU, 0] = -1.0
        C = L @ (V0 * np.array([[1, c.F], [c.F, 1]])) @ L.T
        U = V0
        a_avg = np.zeros(d); a_avg[[2 * i for i in range(n)]] = 0.25; a_avg[iU] = -1.0
        a_one = np.zeros(d); a_one[0] = 1.0; a_one[iU] = -1.0
        for t in range(400):
            if t >= 80:
                D = a_avg @ C @ a_avg; D1 = a_one @ C @ a_one
                acc["DU"].append(D / U); acc["iU"].append(1 / U); acc["lU"].append(np.log(U)); acc["U"].append(U)
                acc["D"].append(D); acc["DU1"].append(D1 / U)
            T = np.zeros((d, d)); Nf = np.zeros((d, d))
            Gv = np.zeros((d, n)); Gr = np.zeros((d, n)); Gw = np.zeros(d)
            k_open = int(pth.sig[t].sum())
            Up = 1.0 / (1.0 / U + n / c.R + k_open / c.Rs)
            for i in range(n):
                Mx, kown, kslot, krs, kro, Np_, _ = round_mats(c, pth.p_prev[t, i], int(pth.sig[t, i]), pth.att[t][i],
                                                              pth.sig_prev[t])
                e = slice(2 * i, 2 * i + 2)
                T[e, e] = Mx
                for j in pth.att[t][i]:
                    T[e, 2 * n + j] = krs
                    if pth.sig_prev[t, j]:
                        T[e, 3 * n + j] = kro
                Gv[e, i] = kown; Gr[e, i] = kslot
                Gw[2 * i] = -1.0
                Nf[e, e] += Np_
                Gv[2 * n + i, i] = 1.0; Gr[3 * n + i, i] = 1.0        # carried for the next round
                Gv[iU, i] = c.F * Up / c.R
                Gr[iU, i] = c.F * Up / c.Rs * pth.sig[t, i]
            T[iU, iU] = c.F * Up / U
            Gw[iU] = -1.0
            C = T @ C @ T.T + c.R * Gv @ Gv.T + c.Rs * Gr @ Gr.T + c.Q * np.outer(Gw, Gw) + Nf
            U = c.F ** 2 * Up + c.Q
    E = {k: float(np.mean(v)) for k, v in acc.items()}
    best = 0.5 * (E["DU"] + np.log(E["iU"]) + E["lU"])
    rev = 0.5 * (np.log(E["U"] + E["D"]) - E["lU"])
    one = 0.5 * (E["DU1"] + np.log(E["iU"]) + E["lU"])
    print(f"[{proto}] 40 paths: E[D/U] {E['DU']:.5f}; best-constant KL {best:.4f}; reverse {rev:.4f}; NEG single member "
          f"{one:.4f} (must exceed {best:.4f}); alpha_I = 0.09 holds: {best <= 0.09}  ({time.time()-t0:.0f}s)", flush=True)
