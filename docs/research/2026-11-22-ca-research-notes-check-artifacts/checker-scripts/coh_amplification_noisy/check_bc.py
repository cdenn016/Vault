"""Independent check of C4-C7 of open_coh_amplification_noisy.md (fresh-context reviewer script)."""
import numpy as np, scipy.linalg as la
from scipy.optimize import minimize

rng = np.random.default_rng(11)

def spd(k, rng, scale=1.0):
    M = rng.standard_normal((k, k)); return scale * (M @ M.T + 0.2 * np.eye(k))
def msqrt(X):
    w, V = la.eigh(X); return (V * np.sqrt(w)) @ V.T
def edge(Pj, Hi, Ri):
    S = Hi @ Pj @ Hi.T + Ri
    return Pj @ Hi.T @ la.solve(S, Hi)
rho = lambda M: float(max(abs(la.eigvals(M))))
lmax = lambda A, B: float(max(la.eigvalsh(A, B)))
kap = lambda A, B: float(max(la.eigvalsh(A, B)) / min(la.eigvalsh(A, B)))

# ---------------------------------------------------------------- C4
print("[C4] posterior edge-ratio bound for ARBITRARY assigned noises (no header self-consistency), unequal ranks")
viol = pl1 = pl2 = 0; kal = 0; mxr = 0
for t in range(4000):
    K = int(rng.integers(2, 5)); N = int(rng.integers(2, 5))
    ranks = [int(rng.integers(1, K+1)) for _ in range(N)]
    Ps = [spd(K, rng, 10**rng.uniform(-1.5, 1.5)) for _ in range(N)]
    Hs = [rng.standard_normal((ranks[i], K)) for i in range(N)]
    Rs = [spd(ranks[i], rng, 10**rng.uniform(-1.5, 1.5)) for i in range(N)]
    As = [edge(Ps[k], Hs[(k-1) % N], Rs[(k-1) % N]) for k in range(N)]       # A_{k,k-1}
    Ac = np.eye(K)
    for k in list(range(1, N)) + [0]: Ac = As[k] @ Ac
    bound = 1.0; plant1 = 1.0; plant2 = 1.0
    for i in range(N):
        im = (i-1) % N; Hm = Hs[im]
        S = Hm @ Ps[i] @ Hm.T + Rs[im]
        Kp = Ps[i] @ Hm.T @ la.inv(S)
        Pt = Ps[i] - Kp @ Hm @ Ps[i]
        kal = max(kal, la.norm(Kp - Pt @ Hm.T @ la.inv(Rs[im])) / la.norm(Kp))
        rplus = lmax(Hs[i] @ Pt @ Hs[i].T, Rs[i])
        snrf = lmax(Hm @ Ps[i] @ Hm.T, S)
        bound *= np.sqrt(rplus * snrf)
        # planted 1: posterior coded variance measured against the receiver's S instead of the header R_i
        ip = (i+1) % N
        plant1 *= np.sqrt(lmax(Hs[i] @ Pt @ Hs[i].T, Hs[i] @ Ps[ip] @ Hs[i].T + Rs[i]) * snrf)
        # planted 2: posterior after reading the WRONG neighbor (successor's code and noise)
        Hw = Hs[i]; Sw = Hw @ Ps[i] @ Hw.T + Rs[i]
        Ptw = Ps[i] - Ps[i] @ Hw.T @ la.solve(Sw, Hw @ Ps[i])
        plant2 *= np.sqrt(lmax(Hs[i] @ Ptw @ Hs[i].T, Rs[i]) * snrf)
    r_ = rho(Ac); mxr = max(mxr, r_/bound)
    viol += r_ > bound * (1 + 1e-9); pl1 += r_ > plant1 * (1 + 1e-6); pl2 += r_ > plant2 * (1 + 1e-6)
print(f"  Kalman gain identity max relative error {kal:.2e}; bound violations {viol}/4000; max rho/bound {mxr:.4f}")
print(f"  planted (ratio against S_ji): violated {pl1}; planted (posterior after reading the wrong neighbor): violated {pl2}")

