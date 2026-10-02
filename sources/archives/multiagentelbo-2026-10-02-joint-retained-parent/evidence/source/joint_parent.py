"""Normalized scheduled parents for the retained pair (P X, J)."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import torch

from .coupled_learning import CoupledModel, CoupledState, expected_costs
from .switching_paths import (
    SwitchingHistory, sheet_force, source_log_posterior, source_transition_log_prob,
)


@dataclass(frozen=True)
class GaussianLift:
    """A fixed activation-conditional lift and positive projected noise."""

    P:          torch.Tensor                 # (m,N*K)
    mu:         torch.Tensor                 # (N,K)
    gain:       torch.Tensor                 # (N*K,m)
    noise_chol: torch.Tensor                 # (m,m)

    def lift(self, R: torch.Tensor) -> torch.Tensor:
        r"""Return E_activation[X|P X=R], without using hidden sampled X."""
        return (self.mu.flatten()+(R-self.mu.flatten()@self.P.T)@self.gain.T).reshape(
            len(R), *self.mu.shape)


def compile_lift(
    P:        torch.Tensor,
    mobility: torch.Tensor,
    initial:  CoupledState,
    dt:       float,
) -> GaussianLift:
    r"""Compile G=Sigma P^T(P Sigma P^T)^-1 and C=2 dt P M P^T."""
    if dt <= 0:
        raise ValueError("positive microstep required")
    Sigma = torch.block_diag(*initial.Sigma)
    L = torch.linalg.cholesky(P@Sigma@P.T)
    gain = torch.cholesky_solve(P@Sigma, L).T
    noise_chol = torch.linalg.cholesky(2*dt*P@torch.block_diag(*mobility)@P.T)
    return GaussianLift(P, initial.mu, gain, noise_chol)


def joint_row_scores(
    history:      SwitchingHistory,
    P:            torch.Tensor,
    mobility:     torch.Tensor,
    initial:      CoupledState,
    schedule:     Sequence[CoupledState],
    model:        CoupledModel,
    dt:           float,
    refresh_rate: float = 1.,
) -> dict[str, torch.Tensor]:
    r"""Score source and Gaussian rows of four normalized joint parents.

    For source rows use beta_q or beta(X_lift); for configuration rows use
    the beta_q force or the newly observed assignment force. All candidates
    retain J and use the same actual projected history. Their initial law is
    the exact projected activation times the independent initial label law.

    The expectation of source_score + drift_score equals retained joint-path
    KL plus a nonnegative, candidate-independent conditional-information gap.
    Individual source scores are signed; they are never clamped.
    """
    if history.paths.shape[1] != len(schedule)+1:
        raise ValueError("joint scores require every microstep of the schedule")
    parent = compile_lift(P, mobility, initial, dt)
    R = history.paths.flatten(2)@P.T            # (B,H+1,m), no hidden coordinates.
    mu_P = history.conditional_means.flatten(2)@P.T
    scores = {name: R.new_zeros(len(R)) for name in (
        "source_reference", "source_lifted", "drift_reference", "drift_assignment")}
    for t, state in enumerate(schedule):
        X_lift = parent.lift(R[:, t])
        cost = expected_costs(state.mu, state.Sigma, state.Theta, model)[0]
        log_beta_q = torch.log_softmax(state.pi.log()-cost/model.tau, -1)
        old, new = history.assignments[:, t], history.assignments[:, t+1]
        rows = {"reference": log_beta_q.expand(len(R), -1, -1),
                "lifted": source_log_posterior(X_lift, state, model)}
        for name, log_beta in rows.items():
            proposed = source_transition_log_prob(log_beta, old, new, dt, refresh_rate)
            scores["source_"+name] += history.log_source_kernel[:, t]-proposed
        weights = {"reference": log_beta_q.exp(),
                   "assignment": torch.nn.functional.one_hot(new, state.pi.shape[-1]).to(R.dtype)}
        for name, weight in weights.items():
            force = sheet_force(X_lift, weight, state.Theta, model)
            mean_S = (X_lift-dt*torch.einsum("nij,bnj->bni", mobility, force)).flatten(1)@P.T
            difference = torch.linalg.solve_triangular(
                parent.noise_chol, (mean_S-mu_P[:, t]).T, upper=False)
            scores["drift_"+name] += .5*difference.square().sum(0)
    return scores
