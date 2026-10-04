r"""Float64 identity checks for the Lie-algebra-link revision of GL(K)_attention_v2.tex (October 4, 2026).

Every check evaluates one displayed identity of the revised manuscript at a small size with random
inputs. The sizes are chosen to test algebra and code-independent formulas; they carry no information
about trained models or large networks. Run with any NumPy/SciPy installation:

    python checks.py > checks_output.txt
"""

import itertools

import numpy as np
from scipy.linalg import expm, logm, null_space, orth

rng = np.random.default_rng(20261004)
results = []


def report(name: str, value: float, tol: float) -> None:
    ok = bool(np.isfinite(value) and value <= tol)
    results.append((name, value, tol, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value:.3e} (tol {tol:.0e})")


def rel(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(b), 1e-300))


def phi1(A: np.ndarray) -> np.ndarray:
    r"""\varphi_1(A)=\sum_{n\ge1}A^{n-1}/n! from the augmented exponential (Van Loan)."""
    n = A.shape[0]
    aug = np.zeros((2 * n, 2 * n))
    aug[:n, :n] = A
    aug[:n, n:] = np.eye(n)
    return expm(aug)[:n, n:]


def rand_gl(n: int, scale: float = 0.6) -> np.ndarray:
    return np.eye(n) + scale * rng.standard_normal((n, n)) / np.sqrt(n)


def rand_spd(n: int, scale: float = 1.0) -> np.ndarray:
    A = rng.standard_normal((n, n))
    return scale * (A @ A.T / n + 0.5 * np.eye(n))


def gauss_kl(m0, S0, m1, S1) -> float:
    r"""KL(N(m0,S0) || N(m1,S1))."""
    k = len(m0)
    S1i = np.linalg.inv(S1)
    d = m1 - m0
    return 0.5 * (np.trace(S1i @ S0) + d @ S1i @ d - k
                  + np.linalg.slogdet(S1)[1] - np.linalg.slogdet(S0)[1])


# ----------------------------------------------------------------------------------------------
# Section: Lie-algebra links
# ----------------------------------------------------------------------------------------------
K, r = 6, 2
P = rng.standard_normal((K, r))
Q = rng.standard_normal((r, K))
report("low-rank exponential exp(PQ)=I+P phi1(QP) Q", rel(expm(P @ Q), np.eye(K) + P @ phi1(Q @ P) @ Q), 1e-13)

A = rng.standard_normal((4, 4))
series = np.zeros((4, 4))
term = np.eye(4)
for n in range(1, 60):
    series += term / np.prod(np.arange(1, n + 1, dtype=float))
    term = term @ A
report("phi1 augmented exponential equals its series", rel(phi1(A), series), 1e-12)
report("phi1(A)=(e^A-I)A^{-1} for invertible A", rel(phi1(A), (expm(A) - np.eye(4)) @ np.linalg.inv(A)), 1e-11)

# Flat transport plus channel term, one head.
s_h = 2
Uh_i, Uh_j = rand_gl(K), rand_gl(K)
O_h = rng.standard_normal((K, s_h))
T_h = rng.standard_normal((s_h, K))
Omega = Uh_i @ np.linalg.inv(Uh_j)
Theta = Uh_i @ expm(O_h @ T_h) @ np.linalg.inv(Uh_j)
report("split Theta = Omega + U_i O phi1(TO) T U_j^{-1}",
       rel(Theta, Omega + Uh_i @ O_h @ phi1(T_h @ O_h) @ T_h @ np.linalg.inv(Uh_j)), 1e-13)
kerT = null_space(T_h)
report("exp(O_h T_h) fixes ker T_h", float(np.linalg.norm(expm(O_h @ T_h) @ kerT - kerT)), 1e-13)
Wimg = orth(O_h)
D = expm(O_h @ T_h) - np.eye(K)
report("image of exp(O_h T_h)-I lies in im O_h", float(np.linalg.norm(D - Wimg @ Wimg.T @ D)), 1e-12)
report("det Theta = det(U_i U_j^{-1}) e^{tr(T_h O_h)}",
       abs(np.linalg.det(Theta) / (np.linalg.det(Omega) * np.exp(np.trace(T_h @ O_h))) - 1), 1e-12)
L = Uh_i @ O_h @ T_h @ np.linalg.inv(Uh_j)
defects = []
for s in (1e-2, 1e-3, 1e-4):
    Ts = Uh_i @ expm(s * O_h @ T_h) @ np.linalg.inv(Uh_j)
    defects.append(rel((Ts - Omega) / s, L))
