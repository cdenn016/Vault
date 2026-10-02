"""Locality through the source prior: omitted-history information of a block parent.

Held-assignment reading at c_*: attention weights are held at the source prior
pi_ij, links are held, and the belief means follow a held Ornstein-Uhlenbeck flow
of the resulting quadratic action. The retained process is a declared block-mean
projection. Everything here is exact dense Gaussian linear algebra for one
declared finite instance; nothing in this module is a large-N theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
import torch

from .network import GaussianAction
from .network_dynamics import GaussianTransition, ou_transition

PRIOR_FAMILIES = ("window", "exponential", "power", "complete", "directed_window")


def _sym(matrix: torch.Tensor) -> torch.Tensor:
    """Remove roundoff asymmetry of a derived covariance."""
    return (matrix + matrix.T) / 2


def _logdet(matrix: torch.Tensor) -> torch.Tensor:
    r"""Return log(det Sigma) for a positive-definite Sigma via Cholesky."""
    return 2 * torch.linalg.cholesky(matrix).diagonal().log().sum()


def ring_distance(n_agents: int) -> torch.Tensor:
    r"""Declared agent-set distance d(i,j)=min(|i-j|, N-|i-j|) on a ring."""
    index = torch.arange(n_agents)
    gap = (index[:, None] - index[None, :]).abs()
    return torch.minimum(gap, n_agents - gap)


def source_prior(
    n_agents: int,
    family:   str,
    radius:   int | None = None,
    decay:    float | None = None,
    alpha:    float | None = None,
) -> torch.Tensor:
    r"""Row-stochastic source prior pi_ij on the ring, pi_ii=0, sum_j pi_ij=1.

    Unnormalized weights with ring distance d=d(i,j)>=1:
    window 1[d<=R]; exponential exp(-m d) (times 1[d<=R] if R is given);
    power d^{-alpha}; complete 1; directed_window 1[j=i-s mod N, 1<=s<=R],
    a one-way support with pi_ij>0 and pi_ji=0.
    Returns an (N,N) float64 tensor, rows are receivers i, columns sources j.
    """
    if n_agents < 3:
        raise ValueError("a ring prior needs at least three agents")
    d = ring_distance(n_agents).to(torch.float64)
    off = d > 0
    if family == "window" or family == "directed_window":
        if radius is None or not 1 <= radius < n_agents / 2:
            raise ValueError("window radius must satisfy 1<=R<N/2")
    if family == "window":
        w = (off & (d <= radius)).to(torch.float64)
    elif family == "exponential":
        if decay is None or decay <= 0:
            raise ValueError("exponential decay rate must be positive")
        w = torch.where(off, torch.exp(-decay * d), torch.zeros_like(d))
        if radius is not None:
            w = w * (d <= radius)
    elif family == "power":
        if alpha is None or alpha <= 0:
            raise ValueError("power-law exponent must be positive")
        w = torch.where(off, d.clamp(min=1) ** (-alpha), torch.zeros_like(d))
    elif family == "complete":
        w = off.to(torch.float64)
    elif family == "directed_window":
        index = torch.arange(n_agents)
        w = torch.zeros((n_agents, n_agents), dtype=torch.float64)
        for step in range(1, radius + 1):
            w[index, (index - step) % n_agents] = 1.0
    else:
        raise ValueError(f"unknown prior family {family!r}; expected one of {PRIOR_FAMILIES}")
    return w / w.sum(dim=1, keepdim=True)


def independent_links(
    n_agents:  int,
    dimension: int,
    sigma:     float,
    seed:      int,
) -> torch.Tensor:
    r"""Seeded independent GL+(K,R) links Omega_ij=exp(sigma G_ij), G_ij iid N(0,1).

    One link per ordered pair, so every prior family on the same N sees the
    same link draw on its support (common random numbers). sigma=0 gives
    identity links. Shape (N,N,K,K).
    """
    generator = torch.Generator(device="cpu").manual_seed(seed)
    G = torch.randn((n_agents, n_agents, dimension, dimension), generator=generator, dtype=torch.float64)
    if sigma == 0:
        return torch.eye(dimension, dtype=torch.float64).expand(n_agents, n_agents, dimension, dimension).clone()
    return torch.linalg.matrix_exp(sigma * G)


def _to_dense(blocks: torch.Tensor) -> torch.Tensor:
    """Map (N,N,K,K) node blocks to the (N K,N K) matrix with node-major order."""
    N, _, K, _ = blocks.shape
    return blocks.permute(0, 2, 1, 3).reshape(N * K, N * K)


def held_prior_action(
    pi:     torch.Tensor,
    Omega:  torch.Tensor,
    a:      float,
    kappa:  float,
) -> GaussianAction:
    r"""Held-assignment quadratic action of the collective free energy.

    E(x)=(a/2) sum_i |x_i|^2 + (kappa/2) sum_{i,j} pi_ij |x_i - Omega_ij x_j|^2,
    i.e. attention held at the prior and each record of precision kappa pi_ij I.
    Its precision has blocks
    J_ii = a I + kappa (sum_j pi_ij) I + kappa sum_l pi_li Omega_li^T Omega_li,
    J_ij = -kappa (pi_ij Omega_ij + pi_ji Omega_ji^T), i != j.
    A one-way row (pi_ij>0, pi_ji=0) still enters both endpoints (joint descent).
    """
    N, _, K, _ = Omega.shape
    if pi.shape != (N, N) or bool((pi.diagonal() != 0).any()):
        raise ValueError("prior must be (N,N) with zero diagonal")
    if a <= 0 or kappa < 0:
        raise ValueError("on-site precision must be positive and kappa nonnegative")
    eye = torch.eye(K, dtype=Omega.dtype)
    weighted = kappa * pi[..., None, None] * Omega                     # (N,N,K,K)
    blocks = -(weighted + weighted.transpose(0, 1).transpose(-1, -2))  # J_ij off-diagonal
    gram = torch.einsum("li,lixy,lixz->iyz", kappa * pi, Omega, Omega)  # sum_l pi_li Omega^T Omega
    diagonal = (a + kappa * pi.sum(1))[:, None, None] * eye + gram
    index = torch.arange(N)
    blocks[index, index] = diagonal
    J = _sym(_to_dense(blocks))
    return GaussianAction(J, torch.zeros(N * K, dtype=J.dtype), 0.0)


def row_only_drift(
    pi:     torch.Tensor,
    Omega:  torch.Tensor,
    a:      float,
    kappa:  float,
) -> torch.Tensor:
    r"""Declared non-descent drift in which a receiver is moved only by its own rows.

    dx_i = -[a x_i + kappa sum_j pi_ij (x_i - Omega_ij x_j)] dt + sqrt(2) dW_i,
    so K_ii=(a+kappa sum_j pi_ij) I and K_ij=-kappa pi_ij Omega_ij. This drops
    the sender terms of other agents' records; it is not descent of the
    collective free energy and is used only as a declared contrast.
    """
    N, _, K, _ = Omega.shape
    blocks = -kappa * pi[..., None, None] * Omega
    index = torch.arange(N)
    blocks[index, index] = (a + kappa * pi.sum(1))[:, None, None] * torch.eye(K, dtype=Omega.dtype)
    return _to_dense(blocks)


def lyapunov_stationary(K: torch.Tensor) -> torch.Tensor:
    r"""Stationary covariance of dX=-K X dt+sqrt(2) dW: K Sigma + Sigma K^T = 2 I.

    The CPU Schur (Bartels-Stewart) solve does not require a diagonalizable K.
    Requires Re lambda(K)>0, and checks the normalized equation residual and
    positive definiteness. This numerical reference does not provide autograd.
    On the mixed torch/SciPy Windows runtime, select MKL_THREADING_LAYER=SEQUENTIAL
    before starting the interpreter; this helper does not change native settings.
    """
    from scipy.linalg import eigvals, solve_continuous_lyapunov

    K_cpu = K.detach().cpu().numpy()
    if bool((eigvals(K_cpu).real <= 0).any()):
        raise ValueError("drift is not stable")
    identity = torch.eye(len(K), dtype=K.dtype, device=K.device)
    Sigma = torch.as_tensor(solve_continuous_lyapunov(K_cpu, 2 * identity.cpu().numpy()),
                            dtype=K.dtype, device=K.device)
    Sigma = _sym(Sigma)
    residual = K @ Sigma + Sigma @ K.T - 2 * identity
    scale = 2 * torch.linalg.matrix_norm(K) * torch.linalg.matrix_norm(Sigma) + 2 * torch.linalg.matrix_norm(identity)
    normalized = torch.linalg.matrix_norm(residual) / scale
    if not bool(torch.isfinite(normalized)) or float(normalized) > 64 * len(K) * torch.finfo(K.dtype).eps:
        raise ValueError("stationary covariance fails the normalized Lyapunov residual check")
    _, info = torch.linalg.cholesky_ex(Sigma)
    if int(info) != 0:
        raise ValueError("stationary covariance is not positive definite")
    return Sigma


def block_mean_projector(n_agents: int, dimension: int, block: int) -> torch.Tensor:
    r"""Declared parent Z_B = b^{-1} sum_{i in B} x_i over contiguous blocks of size b.

    Shape (m, N K) with m=(N/b) K, ordered (block, fiber component).
    """
    if block < 1 or n_agents % block:
        raise ValueError("block size must divide the agent count")
    n_blocks = n_agents // block
    P = torch.zeros((n_blocks, dimension, n_agents, dimension), dtype=torch.float64)
    eye = torch.eye(dimension, dtype=torch.float64)
    for B in range(n_blocks):
        P[B, :, B * block:(B + 1) * block, :] = eye[:, None, :] / block
    return P.reshape(n_blocks * dimension, n_agents * dimension)


def retained_autocovariances(
    F:       torch.Tensor,
    Sigma:   torch.Tensor,
    P:       torch.Tensor,
    horizon: int,
) -> torch.Tensor:
    r"""Stationary lag covariances C(s)=Cov(Z_{t+s},Z_t)=P F^s Sigma P^T, s<horizon.

    Returns shape (horizon, m, m).
    """
    Y = Sigma @ P.T                            # (n, m)
    lags = []
    for _ in range(horizon):
        lags.append(P @ Y)
        Y = F @ Y
    return torch.stack(lags)


def block_toeplitz(C: torch.Tensor) -> torch.Tensor:
    r"""Path covariance [Cov(Z_t,Z_u)]_{t,u<H} with Cov(Z_t,Z_u)=C(t-u) for t>=u."""
    H, m, _ = C.shape
    out = C.new_empty((H * m, H * m))
    for t in range(H):
        for u in range(H):
            out[t * m:(t + 1) * m, u * m:(u + 1) * m] = C[t - u] if t >= u else C[u - t].T
    return out


def innovation_logdets(path_covariance: torch.Tensor, m: int) -> torch.Tensor:
    r"""log det Cov(Z_t | Z_{0:t-1}) for every t from one block Cholesky factor."""
    diagonal = torch.linalg.cholesky(path_covariance).diagonal().log()
    return 2 * diagonal.reshape(-1, m).sum(1)


def omitted_history_information(logdets: torch.Tensor, k: int, horizon: int) -> torch.Tensor:
    r"""Stationary D_{H,k}=sum_{t=k+1}^{H-1} I(Z_t;Z_{0:t-k-1}|Z_{t-k:t-1}).

    With l_t=log det Cov(Z_t|Z_{0:t-1}) and stationarity,
    Cov(Z_t|Z_{t-k:t-1}) has log-determinant l_k, so
    D_{H,k} = (1/2) sum_{t=k+1}^{H-1} (l_k - l_t).
    """
    if not 0 <= k or horizon > len(logdets):
        raise ValueError("need k>=0 and horizon within the computed logdets")
    return (logdets[k] - logdets[k + 1:horizon]).sum() / 2


def omitted_history_information_direct(
    path_covariance: torch.Tensor,
    m:               int,
    k:               int,
    horizon:         int,
) -> torch.Tensor:
    r"""Cancellation-free D_{H,k} term by term from conditional canonical correlations.

    Given the recent block rec=Z_{t-k:t-1}, write S for conditional covariances of
    Z_t and old=Z_{0:t-k-1}. With S_tt=L L^T and nu the eigenvalues of
    W=L^{-1} S_to S_oo^{-1} S_ot L^{-T} (in [0,1)),
    I(Z_t;old|rec) = -(1/2) sum log(1-nu). No stationarity is used.
    """
    total = path_covariance.new_zeros(())
    for t in range(k + 1, horizon):
        target = slice(t * m, (t + 1) * m)
        old, recent = slice(0, (t - k) * m), slice((t - k) * m, t * m)
        S_tt = path_covariance[target, target]
        S_to = path_covariance[target, old]
        S_oo = path_covariance[old, old]
        if k:
            L_r = torch.linalg.cholesky(path_covariance[recent, recent])
            A_t = torch.linalg.solve_triangular(L_r, path_covariance[recent, target], upper=False)
            A_o = torch.linalg.solve_triangular(L_r, path_covariance[recent, old], upper=False)
            S_tt, S_to, S_oo = S_tt - A_t.T @ A_t, S_to - A_t.T @ A_o, S_oo - A_o.T @ A_o
        L_t = torch.linalg.cholesky(_sym(S_tt))
        B = torch.linalg.solve_triangular(L_t, S_to, upper=False)                      # (m, old)
        L_o = torch.linalg.cholesky(_sym(S_oo))
        C = torch.linalg.solve_triangular(L_o, B.T, upper=False)                        # (old, m)
        nu = torch.linalg.eigvalsh(_sym(C.T @ C))
        total = total - torch.log1p(-nu).sum() / 2
    return total


def schur_ou_competitor(
    C0: torch.Tensor,
    P:  torch.Tensor,
    dt: float,
) -> GaussianTransition:
    r"""Memoryless Schur-OU parent: dR=-M_c J_c R dt+sqrt(2 M_c) dW.

    J_c=(P Sigma P^T)^{-1} is the exact marginal precision of the retained
    coordinates and M_c=P P^T the pushed-forward identity mobility. Its
    stationary law equals the actual retained marginal, so the activation
    term b_0 vanishes.
    """
    J_c = _sym(torch.cholesky_inverse(torch.linalg.cholesky(C0)))
    M_c = _sym(P @ P.T)
    return ou_transition(J_c, torch.zeros(len(C0), dtype=C0.dtype), M_c, dt)


def markov_path_covariance(C0: torch.Tensor, F_c: torch.Tensor, horizon: int) -> torch.Tensor:
    r"""Path covariance of a stationary Markov chain: C_c(s)=F_c^s C0."""
    lags, current = [], C0
    for _ in range(horizon):
        lags.append(current)
        current = F_c @ current
    return block_toeplitz(torch.stack(lags))


def gaussian_kl(Sigma_p: torch.Tensor, Sigma_q: torch.Tensor) -> torch.Tensor:
    r"""KL(N(0,Sigma_p)||N(0,Sigma_q)) = [tr(Sigma_q^{-1}Sigma_p)-n+log det Sigma_q-log det Sigma_p]/2."""
    L_q = torch.linalg.cholesky(Sigma_q)
    trace = torch.cholesky_solve(Sigma_p, L_q).diagonal().sum()
    return (trace - len(Sigma_p) + 2 * L_q.diagonal().log().sum() - _logdet(Sigma_p)) / 2


def gaussian_kl_stable(Sigma_p: torch.Tensor, Sigma_q: torch.Tensor) -> torch.Tensor:
    r"""Cancellation-free KL(N(0,Sigma_p)||N(0,Sigma_q)) for nearby covariances.

    With Sigma_q=L L^T and eigenvalues mu of M=L^{-1}(Sigma_p-Sigma_q)L^{-T},
    KL = (1/2) sum (mu - log(1+mu)); the difference is formed before whitening.
    """
    L_q = torch.linalg.cholesky(Sigma_q)
    half = torch.linalg.solve_triangular(L_q, Sigma_p - Sigma_q, upper=False)
    M = torch.linalg.solve_triangular(L_q, half.T, upper=False)
    mu = torch.linalg.eigvalsh(_sym(M))
    return (mu - torch.log1p(mu)).sum() / 2


def competitor_row_risk(
    path_covariance: torch.Tensor,
    m:               int,
    k:               int,
    horizon:         int,
    competitor:      GaussianTransition,
) -> torch.Tensor:
    r"""Expected row divergence of a one-step competitor against optimal k-context rows.

    For context length c=min(k,t) the optimal row is N(G z, S) with
    G=Cov(Z_c,Z_{0:c-1}) Gamma^{-1} and S=C(0)-G Cov(Z_{0:c-1},Z_c); the competitor
    row is N(F_c z_{t-1}, Q_c). With Delta=G-[0,...,0,F_c],
    E KL = KL(N(0,S)||N(0,Q_c)) + tr(Q_c^{-1} Delta Gamma Delta^T)/2, the first term in
    the cancellation-free form of gaussian_kl_stable.
    Summed over t=1..H-1; t=0 contributes b_0=0 (identical stationary marginals).
    """
    if k < 1:
        raise ValueError("a one-step competitor is a k-context row only for k>=1")
    F_c, Q_c = competitor.F, competitor.Q
    L_Q = torch.linalg.cholesky(Q_c)
    C0 = path_covariance[:m, :m]
    total = C0.new_zeros(())
    for c in range(1, min(k, horizon - 1) + 1):
        Gamma = path_covariance[:c * m, :c * m]
        cross = path_covariance[c * m:(c + 1) * m, :c * m]
        G = torch.cholesky_solve(cross.T, torch.linalg.cholesky(Gamma)).T
        S = _sym(C0 - G @ cross.T)
        Delta = G.clone()
        Delta[:, (c - 1) * m:] -= F_c
        spread = torch.cholesky_solve(Delta @ Gamma @ Delta.T, L_Q).diagonal().sum()
        row = gaussian_kl_stable(S, Q_c) + spread / 2
        count = horizon - k if c == k else 1
        total = total + count * row
    return total


def fitted_decay_ratio(values: torch.Tensor, ks: range) -> float | None:
    r"""exp(slope) of a least-squares line through log values[k], k in ks; None if any value<=0."""
    y = torch.stack([values[k] for k in ks])
    if bool((y <= 0).any()):
        return None
    x = torch.tensor(list(ks), dtype=torch.float64)
    slope = ((x - x.mean()) * (y.log() - y.log().mean())).sum() / ((x - x.mean()) ** 2).sum()
    return float(slope.exp())


@dataclass(frozen=True)
class ParentMemory:
    """Omitted-history information of the declared block parent for one instance."""

    logdets:      torch.Tensor   # (H,), log det Cov(Z_t|Z_{0:t-1})
    D:            torch.Tensor   # (k_max+1,), D_{H,k}
    delta:        torch.Tensor   # (k_max+1,), per-step increments (l_k-l_{k+1})/2
    row_risk:     torch.Tensor   # (k_max+1,), competitor row risk; entry 0 is nan
    path_kl:      torch.Tensor | None   # cancellation-free when computed
    path_kl_naive: torch.Tensor | None
    D_direct:     torch.Tensor | None   # cancellation-free D_{H,k}, when computed
    fine_gap:     float          # slowest fine relaxation rate (min Re eig of drift)


def parent_memory(
    Sigma:        torch.Tensor,
    P:            torch.Tensor,
    dt:           float,
    horizon:      int,
    k_max:        int,
    F:            torch.Tensor,
    path_kl:      bool,
    stable_kl:    bool,
    direct_D:     bool,
    fine_gap:     float,
) -> ParentMemory:
    r"""Compute D_{H,k}, decay increments, competitor row risk and optional path KL.

    The fine law is stationary N(0,Sigma) under X_{t+1}=F X_t+eta; Z=P X.
    """
    if horizon < k_max + 2:
        raise ValueError("horizon must exceed k_max+1")
    m = len(P)
    C = retained_autocovariances(F, Sigma, P, horizon)
    path = block_toeplitz(C)
    logdets = innovation_logdets(path, m)
    D = torch.stack([omitted_history_information(logdets, k, horizon) for k in range(k_max + 1)])
    delta = (logdets[:k_max + 1] - logdets[1:k_max + 2]) / 2
    competitor = schur_ou_competitor(_sym(C[0]), P, dt)
    risk = [torch.tensor(float("nan"), dtype=torch.float64)]
    risk += [competitor_row_risk(path, m, k, horizon, competitor) for k in range(1, k_max + 1)]
    kl = naive = None
    if path_kl:
        markov = markov_path_covariance(_sym(C[0]), competitor.F, horizon)
        naive = gaussian_kl(path, markov)
        kl = gaussian_kl_stable(path, markov) if stable_kl else None
    D_direct = (torch.stack([omitted_history_information_direct(path, m, k, horizon) for k in range(k_max + 1)])
                if direct_D else None)
    return ParentMemory(logdets, D, delta, torch.stack(risk), kl, naive, D_direct, fine_gap)


def block_basis(n_agents: int, dimension: int, block: int) -> tuple[torch.Tensor, torch.Tensor]:
    r"""Invertible T with the block means as its first m rows and in-block deviations after.

    Returns (T, retained) so that (T x)[retained] = P x. Used to route the block
    parent through the existing coordinate-selection hidden filter.
    """
    P = block_mean_projector(n_agents, dimension, block)
    n = n_agents * dimension
    rows = []
    for B in range(n_agents // block):
        for j in range(block - 1):
            for c in range(dimension):
                i = (B * block + j) * dimension + c
                e = torch.zeros(n, dtype=torch.float64)
                e[i] = 1.0
                rows.append(e - P[B * dimension + c])
    T = torch.cat((P, torch.stack(rows))) if rows else P
    return T, torch.arange(len(P))

