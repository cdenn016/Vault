"""Predictive Gaussian interfaces and controlled reduced-state path budgets.

Mode selection concerns a fixed future-record stack. The compiled predictor is
an approximation to inherited dynamics, not endogenous learning or formation.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
import torch

from .network_dynamics import (
    GaussianHiddenFilter, GaussianTransition, initialize_filter, propagate_moments,
)


def _sym(Sigma: torch.Tensor) -> torch.Tensor:
    """Remove roundoff asymmetry of a derived covariance."""
    return (Sigma + Sigma.T) / 2


def _logdet(Sigma: torch.Tensor) -> torch.Tensor:
    r"""Return \log\det\Sigma for an SPD covariance."""
    return 2 * torch.linalg.cholesky(Sigma).diagonal().log().sum()


@dataclass(frozen=True)
class PredictiveReference:
    """Offline reference, including the actual fine moments at each time."""

    split:      torch.Tensor
    inverse:    torch.Tensor
    mu_0:       torch.Tensor
    Sigma_0:    torch.Tensor
    Sigma_h:    torch.Tensor
    C:          torch.Tensor
    noise:      torch.Tensor
    path_mu:    torch.Tensor
    path_Sigma: torch.Tensor
    kernels:    tuple[GaussianTransition, ...]
    means:      tuple[torch.Tensor, ...]
    covariances:tuple[torch.Tensor, ...]
    output_dimension: int


def predictive_reference(
    mu_0:        torch.Tensor,
    Sigma_0:     torch.Tensor,
    P:           torch.Tensor,
    transitions: Sequence[GaussianTransition],
) -> PredictiveReference:
    r"""Construct O=C H_0+b(R_0)+epsilon under the actual Gaussian activation.

    R=P X is fixed across all interfaces. Completing P by its orthogonal null
    rows gives an invertible retained/hidden split; F,u,Q are all carried.
    Shared innovation propagation supplies the full covariance of epsilon.
    """
    m, n = P.shape
    if not 0 < m < n or mu_0.shape != (n,) or Sigma_0.shape != (n, n) or not transitions:
        raise ValueError("need a nontrivial output, proper activation, and nonempty schedule")
    torch.linalg.cholesky(P @ P.T)
    torch.linalg.cholesky(Sigma_0)
    complement = torch.linalg.qr(P.T, mode="complete").Q[:, m:].T
    T = torch.cat((P, complement))                  # (n,n); first m rows are the output.
    T_inv = torch.linalg.solve(T, torch.eye(n, dtype=P.dtype, device=P.device))
    mu = T @ mu_0
    Sigma = _sym(T @ Sigma_0 @ T.T)
    kernels = tuple(GaussianTransition(T @ k.F @ T_inv, T @ k.u, _sym(T @ k.Q @ T.T))
                    for k in transitions)
    means, covariances = [mu], [Sigma]
    gain = torch.cholesky_solve(Sigma[:m, m:], torch.linalg.cholesky(Sigma[:m, :m])).T
    Sigma_h = _sym(Sigma[m:, m:] - gain @ Sigma[:m, m:])
    H = len(kernels)
    noise = Sigma.new_zeros((H*m, H*m))
    noise_fine = torch.zeros_like(Sigma)
    cross = Sigma.new_empty((n, 0))
    phi = torch.eye(n, dtype=Sigma.dtype, device=Sigma.device)
    offset = torch.zeros_like(mu)
    maps, offsets = [], []
    for t, kernel in enumerate(kernels):
        phi = kernel.F @ phi
        offset = kernel.F @ offset + kernel.u
        maps.append(phi[:m])
        offsets.append(offset[:m])
        cross = kernel.F @ cross
        noise_fine = _sym(kernel.F @ noise_fine @ kernel.F.T + kernel.Q)
        section = slice(t*m, (t+1)*m)
        noise[section, :t*m] = cross[:m]
        noise[:t*m, section] = cross[:m].T
        noise[section, section] = noise_fine[:m, :m]
        cross = torch.cat((cross, noise_fine[:, :m]), dim=1)
        mu, Sigma = propagate_moments(mu, Sigma, kernel)
        means.append(mu)
        covariances.append(Sigma)
    A = torch.cat(maps)                            # (H*m,n); fixed future observations.
    initial_mu, initial_Sigma = means[0], covariances[0]
    future_mu = A @ initial_mu + torch.cat(offsets)
    future_Sigma = _sym(A @ initial_Sigma @ A.T + noise)
    initial_cross = A @ initial_Sigma[:, :m]
    path_Sigma = torch.cat((
        torch.cat((initial_Sigma[:m, :m], initial_cross.T), dim=1),
        torch.cat((initial_cross, future_Sigma), dim=1),
    ), dim=0)
    return PredictiveReference(T, T_inv, initial_mu, initial_Sigma, Sigma_h,
                              A[:, m:], _sym(noise), torch.cat((initial_mu[:m], future_mu)),
                              _sym(path_Sigma), kernels, tuple(means), tuple(covariances), m)


@dataclass(frozen=True)
class SpectralInterface:
    """Reference-whitened statistic rows, ordered by predictive information."""

    nu: torch.Tensor
    W:  torch.Tensor


def spectral_interface(
    Sigma_h: torch.Tensor,
    C:       torch.Tensor,
    noise:   torch.Tensor,
) -> SpectralInterface:
    r"""Solve C^T Sigma_o^{-1} C x=nu Sigma_h^{-1} x by reference whitening.

    W_r H contains the first r canonical coordinates. PSD Gram eigenvalues
    at the floating-point zero floor are set to zero, not interpreted as
    negative information.
    """
    L_h = torch.linalg.cholesky(Sigma_h)
    whitened = torch.linalg.solve_triangular(torch.linalg.cholesky(noise), C @ L_h, upper=False)
    values, U = torch.linalg.eigh(_sym(whitened.T @ whitened))
    scale = max(1.0, float(values.abs().max()))
    if float(values.min()) < -100 * torch.finfo(values.dtype).eps * len(values) * scale:
        raise ArithmeticError("record Gram matrix has a materially negative eigenvalue")
    nu, U = values.flip(0).clamp_min(0), U.flip(1)
    W = torch.linalg.solve_triangular(L_h.T, U, upper=True).T
    return SpectralInterface(nu, W)


def discarded_information(
    Sigma_h: torch.Tensor,
    C:       torch.Tensor,
    noise:   torch.Tensor,
    W:       torch.Tensor,
) -> torch.Tensor:
    r"""Compute I(O;H|W H)=(log det Cov(O|W H)-log det Sigma_o)/2."""
    covariance = _sym(noise + C @ Sigma_h @ C.T)
    if len(W):
        cross = C @ Sigma_h @ W.T
        gain = torch.cholesky_solve(cross.T, torch.linalg.cholesky(_sym(W @ Sigma_h @ W.T)))
        covariance = _sym(covariance - cross @ gain)
    return (_logdet(covariance) - _logdet(noise)) / 2


@dataclass(frozen=True)
class ReducedPredictor:
    """Deployed controlled model; no fine-network covariance is stored here."""

    mu_0:     torch.Tensor
    Sigma_0:  torch.Tensor
    kernels:  tuple[GaussianTransition, ...]
    output_dimension: int

    def initialize(self, retained_value: torch.Tensor) -> GaussianHiddenFilter:
        """Initialize only the selected hidden coordinates from the actual marginal."""
        retained = torch.arange(self.output_dimension, device=self.mu_0.device)
        return initialize_filter(self.mu_0, self.Sigma_0, retained, retained_value)


def compile_predictor(
    reference: PredictiveReference,
    W:         torch.Tensor,
) -> ReducedPredictor:
    r"""Compile P(Y_next|Y) for Y=(R,W H), from actual fine pair marginals.

    These offline optimal Markov rows reproduce Y's pair marginals. Their
    R-path marginal can still differ from the inherited R path.
    """
    m, n = reference.output_dimension, len(reference.mu_0)
    A = reference.Sigma_0.new_zeros((m+len(W), n))
    A[:m, :m] = torch.eye(m, dtype=A.dtype, device=A.device)
    A[m:, m:] = W
    initial_mu = A @ reference.mu_0
    initial_Sigma = _sym(A @ reference.Sigma_0 @ A.T)
    kernels = []
    for t, fine in enumerate(reference.kernels):
        mu = A @ reference.means[t]
        Sigma = _sym(A @ reference.covariances[t] @ A.T)
        mu_next = A @ reference.means[t+1]
        Sigma_next = _sym(A @ reference.covariances[t+1] @ A.T)
        cross = A @ fine.F @ reference.covariances[t] @ A.T
        F = torch.cholesky_solve(cross.T, torch.linalg.cholesky(Sigma)).T
        kernels.append(GaussianTransition(F, mu_next-F @ mu, _sym(Sigma_next-F @ cross.T)))
    return ReducedPredictor(initial_mu, initial_Sigma, tuple(kernels), m)


def _predictor_path(parent: ReducedPredictor) -> tuple[torch.Tensor, torch.Tensor]:
    """Assemble the small model's output path moments, integrating its hidden state."""
    m, H = parent.output_dimension, len(parent.kernels)+1
    mu, Sigma = parent.mu_0, parent.Sigma_0
    path_mu = mu.new_empty(H*m)
    path_Sigma = Sigma.new_zeros((H*m, H*m))
    path_mu[:m], path_Sigma[:m, :m] = mu[:m], Sigma[:m, :m]
    cross = Sigma[:, :m]
    for t, kernel in enumerate(parent.kernels):
        cross = kernel.F @ cross
        mu, Sigma = propagate_moments(mu, Sigma, kernel)
        section = slice((t+1)*m, (t+2)*m)
        path_mu[section], path_Sigma[section, section] = mu[:m], Sigma[:m, :m]
        path_Sigma[section, :(t+1)*m] = cross[:m]
        path_Sigma[:(t+1)*m, section] = cross[:m].T
        cross = torch.cat((cross, Sigma[:, :m]), dim=1)
    return path_mu, _sym(path_Sigma)