print("    first-order defects (Theta(s)-Omega)/s - L at s=1e-2,1e-3,1e-4:", ", ".join(f"{d:.2e}" for d in defects))
report("first-order defect scales linearly in s", abs(defects[0] / defects[1] / 10 - 1) + abs(defects[1] / defects[2] / 10 - 1), 5e-2)

# Passive covariance and the adjoint action of a common reference change.
X = rng.standard_normal((K, K)) / np.sqrt(K)
g_i, g_j, a = rand_gl(K), rand_gl(K), rand_gl(K)
Th = Uh_i @ expm(X) @ np.linalg.inv(Uh_j)
Th_pass = (g_i @ Uh_i) @ expm(X) @ np.linalg.inv(g_j @ Uh_j)
report("passive law Theta' = g_i Theta g_j^{-1}", rel(Th_pass, g_i @ Th @ np.linalg.inv(g_j)), 1e-13)
Th_ref = (Uh_i @ a) @ expm(np.linalg.inv(a) @ X @ a) @ np.linalg.inv(Uh_j @ a)
report("common reference change with X -> a^{-1} X a leaves Theta unchanged", rel(Th_ref, Th), 1e-12)

# A matrix in GL^+(2) outside the exponential chart (Culver).
Gneg = np.diag([-1.0, -2.0])
Lg = logm(Gneg)
report("diag(-1,-2) has positive determinant and logm returns a complex logarithm (no real log, Culver)",
       0.0 if np.abs(np.imag(Lg)).max() > 1.0 else 1.0, 0.5)

# Two charts of one group: exact conversion (item 4) on the principal-logarithm domain.
Kc, dc = 7, 3
Tc = rng.standard_normal((dc, Kc))
O_lin = 0.05 * rng.standard_normal((Kc, dc))
spec = np.linalg.eigvals(np.eye(dc) + Tc @ O_lin)
assert not np.any((np.abs(spec.imag) < 1e-12) & (spec.real <= 0)), "hypothesis: spectrum off (-inf, 0]"
Z = logm(np.eye(dc) + Tc @ O_lin)
assert np.abs(np.imag(Z)).max() < 1e-12
Z = Z.real
Oc = O_lin @ np.linalg.inv(phi1(Z))
report("chart conversion: T O = Z", rel(Tc @ Oc, Z), 1e-12)
report("chart conversion: exp(OT) = I + O_lin T", rel(expm(Oc @ Tc), np.eye(Kc) + O_lin @ Tc), 1e-12)
Oe = rng.standard_normal((Kc, dc))
TO = Tc @ Oe
Pi = Oe @ np.linalg.inv(TO) @ Tc


def Upsilon(B: np.ndarray) -> np.ndarray:
    return (np.eye(Kc) - Pi) + Oe @ B @ np.linalg.inv(TO) @ Tc


B1, B2 = rand_gl(dc), rand_gl(dc)
report("Upsilon is a homomorphism", rel(Upsilon(B1) @ Upsilon(B2), Upsilon(B1 @ B2)), 1e-11)
report("det Upsilon(B) = det B", abs(np.linalg.det(Upsilon(B1)) / np.linalg.det(B1) - 1), 1e-11)
report("exp(OT) = Upsilon(e^{TO})", rel(expm(Oe @ Tc), Upsilon(expm(TO))), 1e-11)
Cm = rng.standard_normal((dc, dc))
report("I + OCT = Upsilon(I + CTO)", rel(np.eye(Kc) + Oe @ Cm @ Tc, Upsilon(np.eye(dc) + Cm @ TO)), 1e-11)

# ----------------------------------------------------------------------------------------------
# Aggregation, complement split, and the tiled message
# ----------------------------------------------------------------------------------------------
Kn, Hn, dn = 7, 2, 2                       # S = 4 < K: a nontrivial complement
Sn = Hn * dn
On = rng.standard_normal((Kn, Sn))
Tn = rng.standard_normal((Sn, Kn))
TOn = Tn @ On
Pin = On @ np.linalg.inv(TOn) @ Tn
report("complement projector is idempotent", rel(Pin @ Pin, Pin), 1e-12)
report("complement split exp(OT) = (I-Pi) + O e^{TO}(TO)^{-1} T",
       rel(expm(On @ Tn), (np.eye(Kn) - Pin) + On @ expm(TOn) @ np.linalg.inv(TOn) @ Tn), 1e-12)
Ohat = On @ expm(TOn) @ np.linalg.inv(TOn)           # receiving map O' with block columns O'_h
N_src = 3
xi = rng.standard_normal((N_src, Kn))
beta = rng.dirichlet(np.ones(N_src), size=Hn)        # beta[h, j]
i_recv = 2
exact = np.zeros(Kn)
for labels in itertools.product(range(N_src), repeat=Hn):
    prob = np.prod([beta[h, labels[h]] for h in range(Hn)])
    state = (np.eye(Kn) - Pin) @ xi[i_recv]
    for h in range(Hn):
        state = state + Ohat[:, h * dn:(h + 1) * dn] @ Tn[h * dn:(h + 1) * dn] @ xi[labels[h]]
    exact += prob * state
