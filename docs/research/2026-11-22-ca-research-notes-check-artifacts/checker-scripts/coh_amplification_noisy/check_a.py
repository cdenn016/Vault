"""Independent check of C1-C3 of open_coh_amplification_noisy.md (fresh-context reviewer script).
World-coordinate operators are built from the manuscript definition A_ji = P_j H_i^T (H_i P_j H_i^T + R_i)^{-1} H_i only.
"""
import numpy as np, scipy.linalg as la, sympy as sp
from fractions import Fraction as Fr

rng = np.random.default_rng(7)

def spd(k, rng, scale=1.0):
    M = rng.standard_normal((k, k)); return scale * (M @ M.T + 0.2 * np.eye(k))

def edge(Pj, Hi, Ri):
    S = Hi @ Pj @ Hi.T + Ri
    return Pj @ Hi.T @ la.solve(S, Hi)

def msqrt(X):
    w, V = la.eigh(X); return (V * np.sqrt(w)) @ V.T

def build_T(As, K, order=None):
    """As[k] = A_{k,k-1} (0-indexed agent k reads agent k-1). sync if order None, else sequential sweep."""
    N = len(As)
    if order is None:
        T = np.zeros((N*K, N*K))
        for k in range(N):
            km = (k-1) % N
            T[k*K:(k+1)*K, k*K:(k+1)*K] = np.eye(K) - As[k]
            T[k*K:(k+1)*K, km*K:(km+1)*K] += As[k]
        return T
    T = np.eye(N*K)
    for k in order:
        km = (k-1) % N
        St = np.eye(N*K)
        St[k*K:(k+1)*K, k*K:(k+1)*K] = np.eye(K) - As[k]
        St[k*K:(k+1)*K, km*K:(km+1)*K] += As[k]
        T = St @ T
    return T

rho = lambda M: float(max(abs(la.eigvals(M))))

# ---------------------------------------------------------------- C1 exact
print("[C1] exact rational recomputation (sympy), plus the persistent operators T_seq/T_sync on the same instances")
def em(P, h, R):
    S = (h * P * h.T)[0, 0] + R
    return P * h.T * h / S
h1 = sp.Matrix([[0, 1]]); h2 = sp.Matrix([[1, 0]])
inst = {
 "a":  (sp.Matrix([[1, sp.Rational(3,2)],[sp.Rational(3,2),4]]), sp.Matrix([[4, sp.Rational(3,2)],[sp.Rational(3,2),1]]), sp.Rational(1,2), sp.Integer(2)),
 "a'": (sp.Matrix([[1,3],[3,10]]), sp.Matrix([[100,25],[25,7]]), sp.Integer(10), sp.Integer(100)),
 "b":  (sp.Matrix([[1,2],[2,5]]), sp.Matrix([[5,-2],[-2,1]]), sp.Rational(2,3), sp.Integer(1)),
}
for name, (P1, P2, R1, R2) in inst.items():
    A21 = em(P2, h1, R1); A12 = em(P1, h2, R2)
    Ac = A12 * A21
    bar1 = sp.eye(2) - A12 + Ac; bar2 = sp.eye(2) - A21 + A21 * A12
    s21 = (h1*P2*h1.T)[0,0] / ((h1*P2*h1.T)[0,0] + R1); s12 = (h2*P1*h2.T)[0,0] / ((h2*P1*h2.T)[0,0] + R2)
    tau = Ac.trace() / (s21 * s12)
    # edge ratios r_e = X_ii / S_ji
    r12 = (h1*P1*h1.T)[0,0] / ((h1*P2*h1.T)[0,0] + R1); r21 = (h2*P2*h2.T)[0,0] / ((h2*P1*h2.T)[0,0] + R2)
    Asn = [np.array(A12, dtype=float), np.array(A21, dtype=float)]   # agent0=1 reads agent1=2 ; agent1=2 reads agent0=1
    Tsy = build_T(Asn, 2); Tse = build_T(Asn, 2, order=[1, 0])
    print(f"  C1({name}): spec(A_c)={sorted(Ac.eigenvals().keys())} spec(barA^1)={sorted(bar1.eigenvals().keys())} spec(barA^2)={sorted(bar2.eigenvals().keys())}")
    print(f"           tau_circ={tau}  edge ratios r_(1->2)={r12}, r_(2->1)={r21}  rho(T_sync)={rho(Tsy):.6f} rho(T_seq)={rho(Tse):.6f}")
    if name == "a'":
        # direct simulation of the manuscript's sequential story dynamics (proof of thm (b)) with retained own term
        x = np.zeros(4); x[:2] = [1.0, 0.3]
        norms = []
        for n in range(200):
            x = Tse @ x; norms.append(np.linalg.norm(x[:2]))
        print(f"           simulated growth factor per circulation (n=150..200): {(norms[199]/norms[149])**(1/50):.6f}; level-1 header R_i = X_ii exactly, rho(A_c)={float(max(abs(e) for e in Ac.eigenvals())):.6f}")

