"""Tiny CPU checks of source-prior locality and block-parent omitted-history information."""
from __future__ import annotations

from collections.abc import Iterator

import pytest
import torch

from multiagent_elbo.realizations.gaussian.locality import (
    block_basis,
    block_mean_projector,
    block_toeplitz,
    competitor_row_risk,
    gaussian_kl,
    gaussian_kl_stable,
    held_prior_action,
    independent_links,
    innovation_logdets,
    lyapunov_stationary,
    markov_path_covariance,
    omitted_history_information,
    omitted_history_information_direct,
    ParentMemory,
    retained_autocovariances,
    row_only_drift,
    schur_ou_competitor,
    source_prior,
)
from multiagent_elbo.realizations.gaussian.network import assemble_network
from multiagent_elbo.realizations.gaussian.network_dynamics import memory_information, ou_transition


@pytest.fixture(scope="module", autouse=True)
def _single_cpu_thread() -> Iterator[None]:
    previous = torch.get_num_threads()
    torch.set_num_threads(1)
    yield
    torch.set_num_threads(previous)


def _instance(family: str = "window", sigma: float = 0.3, N: int = 6, K: int = 2) -> tuple[torch.Tensor, torch.Tensor]:
    kwargs = {"window": {"radius": 1}, "directed_window": {"radius": 2}, "exponential": {"decay": 0.7},
              "power": {"alpha": 1.5}, "complete": {}}[family]
    return source_prior(N, family, **kwargs), independent_links(N, K, sigma, seed=3)


def _stationary(J: torch.Tensor, dt: float) -> tuple[torch.Tensor, torch.Tensor]:
    F = ou_transition(J, torch.zeros(len(J), dtype=J.dtype), torch.eye(len(J), dtype=J.dtype), dt).F
    return F, torch.cholesky_inverse(torch.linalg.cholesky(J))


def test_prior_families_are_row_stochastic_and_directed_support_is_one_way() -> None:
    for family in ("window", "directed_window", "exponential", "power", "complete"):
        pi, _ = _instance(family, N=7)
        assert torch.allclose(pi.sum(1), torch.ones(7, dtype=torch.float64))
        assert bool((pi.diagonal() == 0).all()) and bool((pi >= 0).all())
    pi, _ = _instance("directed_window", N=7)
    assert bool(((pi > 0) & (pi.T > 0)).sum() == 0)
    assert int((pi[0] > 0).sum()) == 2 and pi[0, 6] > 0 and pi[0, 5] > 0


def test_held_action_matches_existing_record_assembly() -> None:
    a, kappa = 0.4, 1.3
    pi, Omega = _instance("directed_window", N=5)
    edges = pi.nonzero()
    E, K = len(edges), Omega.shape[-1]
    oracle = assemble_network(
        a * torch.eye(K, dtype=torch.float64).expand(5, K, K).clone(),
        torch.zeros((5, K), dtype=torch.float64),
        torch.eye(K, dtype=torch.float64).expand(E, K, K).clone(),
        Omega[edges[:, 0], edges[:, 1]],
        kappa * pi[edges[:, 0], edges[:, 1]][:, None, None] * torch.eye(K, dtype=torch.float64),
        torch.zeros((E, K), dtype=torch.float64),
        edges,
    )
    assert torch.allclose(held_prior_action(pi, Omega, a, kappa).J, oracle.J, atol=1e-13)


def test_row_only_drift_is_the_receiver_gradient_and_lyapunov_solves() -> None:
    a, kappa, N, K = 0.5, 1.0, 5, 2
    pi, Omega = _instance("directed_window", N=N)
    x = torch.randn(N * K, dtype=torch.float64, generator=torch.Generator().manual_seed(1))
    X = x.reshape(N, K)
    expected = a * X + kappa * torch.einsum("ij,ijk->ik", pi, X[:, None, :] - torch.einsum("ijkl,jl->ijk", Omega, X))
    K_drift = row_only_drift(pi, Omega, a, kappa)
    assert torch.allclose(K_drift @ x, expected.reshape(-1), atol=1e-13)
    Sigma = lyapunov_stationary(K_drift)
    residual = K_drift @ Sigma + Sigma @ K_drift.T - 2 * torch.eye(N * K, dtype=torch.float64)
    assert float(residual.abs().max()) < 1e-11


