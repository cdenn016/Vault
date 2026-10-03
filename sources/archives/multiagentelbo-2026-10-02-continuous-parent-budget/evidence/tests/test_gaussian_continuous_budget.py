"""Tiny exact-enumeration and coupled-tape checks for the frozen budget."""
from __future__ import annotations

import importlib
import itertools
from types import ModuleType

import torch

from test_gaussian_message import _example
from multiagent_elbo.realizations.gaussian.gaussian_message import observe_gaussian
from multiagent_elbo.realizations.gaussian.source_gaussian import sequential_source_message
from multiagent_elbo.realizations.gaussian.switching_paths import source_log_posterior, sheet_force


def _api() -> ModuleType:
    return importlib.import_module("multiagent_elbo.realizations.gaussian.continuous_budget")


def test_sampled_prefix_chain_budget_matches_complete_assignment_enumeration() -> None:
    model, state, _ = _example()
    X = (state.mu+.13).unsqueeze(0)
    retained = X.reshape(1, 2, 2, 2).mean(2).flatten(1)
    conditioned = observe_gaussian(state.mu.unsqueeze(0), torch.block_diag(*state.Sigma)[None], retained, 2)
    mu, cov = conditioned["mean"], conditioned["covariance"]
    J = torch.tensor([[0, 1, 0, 1]])
    labels = torch.tensor(list(itertools.product(range(2), repeat=4)))
    native_rows = source_log_posterior(X, state, model)
    native_logs = native_rows.expand(16, -1, -1).gather(-1, labels[..., None]).squeeze(-1).sum(-1)
    candidate_logs = sequential_source_message(mu.expand(16, -1, -1), cov.expand(16, -1, -1),
        J.expand(16, -1), labels, state, model, 2)["log_refresh"]
    expected_mark = (native_logs.exp()*(native_logs-candidate_logs)).sum()
    visible = (labels != J).any(-1)
    expected_visible = (native_logs.exp()*(native_logs-candidate_logs)-native_logs.exp()
                        +candidate_logs.exp())[visible].sum()
    values = [_api().source_budget_probe(X, mu, cov, J, label[None], state, model, 2)
              for label in labels]
    actual_mark = sum(native_logs[i].exp()*value["mark_kl"] for i, value in enumerate(values))
    actual_visible = sum(native_logs[i].exp()*value["visible_kl"] for i, value in enumerate(values))
    torch.testing.assert_close(actual_mark.squeeze(), expected_mark, atol=2e-13, rtol=2e-13)
    torch.testing.assert_close(actual_visible.squeeze(), expected_visible, atol=2e-13, rtol=2e-13)
    assert float(values[0]["self_psi"]) > 0


def test_full_retention_is_zero_cost_on_shared_event_and_brownian_tapes() -> None:
    model, state, mobility = _example()
    result = _api().sample_frozen_budget(mobility, state, model, 1., 1, 4, 2, 78)
    assert result["proposal_times"].numel() > 0
    for level in ("coarse", "fine"):
        times = result[level+"_times"]
        for event in result["proposal_times"]:
            assert bool((times == event).any())
        torch.testing.assert_close(result[level+"_native"], result[level+"_mean"], atol=2e-14, rtol=0.)
        for key in ("drift_integral", "mark_integral", "self_integral", "visible_integral", "total_integral"):
            torch.testing.assert_close(result[level+"_"+key], torch.zeros((), dtype=torch.float64), atol=3e-12, rtol=0.)
    fine_times, fine_noise = result["fine_times"], result["fine_dW"]
    for i, (a, b) in enumerate(zip(result["coarse_times"][:-1], result["coarse_times"][1:])):
        start = int(torch.searchsorted(fine_times, a))
        stop = int(torch.searchsorted(fine_times, b))
        torch.testing.assert_close(result["coarse_dW"][i], fine_noise[start:stop].sum(0), atol=0., rtol=0.)


def test_retained_probe_rows_and_force_records_reproduce_reported_budget() -> None:
    model, state, mobility = _example()
    result = _api().sample_frozen_budget(mobility, state, model, .1, 2, 4, 3, 93)
    for level in ("coarse", "fine"):
        beta, candidate = result[level+"_probe_log_beta"], result[level+"_probe_log_candidate_rows"]
        marks = (beta.exp()*(beta-candidate)).sum((-1, -2))
        torch.testing.assert_close(marks, result[level+"_probe_mark_kl"])
        self_cost = result[level+"_probe_self_psi"]
        torch.testing.assert_close(.1*(marks-self_cost).mean(), result[level+"_visible_integral"])
        times, X, mu, J = [result[level+"_"+key] for key in ("times", "native", "mean", "assignments")]
        weights = torch.nn.functional.one_hot(J[:-1], 2).to(X.dtype)
        difference = sheet_force(X[:-1], weights, state.Theta, model)-sheet_force(mu[:-1], weights, state.Theta, model)
        projected = torch.einsum("nij,tnj->tni", mobility, difference).reshape(-1, 2, 2, 2).mean(2)
        Qr = 2*mobility.reshape(2, 2, 2, 2).sum(1)/4
        rate = .5*torch.einsum("tni,nij,tnj->t", projected, torch.linalg.inv(Qr), projected)
        torch.testing.assert_close(rate, result[level+"_drift_rates"], atol=2e-13, rtol=2e-13)
        torch.testing.assert_close((rate*torch.diff(times)).sum(), result[level+"_drift_integral"])
        torch.testing.assert_close(result[level+"_total_integral"], result[level+"_drift_integral"]+result[level+"_visible_integral"])
        assert float(result[level+"_projection_max_error"]) < 1e-12
        assert float(result[level+"_covariance_projection_max_error"]) < 1e-12
