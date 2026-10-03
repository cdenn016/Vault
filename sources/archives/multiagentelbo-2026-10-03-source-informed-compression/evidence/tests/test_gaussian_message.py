"""Tiny dense-reference checks for retained Gaussian messages."""
from __future__ import annotations

import importlib
from types import ModuleType

import torch

from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledModel, CoupledState


def _api() -> ModuleType:
    return importlib.import_module("multiagent_elbo.realizations.gaussian.gaussian_message")


def _example() -> tuple[CoupledModel, CoupledState, torch.Tensor]:
    dtype = torch.float64
    a = torch.arange(8, dtype=dtype).reshape(4, 2)/11.-.3
    metric = torch.tensor([[1.3, .2], [.2, .9]], dtype=dtype)
    J_0 = metric.expand(4, -1, -1).clone()
    H = torch.tensor([[.8, -.15], [-.15, 1.1]], dtype=dtype).expand(4, -1, -1).clone()
    model = CoupledModel(a, J_0, H, torch.tensor([[1, 2], [0, 3], [3, 0], [2, 1]]),
        torch.tensor([[0, 1], [0, 2], [1, 3], [2, 3]]),
        torch.tensor([[0, 1], [0, 2], [3, 1], [3, 2]]),
        torch.tensor([[False, False], [True, False], [False, True], [True, True]]), .7)
    Theta = torch.tensor([[[1.1, .2], [-.1, .9]], [[.9, -.2], [.1, 1.2]],
                          [[1.2, .1], [.2, .8]], [[.8, -.1], [.1, 1.1]]], dtype=dtype)
    mobility = torch.tensor([[.7, .1], [.1, 1.2]], dtype=dtype).expand(4, -1, -1).clone()
    state = CoupledState(a+.1, torch.linalg.inv(J_0),
                         torch.full((4, 2), .5, dtype=dtype), Theta)
    return model, state, mobility


def _moments() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    generator = torch.Generator().manual_seed(91)
    mu = torch.randn((2, 4, 2), dtype=torch.float64, generator=generator)
    matrix = torch.randn((2, 8, 8), dtype=mu.dtype, generator=generator)
    covariance = matrix @ matrix.mT/8+torch.eye(8, dtype=mu.dtype)
    P = torch.kron(torch.tensor([[.5, .5, 0., 0.], [0., 0., .5, .5]], dtype=mu.dtype),
                   torch.eye(2, dtype=mu.dtype))
    return mu, covariance, P


def test_propagation_matches_independent_quadratic_hessian_with_sender_terms() -> None:
    model, state, mobility = _example()
    mu, covariance, _ = _moments()
    old_mu, old_covariance = mu.clone(), covariance.clone()
    assignments = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0]])
    dt = .03
    expected_mean, expected_covariance = [], []
    M = torch.block_diag(*mobility)
    for batch in range(2):
        H = torch.block_diag(*model.J_0)
        for receiver in range(4):
            label = int(assignments[batch, receiver])
            source = int(model.sources[receiver, label])
            link = state.Theta[model.link_index[receiver, label]]
            if bool(model.reverse[receiver, label]):
                link = torch.linalg.inv(link)
            difference = torch.zeros((2, 8), dtype=mu.dtype)
            difference[:, 2*receiver:2*receiver+2] = torch.eye(2, dtype=mu.dtype)
            difference[:, 2*source:2*source+2] = -link
            H += difference.T @ model.H[receiver] @ difference/model.tau
        A = torch.eye(8, dtype=mu.dtype)-dt*M@H
        offset = dt*M@torch.block_diag(*model.J_0)@model.a.flatten()
        expected_mean.append(A@mu[batch].flatten()+offset)
        expected_covariance.append(A@covariance[batch]@A.T+2*dt*M)
    actual_mean, actual_covariance = _api().propagate_gaussian(
        mu, covariance, assignments, mobility, state, model, dt)
    torch.testing.assert_close(actual_mean.flatten(1), torch.stack(expected_mean), atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(actual_covariance, torch.stack(expected_covariance), atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(mu, old_mu, atol=0., rtol=0.)
    torch.testing.assert_close(covariance, old_covariance, atol=0., rtol=0.)


def test_observation_matches_full_gaussian_density_and_cross_covariance() -> None:
    mu, covariance, P = _moments()
    old_mu, old_covariance = mu.clone(), covariance.clone()
    retained = torch.tensor([[.2, -.1, .4, .7], [-.5, .3, .1, -.2]], dtype=mu.dtype)
    projected_mean = mu.flatten(1)@P.T
    projected_covariance = P@covariance@P.T
    cross = covariance@P.T
    gain = torch.linalg.solve(projected_covariance, cross.mT).mT
    expected_mean = mu.flatten(1)+(gain@(retained-projected_mean).unsqueeze(-1)).squeeze(-1)
    expected_covariance = covariance-gain@cross.mT
    law = torch.distributions.MultivariateNormal(projected_mean, projected_covariance)
    result = _api().observe_gaussian(mu, covariance, retained, block_size=2)
    torch.testing.assert_close(result["log_density"], law.log_prob(retained), atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(result["projected_mean"], projected_mean, atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(result["projected_covariance"], projected_covariance, atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(result["mean"].flatten(1), expected_mean, atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(result["covariance"], expected_covariance, atol=2e-14, rtol=2e-14)
    assert result["covariance"][:, :4, 4:].abs().max() > .01
    torch.testing.assert_close(result["mean"].flatten(1)@P.T, retained, atol=2e-14, rtol=0.)
    torch.testing.assert_close(P@result["covariance"], torch.zeros((2, 4, 8), dtype=mu.dtype), atol=2e-14, rtol=0.)
    torch.testing.assert_close(mu, old_mu, atol=0., rtol=0.)
    torch.testing.assert_close(covariance, old_covariance, atol=0., rtol=0.)


def test_propagation_of_singular_fiber_message_restores_positive_forecast() -> None:
    model, state, mobility = _example()
    mu, covariance, P = _moments()
    retained = mu.flatten(1)@P.T+.1
    conditioned = _api().observe_gaussian(mu, covariance, retained, block_size=2)
    assignments = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0]])
    forecast_mu, forecast_covariance = _api().propagate_gaussian(
        conditioned["mean"], conditioned["covariance"], assignments, mobility, state, model, .03)
    torch.linalg.cholesky(forecast_covariance)
    result = _api().observe_gaussian(forecast_mu, forecast_covariance, retained, block_size=2)
    torch.testing.assert_close(result["mean"].flatten(1)@P.T, retained, atol=2e-14, rtol=0.)
    torch.testing.assert_close(P@result["covariance"], torch.zeros((2, 4, 8), dtype=mu.dtype), atol=2e-14, rtol=0.)


def test_full_retention_has_exact_zero_conditional_covariance() -> None:
    mu, covariance, _ = _moments()
    retained = mu.flatten(1)+.2
    result = _api().observe_gaussian(mu, covariance, retained, block_size=1)
    law = torch.distributions.MultivariateNormal(mu.flatten(1), covariance)
    torch.testing.assert_close(result["log_density"], law.log_prob(retained), atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(result["mean"].flatten(1), retained, atol=0., rtol=0.)
    torch.testing.assert_close(result["covariance"], torch.zeros_like(covariance), atol=0., rtol=0.)
