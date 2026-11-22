r"""Counterexample search for claim C17c.

Setting: z_{t+1} = A z_t + E xi_t (stationary), ytil_t = C z_t + D xi_t + n_t, n_t white with cov Ry
(C = B Gamma, D = B Gamma_xi, n = B nu + w). Hypotheses imposed by construction:
  swap invariance of law(z, ytil) under P (blocks of members 0,1), S equivariant on the pair,
  private-law cross entry (S Cov(z0) S^T)_{01} = 0, k_0 != 0.
Computes
  Cov(z0)              = (1/2pi) int S_zz,
  Cov(E[z0|ytil])      = (1/2pi) int S_zy S_yy^{-1} S_yz      (two-sided Wiener smoother),
  Sigma^c              = S (Cov(z0) - Cov(E[z0|ytil])) S^T     (C17a form).
Checks: k_0 = k_1 for several factors K; Sigma^c_{01} = -|k_0|^2 < 0; Pi^c = (Sigma^c)^{-1} is a Z-matrix?
A counterexample would be an instance passing all hypothesis checks with Sigma^c_{01} >= 0, k_0 != k_1,
or Pi^c a Z-matrix.
"""
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import numpy as np

NF = 1024


def swapP(n: int, d: int) -> np.ndarray:
    P = np.eye(n * d)
    P[:2 * d, :2 * d] = 0
    P[0:d, d:2 * d] = np.eye(d)
    P[d:2 * d, 0:d] = np.eye(d)
    return P


def spectra(A, E, Q, C, D, Ry, nf=NF):
    nz = A.shape[0]
    w = 2 * np.pi * np.arange(nf) / nf
    zz = np.exp(-1j * w)[:, None, None]
    Hz = np.linalg.solve(np.eye(nz)[None] - A[None] * zz, E[None] * zz)  # (nf, nz, nxi)
    Hy = C[None] @ Hz + D[None]                                            # (nf, m, nxi)
    Szz = Hz @ Q[None] @ np.conj(np.transpose(Hz, (0, 2, 1)))
    Szy = Hz @ Q[None] @ np.conj(np.transpose(Hy, (0, 2, 1)))
    Syy = Hy @ Q[None] @ np.conj(np.transpose(Hy, (0, 2, 1))) + Ry[None]
    proj = Szy @ np.linalg.solve(Syy, np.conj(np.transpose(Szy, (0, 2, 1))))
    covz = Szz.mean(0).real
    covE = proj.mean(0).real
    return covz, covE, Szz, Szy


def lyap(A, E, Q):
    nz = A.shape[0]
    rhs = (E @ Q @ E.T).reshape(-1)
    return np.linalg.solve(np.eye(nz * nz) - np.kron(A, A), rhs).reshape(nz, nz)


def window_cond(A, E, Q, C, D, Ry, T):
    """Cov(z0 | ytil_{-T..T}) by finite Gaussian conditioning (time domain)."""
    nz, m = A.shape[0], C.shape[0]
    Sig = lyap(A, E, Q)

    def Gz(h):  # Cov(z_{t+h}, z_t)
        return np.linalg.matrix_power(A, h) @ Sig if h >= 0 else (np.linalg.matrix_power(A, -h) @ Sig).T

    def Czxi(h):  # Cov(z_t, xi_{t-h})
        return np.linalg.matrix_power(A, h - 1) @ E @ Q if h >= 1 else np.zeros((nz, Q.shape[0]))

    ts = range(-T, T + 1)
    L = len(ts)
    Gyy = np.zeros((L * m, L * m))
    Gzy = np.zeros((nz, L * m))
    for a, t in enumerate(ts):
        Gzy[:, a * m:(a + 1) * m] = Gz(0 - t) @ C.T + Czxi(0 - t) @ D.T
        for b, s in enumerate(ts):
            blk = C @ Gz(t - s) @ C.T + C @ Czxi(t - s) @ D.T + (C @ Czxi(s - t) @ D.T).T
            if t == s:
                blk = blk + D @ Q @ D.T + Ry
            Gyy[a * m:(a + 1) * m, b * m:(b + 1) * m] = blk
    return Sig - Gzy @ np.linalg.solve(Gyy, Gzy.T)


