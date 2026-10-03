"""Tiny source-conditioning checks against dense Gaussian calculations."""
from __future__ import annotations

from dataclasses import replace
import importlib
import itertools
import math

import pytest
import torch

from multiagent_elbo.realizations.gaussian.coupled_learning import (
    CoupledModel, CoupledState, comparison_maps,
)
from multiagent_elbo.realizations.gaussian.switching_paths import source_log_posterior


def _example(
    n_agents: int = 6,
    dimension: int = 2,
    block_size: int = 2,
) -> tuple[torch.Tensor, torch.Tensor, CoupledModel, CoupledState]:
    generator = torch.Generator().manual_seed(491)
    dtype = torch.float64
    sources = torch.tensor([[(i+1) % n_agents, (i+3) % n_agents]
                            for i in range(n_agents)])
    if n_agents == 3:
        sources = torch.tensor([[1, 2], [0, 2], [0, 1]])
    pairs = sorted({tuple(sorted((i, int(j)))) for i in range(n_agents)
                    for j in sources[i]})
    index = torch.tensor([[pairs.index(tuple(sorted((i, int(j)))))
                           for j in sources[i]] for i in range(n_agents)])
    reverse = torch.tensor([[i > int(j) for j in sources[i]]
                            for i in range(n_agents)])
    eye = torch.eye(dimension, dtype=dtype)
    H = eye.expand(n_agents, -1, -1).clone()
    H[:, 0, 0] = torch.linspace(.8, 1.3, n_agents)
    a = .15*torch.randn(n_agents, dimension, generator=generator, dtype=dtype)
    model = CoupledModel(a, H, H, sources, torch.tensor(pairs), index, reverse, .9)
    Theta = eye.expand(len(pairs), -1, -1).clone()
    Theta += .05*torch.randn(Theta.shape, generator=generator, dtype=dtype)
    pi = torch.softmax(torch.randn(n_agents, 2, generator=generator, dtype=dtype), -1)
    state = CoupledState(a, eye.expand(n_agents, -1, -1), pi, Theta)
    mu = a.unsqueeze(0)+.2*torch.randn(2, n_agents, dimension, generator=generator, dtype=dtype)
    n_blocks = n_agents//block_size
    hidden = n_blocks*(block_size-1)*dimension
    Z = torch.zeros(n_agents*dimension, hidden, dtype=dtype)
    for block in range(n_blocks):
        for node in range(block_size-1):
            for coord in range(dimension):
                col = (block*(block_size-1)+node)*dimension+coord
                Z[(block*block_size+node)*dimension+coord, col] = 1.
                Z[((block+1)*block_size-1)*dimension+coord, col] = -1.
    A = .1*torch.randn(2, hidden, hidden, generator=generator, dtype=dtype)
    covariance = Z@(A@A.mT+torch.eye(hidden, dtype=dtype))@Z.T
    return mu, covariance, model, state


