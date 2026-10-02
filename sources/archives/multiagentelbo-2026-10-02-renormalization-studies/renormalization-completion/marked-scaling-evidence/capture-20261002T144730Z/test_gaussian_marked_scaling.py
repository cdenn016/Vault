"""Tiny independent checks for the declared massive marked Gaussian study."""
from __future__ import annotations

import numpy as np
from numpy.testing import assert_allclose
from scipy import linalg, sparse

from multiagent_elbo.realizations.gaussian.marked_gaussian_scaling import (
    GaussianPair, block_map, build_precision, cell_map, draw_environment,
    initial_marks, padded_covariance_bound, push_marks, solve_pair,
    susceptibility_reference,
)


def test_quadratic_action_and_uniform_spectrum() -> None:
    A, B = draw_environment(3, 7, 0.05)
    H = build_precision(A, B, 2.0, 0.3, 0.2, 0.4).toarray()
    x = np.arange(12, dtype=float).reshape(3, 2, 2) / 9
    r, u = x[:, 0], x[:, 1]
    twice = 2 * np.sum(x*x) + 0.3*np.sum((r-u)**2)
    twice += 0.2*np.sum((r-np.einsum("nij,nj->ni", A, u))**2)
    twice += 0.2*np.sum((r-np.einsum("nij,nj->ni", B, u))**2)
    twice += 0.4*(np.sum(np.diff(r, axis=0)**2)+r[0]@r[0]+r[-1]@r[-1])
    assert_allclose(x.ravel()@H@x.ravel(), twice, atol=1e-13)
    assert np.linalg.eigvalsh(H)[0] >= 2
    assert np.linalg.eigvalsh(H)[-1] <= 5.5


def test_direct_staged_both_laws_and_independent_schur() -> None:
    n = 4
    A, B = draw_environment(n, 8, 0.05)
    H = build_precision(A, B, 2.0, 0.3, 0.2, 0.4)
    h = np.sin(np.arange(4*n)) * 0.1
    initial, residual = solve_pair(H, cell_map(n, 0), h, 2.0)
    assert residual < 1e-13
    frames = np.tile(np.eye(2), (n, 1, 1))
    P2 = block_map(frames, 2)
    staged = initial.coarsen(P2).coarsen(block_map(frames[::2], 2))
    direct = initial.coarsen(block_map(frames, 4))
    for field in ("mean", "covariance", "reference_covariance"):
        assert_allclose(getattr(staged, field), getattr(direct, field), atol=1e-13)
    assert_allclose([staged.offset, staged.relative_offset, staged.log_mass],
                    [direct.offset, direct.relative_offset, direct.log_mass], atol=1e-13)
    P = (block_map(frames, 4) @ cell_map(n, 0)).toarray()
    T = np.vstack([P, linalg.null_space(P).T])
    Ti = np.linalg.inv(T)
    J, v = Ti.T @ H.toarray() @ Ti, Ti.T @ h
    F = np.linalg.solve(J[2:, 2:], J[2:, :2])
    Jh = J[:2, :2] - J[:2, 2:] @ F
    hh = v[:2] - J[:2, 2:] @ np.linalg.solve(J[2:, 2:], v[2:])
    ch = np.linalg.slogdet(T)[1] + 0.5*np.linalg.slogdet(J[2:, 2:])[1]
    ch -= 0.5*(len(v)-2)*np.log(2*np.pi)
    ch -= 0.5*v[2:]@np.linalg.solve(J[2:, 2:], v[2:])
    assert_allclose(np.linalg.inv(direct.covariance), Jh, atol=1e-13)
    assert_allclose(np.linalg.solve(direct.covariance, direct.mean), hh, atol=1e-13)
    assert_allclose(direct.offset, ch, atol=1e-13)
    both = GaussianPair(np.r_[initial.mean, -initial.mean],
                        linalg.block_diag(initial.covariance, initial.covariance),
                        linalg.block_diag(initial.reference_covariance, initial.reference_covariance),
                        2*initial.log_mass)
    lifted = both.coarsen(sparse.block_diag([P2, P2]))
    assert_allclose(lifted.mean, np.r_[initial.coarsen(P2).mean, -initial.coarsen(P2).mean])
    assert_allclose(lifted.log_mass, 2*staged.log_mass)


def test_every_mark_and_measure_pair_under_nonorthogonal_frames() -> None:
    n = 4
    A, B = draw_environment(n, 9, 0.05)
    frames = np.array([[[1+0.1*i, 0.2], [0.1, 0.9]] for i in range(n)])
    marks = initial_marks(A, B, frames)
    staged = push_marks(push_marks(marks, frames, 2), frames[::2], 2)
    direct = push_marks(marks, frames, 4)
    assert len(direct[0]) == 8*n-2
    for lhs, rhs in zip(staged, direct):
        assert_allclose(lhs, rhs, atol=1e-13)
    original = push_marks(initial_marks(A, B, np.tile(np.eye(2), (n, 1, 1))),
                          np.tile(np.eye(2), (n, 1, 1)), 4)
    assert_allclose(direct[2], frames[0] @ original[2] @ np.linalg.inv(frames[0]), atol=1e-13)
    H = build_precision(A, B, 2.0, 0.3, 0.2, 0.4)
    fine, _ = solve_pair(H, cell_map(n, 0), np.zeros(4*n), 2.0)
    G = linalg.block_diag(*frames)
    changed = fine.coarsen(sparse.csr_matrix(G))
    changed_parent = changed.coarsen(block_map(frames, 4))
    canonical_parent = fine.coarsen(block_map(np.tile(np.eye(2), (n, 1, 1)), 4))
    for field in ("covariance", "reference_covariance"):
        assert_allclose(getattr(changed_parent, field),
                        frames[0] @ getattr(canonical_parent, field) @ frames[0].T, atol=1e-13)
    assert_allclose(changed_parent.relative_offset, canonical_parent.relative_offset, atol=1e-13)
    # The two sectors have identical geometric copies and identity cross morphisms.
    for sector in range(2):
        assert_allclose(staged[2], direct[2], atol=1e-13)


def test_padding_bound_and_local_susceptibility_reference() -> None:
    # A constant environment has an independent Fourier-symbol susceptibility.
    n, pad = 2, 3
    total = n+2*pad
    A = np.tile(np.diag([1.4, 0.7]), (total, 1, 1))
    B = np.tile(np.array([[1.0, 0.45], [0.0, 1.0]]), (total, 1, 1))
    H = build_precision(A, B, 2.0, 0.3, 0.2, 0.4)
    pair, _ = solve_pair(H, cell_map(n, pad), np.zeros(4*total), 2.0)
    bigger_A = np.tile(A[0], (total+8, 1, 1))
    bigger_B = np.tile(B[0], (total+8, 1, 1))
    larger, _ = solve_pair(build_precision(bigger_A, bigger_B, 2.0, 0.3, 0.2, 0.4),
                            cell_map(n, pad+4), np.zeros(4*(total+8)), 2.0)
    assert np.linalg.norm(pair.covariance-larger.covariance, 2) <= padded_covariance_bound(2., 5.5, pad)
    reference, tail = susceptibility_reference(H, 2.0, 5.5, n, pad, pad-1)
    onsite = build_precision(A[:1], B[:1], 2., 0.3, 0.2, 0.4).toarray()
    onsite[:2, :2] -= 0.8*np.eye(2)
    S = np.c_[np.eye(2), np.eye(2)]/np.sqrt(2)
    exact = S @ np.linalg.solve(onsite, S.T)
    assert np.linalg.norm(reference-exact, 2) <= tail