closed = (np.eye(Kn) - Pin) @ xi[i_recv] + sum(
    beta[h, j] * Ohat[:, h * dn:(h + 1) * dn] @ Tn[h * dn:(h + 1) * dn] @ xi[j]
    for h in range(Hn) for j in range(N_src))
report("label enumeration equals the closed-form aggregate with receiver-carried complement", rel(exact, closed), 1e-13)

# Tiled heads: resummed receiving map, zeroth-order projectors, orders.
Kt, Ht, dt = 6, 3, 2
Tt = rand_gl(Kt, 0.8)
Ot = rng.standard_normal((Kt, Kt)) / np.sqrt(Kt)
Opt = Ot @ expm(Tt @ Ot) @ np.linalg.inv(Tt @ Ot)
report("tiled: O e^{TO}(TO)^{-1} = e^{OT} T^{-1}", rel(Opt, expm(Ot @ Tt) @ np.linalg.inv(Tt)), 1e-11)
report("tiled: e^{OT} T^{-1} = T^{-1} + O phi1(TO)", rel(Opt, np.linalg.inv(Tt) + Ot @ phi1(Tt @ Ot)), 1e-11)
report("tiled: T O' = e^{TO}", rel(Tt @ Opt, expm(Tt @ Ot)), 1e-11)
bt = rng.uniform(0.1, 1.0, size=Ht)
Bmat = np.kron(np.diag(bt), np.eye(dt))             # head-diagonal routing matrix
headsum = sum(bt[h] * Opt[:, h * dt:(h + 1) * dt] @ Tt[h * dt:(h + 1) * dt] for h in range(Ht))
report("tiled: sum_h O'_h beta^h T_h = O' bbeta T", rel(headsum, Opt @ Bmat @ Tt), 1e-12)
Tinv = np.linalg.inv(Tt)
Pis = []
for h in range(Ht):
    Delta = np.zeros((Kt, Kt))
    Delta[h * dt:(h + 1) * dt, h * dt:(h + 1) * dt] = np.eye(dt)
    Pis.append(Tinv @ Delta @ Tt)
report("zeroth order: Pi_h = (T^{-1})_{:,h} T_h",
       max(rel(Pis[h], Tinv[:, h * dt:(h + 1) * dt] @ Tt[h * dt:(h + 1) * dt]) for h in range(Ht)), 1e-12)
report("zeroth order: Pi_h Pi_g = delta_hg Pi_h",
       max(float(np.linalg.norm(Pis[h] @ Pis[g] - (Pis[h] if h == g else 0))) for h in range(Ht) for g in range(Ht)), 1e-11)
report("zeroth order: sum_h Pi_h = I", rel(sum(Pis), np.eye(Kt)), 1e-12)
report("zeroth order: ker Pi_h = ker T_h",
       max(float(np.linalg.norm(Pis[h] @ null_space(Tt[h * dt:(h + 1) * dt]))) for h in range(Ht)), 1e-11)
report("zeroth order: T_g Pi_h = 0 for g != h",
       max(float(np.linalg.norm(Tt[g * dt:(g + 1) * dt] @ Pis[h])) for h in range(Ht) for g in range(Ht) if g != h), 1e-11)
report("zeroth order: T^{-1} bbeta T = sum_h beta^h Pi_h", rel(Tinv @ Bmat @ Tt, sum(bt[h] * Pis[h] for h in range(Ht))), 1e-12)
s = 0.7
series = Tinv.copy()
term = Ot.copy()
for n in range(1, 60):
    series = series + s ** n / np.prod(np.arange(1, n + 1, dtype=float)) * term
    term = term @ (Tt @ Ot)
report("orders: O'(s) = T^{-1} + sum_n s^n/n! O (TO)^{n-1}", rel(series, Tinv + s * Ot @ phi1(s * Tt @ Ot)), 1e-12)
Zs = np.array([[-1.0, -1.0], [1.0, -1.0]])
report("second-order truncation I + Z + Z^2/2 vanishes at Z=[[-1,-1],[1,-1]]",
       float(np.linalg.norm(np.eye(2) + Zs + Zs @ Zs / 2)), 1e-15)
sv_bound = []
for _ in range(200):
    Xr = rng.standard_normal((5, 5)) * rng.uniform(0.1, 3.0)
    sv_bound.append(np.exp(-np.linalg.norm(Xr, 2)) - np.linalg.svd(expm(Xr), compute_uv=False).min())
