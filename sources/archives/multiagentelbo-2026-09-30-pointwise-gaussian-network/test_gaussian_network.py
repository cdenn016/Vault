"""Tiny CPU grounding for complete Gaussian laws and their inherited memory."""
from __future__ import annotations

from collections.abc import Iterator
from fractions import Fraction as F
from math import log, pi

import numpy as np
import pytest
import scipy.linalg
import torch

from rg_v2.conditional_gaussian_model import (
    ExactLog, GaussianInfo, log_integral, marginal_schur, moments,
)


@pytest.fixture(scope="module", autouse=True)
def _single_cpu_thread() -> Iterator[None]:
    previous = torch.get_num_threads()
    torch.set_num_threads(1)
    yield
    torch.set_num_threads(previous)


def _tensor(values: object) -> torch.Tensor:
    return torch.as_tensor(np.asarray(values, dtype=np.float64))


def _scalar_network() -> tuple[object, GaussianInfo]:
    from multiagent_elbo.realizations.gaussian.network import assemble_network

    action = assemble_network(
        J_0=_tensor([[[2]], [[3]], [[4]]]),
        mu_0=_tensor([[0.5], [-1], [2]]),
        A_e=_tensor([[[1]], [[2]]]),
        B_e=_tensor([[[1]], [[0.5]]]),
        Gamma_inv=_tensor([[[2]], [[3]]]),
        o_e=_tensor([[1], [-1]]),
        edges=torch.tensor([[0, 1], [1, 2]], dtype=torch.long),
    )
    # Hand-expanded rational precision/source. GaussianInfo uses log-density
    # constant=-c, whereas GaussianAction uses energy offset +c.
    info = GaussianInfo(
        tuple(tuple(F(x) for x in row) for row in
              ((4, -2, 0), (-2, 17, -3), (0, -3, F(19, 4)))),
        (F(3), F(-11), F(19, 2)),
        ExactLog(F(-49, 4), F(-5, 2), F(144)),
    )
    return action, info


def test_normalized_record_assembly_retains_source_and_scalar_mass() -> None:
    action, info = _scalar_network()
    exact = moments(info)
    mu, Sigma = action.moments()

    torch.testing.assert_close(action.J, _tensor(info.J))
    torch.testing.assert_close(action.h, _tensor(info.h))
    torch.testing.assert_close(action.c, _tensor(-info.constant.display()))
    torch.testing.assert_close(mu, _tensor(exact.mean))
    torch.testing.assert_close(Sigma, _tensor(exact.covariance))
    torch.testing.assert_close(action.log_mass(), _tensor(log_integral(info).display()))


def test_ordered_complete_schur_matches_exact_rational_oracle() -> None:
    from multiagent_elbo.realizations.gaussian.network import marginalize

    action, info = _scalar_network()
    parent = marginalize(torch.tensor([2, 0]), action)
    expected = marginal_schur(info, (2, 0))

    assert parent.retained.tolist() == [2, 0]
    assert parent.hidden.tolist() == [1]
    torch.testing.assert_close(parent.action.J, _tensor(expected.J))
    torch.testing.assert_close(parent.action.h, _tensor(expected.h))
    torch.testing.assert_close(parent.action.c, _tensor(-expected.constant.display()))
    torch.testing.assert_close(parent.action.log_mass(), action.log_mass())
    torch.testing.assert_close(parent.hidden_gain, _tensor([[F(3, 17), F(2, 17)]]))
    torch.testing.assert_close(parent.hidden_intercept, _tensor([F(-11, 17)]))
    torch.testing.assert_close(parent.hidden_covariance(), _tensor([[F(1, 17)]]))


def test_staged_elimination_and_reverse_laws_compose() -> None:
    from multiagent_elbo.realizations.gaussian.network import marginalize

    action, info = _scalar_network()
    middle = marginalize(torch.tensor([2, 0]), action)
    staged = marginalize(torch.tensor([1]), middle.action)
    direct = marginalize(torch.tensor([0]), action)
    expected = marginal_schur(info, (0,))

    torch.testing.assert_close(staged.action.J, _tensor(expected.J))
    torch.testing.assert_close(staged.action.h, _tensor(expected.h))
    torch.testing.assert_close(staged.action.c, direct.action.c)
    # Also compose reverse kernels away from equilibrium; a scalar-offset-only
    # comparison would miss lost hidden variance or wrong coordinate ordering.
    coarse_mu, coarse_Sigma = _tensor([0.7]), _tensor([[1.3]])
    middle_mu, middle_Sigma = staged.lift_moments(coarse_mu, coarse_Sigma)
    full_mu, full_Sigma = middle.lift_moments(middle_mu, middle_Sigma)
    direct_mu, direct_Sigma = direct.lift_moments(coarse_mu, coarse_Sigma)
    torch.testing.assert_close(full_mu, direct_mu)
    torch.testing.assert_close(full_Sigma, direct_Sigma)
    equilibrium = middle.lift_moments(*middle.action.moments())
    for lifted, original in zip(equilibrium, action.moments()):
        torch.testing.assert_close(lifted, original)


