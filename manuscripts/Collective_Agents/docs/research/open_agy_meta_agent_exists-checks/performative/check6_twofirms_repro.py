r"""Check 6: reconstruction of ex:met-two-firms (s10a_meta_agents.tex:108-118), bounded model for both
firms, to test that the windowed world-conditional computation reproduces the coordinator's numbers
(chk:met-two-firms, chk10a_meta_agents.tex:57): at n_c = 1 (bounded model) the precision of the eight
members' price coordinates given the price path has largest off-diagonal entry 166.3 and smallest
row sum -0.82 (non-diffusive).  Also n_c = 0 and 4 with the bounded model (not reported there; the
reported exact-model values 0.0515/3.55 and 0.0895/-11.0 concern C1's exact model, not built here).

Declared expectation: n_c = 1 bounded: max offdiag ~ 166.3, min row sum ~ -0.82 (to ~1%), non-diffusive.
Negative control: removing the acts' effect on the price (b_p = 0 in the world only) removes the
C1-C2 entries (they vanish) while the within-firm singular-consensus entries persist.

State (dim 33): p | X_1..8 (sensory channels) | u_1..8 (act channels) | ya_1..8 (stored coarse act)
| eta_1..8 (filter states).  Round map (t -> t+1):
  p'   = f p + b (sum_{C1} u + sum_{C2} u) + w,          Var w = 0.05
  X_i' = p + v_i,                                        Var v_i = R_i
  u_i' = -g_u eta_i + nu_i,                              Var nu_i = 0.01
  ya_i' = sum_{j in C(i)} u_j + c_i,                     Var c_i = 1e-3
  eta_i' = Fb[eta_i + Pb_k (n htilde_i' - Ls_k eta_i)] + Bb sum_{j in C(i)} u_j + c'_i,  Var c'_i = 1e-3
  with htilde' = W^{n_c} h', h_j' = X_j'/R_j = (p + v_j)/R_j.
"""
import numpy as np
from pc import world_conditional_cov, diffusivity, riccati_scalar


def build_twofirms(nc, bp_world=0.2):
    f, bp, Qw, gu = 0.9, 0.2, 0.05, 0.15
    R = np.array([0.5, 1, 2, 4, 1, 1, 2, 2], float)
    firm = [0] * 4 + [1] * 4
    Ls = [sum(1 / R[:4]), sum(1 / R[4:])]
    Pb = []
    for k in range(2):
        Pm, Pp = riccati_scalar(f, 0.1, Ls[k])
        Pb.append(Pp)
    S = np.roll(np.eye(4), 1, axis=1)
    Wr = 0.5 * np.eye(4) + 0.25 * (S + S.T)
    Wn = np.linalg.matrix_power(Wr, nc)
    W = np.zeros((8, 8)); W[:4, :4] = Wn; W[4:, 4:] = Wn
    n = 4
    ip = 0; iX = list(range(1, 9)); iu = list(range(9, 17)); iy = list(range(17, 25)); ie = list(range(25, 33))
    d = 33
    # noises: w, v(8), nu(8), c(8), c'(8)
    nx = 1 + 8 + 8 + 8 + 8
    A = np.zeros((d, d)); G = np.zeros((d, nx))
    A[ip, ip] = f
    for j in range(8):
        A[ip, iu[j]] = bp_world
    G[ip, 0] = np.sqrt(Qw)
    for i in range(8):
        A[iX[i], ip] = 1.0; G[iX[i], 1 + i] = np.sqrt(R[i])
        A[iu[i], ie[i]] = -gu; G[iu[i], 9 + i] = np.sqrt(0.01)
        for j in range(8):
            if firm[j] == firm[i]:
                A[iy[i], iu[j]] = 1.0
        G[iy[i], 17 + i] = np.sqrt(1e-3)
        k = firm[i]
        coef = f * Pb[k] * n * W[i] / R  # length 8
        A[ie[i], ie[i]] = f * (1 - Pb[k] * Ls[k])
        if LATENCY == "eq-met-firms":
            # eq:met-firms: eta' = f Pb s_C + f(1 - Ls Pb) eta + b ya, reading the CURRENT channel states
            for j in range(8):
                A[ie[i], iX[j]] += coef[j]
            A[ie[i], iy[i]] += bp
        else:
            # first reconstruction: reads the channel contents written in the same round
            A[ie[i], ip] += coef.sum()
            for j in range(8):
                G[ie[i], 1 + j] += coef[j] * np.sqrt(R[j])
                if firm[j] == firm[i]:
                    A[ie[i], iu[j]] += bp
        G[ie[i], 25 + i] = np.sqrt(1e-3)
    return A, G @ G.T, [ip], ie


LATENCY = "eq-met-firms"


if __name__ == "__main__":
    for nc in [0, 1, 4]:
        A, Qx, iw, ia = build_twofirms(nc)
        rho = max(abs(np.linalg.eigvals(A)))
        res = {}
        for L in (20, 30, 60):
            res[L] = world_conditional_cov(A, Qx, iw, ia, L)
        Pi = np.linalg.inv(res[60])
        conv = np.max(np.abs(np.linalg.inv(res[30]) - Pi)) / np.max(np.abs(Pi))
        dif = diffusivity(Pi)
        cross = Pi[:4, 4:]
        print("n_c=%d (bounded, both firms) rho(A)=%.3f  max offdiag=%.4g  min rowsum=%.4g  cross in [%.4f, %.4f]  diffusive=%s  conv(L30 vs 60)=%.1e" % (
            nc, rho, dif["max_offdiag"], dif["min_rowsum"], cross.min(), cross.max(), dif["diffusive"], conv))
    A, Qx, iw, ia = build_twofirms(1, bp_world=0.0)
    Pi = np.linalg.inv(world_conditional_cov(A, Qx, iw, ia, 60))
    print("NEG n_c=1, acts without effect on price: max|cross|=%.2e  max offdiag=%.4g" % (np.abs(Pi[:4, 4:]).max(), diffusivity(Pi)["max_offdiag"]))
