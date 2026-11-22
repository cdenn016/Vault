"""Independent rebuild of the audience instance P0 (fixed attention patterns) from the
results-free specification round4_drawn-once-check/spec.md.  Own code; exact Riccati
(iteration to machine precision) and exact discrete Lyapunov (Kronecker solve).
Checks: C15 covariance entries, closed form (with planted-error control), baselines,
attention law, frozen-null value, and the C20(i) enumeration of the 4^4 patterns.
"""
import itertools
import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=160)

F, Q, R, RS, RC, QC, GAM = 0.9, 0.05, 1.0, 0.01, 0.002, 1e-4, 40.0
A2 = np.array([[F, 0.0], [1.0, 0.0]])
QM = np.diag([Q, 0.0]) + QC * np.eye(2)
NA = 5  # agent 0 = source, 1..4 members


def sens_var(a, rs=RS):
    return rs if a == 0 else R


def riccati(own_var, msg_vars):
    """Steady-state prior covariance P^- and gain K for observations
    [eta_t + own noise] and, for each message, [eta_{t-1} + noise]."""
    H = np.array([[1.0, 0.0]] + [[0.0, 1.0]] * len(msg_vars))
    Rm = np.diag([own_var] + list(msg_vars))
    P = np.eye(2)
    for _ in range(100000):
        S = H @ P @ H.T + Rm
        K = P @ H.T @ np.linalg.inv(S)
        Ppost = (np.eye(2) - K @ H) @ P
        Pn = A2 @ Ppost @ A2.T + QM
        if np.max(np.abs(Pn - P)) < 1e-17:
            P = Pn
            break
        P = Pn
    S = H @ P @ H.T + Rm
    K = P @ H.T @ np.linalg.inv(S)
    return P, K, H


def dlyap(Abig, N):
    n = Abig.shape[0]
    X = np.linalg.solve(np.eye(n * n) - np.kron(Abig, Abig), N.reshape(-1))
    return X.reshape(n, n)


def sigma_c(pattern, rs=RS, rc=RC, cond_vS=False):
    """pattern: tuple of 4 tuples, the sets read by members 1..4. Source reads nothing.
    State: dE_a (2 each, a=0..4) then u_j = v_j(t-1) (5).  Returns 5x5 covariance of
    the eta_t components of the prior errors given the world path."""
    sets = [()] + [tuple(p) for p in pattern]
    n = 2 * NA + NA
    Ab = np.zeros((n, n))
    cols = []  # independent noise columns with variances
    var = []
    filt = []
    for a in range(NA):
        P, K, H = riccati(sens_var(a, rs), [sens_var(j, rs) + rc for j in sets[a]])
        filt.append((P, K, H))
        M = A2 @ (np.eye(2) - K @ H)
        AK = A2 @ K
        Ab[2 * a:2 * a + 2, 2 * a:2 * a + 2] = M
        # own sensing noise v_a(t): enters own error now and u_a next round
        c = np.zeros(n)
        c[2 * a:2 * a + 2] = AK[:, 0]
        c[2 * NA + a] = 1.0
        vv = sens_var(a, rs)
        if a == 0 and cond_vS:
            vv = 0.0
        cols.append(c); var.append(vv)
        for k, j in enumerate(sets[a]):
            Ab[2 * a:2 * a + 2, 2 * NA + j] += AK[:, 1 + k]  # carried v_j(t-1)
            c = np.zeros(n); c[2 * a:2 * a + 2] = AK[:, 1 + k]
            cols.append(c); var.append(rc)                    # receiver-specific channel noise
        for comp in range(2):                                  # computation noise
            c = np.zeros(n); c[2 * a + comp] = 1.0
            cols.append(c); var.append(QC)
    B = np.array(cols).T
    N = B @ np.diag(var) @ B.T
    SY = dlyap(Ab, N)
    idx = [2 * a for a in range(NA)]
    return SY[np.ix_(idx, idx)], filt


def diffusive(Pi, tol=1e-9):
    off = Pi - np.diag(np.diag(Pi))
    scale = np.max(np.abs(np.diag(Pi)))
    return (off.max() <= tol * scale) and (Pi.sum(1).min() >= -tol * scale)


def contrast(Pi, C):
    C = list(C); n = len(C)
    out = [k for k in range(Pi.shape[0]) if k not in C]
    PCC = Pi[np.ix_(C, C)]
    acut = -Pi[np.ix_(C, out)].sum(1) if out else np.zeros(n)
    Mx = PCC - np.diag(acut)
    phi = np.ones(n) / np.sqrt(n)
    xout = phi @ PCC @ phi
    # orthonormal basis of 1-perp
    Qm, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, :n - 1]]))
    Bp = Qm[:, 1:]
    xin = np.linalg.eigvalsh(Bp.T @ Mx @ Bp).min()
    return xin / xout


def regions(N=NA):
    for k in range(2, N + 1):
        for C in itertools.combinations(range(N), k):
            yield C


def multiinfo(S, C):
    C = list(C)
    Sc = S[np.ix_(C, C)]
    return 0.5 * (np.log(np.diag(Sc)).sum() - np.linalg.slogdet(Sc)[1])


def substitute(S):
    rho2 = S ** 2 / np.outer(np.diag(S), np.diag(S))
    I = -0.5 * np.log(np.clip(1 - rho2, 1e-300, None))
    best = -np.inf
    for blk in itertools.combinations(range(NA), 2):
        other = [k for k in range(NA) if k not in blk]
        within = [I[blk[0], blk[1]]] + [I[i, j] for i, j in itertools.combinations(other, 2)]
        between = [I[i, j] for i in blk for j in other]
        mb = np.mean(between)
        val = np.inf if mb < 1e-15 else np.mean(within) / mb
        best = max(best, val)
    return best


