r"""Float64 checks: the linear link I + O'T and the exponential link exp(OT) are two charts of the same embedded GL(d)."""
import numpy as np
from scipy.linalg import expm, logm

rng = np.random.default_rng(3)
rel = lambda a, b: np.abs(a - b).max() / max(1.0, np.abs(b).max())
K, d = 7, 3

def phi(Z):
    out, term = np.zeros_like(Z), np.eye(Z.shape[0])
    for n in range(1, 80):
        out = out + term / np.prod(np.arange(1, n + 1, dtype=float)); term = term @ Z
    return out

# (1) Any linear link I + O'T whose I + TO' has a real log is EXACTLY an exponential link.
T = rng.standard_normal((d, K))
for trial in range(3):
    Op = 0.4 * rng.standard_normal((K, d))
    g = np.eye(d) + T @ Op
    if np.linalg.det(g) <= 0: continue
    Z = np.real(logm(g))
    O = Op @ np.linalg.inv(phi(Z))
    print(f"trial {trial}: exp(OT) = I + O'T with O = O' phi(log(I+TO'))^-1   rel err",
          rel(expm(O @ T), np.eye(K) + Op @ T), "  TO = Z err", np.abs(T @ O - Z).max())

# (2) Both families sit in one embedded GL(d): g = (I-P) + O B (TO)^-1 T acts as B on W = im O, identity on ker T.
O = rng.standard_normal((K, d)); P = O @ np.linalg.solve(T @ O, T)
emb = lambda B: (np.eye(K) - P) + O @ B @ np.linalg.solve(T @ O, T)
B1, B2 = expm(0.3 * rng.standard_normal((d, d))), expm(0.3 * rng.standard_normal((d, d)))
print("embedding is a homomorphism: emb(B1)emb(B2) = emb(B1 B2)   rel err", rel(emb(B1) @ emb(B2), emb(B1 @ B2)))
print("exp(OT) = emb(e^{TO})                                      rel err", rel(expm(O @ T), emb(expm(T @ O))))
C = 0.3 * rng.standard_normal((d, d))
print("I + O C T = emb(I + C TO)                                   rel err", rel(np.eye(K) + O @ C @ T, emb(np.eye(d) + C @ (T @ O))))
print("det emb(B) = det B                                          rel err", rel(np.linalg.det(emb(B1)), np.linalg.det(B1)))

# (3) Tiled heads (Hd = K): the current operator O'T equals exp(OT) exactly when O'T has a real log;
#     the code's identity initialization O'T = I is the origin X = OT = 0 of the exponential chart.
Kt = 6
Tt = rng.standard_normal((Kt, Kt)); Xg = 0.3 * rng.standard_normal((Kt, Kt))
Opt = expm(Xg) @ np.linalg.inv(Tt)
print("tiled: O' = e^{X} T^-1 gives O'T = e^{X}                    rel err", rel(Opt @ Tt, expm(Xg)))
print("tiled identity init: O'T = I  <->  X = 0, log(I) =", np.abs(np.real(logm(np.eye(Kt)))).max())
# (4) Counter-check: first-order truncation differs at O(1) at the identity init generator X = I (TO = I).
print("exp(I) vs I + I at TO = I (generator OT = I): rel diff", rel(expm(np.eye(Kt)), 2 * np.eye(Kt)))
