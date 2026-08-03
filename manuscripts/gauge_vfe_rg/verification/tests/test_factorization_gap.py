"""RED contract for stable Gaussian factorization gaps and a non-stub protocol."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import mpmath
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
    rho: float


def runner_module():
    spec = importlib.util.spec_from_file_location("gauge_vfe_rg_run_checks", RUNNER_PATH)
    assert spec and spec.loader, "DEFECT [runner import]: run_checks.py must be importable"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_runner_api(name: str, defect: str):
    value = getattr(runner_module(), name, None)
    assert callable(value), f"DEFECT [{defect}]: run_checks.py must export {name}"
    return value


def require_field(value, name: str, defect: str):
    assert hasattr(value, name), f"DEFECT [{defect}]: required field {name!r} is missing"
    return getattr(value, name)


def rho_for(index: int) -> float:
    # Identity-stable, nonconstant inputs that remain safely SPD.
    return 0.05 + 0.80 * ((index * 37 + 11) % 997) / 996


def frozen_cases() -> tuple[FrozenCase, ...]:
    cases: list[FrozenCase] = []
    for dimension in range(2, 17):
        for condition in CONDITIONS:
            for replica in range(20):
                index = len(cases)
                cases.append(FrozenCase(f"general-d{dimension}-c{condition:.0e}-r{replica:02d}", "general", dimension, condition, replica, rho_for(index)))
    for stratum, count in STRATUM_COUNTS.items():
        if stratum == "general":
            continue
        for replica in range(count):
            index = len(cases)
            cases.append(FrozenCase(f"{stratum}-{replica:03d}", stratum, 2 + replica % 15, CONDITIONS[replica % len(CONDITIONS)], replica, rho_for(index)))
    assert len(cases) == 3138, "DEFECT [frozen schedule]: exact case count must be 3138"
    return tuple(cases)


def spectral_witness(condition_number: float) -> np.ndarray:
    theta = math.pi / 7
    q = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    return q @ np.diag([1.0, 1.0 / condition_number]) @ q.T


def independent_gap_100_digits(case: FrozenCase) -> float:
    with mpmath.workdps(100):
        rho = mpmath.mpf(str(case.rho))
        return float(-mpmath.log1p(-(rho * rho)) / 2)


def result_value(result, defect: str) -> float:
    return require_field(result, "value", defect)


@pytest.mark.parametrize("epsilon", [1e-3, 1e-6, 1e-9])
def test_scalar_gap_uses_log1p(epsilon):
    lam = np.array([[1.0, epsilon], [epsilon, 1.0]])
    factorization_gap = require_runner_api("factorization_gap", "scalar log1p result contract")
    got = factorization_gap(lam, [[0], [1]])
    want = -0.5 * math.log1p(-(epsilon * epsilon))
    assert result_value(got, "scalar log1p result contract") == pytest.approx(want, rel=5e-12, abs=0.0), "DEFECT [scalar log1p result contract]: scalar oracle mismatch"


@pytest.mark.parametrize("condition_number", [1.0e4, 1.0e10, 1.0e14])
def test_spectrally_constructed_condition_witness_reaches_production_call(condition_number):
    lam = spectral_witness(condition_number)
    observed = np.linalg.cond(lam)
    assert observed == pytest.approx(condition_number, rel=2e-2), f"DEFECT [condition witness]: spectral condition {observed:.6e} is not near {condition_number:.6e}"
    got = require_runner_api("factorization_gap", f"condition-{condition_number:.0e} witness")(lam, [[0], [1]])
    assert result_value(got, f"condition-{condition_number:.0e} witness") >= 0.0, "DEFECT [condition witness]: SPD witness must reach the production call"


@pytest.mark.parametrize("partition", [[[0], [0, 1]], [[0], []], [[0]], [[0], [2]]])
def test_validate_partition_rejects_invalid_real_partitions(partition):
    validate_partition = require_runner_api("validate_partition", f"invalid partition {partition!r}")
    with pytest.raises((ValueError, TypeError)):
        validate_partition(np.eye(2), partition)


@pytest.mark.parametrize("bad_lam", [np.array([[1.0, 2.0], [0.0, 1.0]]), np.diag([1.0, -1.0]), np.array([[math.nan, 0.0], [0.0, 1.0]]), np.array([[math.inf, 0.0], [0.0, 1.0]])])
def test_factorization_api_rejects_nonsymmetric_non_spd_and_nonfinite_inputs(bad_lam):
    require_runner_api("GapResult", "invalid precision result type")
    factorization_gap = require_runner_api("factorization_gap", "invalid precision rejection")
    with pytest.raises((ValueError, TypeError)):
        factorization_gap(bad_lam, [[0], [1]])


def test_gap_steps_are_nonempty_and_have_load_bearing_numerical_diagnostics():
    lam = np.array([[2.0, 0.2, 0.1], [0.2, 3.0, 0.3], [0.1, 0.3, 4.0]])
    two = require_runner_api("two_block_factorization_gap", "two-block Schur API")(lam, [0], [1, 2])
    multi = require_runner_api("factorization_gap", "multiblock telescoping API")(lam, [[0], [1], [2]])
    for result, defect in ((two, "two-block diagnostics"), (multi, "multiblock diagnostics")):
        steps = require_field(result, "steps", defect)
        assert steps, f"DEFECT [{defect}]: GapResult.steps must be nonempty"
        merge_order = require_field(result, "merge_order", defect)
        assert merge_order, f"DEFECT [{defect}]: merge order must be nonempty"
        accumulated = require_field(result, "backward_error_bound", defect)
        assert accumulated >= 0.0, f"DEFECT [{defect}]: accumulated backward bound must be nonnegative"
        for step in steps:
            singular_values = require_field(step, "singular_values", defect)
            assert len(singular_values) > 0 and min(singular_values) > 0.0, f"DEFECT [{defect}]: singular values must be positive"
            min_one_minus_rho_squared = require_field(step, "min_one_minus_rho_squared", defect)
            assert min_one_minus_rho_squared > 0.0, f"DEFECT [{defect}]: 1-rho^2 must remain positive"
            assert require_field(step, "cholesky_residual", defect) >= 0.0, f"DEFECT [{defect}]: Cholesky residual must be reported"
            assert require_field(step, "backward_error", defect) <= accumulated, f"DEFECT [{defect}]: step error exceeds accumulated bound"
    assert result_value(multi, "multiblock telescoping") == pytest.approx(sum(result_value(step, "multiblock step") for step in require_field(multi, "steps", "multiblock diagnostics"))), "DEFECT [multiblock telescoping]: step values do not sum to result"


def test_ordinary_no_clip_and_out_of_tolerance_excursion_are_not_silently_accepted():
    ordinary = require_runner_api("factorization_gap", "ordinary no-clip")(
        np.array([[2.0, 0.1], [0.1, 2.0]]), [[0], [1]]
    )
    for step in require_field(ordinary, "steps", "ordinary no-clip"):
        assert require_field(step, "clipping_amount", "ordinary no-clip") == pytest.approx(0.0), "DEFECT [ordinary no-clip]: well-conditioned input must not clip"
    excursion = np.array([[1.0, 1.0 + 1e-10], [1.0 + 1e-10, 1.0]])
    with pytest.raises((ValueError, TypeError)):
        require_runner_api("factorization_gap", "out-of-tolerance excursion")(excursion, [[0], [1]])


def test_new_protocol_records_each_case_identity_nonconstant_oracle_and_repeats_exactly():
    schedule = frozen_cases()
    assert schedule == frozen_cases(), "DEFECT [frozen schedule]: schedule is not deterministic"
    assert {case.dimension for case in schedule} == set(range(2, 17)), "DEFECT [frozen schedule]: dimensions 2..16 missing"
    assert {name: sum(case.stratum == name for case in schedule) for name in STRATUM_COUNTS} == STRATUM_COUNTS, "DEFECT [frozen schedule]: per-stratum counts changed"
    digest = hashlib.sha256(json.dumps([asdict(case) for case in schedule], sort_keys=True).encode()).hexdigest()
    protocol = require_runner_api("run_factorization_gap_protocol", "frozen 3138-draw protocol")
    first, second = protocol(seed=PROTOCOL_SEED, schedule=schedule), protocol(seed=PROTOCOL_SEED, schedule=schedule)
    for report, label in ((first, "first"), (second, "second")):
        assert require_field(report, "protocol_name", f"{label} protocol identity") == "new-deterministic-factorization-gap-3138", f"DEFECT [{label} protocol identity]: wrong protocol label"
        assert require_field(report, "seed", f"{label} protocol identity") == PROTOCOL_SEED, f"DEFECT [{label} protocol identity]: seed mismatch"
        assert require_field(report, "schedule_digest", f"{label} protocol identity") == digest, f"DEFECT [{label} protocol identity]: schedule digest mismatch"
        assert require_field(report, "historical_generator_recovered", f"{label} protocol identity") is False, f"DEFECT [{label} protocol identity]: protocol must be explicitly new"
        records = require_field(report, "cases", f"{label} protocol execution")
        assert len(records) == len(schedule), f"DEFECT [{label} protocol execution]: must contain one actual record per case"
        by_id = {require_field(record, "case_id", f"{label} record identity"): record for record in records}
        assert set(by_id) == {case.case_id for case in schedule}, f"DEFECT [{label} record identity]: records do not match schedule identities"
        values = []
        for case in schedule:
            record = by_id[case.case_id]
            assert require_field(record, "stratum", f"{label} record identity") == case.stratum, f"DEFECT [{label} record identity]: stratum not bound to case"
            assert require_field(record, "input_digest", f"{label} record identity"), f"DEFECT [{label} record identity]: input digest is required"
            values.append(result_value(record, f"{label} record value"))
        assert len({round(value, 15) for value in values}) > 1, f"DEFECT [{label} nonconstant oracle]: constant/echo results are forbidden"
    assert require_field(first, "cases", "repeat equality") == require_field(second, "cases", "repeat equality"), "DEFECT [repeat equality]: same seed and schedule must yield identical records"


def test_protocol_representative_values_and_100_digit_controls_are_independent_and_case_bound():
    schedule = frozen_cases()
    report = require_runner_api("run_factorization_gap_protocol", "100-digit controls")(seed=PROTOCOL_SEED, schedule=schedule)
    records = {require_field(record, "case_id", "representative record"): record for record in require_field(report, "cases", "representative records")}
    representatives = (schedule[0], schedule[997], schedule[-1])
    for case in representatives:
        observed = result_value(records[case.case_id], "representative oracle")
        assert observed == pytest.approx(independent_gap_100_digits(case), rel=1e-12, abs=1e-15), f"DEFECT [representative oracle]: {case.case_id} disagrees with independent 100-digit value"
    controls = require_field(report, "high_precision_controls", "100-digit controls")
    selected = [case for case in schedule if case.stratum == "mpmath_100_digit"]
    assert len(controls) == len(selected), "DEFECT [100-digit controls]: every selected case needs an evaluated control"
    control_by_id = {require_field(control, "case_id", "100-digit control identity"): control for control in controls}
    assert set(control_by_id) == {case.case_id for case in selected}, "DEFECT [100-digit controls]: controls are not case-bound"
    for case in selected:
        control = control_by_id[case.case_id]
        assert require_field(control, "decimal_digits", "100-digit controls") == 100, "DEFECT [100-digit controls]: precision must be exactly 100"
        assert float(require_field(control, "reference_value", "100-digit controls")) == pytest.approx(independent_gap_100_digits(case), rel=1e-12), "DEFECT [100-digit controls]: reference is not independent"
