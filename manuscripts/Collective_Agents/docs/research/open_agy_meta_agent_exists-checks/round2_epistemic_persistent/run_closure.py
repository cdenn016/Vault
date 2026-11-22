r"""Deciding script 3: closure (def:agy-closure, 05_agency.tex:13-24) of C = A at I*.

Declared coarse variable: y(t) = (1/n) sum_{i in A} m^-_i(t) in R^2, the average of the members' prior-mean vectors
(its first coordinate is the collective average of the contrast coordinates plus eta_t).
Internal variables x = (m^-_i)_{i in A} in R^8; given the blanket path (own-sensor and slot channels, the members'
broadcast channels) and the policy path, x_{t+1} = A(t) x_t + B(t) x_B(t) + n_t with
A(t) = blockdiag_i A_F (I - K_i(t) H_i(t)) and internal noise n_t = (A_F k_rel sum_j nu_ij + xi_i)_i (relay read noise
of the internal channels and computation noise), Q^n(t) > 0 because qc > 0.
Memory: closure defect d_cl(t) = 1/2 ln det(I + (P Q^n P^T)^{-1} P A Sigma_{x|y} A^T P^T) (eq:agy-closure-defect)
along sampled policy paths; d_M(t) <= d_cl(t) pathwise because y_{t+1} is independent of y_{0:t-1} given x_t.
Inference: union model = centralized filter on all members' exterior-facing sensations (own sensors, every
member's reading of every open slot); E KL( N(ybar, P_enc) || N(m*, P*) ) on eta_t, strict reading (P_enc a
constant, best constant 1/E[1/P*]) and blanket-path reading (P_enc = the members' claimed prior variance).
Declared expectations: d_cl = 0 (to rounding) at every step of a path on which all members have read the same
number of informative relays since the start; positive but below 1e-3 nats after a forced one-round deviation of one
member; inference KL below 0.05 nats in both readings.  NEGATIVE CONTROL: a member that permanently reads only 2
mates (asymmetric gains every round) must give d_cl bounded away from 0 at every step.
"""
import time
import numpy as np
from lib import Pminus, posterior, A_F, simulate_policy_path, Path
from instance import PAR, T, BURN, sim, PROTO

n = PAR.n
Af = A_F(PAR.F)
Pavg = np.kron(np.ones((1, n)) / n, np.eye(2))   # 2 x 2n


def member_mats(Pm, nrel, nvis, par=PAR):
    Afp = A_F(par.F)
    Pp = posterior(Pm, 1 / par.R + nvis / (par.Rs + par.Rsh), nrel / (par.R + par.Rc))
    Ai = Afp @ (Pp @ np.linalg.inv(Pm))
    krel = Pp[:, 1] / (par.R + par.Rc)
    Qn = Afp @ (nrel * par.Rc * np.outer(krel, krel)) @ Afp.T + par.qc * np.eye(2)
    return Ai, Qn, Pp


