r"""Deciding script D5b: memory clause of the scalar collective average, worst case over REACHABLE single-round
patterns and sustained histories (every pattern below has positive probability: habits have full support and
gamma < inf), and a rigorous upper bound on sup over all paths.

Reachability: in round t member i reads its own sensor, its private sensor iff sigma_i(t) = 1, n_s relays of
s_j(t-1) (any n_s in 0..3) and n_o <= min(n_s, open mates at t-1) relays of o_j(t-1).
Rigorous bound: Sigma(t) = Cov(x_t | blanket, policy) is block diagonal (A(t), Q^n(t) block diagonal, Sigma(0) = 0),
Sigma_i(t+1) = A_i Sigma_i A_i^T + Q_i.  If Sbar_i satisfies A Sbar_i A^T + Q <= Sbar_i for every member config and
every reachable p_prev, then Sigma_i(t) <= Sbar_i for all t.  The conditional covariance Sigma_{x|y} is monotone in
Sigma (Loewner), so d_cl(t) <= max over configs of d_cl(A, Q^n, blockdiag(Sbar)).
Declared expectations (before running): reachable worst single-round pattern between 0.01 and 0.03; the rigorous
bound larger than the reachable worst (it is a bound over a superset).
NEGATIVE CONTROL: the bound must dominate every sampled-path value (max 5.2e-3 in d5_out.txt) and every reachable
worst case computed here; if it does not, the bound computation is wrong.
"""
import itertools, time
import numpy as np
from lib3 import Pminus, A_F
from instance3 import PAR, ALPHA_M

t0 = time.time()
n = 4
Af = A_F(PAR.F)
P1 = np.zeros((1, 8)); P1[0, 0::2] = 0.25


def member_mats(p_prev, own, ns, no, par=PAR):
    P00, P01, P11 = Pminus(par, p_prev)
    Pm = np.array([[P00, P01], [P01, P11]])
    Pp = np.linalg.inv(np.linalg.inv(Pm) + np.diag([1 / par.R + own / par.Rs,
                                                     ns / (par.R + par.Rc) + no / (par.Rs + par.Rc)]))
    Ai = Af @ Pp @ np.linalg.inv(Pm)
    krs = Pp[:, 1] / (par.R + par.Rc); kro = Pp[:, 1] / (par.Rs + par.Rc)
    Qi = Af @ (ns * par.Rc * np.outer(krs, krs) + no * par.Rc * np.outer(kro, kro)) @ Af.T + par.qc * np.eye(2)
    return Ai, Qi, Pp[0, 0]


def dcl(A, Qn, Sig, P=P1):
    PS = P @ Sig
    Sxy = Sig - PS.T @ np.linalg.solve(PS @ P.T, PS)
    M = P @ A @ Sxy @ A.T @ P.T
    return 0.5 * np.log(np.linalg.det(np.eye(P.shape[0]) + np.linalg.solve(P @ Qn @ P.T, M)))


def blockdiag(blocks):
    S = np.zeros((8, 8))
    for i, B in enumerate(blocks):
        S[2*i:2*i+2, 2*i:2*i+2] = B
    return S


