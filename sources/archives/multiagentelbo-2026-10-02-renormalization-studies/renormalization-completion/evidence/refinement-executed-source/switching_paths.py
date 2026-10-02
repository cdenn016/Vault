"""Normalized switching paths and Gaussian parent scores at fixed c_*.

These finite-step kernels are a declared splitting model. They are not an
exact continuous-time diffusion, and their parameter schedule is law-level.
"""
from __future__ import annotations

from math import expm1
from collections.abc import Sequence
import torch

from .coupled_learning import CoupledModel, CoupledState, comparison_maps, free_energy
from .network import assemble_network
from .network_dynamics import GaussianTransition
from .predictive_interfaces import ReducedPredictor


def source_posterior(
    X:     torch.Tensor,
    state: CoupledState,
    model: CoupledModel,
) -> torch.Tensor:
    r"""Return beta_ij(X) proportional to pi_ij exp(-D_ij(X)/tau)."""
    maps = comparison_maps(state.Theta, model)
    residual = X[:, :, None]-torch.einsum("nsij,bnsj->bnsi", maps, X[:, model.sources])
    cost = .5*torch.einsum("bnsi,nij,bnsj->bns", residual, model.H, residual)
    return torch.softmax(state.pi.log()-cost/model.tau, dim=-1)


def sheet_force(
    X:       torch.Tensor,
    weights: torch.Tensor,
    Theta:   torch.Tensor,
    model:   CoupledModel,
) -> torch.Tensor:
    r"""Compute grad_X [prior energy + sum_ij weights_ij D_ij/tau].

    Every receiver and sender contribution is included, for either common
    (N,S) weights or trajectory-specific (B,N,S) weights.
    """
    maps = comparison_maps(Theta, model)
    residual = X[:, :, None]-torch.einsum("nsij,bnsj->bnsi", maps, X[:, model.sources])
    record = weights[..., None]*torch.einsum("nij,bnsj->bnsi", model.H, residual)/model.tau
    force = torch.einsum("nij,bnj->bni", model.J_0, X-model.a)+record.sum(2)
    sender = -torch.einsum("nsji,bnsj->bnsi", maps, record)
    force.index_add_(1, model.sources.flatten(), sender.flatten(1, 2))
    return force


def reference_transition(
    mobility: torch.Tensor,
    state:    CoupledState,
    model:    CoupledModel,
    dt:       float,
) -> GaussianTransition:
    r"""Return X_next=(I-dt M J_beta)X+dt M h+sqrt(2 dt M) xi.

    Only the quadratic coefficients of the weighted-record action are used.
    Its auxiliary record normalization is not the source-label ELBO.
    """
    N, K = state.mu.shape
    beta = free_energy(state, model)[1]
    maps = comparison_maps(state.Theta, model)
    receiver = torch.arange(N, device=state.mu.device)[:, None].expand_as(model.sources)
    edges = torch.stack((receiver.flatten(), model.sources.flatten()), dim=-1)
    eye = torch.eye(K, dtype=state.mu.dtype, device=state.mu.device)
    action = assemble_network(
        model.J_0, model.a, eye.expand(len(edges), K, K), maps.flatten(0, 1),
        (beta[..., None, None]*model.H[:, None]/model.tau).flatten(0, 1),
        state.mu.new_zeros((len(edges), K)), edges)
    M = torch.block_diag(*mobility)
    return GaussianTransition(torch.eye(N*K, dtype=M.dtype, device=M.device)-dt*M@action.J,
                              dt*M@action.h, 2*dt*M)


def fine_row_kl(
    force_P:  torch.Tensor,
    force_Q:  torch.Tensor,
    mobility: torch.Tensor,
    dt:       float,
) -> torch.Tensor:
    r"""Return dt ||g_P-g_Q||_M^2/4 for equal-noise Gaussian transition rows."""
    difference = force_P-force_Q
    return dt/4*torch.einsum("bni,nij,bnj->b", difference, mobility, difference)