report("sigma_min(e^X) >= e^{-||X||_2} on 200 random generators (max violation)", max(0.0, max(sv_bound)), 1e-12)

# Static limit of the latent-link model: pinned generators give the exponential-chart message.
xi_t = rng.standard_normal((N_src, Kt))
beta_t = rng.dirichlet(np.ones(N_src), size=Ht)
GX = expm(Ot @ Tt)
mean_transport = sum(beta_t[h, j] * GX @ Pis[h] @ xi_t[j] for h in range(Ht) for j in range(N_src))
chart_message = sum(Opt @ np.kron(np.diag(beta_t[:, j]), np.eye(dt)) @ Tt @ xi_t[j] for j in range(N_src))
report("static limit: mean of sum_h e^{OT} Pi_h xi_{J^h} equals the exponential-chart message",
       rel(mean_transport, chart_message), 1e-12)

# ----------------------------------------------------------------------------------------------
# Holonomy
# ----------------------------------------------------------------------------------------------
U3 = [rand_gl(Kt) for _ in range(3)]          # tokens k=0 < j=1 < i=2
bb = {e: rng.uniform(0.05, 1.0, size=Ht) for e in [(2, 1), (1, 0), (2, 0)]}


def edge(a_, b_, recv):
    Bab = np.kron(np.diag(bb[(a_, b_)]), np.eye(dt))
    return U3[a_] @ recv @ Bab @ Tt @ np.linalg.inv(U3[b_])


def triangle(recv):
    return np.linalg.inv(edge(2, 0, recv)) @ edge(2, 1, recv) @ edge(1, 0, recv)


rho = np.kron(np.diag(bb[(2, 1)] * bb[(1, 0)] / bb[(2, 0)]), np.eye(dt))


def eig_match(Amat, Bm):
    ea = np.sort_complex(np.linalg.eigvals(Amat))
    eb = np.sort_complex(np.linalg.eigvals(Bm))
    return float(np.max(np.abs(ea - eb)) / np.max(np.abs(eb)))


report("head-sum triangle holonomy is similar to rho (TO) for TO != I", eig_match(triangle(Ot), rho @ Tt @ Ot), 1e-9)
report("exponential-chart triangle holonomy is similar to rho e^{TO}", eig_match(triangle(Opt), rho @ expm(Tt @ Ot)), 1e-9)
Oorth = np.linalg.inv(Tt)                     # TO = I
loop = edge(2, 1, Oorth) @ edge(1, 0, Oorth) @ np.linalg.inv(edge(2, 0, Oorth))
report("head-sum loop with TO=I: U_i O rho O^{-1} U_i^{-1}",
       rel(loop, U3[2] @ Oorth @ rho @ np.linalg.inv(Oorth) @ np.linalg.inv(U3[2])), 1e-11)
report("flat reference identification has trivial triangle holonomy",
       rel(np.linalg.inv(U3[2] @ np.linalg.inv(U3[0])) @ (U3[2] @ np.linalg.inv(U3[1])) @ (U3[1] @ np.linalg.inv(U3[0])), np.eye(Kt)), 1e-12)
errs1, errs2 = [], []
A0, B0, Z0 = (rng.standard_normal((4, 4)) for _ in range(3))
for eps in (0.1, 0.05, 0.025):
    Aa, Bb, Zz = eps * A0, eps * B0, eps * Z0
    exact_log = logm(expm(-Zz) @ expm(Aa) @ expm(Bb)).real
    first = Aa + Bb - Zz
    second = first + 0.5 * ((Aa @ Bb - Bb @ Aa) - (Zz @ Aa - Aa @ Zz) - (Zz @ Bb - Bb @ Zz))
    errs1.append(np.linalg.norm(exact_log - first))
    errs2.append(np.linalg.norm(exact_log - second))
print("    BCH first-order errors:", ", ".join(f"{e:.2e}" for e in errs1), "| second-order:", ", ".join(f"{e:.2e}" for e in errs2))
report("BCH: first-order error ~ eps^2 and second-order error ~ eps^3",
       abs(np.log2(errs1[1] / errs1[2]) - 2) / 2 + abs(np.log2(errs2[1] / errs2[2]) - 3) / 3, 0.1)
c = np.array([1, 0.5, 0.2, 0.05, 0.01])
n_tok = len(c)
Bf = np.zeros((n_tok, n_tok))
for i in range(n_tok):
    Bf[i, 0] = c[i]
    for j in range(1, i):
        Bf[i, j] = c[i] / c[j]
    if i > 0:
        Bf[i, i] = 1 - Bf[i, :i].sum()