# ---------------------------------------------------------------- C2
print("[C2] coded reduction + bound; includes r_N = K, unequal ranks, singular/zero noises, N = 2")
maxspec = 0.0; viol = 0; violmid = 0; planted = 0; planted2 = 0; n_full = 0; n_zero = 0; maxratio = 0
for t in range(4000):
    K = int(rng.integers(2, 5)); N = int(rng.integers(2, 5))
    ranks = [int(rng.integers(1, K+1)) for _ in range(N)]
    Ps = [spd(K, rng, 10**rng.uniform(-1.5, 1.5)) for _ in range(N)]
    Hs = [rng.standard_normal((ranks[i], K)) for i in range(N)]
    Rs = []
    for i in range(N):
        u = rng.uniform()
        if u < 0.15: Rs.append(np.zeros((ranks[i], ranks[i]))); n_zero += 1
        elif u < 0.3:
            v = rng.standard_normal((ranks[i], 1)); Rs.append(v @ v.T)        # singular psd
        else: Rs.append(spd(ranks[i], rng, 10**rng.uniform(-1.5, 1.5)))
    As = [edge(Ps[(i+1) % N], Hs[i], Rs[i]) for i in range(N)]              # As[i] = A_{i+1,i}
    pref = np.eye(K)
    for i in range(N-1): pref = As[i] @ pref
    Ac = As[N-1] @ pref
    bar = np.eye(K) - As[N-1] + Ac
    HN = Hs[N-1]; rN = ranks[N-1]; n_full += (rN == K)
    X1N = HN @ Ps[0] @ HN.T; S1N = X1N + Rs[N-1]
    Xh = msqrt(X1N); Xmh = la.inv(Xh)
    Sig = Xh @ la.solve(S1N, Xh)
    C = Xmh @ HN @ pref @ Ps[0] @ HN.T @ Xmh
    Mrt = np.eye(rN) - Sig + Sig @ C
    e1 = np.sort_complex(la.eigvals(bar)); e2 = np.sort_complex(np.append(la.eigvals(Mrt), np.ones(K - rN)))
    maxspec = max(maxspec, float(np.max(np.abs(e1 - e2))))
    Sh = msqrt(Sig); Mhat = la.solve(Sh, Mrt @ Sh)
    nC = la.norm(C, 2); nM = la.norm(Mhat, 2)
    if nM > max(1, nC) * (1 + 1e-9): violmid += 1
    res = []; snrf = []
    for i in range(N):
        j = (i+1) % N
        Xji = Hs[i] @ Ps[j] @ Hs[i].T; Xii = Hs[i] @ Ps[i] @ Hs[i].T; S = Xji + Rs[i]
        res.append(max(la.eigvalsh(Xii, S))); snrf.append(max(la.eigvalsh(Xji, S)))
    rcirc = max(la.eigvalsh(HN @ Ps[N-1] @ HN.T, X1N))
    prod = np.sqrt(rcirc) * np.prod([np.sqrt(res[i]*snrf[i]) for i in range(N-1)])
    b = max(1.0, prod); r_ = rho(bar)
    if r_ > b * (1 + 1e-9): viol += 1
    if prod > 1: maxratio = max(maxratio, r_/b)
    # planted errors: (i) drop the return-edge factor r^circ entirely; (ii) forget the max{1,.}
    if r_ > max(1.0, prod/np.sqrt(rcirc)) * (1 + 1e-6): planted += 1
    if rN < K and r_ > prod * (1 + 1e-6): planted2 += 1
