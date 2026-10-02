"""Tiny CPU grounding of predictive mode selection and reduced path budgets."""
from __future__ import annotations

from collections.abc import Iterator
import pytest
import torch

from multiagent_elbo.realizations.gaussian.network_dynamics import GaussianTransition


@pytest.fixture(scope="module", autouse=True)
def _single_thread() -> Iterator[None]:
    previous = torch.get_num_threads()
    torch.set_num_threads(1)
    yield
    torch.set_num_threads(previous)


def _example() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, list[GaussianTransition]]:
    mu = torch.tensor([0.7, -1.2, 0.3], dtype=torch.float64)
    Sigma = torch.tensor([[1.4, .2, -.1], [.2, .8, .15], [-.1, .15, 1.1]], dtype=torch.float64)
    P = torch.tensor([[1., 0., 0.]], dtype=torch.float64)
    kernels = []
    for t in range(4):
        F = torch.tensor([[.8, .22 - .05*t, -.07], [.11, .72, .18], [.04, -.16, .86]],
                         dtype=torch.float64)
        L = torch.tensor([[.45, 0, 0], [.18, .4, 0], [-.08, .13, .5]], dtype=torch.float64)
        kernels.append(GaussianTransition(F, torch.tensor([.07*(t+1), -.04, .03], dtype=torch.float64), L @ L.T))
    return mu, Sigma, P, kernels


def _full_path(
    mu: torch.Tensor,
    Sigma: torch.Tensor,
    kernels: list[GaussianTransition],
) -> tuple[torch.Tensor, torch.Tensor]:
    n = len(mu)
    for kernel in kernels:
        cross = kernel.F @ Sigma[-n:, :]
        next_covariance = kernel.F @ Sigma[-n:, -n:] @ kernel.F.T + kernel.Q
        Sigma = torch.cat((torch.cat((Sigma, cross.T), 1), torch.cat((cross, next_covariance), 1)), 0)
        mu = torch.cat((mu, kernel.F @ mu[-n:] + kernel.u))
    return mu, Sigma


def test_future_record_preserves_shared_noise_and_actual_activation() -> None:
    from multiagent_elbo.realizations.gaussian.predictive_interfaces import predictive_reference

    mu, Sigma, P, kernels = _example()
    ref = predictive_reference(mu, Sigma, P, kernels)
    path_mu, path_covariance = _full_path(mu, Sigma, kernels)
    retained = torch.tensor([0, 3, 6, 9, 12])
    torch.testing.assert_close(ref.path_mu, path_mu[retained], atol=1e-12, rtol=1e-12)
    torch.testing.assert_close(ref.path_Sigma, path_covariance[retained][:, retained], atol=1e-12, rtol=1e-12)
    future = retained[1:]
    cross = path_covariance[future, 0:3]
    expected_noise = path_covariance[future][:, future] - cross @ torch.linalg.solve(Sigma, cross.T)
    torch.testing.assert_close(ref.noise, expected_noise, atol=1e-12, rtol=1e-12)
    assert ref.noise[1, 0] != 0
    Sigma_h = Sigma[1:, 1:] - Sigma[1:, :1] @ torch.linalg.solve(Sigma[:1, :1], Sigma[:1, 1:])
    torch.testing.assert_close(ref.Sigma_h, Sigma_h, atol=1e-12, rtol=1e-12)


def test_information_tail_matches_independent_conditioning_and_controls() -> None:
    from multiagent_elbo.realizations.gaussian.predictive_interfaces import (
        discarded_information, predictive_reference, spectral_interface,
    )

    ref = predictive_reference(*_example())
    interface = spectral_interface(ref.Sigma_h, ref.C, ref.noise)
    assert bool((interface.nu[:-1] >= interface.nu[1:]).all())
    for rank in (0, 1, 2):
        W = interface.W[:rank]
        loss = discarded_information(ref.Sigma_h, ref.C, ref.noise, W)
        torch.testing.assert_close(loss, torch.log1p(interface.nu[rank:]).sum()/2, atol=1e-12, rtol=1e-12)
        coordinate = torch.eye(2, dtype=torch.float64)[:rank]
        assert loss <= discarded_information(ref.Sigma_h, ref.C, ref.noise, coordinate) + 1e-12


