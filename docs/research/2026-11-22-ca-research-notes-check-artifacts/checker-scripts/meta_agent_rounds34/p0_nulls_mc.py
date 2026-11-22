"""Rough two-replica Monte Carlo of the audience P0 under the full model, N_hab and
N_pr (redrawn every round).  Second-moment convention of def:col-contrast:
Sigma^c = (1/2) E[(e1-e2)(e1-e2)^T] for two replicas sharing the world innovations,
with independent private noises and independent attention draws.  Members run exact
time-varying Kalman filters on (eta_t, eta_{t-1}).  Own code, vectorized over chains.
"""
import sys
import numpy as np

F, Q, R, RS, RC, QC = 0.9, 0.05, 1.0, 0.01, 0.002, 1e-4
BIG = 1e12


def run(mode, B=60000, T=120, Tacc=60, seed=0):
    rng = np.random.default_rng(seed)
    # arrays indexed [replica, agent, chain]
    P = np.zeros((2, 5, B, 2, 2)); P[..., 0, 0] = 0.3; P[..., 1, 1] = 0.3
    e = np.zeros((2, 5, B, 2))
    vprev = np.zeros((2, 5, B))
    Rsens = np.array([RS, R, R, R, R])
    acc = np.zeros((5, 5)); nacc = 0
    for t in range(T + Tacc):
        w = rng.normal(0, np.sqrt(Q), B)                      # shared by the replicas
        v = rng.normal(size=(2, 5, B)) * np.sqrt(Rsens)[None, :, None]
        # --- own-sensor update (h = [1,0])
        S1 = P[..., 0, 0] + Rsens[None, :, None]
        K1 = P[..., :, 0] / S1[..., None]
        innov = -e[..., 0] + v
        e = e + K1 * innov[..., None]
        P = P - K1[..., :, None] * P[..., 0, :][..., None, :]
        # --- message update for members (h = [0,1])
        if mode == "full":
            part = np.zeros((2, 4, B), dtype=int)             # everyone reads the source
        elif mode == "pr":
            draw = rng.integers(0, 4, size=(2, 4, B))         # uniform over the 4 other agents
            me = np.arange(1, 5)[None, :, None]
            others = np.where(draw >= me, draw + 1, draw)     # skip own index
            part = others
        elif mode == "hab":
            draw = rng.integers(0, 5, size=(2, 4, B))         # {none, S, m1, m2, m3}
            me = np.arange(1, 5)[None, :, None]
            cand = draw - 1                                   # -1 none, 0 source, 1..3 co-member slot
            comem = np.where(cand >= me, cand + 1, cand)
            comem = np.where(cand >= 1, np.where(cand >= me, cand + 1, cand), cand)
            part = comem                                      # -1 = none
        nomsg = part < 0
        pj = np.where(nomsg, 0, part)
        rr = np.arange(2)[:, None, None]; bb = np.arange(B)[None, None, :]
        content_noise = vprev[rr, pj, bb] + rng.normal(0, np.sqrt(RC), size=(2, 4, B))
        mvar = np.where(nomsg, BIG, Rsens[pj] + RC)
        Pm = P[:, 1:]; em = e[:, 1:]
        S2 = Pm[..., 1, 1] + mvar
        K2 = Pm[..., :, 1] / S2[..., None]
        innov2 = -em[..., 1] + np.where(nomsg, 0.0, content_noise)
        em = em + K2 * innov2[..., None]
        Pm = Pm - K2[..., :, None] * Pm[..., 1, :][..., None, :]
        e[:, 1:] = em; P[:, 1:] = Pm
        # --- predict: x' = (F eta + w, eta); mean gets computation noise q_c on each component
        n = rng.normal(0, np.sqrt(QC), size=(2, 5, B, 2))
        e_new = np.empty_like(e)
        e_new[..., 0] = F * e[..., 0] - w[None, None, :] + n[..., 0]
        e_new[..., 1] = e[..., 0] + n[..., 1]
        e = e_new
        Pn = np.empty_like(P)
        Pn[..., 0, 0] = F * F * P[..., 0, 0] + Q + QC
        Pn[..., 0, 1] = F * P[..., 0, 0]
        Pn[..., 1, 0] = Pn[..., 0, 1]
        Pn[..., 1, 1] = P[..., 0, 0] + QC
        P = Pn
        vprev = v
        if t >= T:
            d = e[0, :, :, 0] - e[1, :, :, 0]                 # (5, B)
            acc += 0.5 * d @ d.T / B; nacc += 1
    S = acc / nacc
    sig = S[0, 0]; c = S[0, 1:].mean(); v_ = np.diag(S)[1:].mean()
    b = (S[1:, 1:].sum() - np.trace(S[1:, 1:])) / 12
    al = v_ - b; bp = b - c * c / sig
    return sig, c, v_, b, 1 - c / sig + 4 * bp / al


for mode in ("full", "hab", "pr"):
    out = [run(mode, seed=s) for s in range(4)]
    rs = np.array([o[-1] for o in out])
    m = np.mean(np.array(out), axis=0)
    print("%-5s Var e_S %.5e Cov(S,i) %.5e Var e_i %.5e Cov(i,j) %.5e  r(A) %.4f +- %.4f (4 seeds)"
          % (mode, m[0], m[1], m[2], m[3], rs.mean(), rs.std(ddof=1) / 2))
    sys.stdout.flush()
