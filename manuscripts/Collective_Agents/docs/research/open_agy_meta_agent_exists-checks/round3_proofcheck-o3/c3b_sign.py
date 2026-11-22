r"""Fresh-context check of C3b (Proposition S, sign rule, and its EFE corollary).

Two exchangeable firms on one scalar world, no cross-firm channel. Firm k (n_k members):
  m_i^+ = c0_k m_i + K_s (eta + v_i) + K_c sum_{j != i, j in k} (eta + v_j + nu_ij),  c0_k = 1 - K_s - (n_k-1) K_c,
  m_i(t+1) = a_k m_i^+ + bhat_k U_k + eps_i,  U_k = -g_k sum_{j in k} m_j^+,
  eta(t+1) = F eta + b (U_1 + U_2) + w.
Direct method: stationary covariance of (m, eta) and exact Gaussian conditioning of m(0) on the
window eta_{-L..L}; no spectral argument is used.
Claims:
  S1 all cross entries Pi^c_ij (i in C1, j in C2) are equal, = (V^{-1})_12/sqrt(n1 n2);
  S2 sign(Pi^c_ij) = sign(phi1 kappa1 phi2 kappa2), phi_k = a_k - bhat_k g_k n_k, kappa_k = b g_k sqrt(n_k)
     (eps = 0, as in the proposition's setting).
  C  EFE corollary: g_k = c_k a_k/(bhat_k (1 + n_k c_k)), c_k = sE2 gam Lam bhat_k^2 > 0, sign(bhat_k) =
     sign(b) => cross entries > 0.
Declared expectations: S1 to 1e-9; S2 agreement in every draw with |cross| > 1e-9 relative;
C positive in every draw.
Negative controls (must fail in some draws):
  N1 naive rule sign(kappa1 kappa2) (phi ignored) disagrees whenever phi1 phi2 < 0.
  N2 firm 1 misjudges its effect sign: cross entries negative.
Side remark of the report probed: "computation noise on predictions changes only diag(V)".
  Expected (my reconstruction): FALSE - prediction noise propagates into U_k and then into eta, so
  V_12 changes, and the sign rule can fail (largest risk when phi1 phi2 < 0 and the noise is large).
"""
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import sympy as sp
from scipy.linalg import solve_discrete_lyapunov, toeplitz

rng = np.random.default_rng(2026)


def build(n, Ks, Kc, a, bh, g, b, F, R, Rc, Qw, se2):
    """Return transition M, noise covariance Nc of the state (m_1, m_2, eta)."""
    N = sum(n)
    firm = np.concatenate([[k] * n[k] for k in range(2)])
    c0 = np.array([1 - Ks[firm[i]] - (n[firm[i]] - 1) * Kc[firm[i]] for i in range(N)])
    # noise vector: v (N), nu (receiver-specific, one per ordered in-firm pair), eps (N), w (1)
    pairs = [(i, j) for i in range(N) for j in range(N) if i != j and firm[i] == firm[j]]
    nv, nn = N, len(pairs)
    Gv = np.zeros((N, nv))
    Gn = np.zeros((N, nn))
    for i in range(N):
        k = firm[i]
        Gv[i, i] = Ks[k]
        for j in range(N):
            if j != i and firm[j] == k:
                Gv[i, j] = Kc[k]
    for p, (i, j) in enumerate(pairs):
        Gn[i, p] = Kc[firm[i]]
    T = np.zeros((N, N))
    for k in range(2):
        idx = np.nonzero(firm == k)[0]
        T[np.ix_(idx, idx)] = a[k] * np.eye(n[k]) - bh[k] * g[k] * np.ones((n[k], n[k]))
    d = -b * np.array([g[firm[i]] for i in range(N)])
    keta = 1 - c0
    M = np.zeros((N + 1, N + 1))
    M[:N, :N] = T @ np.diag(c0)
    M[:N, N] = T @ keta
    M[N, :N] = d @ np.diag(c0)
    M[N, N] = F + d @ keta
    Nm = np.zeros((N + 1, nv + nn + N + 1))
    Nm[:N, :nv] = T @ Gv
    Nm[:N, nv:nv + nn] = T @ Gn
    Nm[:N, nv + nn:nv + nn + N] = np.eye(N)
    Nm[N, :nv] = d @ Gv
    Nm[N, nv:nv + nn] = d @ Gn
    Nm[N, -1] = 1.0
    cov = np.diag(np.concatenate([[R] * nv, [Rc] * nn, [se2] * N, [Qw]]))
    return M, Nm @ cov @ Nm.T, c0


