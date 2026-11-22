"""Independent check of C1 (conj_agy_synchronous.md).
(A) Exact rational check of the residual identity (Steps 2-3) on arbitrary full-support laws, n=2,3,4.
(B) Step 1: second difference of G_C equals conditional MI computed directly from the joint
    law of discrete slot outcomes (not from G differences), incl. XOR and random models.
(C) Planted-error controls.
(D) Extremes: n=2, gamma->0, gamma large, zero redundancy.
"""
from fractions import Fraction as Fr
from itertools import product
import random, math
import numpy as np

random.seed(7)


def rand_law(shape):
    w = {s: Fr(random.randint(1, 50)) for s in product(*[range(m) for m in shape])}
    Z = sum(w.values())
    return {s: v / Z for s, v in w.items()}


def cond(P, shape, i):
    K = {}
    for s in P:
        key = s[:i] + (None,) + s[i + 1:]
        K.setdefault(key, [Fr(0)] * shape[i])
        K[key][s[i]] += P[s]
    for key in K:
        tot = sum(K[key])
        K[key] = [v / tot for v in K[key]]
    return K


def one_step_pair00(P, shape, i, j):
    Ki, Kj = cond(P, shape, i), cond(P, shape, j)
    tot = Fr(0)
    for s, p in P.items():
        tot += p * Ki[s[:i] + (None,) + s[i + 1:]][0] * Kj[s[:j] + (None,) + s[j + 1:]][0]
    return tot


def rhs_formula(P, shape, i, j, variant="correct"):
    n = len(shape)
    others = [k for k in range(n) if k not in (i, j)]
    tot = Fr(0)
    for c in product(*[range(shape[k]) for k in others]):
        def idx(a, b):
            s = [None] * n
            s[i], s[j] = a, b
            for k, v in zip(others, c):
                s[k] = v
            return tuple(s)
        pc_un = {(a, b): P[idx(a, b)] for a in range(shape[i]) for b in range(shape[j])}
        Pc = sum(pc_un.values())
        pc = {k: v / Pc for k, v in pc_un.items()}
        r = [sum(pc[(a, b)] for b in range(shape[j])) for a in range(shape[i])]
        s_ = [sum(pc[(a, b)] for a in range(shape[i])) for b in range(shape[j])]
        chi2 = sum((pc[(a, b)] - r[a] * s_[b]) ** 2 / (r[a] * s_[b])
                   for a in range(shape[i]) for b in range(shape[j]))
        extra = Fr(0)
        for a in range(shape[i]):
            for b in range(shape[j]):
                # equals e^{gamma I_c(a,b)} when P is a group posterior (Step 1)
                expfac = pc[(a, 0)] * pc[(0, b)] / (pc[(0, 0)] * pc[(a, b)])
                if variant == "planted":  # deliberately wrong weight p/(r s) instead of p^2/(r s)
                    extra += pc[(a, b)] / (r[a] * s_[b]) * (expfac - 1)
                else:
                    extra += pc[(a, b)] ** 2 / (r[a] * s_[b]) * (expfac - 1)
        tot += Pc * pc[(0, 0)] * (chi2 + extra)
    return tot


print("(A) exact rational residual identity, arbitrary full-support laws")
worst = Fr(0)
nfail_planted = 0
ncase = 0
for shape in [(2, 2), (3, 4), (2, 2, 2), (2, 3, 4), (3, 3, 3), (2, 2, 2, 2), (2, 3, 2, 3)]:
    for trial in range(3):
        P = rand_law(shape)
        n = len(shape)
        for i in range(n):
            for j in range(i + 1, n):
                lhs = one_step_pair00(P, shape, i, j) - sum(p for s, p in P.items() if s[i] == 0 and s[j] == 0)
                rhs = rhs_formula(P, shape, i, j)
                bad = rhs_formula(P, shape, i, j, "planted")
                worst = max(worst, abs(lhs - rhs))
                ncase += 1
                nfail_planted += (bad != lhs)
print(f"  cases={ncase}  max|LHS-RHS| (exact Fractions) = {worst}   planted-error formula differs in {nfail_planted}/{ncase} cases")
assert worst == 0 and nfail_planted == ncase


def entropy(p):
    p = np.asarray(p, float).ravel()
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


def joint_obs(p_eta, liks, active):
    M = len(p_eta)
    arrs = []
    for m in range(M):
        a = np.array(p_eta[m])
        for k in active:
            a = np.multiply.outer(a, liks[k][m])
        arrs.append(a)
    return np.stack(arrs)


def MI_eta_obs(p_eta, liks, active):
    if not active:
        return 0.0
    J = joint_obs(p_eta, liks, active)
    return entropy(J.sum(axis=tuple(range(1, J.ndim)))) + entropy(J.sum(axis=0)) - entropy(J)


def cond_MI_obs(p_eta, liks, A, B, O):
    act = list(A) + list(B) + list(O)
    J = joint_obs(p_eta, liks, act).sum(axis=0)
    nA, nB, nO = len(A), len(B), len(O)
    axA = tuple(range(0, nA))
    axB = tuple(range(nA, nA + nB))
    axO = tuple(range(nA + nB, nA + nB + nO))

    def H(keep):
        if not keep:
            return 0.0
        return entropy(J.sum(axis=tuple(x for x in range(J.ndim) if x not in keep)))
    return H(axA + axO) + H(axB + axO) - H(axA + axB + axO) - H(axO)


