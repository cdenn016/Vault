r"""Two-department firm (TDF) population: the escape from O1/O2.

Firm f has two departments: B_f senses and models a 'revenue' component eta^{3f}, S_f a 'cost' component eta^{3f+1};
both are AR(1) with (F, Q).  Inside a department every member relays its raw reading to its department mates (literal
one-round latency, receiver-specific noise Rc).  No channel joins the departments or the firms.  The firm's outcome
('profit') is a renewed world component
    eta^{3f+2}_{t+1} = h (eta^{3f}_t - eta^{3f+1}_t) + beta * sum_{j in firm f} u_j(t) + w^Z_t,  w^Z ~ N(0, QZ),
and every member regulates it toward 0 with a quadratic preference of precision Lam (common preference map H* = e_Z).
Acts (declaration D2: no intention sharing; each member treats the others' acts and the other department's component
at their prior means): member j's policy posterior with Gaussian habits N(0, sE2) and precision gamma is
    u_j ~ N(-gamma Lam beta s2 z_j, s2),  s2 = 1/(1/sE2 + gamma Lam beta^2),  z_j = h sigma_j m^+_{j,0}(t),
sigma = +1 on B, -1 on S.  Hence kappa_j = gamma Lam beta s2 h sigma_j and act-noise variance s2.  No member reads an
act or senses the outcome, so N_inf is inapplicable and the members' filters are exact for their data (N_ex
inapplicable).
"""
from __future__ import annotations

import numpy as np
import lgx


def act_params(gamma: float, Lam: float, beta: float, sE2: float, h: float) -> tuple[float, float]:
    s2 = 1.0 / (1.0 / sE2 + gamma * Lam * beta ** 2)
    return gamma * Lam * beta * s2 * h, s2


def tdf_spec(nd: int = 2, nf: int = 2, F: float = 0.9, Q: float = 0.05, R: float = 1.0, Rc: float = 0.1,
             qc: float = 1e-4, kappa: float = 0.5, beta: float = 1.0, sa2: float = 0.01, QZ: float = 0.05,
             h: float = 1.0, signs: tuple = (1, -1)) -> dict:
    K = 3 * nf
    Fw = np.zeros((K, K))
    Qw = np.zeros(K)
    ag = []
    for f in range(nf):
        Fw[3 * f, 3 * f] = F
        Fw[3 * f + 1, 3 * f + 1] = F
        Fw[3 * f + 2, 3 * f] = h
        Fw[3 * f + 2, 3 * f + 1] = -h
        Qw[3 * f:3 * f + 3] = [Q, Q, QZ]
        for dep in range(2):
            base = len(ag)
            idx = list(range(base, base + nd))
            for i in idx:
                ag.append({"k": 3 * f + dep, "R": R, "senders": [j for j in idx if j != i],
                           "kappa": signs[dep] * kappa, "Z": 3 * f + 2, "beta": beta, "sa2": sa2, "readacts": []})
    return {"Fw": Fw, "Qw": Qw, "Rc": Rc, "qc": qc, "agents": ag}


def groups(nd: int = 2, nf: int = 2) -> dict:
    out = {}
    for f in range(nf):
        b0 = 2 * nd * f
        out[f"B{f}"] = tuple(range(b0, b0 + nd))
        out[f"S{f}"] = tuple(range(b0 + nd, b0 + 2 * nd))
        out[f"C{f}"] = tuple(range(b0, b0 + 2 * nd))
    return out


def analyze(spec: dict, nd: int, nf: int, null: str = "full", L: int = 40, Sig: np.ndarray | None = None) -> dict:
    if Sig is None:
        Sig = lgx.sigma_c(spec, null, L) if null != "eff" else lgx.sigma_private(spec, "eff")
    Pi = np.linalg.inv(Sig)
    dif = lgx.diffusivity(Pi)
    g = groups(nd, nf)
    res = {"Sigma": Sig, "Pi": Pi, "diff": dif}
    if dif["diffusive"]:
        res["r"] = {k: lgx.contrast(Pi, v)["r"] for k, v in g.items()}
        res["rbar"] = lgx.baseline_mean_coupling(Pi)
        res["top"] = lgx.all_regions(Pi, top=8)
    return res