def factors(M, rng):
    lam, U = np.linalg.eigh(M)
    lam = np.clip(lam, 0, None)
    K1 = U * np.sqrt(lam)
    Qr, _ = np.linalg.qr(rng.standard_normal((M.shape[0], M.shape[0])))
    K2 = K1 @ Qr
    th = rng.uniform(0, 2 * np.pi)
    K3 = np.hstack([K1 * np.cos(th), K1 * np.sin(th)])            # non-square factor
    out = [K1, K2, K3]
    try:
        out.append(np.linalg.cholesky(M + 0 * np.eye(M.shape[0])))
    except np.linalg.LinAlgError:
        pass
    return out


def isotropic_vec(Msym, rng):
    """unit s with s^T Msym s = 0, if Msym indefinite; else None."""
    lam, U = np.linalg.eigh((Msym + Msym.T) / 2)
    if lam[0] >= -1e-9 or lam[-1] <= 1e-9:
        return None
    u, v = U[:, -1], U[:, 0]
    # alpha^2 lam_max + beta^2 lam_min = 0 ; add a random orthogonal component via generic mix
    a = np.sqrt(-lam[0]); b = np.sqrt(lam[-1])
    s = a * u + b * v * rng.choice([-1, 1])
    return s / np.linalg.norm(s)


def draw(rng, n, d, m, variant):
    nz = n * d
    P = swapP(n, d)
    A0 = rng.standard_normal((nz, nz))
    A = (A0 + P @ A0 @ P) / 2
    A *= rng.uniform(0.2, 0.95) / max(abs(np.linalg.eigvals(A)))
    # private inputs: block diagonal E and Q, members 0,1 identical blocks
    Eb = rng.standard_normal((d, d)); Qb = rng.standard_normal((d, d)); Qb = Qb @ Qb.T + 0.1 * np.eye(d)
    Eb2 = rng.standard_normal((d, d)); Qb2 = rng.standard_normal((d, d)); Qb2 = Qb2 @ Qb2.T + 0.1 * np.eye(d)
    E = np.zeros((nz, nz)); Q = np.zeros((nz, nz))
    for k in range(n):
        eb, qb = (Eb, Qb) if k < 2 else (Eb2, Qb2)
        E[k * d:(k + 1) * d, k * d:(k + 1) * d] = eb
        Q[k * d:(k + 1) * d, k * d:(k + 1) * d] = qb
    C0 = rng.standard_normal((m, nz)); C = (C0 + C0 @ P) / 2
    D0 = rng.standard_normal((m, nz)) * rng.choice([0.0, 1.0]); D = (D0 + D0 @ P) / 2
    R0 = rng.standard_normal((m, m)); Ry = R0 @ R0.T * rng.uniform(0.01, 2) + 0.02 * np.eye(m)
    Sig = lyap(A, E, Q)
    if variant == "general":
        s0 = isotropic_vec(Sig @ P, rng)
        if s0 is None:
            return None
        S = np.zeros((n, nz)); S[0] = s0; S[1] = P @ s0
        if n == 3:
            s2 = rng.standard_normal(nz); S[2] = (s2 + P @ s2) / 2
    else:  # local S
        if d == 1:
            # root-find a 0<->1 coupling theta so that Sig_{01} = 0
            Ac = np.zeros((nz, nz)); Ac[0, 1] = Ac[1, 0] = 1.0
            def cross(th):
                At = A + th * Ac
                if max(abs(np.linalg.eigvals(At))) >= 0.99:
                    return None
                return lyap(At, E, Q)[0, 1]
            grid = np.linspace(-1.5, 1.5, 61)
            vals = [cross(t) for t in grid]
            br = None
            for t0, t1, v0, v1 in zip(grid[:-1], grid[1:], vals[:-1], vals[1:]):
                if v0 is not None and v1 is not None and v0 * v1 < 0:
                    br = (t0, t1); break
            if br is None:
                return None
            lo, hi = br
            for _ in range(80):
                mid = (lo + hi) / 2
                if cross(lo) * cross(mid) <= 0: hi = mid
                else: lo = mid
            A = A + (lo + hi) / 2 * Ac
            Sig = lyap(A, E, Q)
            sig = np.array([rng.uniform(0.5, 2)])
        else:
            sig = isotropic_vec(Sig[0:d, d:2 * d], rng)
            if sig is None:
                return None
        S = np.zeros((n, nz)); S[0, 0:d] = sig; S[1, d:2 * d] = sig
        if n == 3:
            S[2, 2 * d:3 * d] = rng.standard_normal(d)
    return dict(A=A, E=E, Q=Q, C=C, D=D, Ry=Ry, S=S, P=P, Sig=Sig)


