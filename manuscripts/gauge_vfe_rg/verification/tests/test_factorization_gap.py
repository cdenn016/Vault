"""Red contract for stable Gaussian factorization gaps and their frozen protocol."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import pytest


RUNNER_PATH = Path(__file__).resolve().parents[1] / "run_checks.py"
PROTOCOL_SEED = 20260803
CONDITIONS = (1.0, 1.0e2, 1.0e4, 1.0e6, 1.0e8, 1.0e10, 1.0e12, 1.0e14)
STRATUM_COUNTS = {
    "general": 2400,
    "exact_block_diagonal": 200,
    "near_decoupled": 200,
    "scale": 120,
    "permutation": 120,
    "nested_refinement": 80,
    "mpmath_100_digit": 18,
}


@dataclass(frozen=True)
class FrozenCase:
    case_id: str
    stratum: str
    dimension: int
    condition_number: float
    replica: int


def runner_module():
    spec = importlib.util.spec_from_file_location("gauge_vfe_rg_run_checks", RUNNER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_runner_api(name: str, defect: str):
    value = getattr(runner_module(), name, None)
    assert callable(value), f"DEFECT [{defect}]: run_checks.py must export {name}"
    return value


def frozen_cases() -> tuple[FrozenCase, ...]:
    cases: list[FrozenCase] = []
    for dimension in range(2, 17):
        for condition in CONDITIONS:
            for replica in range(20):
                cases.append(FrozenCase(f"general-d{dimension}-c{condition:.0e}-r{replica:02d}", "general", dimension, condition, replica))
    for stratum, count in STRATUM_COUNTS.items():
        if stratum == "general":
            continue
        for index in range(count):
            cases.append(FrozenCase(f"{stratum}-{index:03d}", stratum, 2 + index % 15, CONDITIONS[index % len(CONDITIONS)], index))
    assert len(cases) == 3138
    return tuple(cases)


def spectral_witness(condition_number: float) -> np.ndarray:
    theta = math.pi / 7
    q = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    return q @ np.diag([1.0, 1.0 / condition_number]) @ q.T


def result_value(result, defect: str) -> float:
    assert hasattr(result, "value"), f"DEFECT [{defect}]: factorization_gap must return GapResult.value, not {type(result).__name__}"
    return result.value


@pytest.mark.parametrize("epsilon", [1e-3, 1e-6, 1e-9])
def test_scalar_gap_uses_log1p(epsilon):
    lam = np.array([[1.0, epsilon], [epsilon, 1.0]])
    factorization_gap = require_runner_api("factorization_gap", "scalar log1p result contract")
    got = factorization_gap(lam, [[0], [1]])
    want = -0.5 * math.log1p(-(epsilon * epsilon))
    assert result_value(got, "scalar log1p result contract") == pytest.approx(want, rel=5e-12, abs=0.0)


@pytest.mark.parametrize("condition_number", [1.0e4, 1.0e10, 1.0e14])
def test_spectrally_constructed_condition_witness_has_declared_condition(condition_number):
    lam = spectral_witness(condition_number)
    assert np.linalg.cond(lam) == pytest.approx(condition_number, rel=2e-12)
    got = require_runner_api("factorization_gap", f"condition-{condition_number:.0e} witness")(lam, [[0], [1]])
    assert result_value(got, f"condition-{condition_number:.0e} witness") >= 0.0


@pytest.mark.parametrize("partition", [[[0], [0, 1]], [[0], []], [[0]], [[0], [2]]])
def test_validate_partition_rejects_invalid_real_partitions(partition):
    lam = np.eye(2)
    validate_partition = require_runner_api("validate_partition", f"invalid partition {partition!r}")
    with pytest.raises((ValueError, TypeError)):
        validate_partition(lam, partition)


@pytest.mark.parametrize("bad_lam", [np.array([[1.0, 2.0], [0.0, 1.0]]), np.diag([1.0, -1.0]), np.array([[math.nan, 0.0], [0.0, 1.0]]), np.array([[math.inf, 0.0], [0.0, 1.0]])])
def test_factorization_api_rejects_nonsymmetric_non_spd_and_nonfinite_inputs(bad_lam):
    require_runner_api("GapResult", "invalid precision result type")
    factorization_gap = require_runner_api("factorization_gap", "invalid precision rejection")
    with pytest.raises((ValueError, TypeError)):
        factorization_gap(bad_lam, [[0], [1]])


def test_two_block_and_multiblock_results_expose_steps_merge_order_and_clipping_diagnostics():
    lam = np.array([[2.0, 0.2, 0.1], [0.2, 3.0, 0.3], [0.1, 0.3, 4.0]])
    two_block = require_runner_api("two_block_factorization_gap", "two-block Schur API")
    factorization_gap = require_runner_api("factorization_gap", "multiblock telescoping API")
    two = two_block(lam, [0], [1, 2])
    multi = factorization_gap(lam, [[0], [1], [2]])
    for result, defect in ((two, "two-block diagnostics"), (multi, "multiblock diagnostics")):
        assert hasattr(result, "steps"), f"DEFECT [{defect}]: GapResult.steps is required"
        assert hasattr(result, "merge_order"), f"DEFECT [{defect}]: GapResult.merge_order is required"
        assert hasattr(result, "backward_error_bound"), f"DEFECT [{defect}]: GapResult.backward_error_bound is required"
    assert result_value(multi, "multiblock telescoping") == pytest.approx(sum(step.value for step in multi.steps))


def test_gap_result_and_step_contracts_reject_out_of_bound_clipping_and_preserve_legal_clipping_diagnostics():
    gap_step = require_runner_api("GapStep", "GapStep public type")
    gap_result = require_runner_api("GapResult", "GapResult public type")
    assert gap_step is not None and gap_result is not None
    report = require_runner_api("factorization_gap", "residual-derived clipping")(np.array([[2.0, 0.1], [0.1, 2.0]]), [[0], [1]])
    for step in getattr(report, "steps", ()):
        assert step.clipping_amount <= step.residual_derived_clip_bound, "DEFECT [residual-derived clipping]: clipping exceeded its derived bound"


def test_new_protocol_schedule_is_explicit_reproducible_totals_3138_and_executes_each_case_twice():
    first, second = frozen_cases(), frozen_cases()
    assert first == second
    assert len(first) == 3138
    assert {case.dimension for case in first} == set(range(2, 17))
    assert max(case.condition_number for case in first) == 1.0e14
    assert {name: sum(case.stratum == name for case in first) for name in STRATUM_COUNTS} == STRATUM_COUNTS
    digest = hashlib.sha256(json.dumps([asdict(case) for case in first], sort_keys=True).encode()).hexdigest()
    assert digest == hashlib.sha256(json.dumps([asdict(case) for case in second], sort_keys=True).encode()).hexdigest()
    protocol = require_runner_api("run_factorization_gap_protocol", "frozen 3138-draw protocol")
    first_report = protocol(seed=PROTOCOL_SEED, schedule=first)
    second_report = protocol(seed=PROTOCOL_SEED, schedule=second)
    for report, label in ((first_report, "first"), (second_report, "second")):
        assert getattr(report, "protocol_name", None) == "new-deterministic-factorization-gap-3138", f"DEFECT [{label} protocol identity]: wrong protocol label"
        assert getattr(report, "historical_generator_recovered", None) is False, f"DEFECT [{label} protocol identity]: must be explicitly new"
        assert len(getattr(report, "cases", ())) == len(first), f"DEFECT [{label} protocol execution]: report must contain one actual record per case"
    assert first_report.cases == second_report.cases


def test_protocol_uses_selected_100_digit_mpmath_controls_independently_of_float_summary():
    schedule = tuple(case for case in frozen_cases() if case.stratum == "mpmath_100_digit")
    protocol = require_runner_api("run_factorization_gap_protocol", "100-digit controls")
    report = protocol(seed=PROTOCOL_SEED, schedule=schedule)
    controls = getattr(report, "high_precision_controls", None)
    assert controls is not None, "DEFECT [100-digit controls]: report must expose evaluated controls"
    assert len(controls) == len(schedule), "DEFECT [100-digit controls]: constant summary is not an evaluation"
    assert all(control.decimal_digits == 100 and control.reference_value is not None for control in controls), "DEFECT [100-digit controls]: every selected case needs an actual mpmath reference"