def closure_defects(path: Path):
    Tn = path.Pm.shape[0]
    Sig = np.zeros((2 * n, 2 * n))
    out = np.zeros(Tn)
    for t in range(Tn):
        A = np.zeros((2 * n, 2 * n)); Qn = np.zeros((2 * n, 2 * n))
        for i in range(n):
            Ai, Qi, _ = member_mats(path.Pm[t, i], len(path.mates[t][i]), int(path.vis[t, i]))
            A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Ai
            Qn[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Qi
        if t >= 30:
            PS = Pavg @ Sig
            Sxy = Sig - PS.T @ np.linalg.solve(PS @ Pavg.T, PS)
            M = Pavg @ A @ Sxy @ A.T @ Pavg.T
            QP = Pavg @ Qn @ Pavg.T
            out[t] = 0.5 * np.log(np.linalg.det(np.eye(2) + np.linalg.solve(QP, M)))
        Sig = A @ Sig @ A.T + Qn
    return out


def forced_path(dev_round: int, dev_member: int, m_dev: int, Tn: int, slot_profile_seed: int = 0, permanent=False):
    r"""Policy path with the slot law of I* at symmetric states, all members reading all 3 mates except one member
    reading m_dev mates at dev_round (or at every round from dev_round on if permanent)."""
    rng = np.random.default_rng(slot_profile_seed)
    base = sim(PAR, Tn, rng)
    mates = []
    for t in range(Tn):
        row = []
        for i in range(n):
            full = tuple(j for j in range(n) if j != i)
            if i == dev_member and (t == dev_round or (permanent and t >= dev_round)):
                row.append(full[:m_dev])
            else:
                row.append(full)
        mates.append(row)
    # recompute the claimed covariances along the modified attention path with the same slot path
    p = np.full(n, 0.09)
    Pm = np.zeros((Tn, n, 2, 2))
    for t in range(Tn):
        for i in range(n):
            Pm[t, i] = Pminus(PAR, p[i])
            p[i] = posterior(Pm[t, i], 1 / PAR.R + base.vis[t, i] / (PAR.Rs + PAR.Rsh),
                             len(mates[t][i]) / (PAR.R + PAR.Rc))[0, 0]
    return Path(Pm, mates, base.slots, base.vis, 0)


def union_kl(path: Path, t_eval, PAR=PAR):
    r"""Joint second moments of (x, E, V, e*) along a policy path; returns per eval time
    (E[(ybar - m*)^2 | pi], P*_t, members' mean claimed prior variance)."""
    d = 2 + 2 * n + n + 1
    ix, iE, iV, ie = 0, 2, 2 + 2 * n, 2 + 3 * n
    V0 = PAR.Q / (1 - PAR.F ** 2)
    Cx0 = V0 * np.array([[1.0, PAR.F], [PAR.F, 1.0]])
    L = np.zeros((d, 2)); L[0:2] = np.eye(2)
    for i in range(n):
        L[iE + 2 * i: iE + 2 * i + 2] = -np.eye(2)
    L[ie, 0] = -1.0
    C = L @ Cx0 @ L.T
    C[iV:iV + n, iV:iV + n] += PAR.R * np.eye(n)
    Pstar = V0
    res = []
    for t in range(path.Pm.shape[0]):
        if t in t_eval:
            c = np.zeros(d)
            for i in range(n):
                c[iE + 2 * i] = 1.0 / n
            c[ie] = -1.0
            res.append((c @ C @ c, Pstar, float(np.mean(path.Pm[t, :, 0, 0]))))
        nopen = int(path.slots[t].sum())
        # fresh noise: w, v_i, rho_i^agg, nu_i^agg, xi_i (2)
        ne = 1 + 3 * n + 2 * n
        B = np.zeros((d, ne)); var = np.zeros(ne)
        A = np.zeros((d, d))
        Af = A_F(PAR.F)
        A[0:2, 0:2] = Af
        B[0, 0] = 1.0; var[0] = PAR.Q
        Pps = 1.0 / (1.0 / Pstar + n / PAR.R + n * nopen / PAR.Rs)
        A[ie, ie] = PAR.F * Pps / Pstar
        B[ie, 0] = -1.0
        for i in range(n):
            nrel = len(path.mates[t][i])
            Ai, _, Pp = member_mats(path.Pm[t, i], nrel, int(path.vis[t, i]), PAR)
            A[iE + 2 * i: iE + 2 * i + 2, iE + 2 * i: iE + 2 * i + 2] = Ai
            krel = Pp[:, 1] / (PAR.R + PAR.Rc)
            for j in path.mates[t][i]:
                A[iE + 2 * i: iE + 2 * i + 2, iV + j] = Af @ krel
            B[iE + 2 * i, 0] = -1.0
            cv, cr, cn, cx = 1 + i, 1 + n + i, 1 + 2 * n + i, 1 + 3 * n + 2 * i
            B[iE + 2 * i: iE + 2 * i + 2, cv] = Af @ (Pp[:, 0] / PAR.R)
            B[iV + i, cv] = 1.0
            B[ie, cv] = PAR.F * Pps / PAR.R
            var[cv] = PAR.R
            B[iE + 2 * i: iE + 2 * i + 2, cr] = Af @ (Pp[:, 0] / PAR.Rs)
            B[ie, cr] = PAR.F * Pps / PAR.Rs
            var[cr] = nopen * PAR.Rs
            B[iE + 2 * i: iE + 2 * i + 2, cn] = Af @ krel
            var[cn] = nrel * PAR.Rc
            B[iE + 2 * i: iE + 2 * i + 2, cx: cx + 2] = np.eye(2)
            var[cx: cx + 2] = PAR.qc
        C = A @ C @ A.T + B @ np.diag(var) @ B.T
        Pstar = PAR.F ** 2 * Pps + PAR.Q
    return res


if __name__ == "__main__":
    t0 = time.time()
    rng = np.random.default_rng(7001)
    dcl_all, ndev_paths, sym_paths_max = [], 0, 0.0
    for k in range(40):
        pth = sim(PAR, T, rng)
        dc = closure_defects(pth)[BURN:]
        dcl_all.append(dc)
        if pth.att_dev > 0:
            ndev_paths += 1
        else:
            sym_paths_max = max(sym_paths_max, dc.max())
    dcl_all = np.concatenate(dcl_all)
    print(f"[memory] 40 sampled paths x {T - BURN} steps: paths with an attention deviation {ndev_paths}; "
          f"max d_cl on deviation-free paths {sym_paths_max:.2e}; mean d_cl {dcl_all.mean():.2e}; "
          f"max {dcl_all.max():.2e}; fraction of steps with d_cl > 1e-10: {(dcl_all > 1e-10).mean():.4f}")
    for m_dev in (2, 1, 0):
        fp = forced_path(150, 0, m_dev, 260, slot_profile_seed=11)
        dc = closure_defects(fp)
        print(f"[memory] forced one-round deviation of member 0 to {m_dev} mates at round 150: max d_cl {dc.max():.3e} "
              f"at round {dc.argmax()}, sum over rounds {dc[140:].sum():.3e}, d_cl before the deviation {dc[100:150].max():.1e}")
    fpn = forced_path(60, 0, 2, 200, slot_profile_seed=12, permanent=True)
    dcn = closure_defects(fpn)
    print(f"[memory] NEG permanent deviation (member 0 reads 2 mates from round 60): min d_cl over rounds 100..199 "
          f"{dcn[100:].min():.3e}, mean {dcn[100:].mean():.3e}")
    print(f"  t={time.time()-t0:.0f}s", flush=True)

    # inference part
    rng = np.random.default_rng(7002)
    t_eval = set(range(BURN, T, 4))
    D2, Ps, Pc = [], [], []
    for k in range(40):
        pth = sim(PAR, T, rng)
        for d2, pstar, pcl in union_kl(pth, t_eval):
            D2.append(d2); Ps.append(pstar); Pc.append(pcl)
    D2, Ps, Pc = map(np.array, (D2, Ps, Pc))
    Penc = 1.0 / np.mean(1.0 / Ps)
    kl_strict = 0.5 * np.mean(Penc / Ps - 1 - np.log(Penc / Ps) + D2 / Ps)
    kl_blank = 0.5 * np.mean(Pc / Ps - 1 - np.log(Pc / Ps) + D2 / Ps)
    irreducible = 0.5 * np.mean(D2 / Ps)
    print(f"[inference] E(ybar - m*)^2 = {D2.mean():.5f}; union prior variance P* mean {Ps.mean():.5f} "
          f"(range {Ps.min():.5f}..{Ps.max():.5f}); members' claimed prior variance mean {Pc.mean():.5f}")
    print(f"[inference] strict reading (P_enc constant, best = {Penc:.5f}): E KL = {kl_strict:.5f} nats; "
          f"blanket-path reading (P_enc = claimed variance): E KL = {kl_blank:.5f}; mean-term part {irreducible:.5f}")
    print(f"total {time.time()-t0:.1f}s")
