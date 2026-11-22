# Resolve the C5 'excess': rebuild each Gamma_i in multiprecision as h^T h from an exact low-rank factor (exactly PSD, exact rank)
import pickle, numpy as np, mpmath as mp, c5lib
from c5lib import *
mp.mp.dps = 40
def factor(g):
    w, V = np.linalg.eigh(g); keep = w > 1e-9*w.max(); return np.sqrt(w[keep])[:, None]*V[:, keep].T
class MPG:  # wrapper so that mpm(G_i) returns the exact PSD mp matrix
    pass
orig_mpm = c5lib.mpm
def run(inst):
    N, K, p, T, th, f, Q, G, prof = inst
    hs = [factor(g) for g in G]
    mineig = [float(np.linalg.eigvalsh(np.array(mp.matrix(g.tolist()).tolist(), dtype=float)).min()) for g in G]
    exact = [mp.matrix(h.tolist()).T*mp.matrix(h.tolist()) for h in hs]
    # monkeypatch: pass mp matrices through
    c5lib.mpm = lambda a: a if isinstance(a, mp.matrix) else orig_mpm(a)
    rho_e, res_e = c5lib.rho_mp((N, K, p, T, th, f, Q, exact, prof), 300)
    c5lib.mpm = orig_mpm
    rho_f, res_f = c5lib.rho_mp(inst, 300)
    # exact smallest eigenvalue of the float Gamma (in mp)
    mins = [min(mp.eigsy(orig_mpm(g), eigvals_only=True)) for g in G]
    return rho_f-1, rho_e-1, res_e, mins
for name in ("strict",):
    for r, inst in pickle.load(open("c5top_%s.pkl" % name, "rb"))[:4]:
        a, b, res, mins = run(inst)
        print("float-Gamma: rho_rec-1=%s | exact-PSD Gamma: rho_rec-1=%s (residual %s) | min eig of float Gammas: %s" % (mp.nstr(a, 6), mp.nstr(b, 6), mp.nstr(res, 2), [mp.nstr(m, 3) for m in mins]))
