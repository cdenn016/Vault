"""Independent exact checks for open_prv_aware (reviewer script, covariance-form only).

All quantities are exact rationals (sympy). The posterior-mean gain rows are computed
by brute-force joint-Gaussian conditioning of X=(x_1..x_T) on the observations; no J_D,
no Phi(U) formula is used except in Part 2, where the note's Phi(U) is the object tested.
"""
import sympy as sp
from sympy import Matrix, Rational as Rat, eye, zeros


def state_cov(A, Q, P0, T):
    d = A.rows
    P = []
    Pc = P0
    for _ in range(T):
        Pc = A * Pc * A.T + Q
        P.append(Pc)
    S = zeros(T * d, T * d)
    for s in range(T):
        Ap = eye(d)
        for t in range(s, T):
            if t > s:
                Ap = A * Ap
            blk = Ap * P[s]
            S[t * d:(t + 1) * d, s * d:(s + 1) * d] = blk
            S[s * d:(s + 1) * d, t * d:(t + 1) * d] = blk.T
    return S


def gains(A, Q, P0, Hs, Rs, D, tq, T=None):
    """Return (gain matrix d x sum p, column slices per key, posterior cov of x_tq, full post cov of X)."""
    d = A.rows
    if T is None:
        T = max([tq] + [tau for (_, tau) in D])
    S = state_cov(A, Q, P0, T)
    rows, sl, off = [], {}, 0
    for (j, tau) in D:
        H = Hs[j]
        C = zeros(H.rows, T * d)
        C[:, (tau - 1) * d:tau * d] = H
        rows.append(C)
        sl[(j, tau)] = (off, off + H.rows)
        off += H.rows
    C = Matrix.vstack(*rows)
    Rbig = zeros(off, off)
    for (j, tau) in D:
        a, b = sl[(j, tau)]
        Rbig[a:b, a:b] = Rs[j]
    Syy = C * S * C.T + Rbig
    Syy_inv = Syy.inv(method="LU")
    SXy = S * C.T
    Gfull = SXy * Syy_inv                 # (T d) x obs
    post = S - Gfull * SXy.T
    G = Gfull[(tq - 1) * d:tq * d, :]
    return G, sl, post


def cols(G, sl, keys):
    return Matrix.hstack(*[G[:, sl[k][0]:sl[k][1]] for k in keys])


def pad(row_block, total_cols):
    out = zeros(row_block.rows, total_cols)
    out[:, :row_block.cols] = row_block
    return out


print("=== Part 1: C3 counterexample (d=1, all parameters 1) ===")
one = Matrix([[1]])
Hs, Rs = {1: one, 2: one}, {1: one, 2: one}
G2, sl2, post2 = gains(one, one, one, Hs, Rs, [(1, 1), (1, 2)], 2)
G3, sl3, post3 = gains(one, one, one, Hs, Rs, [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3)], 3)
w2 = cols(G2, sl2, [(1, 1), (1, 2)])
w3 = cols(G3, sl3, [(1, 1), (1, 2)])
M = Matrix.vstack(w2, w3)
print("  t=2 weights", list(w2), "var", post2[1, 1])
print("  t=3 weights", list(w3), "var", post3[2, 2])
print("  det", M.det(), "rank", M.rank())
assert list(w2) == [Rat(1, 4), Rat(5, 8)] and list(w3) == [Rat(2, 45), Rat(7, 45)]
assert M.det() == Rat(1, 90) and post2[1, 1] == Rat(5, 8) and post3[2, 2] == Rat(26, 45)
Gs, sls, _ = gains(one, one, one, Hs, Rs, [(1, 1), (1, 2), (2, 1), (2, 2)], 2)
ws = cols(Gs, sls, [(1, 1), (1, 2)])
print("  synchronized t=2 weights", list(ws), " det vs t=3 row:", Matrix.vstack(ws, w3).det())
assert list(ws) == [Rat(2, 19), Rat(7, 19)] and Matrix.vstack(ws, w3).det() == 0

print("=== Part 2: C1(a) Markov factorization, d=2, a=2, b=5, partial-rank other member ===")
A = Matrix([[1, 1], [-1, 2]]) / 2
Q = Matrix([[2, 1], [1, 2]]) / 3
P0 = Matrix([[2, 1], [1, 3]])
Hs = {0: eye(2), 1: Matrix([[1, 2]]), 2: Matrix([[1, 0], [1, 1]])}
Rs = {0: eye(2), 1: Matrix([[2]]), 2: Matrix([[2, 1], [1, 2]])}
Lam = {j: Hs[j].T * Rs[j].inv() * Hs[j] for j in Hs}
a, b, d = 2, 5, 2
W = [3, 4, 5]
U = [(0, 3), (0, 4), (1, 1), (1, 2), (1, 4), (2, 2), (2, 3)]          # D_{<b}
Dge = [(0, 5), (1, 5), (2, 6), (1, 7)]
D = U + Dge


