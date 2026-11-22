"""Independent spot checks for open_hie_record_contrast (my own code; nothing imported from the stored script)."""
from __future__ import annotations
import itertools, math
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyap, expm
import sympy as sp

rng = np.random.default_rng(11)


def drift(A, n, eps, beta, omega, delta):
    N = A.shape[0]
    M = np.zeros((N + 1, N + 1))
    M[:N, :N] = eps * np.eye(N) + np.diag(A.sum(1)) - A
    M[:n, :n] += beta * np.eye(n)
    M[:n, N] = -beta
    M[N, :n] = -omega / n
    M[N, N] = omega + delta
    return M


def precision(M, q, qz):
    N = M.shape[0] - 1
    Q = np.diag([q] * N + [qz])
    # scipy solves A X + X A^H = Q
    Sig = lyap(M, 2 * Q)
    assert np.allclose(M @ Sig + Sig @ M.T, 2 * Q, atol=1e-10)
    return np.linalg.inv(Sig), Sig


def diffusive(P, tol=1e-11):
    s = np.abs(P).max()
    off = P - np.diag(np.diag(P))
    return off.max() <= tol * s and P.sum(1).min() >= -tol * s


def ring(k, a=1.0):
    A = np.zeros((k, k))
    for i in range(k):
        A[i, (i + 1) % k] = A[(i + 1) % k, i] = a
    return A


def contrast(P, S):
    S = list(S); k = len(S)
    out = [v for v in range(P.shape[0]) if v not in S]
    sub = P[np.ix_(S, S)]
    cutv = -P[np.ix_(S, out)].sum(1) if out else np.zeros(k)
    xout = sub.sum() / k
    Min = sub - np.diag(cutv)
    Bq = np.linalg.qr(np.column_stack([np.ones(k), np.eye(k)[:, 1:]]))[0][:, 1:]
    xin = np.linalg.eigvalsh(Bq.T @ Min @ Bq).min()
    return xin / xout


print("== 0. manuscript instance ==")
A16 = np.zeros((16, 16)); A16[:8, :8] = ring(8); A16[8:, 8:] = ring(8)
for i in range(8):
    A16[i, 8 + i] = A16[8 + i, i] = 0.05
eps, beta, omega, q = 0.02, 0.2, 0.1, 1.0
qrev = omega * q / (8 * beta)
P, _ = precision(drift(A16, 8, eps, beta, omega, 0.0), q, qrev)
print("r(C') =", round(contrast(P, list(range(8)) + [16]), 6), " diffusive:", diffusive(P))
for dl in (0.0, 0.01):
    row = []
    for ratio in (0, 0.5, 0.9, 0.99, 1, 1.01, 1.1, 2, 2.6, 2.7, 4):
        Pc, _ = precision(drift(ring(8), 8, eps, beta, omega, dl), q, ratio * qrev)
        Po, _ = precision(drift(A16, 8, eps, beta, omega, dl), q, ratio * qrev)
        row.append(f"{ratio}:{'D' if diffusive(Pc) else '-'}{'D' if diffusive(Po) else '-'}")
    print(f" delta={dl} (closed,open) ", " ".join(row))

print("== C1. closed form, interval, n=2, W1 ==")


def c1_pred(A, n, eps, beta, omega, delta, q, kap):
    T = eps + beta + omega + delta
    D2 = eps * (omega + delta) + beta * delta
    Pk = beta * omega * (kap - 1) ** 2 + T * T * kap
    L = np.diag(A.sum(1)) - A
    Pi = np.zeros((n + 1, n + 1))
    Pi[:n, :n] = ((eps + beta) * np.eye(n) + L) / q + beta * omega * (1 - kap) * ((omega + delta) + kap * (eps + beta)) / (n * q * Pk) * np.ones((n, n))
    Pi[:n, n] = Pi[n, :n] = -beta * T * ((omega + delta) + kap * (eps + beta)) / (q * Pk)
    Pi[n, n] = n * beta * T * ((omega + delta) ** 2 + D2 + kap * beta * omega) / (omega * q * Pk)
    amin = (A + 1e9 * np.eye(n)).min()
    kmax = 1 + delta * T / (eps * omega)
    if amin == 0:
        kmin = 1.0
    else:
        krow = beta * delta / (eps * T + beta * delta)
        if n * amin >= omega + delta:
            koff = 0.0
        else:
            g = lambda k: beta * omega * (1 - k) * ((omega + delta) + k * (eps + beta)) - n * amin * (beta * omega * (k - 1) ** 2 + T * T * k)
            lo, hi = 0.0, 1.0
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if g(mid) > 0 else (lo, mid)
            koff = hi
        kmin = max(krow, koff)
    return Pi, kmin, kmax


