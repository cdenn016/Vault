"""Reviewer script, part B: numerical checks with planted-error controls (numpy, <= 2 threads, < 60 s).

B1  C3: rho(T) = (1+rho(M))/2 on random n=2 vector instances (rho(M) <1, >1, complex, nilpotent);
        lambda_1 = (1/4) ln rho(M) by the EXACT finite-t expectation (binomial sum over run counts);
        two-Gaussian mixture: mu T_i = N(Sigma^(i)) closure identities.
B2  C4: inequalities on 300 random instances with mixed block dimensions.
B3  C6: rho(T) formula, deterministic Sigma_ii, cylinder Sigma_12 with unequal a_i and K_ii != 1,
        deterministic two-sided bound behind lambda_1 = ln|chi| / n^2.
B4  C1: characteristic-function stationarity identity for the backward mixture in the heavy-tailed
        instance K(2) and in the reviewer's O2 instance; det Sigma(omega) lower bound.
"""
from __future__ import annotations

import math

import numpy as np
from numpy.linalg import eigvals, inv, norm
from scipy.stats import binom


def make_A(K: np.ndarray, dims: list[int]) -> list[np.ndarray]:
    r"""A_i = I - E_i K_ii^{-1} E_i^T K."""
    d = sum(dims)
    offs = np.cumsum([0] + dims)
    out = []
    for i in range(len(dims)):
        s, e = int(offs[i]), int(offs[i + 1])
        E = np.zeros((d, e - s))
        E[s:e, :] = np.eye(e - s)
        out.append(np.eye(d) - E @ inv(K[s:e, s:e]) @ E.T @ K)
    return out


def rho(M: np.ndarray) -> float:
    return float(np.max(np.abs(eigvals(M))))


def rho_T(As: list[np.ndarray]) -> float:
    return rho(sum(np.kron(A, A) for A in As) / len(As))


def spd(rng: np.random.Generator, d: int) -> np.ndarray:
    X = rng.normal(size=(d, d))
    return X @ X.T + 0.5 * np.eye(d)