# ---------------------------------------------------------------- C5
print("[C5] general step: P^- not<= P^+(t-1) gives r^+ > 1 for a suitable code; and the registered instance")
ok = 0; tot = 0
for t in range(500):
    K = int(rng.integers(2, 5)); F = rng.standard_normal((K, K)) * 0.6
    Pplus = spd(K, rng); Q = spd(K, rng, 10**rng.uniform(-2, 0))
    Pm = F @ Pplus @ F.T + Q
    w, V = la.eigh(Pm - Pplus)
    if w[-1] <= 1e-6: continue
    tot += 1; v = V[:, -1:]; Hi = v.T
    Hm = rng.standard_normal((1, K)); Rm = np.array([[1e8]])
    S = Hm @ Pm @ Hm.T + Rm
    Pt = Pm - Pm @ Hm.T @ la.solve(S, Hm @ Pm)
    gap = (Hi @ (Pt - Pplus) @ Hi.T).item()
    Rc = 0.5 * gap
    Ri = (Hi @ Pplus @ Hi.T).item() + Rc
    ok += (Hi @ Pt @ Hi.T).item() / Ri > 1
print(f"  r^+ > 1 achieved in {ok}/{tot} admissible random draws")
al, x = 0.9, 4.0
Pa = np.array([[1, al*np.sqrt(x)], [al*np.sqrt(x), x]]); Pb = np.array([[x, al*np.sqrt(x)], [al*np.sqrt(x), 1]])
Fd = 0.5*np.eye(2); Pp = 0.2*np.eye(2)
Qa = Pa - Fd @ Pp @ Fd.T; Qb = Pb - Fd @ Pp @ Fd.T
ha = np.array([[0., 1.]]); hb = np.array([[1., 0.]])
Ra = ha @ Pp @ ha.T + 0.1; Rb = hb @ Pp @ hb.T + 0.1
r5 = rho(edge(Pa, hb, Rb) @ edge(Pb, ha, Ra))
print(f"  instance: min eig Q_a {min(la.eigvalsh(Qa)):.4f}, Q_b {min(la.eigvalsh(Qb)):.4f}, det Q_a {la.det(Qa):.4f}; rho(A_c) = {r5:.6f} vs 324/169 = {324/169:.6f}")

# ---------------------------------------------------------------- C6 Lemma 1
print("[C6] Lemma 1 ||M^-1 E M|| <= s (k^2+1)/(2k), equality case, planted wrong constant")
v1 = v2 = 0; mxl = 0; eqerr = 0
for t in range(20000):
    r = int(rng.integers(2, 6)); M = spd(r, rng, 1.0)
    if rng.uniform() < 0.5:
        E = spd(r, rng);
    else:
        q = int(rng.integers(1, r)); B = rng.standard_normal((r, q)); E = B @ B.T
    s = max(la.eigvalsh(E)); w = la.eigvalsh(M); k = w[-1]/w[0]
    n = la.norm(la.solve(M, E @ M), 2)
    mxl = max(mxl, n / (s*(k*k+1)/(2*k)))
    v1 += n > s*(k*k+1)/(2*k) * (1 + 1e-10)
    v2 += n > s*(k+1)/(2*np.sqrt(k)) * (1 + 1e-10)       # planted: kappa(M) where kappa(M)^2 belongs
    if t < 200:
        w, V = la.eigh(M); u = (V[:, -1] + V[:, 0]) / np.sqrt(2); E0 = np.outer(u, u)
        eqerr = max(eqerr, abs(la.norm(la.solve(M, E0 @ M), 2) - (k*k+1)/(2*k)) / ((k*k+1)/(2*k)))
print(f"  violations {v1}/20000 (max ratio {mxl:.6f}); equality-case relative error {eqerr:.2e}; planted constant violated {v2} times")

print("[C6] spread bound and Kantorovich bound, non-commuting noises, arbitrary reference, world-coordinate A_c")
vs = vk = 0; mk = 0
for t in range(3000):
    K = int(rng.integers(2, 5)); N = int(rng.integers(2, 6)); r = int(rng.integers(2, K+1))
    H = rng.standard_normal((r, K))
    Rs = [spd(r, rng, 10**rng.uniform(-1, 1)) for _ in range(N)]
    Ps = [spd(K, rng, 10**rng.uniform(-1.5, 1.5)) for _ in range(N)]
    As = [edge(Ps[k], H, Rs[(k-1) % N]) for k in range(N)]
    Ac = np.eye(K)
    for k in list(range(1, N)) + [0]: Ac = As[k] @ Ac
    sn = [lmax(H @ Ps[k] @ H.T, H @ Ps[k] @ H.T + Rs[(k-1) % N]) for k in range(N)]
    Sc = sum(np.log(lmax(Rs[(j-1) % N], Rs[j])) for j in range(N))
    Rstar = spd(r, rng)
    bk = np.prod(sn) * np.prod([(kap(Rs[i], Rstar) + 1) / (2*np.sqrt(kap(Rs[i], Rstar))) for i in range(N)])
    r_ = rho(Ac)
    vs += r_ > np.exp(0.5*Sc) * np.prod(sn) * (1 + 1e-9); vk += r_ > bk * (1 + 1e-9); mk = max(mk, r_/bk)