def _gaussian_kl(
    mu:      torch.Tensor,
    Sigma:   torch.Tensor,
    mu_q:    torch.Tensor,
    Sigma_q: torch.Tensor,
) -> torch.Tensor:
    r"""Compute KL(N(mu,Sigma)||N(mu_q,Sigma_q)) with a whitened difference."""
    L = torch.linalg.cholesky(Sigma_q)
    A = torch.linalg.solve_triangular(L, Sigma-Sigma_q, upper=False)
    difference = torch.linalg.solve_triangular(L, A.T, upper=False).T
    values = torch.linalg.eigvalsh(_sym(difference))
    displacement = torch.linalg.solve_triangular(L, (mu-mu_q)[:, None], upper=False)
    return ((values-torch.log1p(values)).sum()+displacement.square().sum())/2


@dataclass(frozen=True)
class PathBudget:
    """Raw per-step omitted information and row risk, plus independent path KL."""

    memory:    torch.Tensor
    row_risk:  torch.Tensor
    direct_kl: torch.Tensor


def path_budget(
    path_mu:    torch.Tensor,
    path_Sigma: torch.Tensor,
    parent:     ReducedPredictor,
) -> PathBudget:
    r"""Split inherited path KL into I(R_next;history|f) plus candidate row risk.

    f=(current R,candidate hidden mean) is a deterministic history statistic;
    the candidate conditional covariance is deterministic. SVD removes only
    redundant statistic rows at the standard floating-point rank tolerance.
    Initial output laws must agree, so the activation term is zero.
    """
    m = parent.output_dimension
    candidate_mu, candidate_Sigma = _predictor_path(parent)
    torch.testing.assert_close(path_mu[:m], candidate_mu[:m])
    torch.testing.assert_close(path_Sigma[:m, :m], candidate_Sigma[:m, :m])
    state = parent.initialize(path_mu.new_zeros(m))
    # state.mu_h is the affine offset at zero observations; B maps the prefix.
    B = torch.cholesky_solve(parent.Sigma_0[:m, m:],
                            torch.linalg.cholesky(parent.Sigma_0[:m, :m])).T
    memory, risk = [], []
    for t, kernel in enumerate(parent.kernels):
        width = (t+1)*m
        history_mu, Gamma = path_mu[:width], path_Sigma[:width, :width]
        target = slice(width, width+m)
        cross = path_Sigma[target, :width]
        target_Sigma = path_Sigma[target, target]
        selector = Gamma.new_zeros((m, width))
        selector[:, -m:] = torch.eye(m, dtype=Gamma.dtype, device=Gamma.device)
        statistic = torch.cat((selector, B))
        _, singular, Vh = torch.linalg.svd(statistic, full_matrices=False)
        tolerance = torch.finfo(Gamma.dtype).eps * max(statistic.shape) * singular[0]
        basis = Vh[singular > tolerance]           # Row-space coordinates of f.
        covariance_f = _sym(basis @ Gamma @ basis.T)
        cross_f = cross @ basis.T
        G_f = torch.cholesky_solve(cross_f.T, torch.linalg.cholesky(covariance_f)).T @ basis
        G_full = torch.cholesky_solve(cross.T, torch.linalg.cholesky(Gamma)).T
        S_f = _sym(target_Sigma-G_f @ cross.T)
        S_full = _sym(target_Sigma-G_full @ cross.T)
        forecast = state.predict(kernel, path_mu.new_zeros(m))
        A, hidden_read = kernel.F[:m, :m], kernel.F[:m, m:]
        G_q = A @ selector + hidden_read @ B
        displacement = path_mu[target]-(forecast.mu_r+G_q @ history_mu)
        Delta = G_f-G_q
        L_q = torch.linalg.cholesky(forecast.Sigma_r)
        spread = torch.cholesky_solve(Delta @ Gamma @ Delta.T, L_q).diagonal().sum()
        memory.append((_logdet(S_f)-_logdet(S_full))/2)
        risk.append(_gaussian_kl(displacement, S_f, torch.zeros_like(displacement),
                                 forecast.Sigma_r)+spread/2)
        gain = torch.cholesky_solve(forecast.Sigma_hr.T, L_q).T
        B = torch.cat((kernel.F[m:, :m] @ selector + kernel.F[m:, m:] @ B-gain @ G_q,
                       gain), dim=1)
        state = state.condition(forecast, path_mu.new_zeros(m))
    return PathBudget(torch.stack(memory), torch.stack(risk),
                      _gaussian_kl(path_mu, path_Sigma, candidate_mu, candidate_Sigma))
