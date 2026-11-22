r"""Attack A4: agency index of PN's act component at the population's own precision gamma = 300.

def:agy-agency-index (05_agency.tex:240-246) uses the ACTUAL conditional laws of the members' joint policies.
PN (investigator) declares one precision for attention and acts, gamma = 300 (check13: attention is sharp only for
gamma of order 100 or more), habits N(0, sigE^2) with sigE^2 = c/(gamma Lam b^2), c = b g n / (n (F - b g n)),
and the admissible class "belief at the members' average, true effect, Lam, habits fixed, one gamma_C in [0,6]".

Declared expectations (before running):
 (a) With the declared class gamma_C in [0,6], the index at gamma = 300 is far below the claimed 0.94 (< 0.2),
     because no member of the class reaches the actual precision.
 (b) With gamma_C free on [0, 1500] the index at gamma = 300 is about 0.966 (investigator's invariance claim).
 (c) If the actual act law is PN's stated dynamics rule (mean -g m_j^+, deliberation covariance) instead of the
     deliberation stationary law (mean -gamma Lam b S z), the index changes by less than 0.02.
 (d) Decision states with the collective mean drawn from its stationary law (instead of fixed 0.3) give an index
     within 0.03 of (b).
 NEG control: at gamma = 300 with members' deviations multiplied by 30 the index must fall below 0.5.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from win import build

F, Q, R, Rc, b, n, g, Lam = 0.9, 0.05, 1.0, 0.2, 0.2, 4, 0.05, 4.0
c = b * g * n / (n * (F - b * g * n))
alpha_prior = 4.202606e-03  # disagreement variance of prior errors (a1_out.txt)


def law_delib(gam: float, sig2: float, z: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    S = np.linalg.inv(np.eye(n) / sig2 + gam * Lam * b * b * np.ones((n, n)))
    return -gam * Lam * b * S @ z, S


def kl(m1, S1, m0, S0) -> float:
    S0i = np.linalg.inv(S0)
    d = m0 - m1
    return 0.5 * (np.trace(S0i @ S1) - n + d @ S0i @ d + np.log(np.linalg.det(S0) / np.linalg.det(S1)))


def index(gam: float, grid: np.ndarray, states: list, rule: str = "delib") -> tuple[float, float]:
    sig2 = c / (gam * Lam * b * b)
    acts, den = [], 0.0
    for (mvec, mC) in states:
        mu, S = law_delib(gam, sig2, F * mvec)
        if rule == "dynamics":
            mu = -g * mvec  # PN's stated act rule u_j = -g m_j^+ (same total act, different deviation gain)
        acts.append((mu, S, mC))
        den += kl(mu, S, np.zeros(n), sig2 * np.eye(n))
    best = (np.inf, None)
    for gC in grid:
        num = 0.0
        for mu, S, mC in acts:
            mC_, SC = law_delib(gC, sig2, F * mC * np.ones(n))
            num += kl(mu, S, mC_, SC)
        if num < best[0]:
            best = (num, gC)
    return 1 - best[0] / den, best[1]


if __name__ == "__main__":
    rng = np.random.default_rng(1)
    Z = np.linalg.qr(np.column_stack([np.ones(n) / 2, rng.standard_normal((n, n - 1))]))[0][:, 1:]
    fixed = []
    for _ in range(200):
        dev = Z @ (np.sqrt(alpha_prior) * rng.standard_normal(n - 1))
        fixed.append((0.3 + dev, 0.3))
    print("c = %.6f; sigE2 at gamma=300: %.4e" % (c, c / (300 * Lam * b * b)))
    for gam in [2.0, 300.0]:
        i6, g6 = index(gam, np.linspace(0, 6, 601), fixed)
        iw, gw = index(gam, np.linspace(0, 5 * gam, 1501), fixed)
        print("gamma=%5.0f  (a) class gamma_C in [0,6]: index %.5f (best gamma_C %.2f) | (b) gamma_C in [0,%g]: index %.5f (best %.2f)" % (
            gam, i6, g6, 5 * gam, iw, gw))
    idyn, gdyn = index(300.0, np.linspace(0, 1500, 1501), fixed, rule="dynamics")
    print("(c) gamma=300, actual mean = PN dynamics rule -g m_j^+: index %.5f (best %.2f)" % (idyn, gdyn))
    # (d) stationary collective mean: Var(mbar^+) from the window model
    mod = build(F, Q, R, Rc, b, g, 60, mode="base")
    mbar = mod["Mp"][40].mean(axis=0)
    sd_m = float(np.sqrt(mbar @ mbar))
    # posterior deviation variance of disagreement modes (member m^+ minus mean)
    devs = mod["Mp"][40] - mbar[None, :]
    var_dev = float(np.mean(np.sum(devs * devs, axis=1))) * n / (n - 1)
    print("    stationary sd of mbar^+ = %.4f ; posterior disagreement variance per mode = %.4e (prior alpha %.4e)" % (
        sd_m, var_dev, alpha_prior))
    stat = []
    for _ in range(200):
        mC = sd_m * rng.standard_normal()
        dev = Z @ (np.sqrt(var_dev) * rng.standard_normal(n - 1))
        stat.append((mC + dev, mC))
    ist, gst = index(300.0, np.linspace(0, 1500, 1501), stat)
    print("(d) gamma=300, stationary decision states, wide class: index %.5f (best %.2f)" % (ist, gst))
    i6s, _ = index(300.0, np.linspace(0, 6, 601), stat)
    print("    same states, declared class [0,6]: index %.5f" % i6s)
    neg = [(0.3 + 30 * (m - 0.3), 0.3) for m, _ in fixed]
    ineg, _ = index(300.0, np.linspace(0, 1500, 1501), neg)
    print("NEG (30x deviations) gamma=300 wide class: index %.5f (must be < 0.5)" % ineg)