def _projection(n_agents: int, dimension: int, block_size: int) -> torch.Tensor:
    return torch.kron(torch.eye(n_agents//block_size, dtype=torch.float64),
                      torch.ones(1, block_size, dtype=torch.float64)/block_size).kron(
                          torch.eye(dimension, dtype=torch.float64))


@pytest.mark.parametrize("block_size", [2, 3])
def test_local_cubature_matches_dense_regression_and_preserves_fiber(block_size: int) -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_gaussian")
    mu, covariance, model, state = _example(block_size=block_size)
    before_mu, before_covariance = mu.clone(), covariance.clone()
    labels = torch.tensor([0, 1])
    logs, updated_mu, updated_covariance = api.gaussian_source_step(
        mu, covariance, labels, state, model, 0, block_size)
    # The complete star is nodes 0,1,3. Only block_size=2 contains a full block.
    independent_nodes = [0, 3] if block_size == 2 else [0, 1, 3]
    coordinates = torch.tensor([2*node+k for node in independent_nodes for k in range(2)])
    C = covariance[:, coordinates][:, :, coordinates]
    L = torch.linalg.cholesky(C)
    r = len(coordinates)
    offsets = math.sqrt(r)*torch.cat((L.mT, -L.mT), dim=1)
    cross = covariance[:, :, coordinates]
    gain = torch.linalg.solve(C, cross.mT).mT
    # Gaussian conditional means at each local cubature node suffice for every
    # native logit; unrelated coordinates do not enter receiver zero's energy.
    points = mu.flatten(1)[:, None]+offsets@gain.mT
    point_logs = source_log_posterior(points.flatten(0, 1).reshape(-1, 6, 2), state, model)
    point_logs = point_logs[:, 0].reshape(2, 2*r, 2)
    expected_logs = torch.logsumexp(point_logs, dim=1)-math.log(2*r)
    weights = torch.softmax(point_logs.gather(-1, labels[:, None, None].expand(-1, 2*r, 1)).squeeze(-1), -1)
    point_mean = (weights[..., None]*points).sum(1)
    centered = points-point_mean[:, None]
    residual = covariance-gain@C@gain.mT
    expected_covariance = residual+torch.einsum("bq,bqi,bqj->bij", weights, centered, centered)
    torch.testing.assert_close(logs, expected_logs)
    torch.testing.assert_close(updated_mu.flatten(1), point_mean)
    torch.testing.assert_close(updated_covariance, expected_covariance)
    P = _projection(6, 2, block_size)
    torch.testing.assert_close(updated_mu.flatten(1)@P.T, mu.flatten(1)@P.T)
    torch.testing.assert_close(P@updated_covariance, torch.zeros_like(P@updated_covariance), atol=2e-13, rtol=0.)
    torch.testing.assert_close(mu, before_mu)
    torch.testing.assert_close(covariance, before_covariance)
    assert torch.linalg.eigvalsh(updated_covariance).min() > -2e-13


def test_constant_source_likelihood_leaves_full_gaussian_unchanged() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_gaussian")
    mu, covariance, model, state = _example()
    model = replace(model, sources=model.sources[:, :1].expand(-1, 2),
                    link_index=model.link_index[:, :1].expand(-1, 2),
                    reverse=model.reverse[:, :1].expand(-1, 2))
    logs, mean, cov = api.gaussian_source_step(mu, covariance, torch.tensor([0, 1]), state, model, 0, 2)
    torch.testing.assert_close(logs, state.pi[0].log().expand(2, -1))
    torch.testing.assert_close(mean, mu)
    torch.testing.assert_close(cov, covariance)


def test_full_retention_has_constant_row_and_zero_hidden_update() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_gaussian")
    mu, covariance, model, state = _example(block_size=1)
    logs, mean, cov = api.gaussian_source_step(mu, covariance, torch.tensor([0, 1]), state, model, 0, 1)
    torch.testing.assert_close(logs, source_log_posterior(mu, state, model)[:, 0])
    torch.testing.assert_close(mean, mu)
    torch.testing.assert_close(cov, covariance)


def test_enumerated_refresh_laws_normalize_and_cutoff_obeys_prefix_bound() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_gaussian")
    mu, covariance, model, state = _example(n_agents=3, dimension=1, block_size=3)
    state = replace(state, pi=torch.tensor([[.01,.99],[.5,.5],[.5,.5]], dtype=mu.dtype))
    labels = torch.tensor(list(itertools.product(range(2), repeat=3)))
    old = torch.zeros_like(labels)
    means = mu[:1].expand(8, -1, -1).clone()
    covariances = covariance[:1].expand(8, -1, -1).clone()
    complete = api.sequential_source_message(means, covariances, old, labels, state, model, 3)
    cutoff = .1
    cut = api.sequential_source_message(means, covariances, old, labels, state, model, 3, cutoff)
    p, q = complete["log_refresh"].exp(), cut["log_refresh"].exp()
    torch.testing.assert_close(p.sum(), p.new_tensor(1.))
    torch.testing.assert_close(q.sum(), q.new_tensor(1.))
    assert bool((p > 0).all() and (q > 0).all())
    assert .5*(p-q).abs().sum() <= cutoff
    assert bool(cut["shortcut"].any())
    assert bool((cut["updates"][cut["shortcut"]] < 3).any())
    assert bool((complete["updates"] == 3).all())
    assert not bool(complete["shortcut"].any())
    # Paths leaving the old prefix at their first label never take its shortcut.
    diverged = labels[:, 0] != old[:, 0]
    torch.testing.assert_close(p[diverged], q[diverged])
    assert not bool(cut["shortcut"][diverged].any())
    P = _projection(3, 1, 3)
    torch.testing.assert_close(cut["mean"].flatten(1)@P.T, means.flatten(1)@P.T)
    torch.testing.assert_close(P@cut["covariance"], torch.zeros_like(P@cut["covariance"]), atol=2e-13, rtol=0.)
