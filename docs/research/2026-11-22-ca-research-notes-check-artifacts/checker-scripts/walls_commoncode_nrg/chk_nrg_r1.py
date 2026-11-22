import numpy as np
exec(open('chk_nrg.py').read().split("P = np.roll")[0])
def Rm(p): return np.array([[np.cos(p), -np.sin(p)], [np.sin(p), np.cos(p)]])
r = 0.7; A = np.block([[r*Rm(np.pi/3), np.zeros((2, 2))], [np.zeros((2, 2)), r*Rm(2*np.pi/3)]]); Q = np.eye(4)
print("R1: per-plane ep = %.6f, ebar(C_mux) = %.6f (note quotes 2.882353 and 3.150186)" % (ebar(A, Q, np.eye(4)[:2]), ebar(A, Q, np.hstack([np.eye(2), np.eye(2)])/np.sqrt(2))))
# m=3 best of a few random searches (note quotes 3.356297 for some m=3 subspace)
rng = np.random.default_rng(0); best = 0
for _ in range(300):
    C = rng.normal(size=(3, 4)); best = max(best, ebar(A, Q, C, 512))
print("    best random m=3: %.4f (note quotes 3.356297 attained by some m=3 subspace)" % best)
