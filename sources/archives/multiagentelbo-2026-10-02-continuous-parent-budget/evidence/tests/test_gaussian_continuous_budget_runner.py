"""Tiny spawned runner check for saved tapes, configuration, and summaries."""
from __future__ import annotations

import json
from pathlib import Path
import zipfile

import numpy as np
import pytest

from test_gaussian_message import _example
from multiagent_elbo.realizations.gaussian import continuous_budget_experiment as runner
from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledModel, CoupledState


def test_spawned_runner_retains_paths_and_reproduces_paired_summaries(
    tmp_path:    Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Exercise a real child with tiny states and reconstruct estimates from NPZs."""
    model, state, _ = _example()
    activation = tmp_path/"activation"
    activation.mkdir()
    np.savez(activation/"N4-learn_both-final.npz", **{
        key: getattr(state, key).numpy() for key in ("mu", "Sigma", "pi", "Theta")})

    def build_case(
        n_agents:   int,
        dimension:  int,
        seed:       int,
        link_scale: float,
    ) -> tuple[CoupledModel, CoupledState]:
        """Substitute only the parent builder; the spawned child gets its context."""
        assert (n_agents, dimension, seed, link_scale) == (4, 2, 11, .2)
        return model, state

    monkeypatch.setattr(runner, "build_coupled_case", build_case)
    run = {"activation_root": str(activation), "model_seed": 11, "path_seed": 93,
           "n_paths": 2, "workers": 1}
    theory = {"n_agents": [4], "dimension": 2, "link_scale": .2, "tau": model.tau,
              "block_size": 2, "horizon": .1, "coarse_steps": 4, "n_probes": 1}
    output = tmp_path/"output"
    result = runner.run_frozen_budget_study(
        run, theory, {"device": "cpu", "dtype": "float64", "cpu_threads": 1},
        {"root": str(output)})
    directory, = output.iterdir()
    metadata = json.loads((directory/"metadata.json").read_text(encoding="utf-8"))
    case = json.loads((directory/"N4.json").read_text(encoding="utf-8"))
    assert result["status"] == metadata["status"] == case["status"] == "pass"
    assert "active_case" not in metadata and "active_path" not in metadata
    assert case["completed_paths"] == 2
    assert case["coarse_dt"] == .025 and case["fine_dt"] == .0125
    assert 0 < case["coarse_dt_times_bound"] <= 1
    assert [path["seed"] for path in case["paths"]] == [93, 103]
    assert (directory/"inputs/N4-learn_both-final.npz").read_bytes() == (activation/"N4-learn_both-final.npz").read_bytes()
    with zipfile.ZipFile(directory/"source.zip") as archive:
        assert "src/multiagent_elbo/realizations/gaussian/continuous_budget.py" in archive.namelist()
        assert "tests/test_gaussian_continuous_limit.py" in archive.namelist()
    paths = []
    for index in range(2):
        with np.load(directory/f"N4-path{index:03d}.npz") as stored:
            values = {key: stored[key].copy() for key in stored.files}
        paths.append(values)
        for key in ("initial_X", "initial_J", "proposal_times", "proposal_uniforms",
                    "probe_times", "probe_uniforms", "fine_times", "fine_dW"):
            assert key in values and np.isfinite(values[key]).all()
        assert values["initial_X"].shape == (4, 2)
        assert values["probe_uniforms"].shape == (1, 4)
        for grid in ("coarse", "fine"):
            assert values[grid+"_native"].shape == values[grid+"_mean"].shape
            assert values[grid+"_assignments"].shape == values[grid+"_native"].shape[:-1]
            beta = values[grid+"_probe_log_beta"]
            rows = values[grid+"_probe_log_candidate_rows"]
            np.testing.assert_allclose((np.exp(beta)*(beta-rows)).sum((-1, -2)),
                                       values[grid+"_probe_mark_kl"], rtol=1e-13, atol=1e-13)
            np.testing.assert_allclose((values[grid+"_drift_rates"]*np.diff(values[grid+"_times"])).sum(),
                                       values[grid+"_drift_integral"], rtol=1e-13, atol=1e-13)
            assert float(values[grid+"_proposal_count"]) == case["paths"][index][grid+"_proposal_count"]
    assert not np.array_equal(paths[0]["initial_X"], paths[1]["initial_X"])
    for metric in ("drift", "mark", "self", "visible", "total", "augmented"):
        key = metric+"_integral"
        coarse = np.array([float(path["coarse_"+key]) for path in paths])
        fine = np.array([float(path["fine_"+key]) for path in paths])
        for grid, values in (("coarse", coarse), ("fine", fine), ("fine_minus_coarse", fine-coarse)):
            np.testing.assert_allclose(case["estimates"][grid][key]["mean"], values.mean(), rtol=0., atol=0.)
            np.testing.assert_allclose(case["estimates"][grid][key]["standard_error"],
                                       values.std(ddof=1)/np.sqrt(2), rtol=0., atol=0.)
