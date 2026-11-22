r"""O6 check B: uniqueness of the stationary policy-covariance law of I* by coupling, with a negative control.

Theorem 1 of the O6 report predicts, for finite gamma, that two copies of the chain started anywhere can be coupled
so that their policies coincide after an a.s. finite time with a geometric tail, after which |p_a - p_b|_inf shrinks
by at least rho_bar = (F/(1 + (Q + qc)/R))^2 = 0.734554 per round (check A).  At gamma = inf (best response) the
real-time chain has absorbing slot profiles (exploration: k = 1 open slot is a self-consistent best-response count
at p*(1)), so the stationary law is not unique and copies started in two such profiles never couple.

Parts and DECLARED EXPECTATIONS (before running):
  B0 validation of sim_core against lib (same kernels, different random-number use): stationary open rate, mean p and
     attention deviation rate agree within 4 combined batch-means SE, T-fast and T-real, 30000 rounds each.
  B1 gamma = 400, 200 pairs per protocol, copy a from (p = 0, all slots closed, no relays), copy b from (p = 0.2,
     all slots open, all relays): at least 99% of pairs couple (policies equal from tau on, verified for 200 further
     rounds, |dp| <= 1e-13 at the end) within 1000 rounds; every post-coupling contraction ratio dp(t+1)/dp(t)
     (dp > 1e-13) is <= rho_bar.
  B2 NEGATIVE CONTROL, gamma = inf, T-real, both copies at p = p*(1) with one open slot, at member 0 resp. member 1,
     all relays: 0 of 50 pairs couple within 1500 rounds and no slot ever changes (absorbing profiles).
  B2+ the same starts at gamma = 400: at least 99% of 100 pairs couple within 1000 rounds.
"""
import os
import sys
import time
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from sim_core import Par, State, run_path, step, n_uniforms, INF, posterior, Pminus
from lib import simulate_policy_path, simulate_policy_path_real

PAR = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, Rsh=0.0, psi=0.024, gamma=400.0, qc=1e-4, n=4, n_zero=4, kmsg=3)
RHO_BAR = (PAR.F / (1 + (PAR.Q + PAR.qc) / PAR.R)) ** 2
ALL = [tuple(j for j in range(4) if j != i) for i in range(4)]


def stats(pth, burn=200, nb=20):
    s = pth.slots[burn:].mean(1)
    pv = (pth.Pm[burn:, :, 1, 1] - PAR.qc).mean(1)
    dv = np.array([sum(1 for mt in pth.mates[t] if len(mt) < 3) for t in range(burn, len(pth.mates))]) / 4.0
    out = []
    for x in (s, pv, dv):
        b = np.array_split(x, nb)
        m = np.array([bb.mean() for bb in b])
        out.append((x.mean(), m.std(ddof=1) / np.sqrt(nb)))
    return out


def coupled_until(par, T, rng, protocol, sa, sb, verify=200, tol=1e-13):
    r"""Run two copies on common uniforms; stop `verify` rounds after the policies have become equal with
    |dp| <= tol, or at T.  Returns (tau or None, list of post-coupling contraction ratios, slot changes a, b)."""
    nu = n_uniforms(par.n)
    eq_since = None
    ratios = []
    prev_dp = None
    changes = [0, 0]
    for t in range(T):
        eq = bool(np.array_equal(sa.slots, sb.slots) and sa.mates == sb.mates)
        dp = float(np.max(np.abs(sa.p - sb.p)))
        if eq:
            if eq_since is None:
                eq_since = t
            if prev_dp is not None and prev_dp > tol:
                ratios.append(dp / prev_dp)
            prev_dp = dp
            if t - eq_since >= verify and dp <= tol:
                return eq_since, ratios, changes
        else:
            eq_since, prev_dp = None, None
        U = rng.random(nu)
        na, _ = step(par, sa, U, protocol)
        nb_, _ = step(par, sb, U, protocol)
        changes[0] += int(not np.array_equal(na.slots, sa.slots))
        changes[1] += int(not np.array_equal(nb_.slots, sb.slots))
        sa, sb = na, nb_
    return None, ratios, changes