def cond(M, Nc, L=120):
    n = M.shape[0] - 1
    if np.max(np.abs(np.linalg.eigvals(M))) >= 0.985:
        return None
    P = solve_discrete_lyapunov(M, Nc)
    MP = [P]
    for _ in range(2 * L + 2):
        MP.append(M @ MP[-1])
    r = np.array([MP[h][n, n] for h in range(2 * L + 2)])
    times = np.arange(-L, L + 1)
    Cee = toeplitz(r[:len(times)])
    Cxe = np.stack([MP[t][n, :n] if t >= 0 else MP[-t][:n, n] for t in times], axis=1)
    S = P[:n, :n] - Cxe @ np.linalg.solve(Cee, Cxe.T)
    return (S + S.T) / 2


def draw(efe=False, wrong_sign=False):
    n = [int(rng.integers(2, 5)), int(rng.integers(2, 5))]
    Ks = rng.uniform(0.05, 0.5, 2)
    Kc = np.array([rng.uniform(0.01, (0.95 - Ks[k]) / (n[k] - 1)) for k in range(2)])
    b = rng.choice([-1, 1]) * rng.uniform(0.1, 1.0)
    a = rng.uniform(-1, 1, 2)
    if efe:
        bh = np.sign(b) * rng.uniform(0.05, 1.2, 2)
        if wrong_sign:
            bh[0] = -bh[0]
        s = rng.exponential(1.0, 2)  # sE2 * gam * Lam
        c = s * bh ** 2
        g = c * a / (bh * (1 + np.array(n) * c))
    else:
        bh = rng.choice([-1, 1], 2) * rng.uniform(0.05, 1.2, 2)
        g = rng.choice([-1, 1], 2) * rng.uniform(0.02, 0.6, 2)
    F = rng.uniform(-0.95, 0.95)
    R, Rc, Qw = rng.uniform(0.3, 3), rng.uniform(0.05, 2), rng.uniform(0.01, 1)
    return dict(n=n, Ks=Ks, Kc=Kc, a=a, bh=bh, g=g, b=b, F=F, R=R, Rc=Rc, Qw=Qw)


def cross_and_V(p, se2):
    M, Nc, c0 = build(p["n"], p["Ks"], p["Kc"], p["a"], p["bh"], p["g"], p["b"], p["F"], p["R"], p["Rc"], p["Qw"], se2)
    if np.max(np.abs(c0 * np.repeat(p["a"], p["n"]))) >= 0.99:
        return None
    S = cond(M, Nc)
    if S is None:
        return None
    n1, n2 = p["n"]
    Pi = np.linalg.inv(S)
    cr = Pi[:n1, n1:]
    Phi = np.zeros((n1 + n2, 2))
    Phi[:n1, 0] = 1 / np.sqrt(n1)
    Phi[n1:, 1] = 1 / np.sqrt(n2)
    V = Phi.T @ S @ Phi
    return cr, V, Pi


def rule(p):
    n = np.array(p["n"])
    phi = p["a"] - p["bh"] * p["g"] * n
    kap = p["b"] * p["g"] * np.sqrt(n)
    return phi, kap


# S1, S2, N1
agree = naive_dis = used = 0
s1 = 0.0
while used < 150:
    p = draw()
    out = cross_and_V(p, 0.0)
    if out is None:
        continue
    cr, V, Pi = out
    if np.max(np.abs(cr)) < 1e-9 * np.max(np.abs(Pi)):
        continue
    used += 1
    n1, n2 = p["n"]
    s1 = max(s1, np.max(np.abs(cr - np.linalg.inv(V)[0, 1] / np.sqrt(n1 * n2))) / np.max(np.abs(cr)))
    phi, kap = rule(p)
    agree += int(np.sign(cr[0, 0]) == np.sign(np.prod(phi) * np.prod(kap)))
    naive_dis += int(np.sign(cr[0, 0]) != np.sign(np.prod(kap)))
