"""Compare one captured covariance update; never replay or alter production code."""
from __future__ import annotations

import os
os.environ['MKL_THREADING_LAYER'] = 'SEQUENTIAL'
os.environ['OMP_NUM_THREADS'] = os.environ['MKL_NUM_THREADS'] = '1'

import hashlib
import json
from pathlib import Path
import sys
import time

import mpmath as mp
import numpy as np
import scipy.linalg as sla


def _mp(value: np.ndarray) -> mp.matrix:
    """Embed stored binary64 entries exactly in 80-digit arithmetic."""
    return mp.matrix([[mp.mpf(float(x)) for x in row] for row in value])


def _absolute_error(value: np.ndarray, reference: mp.matrix) -> float:
    """Compare binary64 values with the high-precision target without rounding it."""
    return float(max(abs(mp.mpf(float(value[i, j]))-reference[i, j])
                     for i in range(value.shape[0]) for j in range(value.shape[1])))


def _local_summary(value: np.ndarray, reference: mp.matrix) -> dict:
    """Report local error and tiny-eigenvalue error against exact stored target."""
    native_min = float(sla.eigvalsh(value, subset_by_index=[0, 0])[0])
    evaluated_min = mp.eigsy(_mp(value), eigvals_only=True)[0]
    reference_min = mp.eigsy(reference, eigvals_only=True)[0]
    return {'max_entry_error': _absolute_error(value, reference),
            'binary64_eigenvalue': native_min,
            'high_precision_eigenvalue_of_binary64_matrix': mp.nstr(evaluated_min, 40),
            'relative_eigenvalue_error_from_matrix_entries': float((evaluated_min-reference_min)/reference_min)}


def _global_summary(value: np.ndarray) -> dict:
    """Inspect each new candidate once on the same hidden principal coordinates."""
    hidden = np.array([2*n+k for n in range(1024) if n % 16 != 15 for k in range(2)])
    principal = value[np.ix_(hidden, hidden)]
    low = float(sla.eigvalsh(principal, subset_by_index=[0, 0])[0])
    high = float(sla.eigvalsh(principal, subset_by_index=[len(principal)-1, len(principal)-1])[0])
    return {'fiber_max': float(np.abs(value.reshape(64, 16, 2, 2048).mean(1)).max()),
            'symmetry_max': float(np.abs(value-value.T).max()),
            'hidden_principal_minimum': low, 'hidden_principal_maximum': high,
            'condition_if_positive': high/low if low > 0 else None,
            'spectrum_scope': 'binary64 diagnostic; not a certified lower eigenvalue bound'}