worst = 0.0; nb = 0
for trial in range(400):
    n = int(rng.integers(2, 7))
    A = 10 ** rng.uniform(-3, 1, (n, n)); A = (A + A.T) / 2; np.fill_diagonal(A, 0)
    if trial % 3 == 0 and n >= 3:
        A[0, 1] = A[1, 0] = 0.0
    e, b, w = (10 ** rng.uniform(-2, 0.7, 3)).tolist()
    d = 0.0 if trial % 4 == 0 else float(10 ** rng.uniform(-2.5, 0.7))
    qq = float(10 ** rng.uniform(-1, 1))
    qr = w * qq / (n * b)
    Pi0, kmin, kmax = c1_pred(A, n, e, b, w, d, qq, 1.0)
    for kap in {0.0, 0.3, 1.0, kmin * 0.999, kmin * 1.001 + 1e-9, kmax * 0.999, kmax * 1.001, 5 * kmax}:
        Pi_pred, _, _ = c1_pred(A, n, e, b, w, d, qq, kap)
        Pi_num, _ = precision(drift(A, n, e, b, w, d), qq, kap * qr)
        worst = max(worst, np.abs(Pi_pred - Pi_num).max() / np.abs(Pi_num).max())
        inside = kmin * (1 + 1e-6) + 1e-12 <= kap <= kmax * (1 - 1e-6)
        outside = kap < kmin * (1 - 1e-6) - 1e-12 or kap > kmax * (1 + 1e-6)
        if inside or outside:
            nb += 1
            assert diffusive(Pi_num, 1e-10) == inside, (trial, kap, kmin, kmax)
print(f" closed form max rel err {worst:.2e}; interval prediction matched on {nb} decided (instance, kappa) pairs")
# planted error: kappa_max without the T/omega factor must be contradicted
A = ring(8); Pi_num, _ = precision(drift(A, 8, 0.02, 0.2, 0.1, 0.01), 1.0, 2.0 * 0.0625)
print(" planted kmax=1+delta/eps=1.5 would predict non-diffusive at 2.0; actual diffusive:", diffusive(Pi_num))
# W1 exact
r = sp.Rational
M1 = sp.Matrix([[r(13, 10), -1, -r(1, 5)], [-1, r(13, 10), -r(1, 5)], [-r(1, 20), -r(1, 20), r(1, 10)]])
X = sp.Matrix(3, 3, sp.symbols("x0:9"))
sol = sp.solve(list(M1 * X + X * M1.T - sp.diag(2, 2, 0)), list(X))
Pi1 = X.subs(sol).inv()
print(" W1 K2 a=1 eps=.1 beta=.2 omega=.1 delta=0 q_z=0: Pi =", Pi1.tolist(), "row sums", [sum(Pi1.row(i)) for i in range(3)])