rng = np.random.default_rng(11)
print("(B) Step 1: d^2 G_C through null policies vs directly computed I(o_A;o_B|o_O)")
maxerr = 0.0
cnt = 0
for trial in range(6):
    M = int(rng.integers(2, 5))
    n = 4
    p_eta = rng.dirichlet(np.ones(M))
    liks = [rng.dirichlet(np.ones(int(rng.integers(2, 4))), size=M) for _ in range(n)]
    I = lambda act: MI_eta_obs(p_eta, liks, act)
    for (i, j) in [(0, 1), (1, 3), (0, 2)]:
        rest = [k for k in range(n) if k not in (i, j)]
        for O in [[], rest[:1], rest]:
            d2 = -I([i, j] + O) + I([i] + O) + I([j] + O) - I(O)
            direct = cond_MI_obs(p_eta, liks, [i], [j], O)
            maxerr = max(maxerr, abs(d2 - direct))
            cnt += 1
            assert direct >= -1e-13
print(f"  {cnt} (pair, context) points in random discrete models: max |d2G - I_direct| = {maxerr:.2e}")
assert maxerr < 1e-12
p_eta = np.ones(4) / 4


def det(f):
    return np.array([[1.0 if f(m) == v else 0.0 for v in (0, 1)] for m in range(4)])


liks = [det(lambda m: m // 2), det(lambda m: m % 2), det(lambda m: (m // 2) ^ (m % 2))]
print(f"  XOR: I(o1;o2)={cond_MI_obs(p_eta, liks, [0], [1], []):.6f}  I(o1;o2|o3)={cond_MI_obs(p_eta, liks, [0], [1], [2]):.6f} (ln2={math.log(2):.6f})")
d2_xor = -MI_eta_obs(p_eta, liks, [0, 1, 2]) + MI_eta_obs(p_eta, liks, [0, 2]) + MI_eta_obs(p_eta, liks, [1, 2]) - MI_eta_obs(p_eta, liks, [2])
print(f"  XOR: d2G at context c=(member 3 active) = {d2_xor:.6f}")
planted = -MI_eta_obs(p_eta, liks, [0, 1]) + MI_eta_obs(p_eta, liks, [0]) + MI_eta_obs(p_eta, liks, [1])
print(f"  planted control (unconditional redundancy used in place of conditional) = {planted:.6f} != {d2_xor:.6f}")


def sync_T(G, E, gamma):
    shape = G.shape
    n = G.ndim
    lp = -gamma * G
    for i in range(n):
        sh = [1] * n
        sh[i] = shape[i]
        lp = lp + np.log(E[i]).reshape(sh)
    P = np.exp(lp - lp.max())
    P /= P.sum()
    K = [P / P.sum(axis=i, keepdims=True) for i in range(n)]
    states = list(product(*[range(m) for m in shape]))
    T = np.zeros((len(states),) * 2)
    for a, s in enumerate(states):
        for b, t in enumerate(states):
            pr = 1.0
            for i in range(n):
                u = list(s)
                u[i] = t[i]
                pr *= K[i][tuple(u)]
            T[a, b] = pr
    return T, P


def stat(T):
    N = T.shape[0]
    A = np.vstack([T.T - np.eye(N), np.ones(N)])
    b = np.zeros(N + 1)
    b[-1] = 1
    return np.linalg.lstsq(A, b, rcond=None)[0]


def gauss_G(Hs, shape, psi):
    d = Hs[0][1].shape[1]
    G = np.zeros(shape)
    for s in product(*[range(m) for m in shape]):
        prec = np.eye(d)
        for i, a in enumerate(s):
            if a > 0:
                prec += Hs[i][a].T @ Hs[i][a]
        G[s] = -0.5 * np.linalg.slogdet(prec)[1] + sum(psi[i][a] for i, a in enumerate(s))
    return G


print("(D) extremes: 3-member 3-policy Gaussian model, n=2, zero redundancy")
shape = (3, 3, 3)
Hs = [[None] + [rng.normal(0, 1.2, size=(1, 2)) for _ in range(2)] for _ in range(3)]
psi = [[0.0, 0.2, -0.3], [0.0, 0.1, 0.4], [0.0, -0.2, 0.3]]
E = [np.array([0.3, 0.3, 0.4]), np.array([0.2, 0.5, 0.3]), np.array([0.5, 0.25, 0.25])]
G = gauss_G(Hs, shape, psi)
for gamma in [1e-4, 1e-2, 1.0, 10.0, 40.0]:
    T, P = sync_T(G, E, gamma)
    ps = stat(T)
    gain = (P.ravel() @ T).reshape(shape).sum(axis=2)[0, 0] - P.sum(axis=2)[0, 0]
    print(f"  gamma={gamma:<7g} TV(P_sync,P_C)={0.5 * np.abs(ps - P.ravel()).sum():.3e}  one-step gain P(Y0=0,Y1=0)-P(X0=0,X1=0)={gain:.3e}")
G2 = gauss_G([Hs[0], Hs[1]], (3, 3), psi[:2])
T, P = sync_T(G2, E[:2], 1.3)
ps = stat(T).reshape(3, 3)
print(f"  n=2: TV(P_sync, product of its marginals)={0.5 * np.abs(ps - np.outer(ps.sum(1), ps.sum(0))).sum():.2e}, TV(P_sync,P_C)={0.5 * np.abs(ps - P).sum():.3e}")
Ho = [[None, np.array([[1.0, 0, 0]]), np.array([[2.0, 0, 0]])],
      [None, np.array([[0, 1.5, 0]]), np.array([[0, 0.7, 0]])],
      [None, np.array([[0, 0, 1.1]]), np.array([[0, 0, 2.2]])]]
Go = gauss_G(Ho, shape, psi)
T, P = sync_T(Go, E, 2.0)
print(f"  zero redundancy: TV(P_sync,P_C)={0.5 * np.abs(stat(T) - P.ravel()).sum():.2e}")
print("done")
