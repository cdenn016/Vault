import pickle, sys, numpy as np, time
from scipy.optimize import minimize
from c5lib import *
top = pickle.load(open("c5top_strict.pkl", "rb")); idx = int(sys.argv[1]); budget = float(sys.argv[2])
r0, inst = top[idx]; N, K, p, T, th, f, Q, G, prof = inst
print("start: rho-1=%.3e N,K,p=%d,%d,%d f=%.4f theta=%.4g" % (r0-1, N, K, p, f, th[0]))
facs = []
for g in G:
    w, V = np.linalg.eigh(g); keep = w > 1e-9*w.max(); facs.append((np.sqrt(w[keep])[:, None]*V[:, keep].T))
    print("   sensor rank %d, singular values %s" % (keep.sum(), np.round(np.sqrt(w[keep]), 4)))
shapes = [h.shape for h in facs]
def pack(T, lth, facs): return np.concatenate([T, [lth]] + [h.ravel() for h in facs])
def unpack(x):
    T = x[:K]; lth = x[K]; k = K+1; hs = []
    for s in shapes:
        hs.append(x[k:k+s[0]*s[1]].reshape(s)); k += s[0]*s[1]
    return T, lth, hs
t0 = time.time(); best = [r0, None]
def obj(x):
    if time.time() - t0 > budget: raise StopIteration
    T, lth, hs = unpack(x)
    if abs(lth) > 6: return 0.0
    r = rho_np((N, K, p, T, np.full(N, np.exp(lth)), f, Q, [h.T @ h for h in hs], prof), iters=3000, tol=1e-14)
    if r is None: return 0.0
    if r > best[0]: best[0] = r; best[1] = x.copy()
    return -(r-1)*1e9
x0 = pack(T, np.log(th[0]), facs)
try:
    for rep in range(50):
        res = minimize(obj, x0, method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-6, maxiter=20000, adaptive=True)); x0 = res.x
except StopIteration: pass
print("best rho_rec-1 (double) after climb: %.6e" % (best[0]-1))
if best[1] is not None:
    T, lth, hs = unpack(best[1])
    inst2 = (N, K, p, T, np.full(N, np.exp(lth)), f, Q, [h.T @ h for h in hs], prof)
    pickle.dump([(best[0], inst2)], open("c5best_%d.pkl" % idx, "wb"))
    print("T=", np.round(T, 5), "theta=", np.exp(lth)); [print("  h_%d=" % i, np.round(h, 5).tolist()) for i, h in enumerate(hs)]
    print("prof (sensing on, listening sets):", prof)
