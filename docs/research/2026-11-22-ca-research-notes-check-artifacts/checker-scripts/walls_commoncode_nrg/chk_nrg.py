# Independent check of problem_8 C1 (rate + e0 formula), C2 (lossless criterion), C3 (gradient), C4 (multiplexing)
import numpy as np
from scipy.linalg import solve_discrete_lyapunov, null_space, orth
rng = np.random.default_rng(31)
def Sigma_of(A, Q): return solve_discrete_lyapunov(A, Q)
def Dn(A, Q, C, n):
    Sig = Sigma_of(A, Q); m = C.shape[0]; N = n+1
    lag = [C @ np.linalg.matrix_power(A, k) @ Sig @ C.T for k in range(N)]
    T = np.zeros((N*m, N*m))
    for s in range(N):
        for t in range(N):
            T[s*m:(s+1)*m, t*m:(t+1)*m] = lag[s-t] if s >= t else lag[t-s].T
    idx = np.concatenate([np.arange((N-1-s)*m, (N-s)*m) for s in range(N)]); Tt = T[np.ix_(idx, idx)]
    return 0.5*(np.trace(np.linalg.solve(Tt, T)) - N*m)
def symbols(A, Q, C, M=4096):
    d = A.shape[0]; th = 2*np.pi*np.arange(M)/M; z = np.exp(1j*th); I = np.eye(d)
    R = np.linalg.inv(z[:, None, None]*I - A)                       # (e^{i th} - A)^{-1}
    Sf = R @ Q @ np.conj(np.transpose(R, (0, 2, 1)))                 # full spectral density
    return th, z, Sf, C @ Sf @ C.T
def ebar(A, Q, C, M=4096):
    th, z, Sf, S = symbols(A, Q, C, M); m = C.shape[0]
    return float(np.mean(np.real(np.trace(np.linalg.solve(np.conj(S), S), axis1=1, axis2=2)) - m)/2)
def e0_formula(A, Q, C, M=4096, plant=None):
    d = A.shape[0]; m = C.shape[0]; th, z, Sf, S = symbols(A, Q, C, M); Sig = Sigma_of(A, Q); I = np.eye(d)
    Sb = np.conj(S); Sbi = np.linalg.inv(Sb)
    L1 = lambda zz: C @ np.linalg.inv(I - np.conj(zz)[:, None, None]*A)          # C (I - e^{-i th} A)^{-1} evaluated at angle of zz
    L2 = lambda zz: C @ Sig @ np.linalg.inv(I - np.conj(zz)[:, None, None]*A.T)
    ph = z[:, None, None] if plant != 'flip_phase' else np.conj(z)[:, None, None]
    PW  = np.concatenate([L1(z), ph*L2(np.conj(z))], axis=2)                     # [L1(th), e^{i th} L2(-th)]
    PWt = np.concatenate([ph*L1(np.conj(z)), L2(z)], axis=2)                     # [e^{i th} L1(-th), L2(th)]
    H = lambda X: np.conj(np.transpose(X, (0, 2, 1)))
    G1 = np.mean(H(PWt) @ Sbi @ PWt, axis=0); G2 = np.mean(H(PW) @ Sbi @ PW, axis=0)
    G3 = np.mean(H(PWt) @ Sbi @ S @ Sbi @ PWt, axis=0); G4 = np.mean(H(PWt) @ Sbi @ PW, axis=0)
    imag = max(np.abs(G.imag).max() for G in (G1, G2, G3, G4)); G1, G2, G3, G4 = (G.real for G in (G1, G2, G3, G4))
    Hm = np.block([[np.zeros((d, d)), A], [A.T, np.zeros((d, d))]]); K = np.eye(2*d) - Hm @ G1; Ki = np.linalg.inv(K)
    br = -np.trace(Hm @ G2) + np.trace(Ki @ Hm @ G3) - np.trace(Ki @ Hm @ G4 @ Hm @ G4.T)
    eb = ebar(A, Q, C, M)
    if plant == 'sign_G4': br = -np.trace(Hm @ G2) + np.trace(Ki @ Hm @ G3) + np.trace(Ki @ Hm @ G4 @ Hm @ G4.T)
    return -eb - 0.5*br, np.linalg.det(K), imag
P = np.roll(np.eye(3), 1, axis=0)
cases = {"ring pair (0.3I+0.5P)": (0.3*np.eye(3)+0.5*P, np.eye(3), np.eye(3)[:2])}
A = rng.normal(size=(4, 4)); A *= 0.8/np.abs(np.linalg.eigvals(A)).max(); B = rng.normal(size=(4, 4))
cases["random non-normal d=4,m=2, full Q"] = (A, B @ B.T + 0.5*np.eye(4), rng.normal(size=(2, 4)))
As = np.array([[0, 0.9, 0.3], [0, 0, 0.7], [0.2, 0, 0.0]]); As[:, 0] = 0   # singular (first column zero) and non-normal
cases["singular A d=3,m=2"] = (np.array([[0, .9, .3], [0, .1, .7], [0, -.4, .2]]), np.diag([1., 2., .5]), np.array([[1., 0, 1], [0, 1., 0]]))
for name, (A, Q, C) in cases.items():
    eb = ebar(A, Q, C); e0, detK, imag = e0_formula(A, Q, C)
    errs = ["%.1e" % abs(n*eb - Dn(A, Q, C, n) - e0) for n in (4, 8, 16, 32, 64)]
    e0_bad1 = e0_formula(A, Q, C, plant='flip_phase')[0]; e0_bad2 = e0_formula(A, Q, C, plant='sign_G4')[0]
    print("%-36s rho(A)=%.3f ebar=%.6f e0(formula)=%+.8f detK=%.3f |n*ebar-D_n-e0| n=4..64: %s" % (name, np.abs(np.linalg.eigvals(A)).max(), eb, e0, detK, errs))
    print("      planted errors: flip phase -> e0=%+.6f (off by %.3f); sign of G4 term -> e0=%+.6f (off by %.3f); max imag part of G's %.1e" % (e0_bad1, abs(e0_bad1-e0), e0_bad2, abs(e0_bad2-e0), imag))