def gaussian_log_ratio(
    samples: torch.Tensor,
    mu_Q:    torch.Tensor,
    Sigma_Q: torch.Tensor,
    mu_S:    torch.Tensor,
    Sigma_S: torch.Tensor,
) -> torch.Tensor:
    r"""Return signed log q(x)-log s(x), without replacing its P-expectation."""
    def log_density(mu: torch.Tensor, Sigma: torch.Tensor) -> torch.Tensor:
        """Drop only the common dimension-dependent normalizing constant."""
        L = torch.linalg.cholesky(Sigma)
        z = torch.linalg.solve_triangular(L, (samples-mu).T, upper=False)
        return -.5*z.square().sum(0)-L.diagonal().log().sum()
    return log_density(mu_Q, Sigma_Q)-log_density(mu_S, Sigma_S)


def sample_switching_paths(
    mobility:    torch.Tensor,
    initial:     CoupledState,
    schedule:    Sequence[CoupledState],
    model:       CoupledModel,
    dt:          float,
    n_paths:     int,
    seed:        int,
    refresh_rate:float = 1.,
    output_stride:int = 1,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    r"""Sample P with global refresh probability 1-exp(-refresh_rate dt).

    On refresh, rows independently draw J from beta(X). The prior J is drawn
    independently from beta_q at activation. With output_stride>1, only the
    observation-grid states and final-microstep conditional means are returned;
    costs still sum all microsteps. Q shares this assignment kernel
    but uses the deterministic beta_q force, so its X marginal is Gaussian.
    """
    if dt <= 0 or refresh_rate < 0 or n_paths <= 0 or not schedule:
        raise ValueError("positive step/path count and nonnegative refresh rate required")
    if output_stride < 1 or len(schedule) % output_stride:
        raise ValueError("output stride must divide the microstep schedule")
    generator = torch.Generator(device=initial.mu.device).manual_seed(seed)
    B, (N, K), H = n_paths, initial.mu.shape, len(schedule)
    def noise() -> torch.Tensor:
        """Draw independent coordinates with the declared generator."""
        return torch.randn((B, N, K), dtype=initial.mu.dtype,
                           device=initial.mu.device, generator=generator)
    def labels(beta: torch.Tensor) -> torch.Tensor:
        """Draw all row labels, preserving a common random stream across arms."""
        return torch.multinomial(beta.reshape(-1, beta.shape[-1]), 1,
                                 generator=generator).reshape(B, N)
    X = initial.mu+torch.einsum("nij,bnj->bni", torch.linalg.cholesky(initial.Sigma), noise())
    J = labels(free_energy(initial, model)[1].expand(B, -1, -1))
    L = torch.linalg.cholesky(2*dt*mobility)
    paths = X.new_empty((B, H//output_stride+1, N, K))
    means = X.new_empty((B, H//output_stride, N, K))
    costs = X.new_zeros(B)
    paths[:, 0] = X
    for t, state in enumerate(schedule):
        beta_P = source_posterior(X, state, model)
        proposed = labels(beta_P)
        refresh = torch.rand((B, 1), dtype=X.dtype, device=X.device,
                             generator=generator) < -expm1(-refresh_rate*dt)
        J = torch.where(refresh, proposed, J)
        weights = torch.nn.functional.one_hot(J, state.pi.shape[-1]).to(X.dtype)
        g_P = sheet_force(X, weights, state.Theta, model)
        g_Q = sheet_force(X, free_energy(state, model)[1], state.Theta, model)
        costs += fine_row_kl(g_P, g_Q, mobility, dt)
        mean = X-dt*torch.einsum("nij,bnj->bni", mobility, g_P)
        X = mean+torch.einsum("nij,bnj->bni", L, noise())
        if (t+1) % output_stride == 0:
            observed = (t+1)//output_stride
            paths[:, observed] = X
            means[:, observed-1] = mean
    return paths, costs, means


def projected_row_bound(
    paths:             torch.Tensor,
    conditional_means: torch.Tensor,
    P:                 torch.Tensor,
    mobility:          torch.Tensor,
    dt:                float,
    parent:            ReducedPredictor,
) -> torch.Tensor:
    r"""Return sum_t KL(P(R_next|X,J)||S(R_next|R_history)) per path.

    Its expectation is retained-path KL plus conditional mutual information.
    The latter is independent of S, so paired score differences equal paired
    retained-path KL differences. Initial retained laws must agree.
    """
    R = paths.flatten(2) @ P.T                  # (B,H+1,m), actual retained history.
    mu_P = conditional_means.flatten(2) @ P.T
    m = parent.output_dimension
    Sigma = parent.Sigma_0
    L_0 = torch.linalg.cholesky(Sigma[:m, :m])
    gain = torch.cholesky_solve(Sigma[:m, m:], L_0).T
    mu_h = parent.mu_0[m:]+(R[:, 0]-parent.mu_0[:m]) @ gain.T
    Sigma_h = Sigma[m:, m:]-gain@Sigma[:m, m:]
    C = 2*dt*P@torch.block_diag(*mobility)@P.T
    logdet_C = 2*torch.linalg.cholesky(C).diagonal().log().sum()
    score = paths.new_zeros(len(paths))
    for t, kernel in enumerate(parent.kernels):
        A, B = kernel.F[:m, :m], kernel.F[:m, m:]
        D, E = kernel.F[m:, :m], kernel.F[m:, m:]
        mu_S = R[:, t]@A.T+mu_h@B.T+kernel.u[:m]
        innovation = B@Sigma_h@B.T+kernel.Q[:m, :m]
        innovation = (innovation+innovation.T)/2
        L = torch.linalg.cholesky(innovation)
        displacement = torch.linalg.solve_triangular(L, (mu_S-mu_P[:, t]).T, upper=False)
        score += .5*(torch.cholesky_solve(C, L).diagonal().sum()-m
                     +2*L.diagonal().log().sum()-logdet_C+displacement.square().sum(0))
        cross = E@Sigma_h@B.T+kernel.Q[m:, :m]
        gain = torch.cholesky_solve(cross.T, L).T
        mu_h = R[:, t]@D.T+mu_h@E.T+kernel.u[m:]+(R[:, t+1]-mu_S)@gain.T
        Sigma_h = E@Sigma_h@E.T+kernel.Q[m:, m:]-gain@cross.T
        Sigma_h = (Sigma_h+Sigma_h.T)/2
    return score


def all_sheet_curvature_bound(
    mobility: torch.Tensor,
    Theta:    torch.Tensor,
    model:    CoupledModel,
) -> float:
    r"""Bound every eigenvalue of L^T J_assignment L by an absolute row sum.

    All candidate record Hessians are PSD, so their sum dominates every
    assignment and every convexly weighted reference. M=L L^T is block diagonal.
    """
    N, K = model.a.shape
    maps = comparison_maps(Theta, model)
    receiver = torch.arange(N, device=Theta.device)[:, None].expand_as(model.sources)
    edges = torch.stack((receiver.flatten(), model.sources.flatten()), dim=-1)
    eye = torch.eye(K, dtype=Theta.dtype, device=Theta.device)
    action = assemble_network(
        model.J_0, model.a, eye.expand(len(edges), K, K), maps.flatten(0, 1),
        (model.H[:, None].expand(N, model.sources.shape[1], K, K)/model.tau).flatten(0, 1),
        model.a.new_zeros((len(edges), K)), edges)
    L = torch.linalg.cholesky(mobility)
    blocks = action.J.reshape(N, K, N, K).permute(0, 2, 1, 3)
    whitened = L[:, None].mT@blocks@L[None, :]
    return float(whitened.abs().sum((1, 3)).max())


def repeat_transition(kernel: GaussianTransition, count: int) -> GaussianTransition:
    r"""Compose count identical affine Gaussian rows by binary doubling."""
    if count < 1 or count & (count-1):
        raise ValueError("this subdivision requires a positive power of two")
    F, u, Q = kernel.F, kernel.u, kernel.Q
    for _ in range(count.bit_length()-1):
        Q_next = Q+F@Q@F.T
        u_next = u+F@u
        F = F@F
        u, Q = u_next, (Q_next+Q_next.T)/2
    return GaussianTransition(F, u, Q)