print(f"  spread-bound violations {vs}/3000; Kantorovich-bound violations {vk}/3000 (max ratio {mk:.4f})")

# ---------------------------------------------------------------- C7
print("[C7(1)] proportional noises: rho(A_c) <= prod snr/(1+snr), rho(barA) <= 1, world coordinates")
va = vb = 0; mxa = 0
for t in range(3000):
    K = int(rng.integers(2, 6)); N = int(rng.integers(2, 6)); r = int(rng.integers(2, K+1))
    H = rng.standard_normal((r, K)); R0 = spd(r, rng); al_ = 10**rng.uniform(-2, 2, N)
    Rs = [al_[i]*R0 for i in range(N)]
    Ps = [spd(K, rng, 10**rng.uniform(-2, 2)) for _ in range(N)]
    As = [edge(Ps[k], H, Rs[(k-1) % N]) for k in range(N)]
    Ac = np.eye(K)
    for k in list(range(1, N)) + [0]: Ac = As[k] @ Ac
    sn = np.prod([lmax(H @ Ps[k] @ H.T, H @ Ps[k] @ H.T + Rs[(k-1) % N]) for k in range(N)])
    r_ = rho(Ac); mxa = max(mxa, r_/sn)
    va += r_ > sn*(1 + 1e-9); vb += rho(np.eye(K) - As[0] + Ac) > 1 + 1e-7
print(f"  violations of rho(A_c) <= prod snr/(1+snr): {va}/3000 (max ratio {mxa:.4f}); rho(barA) > 1: {vb}/3000")

print("[C7(2)] arc construction for N >= 3 with NON-COMMUTING noises, any pair a<b (adjacent or not), r_c in {2,3,4}")
def geig(Ra, Rb):
    # w_p^T Rb^{-1} w_q = delta_pq, w_p^T Ra^{-1} w_p = 1/mu_p with mu = eig(Rb^{-1} Ra)
    mu, Wt = la.eigh(la.inv(Ra), la.inv(Rb))     # Ra^{-1} w = nu Rb^{-1} w, nu = 1/mu, W^T Rb^{-1} W = I
    return 1.0/mu, Wt                              # ascending nu -> descending mu
def trace_limit(us, Rs):
    N = len(us); val = 1.0
    for i in range(N):
        un = us[(i+1) % N]; Ri = la.inv(Rs[i])
        val *= (un @ Ri @ us[i]) / (un @ Ri @ un)
    return val