def test_retain_all_permutation_preserves_law_and_empty_hidden_kernel() -> None:
    from multiagent_elbo.realizations.gaussian.network import marginalize

    action, _ = _scalar_network()
    parent = marginalize(torch.tensor([2, 0, 1]), action)
    order = torch.tensor([2, 0, 1])

    torch.testing.assert_close(parent.action.J, action.J[order][:, order])
    torch.testing.assert_close(parent.action.h, action.h[order])
    torch.testing.assert_close(parent.action.c, action.c)
    assert parent.hidden.numel() == 0
    assert parent.hidden_covariance().shape == (0, 0)
    torch.testing.assert_close(parent.memory_kernel(0.4), torch.zeros_like(action.J))
    torch.testing.assert_close(parent.markov_defect(), torch.zeros_like(action.J))
    for lifted, original in zip(parent.lift_moments(*parent.action.moments()), action.moments()):
        torch.testing.assert_close(lifted, original)


def test_elimination_keeps_generated_asymmetric_cross_blocks() -> None:
    from multiagent_elbo.realizations.gaussian.network import assemble_network, marginalize

    action = assemble_network(
        J_0=torch.eye(2, dtype=torch.float64).repeat(3, 1, 1),
        mu_0=torch.zeros((3, 2), dtype=torch.float64),
        A_e=torch.eye(2, dtype=torch.float64).repeat(2, 1, 1),
        B_e=_tensor([[[1, 1], [0, 1]], [[2, 0], [1, 1]]]),
        Gamma_inv=torch.eye(2, dtype=torch.float64).repeat(2, 1, 1),
        o_e=torch.zeros((2, 2), dtype=torch.float64),
        edges=torch.tensor([[0, 1], [1, 2]], dtype=torch.long),
    )
    parent = marginalize(torch.tensor([0, 1, 4, 5]), action)
    expected_cross = _tensor([[-8, -2], [-1, -3]]) / 11

    torch.testing.assert_close(parent.action.J[:2, 2:], expected_cross)
    assert not torch.allclose(expected_cross, expected_cross.T)
    torch.testing.assert_close(parent.action.J, parent.action.J.T)
    # A direct covariance restriction is an independent moment-level oracle.
    _, fine_Sigma = action.moments()
    keep = torch.tensor([0, 1, 4, 5])
    torch.testing.assert_close(parent.action.moments()[1], fine_Sigma[keep][:, keep])


def test_rectangular_rank_deficient_records_need_only_a_proper_prior() -> None:
    from multiagent_elbo.realizations.gaussian.network import assemble_network

    action = assemble_network(
        J_0=2 * torch.eye(2, dtype=torch.float64).repeat(2, 1, 1),
        mu_0=torch.zeros((2, 2), dtype=torch.float64),
        A_e=_tensor([[[1, 0]]]), B_e=_tensor([[[0, 1]]]),
        Gamma_inv=_tensor([[[3]]]), o_e=_tensor([[2]]),
        edges=torch.tensor([[0, 1]], dtype=torch.long),
    )
    mu, Sigma = action.moments()

    torch.testing.assert_close(action.J, _tensor([[5, 0, 0, -3], [0, 2, 0, 0],
                                                 [0, 0, 2, 0], [-3, 0, 0, 5]]))
    torch.testing.assert_close(mu, _tensor([0.75, 0, 0, -0.75]))
    torch.testing.assert_close(Sigma[[1, 2]][:, [1, 2]], 0.5 * torch.eye(2, dtype=torch.float64))
    # The record has prior predictive variance 1/2+1/2+1/3=4/3.
    expected_mass = -0.5 * (log(2 * pi * 4 / 3) + 3)
    torch.testing.assert_close(action.log_mass(), _tensor(expected_mass))


def test_noncompact_frame_change_carries_prior_and_record_maps() -> None:
    from multiagent_elbo.realizations.gaussian.network import assemble_network, marginalize

    J_0 = _tensor([[[2, 0.2], [0.2, 3]], [[3, -0.1], [-0.1, 2]]])
    mu_0 = _tensor([[0.2, -0.5], [0.7, 0.1]])
    A_e = _tensor([[[1, 0.2], [0, 1]]])
    B_e = _tensor([[[0.5, 1], [-0.2, 0.8]]])
    G = _tensor([[[2, 1], [0, 1]], [[1, 0], [0.3, 1.5]]])
    G_inv = torch.linalg.inv(G)
    shared = dict(Gamma_inv=_tensor([[[2, 0.1], [0.1, 1]]]),
                  o_e=_tensor([[0.4, -0.7]]), edges=torch.tensor([[0, 1]]))
    action = assemble_network(J_0=J_0, mu_0=mu_0, A_e=A_e, B_e=B_e, **shared)
    changed = assemble_network(
        J_0=G_inv.transpose(-1, -2) @ J_0 @ G_inv,
        mu_0=(G @ mu_0.unsqueeze(-1)).squeeze(-1),
        A_e=A_e @ G_inv[0], B_e=B_e @ G_inv[1], **shared,
    )
    T = torch.block_diag(*G)
    T_inv = torch.linalg.inv(T)
    mu, Sigma = action.moments()

    torch.testing.assert_close(changed.J, T_inv.T @ action.J @ T_inv)
    torch.testing.assert_close(changed.h, T_inv.T @ action.h)
    torch.testing.assert_close(changed.c, action.c + torch.linalg.slogdet(T)[1])
    torch.testing.assert_close(changed.log_mass(), action.log_mass())
    torch.testing.assert_close(changed.moments()[0], T @ mu)
    torch.testing.assert_close(changed.moments()[1], T @ Sigma @ T.T)
    parent = marginalize(torch.tensor([2, 3]), action)
    changed_parent = marginalize(torch.tensor([2, 3]), changed)
    torch.testing.assert_close(changed_parent.action.J, G_inv[1].T @ parent.action.J @ G_inv[1])
    torch.testing.assert_close(changed_parent.action.c,
                               parent.action.c + torch.linalg.slogdet(G[1])[1])


