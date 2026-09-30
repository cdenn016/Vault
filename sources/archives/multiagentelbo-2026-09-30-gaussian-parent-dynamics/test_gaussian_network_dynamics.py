"""Tiny CPU validation of finite-horizon Gaussian parent laws at a fixed base point."""
from __future__ import annotations

from collections.abc import Iterator
import numpy as np
import pytest
import scipy.linalg
import scipy.stats
import torch


@pytest.fixture(scope="module", autouse=True)
def _single_cpu_thread() -> Iterator[None]:
    previous = torch.get_num_threads()
    torch.set_num_threads(1)
    yield
    torch.set_num_threads(previous)


def _tensor(values: object) -> torch.Tensor:
    return torch.as_tensor(np.asarray(values, dtype=np.float64))


def _conditional(
    mu:       np.ndarray,
    Sigma:    np.ndarray,
    targets:  np.ndarray,
    observed: np.ndarray,
    values:   np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Independent dense Gaussian conditioning oracle."""
    cross = Sigma[np.ix_(targets, observed)]
    gain = scipy.linalg.solve(Sigma[np.ix_(observed, observed)], cross.T,
                              assume_a="pos").T
    return (mu[targets] + gain @ (values - mu[observed]),
            Sigma[np.ix_(targets, targets)] - gain @ cross.T)


def _schedule() -> list[tuple[np.ndarray, np.ndarray, np.ndarray]]:
    """A four-step held schedule with correlated retained/hidden process noise."""
    factors = [
        np.array([[0.8, 0.22, -0.07], [0.11, 0.72, 0.18], [0.04, -0.16, 0.86]]),
        np.array([[0.75, -0.14, 0.06], [0.18, 0.81, -0.10], [-0.03, 0.25, 0.68]]),
        np.array([[0.83, 0.19, 0.02], [-0.12, 0.69, 0.14], [0.09, 0.21, 0.76]]),
        np.array([[0.71, 0.16, -0.04], [0.15, 0.77, 0.11], [0.03, -0.18, 0.82]]),
    ]
    noise_factors = [
        np.array([[0.45, 0, 0], [0.18, 0.40, 0], [-0.08, 0.13, 0.50]]),
        np.array([[0.50, 0, 0], [-0.15, 0.44, 0], [0.11, 0.09, 0.41]]),
        np.array([[0.39, 0, 0], [0.12, 0.48, 0], [0.07, -0.15, 0.46]]),
        np.array([[0.46, 0, 0], [0.09, 0.37, 0], [-0.10, 0.16, 0.43]]),
    ]
    return [(F, np.array([0.07 * (i + 1), -0.04, 0.03 * (i - 1)]), L @ L.T)
            for i, (F, L) in enumerate(zip(factors, noise_factors))]


def _full_path(
    mu0:         np.ndarray,
    Sigma0:      np.ndarray,
    transitions: list[tuple[np.ndarray, np.ndarray, np.ndarray]],
) -> tuple[np.ndarray, np.ndarray]:
    """Construct the full joint path law without the implementation's filter."""
    d = len(mu0)
    mu, Sigma = mu0.copy(), Sigma0.copy()
    for F, u, Q in transitions:
        cross = F @ Sigma[-d:, :]
        next_covariance = F @ Sigma[-d:, -d:] @ F.T + Q
        Sigma = np.block([[Sigma, cross.T], [cross, next_covariance]])
        mu = np.concatenate((mu, F @ mu[-d:] + u))
    return mu, Sigma


def _torch_schedule(
    schedule: list[tuple[np.ndarray, np.ndarray, np.ndarray]],
) -> list[object]:
    from multiagent_elbo.realizations.gaussian.network_dynamics import GaussianTransition

    return [GaussianTransition(_tensor(F), _tensor(u), _tensor(Q)) for F, u, Q in schedule]


def _activation() -> tuple[np.ndarray, np.ndarray]:
    return (np.array([0.7, -1.2, 0.3]),
            np.array([[1.4, 0.2, -0.1], [0.2, 0.8, 0.15], [-0.1, 0.15, 1.1]]))


def _logdet(matrix: np.ndarray) -> float:
    sign, value = np.linalg.slogdet(matrix)
    assert sign > 0
    return float(value)


def test_general_mobility_ou_matches_independent_block_exponential() -> None:
    from multiagent_elbo.realizations.gaussian.network_dynamics import (
        ou_transition, propagate_moments,
    )

    J = np.array([[2.3, -0.4, 0.2], [-0.4, 1.7, -0.3], [0.2, -0.3, 1.4]])
    h = np.array([0.4, -0.7, 0.2])
    L = np.array([[1.1, 0, 0], [0.3, 0.8, 0], [-0.1, 0.2, 0.9]])
    mobility = L @ L.T
    dt = 0.27
    A = -mobility @ J
    van_loan = scipy.linalg.expm(np.block([[A, 2 * mobility],
                                          [np.zeros_like(A), -A.T]]) * dt)
    F = van_loan[:3, :3]
    Q = van_loan[:3, 3:] @ F.T
    equilibrium_mu = scipy.linalg.solve(J, h, assume_a="pos")
    u = equilibrium_mu - F @ equilibrium_mu
    transition = ou_transition(_tensor(J), _tensor(h), _tensor(mobility), dt)

    torch.testing.assert_close(transition.F, _tensor(F), atol=2e-12, rtol=2e-12)
    torch.testing.assert_close(transition.u, _tensor(u), atol=2e-12, rtol=2e-12)
    torch.testing.assert_close(transition.Q, _tensor(Q), atol=2e-12, rtol=2e-12)
    mu0, Sigma0 = _activation()
    propagated = propagate_moments(_tensor(mu0), _tensor(Sigma0), transition)
    torch.testing.assert_close(propagated[0], _tensor(F @ mu0 + u))
    torch.testing.assert_close(propagated[1], _tensor(F @ Sigma0 @ F.T + Q))


def test_activation_filter_uses_actual_nonequilibrium_law_and_order() -> None:
    from multiagent_elbo.realizations.gaussian.network_dynamics import initialize_filter

    mu0, Sigma0 = _activation()
    retained, hidden = np.array([2, 0]), np.array([1])
    r0 = np.array([-0.2, 0.9])
    expected = _conditional(mu0, Sigma0, hidden, retained, r0)
    state = initialize_filter(_tensor(mu0), _tensor(Sigma0),
                              torch.tensor(retained), _tensor(r0))

    assert state.retained.tolist() == [2, 0]
    assert state.hidden.tolist() == [1]
    torch.testing.assert_close(state.mu_h, _tensor(expected[0]))
    torch.testing.assert_close(state.Sigma_h, _tensor(expected[1]))


def test_history_filter_and_density_match_full_joint_path_conditioning() -> None:
    from multiagent_elbo.realizations.gaussian.network_dynamics import initialize_filter

    mu0, Sigma0 = _activation()
    schedule = _schedule()
    transitions = _torch_schedule(schedule)
    path_mu, path_Sigma = _full_path(mu0, Sigma0, schedule)
    retained, hidden = np.array([2, 0]), np.array([1])
    observations = np.array([[-0.2, 0.9], [0.4, -0.1], [0.7, 0.3],
                             [-0.3, 0.2], [0.1, -0.4]])
    state = initialize_filter(_tensor(mu0), _tensor(Sigma0),
                              torch.tensor(retained), _tensor(observations[0]))

    for step, transition in enumerate(transitions):
        observed = np.concatenate([3 * time + retained for time in range(step + 1)])
        target = 3 * (step + 1) + np.concatenate((retained, hidden))
        expected_mu, expected_Sigma = _conditional(
            path_mu, path_Sigma, target, observed, observations[:step + 1].flatten())
        forecast = state.predict(transition, _tensor(observations[step]))
        torch.testing.assert_close(forecast.mu_r, _tensor(expected_mu[:2]))
        torch.testing.assert_close(forecast.mu_h, _tensor(expected_mu[2:]))
        torch.testing.assert_close(forecast.Sigma_r, _tensor(expected_Sigma[:2, :2]))
        torch.testing.assert_close(forecast.Sigma_h, _tensor(expected_Sigma[2:, 2:]))
        torch.testing.assert_close(forecast.Sigma_hr, _tensor(expected_Sigma[2:, :2]))
        expected_log_density = scipy.stats.multivariate_normal.logpdf(
            observations[step + 1], mean=expected_mu[:2], cov=expected_Sigma[:2, :2])
        torch.testing.assert_close(forecast.log_prob(_tensor(observations[step + 1])),
                                   _tensor(expected_log_density))
        state = state.condition(forecast, _tensor(observations[step + 1]))
        updated = _conditional(path_mu, path_Sigma, 3 * (step + 1) + hidden,
                               np.concatenate((observed, 3 * (step + 1) + retained)),
                               observations[:step + 2].flatten())
        torch.testing.assert_close(state.mu_h, _tensor(updated[0]))
        torch.testing.assert_close(state.Sigma_h, _tensor(updated[1]))


def test_markov_projection_matches_exact_pair_conditionals() -> None:
    from multiagent_elbo.realizations.gaussian.network_dynamics import (
        markov_projection, propagate_moments,
    )

    mu0, Sigma0 = _activation()
    F, u, Q = _schedule()[0]
    transition = _torch_schedule([(F, u, Q)])[0]
    retained = np.array([2, 0])
    next_mu, next_Sigma = F @ mu0 + u, F @ Sigma0 @ F.T + Q
    cross = (F @ Sigma0)[np.ix_(retained, retained)]
    expected_F = scipy.linalg.solve(Sigma0[np.ix_(retained, retained)],
                                    cross.T, assume_a="pos").T
    expected_u = next_mu[retained] - expected_F @ mu0[retained]
    expected_Q = next_Sigma[np.ix_(retained, retained)] - expected_F @ cross.T
    projected = markov_projection(_tensor(mu0), _tensor(Sigma0), transition,
                                  torch.tensor(retained))

    torch.testing.assert_close(projected.F, _tensor(expected_F))
    torch.testing.assert_close(projected.u, _tensor(expected_u))
    torch.testing.assert_close(projected.Q, _tensor(expected_Q))
    marginal_next = propagate_moments(_tensor(mu0[retained]),
                                     _tensor(Sigma0[np.ix_(retained, retained)]), projected)
    torch.testing.assert_close(marginal_next[0], _tensor(next_mu[retained]))
    torch.testing.assert_close(marginal_next[1], _tensor(next_Sigma[np.ix_(retained, retained)]))


def test_memory_information_equals_forward_kl_to_markov_product_law() -> None:
    from multiagent_elbo.realizations.gaussian.network_dynamics import memory_information

    mu0, Sigma0 = _activation()
    schedule = _schedule()
    retained = np.array([2, 0])
    path_mu, path_Sigma = _full_path(mu0, Sigma0, schedule)
    path_retained = np.concatenate([3 * time + retained for time in range(5)])
    actual_mu = path_mu[path_retained]
    actual_Sigma = path_Sigma[np.ix_(path_retained, path_retained)]
    pair_schedule = []
    expected_information = []
    for step in range(4):
        previous = np.arange(2 * step, 2 * (step + 1))
        current = np.arange(2 * (step + 1), 2 * (step + 2))
        cross = actual_Sigma[np.ix_(current, previous)]
        pair_F = scipy.linalg.solve(actual_Sigma[np.ix_(previous, previous)],
                                    cross.T, assume_a="pos").T
        pair_u = actual_mu[current] - pair_F @ actual_mu[previous]
        pair_Q = actual_Sigma[np.ix_(current, current)] - pair_F @ cross.T
        history = np.arange(2 * (step + 1))
        _, innovation = _conditional(actual_mu, actual_Sigma, current, history,
                                      actual_mu[history])
        expected_information.append(0.5 * (_logdet(pair_Q) - _logdet(innovation)))
        pair_schedule.append((pair_F, pair_u, pair_Q))

    markov_mu, markov_Sigma = _full_path(actual_mu[:2], actual_Sigma[:2, :2], pair_schedule)
    delta = markov_mu - actual_mu
    dimension = len(actual_mu)
    forward_kl = 0.5 * (
        np.trace(scipy.linalg.solve(markov_Sigma, actual_Sigma, assume_a="pos"))
        + delta @ scipy.linalg.solve(markov_Sigma, delta, assume_a="pos")
        - dimension + _logdet(markov_Sigma) - _logdet(actual_Sigma))
    information = memory_information(_tensor(mu0), _tensor(Sigma0),
                                     torch.tensor(retained), _torch_schedule(schedule))

    assert information.shape == (4,)
    torch.testing.assert_close(information, _tensor(expected_information),
                               atol=2e-12, rtol=2e-10)
    torch.testing.assert_close(information.sum(), _tensor(forward_kl),
                               atol=2e-12, rtol=2e-10)
    assert float(information[1:].sum()) > 1e-5
    assert abs(float(information[0])) < 2e-12


def test_retaining_all_or_autonomous_retained_block_has_zero_memory() -> None:
    from multiagent_elbo.realizations.gaussian.network_dynamics import memory_information

    mu0, Sigma0 = _activation()
    all_information = memory_information(
        _tensor(mu0), _tensor(Sigma0), torch.tensor([2, 0, 1]), _torch_schedule(_schedule()))
    torch.testing.assert_close(all_information, torch.zeros(4, dtype=torch.float64),
                               atol=2e-12, rtol=0)
    autonomous_schedule = [
        (np.array([[0.7, 0], [0.12, 0.8]]), np.array([0.03, -0.04]),
         np.array([[0.2, 0.05], [0.05, 0.3]]))
    ] * 4
    autonomous_information = memory_information(
        _tensor([0.2, -0.1]), _tensor([[1.1, 0.25], [0.25, 0.8]]),
        torch.tensor([0]), _torch_schedule(autonomous_schedule))
    torch.testing.assert_close(autonomous_information, torch.zeros(4, dtype=torch.float64),
                               atol=2e-12, rtol=0)


def test_passive_noncompact_frame_transforms_mobility_filter_and_memory() -> None:
    from multiagent_elbo.realizations.gaussian.network_dynamics import (
        initialize_filter, memory_information, ou_transition,
    )

    J = np.array([[2.3, -0.4, 0.2], [-0.4, 1.7, -0.3], [0.2, -0.3, 1.4]])
    h = np.array([0.4, -0.7, 0.2])
    mobility = np.array([[1.3, 0.2, -0.1], [0.2, 0.9, 0.15], [-0.1, 0.15, 1.1]])
    retained, hidden = np.array([2, 0]), np.array([1])
    T_r = np.array([[1.3, 0.4], [-0.2, 0.8]])
    T = np.zeros((3, 3))
    T[np.ix_(retained, retained)] = T_r
    T[np.ix_(hidden, hidden)] = np.array([[1.6]])
    inverse = scipy.linalg.inv(T)
    original = ou_transition(_tensor(J), _tensor(h), _tensor(mobility), 0.23)
    transformed = ou_transition(_tensor(inverse.T @ J @ inverse), _tensor(inverse.T @ h),
                                _tensor(T @ mobility @ T.T), 0.23)
    torch.testing.assert_close(transformed.F, _tensor(T) @ original.F @ _tensor(inverse))
    torch.testing.assert_close(transformed.u, _tensor(T) @ original.u)
    torch.testing.assert_close(transformed.Q, _tensor(T) @ original.Q @ _tensor(T.T))

    mu0, Sigma0 = _activation()
    r0, r1 = np.array([-0.2, 0.9]), np.array([0.4, -0.1])
    state = initialize_filter(_tensor(mu0), _tensor(Sigma0), torch.tensor(retained), _tensor(r0))
    changed = initialize_filter(_tensor(T @ mu0), _tensor(T @ Sigma0 @ T.T),
                                torch.tensor(retained), _tensor(T_r @ r0))
    forecast = state.predict(original, _tensor(r0))
    changed_forecast = changed.predict(transformed, _tensor(T_r @ r0))
    torch.testing.assert_close(changed_forecast.mu_r, _tensor(T_r) @ forecast.mu_r)
    torch.testing.assert_close(changed_forecast.Sigma_r,
                               _tensor(T_r) @ forecast.Sigma_r @ _tensor(T_r.T))
    torch.testing.assert_close(changed_forecast.Sigma_hr,
                               1.6 * forecast.Sigma_hr @ _tensor(T_r.T))
    torch.testing.assert_close(changed_forecast.log_prob(_tensor(T_r @ r1)),
                               forecast.log_prob(_tensor(r1)) - _tensor(_logdet(T_r)))
    original_updated = state.condition(forecast, _tensor(r1))
    changed_updated = changed.condition(changed_forecast, _tensor(T_r @ r1))
    torch.testing.assert_close(changed_updated.mu_h, 1.6 * original_updated.mu_h)
    torch.testing.assert_close(changed_updated.Sigma_h, 1.6**2 * original_updated.Sigma_h)
    original_information = memory_information(_tensor(mu0), _tensor(Sigma0),
                                             torch.tensor(retained), [original] * 4)
    changed_information = memory_information(
        _tensor(T @ mu0), _tensor(T @ Sigma0 @ T.T), torch.tensor(retained), [transformed] * 4)
    torch.testing.assert_close(changed_information, original_information,
                               atol=2e-12, rtol=2e-10)