print(f"  spec(barA) vs spec(M_rt) U {{1}}: max discrepancy {maxspec:.2e}; trials with r_N=K: {n_full}; zero-noise edges: {n_zero}")
print(f"  violations of final bound: {viol}/4000; violations of ||Mhat|| <= max(1,||C||): {violmid}/4000; max rho/bound when bound>1: {maxratio:.4f}")
print(f"  planted (drop r^circ factor): violated {planted} times; planted (drop max with 1): violated {planted2} times")

# ---------------------------------------------------------------- C3
print("[C3(1)] exact dissipation identities on arbitrary data, and rho<=1 in WORLD coordinates under heterogeneous r^circ<=1")
maxid = 0.0
for t in range(2000):
    r = int(rng.integers(1, 4)); z = rng.standard_normal(r); y = rng.standard_normal(r)
    Rk = spd(r, rng, 10**rng.uniform(-2, 2)) if rng.uniform() > 0.2 else np.zeros((r, r))
    Sig = la.inv(np.eye(r) + Rk); zp = (np.eye(r) - Sig) @ z + Sig @ y; d = zp - z
    G = np.eye(r) + Rk
    lhs1 = zp @ G @ zp - z @ G @ z; rhs1 = y @ y - z @ z - d @ (Rk + Rk @ Rk) @ d
    lhs2 = zp @ Rk @ zp - z @ Rk @ z; rhs2 = y @ y - zp @ zp - d @ (Rk + Rk @ Rk) @ d
    sc = 1 + abs(lhs1) + abs(rhs1)
    maxid = max(maxid, abs(lhs1 - rhs1)/sc, abs(lhs2 - rhs2)/sc)
    # planted: wrong sign on the R^2 term
print(f"  max relative residual of the two identities (2000 random draws): {maxid:.2e}")
bad_sync = bad_seq = 0; mx = 0; cnt = 0; maxr0 = 0; specerr = 0; inv_res = 0; mxV = 0
for t in range(1500):
    N = int(rng.integers(2, 4)); r = int(rng.integers(1, 3)); K = N * r + int(rng.integers(0, 2))
    base = spd(K, rng, 3.0) + 3*np.eye(K)
    blocks = [0.9 * spd(r, rng, 0.3) for _ in range(N)]
    Ps = [base.copy()]
    for i in range(N-1):
        D = np.zeros((K, K)); a = i; b = (i+1) % N
        D[a*r:(a+1)*r, a*r:(a+1)*r] += blocks[a]; D[b*r:(b+1)*r, b*r:(b+1)*r] -= blocks[b]
        Ps.append(Ps[-1] + D)
    if min(min(la.eigvalsh(P)) for P in Ps) <= 1e-3: continue
    Hs = []
    for i in range(N):
        H = np.zeros((r, K)); H[:, i*r:(i+1)*r] = np.eye(r); Hs.append(H)
    Gm = rng.standard_normal((K, K)) + 2*np.eye(K); Gi = la.inv(Gm)
    Ps = [Gm @ P @ Gm.T for P in Ps]; Hs = [H @ Gi for H in Hs]
    r0 = [max(la.eigvalsh(Hs[i] @ Ps[i] @ Hs[i].T, Hs[i] @ Ps[(i+1) % N] @ Hs[i].T)) for i in range(N)]
    if max(r0) > 1 + 1e-9: continue
    cnt += 1; maxr0 = max(maxr0, max(r0))
    Rs = [spd(r, rng, 10**rng.uniform(-2, 2)) if rng.uniform() > 0.2 else np.zeros((r, r)) for _ in range(N)]
    As = [edge(Ps[k], Hs[(k-1) % N], Rs[(k-1) % N]) for k in range(N)]   # As[k] = A_{k,k-1}
    Tsy = build_T(As, K); Tse = build_T(As, K, order=list(range(1, N)) + [0])
    a_, b_ = rho(Tsy), rho(Tse); mx = max(mx, a_, b_)
    # restriction to the invariant subspace (+)_k col(P_k H_{k-1}^T), computed from the world operator
    Bb = np.zeros((N*K, N*r))
    for k in range(N): Bb[k*K:(k+1)*K, k*r:(k+1)*r] = Ps[k] @ Hs[(k-1) % N].T
    Bp = la.pinv(Bb)
    for Tm, tag in ((Tsy, 'sync'), (Tse, 'seq')):
        TV = Bp @ Tm @ Bb
        inv_res = max(inv_res, la.norm(Tm @ Bb - Bb @ TV) / la.norm(Tm @ Bb))
        mxV = max(mxV, rho(TV))
    bad_sync += a_ > 1 + 1e-7; bad_seq += b_ > 1 + 1e-7