def test_link_gradient_through_assembly_and_complete_schur_matches_difference() -> None:
    from multiagent_elbo.realizations.gaussian.network import assemble_network, marginalize

    def objective(B_e: torch.Tensor) -> torch.Tensor:
        action = assemble_network(
            J_0=2 * torch.eye(2, dtype=torch.float64).repeat(2, 1, 1),
            mu_0=_tensor([[0.1, 0.2], [-0.2, 0.3]]),
            A_e=torch.eye(2, dtype=torch.float64).unsqueeze(0), B_e=B_e,
            Gamma_inv=_tensor([[[1, 0.1], [0.1, 2]]]), o_e=_tensor([[0.2, -0.1]]),
            edges=torch.tensor([[0, 1]]),
        )
        parent = marginalize(torch.tensor([2, 3]), action)
        return action.log_mass() + parent.action.c + 0.1 * parent.action.J.square().sum()

    B = _tensor([[[1, 0.3], [-0.2, 0.9]]]).requires_grad_()
    gradient = torch.autograd.grad(objective(B), B)[0]
    direction = torch.zeros_like(B)
    direction[0, 0, 1] = 1
    eps = 1e-6
    with torch.no_grad():
        difference = (objective(B + eps * direction) - objective(B - eps * direction)) / (2 * eps)
    torch.testing.assert_close(gradient[0, 0, 1], difference, rtol=2e-6, atol=2e-8)


def test_complex_realification_preserves_maps_and_unitary_norms() -> None:
    from multiagent_elbo.realizations.gaussian.network import realify_map

    L = torch.tensor([[1 + 2j, 3 - 1j]], dtype=torch.complex128)
    M = torch.tensor([[1 + 0.5j, 0.2j], [0.3 - 0.1j, 2 - 0.5j]], dtype=torch.complex128)
    z = torch.tensor([0.4 + 0.2j, -0.3 + 0.7j], dtype=torch.complex128)
    real_z = torch.cat((z.real, z.imag))
    value = L @ z

    torch.testing.assert_close(realify_map(L), _tensor([[1, 3, -2, 1], [2, -1, 1, 3]]))
    torch.testing.assert_close(realify_map(L) @ real_z, torch.cat((value.real, value.imag)))
    torch.testing.assert_close(realify_map(L @ M), realify_map(L) @ realify_map(M))
    U = torch.tensor([[0.6, 0.8j], [0.8j, 0.6]], dtype=torch.complex128)
    real_U = realify_map(U)
    torch.testing.assert_close(real_U.T @ real_U, torch.eye(4, dtype=torch.float64))
    torch.testing.assert_close((real_U @ real_z).square().sum(), z.abs().square().sum())


def test_inherited_ou_memory_preserves_equilibrium_without_claiming_markov_law() -> None:
    from multiagent_elbo.realizations.gaussian.network import GaussianAction, marginalize

    action = GaussianAction(J=_tensor([[2, 1], [1, 3]]), h=_tensor([1, -2]), c=_tensor(0.7))
    parent = marginalize(torch.tensor([0]), action)
    t = 0.5
    expected_lag = scipy.linalg.expm(-np.array([[2, 1], [1, 3]]) * t) @ np.array([[0.6, -0.2], [-0.2, 0.4]])
    lag = parent.stationary_lag_covariance(t)
    naive = torch.exp(-parent.action.J * t) * parent.action.moments()[1]

    torch.testing.assert_close(parent.memory_kernel(t), _tensor([[np.exp(-3 * t)]]))
    torch.testing.assert_close(parent.markov_defect(), _tensor([[F(1, 3)]]))
    torch.testing.assert_close(lag, _tensor([[expected_lag[0, 0]]]))
    assert float(torch.abs(lag - naive).max()) > 1e-3
    for lifted, original in zip(parent.lift_moments(*parent.action.moments()), action.moments()):
        torch.testing.assert_close(lifted, original)