def test_spectral_information_and_projector_carry_noncompact_frames() -> None:
    from multiagent_elbo.realizations.gaussian.predictive_interfaces import predictive_reference, spectral_interface

    ref = predictive_reference(*_example())
    original = spectral_interface(ref.Sigma_h, ref.C, ref.noise)
    R = torch.tensor([[1.3, .2], [-.1, .8]], dtype=torch.float64)
    E = torch.diag(torch.tensor([.7, 1.4, .9, 1.1], dtype=torch.float64))
    changed = spectral_interface(R @ ref.Sigma_h @ R.T, E @ ref.C @ torch.linalg.inv(R),
                                 E @ ref.noise @ E.T)
    torch.testing.assert_close(changed.nu, original.nu, atol=1e-12, rtol=1e-12)
    projector = torch.linalg.solve(original.W, torch.diag(torch.tensor([1., 0.], dtype=torch.float64)) @ original.W)
    projector_changed = torch.linalg.solve(changed.W, torch.diag(torch.tensor([1., 0.], dtype=torch.float64)) @ changed.W)
    torch.testing.assert_close(projector_changed, R @ projector @ torch.linalg.inv(R), atol=1e-12, rtol=1e-12)


def test_reduced_predictor_path_budget_and_full_rank_recovery() -> None:
    from multiagent_elbo.realizations.gaussian.network_dynamics import memory_information
    from multiagent_elbo.realizations.gaussian.predictive_interfaces import (
        compile_predictor, path_budget, predictive_reference, spectral_interface,
    )

    mu, Sigma, P, kernels = _example()
    ref = predictive_reference(mu, Sigma, P, kernels)
    interface = spectral_interface(ref.Sigma_h, ref.C, ref.noise)
    for rank in (0, 1, 2):
        parent = compile_predictor(interface.W[:rank], ref)
        state = parent.initialize(torch.tensor([-.2], dtype=torch.float64))
        assert state.mu_h.numel() == rank
        assert state.Sigma_h.numel() == rank*rank
        assert parent.kernels[0].F.shape == (1+rank, 1+rank)
        budget = path_budget(ref.path_mu, ref.path_Sigma, parent)
        torch.testing.assert_close(budget.direct_kl, budget.memory.sum()+budget.row_risk.sum(),
                                   atol=2e-11, rtol=2e-11)
        assert bool((budget.memory >= -1e-11).all())
        assert bool((budget.row_risk >= -1e-11).all())
        if rank == 0:
            expected = memory_information(mu, Sigma, torch.tensor([0]), kernels).sum()
            torch.testing.assert_close(budget.direct_kl, expected, atol=2e-11, rtol=2e-11)
        if rank == 2:
            assert abs(float(budget.direct_kl)) < 1e-20
            assert abs(float(budget.memory.sum())) < 1e-11
            assert abs(float(budget.row_risk.sum())) < 1e-11


def test_deployed_small_filter_matches_its_complete_candidate_path() -> None:
    from multiagent_elbo.realizations.gaussian.predictive_interfaces import (
        compile_predictor, predictive_reference, spectral_interface,
    )

    ref = predictive_reference(*_example())
    W = spectral_interface(ref.Sigma_h, ref.C, ref.noise).W[:1]
    parent = compile_predictor(W, ref)
    mu, Sigma = _full_path(parent.mu_0, parent.Sigma_0, list(parent.kernels))
    observed = torch.tensor([-.2, .1, .4, -.3, .2], dtype=torch.float64)
    state = parent.initialize(observed[:1])
    for t, kernel in enumerate(parent.kernels):
        indices = torch.arange(t+1)*2
        target = (t+1)*2
        cross = Sigma[target, indices]
        G = torch.linalg.solve(Sigma[indices][:, indices], cross)
        expected_mu = mu[target] + G @ (observed[:t+1]-mu[indices])
        expected_variance = Sigma[target, target]-cross @ G
        forecast = state.predict(kernel, observed[t:t+1])
        torch.testing.assert_close(forecast.mu_r[0], expected_mu, atol=1e-12, rtol=1e-12)
        torch.testing.assert_close(forecast.Sigma_r[0, 0], expected_variance, atol=1e-12, rtol=1e-12)
        state = state.condition(forecast, observed[t+1:t+2])
