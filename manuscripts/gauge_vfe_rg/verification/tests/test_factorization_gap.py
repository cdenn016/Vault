"""RED contract for stable Gaussian factorization gaps and a non-stub protocol."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
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
    matrix_seed: int
    partition: tuple[tuple[int, ...], ...]


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


def require_mapping_field(value, name: str, defect: str):
    assert isinstance(value, dict), f"DEFECT [{defect}]: expected a mapping"
    assert name in value, f"DEFECT [{defect}]: required field {name!r} is missing"
    return value[name]


def case_seed(case_id: str, dimension: int, condition_number: float, stratum: str) -> int:
    material = f"{PROTOCOL_SEED}|{case_id}|{dimension}|{condition_number:.17g}|{stratum}".encode()
    return int.from_bytes(hashlib.sha256(material).digest()[:8], "big", signed=False)


def partition_for(dimension: int, stratum: str) -> tuple[tuple[int, ...], ...]:
    if stratum == "nested_refinement" and dimension >= 3:
        cut = max(1, dimension // 3)
        return (tuple(range(cut)), tuple(range(cut, 2 * cut)), tuple(range(2 * cut, dimension)))
    cut = dimension // 2
    return (tuple(range(cut)), tuple(range(cut, dimension)))


def make_case(case_id: str, stratum: str, dimension: int, condition_number: float, replica: int) -> FrozenCase:
    return FrozenCase(case_id, stratum, dimension, condition_number, replica, case_seed(case_id, dimension, condition_number, stratum), partition_for(dimension, stratum))


def regenerate_matrix_and_partition(case: FrozenCase) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    """Independent test oracle: all numerical inputs come from frozen identity fields."""
    seed = case_seed(case.case_id, case.dimension, case.condition_number, case.stratum)
    assert seed == case.matrix_seed, "DEFECT [case matrix seed]: frozen case has an unbound matrix seed"
    rng = np.random.default_rng(seed)
    spectrum = np.geomspace(1.0, 1.0 / case.condition_number, case.dimension)
    partition = partition_for(case.dimension, case.stratum)
    if case.stratum == "exact_block_diagonal":
        blocks = []
        for indices in partition:
            q, _ = np.linalg.qr(rng.standard_normal((len(indices), len(indices))))
            blocks.append(q @ np.diag(np.geomspace(1.0, 1.0 / case.condition_number, len(indices))) @ q.T)
        matrix = np.zeros((case.dimension, case.dimension))
        offset = 0
        for block in blocks:
            size = block.shape[0]
            matrix[offset:offset + size, offset:offset + size] = block
            offset += size
    else:
        q, _ = np.linalg.qr(rng.standard_normal((case.dimension, case.dimension)))
        matrix = q @ np.diag(spectrum) @ q.T
        if case.stratum == "near_decoupled":
            # Blend with the block diagonal while retaining a positive-definite convex combination.
            block = np.zeros_like(matrix)
            for indices in partition:
                block[np.ix_(indices, indices)] = matrix[np.ix_(indices, indices)]
            matrix = 0.999 * block + 0.001 * matrix + np.eye(case.dimension) * 1e-12
        elif case.stratum == "scale":
            matrix *= 10.0 ** ((case.replica % 7) - 3)
        elif case.stratum == "permutation":
            permutation = rng.permutation(case.dimension)
            matrix = matrix[np.ix_(permutation, permutation)]
            # New coordinate j contains old coordinate permutation[j], so an
            # old block moves through P^{-1}, not through P.
            inverse_permutation = np.argsort(permutation)
            original_partition = partition
            partition = tuple(
                tuple(sorted(int(inverse_permutation[index]) for index in indices))
                for indices in original_partition
            )
            assert all(
                {int(permutation[index]) for index in moved_indices} == set(original_indices)
                for original_indices, moved_indices in zip(original_partition, partition)
            ), "DEFECT [permutation coordinate map]: inverse permutation does not preserve original blocks"
    matrix = (matrix + matrix.T) / 2.0
    np.linalg.cholesky(matrix)
    return matrix, partition


def matrix_digest(matrix: np.ndarray) -> str:
    return hashlib.sha256(np.ascontiguousarray(matrix, dtype=np.float64).tobytes()).hexdigest()


def partition_digest(partition: tuple[tuple[int, ...], ...]) -> str:
    return hashlib.sha256(json.dumps(partition, separators=(",", ":")).encode()).hexdigest()


def independent_matrix_gap(matrix: np.ndarray, partition: tuple[tuple[int, ...], ...], digits: int = 100) -> float:
    with mpmath.workdps(digits):
        whole = mpmath.log(mpmath.det(mpmath.matrix(matrix.tolist())))
        block_terms = []
        for indices in partition:
            block_terms.append(mpmath.log(mpmath.det(mpmath.matrix(matrix[np.ix_(indices, indices)].tolist()))))
        return float((sum(block_terms) - whole) / 2)


def frozen_cases() -> tuple[FrozenCase, ...]:
    cases: list[FrozenCase] = []
    for dimension in range(2, 17):
        for condition in CONDITIONS:
            for replica in range(20):
                case_id = f"general-d{dimension}-c{condition:.0e}-r{replica:02d}"
                cases.append(make_case(case_id, "general", dimension, condition, replica))
    for stratum, count in STRATUM_COUNTS.items():
        if stratum == "general":
            continue
        for replica in range(count):
            dimension = 2 + replica % 15
            condition = CONDITIONS[replica % len(CONDITIONS)]
            cases.append(make_case(f"{stratum}-{replica:03d}", stratum, dimension, condition, replica))
    assert len(cases) == 3138, "DEFECT [frozen schedule]: exact case count must be 3138"
    return tuple(cases)


def spectral_witness(condition_number: float) -> np.ndarray:
    theta = math.pi / 7
    q = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    return q @ np.diag([1.0, 1.0 / condition_number]) @ q.T


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


def test_extreme_finite_spd_block_diagonals_and_huge_correlated_scale_remain_valid():
    factorization_gap = require_runner_api(
        "factorization_gap", "extreme finite SPD inputs"
    )
    exact_block_diagonals = {
        "huge": np.diag([1.0e308, 1.0e308]),
        "subnormal": np.diag([1.0, np.nextafter(0.0, 1.0)]),
    }
    for label, matrix in exact_block_diagonals.items():
        assert np.all(np.isfinite(matrix)), f"DEFECT [{label} SPD fixture]: fixture must be finite"
        np.linalg.cholesky(matrix)
        try:
            result = factorization_gap(matrix, [[0], [1]])
        except (ValueError, TypeError, FloatingPointError, np.linalg.LinAlgError) as exc:
            pytest.fail(f"DEFECT [{label} finite SPD]: production rejected a finite positive-definite input: {type(exc).__name__}: {exc}")
        observed = result_value(result, f"{label} finite SPD")
        assert math.isfinite(observed), f"DEFECT [{label} finite SPD]: exact block-diagonal gap must be finite"
        assert observed == 0.0, f"DEFECT [{label} finite SPD]: exact block-diagonal gap must be exactly zero"

    correlation = 0.25
    ordinary = np.array([[1.0, correlation], [correlation, 1.0]])
    huge = 8.0e307 * ordinary
    assert np.all(np.isfinite(huge)), "DEFECT [huge correlated fixture]: scaled fixture must remain finite"
    expected = -0.5 * math.log1p(-(correlation * correlation))
    ordinary_gap = result_value(
        factorization_gap(ordinary, [[0], [1]]), "ordinary correlated scale"
    )
    huge_gap = result_value(
        factorization_gap(huge, [[0], [1]]), "huge correlated scale"
    )
    assert math.isfinite(huge_gap), "DEFECT [huge correlated scale]: scalar gap must be finite"
    assert ordinary_gap == pytest.approx(expected, rel=5e-12, abs=0.0), "DEFECT [ordinary correlated scale]: scalar oracle mismatch"
    assert huge_gap == pytest.approx(expected, rel=5e-12, abs=0.0), "DEFECT [huge correlated scale]: factorization gap must be invariant under finite positive scaling"


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


WITHIN_BOUND_CLIP_WITNESS = np.array([
    [0.012995137302571503, -0.08809796529646897, -0.01062753379868217, 0.07034656148572713],
    [-0.08809796529646897, 0.5974163750322803, 0.07207680102574178, -0.47702552029541695],
    [-0.01062753379868217, 0.07207680102574178, 0.008696311837782767, -0.05755126421432782],
    [0.07034656148572713, -0.47702552029541695, -0.05755126421432782, 0.3808968174377439],
])


def exact_binary64_matrix(matrix: np.ndarray) -> list[list[Fraction]]:
    """Interpret each frozen binary64 entry as its exact rational value."""
    return [[Fraction.from_float(float(entry)) for entry in row] for row in matrix]


def exact_determinant(matrix: list[list[Fraction]]) -> Fraction:
    """Small exact determinant used only for the fixed 4-by-4 witness."""
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        ((-1) ** column)
        * matrix[0][column]
        * exact_determinant([row[:column] + row[column + 1:] for row in matrix[1:]])
        for column in range(len(matrix))
    )


def exact_leading_principal_minors(matrix: list[list[Fraction]]) -> tuple[Fraction, ...]:
    return tuple(
        exact_determinant([row[:order] for row in matrix[:order]])
        for order in range(1, len(matrix) + 1)
    )


def exact_inverse_2x2(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    determinant = exact_determinant(matrix)
    return [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]


def exact_matmul(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [
        [
            sum(
                (left[row][inner] * right[inner][column] for inner in range(len(right))),
                Fraction(0),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def exact_transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def exact_subtract(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [
        [left[row][column] - right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def mpmath_fraction(value: Fraction) -> mpmath.mpf:
    return mpmath.mpf(value.numerator) / value.denominator


def outward_float_upper(value: Fraction) -> float:
    """Round a positive exact rational upward to a binary64 upper bound."""
    rounded = float(value)
    if Fraction.from_float(rounded) < value:
        rounded = math.nextafter(rounded, math.inf)
    return rounded


def canonical_correlation_clip_certificate(matrix: np.ndarray) -> dict[str, object]:
    """Build an exact, witness-specific forward-error certificate.

    This deliberately does not claim a general Cholesky/solve residual theorem.
    Every binary64 input is treated as an exact rational.  For the fixed 2+2
    partition, the squared canonical correlations are the eigenvalues of
    A^{-1} C D^{-1} C^T, so their characteristic polynomial is exactly
    x^2 - trace*x + determinant.  An integer-square-root enclosure of its
    discriminant isolates the larger root to 180 decimal places.
    """
    exact = exact_binary64_matrix(matrix)
    first = [row[:2] for row in exact[:2]]
    second = [row[2:] for row in exact[2:]]
    cross = [row[2:] for row in exact[:2]]
    first_inverse = exact_inverse_2x2(first)
    second_inverse = exact_inverse_2x2(second)
    full_principal_minors = exact_leading_principal_minors(exact)
    first_principal_minors = exact_leading_principal_minors(first)
    second_principal_minors = exact_leading_principal_minors(second)
    schur = exact_subtract(
        first,
        exact_matmul(exact_matmul(cross, second_inverse), exact_transpose(cross)),
    )
    canonical_squared = exact_matmul(
        exact_matmul(exact_matmul(first_inverse, cross), second_inverse),
        exact_transpose(cross),
    )
    trace = canonical_squared[0][0] + canonical_squared[1][1]
    determinant = exact_determinant(canonical_squared)
    discriminant = trace * trace - 4 * determinant

    decimal_digits = 180
    scale = 10**decimal_digits
    scaled_discriminant_floor = (
        discriminant.numerator * scale * scale // discriminant.denominator
    )
    sqrt_floor = math.isqrt(scaled_discriminant_floor)
    sqrt_lower = Fraction(sqrt_floor, scale)
    sqrt_upper = Fraction(sqrt_floor + 1, scale)
    rho_squared_lower = (trace + sqrt_lower) / 2
    rho_squared_upper = (trace + sqrt_upper) / 2

    first_float, second_float, cross_float = (
        matrix[:2, :2],
        matrix[2:, 2:],
        matrix[:2, 2:],
    )
    left = np.linalg.cholesky(first_float)
    right = np.linalg.cholesky(second_float)
    canonical_float = (
        np.linalg.solve(left, cross_float)
        @ np.linalg.solve(right, np.eye(2)).T
    )
    rho = float(np.linalg.svd(canonical_float, compute_uv=False)[0])
    rho_squared = rho * rho
    rho_squared_exact_float = Fraction.from_float(rho_squared)
    forward_error_lower = rho_squared_exact_float - rho_squared_upper
    forward_error_upper = rho_squared_exact_float - rho_squared_lower

    mpmath_digits = 200
    with mpmath.workdps(mpmath_digits):
        high_precision_rho_squared = (
            mpmath_fraction(trace) + mpmath.sqrt(mpmath_fraction(discriminant))
        ) / 2
        mpmath_agrees_with_exact_enclosure = (
            mpmath_fraction(rho_squared_lower)
            <= high_precision_rho_squared
            < mpmath_fraction(rho_squared_upper)
        )
        # This value oracle is distinct from the clipping license above.  It
        # evaluates the exact binary64 input determinants at high precision,
        # so a finite but badly biased value after clipping is still rejected.
        high_precision_gap = (
            mpmath.log(mpmath_fraction(first_principal_minors[-1]))
            + mpmath.log(mpmath_fraction(second_principal_minors[-1]))
            - mpmath.log(mpmath_fraction(full_principal_minors[-1]))
        ) / 2
        high_precision_gap_float = float(high_precision_gap)
        high_precision_gap_decimal = mpmath.nstr(
            high_precision_gap, n=mpmath_digits
        )

    return {
        "decimal_digits": decimal_digits,
        "mpmath_digits": mpmath_digits,
        "full_principal_minors": full_principal_minors,
        "first_principal_minors": first_principal_minors,
        "second_principal_minors": second_principal_minors,
        "schur_principal_minors": exact_leading_principal_minors(schur),
        "characteristic_trace": trace,
        "characteristic_determinant": determinant,
        "characteristic_discriminant": discriminant,
        "characteristic_at_one": Fraction(1) - trace + determinant,
        "sqrt_discriminant_lower": sqrt_lower,
        "sqrt_discriminant_upper": sqrt_upper,
        "rho_squared_lower": rho_squared_lower,
        "rho_squared_upper": rho_squared_upper,
        "mpmath_agrees_with_exact_enclosure": mpmath_agrees_with_exact_enclosure,
        "high_precision_gap": high_precision_gap_float,
        "high_precision_gap_decimal": high_precision_gap_decimal,
        "rho": rho,
        "rho_squared": rho_squared,
        "rho_squared_excess": max(0.0, rho_squared - 1.0),
        "forward_error_lower": forward_error_lower,
        "forward_error_upper": forward_error_upper,
        "forward_error_upper_float": outward_float_upper(forward_error_upper),
    }


def test_ordinary_no_clip_within_bound_clip_and_out_of_tolerance_excursion_are_not_silently_accepted():
    certificate = canonical_correlation_clip_certificate(WITHIN_BOUND_CLIP_WITNESS)
    exact_spd_minors = (
        certificate["full_principal_minors"],
        certificate["first_principal_minors"],
        certificate["second_principal_minors"],
        certificate["schur_principal_minors"],
    )
    assert all(all(minor > 0 for minor in minors) for minors in exact_spd_minors), "DEFECT [within-bound clipping fixture]: exact binary64 matrix, blocks, and Schur complement must be SPD by Sylvester's criterion"
    assert certificate["characteristic_discriminant"] > 0 and 0 <= certificate["characteristic_determinant"] and 0 <= certificate["characteristic_trace"] < 2 and certificate["characteristic_at_one"] > 0, "DEFECT [within-bound clipping fixture]: exact characteristic polynomial must place both canonical rho^2 roots below one"
    assert certificate["sqrt_discriminant_lower"] ** 2 <= certificate["characteristic_discriminant"] < certificate["sqrt_discriminant_upper"] ** 2, "DEFECT [within-bound clipping fixture]: integer-square-root bounds do not enclose the exact discriminant root"
    assert certificate["decimal_digits"] >= 150 and certificate["rho_squared_upper"] - certificate["rho_squared_lower"] <= Fraction(1, 10**150), "DEFECT [within-bound clipping fixture]: exact rho^2 enclosure must resolve at least 150 decimal places"
    assert certificate["mpmath_digits"] >= 200 and certificate["mpmath_agrees_with_exact_enclosure"] is True, "DEFECT [within-bound clipping fixture]: corroborating 200-digit mpmath rho^2 must lie in the exact rational enclosure"
    assert math.isfinite(certificate["high_precision_gap"]) and certificate["high_precision_gap"] > 0, "DEFECT [within-bound clipping fixture]: 200-digit exact-input determinant-gap oracle must be finite and positive"
    assert 0 <= certificate["rho_squared_lower"] < certificate["rho_squared_upper"] < 1, "DEFECT [within-bound clipping fixture]: exact canonical rho^2 must be strictly below one"
    rho = certificate["rho"]
    rho_squared_excess = certificate["rho_squared_excess"]
    independent_bound = certificate["forward_error_upper_float"]
    assert certificate["forward_error_lower"] > 0 and Fraction.from_float(independent_bound) >= certificate["forward_error_upper"], "DEFECT [within-bound clipping fixture]: binary64-to-exact rho^2 discrepancy must have an outward-rounded witness-specific bound"
    assert rho > 1.0 and 0.0 < rho_squared_excess <= independent_bound, "DEFECT [within-bound clipping fixture]: exact-SPD witness must produce a positive but independently certified binary64 excursion"
    ordinary = require_runner_api("factorization_gap", "ordinary no-clip")(
        np.array([[2.0, 0.1], [0.1, 2.0]]), [[0], [1]]
    )
    for step in require_field(ordinary, "steps", "ordinary no-clip"):
        assert require_field(step, "clipping_amount", "ordinary no-clip") == pytest.approx(0.0), "DEFECT [ordinary no-clip]: well-conditioned input must not clip"
        assert require_field(step, "clipping_applied", "ordinary no-clip") is False, "DEFECT [ordinary no-clip]: clipping_applied must be false"
    admitted = require_runner_api("factorization_gap", "within-bound clipping")(WITHIN_BOUND_CLIP_WITNESS, [[0, 1], [2, 3]])
    steps = require_field(admitted, "steps", "within-bound clipping")
    assert steps, "DEFECT [within-bound clipping]: admitted witness needs a nonempty diagnostic step list"
    for step in steps:
        clipping = require_field(step, "clipping_amount", "within-bound clipping")
        bound = require_field(step, "residual_derived_clip_bound", "within-bound clipping")
        assert require_field(step, "clipping_applied", "within-bound clipping") is True, "DEFECT [within-bound clipping]: clipping must be explicitly reported"
        assert math.isfinite(clipping) and clipping > 0.0, "DEFECT [within-bound clipping]: clipping amount must be positive and finite"
        assert rho_squared_excess <= clipping <= bound, "DEFECT [within-bound clipping]: clipping amount is inconsistent with measured rho^2-1 or exceeds its reported allowance"
        # The field retains the planned public name, but this test licenses it
        # only against the frozen witness's exact forward discrepancy; it is
        # not evidence for a general residual-derived perturbation theorem.
        assert rho_squared_excess <= bound <= independent_bound, "DEFECT [within-bound clipping]: reported allowance exceeds the exact witness-specific forward-error certificate"
        assert math.isfinite(require_field(step, "min_one_minus_rho_squared", "within-bound clipping")) and require_field(step, "min_one_minus_rho_squared", "within-bound clipping") > 0.0, "DEFECT [within-bound clipping]: post-clip log1p domain must be finite and positive"
        assert math.isfinite(result_value(step, "within-bound clipping")), "DEFECT [within-bound clipping]: clipped step value must be finite"
    admitted_value = result_value(admitted, "within-bound clipping")
    assert math.isfinite(admitted_value), "DEFECT [within-bound clipping]: clipped total gap must be finite"
    assert admitted_value == pytest.approx(certificate["high_precision_gap"], rel=5e-12, abs=math.ulp(certificate["high_precision_gap"])), "DEFECT [within-bound clipping]: finite clipped value disagrees with the 200-digit exact-input determinant-gap oracle"
    excursion = np.array([[1.0, 1.0 + 1e-10], [1.0 + 1e-10, 1.0]])
    excursion_cross = Fraction.from_float(float(excursion[0, 1]))
    assert excursion_cross * excursion_cross - 1 > certificate["forward_error_upper"], "DEFECT [out-of-tolerance excursion fixture]: rejected excursion must materially exceed the witness-specific certificate"
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
            matrix, partition = regenerate_matrix_and_partition(case)
            assert require_field(record, "matrix_digest", f"{label} record identity") == matrix_digest(matrix), f"DEFECT [{label} record identity]: matrix digest does not bind regenerated input"
            assert require_field(record, "partition_digest", f"{label} record identity") == partition_digest(partition), f"DEFECT [{label} record identity]: partition digest does not bind regenerated input"
            values.append(result_value(record, f"{label} record value"))
        assert len({round(value, 15) for value in values}) > 1, f"DEFECT [{label} nonconstant oracle]: constant/echo results are forbidden"
    assert require_field(first, "cases", "repeat equality") == require_field(second, "cases", "repeat equality"), "DEFECT [repeat equality]: same seed and schedule must yield identical records"


def test_protocol_all_3138_matrix_values_and_100_digit_controls_are_independent_and_case_bound():
    schedule = frozen_cases()
    report = require_runner_api("run_factorization_gap_protocol", "100-digit controls")(seed=PROTOCOL_SEED, schedule=schedule)
    records = {require_field(record, "case_id", "full protocol record"): record for record in require_field(report, "cases", "full protocol records")}
    assert set(records) == {case.case_id for case in schedule}, "DEFECT [full protocol oracle]: protocol records are not case-bound"
    observed_coverage = {(case.stratum, case.dimension, case.condition_number) for case in schedule}
    for stratum in STRATUM_COUNTS:
        assert {dimension for observed_stratum, dimension, _ in observed_coverage if observed_stratum == stratum} == set(range(2, 17)), f"DEFECT [full protocol oracle]: {stratum} omits a declared dimension"
        assert {condition for observed_stratum, _, condition in observed_coverage if observed_stratum == stratum} == set(CONDITIONS), f"DEFECT [full protocol oracle]: {stratum} omits a declared condition tier"
    for case in schedule:
        record = records[case.case_id]
        observed = result_value(record, "full protocol oracle")
        matrix, partition = regenerate_matrix_and_partition(case)
        assert require_field(record, "matrix_digest", "full protocol oracle") == matrix_digest(matrix), f"DEFECT [full protocol oracle]: {case.case_id} uses a different matrix"
        assert require_field(record, "partition_digest", "full protocol oracle") == partition_digest(partition), f"DEFECT [full protocol oracle]: {case.case_id} uses a different partition"
        expected = independent_matrix_gap(matrix, partition)
        assert math.isfinite(observed), f"DEFECT [full protocol oracle]: {case.case_id} emitted a nonfinite scalar"
        assert observed == pytest.approx(expected, rel=1e-4, abs=2e-8), f"DEFECT [full protocol oracle]: {case.case_id} disagrees with its independent matrix-based 100-digit value"
    controls = require_field(report, "high_precision_controls", "100-digit controls")
    selected = [case for case in schedule if case.stratum == "mpmath_100_digit"]
    assert len(controls) == len(selected), "DEFECT [100-digit controls]: every selected case needs an evaluated control"
    control_by_id = {require_field(control, "case_id", "100-digit control identity"): control for control in controls}
    assert set(control_by_id) == {case.case_id for case in selected}, "DEFECT [100-digit controls]: controls are not case-bound"
    for case in selected:
        control = control_by_id[case.case_id]
        assert require_field(control, "decimal_digits", "100-digit controls") == 100, "DEFECT [100-digit controls]: precision must be exactly 100"
        matrix, partition = regenerate_matrix_and_partition(case)
        assert float(require_field(control, "reference_value", "100-digit controls")) == pytest.approx(independent_matrix_gap(matrix, partition), rel=1e-11), "DEFECT [100-digit controls]: reference is not independent"


def test_protocol_records_independently_recomputed_achieved_condition_numbers():
    schedule = frozen_cases()
    report = require_runner_api(
        "run_factorization_gap_protocol", "achieved condition provenance"
    )(seed=PROTOCOL_SEED, schedule=schedule)
    records = {
        require_field(record, "case_id", "achieved condition provenance"): record
        for record in require_field(report, "cases", "achieved condition provenance")
    }
    achieved_by_id: dict[str, float] = {}
    for case in schedule:
        record = records[case.case_id]
        # This legacy field is the requested schedule tier, not evidence that
        # the regenerated binary64 matrix attained that condition number.
        assert require_field(record, "condition_number", "nominal condition tier") == case.condition_number, f"DEFECT [nominal condition tier]: {case.case_id} lost its scheduled condition tier"
        matrix, _ = regenerate_matrix_and_partition(case)
        assert require_field(record, "matrix_digest", "achieved condition provenance") == matrix_digest(matrix), f"DEFECT [achieved condition provenance]: {case.case_id} is not bound to its regenerated matrix"
        achieved = float(np.linalg.cond(matrix))
        reported = float(
            require_field(record, "achieved_condition_number", "achieved condition provenance")
        )
        assert math.isfinite(reported), f"DEFECT [achieved condition provenance]: {case.case_id} reported a nonfinite achieved condition number"
        assert reported == pytest.approx(achieved, rel=5e-13, abs=0.0), f"DEFECT [achieved condition provenance]: {case.case_id} does not match np.linalg.cond of its digest-bound regenerated matrix"
        achieved_by_id[case.case_id] = achieved

    assert max(achieved_by_id.values()) == pytest.approx(1.0e14, rel=2e-2), "DEFECT [achieved condition coverage]: the protocol does not globally exercise an achieved condition near 1e14"
    assert achieved_by_id["exact_block_diagonal-015"] == pytest.approx(1.0), "DEFECT [nominal versus achieved condition]: the d=2 scalar-block control should expose nominal 1e14 separately from achieved condition 1"
    near_decoupled_achieved = [
        achieved_by_id[case.case_id]
        for case in schedule
        if case.stratum == "near_decoupled"
    ]
    assert max(near_decoupled_achieved) < 1.0e12, "DEFECT [near-decoupled condition fixture]: frozen cases unexpectedly invalidate the global-only 1e14 coverage contract"


def test_runtime_stress_binds_boundary_witness_and_all_case_oracle_failures():
    result_record = require_runner_api(
        "check_cg_factor_gap_stress", "runtime stress provenance"
    )()
    assert require_mapping_field(result_record, "status", "runtime stress provenance") == "PASS", "DEFECT [runtime stress provenance]: runtime check must pass only with complete evidence"
    observed = require_mapping_field(
        result_record, "observed", "runtime stress provenance"
    )
    boundary = require_mapping_field(
        observed, "boundary_witness", "runtime boundary witness"
    )
    certificate = canonical_correlation_clip_certificate(WITHIN_BOUND_CLIP_WITNESS)
    assert require_mapping_field(boundary, "matrix_digest", "runtime boundary witness") == matrix_digest(WITHIN_BOUND_CLIP_WITNESS), "DEFECT [runtime boundary witness]: matrix digest does not bind the frozen exact input"
    exact_input_value = float(
        require_mapping_field(boundary, "exact_input_value", "runtime boundary witness")
    )
    assert exact_input_value == pytest.approx(certificate["high_precision_gap"], rel=5e-12, abs=math.ulp(certificate["high_precision_gap"])), "DEFECT [runtime boundary witness]: reported value is not the 200-digit exact-input determinant gap"
    excursion = float(
        require_mapping_field(boundary, "rho_squared_excursion", "runtime boundary witness")
    )
    assert excursion == certificate["rho_squared_excess"] and excursion > 0.0, "DEFECT [runtime boundary witness]: positive binary64 rho^2 excursion is missing or incorrect"
    outward_allowance = float(
        require_mapping_field(boundary, "outward_allowance", "runtime boundary witness")
    )
    assert outward_allowance == certificate["forward_error_upper_float"], "DEFECT [runtime boundary witness]: allowance must be the independently recomputed outward binary64 bound"
    assert Fraction.from_float(outward_allowance) >= certificate["forward_error_upper"], "DEFECT [runtime boundary witness]: reported allowance rounded inward"
    assert require_mapping_field(boundary, "status", "runtime boundary witness") == "PASS", "DEFECT [runtime boundary witness]: bound witness must report PASS"
    assert require_mapping_field(observed, "all_case_oracle_cases", "runtime all-case oracle") == len(frozen_cases()), "DEFECT [runtime all-case oracle]: report must bind the all-case claim to all 3138 frozen cases"
    assert require_mapping_field(observed, "all_case_oracle_failures", "runtime all-case oracle") == 0, "DEFECT [runtime all-case oracle]: an all-case accuracy claim requires zero independently evaluated oracle failures"