def phi_note(U, drop_term=False):
    """Phi(U) as defined in the note's Conventions table (member 0 has H=I,R=I so ledger = raw obs)."""
    Upre = [(j, t) for (j, t) in U if t <= a]
    if Upre:
        _, _, post = gains(A, Q, P0, Hs, Rs, Upre, a, T=a)
        Pa = post[(a - 1) * d:a * d, (a - 1) * d:a * d]
    else:
        Pa = state_cov(A, Q, P0, a)[(a - 1) * d:a * d, (a - 1) * d:a * d]
    Qi = Q.inv()
    m = b - 1 - a
    K = zeros(m * d, m * d)
    K[:d, :d] = (A * Pa * A.T + Q).inv()
    for t in range(m - 1):
        K[t * d:(t + 1) * d, t * d:(t + 1) * d] += A.T * Qi * A
        K[t * d:(t + 1) * d, (t + 1) * d:(t + 2) * d] -= A.T * Qi
        K[(t + 1) * d:(t + 2) * d, t * d:(t + 1) * d] -= Qi * A
        K[(t + 1) * d:(t + 2) * d, (t + 1) * d:(t + 2) * d] += Qi
    for (j, t) in U:
        if a < t < b:
            i = t - a - 1
            K[i * d:(i + 1) * d, i * d:(i + 1) * d] += Lam[j]
    if not drop_term:
        K[(m - 1) * d:m * d, (m - 1) * d:m * d] += A.T * Qi * A
    Ki = K.inv()
    Phi = zeros(d, (m + 1) * d)
    Phi[:, :m * d] = Qi * A * Ki[(m - 1) * d:m * d, :]
    Phi[:, m * d:] = eye(d)
    return Phi


Phi = phi_note(U)
Phi_bad = phi_note(U, drop_term=True)
ok, bad = True, False
for tq in [5, 6, 7]:
    Dt = [(j, t) for (j, t) in D if t <= tq]
    G, sl, post = gains(A, Q, P0, Hs, Rs, Dt, tq)
    Mdt = cols(G, sl, [(0, t) for t in W])        # ledger coords = raw obs for member 0
    Ctb = post[(tq - 1) * d:tq * d, (b - 1) * d:b * d]
    ok = ok and (Mdt - Ctb * Phi) == zeros(d, len(W) * d)
    bad = bad or (Mdt - Ctb * Phi_bad) != zeros(d, len(W) * d)
    assert Ctb.det() != 0
print("  exact identity M_{D,t} = Cov(x_t,x_b|o_D) Phi(D_<b) for t=5,6,7:", ok)
print("  planted error (drop A^T Q^-1 A at b-1) detected:", bad)
assert ok and bad

print("=== Part 3: C4 block-Krylov, d=2, k=4, proportional full-rank sensing, s=1..5 ===")
Hc = Matrix([[1, 1], [0, 2]])
alphas = [1, 2, 3, 5, 7]
Hs4 = {j: Hc for j in range(5)}
Rs4 = {j: eye(2) / alphas[j] for j in range(5)}
k = 4
stack, ranks = [], []
for s in range(1, 6):
    Dset = [(j, t) for j in range(s) for t in range(1, k)] + [(0, k)]
    G, sl, _ = gains(A, Q, P0, Hs4, Rs4, Dset, k)
    stack.append(cols(G, sl, [(0, t) for t in range(1, k + 1)]))
    ranks.append(Matrix.vstack(*stack).rank())
print("  ranks s=1..5:", ranks, " expected", [min(s, k) * 2 for s in range(1, 6)])
assert ranks == [2, 4, 6, 8, 8]
# planted error: claim min(s,k)*d still holds when the c_r coincide (two identical configurations)
dup = Matrix.vstack(stack[0], stack[0], stack[1]).rank()
print("  control with a repeated configuration (s=3 rows, 2 distinct c):", dup, "(not 6)")
assert dup == 4

print("=== Part 4: C6 round-robin in true steady state (a=k), from the actual schedule ===")


