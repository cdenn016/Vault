"""Tiny expectation checks for the joint-channel compression heuristic."""
from __future__ import annotations

import importlib
from collections.abc import Iterator
from itertools import product
from math import expm1

import numpy as np
import pytest
import torch

from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledModel, CoupledState
from tests.test_source_informed_compression import _example, _log_beta, _sigma_point_oracle


@pytest.fixture(autouse=True)
def _single_thread() -> Iterator[None]:
    """Keep the six-dimensional CPU calculations in one Torch thread."""
    previous = torch.get_num_threads()
    torch.set_num_threads(1)
    yield
    torch.set_num_threads(previous)


def _sheet_energy(
    x:      torch.Tensor,
    labels: tuple[int, ...],
    state:  CoupledState,
    model:  CoupledModel,
) -> torch.Tensor:
    r"""Evaluate prior plus selected D_ij/tau, including source dependence."""
    nodes = x.reshape(3, 2)
    energy = x.new_zeros(())
    for receiver, label in enumerate(labels):
        displacement = nodes[receiver] - model.a[receiver]
        energy += .5 * displacement @ model.J_0[receiver] @ displacement
        source = int(model.sources[receiver, label])
        transform = state.Theta[int(model.link_index[receiver, label])]
        if bool(model.reverse[receiver, label]):
            transform = torch.linalg.inv(transform)
        residual = nodes[receiver] - transform @ nodes[source]
        energy += .5 * residual @ model.H[receiver] @ residual / model.tau
    return energy


def _enumerated_configuration(
    P:        torch.Tensor,
    mobility: torch.Tensor,
    beta:     torch.Tensor,
    dt:       float,
    state:    CoupledState,
    model:    CoupledModel,
) -> tuple[torch.Tensor, torch.Tensor]:
    r"""Enumerate all eight sheets and return E[A_J^T Q^-1 A_J] and E[A_J]."""
    M = torch.block_diag(*mobility)
    Q = 2 * dt * P @ M @ P.T
    G = M.new_zeros(M.shape)
    mean_A = P.new_zeros(P.shape)
    for labels in product(range(2), repeat=3):
        probability = beta[torch.arange(3), list(labels)].prod()
        H = torch.autograd.functional.hessian(
            lambda x: _sheet_energy(x, labels, state, model), state.mu.flatten())
        A = P @ (torch.eye(6, dtype=P.dtype) - dt * M @ H)
        G += probability * A.T @ torch.linalg.solve(Q, A)
        mean_A += probability * A
    return G, mean_A


def _geometry() -> tuple[torch.Tensor, torch.Tensor]:
    """Use anisotropic mobility and retained coordinates spanning all nodes."""
    mobility = torch.tensor([[[1., .12], [.12, .8]], [[.7, -.08], [-.08, 1.2]],
                             [[1.1, .15], [.15, .9]]], dtype=torch.float64)
    P = mobility.new_tensor([[.5, 0, .3, 0, .2, 0], [0, .25, 0, .5, 0, .25]])
    return P, mobility


@pytest.mark.parametrize("point_mass", [False, True])
def test_configuration_sensitivity_matches_exact_assignment_enumeration(point_mass: bool) -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.joint_informed_compression")
    model, state = _example()
    P, mobility = _geometry()
    dt = .09
    beta = P.new_tensor([[.1, .9], [.85, .15], [.2, .8]])
    if point_mass:
        beta = P.new_tensor([[0, 1.], [1., 0], [0, 1.]])
    expected, mean_A = _enumerated_configuration(P, mobility, beta, dt, state, model)
    actual = api.configuration_sensitivity(P, mobility, beta, dt, state, model)
    torch.testing.assert_close(actual, expected, atol=3e-13, rtol=3e-13)
    Q = 2 * dt * P @ torch.block_diag(*mobility) @ P.T
    variance = expected - mean_A.T @ torch.linalg.solve(Q, mean_A)
    if point_mass:
        torch.testing.assert_close(variance, torch.zeros_like(variance), atol=2e-14, rtol=0.)
    else:
        assert float(torch.linalg.matrix_norm(variance)) > 1e-3
        assert float(torch.linalg.eigvalsh(variance).min()) > -2e-14


@pytest.mark.parametrize("refresh_rate,rank", [(0., 2), (1.7, 2), (1.7, 4)])
def test_joint_basis_matches_global_mixture_and_independent_channel_oracles(
    refresh_rate: float,
    rank:         int,
) -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.joint_informed_compression")
    model, state = _example()
    P, mobility = _geometry()
    mu = state.mu.flatten()
    A = mu.new_tensor([[1., .1, 0, .2, 0, 0], [0, 1.2, .2, 0, .1, 0],
                       [.2, 0, .8, .1, 0, .1], [0, .1, 0, 1.1, .2, 0],
                       [.1, 0, .1, 0, .9, .1], [0, .2, 0, .1, 0, 1.3]])
    Sigma = A @ A.T + .2 * torch.eye(6, dtype=mu.dtype)
    held_beta = mu.new_tensor([[.1, .9], [.85, .15], [.2, .8]])
    refresh_beta = _log_beta(mu, state, model).exp()
    dt = .09
    probability = -expm1(-refresh_rate * dt)
    held, _ = _enumerated_configuration(P, mobility, held_beta, dt, state, model)
    refreshed, _ = _enumerated_configuration(P, mobility, refresh_beta, dt, state, model)
    configuration = (1 - probability) * held + probability * refreshed
    L = np.linalg.cholesky(Sigma.numpy())
    U = np.linalg.svd(P.numpy() @ L, full_matrices=True)[2][len(P):].T
    B = L @ U
    # This is the frozen-weight gradient proxy, not an exact joint Fisher matrix.
    source = _sigma_point_oracle(mu, torch.from_numpy(B), state, model)
    source_gram = probability * B.T @ source.numpy() @ B
    configuration_gram = B.T @ configuration.numpy() @ B
    gram = source_gram + configuration_gram
    expected_values = np.linalg.eigvalsh(gram)[::-1].copy()
    W, values, diagnostics = api.joint_informed_basis(
        mu, Sigma, P, mobility, held_beta, dt, refresh_rate, rank, state, model)
    np.testing.assert_allclose(values.numpy(), expected_values, atol=2e-12, rtol=2e-12)
    assert W.shape == (rank, 6)
    V = U.T @ L.T @ W.numpy().T
    np.testing.assert_allclose(gram @ V, V * expected_values[:rank], atol=2e-12, rtol=2e-12)
    np.testing.assert_allclose(W.numpy() @ (B @ B.T) @ W.numpy().T, np.eye(rank), atol=3e-14)
    np.testing.assert_allclose(W.numpy() @ Sigma.numpy() @ P.numpy().T, np.zeros((rank, 2)), atol=3e-14)
    assert diagnostics["refresh_probability"] == pytest.approx(probability, abs=2e-15)
    assert diagnostics["source_hidden_trace"] == pytest.approx(float(np.trace(source_gram)), abs=2e-12)
    assert diagnostics["configuration_hidden_trace"] == pytest.approx(float(np.trace(configuration_gram)), abs=2e-12)
    if refresh_rate:
        mixed_beta = (1 - probability) * held_beta + probability * refresh_beta
        independent_marginals, _ = _enumerated_configuration(P, mobility, mixed_beta, dt, state, model)
        # A global coin produces a mixture of product laws, not mixed independent rows.
        assert float(torch.linalg.matrix_norm(configuration - independent_marginals)) > 1e-4
    else:
        assert diagnostics["source_hidden_trace"] == 0.
