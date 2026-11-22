import numpy as np, time, pickle, sys
from c5lib import *
strict = sys.argv[1] == 'strict'; seed = int(sys.argv[2]); budget = float(sys.argv[3])
rng = np.random.default_rng(seed); t0 = time.time(); top = []; cnt = 0
while time.time() - t0 < budget:
    N = int(rng.integers(2, 4)); K = int(rng.integers(2, 4)); p = int(rng.integers(2, 4))
    T = rng.normal(size=K)
    th = np.full(N, 10.0**rng.uniform(-1, 2.3)) if strict else 10.0**rng.uniform(-1, 2.3, N)
    f = rng.uniform(0.8, 0.999); Q = np.eye(K) if (strict or rng.uniform() < 0.5) else spd(rng, K)
    G = []
    for i in range(N):
        r = int(rng.integers(1, K+1)); h = rng.normal(size=(r, K))*10.0**rng.uniform(-1, 2.5); G.append(h.T @ h)
    prof = [([bool(rng.uniform() < 0.6) for i in range(N)], [[j for j in range(N) if j != i and rng.uniform() < 0.6] for i in range(N)]) for t in range(p)]
    inst = (N, K, p, T, th, f, Q, G, prof); r = rho_np(inst)
    if r is None: continue
    cnt += 1; top.append((r, inst)); top.sort(key=lambda x: -x[0]); top = top[:5]
print("mode=%s seed=%d: %d converged profiles; top rho_rec-1 (double): %s" % (sys.argv[1], seed, cnt, ["%.3e" % (t[0]-1) for t in top]))
pickle.dump(top, open("c5top_%s.pkl" % sys.argv[1], "wb"))
