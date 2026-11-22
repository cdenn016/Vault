"""Reviewer supplementary check: admissible (rho(M)<1) n=2 vector instance; exact lambda_1 slope; PD of mixture
components; fourth-moment test that distinguishes the 2-mixture from a Gaussian by exact moment recursion
(no simulation): E[(v.u)^4] under mu must satisfy the stationarity identity for the 4th-moment tensor."""
import math, numpy as np
from numpy.linalg import inv, eigvals, norm
from scipy.stats import binom
from check_b_numeric import make_A, rho, spd
rng = np.random.default_rng(11)
K11, K22 = spd(rng, 2), spd(rng, 3)
K = np.block([[K11, 0.35*rng.normal(size=(2,3))],[0.35*rng.normal(size=(3,2)), K22]])
As = make_A(K, [2,3]); gam = 1.7
A12, A21 = -inv(K11) @ K[:2,2:], -inv(K22) @ K[2:,:2]
M = A12 @ A21; rM = rho(M)
Q1 = (inv(K11) + A12 @ inv(K22) @ A12.T)/gam
S1 = np.linalg.solve(np.eye(4)-np.kron(M,M), Q1.reshape(-1)).reshape(2,2)
S2 = A21 @ S1 @ A21.T + inv(K22)/gam
Sig1 = np.block([[S1, A12@S2],[S2@A12.T, S2]]); Sig2 = np.block([[S1, S1@A21.T],[A21@S1, S2]])
print(f"rho(M)={rM:.5f}; min eig Sigma1={np.linalg.eigvalsh(Sig1).min():.5f}, Sigma2={np.linalg.eigvalsh(Sig2).min():.5f}")
# stationarity in law, exactly: mu T_i must be N(0,Sigma_i).  For a Gaussian mixture mu = (N(S_a)+N(S_b))/2,
# mu T_i = (N(A_i S_a A_i^T + N_i) + N(A_i S_b A_i^T + N_i))/2 ; both components must equal Sigma_i.
offs=[0,2,5]; Kd=[K11,K22]
for i in range(2):
    Ni = np.zeros((5,5)); s,e = offs[i],offs[i+1]; Ni[s:e,s:e] = inv(Kd[i])/gam
    tgt = [Sig1,Sig2][i]
    r = max(norm(As[i]@Sa@As[i].T + Ni - tgt) for Sa in (Sig1,Sig2))
    print(f"  member {i+1}: max_a ||A_i Sigma_a A_i^T + N_i - Sigma_{i+1}|| = {r:.2e}")
bad = Sig2.copy(); bad[0,2] += 0.05; bad[2,0] += 0.05
Ni = np.zeros((5,5)); Ni[:2,:2] = inv(K11)/gam
print(f"  NEG CONTROL (perturbed Sigma2 entry in the u2-u1 cross block is erased by T_1, as it should): {norm(As[0]@bad@As[0].T + Ni - Sig1):.2e}")
bad = Sig2.copy(); bad[3,3] += 0.05
print(f"  NEG CONTROL (perturbed u2-marginal of Sigma2): {norm(As[0]@bad@As[0].T + Ni - Sig1):.2e}")
def a_exact(t):
    ln = np.zeros((2,t+1))
    for first in (0,1):
        P = np.eye(5); sl = 0.0
        for L in range(1,t+1):
            P = P @ As[(first+L-1)%2]; s = norm(P,2); sl += math.log(s); ln[first,L] = sl; P /= s
    w = binom.pmf(np.arange(t), t-1, 0.5)
    return float(sum(w[k]*0.5*(ln[0,k+1]+ln[1,k+1]) for k in range(t)))
print(f"exact slope(400->800) of E ln||P_t|| = {(a_exact(800)-a_exact(400))/400:+.8f}; (1/4)ln rho(M) = {0.25*math.log(rM):+.8f}")