Bf[0, 0] = 1.0
defect = max(abs(Bf[i, j] * Bf[j, k] - Bf[i, k]) for i in range(n_tok) for j in range(n_tok) for k in range(n_tok) if k < j < i)
report("flat normalized routing: positive rows summing to one with zero cocycle defect",
       defect + abs(Bf.sum(1) - 1).max() + (0.0 if (np.diag(Bf) > 0).all() else 1.0), 1e-14)
uniform_defect = max(abs(1 / (j + 1) - 1) for i in range(5) for j in range(5) for k in range(5) if k < j < i)
print(f"    uniform causal routing: largest multiplicative weight defect |1/(j+1) - 1| = {uniform_defect:.4f}")

# Class functions are blind to unipotent holonomy; the Frobenius defect is not.
W = np.eye(3)
W[0, 1] = 1.0
lam = np.linalg.eigvals(W)
report("shear I+E_12: eigenvalue density sum|lambda-1| vanishes", float(np.abs(lam - 1).sum()), 1e-15)
report("shear I+E_12: Frobenius defect 0.5||W-I||_F^2 equals 0.5", abs(0.5 * np.linalg.norm(W - np.eye(3)) ** 2 - 0.5), 1e-15)
conj = [np.linalg.norm(np.diag([1, 1 / t, 1 / t ** 2]) @ W @ np.diag([1, t, t ** 2]) - np.eye(3)) for t in (1e-1, 1e-2, 1e-3)]
report("conjugates D_t W D_t^{-1} converge to I", conj[-1], 1e-2)
Wg = rand_gl(4)
Oq, _ = np.linalg.qr(rng.standard_normal((4, 4)))
hc = 2.7 * Oq


def frob(Wm):
    return 0.5 * np.linalg.norm(Wm - np.eye(len(Wm))) ** 2


report("Frobenius defect invariant under h = c O", abs(frob(hc @ Wg @ np.linalg.inv(hc)) - frob(Wg)), 1e-12)
hn = np.diag([1.0, 2.0, 1.0, 1.0])
print(f"    non-conformal h changes the defect: {frob(Wg):.4f} -> {frob(hn @ Wg @ np.linalg.inv(hn)):.4f}")

# ----------------------------------------------------------------------------------------------
# Receiver inference: the channel likelihood and its closed form
# ----------------------------------------------------------------------------------------------
Kr, Hr, dr, Nr = 6, 2, 2, 4                   # Hr*dr < Kr leaves an unobserved complement
xi_p = rng.standard_normal(Kr)
C_p = rand_spd(Kr)
xbar = rng.standard_normal((Nr, Kr))
Cbar = [rand_spd(Kr) for _ in range(Nr)]
Tr = [rng.standard_normal((dr, Kr)) for _ in range(Hr)]
Pr = [rng.standard_normal((dr, Kr)) for _ in range(Hr)]   # receiving measurements (untied)
beta_r = rng.dirichlet(np.ones(Nr), size=Hr)
lam_alpha, lam_beta, varsigma2 = 0.7, 1.3, 0.4
w = lam_beta * beta_r
R = [[Tr[h] @ Cbar[j] @ Tr[h].T + varsigma2 * np.eye(dr) for j in range(Nr)] for h in range(Hr)]
y = [[Tr[h] @ xbar[j] for j in range(Nr)] for h in range(Hr)]


def receiver_energy(m: np.ndarray, Cq: np.ndarray) -> float:
    r"""lambda_alpha KL(N(m,C)||N(xi_p,C_p)) + sum_hj w_hj E_q[-log N(y_hj; P_h x, R_hj)] (constants kept)."""
    val = lam_alpha * gauss_kl(m, Cq, xi_p, C_p)
    for h in range(Hr):
        for j in range(Nr):
            Ri = np.linalg.inv(R[h][j])
            e = y[h][j] - Pr[h] @ m
            val += w[h, j] * 0.5 * (e @ Ri @ e + np.trace(Pr[h].T @ Ri @ Pr[h] @ Cq)
                                    + np.linalg.slogdet(2 * np.pi * R[h][j])[1])
    return val


Wh = [sum(w[h, j] * np.linalg.inv(R[h][j]) for j in range(Nr)) for h in range(Hr)]
om = [sum(w[h, j] * np.linalg.inv(R[h][j]) @ y[h][j] for j in range(Nr)) for h in range(Hr)]
Cpi = np.linalg.inv(C_p)
Lam = lam_alpha * Cpi + sum(Pr[h].T @ Wh[h] @ Pr[h] for h in range(Hr))
eta = lam_alpha * Cpi @ xi_p + sum(Pr[h].T @ om[h] for h in range(Hr))
m_star = np.linalg.solve(Lam, eta)
C_star = lam_alpha * np.linalg.inv(Lam)
F_star = receiver_energy(m_star, C_star)
worst = 0.0
for _ in range(200):
    dm = 0.3 * rng.standard_normal(Kr)
    E = 0.2 * rng.standard_normal((Kr, Kr))
    Cpert = (np.eye(Kr) + E) @ C_star @ (np.eye(Kr) + E).T
    worst = max(worst, F_star - receiver_energy(m_star + dm, Cpert))