def evaluate(inst, rng, nf=NF):
    A, E, Q, C, D, Ry, S, P = (inst[k] for k in "A E Q C D Ry S P".split())
    covz, covE, Szz, Szy = spectra(A, E, Q, C, D, Ry, nf)
    # hypothesis checks
    h_swap = max(np.abs(P[None] @ Szy - Szy).max(), np.abs(P[None] @ Szz @ P[None] - Szz).max())
    h_equiv = np.abs((S @ P)[[0, 1]] - S[[1, 0]]).max()
    priv = S @ covz @ S.T
    h_priv = abs(priv[0, 1]) / np.sqrt(priv[0, 0] * priv[1, 1])
    lyap_err = np.abs(covz - inst["Sig"]).max()
    M = S @ covE @ S.T
    Sc = S @ (covz - covE) @ S.T
    kdiff = max(np.linalg.norm(K[0] - K[1]) for K in factors(M, rng))
    k0sq = M[0, 0]
    gap01 = (M[0, 0] + M[1, 1] - 2 * M[0, 1]) / M[0, 0]   # |k_0-k_1|^2/|k_0|^2, factor-independent
    kdiff = kdiff / np.sqrt(np.abs(M).max())              # factor round-off scale: sqrt(eps)
    eq_err = abs(Sc[0, 1] + k0sq)
    evs = np.linalg.eigvalsh(Sc)
    Pi = np.linalg.inv(Sc) if evs[0] > 1e-12 * evs[-1] else None
    zmat = None if Pi is None else bool(np.all(Pi[~np.eye(len(Pi), dtype=bool)] <= 1e-12))
    return dict(h_swap=h_swap, h_equiv=h_equiv, h_priv=h_priv, lyap_err=lyap_err, k0sq=k0sq,
                kdiff=kdiff, gap01=gap01, Sc01=Sc[0, 1], eq_err=eq_err, minev=evs[0], zmat=zmat,
                Pi01=None if Pi is None else Pi[0, 1])