def test_omitted_history_matches_brute_force_conditioning_and_decreases() -> None:
    pi, Omega = _instance("power", N=6)
    F, Sigma = _stationary(held_prior_action(pi, Omega, 0.3, 1.0).J, 0.4)
    P, H, m = block_mean_projector(6, 2, 2), 6, 6
    # Independent path covariance directly from fine powers, not the lag helper.
    fine = [torch.linalg.matrix_power(F, s) @ Sigma for s in range(H)]
    path = torch.zeros((H * m, H * m), dtype=torch.float64)
    for t in range(H):
        for u in range(t + 1):
            path[t * m:(t + 1) * m, u * m:(u + 1) * m] = P @ fine[t - u] @ P.T
            path[u * m:(u + 1) * m, t * m:(t + 1) * m] = (P @ fine[t - u] @ P.T).T

    def cond_logdet(t: int, first: int) -> torch.Tensor:
        target, context = slice(t * m, (t + 1) * m), slice(first * m, t * m)
        S = path[target, target]
        if t > first:
            S = S - path[target, context] @ torch.linalg.solve(path[context, context], path[context, target])
        return torch.linalg.slogdet(S)[1]

    logdets = innovation_logdets(block_toeplitz(retained_autocovariances(F, Sigma, P, H)), m)
    D = [omitted_history_information(logdets, k, H) for k in range(4)]
    for k in range(4):
        brute = sum((cond_logdet(t, t - k) - cond_logdet(t, 0)) / 2 for t in range(k + 1, H))
        assert torch.isclose(D[k], brute, rtol=1e-10, atol=1e-13)
        assert torch.isclose(omitted_history_information_direct(path, m, k, H), brute, rtol=1e-10, atol=1e-13)
    assert all(D[k + 1] <= D[k] + 1e-13 for k in range(3)) and D[0] > D[1] > 0


def test_path_kl_equals_memory_plus_competitor_row_risk() -> None:
    pi, Omega = _instance("window", N=6)
    dt, H = 0.5, 6
    F, Sigma = _stationary(held_prior_action(pi, Omega, 0.2, 1.0).J, dt)
    P = block_mean_projector(6, 2, 3)
    C = retained_autocovariances(F, Sigma, P, H)
    path, m = block_toeplitz(C), len(P)
    competitor = schur_ou_competitor(C[0], P, dt)
    markov = markov_path_covariance(C[0], competitor.F, H)
    kl = gaussian_kl_stable(path, markov)
    assert torch.isclose(kl, gaussian_kl(path, markov), rtol=1e-10)
    logdets = innovation_logdets(path, m)
    for k in range(1, 4):
        total = omitted_history_information(logdets, k, H) + competitor_row_risk(path, m, k, H, competitor)
        assert abs(float(total - kl)) <= 1e-9 * float(kl)


def test_block_parent_memory_agrees_with_existing_hidden_filter() -> None:
    pi, Omega = _instance("exponential", N=6)
    dt, H = 0.5, 5
    J = held_prior_action(pi, Omega, 0.2, 1.0).J
    F, Sigma = _stationary(J, dt)
    T, retained = block_basis(6, 2, 3)
    T_inv = torch.linalg.inv(T)
    J_new = T_inv.T @ J @ T_inv
    J_new = (J_new + J_new.T) / 2
    kernel = ou_transition(J_new, torch.zeros(12, dtype=torch.float64), T @ T.T, dt)
    Sigma_new = T @ Sigma @ T.T
    steps = memory_information(torch.zeros(12, dtype=torch.float64), (Sigma_new + Sigma_new.T) / 2, retained, [kernel] * (H - 1))
    P = block_mean_projector(6, 2, 3)
    logdets = innovation_logdets(block_toeplitz(retained_autocovariances(F, Sigma, P, H)), len(P))
    assert torch.isclose(steps.sum(), omitted_history_information(logdets, 1, H), rtol=1e-10, atol=1e-13)


