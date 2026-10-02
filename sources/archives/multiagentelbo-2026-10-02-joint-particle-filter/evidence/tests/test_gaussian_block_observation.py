"""Tiny dense-Gaussian checks for arithmetic block observations."""
from __future__ import annotations

from collections.abc import Iterator
import importlib
from types import ModuleType

import pytest
import torch


@pytest.fixture(autouse=True)
def _threads() -> Iterator[None]:
    previous = torch.get_num_threads()
    torch.set_num_threads(1)
    yield
    torch.set_num_threads(previous)


def _api() -> ModuleType:
    return importlib.import_module("multiagent_elbo.realizations.gaussian.block_observation")


def _example() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    covariance = torch.tensor([
        [[1.2, .3], [.3, .8]], [[.7, -.2], [-.2, 1.5]],
        [[1.8, .4], [.4, .9]], [[.6, -.15], [-.15, 1.1]],
    ], dtype=torch.float64)
    P = torch.kron(torch.tensor([[.5, .5, 0., 0.], [0., 0., .5, .5]], dtype=torch.float64),
                   torch.eye(2, dtype=torch.float64))
    dense_covariance = torch.block_diag(*covariance.unbind())
    return covariance, P, dense_covariance


def test_conditional_mean_matches_dense_formula_with_particle_broadcast() -> None:
    covariance, P, dense_covariance = _example()
    observation = _api().BlockObservation.compile(covariance, block_size=2)
    mean = torch.arange(48, dtype=torch.float64).reshape(2, 3, 4, 2)/13.
    R = torch.tensor([[[[.2, -.3], [.8, .1]]], [[[.4, .9], [-.5, .3]]]], dtype=mean.dtype)
    dense_gain = torch.linalg.solve(P @ dense_covariance @ P.T, P @ dense_covariance).T
    expected = mean.flatten(-2)+(R.flatten(-2)-mean.flatten(-2) @ P.T) @ dense_gain.T
    actual = observation.conditional_mean(mean, R)
    torch.testing.assert_close(actual.flatten(-2), expected, atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(observation.project(mean).flatten(-2), mean.flatten(-2) @ P.T)
    torch.testing.assert_close(observation.project(actual), R.expand(2, 3, 2, 2), atol=2e-14, rtol=2e-14)


def test_supplied_basis_noise_has_exact_dense_conditional_covariance() -> None:
    covariance, P, dense_covariance = _example()
    observation = _api().BlockObservation.compile(covariance, block_size=2)
    standard_normal = torch.eye(8, dtype=covariance.dtype).reshape(8, 4, 2)
    mean = torch.zeros_like(standard_normal)
    R = torch.zeros((8, 2, 2), dtype=covariance.dtype)
    noise_rows = observation.sample_conditional(mean, R, standard_normal).flatten(-2)
    dense_gain = torch.linalg.solve(P @ dense_covariance @ P.T, P @ dense_covariance).T
    expected = dense_covariance-dense_gain @ P @ dense_covariance
    torch.testing.assert_close(noise_rows.T @ noise_rows, expected, atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(noise_rows @ P.T, torch.zeros((8, 4), dtype=covariance.dtype),
                               atol=2e-14, rtol=0.)


def test_projected_log_prob_matches_normalized_dense_gaussian() -> None:
    covariance, P, dense_covariance = _example()
    observation = _api().BlockObservation.compile(covariance, block_size=2)
    mean = torch.arange(48, dtype=torch.float64).reshape(2, 3, 4, 2)/17.
    R = torch.tensor([[[[.2, -.3], [.8, .1]]], [[[.4, .9], [-.5, .3]]]], dtype=mean.dtype)
    law = torch.distributions.MultivariateNormal(mean.flatten(-2) @ P.T,
                                                 covariance_matrix=P @ dense_covariance @ P.T)
    torch.testing.assert_close(observation.log_prob(R, mean), law.log_prob(R.flatten(-2)),
                               atol=2e-14, rtol=2e-14)


def test_identity_retention_has_zero_hidden_noise() -> None:
    covariance, _, _ = _example()
    observation = _api().BlockObservation.compile(covariance, block_size=1)
    mean = torch.arange(24, dtype=covariance.dtype).reshape(3, 4, 2)/7.
    R = torch.arange(8, dtype=covariance.dtype).reshape(1, 4, 2)/5.
    standard_normal = torch.arange(24, dtype=covariance.dtype).reshape(3, 4, 2)/3.-2.
    torch.testing.assert_close(observation.project(mean), mean, atol=0., rtol=0.)
    torch.testing.assert_close(observation.conditional_mean(mean, R), R.expand_as(mean), atol=0., rtol=0.)
    torch.testing.assert_close(observation.sample_conditional(mean, R, standard_normal),
                               R.expand_as(mean), atol=0., rtol=0.)
