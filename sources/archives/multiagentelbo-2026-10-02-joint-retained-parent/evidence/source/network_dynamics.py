"""History-conditioned Gaussian parents for observed pointwise link schedules.

Fine affine kernels and their schedule are supplied. Exact filtering does not
establish a small autonomous parent for endogenous source/link dynamics.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, log, pi
from typing import Sequence

import torch

from .network import GaussianAction


def _sym(matrix: torch.Tensor) -> torch.Tensor:
    """Remove only the roundoff asymmetry of a derived covariance."""
    return (matrix + matrix.T) / 2


def _logdet(matrix: torch.Tensor) -> torch.Tensor:
    r"""Compute log(det Sigma) from a positive-definite covariance."""
    return 2 * torch.linalg.cholesky(matrix).diagonal().log().sum()


def _partition(retained: torch.Tensor, dimension: int) -> torch.Tensor:
    """Validate ordered retained coordinates and return their complement."""
    if (retained.ndim != 1 or retained.dtype != torch.long or not retained.numel()
            or retained.unique().numel() != retained.numel()):
        raise ValueError("retained coordinates must be a distinct nonempty long vector")
    if bool(((retained < 0) | (retained >= dimension)).any()):
        raise ValueError("retained coordinate lies outside the fine state")
    keep = torch.ones(dimension, dtype=torch.bool, device=retained.device)
    keep[retained] = False
    return torch.arange(dimension, device=retained.device)[keep]


@dataclass(frozen=True)
class GaussianTransition:
    r"""Affine kernel X_next=F X+u+eta with independent eta~N(0,Q)."""

    F: torch.Tensor
    u: torch.Tensor
    Q: torch.Tensor

    def __post_init__(self) -> None:
        if self.F.ndim != 2 or self.F.shape[0] != self.F.shape[1]:
            raise ValueError("F must be square")
        if self.u.shape != (len(self.F),) or self.Q.shape != self.F.shape:
            raise ValueError("transition dimensions differ")
        if any(x.dtype != self.F.dtype or x.device != self.F.device for x in (self.u, self.Q)):
            raise ValueError("transition tensors must share dtype and device")
        GaussianAction(self.Q, self.u, 0.0)
        if not bool(torch.isfinite(self.F).all()):
            raise ValueError("F must be finite")
        torch.linalg.cholesky(self.Q)


def ou_transition(
    J:        torch.Tensor,
    h:        torch.Tensor,
    mobility: torch.Tensor,
    dt:       float,
) -> GaussianTransition:
    r"""Exact frozen-interval kernel of dX=-M(JX-h)dt+sqrt(2M)dW.

    For M=L L^T and S=L^T J L, F=L exp(-S dt)L^-1,
    u=L S^-1(I-exp(-S dt))L^T h, and
    Q=L S^-1(I-exp(-2S dt))L^T. A changing action is held
    over each interval; this is not the exact flow of a smooth schedule.
    """
    if not isfinite(dt) or dt <= 0:
        raise ValueError("dt must be finite and positive")
    GaussianAction(J, h, 0.0)
    if mobility.shape != J.shape or mobility.dtype != J.dtype or mobility.device != J.device:
        raise ValueError("mobility must match J")
    GaussianAction(mobility, torch.zeros_like(h), 0.0)
    L = torch.linalg.cholesky(mobility)
    eigenvalues, U = torch.linalg.eigh(_sym(L.T @ J @ L))
    if bool((eigenvalues <= 0).any()):
        raise ValueError("OU action must be positive definite")
    decay = torch.exp(-dt * eigenvalues)
    E = (U * decay) @ U.T
    F = torch.linalg.solve_triangular(L.T, (L @ E).T, upper=True).T
    response = -torch.expm1(-dt * eigenvalues) / eigenvalues
    u = L @ (U @ (response * (U.T @ (L.T @ h))))
    noise = -torch.expm1(-2 * dt * eigenvalues) / eigenvalues
    Q = _sym(L @ ((U * noise) @ U.T) @ L.T)
    return GaussianTransition(F, u, Q)


def propagate_moments(
    mu:         torch.Tensor,
    Sigma:      torch.Tensor,
    transition: GaussianTransition,
) -> tuple[torch.Tensor, torch.Tensor]:
    r"""Propagate actual moments: mu'=F mu+u, Sigma'=F Sigma F^T+Q."""
    return transition.F @ mu + transition.u, _sym(transition.F @ Sigma @ transition.F.T + transition.Q)


@dataclass(frozen=True)
class GaussianForecast:
    """Joint next-step law conditional on the supplied retained history."""

    mu_r:     torch.Tensor
    Sigma_r:  torch.Tensor
    mu_h:     torch.Tensor
    Sigma_h:  torch.Tensor
    Sigma_hr: torch.Tensor

    def log_prob(self, retained_value: torch.Tensor) -> torch.Tensor:
        r"""Return the retained predictive log density at the next observation."""
        residual = retained_value - self.mu_r
        L = torch.linalg.cholesky(self.Sigma_r)
        solved = torch.linalg.solve_triangular(L, residual[:, None], upper=False)[:, 0]
        return -(len(residual) * log(2 * pi) + 2 * L.diagonal().log().sum() + solved @ solved) / 2


@dataclass(frozen=True)
class GaussianHiddenFilter:
    """Hidden conditional given retained history; dimension grows with fine state."""

    retained: torch.Tensor
    hidden:   torch.Tensor
    mu_h:     torch.Tensor
    Sigma_h:  torch.Tensor

    def predict(
        self,
        transition:     GaussianTransition,
        retained_value: torch.Tensor,
    ) -> GaussianForecast:
        r"""Predict the next joint law, including correlated process-noise blocks."""
        r, h = self.retained, self.hidden
        F, u, Q = transition.F, transition.u, transition.Q
        A, B = F[r][:, r], F[r][:, h]
        C, D = F[h][:, r], F[h][:, h]
        mu_r = A @ retained_value + B @ self.mu_h + u[r]
        mu_h = C @ retained_value + D @ self.mu_h + u[h]
        Sigma_r = _sym(B @ self.Sigma_h @ B.T + Q[r][:, r])
        Sigma_h = _sym(D @ self.Sigma_h @ D.T + Q[h][:, h])
        Sigma_hr = D @ self.Sigma_h @ B.T + Q[h][:, r]
        return GaussianForecast(mu_r, Sigma_r, mu_h, Sigma_h, Sigma_hr)

    def condition(
        self,
        forecast:       GaussianForecast,
        retained_value: torch.Tensor,
    ) -> GaussianHiddenFilter:
        r"""Condition the predicted hidden law on the next retained observation."""
        L = torch.linalg.cholesky(forecast.Sigma_r)
        gain = torch.cholesky_solve(forecast.Sigma_hr.T, L).T
        mu_h = forecast.mu_h + gain @ (retained_value - forecast.mu_r)
        Sigma_h = _sym(forecast.Sigma_h - gain @ forecast.Sigma_hr.T)
        return GaussianHiddenFilter(self.retained, self.hidden, mu_h, Sigma_h)


def initialize_filter(
    mu_0:           torch.Tensor,
    Sigma_0:        torch.Tensor,
    retained:       torch.Tensor,
    retained_value: torch.Tensor,
) -> GaussianHiddenFilter:
    r"""Initialize from the actual joint activation law, not an equilibrium reset."""
    if mu_0.ndim != 1 or Sigma_0.shape != (len(mu_0), len(mu_0)):
        raise ValueError("activation moment dimensions differ")
    if retained.device != mu_0.device:
        raise ValueError("retained coordinates must share the activation device")
    hidden = _partition(retained, len(mu_0))
    if retained_value.shape != retained.shape:
        raise ValueError("retained observation dimension differs")
    covariance_r = Sigma_0[retained][:, retained]
    covariance_hr = Sigma_0[hidden][:, retained]
    L = torch.linalg.cholesky(covariance_r)
    gain = torch.cholesky_solve(covariance_hr.T, L).T
    mu_h = mu_0[hidden] + gain @ (retained_value - mu_0[retained])
    Sigma_h = _sym(Sigma_0[hidden][:, hidden] - gain @ covariance_hr.T)
    return GaussianHiddenFilter(retained, hidden, mu_h, Sigma_h)


def _pair_projection(
    mu:         torch.Tensor,
    Sigma:      torch.Tensor,
    mu_next:    torch.Tensor,
    Sigma_next: torch.Tensor,
    retained:   torch.Tensor,
    transition: GaussianTransition,
) -> GaussianTransition:
    """Construct the retained kernel from one actual pair marginal."""
    Sigma_r = Sigma[retained][:, retained]
    cross = transition.F[retained] @ Sigma[:, retained]  # (r,r), Cov(R_next,R)
    F = torch.cholesky_solve(cross.T, torch.linalg.cholesky(Sigma_r)).T
    u = mu_next[retained] - F @ mu[retained]
    Q = _sym(Sigma_next[retained][:, retained] - F @ cross.T)
    return GaussianTransition(F, u, Q)


def markov_projection(
    mu:         torch.Tensor,
    Sigma:      torch.Tensor,
    transition: GaussianTransition,
    retained:   torch.Tensor,
) -> GaussianTransition:
    r"""Return P(R_next|R) from actual moments, the optimal one-step path rows.

    Rows depend on time and the actual preparation. They reproduce pair and
    one-time marginals, but need not reproduce the full retained path law.
    """
    _partition(retained, len(mu))
    mu_next, Sigma_next = propagate_moments(mu, Sigma, transition)
    return _pair_projection(mu, Sigma, mu_next, Sigma_next, retained, transition)


def memory_information(
    mu_0:        torch.Tensor,
    Sigma_0:     torch.Tensor,
    retained:    torch.Tensor,
    transitions: Sequence[GaussianTransition],
) -> torch.Tensor:
    r"""Per-step forward KL to the optimal time-dependent one-step parent.

    For a deterministic affine schedule with independent Gaussian noises,
    D_path=1/2 sum_n [log(det Q_M,n)-log(det S_history,n)].
    The first contribution is zero. This expectation identity uses the actual
    activation law; it does not score arbitrary candidate or equilibrium rows.
    """
    mu, Sigma = mu_0, Sigma_0
    state = initialize_filter(mu, Sigma, retained, mu[retained])
    values: list[torch.Tensor] = []
    for transition in transitions:
        forecast = state.predict(transition, mu[retained])
        mu_next, Sigma_next = propagate_moments(mu, Sigma, transition)
        parent = _pair_projection(mu, Sigma, mu_next, Sigma_next, retained, transition)
        values.append((_logdet(parent.Q) - _logdet(forecast.Sigma_r)) / 2)
        state = state.condition(forecast, mu_next[retained])
        mu, Sigma = mu_next, Sigma_next
    return torch.stack(values) if values else mu.new_empty(0)
