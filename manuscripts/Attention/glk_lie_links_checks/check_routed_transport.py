r"""Float64 checks of the identities written by W3 (Section 3, Appendix B, Supplement S1-S3).

Small sizes only (K=6, H=3 heads of width 2, N=4 positions). Every check prints the maximal
absolute or relative residual. The checks test formulas; they carry no information about trained
models.

Notation follows PLAN.md Section 3: L = O T is the shared generator, Theta_ij = U_i e^L U_j^{-1},
Omega_ij = U_i U_j^{-1}, M_h = Otilde_h T_h, Pi_h = T^{-1} Delta_h T, Pi(beta) = T^{-1} bbeta T.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import expm, logm, block_diag

rng = np.random.default_rng(20261005)
K, H, N = 6, 3, 4
s = [2, 2, 2]
offs = np.cumsum([0] + s)
results: list[tuple[str, float]] = []


def rec(name: str, val: float) -> None:
    results.append((name, float(val)))


def rel(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(a - b) / max(1.0, np.linalg.norm(b)))


def phi1(Z: np.ndarray) -> np.ndarray:
    r"""\varphi_1(Z)=\sum_{n\ge1} Z^{n-1}/n!, via the augmented exponential."""
    n = Z.shape[0]
    A = np.zeros((2 * n, 2 * n))
    A[:n, :n] = Z
    A[:n, n:] = np.eye(n)
    return expm(A)[:n, n:]


def phi1_series(Z: np.ndarray, terms: int = 60) -> np.ndarray:
    out = np.zeros_like(Z)
    P = np.eye(Z.shape[0])
    fact = 1.0
    for n in range(1, terms):
        fact *= n
        out = out + P / fact
        P = P @ Z
    return out


def rand_inv(n: int, scale: float = 1.0) -> np.ndarray:
    return np.eye(n) + scale * rng.standard_normal((n, n)) / np.sqrt(n)


def Delta(h: int) -> np.ndarray:
    D = np.zeros((K, K))
    D[offs[h]:offs[h + 1], offs[h]:offs[h + 1]] = np.eye(s[h])
    return D


def bbeta(b: np.ndarray) -> np.ndarray:
    """Head-diagonal routing matrix oplus_h beta^(h) I_{s_h}."""
    return block_diag(*[b[h] * np.eye(s[h]) for h in range(H)])


# ---------------- data ----------------
T = rng.standard_normal((K, K))            # stacked sending map, invertible a.s.
O = 0.7 * rng.standard_normal((K, K))      # stacked stored receiving factor
L = O @ T
Ti = np.linalg.inv(T)
U = [rand_inv(K, 0.6) for _ in range(N)]
Ui = [np.linalg.inv(u) for u in U]
mu = [rng.standard_normal(K) for _ in range(N)]
xi = [Ui[j] @ mu[j] for j in range(N)]
# causal routing, positive on support j <= i, one row-stochastic row per head
beta = np.zeros((H, N, N))
for h in range(H):
    for i in range(N):
        w = rng.random(i + 1) + 0.05
        beta[h, i, : i + 1] = w / w.sum()

Theta = lambda i, j: U[i] @ expm(L) @ Ui[j]
Omega = lambda i, j: U[i] @ Ui[j]

# ---------------- Lemma lem:lie_lowrank ----------------
A = rng.standard_normal((K, 2))
B = rng.standard_normal((2, K))
rec("lem:lie_lowrank  e^{AB} = I + A phi1(BA) B", rel(expm(A @ B), np.eye(K) + A @ phi1(B @ A) @ B))
rec("eq:lie_augmented  phi1 (augmented) vs series", rel(phi1(B @ A), phi1_series(B @ A)))

# ---------------- Prop prop:lie_split (one head, s_h=2) ----------------
Th = T[offs[0]:offs[1], :]
Oh = O[:, offs[0]:offs[1]]
Lh = Oh @ Th
i, j = 2, 1
lhs = U[i] @ expm(Lh) @ Ui[j]
rhs = Omega(i, j) + U[i] @ Oh @ phi1(Th @ Oh) @ Th @ Ui[j]
rec("prop:lie_split  Theta = Omega + U_i O_h phi1(T_h O_h) T_h U_j^-1", rel(lhs, rhs))
kerT = np.linalg.svd(Th)[2][2:].T          # basis of ker T_h
rec("prop:lie_split item 1  e^{O_hT_h} = id on ker T_h", np.abs(expm(Lh) @ kerT - kerT).max())
Pim = Oh @ np.linalg.pinv(Oh)
rec("prop:lie_split item 2  im(e^{L_h}-I) in im O_h", np.abs((np.eye(K) - Pim) @ (expm(Lh) - np.eye(K))).max())
rec("prop:lie_split item 4  det", abs(np.linalg.det(lhs) - np.linalg.det(U[i] @ Ui[j]) * np.exp(np.trace(Th @ Oh))) / abs(np.linalg.det(lhs)))

# ---------------- Theorem thm:routed_transport ----------------
Pi = [Ti @ Delta(h) @ T for h in range(H)]
err = 0.0
for h in range(H):
    err = max(err, np.abs(Pi[h] - Ti[:, offs[h]:offs[h + 1]] @ T[offs[h]:offs[h + 1], :]).max())
    for g in range(H):
        err = max(err, np.abs(Pi[h] @ Pi[g] - (Pi[h] if g == h else 0)).max())
err = max(err, np.abs(sum(Pi) - np.eye(K)).max())
rec("thm item 1  Pi_h = (T^-1)_{:,h} T_h, Pi_h Pi_g = delta Pi_h, sum = I", err)
# ker / im relations
err = 0.0
for h in range(H):
    Thh = T[offs[h]:offs[h + 1], :]
    kerTh = np.linalg.svd(Thh)[2][s[h]:].T
    err = max(err, np.abs(Pi[h] @ kerTh).max())                     # ker T_h in ker Pi_h
    imPi = Pi[h] @ rng.standard_normal((K, 3))
    for g in range(H):
        if g != h:
            err = max(err, np.abs(T[offs[g]:offs[g + 1], :] @ imPi).max())  # im Pi_h in ker T_g
    err = max(err, abs(np.linalg.matrix_rank(Pi[h]) - s[h]))
rec("thm item 1  ker Pi_h = ker T_h, im Pi_h = cap_{g!=h} ker T_g (inclusions + rank)", err)

b = beta[:, 3, 1]
PiB = Ti @ bbeta(b) @ T
rec("thm item 1  T^-1 bbeta T = sum_h beta^(h) Pi_h", np.abs(PiB - sum(b[h] * Pi[h] for h in range(H))).max())
ev = np.sort(np.linalg.eigvals(PiB).real)
rec("thm item 1  eig Pi(beta) = beta^(h) with multiplicity s_h", np.abs(ev - np.sort(np.repeat(b, s))).max())
rec("thm item 1  det Pi(beta) = prod beta^(h)^{s_h}", abs(np.linalg.det(PiB) - np.prod(b ** np.array(s))) / np.prod(b ** np.array(s)))

# charts
Ot = {
    "affine": O,
    "first-order": Ti + O,
    "exponential": expm(L) @ Ti,
}
f = {"affine": L, "first-order": np.eye(K) + L, "exponential": expm(L)}
for c in Ot:
    rec(f"thm item 2  [{c}] Otilde T = f(L)", rel(Ot[c] @ T, f[c]))
rec("thm item 2  e^L T^-1 = T^-1 + O phi1(TO)", rel(expm(L) @ Ti, Ti + O @ phi1(T @ O)))
rec("thm item 2  T Otilde = e^{TO}", rel(T @ Ot["exponential"], expm(T @ O)))
rec("thm item 2  det(T Otilde) = e^{tr TO} > 0", abs(np.linalg.det(T @ Ot["exponential"]) / np.exp(np.trace(T @ O)) - 1.0))

# routed edge map and message, all charts, all receivers
for c in Ot:
    e1 = e2 = 0.0
    for i in range(N):
        m_def = np.zeros(K)
        m_thm = np.zeros(K)
        m_heads = np.zeros(K)
        for j in range(i + 1):
            bb = bbeta(beta[:, i, j])
            Mdef = U[i] @ Ot[c] @ bb @ T @ Ui[j]                         # eq:main_routed_link
            Mthm = U[i] @ f[c] @ (Ti @ bb @ T) @ Ui[j]                    # U_i f(L) Pi(beta) U_j^-1
            e1 = max(e1, rel(Mdef, Mthm))
            m_def += Mdef @ mu[j]
            m_thm += Mthm @ mu[j]
            for h in range(H):
                Oth = Ot[c][:, offs[h]:offs[h + 1]]
                m_heads += beta[h, i, j] * U[i] @ Oth @ T[offs[h]:offs[h + 1], :] @ Ui[j] @ mu[j]
        e2 = max(e2, rel(m_def, m_thm), rel(m_def, m_heads))
    rec(f"thm item 3  [{c}] calM_ij = U_i f(L) Pi(beta_ij) U_j^-1", e1)
    rec(f"thm item 3  [{c}] m_i forms agree (incl. head sum eq:lie_tiled)", e2)

# exponential chart factorization and invertibility
e1 = e2 = 0.0
dmin = np.inf
for i in range(N):
    for j in range(i + 1):
        bb = bbeta(beta[:, i, j])
        Mexp = U[i] @ Ot["exponential"] @ bb @ T @ Ui[j]
        fac = Theta(i, j) @ U[j] @ (Ti @ bb @ T) @ Ui[j]
        e1 = max(e1, rel(Mexp, fac))
        ref = expm(L) @ Ti @ bb @ T
        d = np.linalg.det(ref)
        pred = np.exp(np.trace(L)) * np.prod(beta[:, i, j] ** np.array(s))
        e2 = max(e2, abs(d / pred - 1.0))
        dmin = min(dmin, d)
rec("thm item 4  calM_ij = Theta_ij U_j Pi(beta_ij) U_j^-1", e1)
rec("thm item 4  det(e^L Pi(beta)) = e^{tr L} prod beta^{s_h}", e2)
rec("thm item 4  min det of reference rep (must be > 0)", dmin)

# shared routing: hopping form, affine and first-order forms
e = 0.0
for i in range(N):
    mh = np.zeros(K)
    ma = np.zeros(K)
    mf = np.zeros(K)
    mh_def = np.zeros(K)
    ma_def = np.zeros(K)
    mf_def = np.zeros(K)
    for j in range(i + 1):
        bsh = beta[0, i, j]
        bb = bbeta(np.full(H, bsh))
        mh += bsh * Theta(i, j) @ mu[j]
        ma += bsh * U[i] @ L @ Ui[j] @ mu[j]
        mf += bsh * (Omega(i, j) + U[i] @ L @ Ui[j]) @ mu[j]
        mh_def += U[i] @ Ot["exponential"] @ bb @ T @ Ui[j] @ mu[j]
        ma_def += U[i] @ Ot["affine"] @ bb @ T @ Ui[j] @ mu[j]
        mf_def += U[i] @ Ot["first-order"] @ bb @ T @ Ui[j] @ mu[j]
    e = max(e, rel(mh_def, mh), rel(ma_def, ma), rel(mf_def, mf))
rec("thm item 4  shared routing: sum beta Theta mu, sum beta U_i L U_j^-1 mu, sum beta U_i(I+L)U_j^-1 mu", e)

# orders
sc = 0.37
bb = bbeta(beta[:, 3, 2])
PiB = Ti @ bb @ T
Os = sc * O
Ots = Ti + Os @ phi1(T @ Os)
series = Ti.copy()
fact = 1.0
P = np.eye(K)
for n in range(1, 40):
    fact *= n
    series = series + sc ** n / fact * O @ P
    P = P @ (T @ O)
rec("thm item 5  eq:lie_orders series of Otilde(s)", rel(Ots, series))
orders = [np.linalg.matrix_power(sc * L, n) / np.prod(np.arange(1, n + 1)) @ PiB for n in range(40)]
rec("thm item 5  sum_n (sL)^n/n! Pi(beta) = e^{sL} Pi(beta)", rel(sum(orders), expm(sc * L) @ PiB))
rec("thm item 5  order 0 = sum_h beta Pi_h", np.abs(orders[0] - sum(beta[h, 3, 2] * Pi[h] for h in range(H))).max())
rec("thm item 5  order 1 = s O bbeta T", rel(orders[1], sc * O @ bb @ T))
o2 = 0.5 * sc ** 2 * O @ (T @ O) @ bb @ T
o2b = 0.5 * sc ** 2 * sum(O[:, offs[g]:offs[g + 1]] @ (T[offs[g]:offs[g + 1], :] @ O[:, offs[h]:offs[h + 1]]) * beta[h, 3, 2] @ T[offs[h]:offs[h + 1], :]
                          for g in range(H) for h in range(H))
rec("thm item 5  order 2 = 1/2 O(TO) bbeta T = 1/2 sum O_g(T_gO_h)beta^h T_h", max(rel(orders[2], o2), rel(o2, o2b)))
e = 0.0
for i in range(N):
    m0 = sum(U[i] @ (Ti @ bbeta(np.full(H, beta[0, i, j])) @ T) @ xi[j] for j in range(i + 1))
    m0b = sum(beta[0, i, j] * Omega(i, j) @ mu[j] for j in range(i + 1))
    e = max(e, rel(m0, m0b))
rec("thm item 5  shared routing: zeroth order = sum beta Omega mu", e)

# no residual (O invertible): complement projector = I, Otilde = O e^{TO}(TO)^{-1} = e^{OT} T^{-1}
TO = T @ O
Pc = O @ np.linalg.inv(TO) @ T
rec("thm item 6  O(TO)^-1 T = I for tiled invertible O,T", np.abs(Pc - np.eye(K)).max())
rec("thm item 6  O e^{TO}(TO)^-1 = e^{OT} T^-1", rel(O @ expm(TO) @ np.linalg.inv(TO), expm(L) @ Ti))

# gauge covariance of calM and m
g = [rand_inv(K, 0.5) for _ in range(N)]
gi = [np.linalg.inv(x) for x in g]
e = 0.0
for i in range(N):
    for j in range(i + 1):
        bb = bbeta(beta[:, i, j])
        M0 = U[i] @ Ot["exponential"] @ bb @ T @ Ui[j]
        M1 = (g[i] @ U[i]) @ Ot["exponential"] @ bb @ T @ np.linalg.inv(g[j] @ U[j])
        e = max(e, rel(M1, g[i] @ M0 @ gi[j]))
rec("covariance  calM'_ij = g_i calM_ij g_j^-1", e)

# ---------------- Supplement S1: complement split, non-tiled (K=6, sbar=4) ----------------
Tn = rng.standard_normal((4, K))
On = rng.standard_normal((K, 4))
TOn = Tn @ On
Pn = On @ np.linalg.inv(TOn) @ Tn
rec("S1 lem:lie_complement  e^{OT} = (I-Pi) + O e^{TO}(TO)^-1 T", rel(expm(On @ Tn), np.eye(K) - Pn + On @ expm(TOn) @ np.linalg.inv(TOn) @ Tn))
# sigma_min bound
worst = np.inf
for _ in range(200):
    X = rng.standard_normal((K, K)) * rng.uniform(0.1, 3)
    worst = min(worst, np.linalg.svd(expm(X), compute_uv=False)[-1] - np.exp(-np.linalg.norm(X, 2)))
rec("S1  min over 200 of sigma_min(e^X) - e^{-||X||_2} (must be >= 0)", worst)
Z = np.array([[-1.0, -1.0], [1.0, -1.0]])
rec("S1  I + Z + Z^2/2 singular at stated Z (|det|)", abs(np.linalg.det(np.eye(2) + Z + Z @ Z / 2)))

# ---------------- prop:lie_charts and Upsilon (general s=3) ----------------
Tc = rng.standard_normal((3, K))
Oc = rng.standard_normal((K, 3))
TOc = Tc @ Oc
Pc3 = Oc @ np.linalg.inv(TOc) @ Tc
Ups = lambda Bm: np.eye(K) - Pc3 + Oc @ Bm @ np.linalg.inv(TOc) @ Tc
B1, B2 = rand_inv(3), rand_inv(3)
rec("lem:lie_embed  Upsilon homomorphism", rel(Ups(B1) @ Ups(B2), Ups(B1 @ B2)))
rec("lem:lie_embed  det Upsilon(B) = det B", abs(np.linalg.det(Ups(B1)) / np.linalg.det(B1) - 1))
C = rng.standard_normal((3, 3))
rec("prop:lie_charts item 1  I + OCT = Upsilon(I + C TO)", rel(np.eye(K) + Oc @ C @ Tc, Ups(np.eye(3) + C @ TOc)))
rec("prop:lie_charts item 2  e^{OT} = Upsilon(e^{TO})", rel(expm(Oc @ Tc), Ups(expm(TOc))))
Olin = 0.3 * rng.standard_normal((K, 3))
Zc = logm(np.eye(3) + Tc @ Olin).real
Oconv = Olin @ np.linalg.inv(phi1(Zc))
rec("prop:lie_charts item 3  TO = Z", rel(Tc @ Oconv, Zc))
rec("prop:lie_charts item 3  e^{OT} = I + O_lin T", rel(expm(Oconv @ Tc), np.eye(K) + Olin @ Tc))

# ---------------- Standard layer at fixed routing (joint level) ----------------
Mh = [O[:, offs[h]:offs[h + 1]] @ T[offs[h]:offs[h + 1], :] for h in range(H)]  # W_O^h W_V^h
rec("std  sum_h M_h = OT", rel(sum(Mh), L))
rec("std  max rank of a single head map (K/H = 2)", max(np.linalg.matrix_rank(m) for m in Mh))
frakL = np.zeros((N * K, N * K))
for i in range(N):
    for j in range(N):
        blk = sum(beta[h, i, j] * Mh[h] for h in range(H))
        frakL[i * K:(i + 1) * K, j * K:(j + 1) * K] = U[i] @ blk @ Ui[j]
Xs = np.concatenate(mu)
Xnew = (np.eye(N * K) + frakL) @ Xs
e = 0.0
for i in range(N):
    ma = mu[i] + sum(U[i] @ O @ bbeta(beta[:, i, j]) @ T @ Ui[j] @ mu[j] for j in range(i + 1))
    e = max(e, rel(Xnew[i * K:(i + 1) * K], ma))
rec("std  (I + frakL_beta) X = affine chart with c_res = 1, per receiver", e)
upper = max(np.abs(frakL[i * K:(i + 1) * K, j * K:(j + 1) * K]).max() for i in range(N) for j in range(i + 1, N))
rec("std  frakL_beta block lower triangular (max strictly-upper block)", upper)
dprod = np.prod([np.linalg.det(np.eye(K) + sum(beta[h, i, i] * Mh[h] for h in range(H))) for i in range(N)])
rec("std  det(I+frakL) = prod_i det(I + sum_h beta_ii M_h)", abs(np.linalg.det(np.eye(N * K) + frakL) / dprod - 1))
rec("std  token-0 self block = I + OT (beta_00 = 1)", rel(sum(beta[h, 0, 0] * Mh[h] for h in range(H)), L))
# principal log is block lower triangular when no self-block eigenvalue on (-inf,0]
frak_small = 0.15 * frakL
Jt = np.eye(N * K) + frak_small
selfev = np.concatenate([np.linalg.eigvals(Jt[i * K:(i + 1) * K, i * K:(i + 1) * K]) for i in range(N)])
neg_axis = np.any((np.abs(selfev.imag) < 1e-12) & (selfev.real <= 0))
Lg = logm(Jt)
upper_log = max(np.abs(Lg[i * K:(i + 1) * K, j * K:(j + 1) * K]).max() for i in range(N) for j in range(i + 1, N))
rec("std  self-block eigenvalue on (-inf,0] (0 = none)", float(neg_axis))
rec("std  principal log of I + frakL block lower triangular (max strictly-upper block)", upper_log)
rec("std  exp(log(I+frakL)) = I + frakL", rel(expm(Lg), Jt))
# exp(frakL) composes multi-hop paths: (frakL^2)_{ik} = sum_j frakL_ij frakL_jk differs from per-edge exponential
e_joint = expm(frakL)[3 * K:4 * K, 1 * K:2 * K]
e_edge = U[3] @ expm(L) @ Ti @ bbeta(beta[:, 3, 1]) @ T @ Ui[1]
rec("std  ||exp(frakL)_{31} - per-edge exponential message map|| (expected O(1), not 0)", rel(e_joint, e_edge))

# ---------------- holonomy (Section 3.5, Supplement S3) ----------------
i, j, k = 3, 2, 0
Hijk = np.linalg.inv(Theta(i, k)) @ Theta(i, j) @ Theta(j, k)
rec("3.5  shared generator: H_ijk = U_k e^L U_k^-1", rel(Hijk, U[k] @ expm(L) @ Ui[k]))
rec("3.5  Theta_ij = Theta_ii Omega_ij", rel(Theta(i, j), (U[i] @ expm(L) @ Ui[i]) @ Omega(i, j)))
rec("3.5  M^(h)_ij = M^(h)_ii Omega_ij", rel(U[i] @ Mh[0] @ Ui[j], (U[i] @ Mh[0] @ Ui[i]) @ Omega(i, j)))
rec("3.5  flat identification has trivial triangle holonomy", rel(np.linalg.inv(Omega(i, k)) @ Omega(i, j) @ Omega(j, k), np.eye(K)))
# triangle spectrum (S3 prop:lie_triangle_spectrum), exponential chart, TO != I
Me = lambda a, c: U[a] @ Ot["exponential"] @ bbeta(beta[:, a, c]) @ T @ Ui[c]
Hr = np.linalg.inv(Me(i, k)) @ Me(i, j) @ Me(j, k)
rho = beta[:, i, j] * beta[:, j, k] / beta[:, i, k]
ev1 = np.sort_complex(np.linalg.eigvals(Hr))
ev2 = np.sort_complex(np.linalg.eigvals(bbeta(rho) @ expm(T @ O)))
rec("S3 prop:lie_triangle_spectrum  spec(H) = spec(rho e^{TO})", np.abs(ev1 - ev2).max() / np.abs(ev2).max())
rec("S3  log|det H| = sum_h s_h log rho_h + tr(TO)", abs(np.log(abs(np.linalg.det(Hr))) - (np.dot(s, np.log(rho)) + np.trace(T @ O))))
# BCH second order
eps = 1e-2
Ag, Bg, Zg = (eps * rng.standard_normal((K, K)) for _ in range(3))
lhs = logm(expm(-Zg) @ expm(Ag) @ expm(Bg)).real
com = lambda a, c: a @ c - c @ a
rhs = (Ag + Bg - Zg) + 0.5 * (com(Ag, Bg) - com(Zg, Ag) - com(Zg, Bg))
rem2 = np.linalg.norm(lhs - rhs)
lhs3 = logm(expm(-Zg / 10) @ expm(Ag / 10) @ expm(Bg / 10)).real
rhs3 = (Ag + Bg - Zg) / 10 + 0.5 * (com(Ag, Bg) - com(Zg, Ag) - com(Zg, Bg)) / 100
rec("S3 lem:lie_bch  third-order remainder at generator scale 1e-2", rem2)
rec("S3 lem:lie_bch  remainder ratio for scale 1e-2 vs 1e-3 (cubic: ~1e3)", rem2 / np.linalg.norm(lhs3 - rhs3))
# head-sum row of tab:lie_holonomy with TO = I
Tq = rng.standard_normal((K, K))
Oq = np.linalg.inv(Tq)
Mq = lambda a, c: U[a] @ Oq @ bbeta(beta[:, a, c]) @ Tq @ Ui[c]
Hq = np.linalg.inv(Mq(i, k)) @ Mq(i, j) @ Mq(j, k)
pred = U[k] @ Oq @ np.linalg.inv(bbeta(beta[:, i, k])) @ bbeta(beta[:, i, j]) @ bbeta(beta[:, j, k]) @ Tq @ Ui[k]
rec("S3 tab:lie_holonomy head-sum row (TO=I)", rel(Hq, pred))
# shear blindness
Sh = np.eye(K)
Sh[0, 1] = 1.0
rec("S3 prop:lie_blind  eigenvalues of shear all 1 (max |lambda-1|)", np.abs(np.linalg.eigvals(Sh) - 1).max())
rec("S3 prop:lie_blind  Psi(shear) = 1/2", 0.5 * np.linalg.norm(Sh - np.eye(K)) ** 2)

# ---------------- Supplement S2: Gaussian lift reduces to S_Q^{-1} for square S_Q ----------------
SQ = rand_inv(K)
SK = rng.standard_normal((K, K))
Cm = rng.standard_normal((K, K))
Cm = Cm @ Cm.T + K * np.eye(K)
RQ = Cm @ SQ.T @ np.linalg.inv(SQ @ Cm @ SQ.T)
rec("S2  R_{Q,i} = S_Q^{-1} for square invertible S_Q", rel(RQ, np.linalg.inv(SQ)))
Mcmp = U[i] @ RQ @ SK @ Ui[j]
Thcmp = U[i] @ np.linalg.inv(SQ) @ SK @ Ui[j]
rec("S2  M^cmp_ij = Theta^cmp_ij for square invertible S_Q", rel(Mcmp, Thcmp))
# rectangular lift: S_Q R = I and minimal C^{-1}-norm
SQr = rng.standard_normal((3, K))
Rr = Cm @ SQr.T @ np.linalg.inv(SQr @ Cm @ SQr.T)
rec("S2  S_Q R_{Q,i} = I_{r_h} (rectangular)", np.abs(SQr @ Rr - np.eye(3)).max())
y = rng.standard_normal(3)
d0 = Rr @ y
kerS = np.linalg.svd(SQr)[2][3:].T
w = kerS @ rng.standard_normal(K - 3)
Ci = np.linalg.inv(Cm)
rec("S2  lift is C^{-1}-orthogonal to ker S_Q", abs(d0 @ Ci @ w))
# K=2 example of prop:link_algebra
rec("S2  K=2 example det diag(b1,b2) > 0", np.linalg.det(np.diag([0.3, 0.7])))

width = max(len(n) for n, _ in results)
for n, v in results:
    print(f"{n:<{width}}  {v: .3e}")
