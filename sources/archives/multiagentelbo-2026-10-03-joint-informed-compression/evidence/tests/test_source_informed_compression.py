"""Tiny independent checks for the frozen-weight source-sensitivity heuristic."""
from __future__ import annotations

import importlib
from collections.abc import Iterator

import numpy as np
import pytest
import torch

from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledModel, CoupledState


@pytest.fixture(autouse=True)
def _single_thread() -> Iterator[None]:
    """Keep the six-dimensional CPU calculations in one Torch thread."""
    previous = torch.get_num_threads()
    torch.set_num_threads(1)
    yield
    torch.set_num_threads(previous)


def _example() -> tuple[CoupledModel, CoupledState]:
    """Use three noncommuting GL links with both edge orientations."""
    mu = torch.tensor([[.2, -.3], [.6, .1], [-.4, .5]], dtype=torch.float64)
    H = mu.new_tensor([[[1.4, .2], [.2, .8]], [[.9, -.15], [-.15, 1.3]], [[1.1, .1], [.1, .7]]])
    Sigma = mu.new_tensor([[[.8, .1], [.1, 1.2]], [[1.1, -.1], [-.1, .9]], [[.7, .15], [.15, 1.4]]])
    Theta = mu.new_tensor([[[1.1, .35], [-.15, .9]], [[.8, -.25], [.4, 1.2]], [[1.3, .1], [.3, .85]]])
    model = CoupledModel(
        torch.zeros_like(mu), torch.eye(2, dtype=mu.dtype).expand(3, 2, 2).clone(), H,
        torch.tensor([[1, 2], [0, 2], [0, 1]]),
        torch.tensor([[0, 1], [0, 2], [1, 2]]),
        torch.tensor([[0, 1], [0, 2], [1, 2]]),
        torch.tensor([[False, False], [True, False], [True, True]]), .7,
    )
    state = CoupledState(mu, Sigma, mu.new_tensor([[.7, .3], [.35, .65], [.55, .45]]), Theta)
    return model, state


def _log_beta(
    x:     torch.Tensor,
    state: CoupledState,
    model: CoupledModel,
) -> torch.Tensor:
    r"""Independently evaluate log beta from the oriented quadratic records."""
    nodes = x.reshape(3, 2)
    logits = []
    for receiver in range(3):
        row = []
        for label in range(2):
            edge = int(model.link_index[receiver, label])
            transform = state.Theta[edge]
            if bool(model.reverse[receiver, label]):
                transform = torch.linalg.inv(transform)
            source = int(model.sources[receiver, label])
            residual = nodes[receiver] - transform @ nodes[source]
            cost = .5 * residual @ model.H[receiver] @ residual
            row.append(state.pi[receiver, label].log() - cost / model.tau)
        logits.append(torch.stack(row))
    return torch.log_softmax(torch.stack(logits), dim=-1)


def _sigma_point_oracle(
    mu:    torch.Tensor,
    root:  torch.Tensor,
    state: CoupledState,
    model: CoupledModel,
) -> torch.Tensor:
    r"""Integrate affine log-odds gradients exactly under covariance root root^T."""
    columns = root.shape[1]
    offsets = columns**.5 * root.T
    points = torch.cat((mu + offsets, mu - offsets))
    beta = _log_beta(mu, state, model).exp()
    weights = beta[:, 0] * beta[:, 1]
    result = mu.new_zeros((len(mu), len(mu)))
    for x in points:
        def odds(value: torch.Tensor) -> torch.Tensor:
            logs = _log_beta(value, state, model)
            return logs[:, 0] - logs[:, 1]
        gradients = torch.autograd.functional.jacobian(odds, x)
        result += torch.einsum("n,ni,nj->ij", weights, gradients, gradients) / len(points)
    return result


@pytest.mark.parametrize("zero_mean", [False, True])
def test_source_sensitivity_matches_autograd_second_moment(zero_mean: bool) -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_informed_compression")
    model, state = _example()
    mu = torch.zeros(6, dtype=state.mu.dtype) if zero_mean else state.mu.flatten() + .17
    # This rank-four covariance exercises the allowed positive-semidefinite input.
    root = mu.new_tensor([[.6, .1, 0, .1], [.1, .8, -.1, 0], [0, .2, .7, .1],
                          [.2, 0, .1, .9], [.3, .1, -.2, .1], [.1, -.2, .1, .4]])
    expected = _sigma_point_oracle(mu, root, state, model)
    actual = api.source_sensitivity(mu, root @ root.T, state, model)
    torch.testing.assert_close(actual, expected, atol=2e-13, rtol=2e-13)
    torch.testing.assert_close(actual, actual.T, atol=2e-13, rtol=0.)
    if zero_mean:
        # Gradients at the mean vanish, but their quadratic sensitivity does not.
        assert float(expected.trace()) > .1


@pytest.mark.parametrize("rank", [0, 2, 4])
def test_basis_whitens_hidden_coordinates_and_solves_independent_pencil(rank: int) -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_informed_compression")
    model, state = _example()
    mu = state.mu.flatten()
    A = mu.new_tensor([[1., .1, 0, .2, 0, 0], [0, 1.2, .2, 0, .1, 0],
                       [.2, 0, .8, .1, 0, .1], [0, .1, 0, 1.1, .2, 0],
                       [.1, 0, .1, 0, .9, .1], [0, .2, 0, .1, 0, 1.3]])
    Sigma = A @ A.T + .2 * torch.eye(6, dtype=mu.dtype)
    P = mu.new_tensor([[.5, 0, .5, 0, 0, 0], [0, .5, 0, .5, 0, 0]])
    # Independent NumPy SVD constructs the conditioned hidden covariance.
    L = np.linalg.cholesky(Sigma.numpy())
    U = np.linalg.svd(P.numpy() @ L, full_matrices=True)[2][len(P):].T
    B = L @ U
    covariance = Sigma.numpy() - Sigma.numpy() @ P.numpy().T @ np.linalg.solve(
        P.numpy() @ Sigma.numpy() @ P.numpy().T, P.numpy() @ Sigma.numpy())
    np.testing.assert_allclose(B @ B.T, covariance, atol=2e-15)
    G = _sigma_point_oracle(mu, torch.from_numpy(B), state, model).numpy()
    gram = B.T @ G @ B
    expected_values = np.linalg.eigvalsh(gram)[::-1].copy()
    W, values = api.source_informed_basis(mu, Sigma, P, rank, state, model)
    assert W.shape == (rank, 6)
    assert values.shape == (4,)
    np.testing.assert_allclose(values.numpy(), expected_values, rtol=2e-12, atol=2e-12)
    np.testing.assert_allclose(W.numpy() @ covariance @ W.numpy().T, np.eye(rank), atol=3e-14)
    np.testing.assert_allclose(W.numpy() @ Sigma.numpy() @ P.numpy().T, np.zeros((rank, 2)), atol=3e-14)
    # Recover coordinates in the independently chosen hidden frame; sign is free.
    V = U.T @ L.T @ W.numpy().T
    np.testing.assert_allclose(gram @ V, V * expected_values[:rank], rtol=2e-12, atol=2e-12)
    if rank == 4:
        np.testing.assert_allclose(V @ V.T, np.eye(4), atol=3e-14)