print(f"S1: max rel |cross - (V^-1)_12/sqrt(n1 n2)| = {s1:.2e} over {used} draws")
print(f"S2: sign rule agrees in {agree}/{used};  N1 naive sign(kappa1 kappa2) disagrees in {naive_dis}/{used}")

# Corollary C and N2
pos = used = 0
while used < 100:
    p = draw(efe=True)
    out = cross_and_V(p, 0.0)
    if out is None:
        continue
    used += 1
    pos += int(np.min(out[0]) > 0)
negc = usedn = 0
while usedn < 100:
    p = draw(efe=True, wrong_sign=True)
    out = cross_and_V(p, 0.0)
    if out is None:
        continue
    usedn += 1
    negc += int(np.max(out[0]) < 0)
print(f"C: EFE-consistent firms with correct effect sign: cross entries > 0 in {pos}/{used}")
print(f"N2: firm 1 misjudges its effect sign: cross entries < 0 in {negc}/{usedn}")

# symbolic check of the corollary algebra
u, mbar, a_, bh_, s_, nn = sp.symbols("u mbar a bhat s n", real=True)
c_ = s_ * bh_ ** 2
# group posterior with Gaussian habits N(0, sE2) per member and act part (gam Lam/2)(a mbar + bhat n u)^2,
# common act u by symmetry; s = sE2 gam Lam.  Objective * sE2:
obj = nn * u ** 2 / 2 + s_ * (a_ * mbar + bh_ * nn * u) ** 2 / 2
ustar = sp.solve(sp.diff(obj, u), u)[0]
g_ = sp.simplify(-ustar / mbar)
phi_ = sp.simplify(a_ - bh_ * g_ * nn)
bb = sp.symbols("b", real=True)
phikap = sp.simplify(phi_ * bb * g_ * sp.sqrt(nn))
target = (bb / bh_) * a_ ** 2 * c_ * sp.sqrt(nn) / (1 + nn * c_) ** 2
print("symbolic: g =", sp.simplify(g_ - c_ * a_ / (bh_ * (1 + nn * c_))) == 0,
      "; phi*kappa matches the report:", sp.simplify(phikap - target) == 0)

# Side remark: computation (prediction) noise
v12_change = fail = fail_neg_phi = tested = 0
worst_case = None
while tested < 300:
    p = draw()
    out0 = cross_and_V(p, 0.0)
    se2 = 10 ** rng.uniform(-2, 1)
    out1 = cross_and_V(p, se2)
    if out0 is None or out1 is None:
        continue
    cr1, V1, Pi1 = out1
    if np.max(np.abs(cr1)) < 1e-9 * np.max(np.abs(Pi1)):
        continue
    tested += 1
    V0 = out0[1]
    if abs(V1[0, 1] - V0[0, 1]) > 1e-8 * max(abs(V0[0, 1]), 1e-12):
        v12_change += 1
    phi, kap = rule(p)
    if np.sign(cr1[0, 0]) != np.sign(np.prod(phi) * np.prod(kap)):
        fail += 1
        fail_neg_phi += int(np.prod(phi) < 0)
        if worst_case is None:
            worst_case = (p, se2, cr1[0, 0], np.prod(phi) * np.prod(kap), out0[0][0, 0])
print(f"remark: V_12 changed by prediction noise in {v12_change}/{tested}; sign rule fails in {fail}/{tested} (with phi1 phi2 < 0 in {fail_neg_phi})")
if worst_case is not None:
    p, se2, c1, prod, c0v = worst_case
    print("first failing case:", {k: (np.round(v, 4).tolist() if hasattr(v, '__len__') else round(float(v), 4)) for k, v in p.items()},
          f"se2={se2:.4f}, cross with noise={c1:.4e}, cross without={c0v:.4e}, phi1k1phi2k2={prod:.4e}")
