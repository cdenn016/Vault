r"""a0: validate my CCP implementation before using it.

Declared expectations (before running):
 E1 window conditioning converges in L: L=40 vs L=80 agree to < 1e-10 (relative).
 E2 an independent frequency-domain two-sided Wiener smoother gives the same
    conditional covariance to < 1e-8 (relative).
 E3 NEGATIVE CONTROL: with the collider removed (C=Dm=0 is not allowed for the
    solver, so use a huge observation noise QZ=1e12), the conditional covariance
    equals the stationary (N_eff) covariance to < 1e-9 relative.
 E4 NEGATIVE CONTROL that must FAIL: a deliberately wrong spectral formula
    (dropping the cross term) must disagree with the window result by > 1e-3.
 E5 Monte Carlo of the unconditional private process reproduces the Lyapunov
    covariance (z-scores |z| < 4 on the 'own' entries).
"""
import numpy as np
from ccp_lib import *

p = default_params()
filt = member_filters(p)
A, B, C, Dm, qv = private_system(p, filt, "full")
print("spectral radius of private A:", max(abs(np.linalg.eigvals(A))))
for j in "bs":
    print(j, "K=\n", np.round(filt[j]["K"], 6))
T = coord_map("own")
S40 = window_condition(A, B, C, Dm, qv, T, L=40)
S80 = window_condition(A, B, C, Dm, qv, T, L=80)
print("E1 window L=40:\n", S40, "\nL=80:\n", S80)
print("E1 rel diff:", np.max(np.abs(S40 - S80)) / np.max(np.abs(S80)))

# E2 frequency-domain Wiener smoother
def spectral_cond(A, B, C, Dm, qv, T, n=4096, wrong=False):
    Qx = np.diag(qv)
    I = np.eye(A.shape[0])
    acc = np.zeros((T.shape[0], T.shape[0]), dtype=complex)
    for k in range(n):
        w = 2 * np.pi * k / n
        zinv = np.exp(-1j * w)
        HS = zinv * np.linalg.solve(I - A * zinv, B)
        Ho = C @ HS + Dm
        Hz = T @ HS
        Szz = Hz @ Qx @ Hz.conj().T
        Szo = Hz @ Qx @ Ho.conj().T
        Soo = Ho @ Qx @ Ho.conj().T
        if wrong:
            acc += Szz - (Szo.real) @ np.linalg.inv(Soo) @ (Szo.real).T
        else:
            acc += Szz - Szo @ np.linalg.inv(Soo) @ Szo.conj().T
    return (acc / n).real

Ssp = spectral_cond(A, B, C, Dm, qv, T)
print("E2 spectral:\n", Ssp, "\nrel diff vs window:", np.max(np.abs(Ssp - S80)) / np.max(np.abs(S80)))
Swr = spectral_cond(A, B, C, Dm, qv, T, wrong=True)
print("E4 wrong spectral rel diff (must be > 1e-3):", np.max(np.abs(Swr - S80)) / np.max(np.abs(S80)))

# E3 collider switched off by huge observation noise
p2 = dict(p); p2["QZ"] = 1e12
A2, B2, C2, Dm2, qv2 = private_system(p2, filt, "full")
Sc = window_condition(A2, B2, C2, Dm2, qv2, T, L=40)
Sst = T @ stationary_cov(A, B, qv) @ T.T
print("E3 cond with QZ=1e12:\n", Sc, "\nstationary:\n", Sst, "\nrel diff:", np.max(np.abs(Sc - Sst)) / np.max(np.abs(Sst)))

# E5 Monte Carlo of the private process (unconditional)
rng = np.random.default_rng(12345)
nT, nb = 400000, 2000
S = np.zeros(NX)
acc = []
sd = np.sqrt(qv)
for t in range(nT + nb):
    xi = rng.standard_normal(NXI) * sd
    S = A @ S + B @ xi
    if t >= nb:
        acc.append(T @ S)
acc = np.array(acc)
Cmc = np.cov(acc.T)
# batch-means standard errors
nbat = 100
bs = len(acc) // nbat
covs = np.array([np.cov(acc[i*bs:(i+1)*bs].T) for i in range(nbat)])
se = covs.std(0) / np.sqrt(nbat)
print("E5 MC cov:\n", Cmc, "\nLyapunov:\n", Sst, "\nz:\n", (Cmc - Sst) / se)
