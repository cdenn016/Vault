import numpy as np
from scipy.linalg import expm, logm
J = np.array([[0.0, -1.0], [1.0, 0.0]])
N = np.array([[0.0, -1.0], [0.0, 0.0]])
A = expm(np.pi * J) @ expm(N)
print("A =", np.round(A, 12).tolist(), "det =", np.linalg.det(A))
print("A + I nilpotent nonzero:", np.round(A + np.eye(2), 12).tolist())
L = logm(A)
print("principal logm(A) =", np.round(L, 6).tolist(), "max |imag| =", np.abs(np.imag(L)).max())