def b1() -> None:
    print("[B1] C3")
    rng = np.random.default_rng(101)
    worst = 0.0
    kinds = []
    for trial in range(40):
        d1, d2 = int(rng.integers(1, 4)), int(rng.integers(1, 4))
        K11, K22 = spd(rng, d1), spd(rng, d2)
        scale = [0.3, 1.0, 3.0][trial % 3]
        K12, K21 = scale * rng.normal(size=(d1, d2)), scale * rng.normal(size=(d2, d1))
        K = np.block([[K11, K12], [K21, K22]])
        M = inv(K11) @ K12 @ inv(K22) @ K21
        ev = eigvals(M)
        top = ev[np.argmax(np.abs(ev))]
        kinds.append((rho(M) > 1, abs(top.imag) > 1e-9))
        worst = max(worst, abs(rho_T(make_A(K, [d1, d2])) - (1 + rho(M)) / 2) / (1 + rho(M)))
    print(f"  40 random instances (rho(M)>1 in {sum(k[0] for k in kinds)}, complex top eigenvalue in {sum(k[1] for k in kinds)}):"
          f" max rel |rho(T)-(1+rho(M))/2| = {worst:.2e}")
    # planted error: (1+rho(M)^2)/2
    print(f"  NEG CONTROL formula (1+rho(M)^2)/2 on last instance: rel err = {abs(rho_T(make_A(K, [d1, d2])) - (1 + rho(M) ** 2) / 2) / (1 + rho(M)):.3f}")
    # nilpotent M: K12 K22^{-1} K21 nilpotent
    K = np.block([[np.eye(2), np.array([[0.0, 1.0], [0.0, 0.0]])], [np.eye(2) * 3.0, np.eye(2)]])
    As = make_A(K, [2, 2])
    print(f"  nilpotent M: rho(M)={rho(inv(K[:2,:2]) @ K[:2,2:] @ inv(K[2:,2:]) @ K[2:,:2]):.1e}, rho(T)={rho_T(As):.6f} (claim 1/2),"
          f" ||(A1A2)^3|| = {norm(np.linalg.matrix_power(As[0] @ As[1], 3)):.1e}")

    # exact finite-t expectation of ln||P_t||: P_t is the alternating word of length N_t+1, N_t ~ Bin(t-1,1/2),
    # first letter uniform.  (Uses only A_i^2 = A_i, which is asserted.)
    rng = np.random.default_rng(7)
    K11, K22 = spd(rng, 2), spd(rng, 3)
    K = np.block([[K11, 0.9 * rng.normal(size=(2, 3))], [0.9 * rng.normal(size=(3, 2)), K22]])
    As = make_A(K, [2, 3])
    assert all(norm(A @ A - A) < 1e-12 for A in As)
    rM = rho(inv(K11) @ K[:2, 2:] @ inv(K22) @ K[2:, :2])

    def a_exact(t: int) -> float:
        ln_norm = np.zeros((2, t + 1))
        for first in (0, 1):
            P = np.eye(5)
            scale_log = 0.0
            for L in range(1, t + 1):
                P = P @ As[(first + L - 1) % 2]
                s = norm(P, 2)
                ln_norm[first, L] = scale_log + math.log(s)
                P /= s
                scale_log += math.log(s)
        w = binom.pmf(np.arange(t), t - 1, 0.5)  # N_t = k -> word length k+1
        return float(sum(w[k] * 0.5 * (ln_norm[0, k + 1] + ln_norm[1, k + 1]) for k in range(t)))

    a400, a800 = a_exact(400), a_exact(800)
    slope = (a800 - a400) / 400
    print(f"  exact E ln||P_t||: slope(400->800) = {slope:+.8f}; (1/4) ln rho(M) = {0.25*math.log(rM):+.8f};"
          f" NEG CONTROL (1/2) ln rho(M) = {0.5*math.log(rM):+.8f}")

    # mixture closure: S1 = A12 S2 A12^T + (gamma K11)^{-1}, S2 = A21 S1 A21^T + (gamma K22)^{-1}
    gam = 1.7
    A12, A21 = -inv(K11) @ K[:2, 2:], -inv(K22) @ K[2:, :2]
    Mm = A12 @ A21
    Q1 = (inv(K11) + A12 @ inv(K22) @ A12.T) / gam
    S1 = np.linalg.solve(np.eye(4) - np.kron(Mm, Mm), Q1.reshape(-1)).reshape(2, 2)
    S2 = A21 @ S1 @ A21.T + inv(K22) / gam
    print(f"  mixture closure residual ||S1 - (A12 S2 A12^T + (gamma K11)^-1)|| = {norm(S1 - (A12 @ S2 @ A12.T + inv(K11)/gam)):.2e}"
          f"  (rho(M)={rM:.4f});  NEG CONTROL with S1*1.01: {norm(1.01*S1 - (A12 @ (A21 @ (1.01*S1) @ A21.T + inv(K22)/gam) @ A12.T + inv(K11)/gam)):.2e}")
    Sig1 = np.block([[S1, A12 @ S2], [S2 @ A12.T, S2]])
    Sig2 = np.block([[S1, S1 @ A21.T], [A21 @ S1, S2]])
    print(f"  min eig Sigma1, Sigma2 = {np.linalg.eigvalsh(Sig1).min():.4f}, {np.linalg.eigvalsh(Sig2).min():.4f};"
          f" ||Sigma1-Sigma2|| = {norm(Sig1-Sig2):.4f} (nonsymmetric K => non-Gaussian)")