def main() -> None:
    """Use only the captured matrices for direct-block and moment comparisons."""
    started = time.perf_counter()
    mp.mp.dps = 80
    root = Path(__file__).resolve().parents[2]
    folder = root/'artifacts/gaussian-covariance-diagnostic/20261003T025107540279Z'
    out = Path(__file__).parent
    with np.load(folder/'capture.npz') as saved:
        incoming = saved['input_covariance'][0].copy()
        original = saved['output_covariance'][0].copy()
    with np.load(folder/'local-moments.npz') as saved:
        local = {key: saved[key].copy() for key in saved.files}
    I = local['coordinates']; J = np.setdiff1d(np.arange(len(incoming)), I)
    C, T_raw, G = local['C'][0], local['tilted_C'][0], local['gain'][0]
    T = .5*(T_raw+T_raw.T)
    direct = original.copy()
    cross = G[J]@T
    direct[np.ix_(I, I)] = T
    direct[np.ix_(J, I)] = cross
    direct[np.ix_(I, J)] = cross.T
    # Also expose the rounding change from explicitly separating residual and tilt.
    schur = direct.copy()
    G_J = G[J]
    D = incoming[np.ix_(J, J)]
    residual = D-(G_J@C)@G_J.T
    remainder = residual+(G_J@T)@G_J.T
    schur[np.ix_(J, J)] = .5*(remainder+remainder.T)

    C_mp, T_mp = _mp(C), _mp(T)
    C_inverse = C_mp**-1
    chosen = J[np.argsort(np.linalg.norm(G[J], axis=1))[-6:]]
    G_mp = _mp(incoming[np.ix_(chosen, I)])*C_inverse
    cross_reference = G_mp*T_mp
    remainder_reference = (_mp(incoming[np.ix_(chosen, chosen)])
        -G_mp*C_mp*G_mp.T+G_mp*T_mp*G_mp.T)
    variants = {'captured': original, 'direct_blocks': direct, 'separate_schur_and_tilt': schur}
    results = {}
    for name, matrix in variants.items():
        results[name] = {'local': _local_summary(matrix[np.ix_(I, I)], T_mp),
                         'selected_cross_error': _absolute_error(matrix[np.ix_(chosen, I)], cross_reference),
                         'selected_remainder_error': _absolute_error(matrix[np.ix_(chosen, chosen)], remainder_reference),
                         'max_change_from_captured': float(np.abs(matrix-original).max())}
        if name != 'captured':
            results[name]['global'] = _global_summary(matrix)

    # Independent moment target: stored positive weights and rounded source offsets,
    # normalized in high precision. This does not recompute likelihoods or any path.
    L = local['L'][0]
    offsets = np.sqrt(6.)*np.concatenate((L.T, -L.T), axis=0)
    weights = [mp.mpf(float(w)) for w in local['weights'][0]]
    total = sum(weights)
    weights = [w/total for w in weights]
    points = _mp(offsets)
    center = mp.matrix([sum(weights[q]*points[q, j] for q in range(12)) for j in range(6)])
    moment = mp.matrix(6, 6)
    for i in range(6):
        for j in range(6):
            moment[i, j] = sum(weights[q]*(points[q, i]-center[i])*(points[q, j]-center[j]) for q in range(12))
    exact_eigenvalues = mp.eigsy(moment, eigvals_only=True)
    native_weights = local['weights'][0]/local['weights'][0].sum()
    native_center = native_weights@offsets
    weighted_factor = ((offsets-native_center)*np.sqrt(native_weights)[:, None]).T
    singular = sla.svdvals(weighted_factor)
    factor_min = float(singular[-1]**2)
    reference_min = exact_eigenvalues[0]
    moment_result = {'weight_sum_minus_one': mp.nstr(total-1, 40),
                    'stored_tilt_asymmetry_max': float(np.abs(T_raw-T_raw.T).max()),
                    'high_precision_minimum': mp.nstr(reference_min, 40),
                    'high_precision_maximum': mp.nstr(exact_eigenvalues[5], 40),
                    'stored_symmetrized_tilt': _local_summary(T, moment),
                    'captured_local': _local_summary(original[np.ix_(I, I)], moment),
                    'weighted_factor_svd_minimum_squared': factor_min,
                    'weighted_factor_relative_minimum_error': float((mp.mpf(factor_min)-reference_min)/reference_min),
                    'weighted_factor_condition': float(singular[0]/singular[-1]),
                    'scope': '80-digit six-dimensional covariance from stored normalized weights and rounded offsets; not exact real-arithmetic likelihoods'}
    result = {'scope': 'one captured source update, no trajectory continuation or production modification',
              'python': sys.executable, 'precision_digits': 80, 'device': 'cpu',
              'thread_environment': {key: os.environ[key] for key in ('MKL_THREADING_LAYER','OMP_NUM_THREADS','MKL_NUM_THREADS')},
              'source_directory': str(folder), 'coordinates': I.tolist(), 'selected_remainder_coordinates': chosen.tolist(),
              'input_sha256': {name: hashlib.sha256((folder/name).read_bytes()).hexdigest() for name in ('capture.npz','local-moments.npz')},
              'recorded_target_minimum_high_precision': mp.nstr(mp.eigsy(T_mp, eigvals_only=True)[0], 40),
              'variants': results, 'local_moments': moment_result,
              'elapsed_seconds': time.perf_counter()-started}
    with (out/'block-update-comparison.json').open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
    with (out/'block-update-comparison.npz').open('xb') as stream:
        np.savez_compressed(stream, coordinates=I, selected_remainder_coordinates=chosen,
            captured_local=original[np.ix_(I, I)], target_local=T,
            direct_cross=cross, direct_cross_coordinates=J, weighted_factor=weighted_factor)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