t0 = time.time()
print("B0 validation (sim_core vs lib), 30000 rounds each, batch-means SE over 20 batches")
for proto in ("fast", "real"):
    rng = np.random.default_rng(11 if proto == "fast" else 12)
    mine = stats(run_path(PAR, 30000, rng, proto))
    libp = simulate_policy_path(PAR, 30000, rng, "full") if proto == "fast" else \
        simulate_policy_path_real(PAR, 30000, rng, "full")
    ref = stats(libp)
    ok = True
    for name, (m1, s1), (m2, s2) in zip(("open rate", "mean p", "attention deviation"), mine, ref):
        z = (m1 - m2) / np.sqrt(s1 ** 2 + s2 ** 2 + 1e-300)
        ok &= abs(z) < 4
        print(f"  T-{proto} {name}: sim_core {m1:.6f} +/- {s1:.1e}, lib {m2:.6f} +/- {s2:.1e}, z = {z:+.2f}")
    print(f"  T-{proto}: {'PASS' if ok else 'FAIL'}  ({time.time()-t0:.1f}s)")

print(f"B1 coupling at gamma = 400 from extreme initial states (rho_bar = {RHO_BAR:.6f})")
for proto in ("fast", "real"):
    rng = np.random.default_rng(21 if proto == "fast" else 22)
    taus, rmax, fail = [], 0.0, 0
    for k in range(200):
        sa = State(np.zeros(4), np.zeros(4, dtype=int), [tuple()] * 4)
        sb = State(np.full(4, 0.2), np.ones(4, dtype=int), list(ALL))
        tau, ratios, _ = coupled_until(PAR, 1000, rng, proto, sa, sb)
        if tau is None:
            fail += 1
        else:
            taus.append(tau)
            if ratios:
                rmax = max(rmax, max(ratios))
    taus = np.array(taus)
    frac = len(taus) / 200
    ok = frac >= 0.99 and rmax <= RHO_BAR + 1e-12
    print(f"  T-{proto}: coupled {len(taus)}/200; tau median {np.median(taus):.0f}, 90% {np.quantile(taus, 0.9):.0f}, "
          f"max {taus.max()}; max post-coupling ratio dp(t+1)/dp(t) = {rmax:.6f} -> {'PASS' if ok else 'FAIL'} "
          f"({time.time()-t0:.1f}s)")

# p*(1): fixed point with one open slot and three relays
p1 = 0.09
for _ in range(3000):
    p1 = posterior(Pminus(PAR, p1), 1 / PAR.R + 1 / PAR.Rs, 3 / (PAR.R + PAR.Rc))[0, 0]
print(f"B2 negative control: gamma = inf, T-real, starts at p*(1) = {p1:.6f}, slots e_0 vs e_1")
for gam, T, npair, label in ((INF, 1500, 50, "B2  gamma=inf"), (400.0, 1000, 100, "B2+ gamma=400")):
    par = PAR.with_(gamma=gam)
    rng = np.random.default_rng(31)
    coupled, tot_changes = 0, 0
    for k in range(npair):
        sa = State(np.full(4, p1), np.array([1, 0, 0, 0]), list(ALL))
        sb = State(np.full(4, p1), np.array([0, 1, 0, 0]), list(ALL))
        tau, _, ch = coupled_until(par, T, rng, "real", sa, sb)
        coupled += tau is not None
        tot_changes += ch[0] + ch[1]
    if gam == INF:
        ok = coupled == 0 and tot_changes == 0
        print(f"  {label}: coupled {coupled}/{npair}, slot changes {tot_changes} -> "
              f"{'FAIL-as-expected (no coupling: invariant law not unique)' if ok else 'UNEXPECTED'} ({time.time()-t0:.1f}s)")
    else:
        ok = coupled >= 0.99 * npair
        print(f"  {label}: coupled {coupled}/{npair}, slot changes {tot_changes} -> {'PASS' if ok else 'FAIL'} "
              f"({time.time()-t0:.1f}s)")
