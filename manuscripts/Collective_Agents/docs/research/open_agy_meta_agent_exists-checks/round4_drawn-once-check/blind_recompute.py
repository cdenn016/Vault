r"""Blind recomputation for fixed-attention audience patterns (spec.md in this folder).

Model. World eta_{t+1} = F eta_t + w_t, w_t ~ N(0, Q). Every agent a runs a steady-state
Kalman filter for x_t = (eta_t, eta_{t-1}) with x_{t+1} = A x_t + G w_t, A = [[F,0],[1,0]],
G = (1,0)^T, and computation noise c_a(t) ~ N(0, q_c I_2) added to the predicted mean.
Round t observations of agent a:
    own      s_a(t)    = eta_t     + v_a(t),                       H = [1,0], var R_a,
    message  y_aj(t)   = s_j(t-1)  + nu_aj(t) = eta_{t-1} + v_j(t-1) + nu_aj(t),
                                                                     H = [0,1], var R_j + R_c.
Prior error eps_a(t) = m^-_a(t) - x_t obeys
    eps_a(t+1) = M_a eps_a(t) + A K_a n_a(t) + c_a(t) - G w_t,   M_a = A (I - K_a H_a).
World-conditional law: condition on the world path only (w), so -G w_t goes to the mean; the
sensing noises v (shared by a sender and its receivers), nu and c are random.

Route 1 (float64): joint state X(t) = (eps_0..eps_4 (2 each), v_0(t-1)..v_4(t-1)) in R^15,
    X(t+1) = cA X(t) + cB xi(t),  Sigma_X = cA Sigma_X cA^T + cB Q_xi cB^T  (Kronecker solve).
Route 2 (mpmath, 50 digits): pairwise Stein equations. eps_a responds to v_m(t - tau) with
    M_a^{tau - d} A k_a^{(m)},  d = 1 (own sensor, m = a), d = 2 (message from m),
so Cov(eps_a, eps_b) = sum_{m shared} R_m X_m,  X_m = M_a X_m M_b^T + u w^T, with
u = M_a^{D-d_a} A k_a^{(m)}, w = M_b^{D-d_b} A k_b^{(m)}, D = max(d_a, d_b), and
Var(eps_a) = X,  X = M_a X M_a^T + A K_a R_obs K_a^T A^T + q_c I.
Contrast coordinates e_a = eps_{a,0}. Contrast per 04_collectives.tex eq. (col-rates).
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"

import itertools
import json
import time
from typing import Any

import mpmath as mp
import numpy as np
import scipy.linalg as sla

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 50

F_S, Q_S, QC_S = "0.9", "0.05", "0.0001"
RS_S, RM_S, RC_S = "0.01", "1", "0.002"
LABEL = ["S", "1", "2", "3", "4"]
N_AG = 5
MEMBERS = (1, 2, 3, 4)
A_SET = frozenset(MEMBERS)

LINES: list[str] = []


def log(s: str = "") -> None:
    print(s, flush=True)
    LINES.append(s)


# ----------------------------------------------------------------------------------------
# Steady-state Kalman filters
# ----------------------------------------------------------------------------------------
def filt_np(R_own: float, R_msgs: tuple[float, ...], F: float, Q: float, qc: float) -> dict[str, Any]:
    r"""Steady-state prior covariance P^- (DARE), gain K = P^- H^T (H P^- H^T + R)^{-1}, M = A(I-KH)."""
    A = np.array([[F, 0.0], [1.0, 0.0]])
    H = np.array([[1.0, 0.0]] + [[0.0, 1.0]] * len(R_msgs))
    Robs = np.diag([R_own] + list(R_msgs))
    Qx = np.diag([Q + qc, qc])
    P = sla.solve_discrete_are(A.T, H.T, Qx, Robs)  # prior covariance P^-
    P = 0.5 * (P + P.T)
    S = H @ P @ H.T + Robs
    K = P @ H.T @ np.linalg.inv(S)  # (2, 1+|J|)
    M = A @ (np.eye(2) - K @ H)
    # residual of the Riccati equation in the explicit prediction-update form
    Ppost = (np.eye(2) - K @ H) @ P
    res = np.abs(A @ Ppost @ A.T + Qx - P).max()
    return dict(A=A, H=H, Robs=Robs, P=P, K=K, M=M, res=res, rho=max(abs(np.linalg.eigvals(M))))


def filt_mp(R_own: Any, R_msgs: tuple[Any, ...], F: Any, Q: Any, qc: Any) -> dict[str, Any]:
    r"""Same filter in mpmath by fixed-point iteration of the Riccati recursion to 1e-45."""
    A = mp.matrix([[F, 0], [1, 0]])
    rows = [[1, 0]] + [[0, 1]] * len(R_msgs)
    H = mp.matrix(rows)
    m = len(rows)
    Robs = mp.zeros(m, m)
    Robs[0, 0] = R_own
    for i, r in enumerate(R_msgs):
        Robs[i + 1, i + 1] = r
    Qx = mp.matrix([[Q + qc, 0], [0, qc]])
    P = Qx.copy()
    I2 = mp.eye(2)
    for it in range(200000):
        S = H * P * H.T + Robs
        K = P * H.T * mp.inverse(S)
        Pn = A * ((I2 - K * H) * P) * A.T + Qx
        Pn = (Pn + Pn.T) / 2
        d = mp.mnorm(Pn - P, 1)
        P = Pn
        if d < mp.mpf("1e-46"):
            break
    S = H * P * H.T + Robs
    K = P * H.T * mp.inverse(S)
    M = A * (I2 - K * H)
    return dict(A=A, H=H, Robs=Robs, P=P, K=K, M=M, iters=it)


# ----------------------------------------------------------------------------------------
# Patterns
# ----------------------------------------------------------------------------------------
def family_patterns(k: int) -> list[tuple[tuple[int, ...], ...]]:
    """All patterns: member i reads a k-subset of the four other agents. Index 0 is S (reads nothing)."""
    choices = []
    for i in MEMBERS:
        others = [j for j in range(N_AG) if j != i]
        choices.append([tuple(c) for c in itertools.combinations(others, k)])
    pats = []
    for combo in itertools.product(*choices):
        pats.append(((),) + tuple(combo))
    return pats


def pat_str(p: tuple[tuple[int, ...], ...]) -> str:
    return " ".join(f"{LABEL[i]}<-{{{','.join(LABEL[j] for j in p[i])}}}" for i in MEMBERS)


def canon(p: tuple[tuple[int, ...], ...]) -> tuple:
    """Canonical form under relabeling of members (S fixed)."""
    best = None
    for perm in itertools.permutations(MEMBERS):
        mp_ = {0: 0}
        for old, new in zip(MEMBERS, perm):
            mp_[old] = new
        q = [None] * N_AG
        q[0] = ()
        for i in MEMBERS:
            q[mp_[i]] = tuple(sorted(mp_[j] for j in p[i]))
        q = tuple(q)
        if best is None or q < best:
            best = q
    return best


def support_sets(p) -> list[frozenset[int]]:
    """S_a = {a} cup J_a: the sensing noises that enter e_a."""
    return [frozenset({a}) | frozenset(p[a]) for a in range(N_AG)]


# ----------------------------------------------------------------------------------------
# Route 1: joint 15-dimensional Lyapunov equation (float64)
# ----------------------------------------------------------------------------------------
def joint_lyapunov_np(p, Rsens: list[float], Rc: float, F: float, Q: float, qc: float,
                      cache: dict, conditioned_v: frozenset[int] = frozenset()) -> tuple[np.ndarray, dict]:
    r"""Solve Sigma_X = cA Sigma_X cA^T + W for X=(eps_0..eps_4, v_0(t-1)..v_4(t-1)).

    Sensing noises in `conditioned_v` are put in the conditioning set (their variance removed
    from W only; filters still use their true variance). Returns the 10x10 eps covariance."""
    filts = {}
    for a in range(N_AG):
        key = (Rsens[a], tuple(sorted(Rsens[j] + Rc for j in p[a])))
        if key not in cache:
            cache[key] = filt_np(key[0], key[1], F, Q, qc)
        filts[a] = cache[key]
    D = 2 * N_AG + N_AG
    cA = np.zeros((D, D))
    W = np.zeros((D, D))
    for a in range(N_AG):
        f = filts[a]
        Aa, K, M = f["A"], f["K"], f["M"]
        cA[2 * a:2 * a + 2, 2 * a:2 * a + 2] = M
        msgR = sorted(Rsens[j] + Rc for j in p[a])
        for j in p[a]:
            col = 1 + msgR.index(Rsens[j] + Rc)
            b = Aa @ K[:, col]
            cA[2 * a:2 * a + 2, 2 * N_AG + j] = b  # message at next round carries v_j(t-1)
            W[2 * a:2 * a + 2, 2 * a:2 * a + 2] += Rc * np.outer(b, b)  # receiver-specific nu_aj
        W[2 * a:2 * a + 2, 2 * a:2 * a + 2] += qc * np.eye(2)  # computation noise
    for m in range(N_AG):
        if m in conditioned_v:
            continue
        u = np.zeros(D)
        u[2 * m:2 * m + 2] = filts[m]["A"] @ filts[m]["K"][:, 0]  # own-sensor use at round t
        u[2 * N_AG + m] = 1.0  # stored for the receivers' next round
        W += Rsens[m] * np.outer(u, u)
    # Kronecker (row-major vec): vec(cA X cA^T) = kron(cA, cA) vec(X)
    L = np.eye(D * D) - np.kron(cA, cA)
    X = np.linalg.solve(L, W.reshape(-1)).reshape(D, D)
    X = 0.5 * (X + X.T)
    resid = np.abs(cA @ X @ cA.T + W - X).max()
    return X[:2 * N_AG, :2 * N_AG], dict(resid=resid, rho=max(abs(np.linalg.eigvals(cA))))


# ----------------------------------------------------------------------------------------
# Route 2: pairwise Stein equations (mpmath)
# ----------------------------------------------------------------------------------------
def stein_mp(Ma, Mb, C):
    r"""Solve X = Ma X Mb^T + C (2x2) via (I - kron(Ma, Mb)) vec_row(X) = vec_row(C)."""
    Kr = mp.zeros(4, 4)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    Kr[2 * i + j, 2 * k + l] = Ma[i, k] * Mb[j, l]
    L = mp.eye(4) - Kr
    c = mp.matrix([C[0, 0], C[0, 1], C[1, 0], C[1, 1]])
    x = mp.lu_solve(L, c)
    return mp.matrix([[x[0], x[1]], [x[2], x[3]]])


class MPModel:
    """Caches filters and Stein blocks keyed by filter type and noise role."""

    def __init__(self, Rsens: list[Any], Rc: Any, F: Any, Q: Any, qc: Any):
        self.Rsens, self.Rc, self.F, self.Q, self.qc = Rsens, Rc, F, Q, qc
        self.fcache: dict = {}
        self.vcache: dict = {}
        self.wcache: dict = {}
        self.ccache: dict = {}

    def fkey(self, p, a):
        return (self.Rsens[a], tuple(sorted(self.Rsens[j] + self.Rc for j in p[a])))

    def filt(self, key):
        if key not in self.fcache:
            self.fcache[key] = filt_mp(key[0], key[1], self.F, self.Q, self.qc)
        return self.fcache[key]

    def var_block(self, key):
        r"""World-conditional Var(eps_a): X = M X M^T + A K R_obs K^T A^T + q_c I."""
        if key not in self.vcache:
            f = self.filt(key)
            C = f["A"] * f["K"] * f["Robs"] * f["K"].T * f["A"].T + self.qc * mp.eye(2)
            self.vcache[key] = stein_mp(f["M"], f["M"], C)
        return self.vcache[key]

    def world_block(self, key):
        r"""World-driven part: Y = M Y M^T + G Q G^T (for the check P^- = X + Y)."""
        if key not in self.wcache:
            f = self.filt(key)
            C = mp.matrix([[self.Q, 0], [0, 0]])
            self.wcache[key] = stein_mp(f["M"], f["M"], C)
        return self.wcache[key]

    def resp(self, key, role):
        """(delay, vector A k) for role 'own' or ('msg', Rmsg)."""
        f = self.filt(key)
        if role == "own":
            col, d = 0, 1
        else:
            col, d = 1 + list(key[1]).index(role[1]), 2
        b = f["A"] * f["K"][:, col]
        return d, b

    def cross_unit(self, ka, ra, kb, rb):
        ck = (ka, ra, kb, rb)
        if ck not in self.ccache:
            fa, fb = self.filt(ka), self.filt(kb)
            da, ba = self.resp(ka, ra)
            db, bb = self.resp(kb, rb)
            Dm = max(da, db)
            u = ba
            for _ in range(Dm - da):
                u = fa["M"] * u
            w = bb
            for _ in range(Dm - db):
                w = fb["M"] * w
            self.ccache[ck] = stein_mp(fa["M"], fb["M"], u * w.T)
        return self.ccache[ck]

    def sigma_blocks(self, p, conditioned_v: frozenset[int] = frozenset()):
        """10x10 world-conditional covariance of the prior errors (2x2 blocks)."""
        Sg = mp.zeros(2 * N_AG, 2 * N_AG)
        keys = [self.fkey(p, a) for a in range(N_AG)]
        sup = support_sets(p)
        for a in range(N_AG):
            for b in range(a, N_AG):
                if a == b:
                    B = self.var_block(keys[a])
                    if conditioned_v:
                        for m in conditioned_v & sup[a]:
                            role = "own" if m == a else ("msg", self.Rsens[m] + self.Rc)
                            B = B - self.Rsens[m] * self.cross_unit(keys[a], role, keys[a], role)
                else:
                    B = mp.zeros(2, 2)
                    for m in sorted(sup[a] & sup[b]):
                        if m in conditioned_v:
                            continue
                        ra = "own" if m == a else ("msg", self.Rsens[m] + self.Rc)
                        rb = "own" if m == b else ("msg", self.Rsens[m] + self.Rc)
                        B = B + self.Rsens[m] * self.cross_unit(keys[a], ra, keys[b], rb)
                for i in range(2):
                    for j in range(2):
                        Sg[2 * a + i, 2 * b + j] = B[i, j]
                        Sg[2 * b + j, 2 * a + i] = B[i, j]
        return Sg


def first_components(Sg) -> Any:
    S5 = mp.zeros(N_AG, N_AG)
    for a in range(N_AG):
        for b in range(N_AG):
            S5[a, b] = Sg[2 * a, 2 * b]
    return S5


# ----------------------------------------------------------------------------------------
# Precision, diffusivity, contrast, substitute selector
# ----------------------------------------------------------------------------------------
def components(S5, n=N_AG):
    adj = {a: [b for b in range(n) if b != a and S5[a, b] != 0] for a in range(n)}
    seen, comps = set(), []
    for a in range(n):
        if a in seen:
            continue
        stack, comp = [a], []
        seen.add(a)
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        comps.append(sorted(comp))
    return comps


def precision_mp(S5):
    """Inverse by connected components of the support graph (exact zeros between components)."""
    Pi = mp.zeros(N_AG, N_AG)
    for comp in components(S5):
        sub = mp.matrix([[S5[i, j] for j in comp] for i in comp])
        inv = mp.inverse(sub)
        for ii, i in enumerate(comp):
            for jj, j in enumerate(comp):
                Pi[i, j] = inv[ii, jj]
    for i in range(N_AG):
        for j in range(i + 1, N_AG):
            s = (Pi[i, j] + Pi[j, i]) / 2
            Pi[i, j] = s
            Pi[j, i] = s
    return Pi


def diffusive_info(Pi) -> dict[str, Any]:
    offs = [(Pi[i, j], i, j) for i in range(N_AG) for j in range(i + 1, N_AG)]
    rows = [sum(Pi[i, j] for j in range(N_AG)) for i in range(N_AG)]
    max_off = max(o[0] for o in offs)
    min_row = min(rows)
    scale = max(Pi[i, i] for i in range(N_AG))
    tiny = mp.mpf("1e-35") * scale
    near = [(float(o[0] / scale), LABEL[o[1]], LABEL[o[2]]) for o in offs if o[0] != 0 and abs(o[0]) < tiny]
    near += [(float(r / scale), "row", LABEL[i]) for i, r in enumerate(rows) if abs(r) < tiny]
    diff = (max_off <= tiny) and (min_row >= -tiny)
    return dict(diffusive=bool(diff), max_off=max_off, min_row=min_row, scale=scale, near=near, rows=rows)


def helmert(n: int) -> np.ndarray:
    U = np.zeros((n, n - 1))
    for k in range(1, n):
        U[:k, k - 1] = 1.0
        U[k, k - 1] = -k
        U[:, k - 1] /= np.sqrt(k * (k + 1))
    return U


HELM = {n: helmert(n) for n in range(2, N_AG + 1)}


def contrast_np(Pi: np.ndarray, C: tuple[int, ...]) -> tuple[float, float, float, float]:
    r"""r(C) = xin/xout; xout = phi^T Pi phi; xin = min_{f perp 1_C} f^T(diag(eps)+L_C)f/f^Tf.

    diag(eps)+L_C = Pi_CC - diag(a^partial), a^partial_i = sum_{k notin C} (-Pi_ik).
    Returns (r, xin, xout, xout_alt) with xout_alt = mean leak + cut/n."""
    idx = list(C)
    n = len(idx)
    out = [k for k in range(Pi.shape[0]) if k not in C]
    PCC = Pi[np.ix_(idx, idx)]
    apart = -Pi[np.ix_(idx, out)].sum(axis=1) if out else np.zeros(n)
    B = PCC - np.diag(apart)
    xout = PCC.sum() / n
    eps = Pi.sum(axis=1)
    xout_alt = eps[idx].mean() + apart.sum() / n
    U = HELM[n]
    xin = np.linalg.eigvalsh(U.T @ B @ U).min()
    return xin / xout, xin, xout, xout_alt


def contrast_mp(Pi, C):
    idx = list(C)
    n = len(idx)
    out = [k for k in range(N_AG) if k not in C]
    PCC = mp.matrix([[Pi[i, j] for j in idx] for i in idx])
    B = PCC.copy()
    for ii, i in enumerate(idx):
        B[ii, ii] -= -sum((Pi[i, k] for k in out), mp.mpf(0))
    xout = sum(PCC[i, j] for i in range(n) for j in range(n)) / n
    U = mp.matrix(HELM[n].shape[0], HELM[n].shape[1])
    for k in range(1, n):
        nrm = mp.sqrt(k * (k + 1))
        for i in range(k):
            U[i, k - 1] = 1 / nrm
        U[k, k - 1] = -k / nrm
    T = U.T * B * U
    if n == 2:
        xin = T[0, 0]
    else:
        E = mp.eigsy(T, eigvals_only=True)
        xin = min(E[i] for i in range(E.rows))
    return xin / xout


REGIONS = [tuple(c) for k in range(2, N_AG + 1) for c in itertools.combinations(range(N_AG), k)]
A_TUP = (1, 2, 3, 4)
BIPART = [(tuple(b2), tuple(sorted(set(range(N_AG)) - set(b2)))) for b2 in itertools.combinations(range(N_AG), 2)]


def reg_str(C) -> str:
    return "{" + ",".join(LABEL[i] for i in C) + "}"


def selector_mp(S5, sup) -> tuple[Any, list]:
    r"""max over balanced (2|3) bipartitions of mean within-block MI / mean between-block MI.

    MI_ab = -1/2 ln(1 - rho_ab^2); exactly 0 when S_a cap S_b is empty (structurally uncorrelated)."""
    MI = {}
    for a in range(N_AG):
        for b in range(a + 1, N_AG):
            if not (sup[a] & sup[b]):
                MI[(a, b)] = mp.mpf(0)
            else:
                rho = S5[a, b] / mp.sqrt(S5[a, a] * S5[b, b])
                MI[(a, b)] = -mp.log(1 - rho ** 2) / 2
    vals = []
    for b2, b3 in BIPART:
        within = [MI[tuple(sorted(pq))] for blk in (b2, b3) for pq in itertools.combinations(blk, 2)]
        between = [MI[tuple(sorted((x, y)))] for x in b2 for y in b3]
        w = sum(within) / len(within)
        bt = sum(between) / len(between)
        if bt == 0:
            v = mp.inf if w > 0 else mp.nan
        else:
            v = w / bt
        vals.append(v)
    finite_or_inf = [v for v in vals if not mp.isnan(v)]
    best = max(finite_or_inf) if finite_or_inf else mp.nan
    return best, vals, MI


# ----------------------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------------------
def run_family(name: str, pats, model: MPModel, npcache: dict, Rs_np, params_np, r0: float,
               special: dict[str, Any]) -> dict[str, Any]:
    t0 = time.time()
    recs = []
    max_dev = 0.0
    max_resid = 0.0
    for p in pats:
        Sg_np, info = joint_lyapunov_np(p, Rs_np, params_np["Rc"], params_np["F"], params_np["Q"],
                                        params_np["qc"], npcache)
        Sg_mp = model.sigma_blocks(p)
        Sg_mp_np = np.array(Sg_mp.tolist(), dtype=float)
        dev = np.abs(Sg_np - Sg_mp_np).max() / np.abs(Sg_mp_np).max()
        max_dev = max(max_dev, dev)
        max_resid = max(max_resid, info["resid"])
        S5 = first_components(Sg_mp)
        sup = support_sets(p)
        Pi = precision_mp(S5)
        dinfo = diffusive_info(Pi)
        sel, selvals, MI = selector_mp(S5, sup)
        Pi_np = np.array(Pi.tolist(), dtype=float)
        rec = dict(p=p, S5=S5, Pi=Pi, Pi_np=Pi_np, diff=dinfo, sel=sel, selvals=selvals, MI=MI)
        if dinfo["diffusive"]:
            rs = {}
            for C in REGIONS:
                r, xin, xout, xalt = contrast_np(Pi_np, C)
                assert abs(xout - xalt) <= 1e-10 * abs(xout)
                rs[C] = r
            rec["r"] = rs
            rec["rmax"] = max(rs.values())
            rec["argmax"] = max(rs, key=rs.get)
        recs.append(rec)
    log(f"[{name}] {len(pats)} patterns, wall {time.time() - t0:.1f}s; "
        f"max rel. dev joint-Lyapunov(float64) vs pairwise-Stein(mp50) over 10x10 eps covariances = {max_dev:.2e}; "
        f"max Lyapunov residual = {max_resid:.2e}")
    return dict(recs=recs, max_dev=max_dev)


def fmt(x, d=12) -> str:
    if isinstance(x, mp.mpf) or isinstance(x, mp.mpc):
        if mp.isinf(x):
            return "inf"
        if mp.isnan(x):
            return "nan"
        return mp.nstr(x, d)
    return f"{x:.{d}g}"


def mat_str(M, d=10) -> str:
    rows = []
    for i in range(M.rows):
        rows.append("  [" + ", ".join(f"{mp.nstr(M[i, j], d):>16}" for j in range(M.cols)) + "]")
    return "\n".join(rows)


def report_pattern(rec, title: str) -> None:
    p = rec["p"]
    log(f"--- {title}: {pat_str(p)}")
    log("Sigma^c (rows/cols S,1,2,3,4):")
    log(mat_str(rec["S5"]))
    log("Pi^c:")
    log(mat_str(rec["Pi"]))
    d = rec["diff"]
    log(f"diffusive = {d['diffusive']}; max off-diagonal = {fmt(d['max_off'])}; min row sum = {fmt(d['min_row'])}")
    log("row sums (leaks eps^Pi): " + ", ".join(fmt(x, 10) for x in d["rows"]))
    if d["diffusive"]:
        rA = contrast_mp(rec["Pi"], A_TUP)
        log(f"r(A) [mp50] = {fmt(rA, 15)};  r(A) [float64] = {rec['r'][A_TUP]:.15g}")
        lk = [d["rows"][i] for i in A_TUP]
        log(f"leak heterogeneity on A eps_max/eps_mean = {fmt(max(lk) / (sum(lk) / 4), 10)}")
        top = sorted(rec["r"].items(), key=lambda kv: -kv[1])[:6]
        log("largest regional contrasts: " + "; ".join(f"{reg_str(C)}={v:.10g}" for C, v in top))
    log(f"substitute selector = {fmt(rec['sel'], 15)}")
    log("bipartition ratios: " + "; ".join(f"{reg_str(b2)}|{reg_str(b3)}={fmt(v, 8)}"
                                           for (b2, b3), v in zip(BIPART, rec["selvals"])))


def summarize(name: str, fam: dict, r0: float, thr: float, mi_ref: Any, mi_ref_name: str) -> dict[str, Any]:
    recs = fam["recs"]
    drecs = [r for r in recs if r["diff"]["diffusive"]]
    log(f"\n===== {name} summary =====")
    log(f"number of patterns = {len(recs)}; diffusive = {len(drecs)}")
    near = [(pat_str(r["p"]), r["diff"]["near"]) for r in recs if r["diff"]["near"]]
    log(f"patterns with an off-diagonal or row sum within 1e-35*scale of 0 (nonzero): {len(near)}")
    for s, n in near[:10]:
        log(f"   {s}: {n}")
    # margins of the diffusive classification
    mo = sorted(recs, key=lambda r: abs(r["diff"]["max_off"] / r["diff"]["scale"]))
    nd_margin = min((r["diff"]["max_off"] / r["diff"]["scale"] for r in recs if not r["diff"]["diffusive"]
                     and r["diff"]["max_off"] > 0), default=None)
    d_margin = max((r["diff"]["max_off"] / r["diff"]["scale"] for r in drecs), default=None)
    minrow = min((r["diff"]["min_row"] / r["diff"]["scale"] for r in drecs), default=None)
    log(f"smallest positive (max off-diag / max diag) among non-diffusive = {fmt(nd_margin, 6) if nd_margin is not None else None}")
    log(f"largest (max off-diag / max diag) among diffusive = {fmt(d_margin, 6) if d_margin is not None else None}")
    log(f"smallest (min row sum / max diag) among diffusive = {fmt(minrow, 6) if minrow is not None else None}")
    nonpos_row_nd = sum(1 for r in recs if not r["diff"]["diffusive"] and r["diff"]["max_off"] <= 0)
    log(f"non-diffusive because of a negative row sum only: {nonpos_row_nd}")
    out: dict[str, Any] = dict(n_diffusive=len(drecs))
    # orbits
    orb: dict = {}
    for r in recs:
        orb.setdefault(canon(r["p"]), []).append(r)
    dorb = {k: v for k, v in orb.items() if v[0]["diff"]["diffusive"]}
    log(f"orbits under member relabeling: {len(orb)}; diffusive orbits: {len(dorb)}")
    # consistency within orbits
    worst = 0.0
    for k, v in orb.items():
        s0 = v[0]["sel"]
        for r in v[1:]:
            if mp.isinf(s0) or mp.isnan(s0):
                assert (mp.isinf(r["sel"]) and mp.isinf(s0)) or (mp.isnan(r["sel"]) and mp.isnan(s0))
            else:
                worst = max(worst, float(abs(r["sel"] - s0)))
            if v[0]["diff"]["diffusive"]:
                assert r["diff"]["diffusive"]
                worst = max(worst, abs(r["rmax"] - v[0]["rmax"]) / v[0]["rmax"] * 1e-0)
    log(f"max within-orbit discrepancy (selector abs / rmax rel) = {worst:.2e}")
    # item 3
    if drecs:
        rm_sorted = sorted(drecs, key=lambda r: -r["rmax"])
        log("diffusive patterns by largest regional contrast (top 12 patterns):")
        for r in rm_sorted[:12]:
            log(f"   rmax={r['rmax']:.12g} at {reg_str(r['argmax'])}  r(A)={r['r'][A_TUP]:.12g}  {pat_str(r['p'])}")
        # distinct values (orbits)
        dist = []
        for k, v in dorb.items():
            dist.append((v[0]["rmax"], len(v), v[0], k))
        dist.sort(key=lambda x: -x[0])
        log("five largest distinct values of the largest regional contrast (orbit size, attaining region, representative):")
        for val, sz, r, k in dist[:5]:
            rmp = contrast_mp(r["Pi"], r["argmax"])
            log(f"   {val:.12g} [mp50 {fmt(rmp, 14)}]  orbit size {sz}  region {reg_str(r['argmax'])}  rep: {pat_str(r['p'])}")
            for rr in orb[k]:
                log(f"        member of orbit: {pat_str(rr['p'])}")
        out["top5_distinct"] = [float(x[0]) for x in dist[:5]]
        out["top5_patterns"] = [float(r["rmax"]) for r in rm_sorted[:5]]
        # threshold count with margin
        n_ge = sum(1 for r in drecs if r["rmax"] >= thr)
        closest = min(drecs, key=lambda r: abs(r["rmax"] - thr))
        cl_mp = contrast_mp(closest["Pi"], closest["argmax"])
        log(f"patterns with largest regional contrast >= {thr}: {n_ge}; closest value to the threshold: "
            f"{closest['rmax']:.12g} [mp50 {fmt(cl_mp, 14)}] ({pat_str(closest['p'])})")
        out["n_rmax_ge_thr"] = n_ge
        # item 4
        n_exact = 0
        closest_gap = None
        for r in drecs:
            S = {C for C, v in r["r"].items() if v >= r0}
            if S == {A_TUP}:
                n_exact += 1
            for C, v in r["r"].items():
                g = abs(v - r0)
                if closest_gap is None or g < closest_gap[0]:
                    closest_gap = (g, v, C, r)
        log(f"diffusive patterns whose regions with r >= {r0} are exactly {{A}}: {n_exact}")
        g, v, C, r = closest_gap
        vmp = contrast_mp(r["Pi"], C)
        log(f"   closest regional contrast to r0 over all diffusive patterns/regions: {v:.12g} [mp50 {fmt(vmp, 14)}] "
            f"region {reg_str(C)} in {pat_str(r['p'])}")
        out["n_exactly_A"] = n_exact
        # distribution of which region sets
        setcount: dict = {}
        for r in drecs:
            S = tuple(sorted(reg_str(C) for C, v in r["r"].items() if v >= r0))
            setcount[S] = setcount.get(S, 0) + 1
        log(f"   region sets with r >= {r0} among diffusive patterns (set: count): " +
            "; ".join(f"{list(k)}: {c}" for k, c in sorted(setcount.items(), key=lambda kv: -kv[1])))
    # item 5
    sels = [r["sel"] for r in recs]
    n_inf = sum(1 for s in sels if mp.isinf(s))
    n_nan = sum(1 for s in sels if mp.isnan(s))
    fin = sorted([s for s in sels if not (mp.isinf(s) or mp.isnan(s))])
    allv = sorted([s for s in sels if not mp.isnan(s)], key=lambda x: (mp.isinf(x), x))
    nn = len(allv)
    if nn % 2 == 1:
        med = allv[nn // 2]
    else:
        lo, hi = allv[nn // 2 - 1], allv[nn // 2]
        med = mp.inf if (mp.isinf(lo) or mp.isinf(hi)) else (lo + hi) / 2
    log(f"substitute selector: min = {fmt(fin[0], 15)}, median = {fmt(med, 15)} (order stats {fmt(allv[nn // 2 - 1], 15)}, "
        f"{fmt(allv[nn // 2], 15)}), max = {'inf' if n_inf else fmt(fin[-1], 15)}, max finite = {fmt(fin[-1], 15)}, "
        f"#inf = {n_inf}, #undefined(0/0) = {n_nan}")
    tol = mp.mpf("1e-30")
    n_ge = sum(1 for s in sels if (not mp.isnan(s)) and (mp.isinf(s) or s >= mi_ref - tol))
    n_gt = sum(1 for s in sels if (not mp.isnan(s)) and (mp.isinf(s) or s > mi_ref + tol))
    n_tie = n_ge - n_gt
    nearest = sorted([s for s in fin if abs(s - mi_ref) > tol], key=lambda s: abs(s - mi_ref))[:3]
    log(f"selector >= {mi_ref_name} ({fmt(mi_ref, 15)}): {n_ge}  [strictly greater: {n_gt}; equal to 1e-30: {n_tie}]; "
        f"nearest non-tied values: {[fmt(s, 15) for s in nearest]}")
    out.update(mi_min=fin[0], mi_median=med, mi_max_finite=fin[-1], n_inf=n_inf, n_nan=n_nan,
               n_mi_ge=n_ge, n_mi_gt=n_gt, n_mi_tie=n_tie)
    # selector and diffusivity cross-tab
    return out


def main() -> None:
    t_start = time.time()
    F, Q, qc = mp.mpf(F_S), mp.mpf(Q_S), mp.mpf(QC_S)
    RS, RM, RC = mp.mpf(RS_S), mp.mpf(RM_S), mp.mpf(RC_S)
    Rs_mp = [RS, RM, RM, RM, RM]
    Rs_np = [float(x) for x in Rs_mp]
    pnp = dict(F=float(F), Q=float(Q), qc=float(qc), Rc=float(RC))
    log("Blind recomputation, fixed-attention audience patterns. mp.dps = 50.")
    log(f"F={F_S} Q={Q_S} q_c={QC_S} R_S={RS_S} R={RM_S} R_c={RC_S}")

    # ---------------- validation of contrast code on the compound-symmetric test value
    al, be, n = 1.0, 0.5, 4
    Sig = al * np.eye(n) + be * np.ones((n, n))
    Pi = np.linalg.inv(Sig)
    HELM_save = HELM
    r_test = None
    idx = tuple(range(n))
    PCC = Pi
    xout = PCC.sum() / n
    U = helmert(n)
    xin = np.linalg.eigvalsh(U.T @ PCC @ U).min()
    r_test = xin / xout
    Sig_mp = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            Sig_mp[i, j] = mp.mpf(1) * (i == j) + mp.mpf("0.5")
    log(f"[validation] compound symmetric alpha=1, beta=0.5, n=4, no cut: r = {r_test:.15g} (expected 3)")
    # also through the population-level routine on a 5-agent matrix with an isolated 5th agent (cut = 0)
    Sig5 = np.eye(5)
    Sig5[:4, :4] = Sig
    Sig5[4, 4] = 2.0
    Pi5 = np.linalg.inv(Sig5)
    Pi5[np.abs(Pi5) < 1e-15] = 0.0
    r5 = contrast_np(Pi5, (0, 1, 2, 3))[0]
    Pi5mp = mp.inverse(mp.matrix(Sig5.tolist()))
    r5mp = contrast_mp(Pi5mp, (0, 1, 2, 3))
    log(f"[validation] same block inside a 5-agent population (isolated 5th agent): r_float = {r5:.15g}, r_mp = {fmt(r5mp, 20)}")
    # a block with a cut: check xout = phi^T Pi phi = mean leak + cut/n, and the scalar n=2 formula
    rng = np.random.default_rng(1)
    G = rng.standard_normal((5, 5))
    Sg = G @ G.T + 5 * np.eye(5)
    Pr = np.linalg.inv(Sg)
    r, xin, xo, xa = contrast_np(Pr, (0, 2))
    a01 = -Pr[0, 2]
    eps = Pr.sum(axis=1)
    apar = [-(Pr[0, 1] + Pr[0, 3] + Pr[0, 4]), -(Pr[2, 0] * 0 + Pr[2, 1] + Pr[2, 3] + Pr[2, 4])]
    # for n=2: f = (1,-1)/sqrt2, f^T (diag(eps)+L_C) f = (eps0+eps2)/2 + 2 a02
    xin2 = (eps[0] + eps[2]) / 2 + 2 * a01
    log(f"[validation] random 5x5 precision, C={{0,2}}: xout {xo:.15g} vs mean-leak+cut/n {xa:.15g}; xin {xin:.15g} vs closed form {xin2:.15g}")

    # ---------------- filters
    model = MPModel(Rs_mp, RC, F, Q, qc)
    log("\n===== steady-state filters (mp50; float64 DARE cross-check) =====")
    fkeys = [(RS, ()), (RM, (RS + RC,)), (RM, (RM + RC,)), (RM, tuple(sorted((RS + RC, RM + RC)))),
             (RM, (RM + RC, RM + RC))]
    names = ["S (own only)", "member reads S", "member reads a member", "member reads S + member",
             "member reads two members"]
    for nm, k in zip(names, fkeys):
        f = model.filt(k)
        fn = filt_np(float(k[0]), tuple(float(x) for x in k[1]), float(F), float(Q), float(qc))
        Pm = np.array(f["P"].tolist(), dtype=float)
        V = model.var_block(k)
        Wb = model.world_block(k)
        chk = mp.mnorm(V + Wb - f["P"], 1)
        rho = max(abs(x) for x in mp.eig(f["M"])[0])
        log(f"{nm}: R_obs diag = {[mp.nstr(f['Robs'][i, i], 6) for i in range(f['Robs'].rows)]}, Riccati iters {f['iters']}")
        log(f"   P^- = [[{mp.nstr(f['P'][0, 0], 14)}, {mp.nstr(f['P'][0, 1], 14)}], [., {mp.nstr(f['P'][1, 1], 14)}]]"
            f"  |P^-_mp - P^-_scipy| = {np.abs(Pm - fn['P']).max():.1e}")
        log(f"   K = {[[mp.nstr(f['K'][i, j], 12) for j in range(f['K'].cols)] for i in range(2)]}")
        log(f"   rho(M) = {mp.nstr(rho, 10)};  world-conditional Var(eps) = [[{mp.nstr(V[0, 0], 14)}, {mp.nstr(V[0, 1], 12)}],"
            f" [., {mp.nstr(V[1, 1], 12)}]];  |Var_c + Var_world - P^-| = {mp.nstr(chk, 3)}")

    # ---------------- families
    fam1 = family_patterns(1)
    fam2 = family_patterns(2)
    allS = ((),) + tuple(((0,),) for _ in MEMBERS)
    allS = ((),) + ((0,), (0,), (0,), (0,))
    mate = ((), (0, 2), (0, 1), (0, 4), (0, 3))
    assert allS in fam1 and mate in fam2
    npcache: dict = {}
    log("\n===== Family 1: each member reads one other agent (256 patterns) =====")
    F1 = run_family("family 1", fam1, model, npcache, Rs_np, pnp, 4.5, {})
    rec_allS = [r for r in F1["recs"] if r["p"] == allS][0]
    report_pattern(rec_allS, "family 1 all-source pattern")
    mi_allS = rec_allS["sel"]
    S1 = summarize("family 1", F1, 4.5, 5.3724, mi_allS, "all-source value")

    log("\n===== Family 2: each member reads two other agents (1296 patterns) =====")
    F2 = run_family("family 2", fam2, model, npcache, Rs_np, pnp, 4.45, {})
    rec_mate = [r for r in F2["recs"] if r["p"] == mate][0]
    report_pattern(rec_mate, "family 2 all-S + mutual mate (1<->2, 3<->4)")
    # all 81 patterns 'S + one co-member'
    smates = [r for r in F2["recs"] if all(0 in r["p"][i] for i in MEMBERS)]
    log(f"all {len(smates)} patterns in which every member reads S and one co-member:")
    byorb: dict = {}
    for r in smates:
        byorb.setdefault(canon(r["p"]), []).append(r)
    for k, v in byorb.items():
        r = v[0]
        rA = r["r"][A_TUP] if r["diff"]["diffusive"] else None
        log(f"   orbit size {len(v):2d}  diffusive={r['diff']['diffusive']}  r(A)={'%.12g' % rA if rA is not None else 'undef'}"
            f"  selector={fmt(r['sel'], 12)}  rep: {pat_str(r['p'])}")
    S2 = summarize("family 2", F2, 4.45, 5.3724, mp.mpf("1.5"), "1.5")
    # same thresholds reported for family 1 too (done above), and the 1.5-count for family 1 as extra
    n15_f1 = sum(1 for r in F1["recs"] if (not mp.isnan(r["sel"])) and (mp.isinf(r["sel"]) or r["sel"] >= mp.mpf("1.5")))
    log(f"\n[extra] family 1 patterns with selector >= 1.5: {n15_f1}")

    # exact ties at 1.5 in family 2: list the structure
    ties = [r for r in F2["recs"] if (not mp.isinf(r["sel"])) and (not mp.isnan(r["sel"])) and abs(r["sel"] - mp.mpf("1.5")) < mp.mpf("1e-30")]
    log(f"[family 2] patterns with selector equal to 1.5 within 1e-30: {len(ties)}")
    for r in ties[:6]:
        log(f"   {pat_str(r['p'])}  selector-1.5 = {mp.nstr(r['sel'] - mp.mpf('1.5'), 5)}")

    # ---------------- negative controls
    log("\n===== Negative controls on the family-1 all-source pattern =====")
    log("(i) R_c x 100 = 0.2: expect weaker member-member correlation and r(A) far below the base value.")
    model_nc = MPModel(Rs_mp, RC * 100, F, Q, qc)
    Sg_nc = model_nc.sigma_blocks(allS)
    Sgn_np, info_nc = joint_lyapunov_np(allS, Rs_np, float(RC) * 100, float(F), float(Q), float(qc), {})
    dev_nc = np.abs(Sgn_np - np.array(Sg_nc.tolist(), dtype=float)).max()
    S5n = first_components(Sg_nc)
    Pin = precision_mp(S5n)
    dn = diffusive_info(Pin)
    seln, _, _ = selector_mp(S5n, support_sets(allS))
    log("Sigma^c:")
    log(mat_str(S5n))
    log(f"diffusive={dn['diffusive']}  r(A)={fmt(contrast_mp(Pin, A_TUP), 12) if dn['diffusive'] else 'undef'}  "
        f"selector={fmt(seln, 12)}  |joint-Lyapunov - Stein| = {dev_nc:.1e}")
    if dn["diffusive"]:
        rr = {C: float(contrast_mp(Pin, C)) for C in REGIONS}
        top = sorted(rr.items(), key=lambda kv: -kv[1])[:4]
        log("   largest regional contrasts: " + "; ".join(f"{reg_str(C)}={v:.8g}" for C, v in top))
    log("(ii) v_S added to the conditioning set (S's sensing noise treated as sender-side broadcast noise):"
        " expect member errors uncorrelated, Pi diagonal on A, r(A) = 1 exactly if leaks equal.")
    Sg_c = model.sigma_blocks(allS, conditioned_v=frozenset({0}))
    Sgc_np, _ = joint_lyapunov_np(allS, Rs_np, float(RC), float(F), float(Q), float(qc), {}, conditioned_v=frozenset({0}))
    dev_c = np.abs(Sgc_np - np.array(Sg_c.tolist(), dtype=float)).max()
    S5c = first_components(Sg_c)
    log(mat_str(S5c))
    Pic = precision_mp(S5c)
    log(f"r(A) = {fmt(contrast_mp(Pic, A_TUP), 15)};  |joint-Lyapunov - Stein| = {dev_c:.1e}")

    # ---------------- results json
    res = dict(
        f1_allsource=dict(Sigma=[[str(rec_allS['S5'][i, j]) for j in range(5)] for i in range(5)],
                          diffusive=rec_allS['diff']['diffusive'], rA=float(contrast_mp(rec_allS['Pi'], A_TUP)),
                          selector=float(mi_allS)),
        f2_mate=dict(Sigma=[[str(rec_mate['S5'][i, j]) for j in range(5)] for i in range(5)],
                     diffusive=rec_mate['diff']['diffusive'],
                     rA=float(contrast_mp(rec_mate['Pi'], A_TUP)) if rec_mate['diff']['diffusive'] else None,
                     selector=float(rec_mate['sel'])),
        f1={k: (float(v) if isinstance(v, mp.mpf) else v) for k, v in S1.items()},
        f2={k: (float(v) if isinstance(v, mp.mpf) else v) for k, v in S2.items()},
        max_dev_f1=F1["max_dev"], max_dev_f2=F2["max_dev"],
    )
    with open(os.path.join(OUT_DIR, "blind_recompute_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    log(f"\ntotal wall time {time.time() - t_start:.1f}s")
    with open(os.path.join(OUT_DIR, "blind_recompute_output.txt"), "w") as fh:
        fh.write("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