# ---- (a) reachable worst cases from sustained base histories ----
opts_all = [(o, ns, no) for o in (0, 1) for ns in range(4) for no in range(ns + 1)]
bases = {"0000": (0, 0, 0, 0), "1000": (1, 0, 0, 0), "1100": (1, 1, 0, 0), "1110": (1, 1, 1, 0), "1111": (1, 1, 1, 1)}
worst_reach = 0.0
for name, sb in bases.items():
    # sustained base: every member reads all three mates, statuses sb, for 400 rounds
    p = np.full(n, PAR.p0); Sb = [np.zeros((2, 2)) for _ in range(n)]
    for _ in range(400):
        new = []
        for i in range(n):
            k1 = sum(sb[j] for j in range(n) if j != i)
            Ai, Qi, pp = member_mats(p[i], sb[i], 3, k1)
            Sb[i] = Ai @ Sb[i] @ Ai.T + Qi; new.append(pp)
        p = np.array(new)
    Sig = blockdiag(Sb)
    best, arg = 0.0, None
    per = []
    for i in range(n):
        k1 = sum(sb[j] for j in range(n) if j != i)
        per.append([(o, ns, no) for (o, ns, no) in opts_all if no <= min(ns, k1)])
    mats = [{c: member_mats(p[i], *c) for c in per[i]} for i in range(n)]
    for combo in itertools.product(*per):
        A = blockdiag([mats[i][c][0] for i, c in enumerate(combo)])
        Qn = blockdiag([mats[i][c][1] for i, c in enumerate(combo)])
        v = dcl(A, Qn, Sig)
        if v > best:
            best, arg = v, combo
    worst_reach = max(worst_reach, best)
    print(f"(a) base {name} sustained: reachable worst single round d_cl {best:.4e} at {arg}  ({time.time()-t0:.0f}s)",
          flush=True)

# ---- (b) rigorous upper bound ----
# reachable range of p_prev: between the all-data and the own-sensor-only Riccati limits (and the start p0)
def riccati(own, ns, no):
    p = PAR.p0
    for _ in range(3000):
        p = member_mats(p, own, ns, no)[2]
    return p
p_lo = riccati(1, 3, 3); p_hi = max(riccati(0, 0, 0), PAR.p0)
pgrid = np.linspace(p_lo, p_hi, 121)
cfgs = opts_all
# common quadratic bound Sbar = c * M; M solves M = A_w M A_w^T + I for the least contractive config (own sensor only,
# p_hi); c = max over configs and p_prev of lambda_max(Q relative to M - A M A^T)
A_w, _, _ = member_mats(p_hi, 0, 0, 0)
M = np.eye(2)
for _ in range(5000):
    M = A_w @ M @ A_w.T + np.eye(2)
ok = True
cmax = 0.0
for (o, ns, no) in cfgs:
    for pp in pgrid:
        A, Q, _ = member_mats(pp, o, ns, no)
        D = M - A @ M @ A.T
        ev = np.linalg.eigvalsh(D)
        if ev.min() <= 0:
            ok = False
            continue
        L = np.linalg.cholesky(D)
        Li = np.linalg.inv(L)
        cmax = max(cmax, np.linalg.eigvalsh(Li @ Q @ Li.T).max())
print(f"(b) common Lyapunov M (own-sensor-only config at p_hi={p_hi:.4f}, p_lo={p_lo:.4f}): M - A M A^T > 0 for all "
      f"configs and p_prev on the grid: {ok}; c = {cmax:.4e}")
if ok:
    Sbar = cmax * M
    # sup over all single-round configs (superset: any n_o <= n_s) and p_prev on the grid (coarse), members independent
    best_b, arg_b = 0.0, None
    pcoarse = pgrid[::20]
    Sig = blockdiag([Sbar] * n)
    for pp in pcoarse:
        mats = {c: member_mats(pp, *c) for c in cfgs}
        for combo in itertools.product(cfgs, repeat=n):
            A = blockdiag([mats[c][0] for c in combo]); Qn = blockdiag([mats[c][1] for c in combo])
            v = dcl(A, Qn, Sig)
            if v > best_b:
                best_b, arg_b = v, (pp, combo)
    print(f"(b) rigorous-type bound (Sigma <= Sbar, common p_prev on a coarse grid of 7 values): sup d_cl <= {best_b:.4e} "
          f"at {arg_b}  ({time.time()-t0:.0f}s)")
    print(f"NEG: bound >= sampled max 5.2e-3 and >= reachable worst {worst_reach:.4e}: {best_b >= max(5.2e-3, worst_reach)}")
print(f"MEMORY (strict sup over reachable patterns, explored): {worst_reach:.4e} vs alpha_M = {ALPHA_M}: "
      f"holds {worst_reach <= ALPHA_M} (margin {ALPHA_M - worst_reach:.4e})")
print(f"total {time.time()-t0:.0f}s")