def test_complete_support_with_identity_links_is_exactly_lumpable() -> None:
    pi, Omega = _instance("complete", sigma=0.0, N=6, K=1)
    F, Sigma = _stationary(held_prior_action(pi, Omega, 0.1, 1.0).J, 0.5)
    P = block_mean_projector(6, 1, 2)
    logdets = innovation_logdets(block_toeplitz(retained_autocovariances(F, Sigma, P, 5)), len(P))
    assert abs(float(omitted_history_information(logdets, 1, 5))) < 1e-10


@pytest.mark.parametrize("dimension", [3, 4])
def test_lyapunov_stationary_handles_stable_jordan_drift(dimension: int) -> None:
    shift = torch.diag(torch.ones(dimension - 1, dtype=torch.float64), diagonal=1)
    identity = torch.eye(dimension, dtype=torch.float64)
    K = identity - shift
    # Exact finite nilpotent series: Sigma=sum A^j(I), A(B)=(NB+BN^T)/2.
    expected, term = identity.clone(), identity.clone()
    for _ in range(2 * dimension - 2):
        term = (shift @ term + term @ shift.T) / 2
        expected = expected + term
    Sigma = lyapunov_stationary(K)
    assert torch.allclose(Sigma, expected, rtol=1e-12, atol=1e-13)
    torch.linalg.cholesky(Sigma)


def test_lyapunov_stationary_handles_directed_shear_ring() -> None:
    pi = source_prior(3, "directed_window", radius=1)
    Omega = independent_links(3, 2, 0.0, seed=0)
    Omega[0, 2, 0, 1] = 0.5
    K = row_only_drift(pi, Omega, a=2.0, kappa=1.0)
    Sigma = lyapunov_stationary(K)
    residual = K @ Sigma + Sigma @ K.T - 2 * torch.eye(6, dtype=torch.float64)
    assert float(residual.abs().max()) < 1e-12
    torch.linalg.cholesky(Sigma)


def test_analytic_zero_uses_model_structure_and_explicit_error_units(monkeypatch: pytest.MonkeyPatch) -> None:
    from multiagent_elbo.realizations.gaussian import locality_experiment as experiment

    # A roundoff-sized total can exceed the numerical floor without changing
    # the complete/identity/joint-descent control's analytical Markov property.
    zero = torch.zeros(3, dtype=torch.float64)
    numerical_kl = torch.tensor(4e-11, dtype=torch.float64)
    memory = ParentMemory(torch.zeros(5, dtype=torch.float64), zero, zero, zero,
                          numerical_kl, numerical_kl, zero, 0.2)
    monkeypatch.setattr(experiment, "parent_memory", lambda *args, **kwargs: memory)
    theory = {"a": 0.2, "kappa": 1.0, "dt": 0.5, "block": 2,
              "horizon": 5, "k_max": 2, "dimension": 1}
    numerics = {"stable_kl_max_N": 6, "identity_gate_max_N": 6,
                "filter_check_max_N": 0, "analytic_zero_floor": 1e-12}
    case = {"name": "id_complete", "family": "complete", "links": "identity", "dynamics": "joint_descent"}
    record = experiment.measure_case(6, case, independent_links(6, 1, 0.0, seed=0), theory, numerics)
    assert record["analytic_zero"] is True
    assert record["identity_relative_error"] == [None, None]
    assert record["path_kl_total"] == pytest.approx(4e-11)
    assert record["identity_abs_error_total_nats"] == pytest.approx([4e-11, 4e-11])
    assert record["identity_abs_error_per_block_nats"] == pytest.approx([4e-11 / 3, 4e-11 / 3])
