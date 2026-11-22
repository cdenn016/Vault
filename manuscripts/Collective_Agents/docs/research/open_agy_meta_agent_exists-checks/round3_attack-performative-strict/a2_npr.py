r"""a2: partner randomization redrawn every round (annealed N_pr) for the CCP,
'own' coordinate, with my own time-varying code.

Within-sequence second moment W = E_seq[Cov(e(t0) | world path, seq)] is exact
for every-round redraws (E_eta P(seq|eta) = P(seq)); the mixture term
E[Var_seq(E[e|eta,seq])] is PSD and is not computed here.

Conventions:
 zero-gain : a receiver's exact filter knows whom it read and gives zero gain to a
             partner from the other firm (independent world); gains time-varying.
 kept-gain : a receiver keeps its full-model steady-state gains and applies the
             relay column to whatever partner it read (other-firm sensing noise
             then enters its error); 4-agent joint system.

Declared expectations (before running):
 E1 zero-gain: diffusive, r(pair) about 2.0-2.1 (candidate 2.016-2.097), below the
    lower edge 3.2224 of the window.
 E2 NEGATIVE CONTROL: with the mate always read (p_mate = 1) the time-varying code
    reproduces the stationary full-model Sigma^c (4.3336) to 1e-8.
 E3 kept-gain: cross-firm entries appear; I expect the precision to be
    non-diffusive (as the candidate found for the TDF).  If it is, the CCP's
    differ verdict against N_pr needs reading (h) or the zero-gain convention.
"""
import sys
import numpy as np
from ccp_lib import *

np.set_printoptions(precision=6, suppress=True)
p = default_params()
Phi, Qw, Gm = world_mats(p)
Qtot = Gm @ Qw @ Gm.T + p["qc"] * np.eye(4)
filt = member_filters(p)
kap = p["kappa"]
OWN = {"b": 0, "s": 1}
REL = {"b": 3, "s": 2}


def firm_window_zero_gain(rb, rs, L, Lr, burn=60):
    """One firm, zero-gain convention. rb, rs: arrays of length burn+L+Lr+1 of 0/1
    (1 = the member reads its mate this round). Returns Cov of the two 'own'
    coordinates at t0 given the collider observations in [t0-L, t0+Lr]."""
    nT = len(rb)
    # time-varying gains, start from steady state of the full model
    gains = {}
    for j, seq in (("b", rb), ("s", rs)):
        P = filt[j]["P"].copy()
        Kl, Hl = [], []
        for t in range(nT):
            if seq[t]:
                H = np.zeros((2, 4)); H[0, OWN[j]] = 1; H[1, REL[j]] = 1
                Rm = np.diag([p["R"], p["R"] + p["Rc"]])
            else:
                H = np.zeros((1, 4)); H[0, OWN[j]] = 1
                Rm = np.array([[p["R"]]])
            S = H @ P @ H.T + Rm
            K = P @ H.T @ np.linalg.inv(S)
            Kl.append(K); Hl.append(H)
            P = Phi @ ((np.eye(4) - K @ H) @ P) @ Phi.T + Qtot
        gains[j] = (Kl, Hl)
    # private linear system, time varying; state as in ccp_lib (10), noise (15)
    A0, B0, C0, Dm0, qv = private_system(p, filt, "full")
    S0cov = stationary_cov(A0, B0, qv)
    t_start = burn  # window starts after burn rounds of the gain recursion
    t0 = t_start + L
    nsteps = L + Lr + 1
    nx, nxi = NX, NXI
    dimU = nx + nxi * nsteps
    coefS = np.zeros((nx, dimU)); coefS[:, :nx] = np.eye(nx)
    O = np.zeros((nsteps, dimU))
    tgt = None
    T = coord_map("own")
    for k in range(nsteps):
        t = t_start + k
        if t == t0:
            tgt = T @ coefS
        A = np.zeros((nx, nx)); B = np.zeros((nx, nxi))
        Crow = np.zeros(nx); Drow = np.zeros(nxi)
        for j, (zs, own_i, mate_lag, nu_i, c0) in {"b": (0, 0, 9, 2, 4), "s": (4, 1, 8, 3, 8)}.items():
            K, H = gains[j][0][t], gains[j][1][t]
            M = np.eye(4) - K @ H
            ZpS = np.zeros((4, nx)); ZpS[:, zs:zs + 4] = M
            ZpX = np.zeros((4, nxi)); ZpX[:, own_i] += K[:, 0]
            if K.shape[1] == 2:
                ZpS[:, mate_lag] += K[:, 1]
                ZpX[:, nu_i] += K[:, 1]
            A[zs:zs + 4] = Phi @ ZpS
            B[zs:zs + 4] = Phi @ ZpX
            B[zs:zs + 4, c0:c0 + 4] += np.eye(4)
            Crow += -kap * D @ ZpS
            Drow += -kap * D @ ZpX
        B[8, 0] = 1.0; B[9, 1] = 1.0
        Drow[12] += 1; Drow[13] += 1; Drow[14] += 1
        cx = np.zeros((nxi, dimU)); cx[:, nx + k * nxi: nx + (k + 1) * nxi] = np.eye(nxi)
        O[k] = Crow @ coefS + Drow @ cx
        coefS = A @ coefS + B @ cx
    dg = np.tile(qv, nsteps)

    def cov(X, Y):
        return X[:, :nx] @ S0cov @ Y[:, :nx].T + (X[:, nx:] * dg) @ Y[:, nx:].T
    Soo = cov(O, O); Sto = cov(tgt, O); Stt = cov(tgt, tgt)
    return Stt - Sto @ np.linalg.solve(Soo, Sto.T)


rng = np.random.default_rng(2026)
L, Lr, burn = 60, 60, 60
nT = burn + L + Lr + 1
# E2 negative control: mate always read
ones = np.ones(nT, dtype=int)
Sc = firm_window_zero_gain(ones, ones, L, Lr, burn)
print("E2 mate always read:", Sc.ravel(), " r=%.8f" % ((Sc[0, 0] + Sc[0, 1]) / (Sc[0, 0] - Sc[0, 1])))

nseq = int(sys.argv[1]) if len(sys.argv) > 1 else 300
acc = []
for k in range(nseq):
    rb = (rng.random(nT) < 1 / 3).astype(int)
    rs = (rng.random(nT) < 1 / 3).astype(int)
    acc.append(firm_window_zero_gain(rb, rs, L, Lr, burn))
acc = np.array(acc)
W = acc.mean(0)
se = acc.std(0) / np.sqrt(nseq)
o = summarize_pair(W)
print("zero-gain W (n=%d):" % nseq, W.ravel(), "SE", se.ravel())
print("  diffusive", o["diffusive"], " r(pair)=%.4f  own-medium rbar=%.4f" % (o["r_pair"], o["rbar"]))
# half-sample spread
for h, sl in (("first half", slice(0, nseq // 2)), ("second half", slice(nseq // 2, nseq))):
    oo = summarize_pair(acc[sl].mean(0))
    print("  %s: r(pair)=%.4f" % (h, oo["r_pair"]))
# how large a positive mixture cross term would bring r to 3.2224?
s, c = W[0, 0], W[0, 1]
rt = 3.2224
# r = (s+c')/(s-c') with c' = c + m  ->  m = s (rt-1)/(rt+1) - c
print("  extra positive cross-covariance needed to reach 3.2224 (no extra variance): %.5f (W cross %.5f, W var %.5f)" % (s * (rt - 1) / (rt + 1) - c, c, s))