report("closed form (Lambda^{-1} eta, lambda_alpha Lambda^{-1}) is not beaten by 200 perturbations", max(worst, 0.0), 1e-12)
Lchol = np.linalg.cholesky(C_star)
grad = []
h_fd = 1e-6
for k in range(Kr):
    ek = np.zeros(Kr)
    ek[k] = h_fd
    grad.append((receiver_energy(m_star + ek, C_star) - receiver_energy(m_star - ek, C_star)) / (2 * h_fd))
for a_ in range(Kr):
    for b_ in range(a_ + 1):
        Eab = np.zeros((Kr, Kr))
        Eab[a_, b_] = h_fd
        Cp_ = (Lchol + Eab) @ (Lchol + Eab).T
        Cm_ = (Lchol - Eab) @ (Lchol - Eab).T
        grad.append((receiver_energy(m_star, Cp_) - receiver_energy(m_star, Cm_)) / (2 * h_fd))
report("finite-difference gradient vanishes at the closed form (max |grad|)", float(np.abs(grad).max()), 1e-6)
prec_pow = Cpi + sum((w[h, j] / lam_alpha) * Pr[h].T @ np.linalg.inv(R[h][j]) @ Pr[h] for h in range(Hr) for j in range(Nr))
mean_pow = np.linalg.solve(prec_pow, Cpi @ xi_p + sum((w[h, j] / lam_alpha) * Pr[h].T @ np.linalg.inv(R[h][j]) @ y[h][j]
                                                    for h in range(Hr) for j in range(Nr)))
report("closed form equals the Gaussian power posterior with powers w/lambda_alpha",
       rel(m_star, mean_pow) + rel(C_star, np.linalg.inv(prec_pow)), 1e-12)
offs = []
for _ in range(5):
    mq = rng.standard_normal(Kr)
    Cq = rand_spd(Kr)
    offs.append(receiver_energy(mq, Cq) - lam_alpha * gauss_kl(mq, Cq, mean_pow, np.linalg.inv(prec_pow)))
report("F - lambda_alpha KL(q||p_pow) is constant in q", float(np.ptp(offs)), 1e-10)
# No complement pinning: with C_p not coupling V0 = cap ker P_h to its orthogonal complement.
Wobs = orth(np.vstack(Pr).T)
V0 = null_space(np.vstack(Pr))
Qb = np.hstack([Wobs, V0])
C1, C2 = rand_spd(Wobs.shape[1]), rand_spd(V0.shape[1])
C_p_dec = Qb @ np.block([[C1, np.zeros((C1.shape[0], C2.shape[0]))], [np.zeros((C2.shape[0], C1.shape[0])), C2]]) @ Qb.T
Lam_d = lam_alpha * np.linalg.inv(C_p_dec) + sum(Pr[h].T @ Wh[h] @ Pr[h] for h in range(Hr))
eta_d = lam_alpha * np.linalg.inv(C_p_dec) @ xi_p + sum(Pr[h].T @ om[h] for h in range(Hr))
m_d = np.linalg.solve(Lam_d, eta_d)
C_d = lam_alpha * np.linalg.inv(Lam_d)
report("no pinning: posterior V0-marginal equals the prior V0-marginal",
       rel(V0.T @ m_d, V0.T @ xi_p) + rel(V0.T @ C_d @ V0, V0.T @ C_p_dec @ V0), 1e-11)
# Predictive limit with tied orthonormal measurements and equal channel covariances.
Qo, _ = np.linalg.qr(rng.standard_normal((Kt, Kt)))
O_blocks = [Qo[:, h * dt:(h + 1) * dt] for h in range(Ht)]
T_blocks = [rng.standard_normal((dt, Kt)) for _ in range(Ht)]
Cc = rand_spd(Kt)
xb = rng.standard_normal((N_src, Kt))
bp = rng.dirichlet(np.ones(N_src), size=Ht)
tiny = 1e-10
Lam_l = tiny * np.eye(Kt)
eta_l = np.zeros(Kt)
for h in range(Ht):
    Rh = T_blocks[h] @ Cc @ T_blocks[h].T + varsigma2 * np.eye(dt)
    Lam_l += O_blocks[h] @ np.linalg.inv(Rh) @ O_blocks[h].T
    eta_l += O_blocks[h] @ np.linalg.inv(Rh) @ sum(bp[h, j] * T_blocks[h] @ xb[j] for j in range(N_src))
