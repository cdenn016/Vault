"""Exact-identity check: det(I - T|V) = prod_k det(Sigma_k) * det(I - A_c^noiseless), built in coded coordinates from world quantities."""
import numpy as np, scipy.linalg as la
rng = np.random.default_rng(5)
def spd(k, rng, scale=1.0):
    M = rng.standard_normal((k, k)); return scale * (M @ M.T + 0.5 * np.eye(k))
def msqrt(X):
    w, V = la.eigh(X); return (V * np.sqrt(w)) @ V.T
bad = []; mx_rest = 0; mx = 0; mxw = 0; neg = negunst = 0; skipped = 0
for t in range(3000):
    N = int(rng.integers(2, 5)); K = int(rng.integers(2, 5)); rk = [int(rng.integers(1, K+1)) for _ in range(N)]
    Ps = [spd(K, rng, 10**rng.uniform(-0.5, 0.5)) for _ in range(N)]
    Hs = [rng.standard_normal((rk[i], K)) for i in range(N)]
    Rs = [spd(rk[i], rng, 10**rng.uniform(-1, 1)) for i in range(N)]
    # world operators
    A = []; A0 = []
    for k in range(N):
        H = Hs[(k-1) % N]; X = H @ Ps[k] @ H.T
        A.append(Ps[k] @ H.T @ la.solve(X + Rs[(k-1) % N], H)); A0.append(Ps[k] @ H.T @ la.solve(X, H))
    Ac0 = np.eye(K)
    for k in list(range(1, N)) + [0]: Ac0 = A0[k] @ Ac0
    # exact basis change: Phi_k = P_k H^T X^{-1/2}, Phi_k^+ = X^{-1/2} H  (Phi^+ Phi = I)
    Phi = []; Phip = []; sig = 1.0
    for k in range(N):
        H = Hs[(k-1) % N]; X = H @ Ps[k] @ H.T; Xmh = la.inv(msqrt(X))
        Phi.append(Ps[k] @ H.T @ Xmh); Phip.append(Xmh @ H); sig *= la.det(X) / la.det(X + Rs[(k-1) % N])
    off = np.cumsum([0] + [rk[(k-1) % N] for k in range(N)]); n = off[-1]
    for mode in ("sync", "seq"):
        if mode == "sync":
            T = np.zeros((N*K, N*K))
            for k in range(N):
                km = (k-1) % N; T[k*K:(k+1)*K, k*K:(k+1)*K] = np.eye(K) - A[k]; T[k*K:(k+1)*K, km*K:(km+1)*K] += A[k]
        else:
            T = np.eye(N*K)
            for k in list(range(1, N)) + [0]:
                km = (k-1) % N; St = np.eye(N*K)
                St[k*K:(k+1)*K, k*K:(k+1)*K] = np.eye(K) - A[k]; St[k*K:(k+1)*K, km*K:(km+1)*K] += A[k]; T = St @ T
        TV = np.zeros((n, n))
        for a in range(N):
            for b in range(N):
                TV[off[a]:off[a+1], off[b]:off[b+1]] = Phip[a] @ T[a*K:(a+1)*K, b*K:(b+1)*K] @ Phi[b]
        d = la.det(np.eye(n) - TV); pred = sig * la.det(np.eye(K) - Ac0)
        if abs(pred) < 1e-6 * sig: skipped += 1; continue          # all codes of full rank K: A_c^noiseless = I, both sides vanish
        rel = abs(d - pred) / max(abs(pred), abs(d))
        if rel > 1e-6: bad.append((rel, mode, N, K, tuple(rk), d, pred, sig, la.det(np.eye(K) - Ac0)))
        mx = max(mx, rel)
        if rel <= 1e-6: mx_rest = max(mx_rest, rel)
        if pred < 0:
            neg += 1; negunst += max(abs(la.eigvals(TV))) > 1
print(f"max relative error of det(I - T|V) = prod det(Sigma_k) det(I - A_c^noiseless) over 3000 cycles x 2 operators (ranks 1..K, N=2..4): {mx:.2e}")
print(f"skipped (degenerate, both sides zero to rounding): {skipped}")
print(f"negative determinant (odd number of real noiseless cycle eigenvalues above 1) in {neg} operator draws; unstable in {negunst} of them")

print(f"non-degenerate comparisons: {6000 - skipped}; with relative error > 1e-6: {len(bad)}, all of them with |det| <= {max(abs(b[5]) for b in bad):.1e} (rounding in a determinant of size 1e-8 or less); largest relative error among the rest: {mx_rest:.1e}")
