"""Tiny serial-versus-spawn parity for the continuation transport."""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
import importlib
import multiprocessing

import numpy as np
import torch

from multiagent_elbo.realizations.gaussian.source_adapted_filter import gaussian_joint_scores
from multiagent_elbo.realizations.gaussian.switching_paths import sample_switching_history
from tests.test_gaussian_joint_parent import _example


def test_spawn_worker_preserves_both_deterministic_arm_results() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_adapted_parallel")
    model, initial, mobility = _example()
    schedule = (initial,)*2
    history = sample_switching_history(mobility, initial, schedule, model, .02, 1, 41)
    R = history.paths.mean(2)
    context = {"R": R, "assignments": history.assignments, "initial": initial,
               "schedule": schedule, "model": model, "dt": .02, "block": 3,
               "refresh_rate": 1., "shortcut_mass": 1e-4}
    with ProcessPoolExecutor(max_workers=1, mp_context=multiprocessing.get_context("spawn"),
                             initializer=api._initialize_worker, initargs=(context,)) as pool:
        for arm, reset in (("gaussian", False), ("reset_gaussian", True)):
            serial = gaussian_joint_scores(R, history.assignments, mobility, initial,
                schedule, model, .02, 3, shortcut_mass=1e-4, reset_each_step=reset)
            remote = pool.submit(api._score_task, (arm, 0)).result()
            assert remote["arm"] == arm and remote["path_index"] == 0
            for key in ("log_joint", "log_source", "source_updates", "shortcut"):
                np.testing.assert_array_equal(remote[key], serial[key].numpy())
            for key in ("projection_max_error", "covariance_projection_max_error"):
                assert remote[key] == serial[key]