pred = sum(O_blocks[h] @ sum(bp[h, j] * T_blocks[h] @ xb[j] for j in range(N_src)) for h in range(Ht))
report("predictive limit: flat prior, tied orthonormal maps, equal R give the head sum",
       rel(np.linalg.solve(Lam_l, eta_l), pred), 1e-8)

# Exact natural-parameter flow of the quadratic family (full covariance).
cH = 1.7
Lq = rand_spd(4, 2.0)
eq = rng.standard_normal(4)
m0 = rng.standard_normal(4)
S0 = rand_spd(4)


def flow_rhs(m, S):
    return -S @ (Lq @ m - eq), cH * S - S @ Lq @ S


m_, S_ = m0.copy(), S0.copy()
dt_ode, t_end = 1e-4, 0.7
for _ in range(int(round(t_end / dt_ode))):
    k1 = flow_rhs(m_, S_)
    k2 = flow_rhs(m_ + dt_ode / 2 * k1[0], S_ + dt_ode / 2 * k1[1])
    k3 = flow_rhs(m_ + dt_ode / 2 * k2[0], S_ + dt_ode / 2 * k2[1])
    k4 = flow_rhs(m_ + dt_ode * k3[0], S_ + dt_ode * k3[1])
    m_ = m_ + dt_ode / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
    S_ = S_ + dt_ode / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
rho_t = 1 - np.exp(-cH * t_end)
J = (1 - rho_t) * np.linalg.inv(S0) + rho_t * Lq / cH
hvec = (1 - rho_t) * np.linalg.inv(S0) @ m0 + rho_t * eq / cH
report("natural-parameter interpolation solves the Fisher flow", rel(S_, np.linalg.inv(J)) + rel(m_, np.linalg.solve(J, hvec)), 1e-9)


def quad_energy(m, S, Lm=Lq, em=eq, cm=cH):
    return 0.5 * np.trace(Lm @ S) + 0.5 * m @ Lm @ m - em @ m - 0.5 * cm * np.linalg.slogdet(S)[1]


vals = []
for rr in np.linspace(0, 1, 21):
    Jr = (1 - rr) * np.linalg.inv(S0) + rr * Lq / cH
    hr = (1 - rr) * np.linalg.inv(S0) @ m0 + rr * eq / cH
    vals.append(quad_energy(np.linalg.solve(Jr, hr), np.linalg.inv(Jr)))
report("frozen energy is nonincreasing along the damped full-family update", max(0.0, max(np.diff(vals))), 1e-12)

# Profiled per-coordinate self-coupling on the diagonal family: majorize-minimize descent.
Kd = 5
b0, c0 = 1.0, 1.0
worst_mm = -np.inf
for trial in range(300):
    Lg_ = rand_spd(Kd, rng.uniform(0.2, 3.0))
    eg_ = rng.standard_normal(Kd)
    mu_p = rng.standard_normal(Kd)
    pvar = rng.uniform(0.2, 3.0, Kd)
    mu = mu_p + rng.standard_normal(Kd)
    sv = rng.uniform(0.2, 3.0, Kd)

    def Dk(m, s_):
        return 0.5 * (s_ / pvar + (m - mu_p) ** 2 / pvar - 1 - np.log(s_ / pvar))

    def E_prof(m, s_):
        return float(np.sum(c0 * np.log(b0 + Dk(m, s_))) + 0.5 * np.sum(np.diag(Lg_) * s_) + 0.5 * m @ Lg_ @ m - eg_ @ m)

    for it in range(4):
        alpha_k = c0 / (b0 + Dk(mu, sv))
        Lam_k = Lg_ + np.diag(alpha_k / pvar)
        eta_k = eg_ + alpha_k * mu_p / pvar
        mu_new = np.linalg.solve(Lam_k, eta_k)
        s_new = alpha_k / np.diag(Lam_k)
        worst_mm = max(worst_mm, E_prof(mu_new, s_new) - E_prof(mu, sv))
        mu_only = E_prof(mu_new, sv) - E_prof(mu, sv)
        worst_mm = max(worst_mm, mu_only)
        mu, sv = mu_new, s_new