# ---- C2
def ep_direct(A, Q): return Dn(A, Q, np.eye(A.shape[0]), 1)       # Markov: D_1(I) = ep (one transition)
print("C2 lossless criterion:")
for d in (3, 5):
    A = rng.normal(size=(d, d)); A *= 0.7/np.abs(np.linalg.eigvals(A)).max(); B = rng.normal(size=(d, d)); Q = B @ B.T + 0.3*np.eye(d)
    Qi = np.linalg.inv(Q); Om = Qi @ A - A.T @ Qi; r = np.linalg.matrix_rank(Om, tol=1e-9)
    Cr = orth(Om).T; ep = ep_direct(A, Q); ep2 = Dn(A, Q, np.eye(d), 3)/3
    Cwrong = orth(A - A.T).T[:r]                                   # planted wrong criterion: range(A - A^T), ignores Q
    Cpert = Cr + 0.05*rng.normal(size=Cr.shape)
    print("  d=%d rank(Omega)=%d ep=D_1(I)=%.10f (D_3/3=%.10f) ebar(I)=%.10f | ebar(range Omega)=%.10f | perturbed C: %.10f | planted range(A-A^T): %.10f" % (d, r, ep, ep2, ebar(A, Q, np.eye(d)), ebar(A, Q, Cr), ebar(A, Q, Cpert), ebar(A, Q, Cwrong)))
d = 4; Ssym = rng.normal(size=(4, 4)); Ssym = 0.15*(Ssym + Ssym.T); A = Ssym + 0.4*(np.outer(np.eye(4)[0], np.eye(4)[1]) - np.outer(np.eye(4)[1], np.eye(4)[0]))
print("  d=4, Q=I, rank(Omega)=%d, rho(A)=%.3f: ep=%.10f  ebar(C=[e1;e2])=%.10f  ebar(C=[e1;e3])=%.10f  ebar(C=[e1+e3;e2])=%.10f  D_n(C=[e1;e2])/n at n=40: %.8f" % (np.linalg.matrix_rank(A-A.T), np.abs(np.linalg.eigvals(A)).max(), ep_direct(A, np.eye(4)), ebar(A, np.eye(4), np.eye(4)[:2]), ebar(A, np.eye(4), np.eye(4)[[0, 2]]), ebar(A, np.eye(4), np.array([[1., 0, 1, 0], [0, 1., 0, 0]])), Dn(A, np.eye(4), np.eye(4)[:2], 40)/40))
# ---- C3 gradient (finite differences) on the random d=4 case
A, Q, C = cases["random non-normal d=4,m=2, full Q"]
th, z, Sf, S = symbols(A, Q, C); Sbi = np.linalg.inv(np.conj(S))
grad = 2*np.mean(np.real(Sbi @ C @ Sf - Sbi @ S @ Sbi @ C @ np.conj(Sf)), axis=0)/2     # (1/2pi) int Re[...] = mean over grid
fd = np.zeros_like(C)
for a in range(C.shape[0]):
    for b in range(C.shape[1]):
        E = np.zeros_like(C); E[a, b] = 1e-6; fd[a, b] = (ebar(A, Q, C+E) - ebar(A, Q, C-E))/2e-6
print("C3 gradient: max|analytic-FD|=%.2e, max|grad C^T|=%.2e, |grad| scale=%.3f" % (np.abs(grad-fd).max(), np.abs(grad @ C.T).max(), np.abs(grad).max()))
# ---- C4 multiplexing
def Rm(p): return np.array([[np.cos(p), -np.sin(p)], [np.sin(p), np.cos(p)]])
for eps, r in ((np.pi/3, 0.99), (0.2, 0.998)):
    A = np.block([[r*Rm(eps), np.zeros((2, 2))], [np.zeros((2, 2)), r*Rm(np.pi-eps)]]); Q = np.eye(4)
    ep = ep_direct(A, Q); M = 2**16
    print("C4 eps=%.4f r=%.3f: ep=%.4f (formula 8r^2 sin^2/(1-r^2)=%.4f) invariant plane ratio=%.6f  C_mux ratio=%.6f  limit 1/(1+sin^2 eps)=%.6f" % (eps, r, ep, 8*r*r*np.sin(eps)**2/(1-r*r), ebar(A, Q, np.eye(4)[:2], M)/ep, ebar(A, Q, np.hstack([np.eye(2), np.eye(2)])/np.sqrt(2), M)/ep, 1/(1+np.sin(eps)**2)))
