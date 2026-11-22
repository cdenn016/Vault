r"""Sampled-noise two-replica Monte Carlo of P0 under random attention.

Sigma^c = E[Cov(e(t)|eta)] = 1/2 E[(e^1-e^2)(e^1-e^2)^T] with the two replicas
sharing the world innovations w and independent in everything else (sensing,
channel and computation noise, and attention).  Exact time-varying Kalman
filters per agent and replica (covariances depend on the realized attention).

mode:
  'full'  : members choose by EFE (gamma) at their current P^- (decision at end of round)
  'hab'   : gamma = 0, uniform over {none, S, m_j}
  'pr'    : one uniformly drawn partner among {S, m_j} every round
  'dead'  : members read nothing (negative control: Sigma^c diagonal)
indep_world=True gives each replica its own world innovations (negative control).
"""
from __future__ import annotations
import numpy as np

AF2 = lambda F: np.array([[F, 0.0], [1.0, 0.0]])


def inv2(M):
    a, b, c, d = M[..., 0, 0], M[..., 0, 1], M[..., 1, 0], M[..., 1, 1]
    det = a * d - b * c
    out = np.empty_like(M)
    out[..., 0, 0] = d / det
    out[..., 0, 1] = -b / det
    out[..., 1, 0] = -c / det
    out[..., 1, 1] = a / det
    return out


def run(mode: str, B: int = 2000, T: int = 1200, burn: int = 150, seed: int = 0,
        F=0.9, Q=0.05, R=1.0, RS=0.01, Rc=0.002, qc=1e-4, gamma=40.0, n=4,
        indep_world: bool = False, nbatch: int = 20):
    rng = np.random.default_rng(seed)
    A = AF2(F)
    Qx = np.diag([Q, 0.0]) + qc * np.eye(2)
    N = n + 1
    Rsen = np.array([RS] + [R] * n)
    # state per replica r in {0,1}: eps[r] (B,N,2), Pm[r] (B,N,2,2), choice[r] (B,n) in {-1 none, 0 S, j member}
    eps = np.zeros((2, B, N, 2))
    Pm = np.tile(np.eye(2) * 0.1, (2, B, N, 1, 1))
    choice = np.zeros((2, B, n), dtype=int)  # start: all read S
    vlag = np.zeros((2, B, N))  # v_a(t-1)
    acc = np.zeros((nbatch, N, N))
    cnt = np.zeros(nbatch)
    bidx = np.arange(B) % nbatch
    h_own = np.array([1.0, 0.0])
    for t in range(T):
        w = rng.normal(0.0, np.sqrt(Q), size=B)
        w2 = rng.normal(0.0, np.sqrt(Q), size=B) if indep_world else w
        e_now = eps[..., 0]  # (2,B,N) prior errors at round t
        if t >= burn:
            d = e_now[0] - e_now[1]
            outer = 0.5 * d[:, :, None] * d[:, None, :]
            acc += outer.reshape(nbatch, B // nbatch, N, N).sum(axis=1)
            cnt += B // nbatch
        newv = np.empty((2, B, N))
        for r in range(2):
            v = rng.normal(0.0, 1.0, size=(B, N)) * np.sqrt(Rsen)[None, :]
            newv[r] = v
            # information matrices
            Pinv = inv2(Pm[r])  # (B,N,2,2)
            J = Pinv.copy()
            J[:, :, 0, 0] += 1.0 / Rsen[None, :]
            # channel for members
            chR = np.zeros((B, N))  # claimed noise of channel read this round (0 = none)
            chnoise = np.zeros((B, N))
            for i in range(1, N):
                c = choice[r][:, i - 1]
                readS = c == 0
                readM = c > 0
                chR[readS, i] = RS + Rc
                if np.any(readM):
                    chR[readM, i] = R + Rc
                nu = rng.normal(0.0, np.sqrt(Rc), size=B)
                src = np.where(c >= 0, c, 0)
                chnoise[:, i] = np.where(c >= 0, vlag[r][np.arange(B), src] + nu, 0.0)
            has = chR > 0
            J[:, :, 1, 1] += np.where(has, 1.0 / np.where(has, chR, 1.0), 0.0)
            Pp = inv2(J)
            # posterior error: Pp (Pinv eps + H^T R^{-1} noise)
            rhs = np.einsum("bnij,bnj->bni", Pinv, eps[r])
            rhs[:, :, 0] += v / Rsen[None, :]
            rhs[:, :, 1] += np.where(has, chnoise / np.where(has, chR, 1.0), 0.0)
            ep = np.einsum("bnij,bnj->bni", Pp, rhs)
            ww = w if r == 0 else w2
            en = np.einsum("ij,bnj->bni", A, ep)
            en += rng.normal(0.0, np.sqrt(qc), size=(B, N, 2))
            en[:, :, 0] -= ww[:, None]
            eps[r] = en
            Pm[r] = np.einsum("ij,bnjk,lk->bnil", A, Pp, A) + Qx[None, None]
            # attention for next round
            if mode == "full":
                Pn = Pm[r][:, 1:]  # (B,n,2,2)
                # info gain from own sensor + channel with noise rho, minus own only
                def gain(rho):
                    Jm = inv2(Pn).copy()
                    Jm[..., 0, 0] += 1.0 / R
                    if rho is not None:
                        Jm[..., 1, 1] += 1.0 / rho
                    Pq = inv2(Jm)
                    return 0.5 * np.log((Pn[..., 0, 0] * Pn[..., 1, 1] - Pn[..., 0, 1] ** 2) /
                                        (Pq[..., 0, 0] * Pq[..., 1, 1] - Pq[..., 0, 1] ** 2))
                gN, gS, gM = gain(None), gain(RS + Rc), gain(R + Rc)
                # options: none, S, mates (n-1)
                L = np.stack([gN, gS] + [gM] * (n - 1), axis=-1) * gamma
                L -= L.max(axis=-1, keepdims=True)
                P = np.exp(L); P /= P.sum(axis=-1, keepdims=True)
                u = rng.random(size=(B, n, 1))
                k = (np.cumsum(P, axis=-1) < u).sum(axis=-1)
            elif mode == "hab":
                k = rng.integers(0, n + 1, size=(B, n))  # 0 none, 1 S, 2.. mates
            elif mode == "pr":
                k = rng.integers(1, n + 1, size=(B, n))  # S or a mate
            elif mode == "dead":
                k = np.zeros((B, n), dtype=int)
            else:
                raise ValueError(mode)
            # map option index k -> choice code: 0 none -> -1 ; 1 -> S (0) ; 2.. -> mates
            ch = np.empty((B, n), dtype=int)
            for i in range(1, N):
                mates = [j for j in range(1, N) if j != i]
                kk = k[:, i - 1]
                ci = np.full(B, -1)
                ci[kk == 1] = 0
                for m_idx, j in enumerate(mates):
                    ci[kk == 2 + m_idx] = j
                ch[:, i - 1] = ci
            choice[r] = ch
        vlag = newv
    S_b = acc / cnt[:, None, None]
    S_all = acc.sum(axis=0) / cnt.sum()
    return S_all, S_b
