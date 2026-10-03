"""Local continuous-filter coefficients of tiny Gaussian Euler/observation steps."""
from __future__ import annotations

import json

import torch

from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledModel, CoupledState
from multiagent_elbo.realizations.gaussian.gaussian_message import observe_gaussian, propagate_gaussian


def _example() -> tuple[CoupledModel, CoupledState, torch.Tensor, torch.Tensor]:
    dtype = torch.float64
    a = torch.arange(8, dtype=dtype).reshape(4, 2)/11.-.3
    J_0 = torch.tensor([[1.3, .2], [.2, .9]], dtype=dtype).expand(4, -1, -1).clone()
    H = torch.tensor([[.8, -.15], [-.15, 1.1]], dtype=dtype).expand(4, -1, -1).clone()
    model = CoupledModel(a, J_0, H, torch.tensor([[1, 2], [0, 3], [3, 0], [2, 1]]),
        torch.tensor([[0, 1], [0, 2], [1, 3], [2, 3]]),
        torch.tensor([[0, 1], [0, 2], [3, 1], [3, 2]]),
        torch.tensor([[False, False], [True, False], [False, True], [True, True]]), .7)
    Theta = torch.tensor([[[1.1, .2], [-.1, .9]], [[.9, -.2], [.1, 1.2]],
                          [[1.2, .1], [.2, .8]], [[.8, -.1], [.1, 1.1]]], dtype=dtype)
    mobility = torch.tensor([[[.7, .1], [.1, 1.2]], [[1.1, -.2], [-.2, .8]],
                             [[.9, .3], [.3, 1.4]], [[1.3, -.1], [-.1, .6]]], dtype=dtype)
    state = CoupledState(a+.1, torch.linalg.inv(J_0),
                         torch.full((4, 2), .5, dtype=dtype), Theta)
    return model, state, mobility, torch.tensor([[0, 1, 0, 1]])