def b2() -> None:
    print("[B2] C4")
    rng = np.random.default_rng(202)
    m1 = m2 = 1e9
    for _ in range(300):
        n = int(rng.integers(2, 5))
        dims = [int(rng.integers(1, 3)) for _ in range(n)]
        d = sum(dims)
        K = rng.normal(size=(d, d)) * rng.choice([0.2, 0.6, 1.5])
        offs = np.cumsum([0] + dims)
        for i in range(n):
            s, e = int(offs[i]), int(offs[i + 1])
            K[s:e, s:e] = spd(rng, e - s)
        As = make_A(K, dims)
        rT = rho_T(As)
        m1 = min(m1, rT - (n - 1) / n)
        m2 = min(m2, rT - rho(sum(As) / n) ** 2)
    print(f"  300 random instances: min[rho(T)-(n-1)/n] = {m1:.3e}, min[rho(T)-rho(barA)^2] = {m2:.3e} (both must be >= 0)")


def b3() -> None:
    print("[B3] C6")
    rng = np.random.default_rng(303)
    for n in (3, 4, 5):
        a = rng.uniform(0.3, 1.4, size=n) * rng.choice([-1, 1], size=n)
        kd = rng.uniform(0.5, 2.0, size=n)
        K = np.diag(kd)
        for i in range(n):
            K[i, (i + 1) % n] = -a[i] * kd[i]
        chi = float(np.prod(a))
        As = make_A(K, [1] * n)
        pred = (n - 1 + abs(chi) ** (2 / n)) / n
        wrong = (n - 1 + abs(chi)) / n
        # deterministic bound: | ln||Q_t||_inf - S_t ln|chi| / n^2 | <= C  along one long random path
        L = np.zeros(n, dtype=int)
        Q = np.eye(n)
        logscale = 0.0
        dev = 0.0
        t_end = 30000
        for t in range(t_end):
            i = int(rng.integers(0, n))
            L[i] = L[(i + 1) % n] + 1
            Q = As[i] @ Q
            s = np.abs(Q).sum(axis=1).max()
            Q /= s
            logscale += math.log(s)
            dev = max(dev, abs(logscale - L.sum() * math.log(abs(chi)) / n**2))
        C1 = np.abs(np.log(np.abs(a))).sum()
        bound = C1 + (2 * n - 1) / n * abs(math.log(abs(chi)))
        print(f"  n={n}, chi={chi:+.4f}: rho(T)={rho_T(As):.8f} pred={pred:.8f} (NEG CONTROL exponent 1 instead of 2/n: {wrong:.8f});"
              f" max|ln||Q_t|| - S_t ln|chi|/n^2| = {dev:.3f} <= bound {bound:.3f};"
              f" S_t/t = {L.sum()/t_end:.4f}; max-min L = {L.max()-L.min()} <= {n-1}")
    # deterministic Sigma_ii and cylinder Sigma_12 for n=3 with unequal a_i, K_ii
    a = np.array([0.7, -0.9, 0.8])
    kd = np.array([1.3, 0.6, 2.0])
    gam = 0.8
    K = np.diag(kd)
    for i in range(3):
        K[i, (i + 1) % 3] = -a[i] * kd[i]
    chi = float(np.prod(a))
    As = make_A(K, [1, 1, 1])
    s_pred = [sum(np.prod(a[[(i + q) % 3 for q in range(r)]] ** 2) / kd[(i + r) % 3] for r in range(3)) / (gam * (1 - chi**2)) for i in range(3)]

    def Sigma(word: list[int]) -> np.ndarray:
        P = np.eye(3)
        S = np.zeros((3, 3))
        for i in word:
            v = P[:, [i]]
            S += v @ v.T / (gam * kd[i])
            P = P @ As[i]
        return S

    diag_dev = 0.0
    offdiag_vals = []
    for _ in range(30):
        S = Sigma(list(rng.integers(0, 3, size=600)))
        diag_dev = max(diag_dev, np.abs(np.diag(S) - s_pred).max())
        offdiag_vals.append(S[0, 1])
    print(f"  n=3 (chi={chi:+.3f}): max |Sigma_ii - s_i| over 30 random schedules = {diag_dev:.2e};"
          f" Sigma_12 ranges over [{min(offdiag_vals):+.4f}, {max(offdiag_vals):+.4f}] (random)")
    cyl = 0.0
    for m in range(5):
        word = [1, 0, 2, 1, 0, 2] * m + [0] + list(rng.integers(0, 3, size=600))
        cyl = max(cyl, abs(Sigma(word)[0, 1] - a[0] * s_pred[1] * chi ** (2 * m)))
    wrongcyl = abs(Sigma([1, 0, 2, 1, 0, 2] * 1 + [0] + list(rng.integers(0, 3, size=600)))[0, 1] - a[0] * s_pred[1] * chi ** 1)
    print(f"  cylinder C_m, m=0..4: max |Sigma_12 - a1 s2 chi^(2m)| = {cyl:.2e};  NEG CONTROL chi^m at m=1: {wrongcyl:.3e}")