def round_robin_rank(d, k, phases, Hs, Rs, Aq, Qq, Pq, period_index=1):
    n = len(phases)
    a = period_index * k
    b = a + k
    rows = []
    for t in range(b, b + k):
        Dt = []
        for j, ph in enumerate(phases):
            last = max(r for r in range(ph, t + 1, k)) if t >= ph else 0
            Dt += [(j, tau) for tau in range(1, last + 1)]
        G, sl, _ = gains(Aq, Qq, Pq, Hs, Rs, Dt, t)
        rows.append(cols(G, sl, [(n - 1, tau) for tau in range(a + 1, b + 1)]))
    return Matrix.vstack(*rows).rank()


one = Matrix([[1]])
half = Matrix([[Rat(1, 2)]])
for phases, exp_p in [((1, 2, 4), 2), ((1, 3, 4), 1), ((3, 4), 0), ((1, 2, 3, 4), 2)]:
    n = len(phases)
    Hs1 = {j: one for j in range(n)}
    Rs1 = {j: Matrix([[j + 1]]) for j in range(n)}
    rk = round_robin_rank(1, 4, phases, Hs1, Rs1, Matrix([[Rat(9, 10)]]), half, one)
    print(f"  d=1,k=4,phases={phases}: rank={rk}, (p+1)d={(exp_p + 1)}")
    assert rk == exp_p + 1
Hs2 = {0: eye(2), 1: Matrix([[1, 1], [0, 1]]), 2: Matrix([[2, 0], [1, 1]])}
Rs2 = {0: eye(2), 1: Matrix([[2, 1], [1, 2]]), 2: eye(2) * 3}
rk = round_robin_rank(2, 3, (1, 2, 3), Hs2, Rs2, A, Q, P0)
print(f"  d=2,k=3,n=3,phases=(1,2,3): rank={rk}, (p+1)d=(1+1)*2=4, blind kd=6")
assert rk == 4

print("=== Part 5: Bernoulli member 2 in steady state (a=3>0): pre-window variation ===")
Hs5 = {0: eye(2), 1: Matrix([[1, 2]])}
Rs5 = {0: eye(2), 1: Matrix([[2]])}
a, k = 3, 4
b = a + k
rows_all, rows_nopre = [], []
for u in range(0, b):
    Dt = [(0, t) for t in range(1, b + 1)] + [(1, t) for t in range(1, u + 1)]
    G, sl, _ = gains(A, Q, P0, Hs5, Rs5, Dt, b)
    r = cols(G, sl, [(0, t) for t in range(a + 1, b + 1)])
    rows_all.append(r)
    if u >= a:
        rows_nopre.append(r)
r_all = Matrix.vstack(*rows_all).rank()
r_nopre = Matrix.vstack(*rows_nopre).rank()
print(f"  d=2,r1=2,r2=1,k=4: rank with u in {{a..b-1}} = {r_nopre} (C5(a) formula d+(k-1)r2 = 5)")
print(f"                     rank with u in {{0..b-1}} = {r_all} (C2 bound d+rankA+(k-2)r2 = 6, blind 8)")

print("=== Part 6: late arrivals older than one reporting period (cross-window accounting) ===")
Hs6, Rs6 = {1: one, 2: one}, {1: one, 2: one}
own = lambda upto: [(1, t) for t in range(1, upto + 1)]
sched = {3: own(3), 4: own(3), 5: own(3), 6: own(6), 7: own(6) + [(2, 1)], 8: own(6) + [(2, 1), (2, 2)]}
rows = {}
for t, Dt in sched.items():
    G, sl, _ = gains(one, one, one, Hs6, Rs6, Dt, t)
    keys = [kk for kk in own(6) if kk in sl]
    rows[t] = pad(cols(G, sl, keys), 6)
R = lambda ts, c0, c1: Matrix.vstack(*[rows[t][:, c0:c1] for t in ts]).rank()
r1_trunc = R([3, 4, 5], 0, 3)
r1_full = R([3, 4, 5, 6, 7, 8], 0, 3)
r2 = R([6, 7, 8], 3, 6)
joint = R([3, 4, 5, 6, 7, 8], 0, 6)
print(f"  r*(W1; evaluations before next report) = {r1_trunc}")
print(f"  r*(W1; all evaluations t=3..8)         = {r1_full}")
print(f"  r*(W2; evaluations t=6..8)             = {r2}")
print(f"  rank of all rows on the six observations (total transcript needed) = {joint}")
print(f"  => truncated per-window sum {r1_trunc + r2} < {joint} <= single-transmission sum {r1_full + r2}")
print("ALL REVIEWER CHECKS FOR prv_aware COMPLETED.")
