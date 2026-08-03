"""Red specification for the stable Gaussian factorization-gap protocol."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import numpy as np
import pytest


VERIFICATION_DIR = Path(__file__).resolve().parents[1]
RUNNER_PATH = VERIFICATION_DIR / "run_checks.py"


def runner_module():
    spec = importlib.util.spec_from_file_location("gauge_vfe_rg_run_checks", RUNNER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


factorization_gap = runner_module().factorization_gap


@pytest.mark.parametrize("epsilon", [1e-3, 1e-6, 1e-9])
def test_scalar_gap_uses_log1p(epsilon):
    lam = np.array([[1.0, epsilon], [epsilon, 1.0]])
    got = factorization_gap(lam, [[0], [1]])
    want = -0.5 * math.log1p(-(epsilon * epsilon))
    assert got.value == pytest.approx(want, rel=5e-12, abs=0.0)


def test_high_condition_witness_reports_nonnegative_log1p_gap():
    """A relative calculation must not turn a valid gap negative at condition 1e14."""
    lam = np.array([[1.0e14, 1.0e7 * (1.0 - 1.0e-10)], [1.0e7 * (1.0 - 1.0e-10), 1.0]])
    got = factorization_gap(lam, [[0], [1]])
    assert got.value >= 0.0
    assert got.algorithm == "schur-canonical-correlation-log1p"
    assert got.relative_error_bound > 0.0


def test_new_3138_draw_protocol_is_frozen_and_not_historical_recovery():
    module = runner_module()
    assert hasattr(module, "run_factorization_gap_protocol"), "missing deterministic protocol interface"
    report = module.run_factorization_gap_protocol()
    assert report.protocol_name == "new-deterministic-factorization-gap-3138"
    assert report.historical_generator_recovered is False
    assert report.draw_count == 3138
    assert report.dimensions == tuple(range(2, 17))
    assert report.maximum_condition_number == 1e14
    assert report.negative_gap_count == 0


def test_protocol_covers_declared_controls_and_selected_100_digit_references():
    module = runner_module()
    assert hasattr(module, "run_factorization_gap_protocol"), "missing deterministic protocol interface"
    report = module.run_factorization_gap_protocol()
    assert set(report.control_kinds) >= {
        "exact_block_diagonal",
        "near_decoupled",
        "scale",
        "permutation",
        "nested_refinement",
    }
    assert report.reference_precision_decimal_digits == 100
    assert report.selected_high_precision_controls > 0
    assert report.maximum_reference_relative_error <= report.reference_relative_tolerance
