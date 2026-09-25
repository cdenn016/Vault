"""L13: O1/O2 exclude nothing (Kretschmann-type vacuity check).

Any autonomous system dx/dt = f(x), including a non-gradient (rotational, dissipative) flow, is the
exact minimizer of the residual functional S[x] = sum_t |x_{t+1} - x_t - h f(x_t)|^2 / 2 with fixed x_0,
and it can be dressed with a trivial bundle (phi = 0, Omega_ij = I) and a Gaussian belief
q = N(x, s^2 I) whose Fisher-Rao pullback is s^{-2}|dx|^2. So 'carries gauge-frame structure and
participates in variational dynamics on a statistical manifold' is satisfiable by every system.
"""
import numpy as np
rng = np.random.default_rng(1)
h, T = 0.01, 200
A = np.array([[-0.1, -1.0], [1.0, -0.1]])        # rotational, non-gradient: A != A^T
f = lambda x: A @ x + 0.3 * np.array([np.sin(x[1]), 0.0])
x0 = np.array([1.0, 0.0])
X = [x0]
for _ in range(T):
    X.append(X[-1] + h * f(X[-1]))
X = np.array(X)

def S(Xf):
    Xf = np.vstack([x0, Xf.reshape(T, 2)])
    r = Xf[1:] - Xf[:-1] - h * np.array([f(x) for x in Xf[:-1]])
    return 0.5 * (r ** 2).sum()

z = X[1:].ravel()
eps = 1e-6
g = np.array([(S(z + eps * e) - S(z - eps * e)) / (2 * eps) for e in np.eye(z.size)[:40]])
print("S at solution =", S(z), "; max |dS| over first 40 coords (central FD) =", np.abs(g).max())
print("S at perturbed paths:", [round(S(z + 1e-2 * rng.standard_normal(z.size)), 6) for _ in range(3)])
print("asymmetry of Jacobian (non-gradient check): |A - A^T| =", np.abs(A - A.T).max())