print("== C2. upper barrier with outsiders; extremes ==")
cnt = 0; minpos = np.inf
for trial in range(600):
    n = int(rng.integers(2, 5)); m = int(rng.integers(1, 4)); N = n + m
    A = 10 ** rng.uniform(-2, 1.5, (N, N)); A = (A + A.T) / 2; np.fill_diagonal(A, 0)
    if trial % 2 == 0:  # sparse: keep a random spanning structure with one cross edge
        mask = np.triu(rng.uniform(size=(N, N)) < 0.4, 1); mask = mask | mask.T
        A = A * mask
        A[0, n] = A[n, 0] = float(10 ** rng.uniform(-2, 1))
    e, b, w = (10 ** rng.uniform(-2, 1, 3)).tolist()
    d = 0.0 if trial % 3 == 0 else float(10 ** rng.uniform(-2, 1))
    M = drift(A, n, e, b, w, d); qr = w / (n * b)
    for ratio in (1.02, 1.5, 3.0, 30.0):
        Pi, _ = precision(M, 1.0, ratio * qr)
        off = Pi - np.diag(np.diag(Pi))
        rel = off.max() / np.abs(Pi).max()
        minpos = min(minpos, rel)
        assert rel > 1e-13, (trial, ratio, rel)
        cnt += 1
print(f" {cnt} open instances above q_rev: all have a positive off-diagonal entry (smallest relative size {minpos:.1e})")

print("== C3. q_z = 0 ==")
bad = 0
for trial in range(300):
    n = int(rng.integers(2, 5)); m = int(rng.integers(1, 4)); N = n + m
    A = 10 ** rng.uniform(-1.5, 1.5, (N, N)); A = (A + A.T) / 2; np.fill_diagonal(A, 0)
    e, b, w = (10 ** rng.uniform(-1.5, 0.7, 3)).tolist()
    d = 0.0 if trial % 2 == 0 else float(10 ** rng.uniform(-2, 0.5))
    M = drift(A, n, e, b, w, d)
    Pi, Sig = precision(M, 1.0, 0.0)
    G = M @ Sig
    rs = Pi.sum(1)
    assert abs(G[N, N]) < 1e-9 and np.all(G[:N, N] > 0)
    assert abs(rs[:N] @ G[:N, N] + d) < 1e-7 * (1 + d + np.abs(rs).max() * np.abs(G).max())
    bad += diffusive(Pi, 1e-12)
print(f" identity sum_i r_i (M Sigma)_iz = -delta and (M Sigma)_iz > 0 hold on 300 open instances; diffusive at q_z=0: {bad}")
# complete closed graph threshold a_ij >= omega/n at delta = 0
for a in (0.049, 0.051):
    Pi, _ = precision(drift(np.array([[0, a], [a, 0.0]]), 2, 0.1, 0.2, 0.1, 0.0), 1.0, 0.0)
    print(f"  closed K2, a={a}, omega/n=0.05, q_z=0: diffusive={diffusive(Pi)}  Pi_01={Pi[0,1]:+.4f}")

print("== C4. below q_rev ==")
for dl in (0.0, 0.01):
    M = drift(A16, 8, 0.02, 0.2, 0.1, dl)
    vals = [precision(M, 1.0, rt * 0.0625)[0][0, 2] for rt in (0.0, 0.5, 0.99)]
    print(f" open16 delta={dl}: Pi_02 at ratio 0,0.5,0.99 = {vals[0]:+.3e} {vals[1]:+.3e} {vals[2]:+.3e} (claimed > 0)")
K3 = np.ones((3, 3)) - np.eye(3)
for dl in (0.0, 0.05):
    M = drift(K3, 2, 0.1, 0.2, 0.1, dl)
    out = []
    for rt in (0.0, 0.1, 0.25, 0.5, 0.9, 1.0, 1.1):
        out.append(f"{rt}:{'D' if diffusive(precision(M, 1.0, rt * 0.25)[0]) else '-'}")
    print(f" W2 K3 delta={dl}:", " ".join(out))
A4 = np.array([[0, 1, 5, 0], [1, 0, 5, 0], [5, 5, 0, 1], [0, 0, 1, 0.0]])
M = drift(A4, 2, 0.5, 8.0, 0.25, 8.0)
out = []
for rt in (0.5, 0.8, 0.9, 0.99, 1.0, 1.1):
    Pi = precision(M, 1.0, rt / 64)[0]
    out.append(f"{rt}:{'D' if diffusive(Pi) else '-'}({Pi[0,3]:+.1e})")