maxerr = 0; maxerr_fin = 0; rev_vals = []; n = 0; shifted_mismatch = 0
for t in range(1500):
    N = int(rng.integers(3, 7)); r = int(rng.integers(2, 5)); K = r + int(rng.integers(0, 3))
    Rs = [spd(r, rng, 10**rng.uniform(-1, 1)) for _ in range(N)]
    a, b = sorted(rng.choice(N, 2, replace=False))          # 0-indexed senders a<b
    mu, W = geig(Rs[a], Rs[b])
    w1 = W[:, 0]; w2 = W[:, -1]                               # mu_max, mu_min
    kab = kap(Rs[b], Rs[a]); m = np.sqrt(kab)
    assert abs(mu[0]/mu[-1] - kab) < 1e-8*kab
    vA = w1 + w2; vB = m*w1 + w2
    us = [vB if (a < k <= b) else vA for k in range(N)]       # u_k = v_2 on {a+1..b}
    target = (m+1)**2/(4*m)
    tl = trace_limit(us, Rs)
    maxerr = max(maxerr, abs(tl - target)/target); n += 1
    # planted: roles of v_1 and v_2 exchanged on the arcs (the orientation error the log says was repaired)
    us_rev = [vA if (a < k <= b) else vB for k in range(N)]
    rev_vals.append(trace_limit(us_rev, Rs) / target)
    # planted: arc shifted by one sender (mismatch placed on the wrong noise matrices)
    us_sh = [vB if (a <= k < b) else vA for k in range(N)]
    shifted_mismatch += abs(trace_limit(us_sh, Rs) - target)/target > 1e-6
    if t < 300:
        # finite (s, eps) priors in world coordinates, generic full-row-rank common code
        H = rng.standard_normal((r, K)); Hp = H.T @ la.inv(H @ H.T)
        s_, eps = 1e9, 1e-9
        Ps = [Hp @ (s_*np.outer(u, u)/ (u @ u) + eps*np.eye(r)) @ Hp.T + (np.eye(K) - Hp @ H) for u in us]
        As = [edge(Ps[k], H, Rs[(k-1) % N]) for k in range(N)]   # receiver k has coded prior built on u_k, reads sender k-1
        Ac = np.eye(K)
        for k in list(range(1, N)) + [0]: Ac = As[k] @ Ac
        maxerr_fin = max(maxerr_fin, abs(rho(Ac) - target)/target)
rev_vals = np.array(rev_vals)
print(f"  {n} random instances: max relative error of tr(B^inf) against cosh^2(d_H(R_a,R_b)/4): {maxerr:.2e}")
print(f"  finite (s=1e9, eps=1e-9) world-coordinate rho(A_c) against the same value (300 instances): max relative error {maxerr_fin:.2e}")
print(f"  planted exchanged-orientation: ratio to target min {rev_vals.min():.4f}, median {np.median(rev_vals):.4f}, max {rev_vals.max():.4f}; equals target in {(abs(rev_vals-1)<1e-6).sum()} of {n}")
print(f"  planted shifted arc: differs from target in {shifted_mismatch} of {n}")

print("[C7] is the two-sender value the supremum? N=2: random + local search against cosh^2(d_H/4); N=3: search over rank-one limits")
exceed2 = 0; best2 = 0
for t in range(60):
    r = int(rng.integers(2, 4)); R1 = spd(r, rng); R2 = spd(r, rng, 10**rng.uniform(-1, 1))
    m = np.sqrt(kap(R1, R2)); target = (m+1)**2/(4*m)
    def f(p):
        L1 = p[:r*r].reshape(r, r); L2 = p[r*r:].reshape(r, r)
        X1 = L1 @ L1.T + 1e-12*np.eye(r); X2 = L2 @ L2.T + 1e-12*np.eye(r)
        return -rho(X1 @ la.inv(X1 + R2) @ X2 @ la.inv(X2 + R1))
    best = 0
    for rs in range(4):
        res = minimize(f, rng.standard_normal(2*r*r)*10**rng.uniform(0, 2), method='Nelder-Mead', options={'maxiter': 1500, 'xatol': 1e-9, 'fatol': 1e-12})
        best = max(best, -res.fun)
    exceed2 += best > target*(1 + 1e-9); best2 = max(best2, best/target)
print(f"  N=2: searched sup exceeded the closed form in {exceed2}/60 instances; best found/closed form = {best2:.5f}")
ex3 = 0; ratios = []
for t in range(40):
    r = 2; Rs = [spd(r, rng, 10**rng.uniform(-0.5, 0.5)) for _ in range(3)]
    pair = max((np.sqrt(kap(Rs[i], Rs[j])) + 1)**2/(4*np.sqrt(kap(Rs[i], Rs[j]))) for i in range(3) for j in range(i+1, 3))
    def g(th):
        us = [np.array([np.cos(x), np.sin(x)]) for x in th]
        return -abs(trace_limit(us, Rs))
    best = 0
    for rs in range(30):
        res = minimize(g, rng.uniform(0, np.pi, 3), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-13})
        best = max(best, -res.fun)
    ratios.append(best/pair); ex3 += best > pair*(1 + 1e-7)
ratios = np.array(ratios)
print(f"  N=3 (r_c=2): best rank-one-limit value exceeds the best two-sender value in {ex3}/40 instances; ratio min {ratios.min():.4f} median {np.median(ratios):.4f} max {ratios.max():.4f}")