report("profiled per-coordinate MM step never increases the profiled energy (max increase)", max(worst_mm, 0.0), 1e-10)
# At an episode start with q equal to the layer prior, alpha = c0/b0 and the step is a Kalman update.
Lg_ = rand_spd(Kd)
eg_ = rng.standard_normal(Kd)
mu_in = rng.standard_normal(Kd)
p_in = rng.uniform(0.3, 2.0, Kd)
alpha0 = c0 / (b0 + 0.0)
mu_plus = np.linalg.solve(Lg_ + np.diag(alpha0 / p_in), eg_ + alpha0 * mu_in / p_in)
kalman = mu_in + np.linalg.solve(np.diag(1 / p_in) + Lg_, eg_ - Lg_ @ mu_in)
report("q = p at episode start: one closed-form step is the Kalman update of the incoming mean", rel(mu_plus, kalman), 1e-12)
# Damped diagonal interpolation can increase the frozen energy (counterexample).
Lx = np.array([[1.0, 0.99], [0.99, 1.0]])
ex = np.zeros(2)
m_x = np.array([5.0, -5.0])
s_x = np.array([0.5, 2.0])


def diag_energy(m, s_):
    return 0.5 * np.sum(np.diag(Lx) * s_) + 0.5 * m @ Lx @ m - 0.5 * np.sum(np.log(s_))


rho_x = 0.5
J_star = np.diag(Lx) / 1.0
mu_star_x = np.linalg.solve(Lx, ex)
Jd = (1 - rho_x) / s_x + rho_x * J_star
s_d = 1 / Jd
m_d_ = s_d * ((1 - rho_x) * m_x / s_x + rho_x * J_star * mu_star_x)
before, after, full = diag_energy(m_x, s_x), diag_energy(m_d_, s_d), diag_energy(mu_star_x, 1 / J_star)
print(f"    damped diagonal counterexample: {before:.3f} -> {after:.3f} (rho=1/2), {full:.3f} (rho=1)")
report("damped diagonal counterexample values 1.500 -> 2.503, rho=1 gives 1.000",
       abs(before - 1.5) + abs(after - 2.503) + abs(full - 1.0), 2e-3)
# Gauge covariance of the receiver closed form (full family).
Ug = rand_gl(Kr)
Lam_loc = np.linalg.inv(Ug).T @ Lam @ np.linalg.inv(Ug)
eta_loc = np.linalg.inv(Ug).T @ eta
report("local closed form is the frame image of the reference closed form",
       rel(np.linalg.solve(Lam_loc, eta_loc), Ug @ m_star) + rel(lam_alpha * np.linalg.inv(Lam_loc), Ug @ C_star @ Ug.T), 1e-11)

# ----------------------------------------------------------------------------------------------
# Moment-matched predictive covariance with persistence coefficient r in {0, 1} (Monte Carlo)
# ----------------------------------------------------------------------------------------------
Km, Hm, dm_, Nm = 4, 2, 2, 3
Tm = rng.standard_normal((Hm * dm_, Km))
Om = rng.standard_normal((Km, Hm * dm_))
Mh = [Om[:, h * dm_:(h + 1) * dm_] @ Tm[h * dm_:(h + 1) * dm_] for h in range(Hm)]
xs = rng.standard_normal((Nm, Km))
Cs = [rand_spd(Km) for _ in range(Nm)]
bm = rng.dirichlet(np.ones(Nm), size=Hm)
ir = Nm - 1
for r_res in (0, 1):
    Catt = np.zeros((Km, Km))
    if r_res:
        Catt += Cs[ir] + sum(bm[h, ir] * (Mh[h] @ Cs[ir] + Cs[ir] @ Mh[h].T) for h in range(Hm))
    for j in range(Nm):
        for h in range(Hm):
            for g in range(Hm):
                cw = bm[h, j] if h == g else bm[h, j] * bm[g, j]
                Catt += cw * Mh[h] @ Cs[j] @ Mh[g].T
    for h in range(Hm):
        nbar = sum(bm[h, j] * Mh[h] @ xs[j] for j in range(Nm))
        Catt += sum(bm[h, j] * np.outer(Mh[h] @ xs[j], Mh[h] @ xs[j]) for j in range(Nm)) - np.outer(nbar, nbar)
    n_mc = 400000
    labels = np.stack([rng.choice(Nm, size=n_mc, p=bm[h]) for h in range(Hm)])
    states = np.stack([rng.multivariate_normal(xs[j], Cs[j], size=n_mc) for j in range(Nm)])  # (Nm, n, K)
    out = r_res * states[ir].copy()
    for h in range(Hm):
        chosen = states[labels[h], np.arange(n_mc)]
        out = out + chosen @ Mh[h].T
    emp = np.cov(out.T)
    report(f"moment-matched covariance, r={r_res}, against Monte Carlo (relative)", rel(emp, Catt), 2e-2)

print()
n_fail = sum(1 for *_, ok in results if not ok)
print(f"{len(results)} checks, {n_fail} failed")