print(" W3:", " ".join(out))
# first-order criterion: d Pi_tilde/d eta = -S Y S  (finite difference)
qr = 0.25; M = drift(K3, 2, 0.1, 0.2, 0.1, 0.05)
D = np.diag([1, 1, 1, math.sqrt(qr)]); Di = np.linalg.inv(D)
S = Di @ M @ D
assert np.allclose(S, S.T)
E = np.zeros((4, 4)); E[3, 3] = 2.0
Y = lyap(S, E)
h = 1e-5
fd = (D @ precision(M, 1.0, (1 + h) * qr)[0] @ D - D @ precision(M, 1.0, (1 - h) * qr)[0] @ D) / (2 * h)
print(" first-order formula dPi~/deta = -SYS: max abs err", np.abs(fd + S @ Y @ S).max(), " (SYS)_oz =", (S @ Y @ S)[2, 3], " (SYS d)_z =", (S @ Y @ S @ Di @ np.ones(4))[3])
# O1 probe (numerical only): asymmetric graphs with an uncoupled member pair, sign of (SYS)_ij
neg = 0; tot = 0; smallest = np.inf
for trial in range(4000):
    n = int(rng.integers(2, 5)); m = int(rng.integers(1, 5)); N = n + m
    A = 10 ** rng.uniform(-3, 2.5, (N, N)); A = (A + A.T) / 2; np.fill_diagonal(A, 0)
    A *= (rng.uniform(size=(N, N)) < 0.6); A = np.maximum(A, A.T)
    A[0, 1] = A[1, 0] = 0.0
    A[0, n] = A[n, 0] = float(10 ** rng.uniform(-3, 2.5))
    e, b, w = (10 ** rng.uniform(-3, 1.5, 3)).tolist(); d = float(10 ** rng.uniform(-3, 1.5)) * (trial % 2)
    M = drift(A, n, e, b, w, d); qr = w / (n * b)
    D = np.diag([1.0] * N + [math.sqrt(qr)]); S = np.linalg.inv(D) @ M @ D
    E = np.zeros((N + 1, N + 1)); E[N, N] = 2.0
    v = (S @ lyap(S, E) @ S)[0, 1]
    tot += 1; neg += v <= 0; smallest = min(smallest, v / np.abs(S).max())
print(f" O1 probe: (SYS)_01 <= 0 in {neg} of {tot} random asymmetric instances (min scaled value {smallest:.2e}); numerical observation only")

print("== C5. marginal ==")
A3 = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 0.0]])
M = drift(A3, 2, 0.1, 0.2, 0.1, 0.01)
out = []
for rt in (0, 0.5, 1, 2, 10):
    Sig = precision(M, 1.0, rt * 0.25)[1]
    out.append(f"{rt}:{'D' if diffusive(np.linalg.inv(Sig[:3, :3])) else '-'}")
print(" W4 path 0-2-1 marginal:", " ".join(out))
N = 3; qr = 0.25
Msch = M[:N, :N] - np.outer(M[:N, N], M[N, :N]) / M[N, N]
print(" Pi_marg(q_rev) = M_schur/q: err", np.abs(np.linalg.inv(precision(M, 1.0, qr)[1][:N, :N]) - Msch).max())
D = np.diag([1, 1, 1, math.sqrt(qr)]); S = np.linalg.inv(D) @ M @ D
E = np.zeros((4, 4)); E[3, 3] = 2.0; Y = lyap(S, E)
fd = (np.linalg.inv(precision(M, 1.0, (1 + h) * qr)[1][:N, :N]) - np.linalg.inv(precision(M, 1.0, (1 - h) * qr)[1][:N, :N])) / (2 * h)
print(" d Pi_marg/d eta = -M_schur Y_VV M_schur: err", np.abs(fd + Msch @ Y[:N, :N] @ Msch).max())

print("== C6. weighted contrast ==")