def b4() -> None:
    print("[B4] C1 backward mixture is T-invariant (characteristic functions), heavy-tailed instances")
    for name, K in (("K(2)", np.array([[1.0, -2.0, 2.0], [-1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]])),
                    ("K_o (reviewer O2 example)", np.array([[1.0, -1.0, 0.0], [-7.0, 1.0, -7.0], [1.0, 0.0, 1.0]]))):
        As = np.stack(make_A(K, [1, 1, 1]))  # (3,3,3)
        rng = np.random.default_rng(404)
        N, Tmax = 150000, 600
        P = np.broadcast_to(np.eye(3), (N, 3, 3)).copy()
        S = np.zeros((N, 3, 3))
        S_drop0 = np.zeros((N, 3, 3))
        alive = np.ones(N, dtype=bool)
        for k in range(Tmax):
            idx = rng.integers(0, 3, size=N)
            v = P[np.arange(N), :, idx]  # (N,3) column idx of P
            add = v[:, :, None] * v[:, None, :]
            S += add
            if k > 0:
                S_drop0 += add
            P = np.einsum("nij,njk->nik", P, As[idx])
            alive = np.abs(P).reshape(N, -1).max(axis=1) > 0
            if not alive.any():
                break
        print(f"  {name}: all {N} schedules absorbed by step {k+1}: {not alive.any()};"
              f" det Sigma min = {np.linalg.det(S).min():.6f} (lower bound gamma^-d / det K_d = 1)")

        def phi(Sm: np.ndarray, t: np.ndarray) -> float:
            return float(np.mean(np.exp(-0.5 * np.einsum("i,nij,j->n", t, Sm, t))))

        worst = 0.0
        worst_bad = 0.0
        for t in (np.array([0.3, 0.0, 0.0]), np.array([0.2, -0.4, 0.1]), np.array([0.05, 0.05, 0.05]), np.array([0.0, 0.6, -0.6])):
            lhs = phi(S, t)
            rhs = sum(math.exp(-0.5 * t[i] ** 2) * phi(S, As[i].T @ t) for i in range(3)) / 3
            lhs_bad = phi(S_drop0, t)
            rhs_bad = sum(math.exp(-0.5 * t[i] ** 2) * phi(S_drop0, As[i].T @ t) for i in range(3)) / 3
            worst = max(worst, abs(lhs - rhs))
            worst_bad = max(worst_bad, abs(lhs_bad - rhs_bad))
        print(f"    max |phi_mu(t) - (1/3) sum_i e^(-t_i^2/2) phi_mu(A_i^T t)| over 4 t = {worst:.4f} (MC error ~ {1/math.sqrt(N):.4f});"
              f"  NEG CONTROL (k=0 term dropped): {worst_bad:.4f}")
        q = np.quantile(S[:, 0, 0], [0.5, 0.9, 0.99, 0.999])
        print(f"    quantiles of Sigma_11: 50% {q[0]:.3g}, 90% {q[1]:.3g}, 99% {q[2]:.3g}, 99.9% {q[3]:.3g};  E sqrt(Sigma_11) sample mean = {np.sqrt(S[:,0,0]).mean():.3g}")


if __name__ == "__main__":
    b1()
    b2()
    b3()
    b4()
