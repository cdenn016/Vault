r"""Exact Markov defect of the coarse variable y = (1/4) sum_i m^-_{i,0} along a given policy path (attack code).

Given the blanket and policy paths, x_{t+1} = A_t x_t + (input) + n_t, x = (m^-_i)_{i in A} in R^8, A_t block diagonal,
Q^n_t block diagonal (relay-channel noise and computation noise).  For the Gaussian law of y given the input path:
   I_t = I(y_{t+1}; y_{0:t-1} | y_t) = 1/2 ln[ Var(y_{t+1} | y_t) / Var(y_{t+1} | y_{0:t}) ],
   Var(y_{t+1} | y_t) = P S_{t+1} P^T - (P A_t S_t P^T)^2 / (P S_t P^T),   S_t = Cov(x_t | inputs),
   Var(y_{t+1} | y_{0:t}) = P (A_t Sh_t A_t^T + Q_t) P^T,   Sh_t = Cov(x_t | y_{0:t}, inputs) (Kalman filter, noiseless y).
d_M (def:agy-closure (i), input-conditional form, 05_agency.tex:20) is sup_t I_t; d_cl(t) = 1/2 ln[Var(y_{t+1}|y_t)/(P Q_t P^T)]
is the candidate's upper bound (data processing).
A member's round configuration is (own sigma_i(t), n_s attended mates, n_o of them with sigma_j(t-1) = 1).
"""
import numpy as np
from mylib import Cfg, prior_cov, AF

P = np.zeros((1, 8)); P[0, 0::2] = 0.25


def member(c: Cfg, p_prev: float, own: int, ns: int, no: int):
    Af = AF(c.F)
    Pm = prior_cov(c, p_prev)
    Pp = np.linalg.inv(np.linalg.inv(Pm) + np.diag([1.0 / c.R + own / c.Rs, ns / (c.R + c.Rc) + no / (c.Rs + c.Rc)]))
    Mx = Af @ Pp @ np.linalg.inv(Pm)
    krs = Af @ Pp[:, 1] / (c.R + c.Rc); kro = Af @ Pp[:, 1] / (c.Rs + c.Rc)
    Qn = c.qc * np.eye(2) + c.Rc * (ns * np.outer(krs, krs) + no * np.outer(kro, kro))
    return Mx, Qn, Pp[0, 0]


def step_mats(c, p, cfgs):
    A = np.zeros((8, 8)); Qn = np.zeros((8, 8)); pn = np.empty(4)
    for i, (o, ns, no) in enumerate(cfgs):
        Mx, Qi, pp = member(c, p[i], o, ns, no)
        A[2*i:2*i+2, 2*i:2*i+2] = Mx; Qn[2*i:2*i+2, 2*i:2*i+2] = Qi; pn[i] = pp
    return A, Qn, pn


class Tracker:
    r"""Propagates (p, S, Sh) along a path; S = Cov(x | inputs), Sh = Cov(x | y-path, inputs)."""

    def __init__(self, c: Cfg):
        self.c = c
        self.p = np.full(4, c.p0)
        self.S = np.zeros((8, 8))
        self.Sh = np.zeros((8, 8))

    def copy(self):
        t = Tracker(self.c); t.p = self.p.copy(); t.S = self.S.copy(); t.Sh = self.Sh.copy(); return t

    def step(self, cfgs):
        A, Qn, pn = step_mats(self.c, self.p, cfgs)
        S1 = A @ self.S @ A.T + Qn
        vy = (P @ self.S @ P.T).item()
        if vy > 0:
            cyy = (P @ A @ self.S @ P.T).item()
            v_given_y = (P @ S1 @ P.T).item() - cyy ** 2 / vy
        else:
            v_given_y = (P @ S1 @ P.T).item()
        Sm = A @ self.Sh @ A.T + Qn
        v_given_past = (P @ Sm @ P.T).item()
        I = 0.5 * np.log(v_given_y / v_given_past)
        dcl = 0.5 * np.log(v_given_y / (P @ Qn @ P.T).item())
        k = Sm @ P.T / v_given_past
        self.Sh = Sm - k @ (P @ Sm)
        self.S = S1
        self.p = pn
        return I, dcl


def base_cfgs(sig):
    return [(int(sig[i]), 3, int(sum(sig[j] for j in range(4) if j != i))) for i in range(4)]