def contrast_w(P, w, S):
    S = list(S); out = [v for v in range(P.shape[0]) if v not in S]
    sub = P[np.ix_(S, S)]; ws = w[S]
    cutv = -P[np.ix_(S, out)].sum(1) if out else np.zeros(len(S))
    Min = sub - np.diag(cutv)
    xout = sub.sum() / ws.sum()
    # generalized problem on the W-orthogonal complement of 1
    sw = np.sqrt(ws); B = np.linalg.qr(np.column_stack([sw, np.eye(len(S))[:, 1:]]))[0][:, 1:]
    Mt = np.diag(1 / sw) @ Min @ np.diag(1 / sw)
    return np.linalg.eigvalsh(B.T @ Mt @ B).min() / xout


worst = 0
for trial in range(200):
    n = int(rng.integers(2, 6)); m = int(rng.integers(0, 4)); N = n + m
    A = 10 ** rng.uniform(-1.5, 1, (N, N)); A = (A + A.T) / 2; np.fill_diagonal(A, 0)
    e, b, w_ = (10 ** rng.uniform(-2, 0.7, 3)).tolist(); d = float(10 ** rng.uniform(-2, 0.7)) * (trial % 2); qq = 0.7
    M = drift(A, n, e, b, w_, d); qr = w_ * qq / (n * b)
    Qv = np.array([qq] * N + [qr]); Pi = M / Qv[:, None]
    assert np.allclose(Pi, Pi.T)
    Rr = b / w_
    lam2 = np.sort(np.linalg.eigvalsh(np.diag(A[:n, :n].sum(1)) - A[:n, :n]))[1]
    cutC = A[:n, n:].sum()
    pred = (1 + Rr) * min(e + b + lam2, b + w_ + (e * Rr + d) / (1 + Rr)) / (e + Rr * d + cutC / n)
    got = contrast_w(Pi, 1 / Qv, list(range(n)) + [N])
    worst = max(worst, abs(pred - got) / pred)
print(f" r_W(C') formula: max rel err {worst:.1e} over 200 random instances")
print(" planted (drop the 1+R prefactor) rel err on last instance:", abs(pred / (1 + Rr) - got) / got)

print("== C7(4). typed-graph baselines ==")


def typed_medium(nring, abar, bbar, eps):
    NV = 2 * nring
    A = np.zeros((NV, NV)); A[:nring, :nring] = ring(nring, abar); A[nring:, nring:] = ring(nring, abar)
    for i in range(nring):
        A[i, nring + i] = A[nring + i, i] = abar
    Pi = np.zeros((NV + 1, NV + 1))
    Pi[:NV, :NV] = (eps + bbar) * np.eye(NV) + np.diag(A.sum(1)) - A
    Pi[:NV, NV] = Pi[NV, :NV] = -bbar
    Pi[NV, NV] = NV * bbar
    return Pi


Ph = typed_medium(8, 41 / 60, 0.1, 0.02)
print(" 17-node medium: r_hom(V u {z}) =", round(contrast(Ph, range(17)), 4), " (note: 27.6403); r(C') = 12.9501")
for e in (0.05, 0.20, 0.50):
    Ph = typed_medium(4, 41 / 60, 0.2, e)
    best = max((contrast(Ph, S), S) for k in range(2, 10) for S in itertools.combinations(range(9), k))
    Aact = np.zeros((8, 8)); Aact[:4, :4] = ring(4); Aact[4:, 4:] = ring(4)
    for i in range(4):
        Aact[i, 4 + i] = Aact[4 + i, i] = 0.05
    Pa = np.zeros((9, 9)); Pa[:8, :8] = e * np.eye(8) + np.diag(Aact.sum(1)) - Aact
    Pa[:4, :4] += 0.4 * np.eye(4); Pa[:4, 8] = Pa[8, :4] = -0.4; Pa[8, 8] = 1.6
    print(f" 9-node eps={e}: r(C')={contrast(Pa,[0,1,2,3,8]):.4f}  baseline={best[0]:.4f} attained by {best[1]}")