def _dense_sheet(
    assignments: torch.Tensor,
    mobility:    torch.Tensor,
    state:       CoupledState,
    model:       CoupledModel,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    r"""Independently assemble F=-M H_J, f=M J_0 a, Q=2M from full records."""
    M = torch.block_diag(*mobility)
    J_0 = torch.block_diag(*model.J_0)
    H_J = J_0.clone()
    for receiver in range(4):
        label = int(assignments[0, receiver])
        source = int(model.sources[receiver, label])
        link = state.Theta[model.link_index[receiver, label]]
        if bool(model.reverse[receiver, label]):
            link = torch.linalg.inv(link)
        difference = torch.zeros((2, 8), dtype=M.dtype)
        difference[:, 2*receiver:2*receiver+2] = torch.eye(2, dtype=M.dtype)
        difference[:, 2*source:2*source+2] = -link
        H_J += difference.T @ model.H[receiver] @ difference/model.tau
    return -M@H_J, M@J_0@model.a.flatten(), 2*M


def _fiber() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    dtype = torch.float64
    P = torch.kron(torch.tensor([[.5, .5, 0., 0.], [0., 0., .5, .5]], dtype=dtype),
                   torch.eye(2, dtype=dtype))
    Z = torch.kron(torch.tensor([[1., 0.], [-1., 0.], [0., 1.], [0., -1.]], dtype=dtype),
                   torch.eye(2, dtype=dtype))/2**.5
    r = torch.tensor([.2, -.3, .4, .1], dtype=dtype)
    m = torch.tensor([-.2, .1, .3, -.4], dtype=dtype)
    L = torch.tensor([[.8, 0., 0., 0.], [.2, .9, 0., 0.],
                      [-.1, .1, .7, 0.], [.2, -.1, .3, 1.]], dtype=dtype)
    S = L@L.T
    T = P.T@torch.linalg.inv(P@P.T)
    return P, Z, (T@r+Z@m).reshape(1, 4, 2), (Z@S@Z.T).unsqueeze(0), S


def test_correlated_gain_and_riccati_coefficients_from_endpoint_conditioning() -> None:
    model, state, mobility, assignments = _example()
    F, _, Q = _dense_sheet(assignments, mobility, state, model)
    P, Z, mu, covariance, S = _fiber()
    C, D = P@F@Z, Z.T@F@Z
    Q_r, Q_z, Q_zr = P@Q@P.T, Z.T@Q@Z, Z.T@Q@P.T
    K = torch.linalg.solve(Q_r, (S@C.T+Q_zr).T).T
    V = D@S+S@D.T+Q_z-K@Q_r@K.T
    assert torch.linalg.matrix_norm(Q_zr) > .5
    assert torch.linalg.matrix_norm(F-F.T) > 1.
    assert torch.linalg.matrix_norm(S@D-D@S) > .5
    gain_errors, covariance_errors = [], []
    for h in (.002, .001, .0005):
        forecast_mu, forecast_covariance = propagate_gaussian(
            mu, covariance, assignments, mobility, state, model, h)
        forecast_r = forecast_mu.flatten(1)@P.T
        # Probe every retained innovation direction through the production mean update.
        innovations = torch.cat((torch.zeros((1, 4), dtype=mu.dtype), torch.eye(4, dtype=mu.dtype)))
        result = observe_gaussian(forecast_mu.expand(5, -1, -1),
            forecast_covariance.expand(5, -1, -1), forecast_r+innovations, block_size=2)
        hidden_means = result['mean'].flatten(1)@Z
        K_h = (hidden_means[1:]-hidden_means[0]).T
        S_h = Z.T@result['covariance'][0]@Z
        exact_K_h = torch.linalg.solve(Q_r+h*C@S@C.T,
            (S@C.T+Q_zr+h*D@S@C.T).T).T
        torch.testing.assert_close(K_h, exact_K_h, atol=2e-12, rtol=2e-12)
        torch.testing.assert_close(result['mean'].flatten(1)@P.T,
            forecast_r+innovations, atol=2e-12, rtol=0.)
        torch.testing.assert_close(P@result['covariance'][0],
            torch.zeros((4, 8), dtype=mu.dtype), atol=2e-12, rtol=0.)
        gain_errors.append(float(torch.linalg.matrix_norm(K_h-K)))
        covariance_errors.append(float(torch.linalg.matrix_norm((S_h-S)/h-V)))
    for errors in (gain_errors, covariance_errors):
        assert 1.95 < errors[0]/errors[1] < 2.05
        assert 1.95 < errors[1]/errors[2] < 2.05
    print(json.dumps({'gain_coefficient_errors': gain_errors, 'riccati_coefficient_errors': covariance_errors,
        'observation_noise_condition': float(torch.linalg.cond(Q_r)),
        'hidden_covariance_condition': float(torch.linalg.cond(S))}))


def test_mean_innovation_matches_correlated_filter_with_sender_force() -> None:
    model, state, mobility, assignments = _example()
    F, f, Q = _dense_sheet(assignments, mobility, state, model)
    P, Z, mu, covariance, S = _fiber()
    C, D = P@F@Z, Z.T@F@Z
    Q_r, Q_zr = P@Q@P.T, Z.T@Q@P.T
    K = torch.linalg.solve(Q_r, (S@C.T+Q_zr).T).T
    K_1 = torch.linalg.solve(Q_r, (D@S@C.T-K@C@S@C.T).T).T
    velocity = F@mu.flatten()+f
    xi = torch.linalg.cholesky(Q_r)@torch.tensor([.2, -.4, .3, -.1], dtype=mu.dtype)
    errors = []
    for h in (.002, .001, .0005):
        forecast_mu, forecast_covariance = propagate_gaussian(
            mu, covariance, assignments, mobility, state, model, h)
        retained = (P@mu.flatten()+h*P@velocity+h**.5*xi).unsqueeze(0)
        result = observe_gaussian(forecast_mu, forecast_covariance, retained, block_size=2)
        expected = Z.T@mu.flatten()+h*Z.T@velocity+h**.5*K@xi
        actual = Z.T@result['mean'].flatten()
        # The scaled leading local residual is K_1 xi, not an order-one drift omission.
        residual = (actual-expected)/h**1.5
        errors.append(float(torch.linalg.vector_norm(residual-K_1@xi)))
    assert 1.95 < errors[0]/errors[1] < 2.05
    assert 1.95 < errors[1]/errors[2] < 2.05
    print(json.dumps({'scaled_mean_remainder_errors': errors}))


def test_full_retention_forecast_and_conditioning_has_no_hidden_message() -> None:
    model, state, mobility, assignments = _example()
    F, f, Q = _dense_sheet(assignments, mobility, state, model)
    mu = state.mu.unsqueeze(0)
    covariance = torch.zeros((1, 8, 8), dtype=mu.dtype)
    h = .003
    forecast_mu, forecast_covariance = propagate_gaussian(
        mu, covariance, assignments, mobility, state, model, h)
    torch.testing.assert_close(forecast_mu.flatten(), mu.flatten()+h*(F@mu.flatten()+f),
        atol=2e-14, rtol=2e-14)
    torch.testing.assert_close(forecast_covariance[0], h*Q, atol=2e-14, rtol=2e-14)
    retained = forecast_mu.flatten(1)+.01
    result = observe_gaussian(forecast_mu, forecast_covariance, retained, block_size=1)
    torch.testing.assert_close(result['mean'].flatten(1), retained, atol=0., rtol=0.)
    torch.testing.assert_close(result['covariance'], covariance, atol=0., rtol=0.)