def main():
    rng = np.random.default_rng(20261122)
    # ---- sanity 1: spectral smoother vs finite-window conditioning ----
    inst = None
    while inst is None:
        inst = draw(rng, 3, 2, 2, "general")
    covz, covE, _, _ = spectra(*(inst[k] for k in "A E Q C D Ry".split()))
    for T in (10, 40):
        wc = window_cond(*(inst[k] for k in "A E Q C D Ry".split()), T)
        print(f"sanity window T={T}: max|Cov(z0|y_window) - Cov(z0|y_all)| = {np.abs(wc - (covz - covE)).max():.3e}")
    covz2, covE2, _, _ = spectra(*(inst[k] for k in "A E Q C D Ry".split()), nf=2 * NF)
    print(f"sanity quadrature NF vs 2NF: {np.abs(covE2 - covE).max():.3e}")

    # ---- edge case 1: A = [[0,c],[c,0]] scalar, local S: private cross entry exactly zero ----
    c = 0.7
    A = np.array([[0, c], [c, 0.]]); E = np.eye(2); Q = np.eye(2)
    C = np.array([[1., 1.]]); D = np.zeros((1, 2)); Ry = np.array([[0.3]])
    inst = dict(A=A, E=E, Q=Q, C=C, D=D, Ry=Ry, S=np.eye(2), P=swapP(2, 1), Sig=lyap(A, E, Q))
    r = evaluate(inst, rng)
    print("edge A=[[0,c],[c,0]]:", {k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()})

    # ---- edge case 2: singular Sigma^c (A=0, noiseless ytil = z_0 + z_1) ----
    A = np.zeros((2, 2)); Ry = np.array([[0.0]])
    inst = dict(A=A, E=E, Q=Q, C=C, D=D, Ry=Ry, S=np.eye(2), P=swapP(2, 1), Sig=lyap(A, E, Q))
    covz, covE, _, _ = spectra(A, E, Q, C, D, Ry)
    Sc = covz - covE
    print("edge singular: Sigma^c =", np.round(Sc, 6).tolist(), " eigs =", np.round(np.linalg.eigvalsh(Sc), 6).tolist())

    # ---- edge case 3: barely informative ytil (k_0 tiny) ----
    A = np.array([[0, c], [c, 0.]]); Ry = np.array([[1e6]])
    inst = dict(A=A, E=E, Q=Q, C=C, D=D, Ry=Ry, S=np.eye(2), P=swapP(2, 1), Sig=lyap(A, E, Q))
    r = evaluate(inst, rng)
    print("edge barely:", {k: (float(f"{v:.3e}") if isinstance(v, float) else v) for k, v in r.items()})

    # ---- random search ----
    stats = dict(tried=0, admissible=0, violations=0, zmat=0, singular=0)
    worst = dict(h_swap=0, h_equiv=0, h_priv=0, lyap_err=0, kdiff_rel=0, gap01=0, eq_err_rel=0)
    max_Sc01_over_k = -np.inf
    for it in range(1500):
        n = rng.choice([2, 3]); d = rng.choice([1, 2]); m = rng.choice([1, 2, 3])
        variant = rng.choice(["general", "local"])
        inst = draw(rng, n, d, m, variant)
        stats["tried"] += 1
        if inst is None:
            continue
        r = evaluate(inst, rng)
        ok = r["h_swap"] < 1e-9 and r["h_equiv"] < 1e-12 and r["h_priv"] < 1e-8 and r["k0sq"] > 1e-10
        if not ok:
            continue
        stats["admissible"] += 1
        for k in ("h_swap", "h_equiv", "h_priv", "lyap_err"):
            worst[k] = max(worst[k], r[k])
        worst["kdiff_rel"] = max(worst["kdiff_rel"], r["kdiff"])
        worst["gap01"] = max(worst["gap01"], abs(r["gap01"]))
        worst["eq_err_rel"] = max(worst["eq_err_rel"], r["eq_err"] / r["k0sq"])
        max_Sc01_over_k = max(max_Sc01_over_k, r["Sc01"] / r["k0sq"])
        if r["zmat"] is None:
            stats["singular"] += 1
        elif r["zmat"]:
            stats["zmat"] += 1
        if r["Sc01"] >= 0 or abs(r["gap01"]) > 1e-8 or r["kdiff"] > 1e-6 or r["zmat"]:
            stats["violations"] += 1
            print("VIOLATION", n, d, m, variant, r)
    print("search stats:", stats)
    print("worst hypothesis residuals / identity errors:", {k: float(f"{v:.2e}") for k, v in worst.items()})
    print(f"max over admissible of Sigma^c_01 / |k_0|^2 = {max_Sc01_over_k:.12f} (claim: exactly -1)")


if __name__ == "__main__":
    main()
