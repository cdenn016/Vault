r"""General two-replica Monte Carlo for raw-relay populations with EFE attention.

Agents a = 0..N-1 with own-sensor noise Rsen[a] (read every round) and an option
list opts[a] of sets of senders (channels read next round).  Every agent
broadcasts its raw reading; y_aj(t) = v_j(t-1) + eta_{t-1} + nu_aj(t), read with
claimed noise Rsen[j] + Rc (exact).  Filters on x_t = (eta_t, eta_{t-1}) with
computation noise qc I added to predicted means and to P^-.

Attention modes:
  'efe'     : option o with prob ∝ exp(gamma * I(x_{t+1}; own sensor, channels o))
              (uniform habits; EFE = -information gain, no pragmatic term)
  'uniform' : gamma = 0 over the option list (habit null)
  'pr'      : partner randomization redrawn every round: number of partners drawn
              from size_probs[a], partners uniform among the agent's potential senders
Replicas share the world innovations; with share=('S',) they also share agent 0's
sensing and computation noise (conditioning on zeta_S).
Returns Sigma (N x N) = 1/2 E[(e^1-e^2)(e^1-e^2)^T] and batch estimates, plus the
empirical option-frequency per agent.
"""
from __future__ import annotations
import numpy as np


def inv2(M):
    a, b, c, d = M[..., 0, 0], M[..., 0, 1], M[..., 1, 0], M[..., 1, 1]
    det = a * d - b * c
    out = np.empty_like(M)
    out[..., 0, 0] = d / det; out[..., 0, 1] = -b / det
    out[..., 1, 0] = -c / det; out[..., 1, 1] = a / det
    return out


def logdet2(M):
    return np.log(M[..., 0, 0] * M[..., 1, 1] - M[..., 0, 1] * M[..., 1, 0])


def run(Rsen, opts, mode="efe", gamma=40.0, F=0.9, Q=0.05, Rc=0.002, qc=1e-4,
        B=2000, T=1200, burn=150, seed=0, share_S=False, size_probs=None,
        potential=None, nbatch=20):
    rng = np.random.default_rng(seed)
    Rsen = np.asarray(Rsen, float)
    N = len(Rsen)
    A = np.array([[F, 0.0], [1.0, 0.0]])
    Qx = np.diag([Q, 0.0]) + qc * np.eye(2)
    chinfo = 1.0 / (Rsen + Rc)  # information of a channel from j
    Om = []
    for a in range(N):
        M = np.zeros((len(opts[a]), N))
        for k, s in enumerate(opts[a]):
            for j in s:
                M[k, j] = 1.0
        Om.append(M)
    eps = np.zeros((2, B, N, 2))
    Pm = np.tile(np.eye(2) * 0.1, (2, B, N, 1, 1))
    C = np.zeros((2, B, N, N))  # C[r,b,a,j] = 1 if a reads j this round
    vlag = np.zeros((2, B, N))
    acc = np.zeros((nbatch, N, N)); cnt = 0
    freq = [np.zeros(len(opts[a])) for a in range(N)]
    for t in range(T):
        w = rng.normal(0.0, np.sqrt(Q), size=B)
        if t >= burn:
            d = eps[0, :, :, 0] - eps[1, :, :, 0]
            outer = 0.5 * d[:, :, None] * d[:, None, :]
            acc += outer.reshape(nbatch, B // nbatch, N, N).sum(axis=1)
            cnt += B // nbatch
        vS_shared = rng.normal(0.0, np.sqrt(Rsen[0]), size=B)
        nS_shared = rng.normal(0.0, np.sqrt(qc), size=(B, 2))
        newv = np.empty((2, B, N))
        for r in range(2):
            v = rng.normal(0.0, 1.0, size=(B, N)) * np.sqrt(Rsen)[None, :]
            if share_S:
                v[:, 0] = vS_shared
            newv[r] = v
            Pinv = inv2(Pm[r])
            J = Pinv.copy()
            J[:, :, 0, 0] += 1.0 / Rsen[None, :]
            J[:, :, 1, 1] += C[r] @ chinfo
            nu = rng.normal(0.0, np.sqrt(Rc), size=(B, N, N))
            rhs = np.einsum("bnij,bnj->bni", Pinv, eps[r])
            rhs[:, :, 0] += v / Rsen[None, :]
            rhs[:, :, 1] += np.sum(C[r] * (vlag[r][:, None, :] + nu) * chinfo[None, None, :], axis=2)
            Pp = inv2(J)
            ep = np.einsum("bnij,bnj->bni", Pp, rhs)
            en = np.einsum("ij,bnj->bni", A, ep)
            cn = rng.normal(0.0, np.sqrt(qc), size=(B, N, 2))
            if share_S:
                cn[:, 0, :] = nS_shared
            en += cn
            en[:, :, 0] -= w[:, None]
            eps[r] = en
            Pm[r] = np.einsum("ij,bnjk,lk->bnil", A, Pp, A) + Qx[None, None]
            # attention for next round
            Cn = np.zeros((B, N, N))
            for a in range(N):
                no = Om[a].shape[0]
                if no == 1:
                    Cn[:, a, :] = Om[a][0][None, :]
                    freq[a][0] += B if (t >= burn and r == 0) else 0
                    continue
                if mode == "efe":
                    Pa = Pm[r][:, a]  # (B,2,2)
                    Pai = inv2(Pa)
                    infos = Om[a] @ chinfo  # (no,)
                    Jm = np.repeat(Pai[:, None], no, axis=1)
                    Jm[..., 0, 0] += 1.0 / Rsen[a]
                    Jm[..., 1, 1] += infos[None, :]
                    gain = 0.5 * (logdet2(Pa)[:, None] + logdet2(Jm))  # I = 1/2 ln det(P^-) det(J)
                    L = gamma * gain
                    L -= L.max(axis=1, keepdims=True)
                    P = np.exp(L); P /= P.sum(axis=1, keepdims=True)
                    u = rng.random((B, 1))
                    k = (np.cumsum(P, axis=1) < u).sum(axis=1)
                    k = np.minimum(k, no - 1)
                elif mode == "uniform":
                    k = rng.integers(0, no, size=B)
                elif mode == "pr":
                    pot = potential[a]
                    sp = np.asarray(size_probs[a], float)
                    sizes = rng.choice(len(sp), size=B, p=sp)
                    row = np.zeros((B, N))
                    keys = rng.random((B, len(pot)))
                    order = np.argsort(keys, axis=1)
                    for s in range(1, len(sp)):
                        sel = sizes >= s
                        idx = np.array(pot)[order[:, s - 1]]
                        row[np.arange(B)[sel], idx[sel]] = 1.0
                    Cn[:, a, :] = row
                    continue
                else:
                    raise ValueError(mode)
                Cn[:, a, :] = Om[a][k]
                if t >= burn and r == 0:
                    freq[a] += np.bincount(k, minlength=no)
            C[r] = Cn
        vlag = newv
    S_b = acc / (cnt / 1.0) * nbatch / nbatch
    S_b = acc / (cnt)  # each batch accumulated cnt samples
    S_all = S_b.mean(axis=0)
    freq = [f / max(f.sum(), 1) for f in freq]
    return S_all, S_b, freq
