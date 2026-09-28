r"""Operator norm of the model-mean readout on the hidden space, and d_z identity (check only)."""
import math, numpy as np
exec(open("stage4_activation_check.py").read().split("# ---------------------------------------------------------------- 2. constants")[0])
Pm = np.zeros((4, 12)); Pm[:, 4:8] = np.eye(4)
print("||P_m F^T||_op =", np.linalg.norm(Pm @ F.T, 2))
# |d_z|^2 with d = D F^T z should equal 2(z2^2+z3^2)
zz = np.random.default_rng(1).standard_normal((5, 3))
dz = (D @ F.T @ zz.T).T
print("max | |d_z|^2 - 2(z2^2+z3^2) | =", np.abs((dz**2).sum(1) - 2*(zz[:,1]**2+zz[:,2]**2)).max())
# exterior residual hidden components (other worker noted (0,-1/2,-1/2) for the half-difference)
for g in (1, 3):
    print("edge", g, "belief row on Z:", F @ ab[g], " model row on Z:", F @ am[g])