# validation of the contrast code on the record's test value
Stest = np.eye(4) + 0.5 * np.ones((4, 4))
print("test value r (expect 3):", contrast(np.linalg.inv(Stest), range(4)))

# ---------------- all-source pattern (P0 up to attention events of prob ~2e-14)
allS = ((0,), (0,), (0,), (0,))
S, filt = sigma_c(allS)
sig, c, v, b = S[0, 0], S[0, 1], S[1, 1], S[1, 2]
print("Var e_S, Cov(e_S,e_i), Var e_i, Cov(e_i,e_j):", sig, c, v, b)
Pi = np.linalg.inv(S)
print("Pi diffusive:", diffusive(Pi), " coupling AA %.3f  SA %.3f  leaks member %.3f source %.3f"
      % (-Pi[1, 2], -Pi[0, 1], Pi[1].sum(), Pi[0].sum()))
A = (1, 2, 3, 4)
rA = contrast(Pi, A)
al = v - b; bp = b - c * c / sig
print("r(A) direct %.6f   closed form 1-c/sig+n*beta'/alpha %.6f   planted-wrong 1+n*beta/alpha %.6f"
      % (rA, 1 - c / sig + 4 * bp / al, 1 + 4 * b / al))
others = sorted(((contrast(Pi, C), C) for C in regions() if C != A), reverse=True)[:2]
print("largest other regions:", others)
offs = [-Pi[i, j] for i in range(NA) for j in range(i + 1, NA)]
abar = np.mean(offs); ebar = Pi.sum(1).mean()
print("mean-coupling baseline 1+N*abar/ebar: %.6f (abar %.3f, ebar %.3f)" % (1 + NA * abar / ebar, abar, ebar))
vb = np.mean(np.diag(S)); ob = (S.sum() - np.trace(S)) / 20
print("relabeling-averaged baseline: %.6f" % (1 + 5 * ob / (vb - ob)))
print("multi-information of A: %.6f" % multiinfo(S, A))
print("substitute selector: %.6f" % substitute(S))
Sc, _ = sigma_c(allS, cond_vS=True)
print("conditioning on source sensing noise: max offdiag among members %.2e, r(A) %.6f"
      % (np.abs(Sc[1:, 1:] - np.diag(np.diag(Sc[1:, 1:]))).max(), contrast(np.linalg.inv(Sc), A)))
Sn, _ = sigma_c(allS, rc=100 * RC)
Pn = np.linalg.inv(Sn)
print("negative control Rc x100: diffusive %s r(A) %.4f" % (diffusive(Pn), contrast(Pn, A)))

# attention law of a member at the all-source steady state
Pm, Km, Hm = filt[1]


def info(msg_vars):
    H = np.array([[1.0, 0.0]] + [[0.0, 1.0]] * len(msg_vars))
    Rm = np.diag([R] + list(msg_vars))
    Sx = H @ Pm @ H.T + Rm
    return 0.5 * (np.linalg.slogdet(Sx)[1] - np.linalg.slogdet(Rm)[1])


I0, IS, Im = info([]), info([RS + RC]), info([R + RC])
w = np.array([np.exp(GAM * (I0 - IS)), 1.0, np.exp(GAM * (Im - IS))])
Z = w[0] + w[1] + 3 * w[2]
print("info gains (nats): none %.5f source %.5f co-member %.5f" % (I0, IS, Im))
print("P(read nothing) %.3e  P(read some co-member) %.3e  P(source) = 1 - %.3e"
      % (w[0] / Z, 3 * w[2] / Z, (w[0] + 3 * w[2]) / Z))

# frozen null with unconditioned frozen content: common offset v_S(0)
M = A2 @ (np.eye(2) - Km @ Hm)
g = (np.linalg.solve(np.eye(2) - M, (A2 @ Km)[:, 1]))[0]
print("g = %.6f, r_fr(A) = 1+4 g^2 R_S/alpha = %.4f, member correlation %.3f"
      % (g, 1 + 4 * g * g * RS / al, g * g * RS / (al + g * g * RS)))

# ---------------- C20(i): the 4^4 fixed patterns
opts = lambda i: [j for j in range(NA) if j != i]
ndiff = 0; best = []; selA = 0; mi = []; sub = []; nd_mi = []
for pat in itertools.product(*[opts(i) for i in range(1, 5)]):
    Sp, _ = sigma_c(tuple((j,) for j in pat))
    Pp = np.linalg.inv(Sp)
    m4 = max(multiinfo(Sp, C) for C in itertools.combinations(range(NA), 4))
    sub.append(substitute(Sp))
    if diffusive(Pp):
        ndiff += 1
        rs_ = {C: contrast(Pp, C) for C in regions()}
        best.append((max(rs_.values()), pat))
        if [C for C, r in rs_.items() if r >= 4.5] == [A]:
            selA += 1
        mi.append((m4, pat, True))
    else:
        nd_mi.append(m4)
        mi.append((m4, pat, False))
best.sort(reverse=True)
print("diffusive patterns: %d of 256" % ndiff)
print("largest regional contrasts over diffusive patterns:", [(round(x, 4), p) for x, p in best[:3]],
      " count >= 5.384863: %d" % sum(x >= 5.384863 for x, _ in best))
print("patterns whose regions at r0=4.5 are exactly {A}: %d" % selA)
mi.sort(reverse=True)
print("multi-info top values:", [(round(x, 6), p, d) for x, p, d in mi[:3]], " max over non-diffusive %.6f" % max(nd_mi))
sub = np.array(sub)
print("substitute selector: min %.6f  median %.2f  infinite %d  count > 1.5: %d"
      % (sub.min(), np.median(sub), np.isinf(sub).sum(), (sub > 1.5 + 1e-12).sum()))