print(f"  heterogeneous-prior cycles with all r^circ_e <= 1 (max r^circ {maxr0:.4f}, distinct priors): {cnt}; rho(T_sync)>1: {bad_sync}; rho(T_seq)>1: {bad_seq}; max rho {mx:.10f}")
print(f"  restricted to the invariant subspace: invariance residual {inv_res:.2e}; max rho(T|V) over both operators {mxV:.10f} (other eigenvalues are exactly 1 by block-triangularity)")

print("[C3(2)] rank-one characteristic polynomials: all coefficients, N = 2..6, world-coordinate operators")
maxc = 0.0; maxc_planted = 0.0; pos_fail = 0; npos = 0; small_fail = 0; nsmall = 0; neg_stable = 0; neg_unstable = 0
for t in range(3000):
    K = int(rng.integers(2, 4)); N = int(rng.integers(2, 7))
    Ps = [spd(K, rng, 10**rng.uniform(-1, 1)) for _ in range(N)]
    hs = [rng.standard_normal((1, K)) for _ in range(N)]
    Rs = [np.array([[10**rng.uniform(-2, 2)]]) if rng.uniform() > 0.15 else np.zeros((1, 1)) for _ in range(N)]
    As = [edge(Ps[k], hs[(k-1) % N], Rs[(k-1) % N]) for k in range(N)]
    s = [(hs[(k-1) % N] @ Ps[k] @ hs[(k-1) % N].T).item() for k in range(N)]
    s = [s[k] / (s[k] + Rs[(k-1) % N].item()) for k in range(N)]
    Ac = np.eye(K)
    for k in list(range(1, N)) + [0]: Ac = As[k] @ Ac
    trA = float(np.trace(Ac)); tau = trA / np.prod(s)
    Tsy = build_T(As, K); Tse = build_T(As, K, order=list(range(1, N)) + [0])
    base = np.poly(np.array([1 - sk for sk in s]))            # prod (lam - (1-s_k))
    psync = base.copy(); psync[-1] -= trA
    pseq = base.copy(); pseq[1] -= trA                        # coefficient of lam^{N-1}
    unit = np.poly(np.ones(N*K - N))                          # the (K-1)N unit eigenvalues
    full_sync = np.polymul(psync, unit); full_seq = np.polymul(pseq, unit)
    c1 = np.poly(Tsy); c2 = np.poly(Tse)
    sc = 1 + np.max(np.abs(c1)); sc2 = 1 + np.max(np.abs(c2))
    maxc = max(maxc, np.max(np.abs(c1 - full_sync))/sc, np.max(np.abs(c2 - full_seq))/sc2)
    pl = base.copy(); pl[2 if N > 2 else 0] -= trA             # planted: lam^{N-2} instead of lam^{N-1}
    maxc_planted = max(maxc_planted, np.max(np.abs(c2 - np.polymul(pl, unit)))/sc2)
    rs, rq = rho(Tsy), rho(Tse)
    if tau > 1 + 1e-9:
        npos += 1; pos_fail += (rs <= 1 + 1e-12) or (rq <= 1 + 1e-12)
    elif abs(tau) <= 1:
        nsmall += 1; small_fail += (rs > 1 + 1e-7) or (rq > 1 + 1e-7)
    elif tau < -1:
        if rs <= 1 + 1e-9 and rq <= 1 + 1e-9: neg_stable += 1
        else: neg_unstable += 1
print(f"  max relative coefficient error (true formulas): {maxc:.2e}; with planted lam^(N-2) error: {maxc_planted:.2e}")
print(f"  tau>1: {npos} draws, failures of rho>1: {pos_fail};  |tau|<=1: {nsmall} draws, failures of rho<=1: {small_fail}")
print(f"  tau<-1 (not covered by C3): both operators stable in {neg_stable} draws, at least one unstable in {neg_unstable} draws")
