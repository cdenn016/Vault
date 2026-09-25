r"""G1 checks for the frame-mean hypotheses (PIFB2.tex 1573, 1580-1585, 3758-3762, 3807-3811).

 (1) The consensus detector Gamma = P C_q C_s is blind to frame spread: with q_j = (U_j)_# q0 every transported
     KL vanishes (Gamma = 1) for arbitrary frames. Cyclic SO(3) triple U_j = Rz(2 pi j/3): the Karcher
     objective (bi-invariant d = ||log(U^{-1}V)||_F) has at least three global minimizers {v^k M*}.
     The frame-free parent pair (m, S) = (U_I^{-1} mu_I, U_I^{-1} Sigma_I U_I^{-T}) is the same for all of them.
 (2) GL+(2) pair R(+-pi/2) under d = ||log(U^{-1}V)||_F: I and -I are both global minimizers (left
     multiplication by -I permutes the pair); FD gradient and Hessian at both.
 (3) An explicit triangle-inequality violation of d on GL+(2) with both legs below 1, recomputed with an
     eigendecomposition logarithm independent of scipy.linalg.logm.
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
from scipy.linalg import expm, logm
from scipy.optimize import minimize
from scipy.spatial.transform import Rotation as Rr
rng = np.random.default_rng(11)

def kl(m1, S1, m2, S2):
    K = len(m1); S2i = np.linalg.inv(S2); dd = m2 - m1
    return 0.5*(np.trace(S2i@S1) + dd@S2i@dd - K + np.log(np.linalg.det(S2)/np.linalg.det(S1)))

# (1) detector blindness and Karcher non-uniqueness on SO(3)
Rz = lambda a: Rr.from_rotvec([0, 0, a]).as_matrix()
Us = [Rz(2*np.pi*j/3) for j in range(3)]
mu0 = np.array([1.0, -0.5, 2.0]); A = rng.standard_normal((3, 3)); S0 = A@A.T + np.eye(3)
qs = [(U@mu0, U@S0@U.T) for U in Us]
KLs = [kl(qs[i][0], qs[i][1], (Us[i]@Us[j].T)@qs[j][0], (Us[i]@Us[j].T)@qs[j][1]@(Us[i]@Us[j].T).T) for i in range(3) for j in range(3)]
Cq = np.exp(-np.mean(KLs)/0.05)
print(f"(1) cyclic SO(3) frames 120 deg apart: max transported KL = {max(KLs):.2e}, C_q = {Cq:.6f} (Gamma = 1 with P = C_s = 1)")
def dso(U, V): return np.linalg.norm(Rr.from_matrix(U.T@V).as_rotvec())*np.sqrt(2)
def F(U): return sum(dso(U, V)**2 for V in Us)/3
best = []
for _ in range(60):
    r = minimize(lambda p: F(Rr.from_rotvec(p).as_matrix()), rng.standard_normal(3)*2, method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-13, maxiter=4000))
    best.append((r.fun, Rr.from_rotvec(r.x).as_matrix()))
fmin = min(b[0] for b in best); mins = []
for fv, M in best:
    if fv < fmin + 1e-7 and not any(np.linalg.norm(M - M2) < 1e-4 for M2 in mins): mins.append(M)
print(f"    Karcher objective: global minimum {fmin:.8f} (16 pi^2/27 = {16*np.pi**2/27:.8f}); distinct minimizers found from 60 starts: {len(mins)}")
v = Us[1]; orbit = [np.linalg.matrix_power(v, k)@mins[0] for k in range(3)]
print(f"    objective on the v-orbit of one minimizer: {[round(F(M), 10) for M in orbit]}")
pairs = []
for UI in orbit:
    mt = [UI@U.T@q[0] for U, q in zip(Us, qs)]; St = [(UI@U.T)@q[1]@(UI@U.T).T for U, q in zip(Us, qs)]
    muI = np.mean(mt, 0); SigI = np.mean([S + np.outer(m - muI, m - muI) for S, m in zip(St, mt)], 0)
    pairs.append((np.linalg.solve(UI, muI), np.linalg.solve(UI, np.linalg.solve(UI, SigI).T)))
print(f"    frame-free parent pair (m,S) spread over the minimizer orbit: {max(np.linalg.norm(p[0]-pairs[0][0]) + np.linalg.norm(p[1]-pairs[0][1]) for p in pairs):.2e}")

# (2) GL+(2) pair: I and -I
def rlog(A):
    ev = np.linalg.eigvals(A)
    if np.any((abs(ev.imag) < 1e-12) & (ev.real <= 0)): return None
    return np.real(logm(A))
def d(U, V):
    L = rlog(np.linalg.solve(U, V)); return np.inf if L is None else np.linalg.norm(L)
Rot = lambda a: np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
P = [Rot(np.pi/2), Rot(-np.pi/2)]
f = lambda M: 0.5*(d(M, P[0])**2 + d(M, P[1])**2)
basis = [np.eye(2)[:, [i]]@np.eye(2)[[j], :] for i in range(2) for j in range(2)]
for M0, lab in ((np.eye(2), "I"), (-np.eye(2), "-I")):
    h = 1e-4; g = [(f(M0@expm(h*E)) - f(M0@expm(-h*E)))/(2*h) for E in basis]
    H = np.array([[(f(M0@expm(h*(E1 + E2))) - f(M0@expm(h*(E1 - E2))) - f(M0@expm(h*(E2 - E1))) + f(M0@expm(-h*(E1 + E2))))/(4*h*h) for E2 in basis] for E1 in basis])
    print(f"(2) GL+(2) pair R(+-pi/2), M = {lab}: objective {f(M0):.10f}, |grad| = {np.linalg.norm(g):.1e}, Hessian eigenvalues {np.round(np.linalg.eigvalsh((H + H.T)/2), 4)}")

# (3) explicit triangle violation with an eigendecomposition log
def elog(A):
    lam, V = np.linalg.eig(A); return np.real(V@np.diag(np.log(lam.astype(complex)))@np.linalg.inv(V))
found = None
for _ in range(200000):
    X, Y = rng.standard_normal((2, 2))*0.5, rng.standard_normal((2, 2))*0.5
    if max(np.linalg.norm(X), np.linalg.norm(Y)) >= 1: continue
    C = expm(X)@expm(Y)
    if rlog(C) is None: continue
    ex = np.linalg.norm(elog(C)) - np.linalg.norm(X) - np.linalg.norm(Y)
    if found is None or ex > found[0]: found = (ex, X, Y)
ex, X, Y = found
print(f"(3) d(I, e^X e^Y) - d(I, e^X) - d(e^X, e^X e^Y) = {ex:.4f} with ||X||={np.linalg.norm(X):.3f}, ||Y||={np.linalg.norm(Y):.3f}; "
      f"logm/elog agreement {np.linalg.norm(elog(expm(X)@expm(Y)) - rlog(expm(X)@expm(Y))):.1e}; elog(e^Y)-Y = {np.linalg.norm(elog(expm(Y)) - Y):.1e}")
print("    X =", np.round(X, 4).tolist(), " Y =", np.round(Y, 4).tolist())
