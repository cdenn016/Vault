"""Conditional Gaussian networks and exact coordinate coarse-graining at c_*.

Structural links and source assignments are held. Complex linear maps must be
realified explicitly; every probability density here uses real Lebesgue measure.
A static Schur marginal does not establish autonomous retained dynamics.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, log, pi

import torch


def _symmetric(matrix: torch.Tensor) -> None:
    """Require symmetry within floating-point roundoff without repairing inputs."""
    tolerance = 32 * torch.finfo(matrix.dtype).eps
    if not torch.allclose(matrix, matrix.transpose(-1, -2), atol=tolerance, rtol=tolerance):
        raise ValueError("precision must be symmetric")


def _logdet_cholesky(factor: torch.Tensor) -> torch.Tensor:
    r"""Return log(det J)=2 sum_i log L_ii for J=L L^T."""
    return 2 * factor.diagonal(dim1=-2, dim2=-1).log().sum(-1)


def _time(t: float) -> None:
    """Require a finite nonnegative lag in the declared microscopic clock."""
    if not isfinite(t) or t < 0:
        raise ValueError("lag must be finite and nonnegative")


@dataclass(frozen=True)
class GaussianAction:
    r"""Real action E(x)=x^T J x/2-h^T x+c; raw mass is integral exp(-E)."""

    J: torch.Tensor                     # (d, d), full precision
    h: torch.Tensor                     # (d,), information vector
    c: float | torch.Tensor             # scalar energy offset

    def __post_init__(self) -> None:
        if self.J.ndim != 2 or self.J.shape[0] != self.J.shape[1] or not self.J.shape[0]:
            raise ValueError("J must be a nonempty square real precision")
        if self.J.dtype not in (torch.float32, torch.float64):
            raise ValueError("Gaussian actions require real float32 or float64 tensors")
        if self.h.shape != (len(self.J),) or self.h.dtype != self.J.dtype or self.h.device != self.J.device:
            raise ValueError("h must match the precision dimension, dtype and device")
        c = torch.as_tensor(self.c, dtype=self.J.dtype, device=self.J.device)
        if c.ndim or not all(bool(torch.isfinite(x).all()) for x in (self.J, self.h, c)):
            raise ValueError("action coefficients must be finite and c scalar")
        _symmetric(self.J)
        object.__setattr__(self, "c", c)

    def moments(self) -> tuple[torch.Tensor, torch.Tensor]:
        r"""Return mu=J^-1 h and Sigma=J^-1 using one Cholesky solve."""
        L = torch.linalg.cholesky(self.J)
        rhs = torch.cat((self.h[:, None], torch.eye(len(self.J), dtype=self.J.dtype,
                                                   device=self.J.device)), dim=1)
        solved = torch.cholesky_solve(rhs, L)
        return solved[:, 0], solved[:, 1:]

    def log_mass(self) -> torch.Tensor:
        r"""Return log Z=d log(2 pi)/2-log(det J)/2+h^T J^-1 h/2-c."""
        L = torch.linalg.cholesky(self.J)
        mu = torch.cholesky_solve(self.h[:, None], L)[:, 0]
        return (len(self.J) * log(2 * pi) - _logdet_cholesky(L) + self.h @ mu) / 2 - self.c


def realify_map(L: torch.Tensor) -> torch.Tensor:
    r"""Represent a complex map by [[Re L,-Im L],[Im L,Re L]].

    Within each endpoint, real coordinates precede imaginary coordinates. This
    is a real linear map, not an implicit choice of a proper complex Gaussian.
    """
    if L.ndim < 2 or not L.is_complex():
        raise ValueError("realification requires a complex matrix or matrix batch")
    return torch.cat((torch.cat((L.real, -L.imag), dim=-1),
                      torch.cat((L.imag, L.real), dim=-1)), dim=-2)


def assemble_network(
    J_0:       torch.Tensor,             # (N, K, K), proper on-site prior precision
    mu_0:      torch.Tensor,             # (N, K), on-site prior mean
    A_e:       torch.Tensor,             # (E, R, K), receiver comparison maps
    B_e:       torch.Tensor,             # (E, R, K), source comparison maps
    Gamma_inv: torch.Tensor,             # (E, R, R), record precision
    o_e:       torch.Tensor,             # (E, R), observed records
    edges:     torch.Tensor,             # (E, 2), (receiver, source)
) -> GaussianAction:
    r"""Assemble a proper Gaussian prior times normalized endpoint likelihoods.

    The record residual is A_e x_i-B_e x_j-o_e. Each likelihood includes
    R log(2 pi)/2-log(det Gamma_inv)/2 in its energy. Flat, independent
    group-valued and rectangular comparison maps share this conditional law.
    """
    if J_0.ndim != 3 or J_0.shape[-1] != J_0.shape[-2] or not J_0.shape[0]:
        raise ValueError("on-site precision must have shape (N,K,K)")
    N, K, _ = J_0.shape
    if K == 0 or J_0.dtype not in (torch.float32, torch.float64):
        raise ValueError("positive real fiber dimension required")
    if A_e.ndim != 3:
        raise ValueError("comparison maps must have shape (E,R,K)")
    E, R, _ = A_e.shape
    if R == 0 or mu_0.shape != (N, K) or A_e.shape != (E, R, K):
        raise ValueError("prior or receiver comparison dimensions differ")
    if B_e.shape != A_e.shape or Gamma_inv.shape != (E, R, R) or o_e.shape != (E, R):
        raise ValueError("source map or record dimensions differ")
    values = (mu_0, A_e, B_e, Gamma_inv, o_e)
    if any(x.dtype != J_0.dtype or x.device != J_0.device for x in values):
        raise ValueError("all law coefficients must share a real dtype and device")
    if not all(bool(torch.isfinite(x).all()) for x in (J_0, *values)):
        raise ValueError("law coefficients must be finite")
    if edges.shape != (E, 2) or edges.dtype != torch.long or edges.device != J_0.device:
        raise ValueError("edges must be a matching-device long tensor of endpoint pairs")
    if bool(((edges < 0) | (edges >= N)).any()):
        raise ValueError("edge endpoint lies outside the node set")
    _symmetric(J_0)
    _symmetric(Gamma_inv)
    L_0 = torch.linalg.cholesky(J_0)
    L_e = torch.linalg.cholesky(Gamma_inv)
    J = torch.block_diag(*J_0.unbind(0))  # (N K,N K), complete dense quadratic carrier
    h_0 = (J_0 @ mu_0[..., None]).squeeze(-1)
    h = h_0.flatten()
    c = (N * K * log(2 * pi) - _logdet_cholesky(L_0).sum()
         + (mu_0 * h_0).sum()) / 2
    G_A, G_B = Gamma_inv @ A_e, Gamma_inv @ B_e
    G_o = (Gamma_inv @ o_e[..., None]).squeeze(-1)
    blocks = (A_e.transpose(-1, -2) @ G_A,
              B_e.transpose(-1, -2) @ G_B,
              -A_e.transpose(-1, -2) @ G_B)
    coordinate = torch.arange(K, device=J.device)
    receiver = edges[:, 0, None] * K + coordinate
    source = edges[:, 1, None] * K + coordinate

    def add_block(rows: torch.Tensor, cols: torch.Tensor, block: torch.Tensor) -> None:
        """Accumulate repeated endpoint blocks without assuming a simple graph."""
        index = (rows[:, :, None].expand(E, K, K).reshape(-1),
                 cols[:, None, :].expand(E, K, K).reshape(-1))
        J.index_put_(index, block.reshape(-1), accumulate=True)

    add_block(receiver, receiver, blocks[0])
    add_block(source, source, blocks[1])
    add_block(receiver, source, blocks[2])
    add_block(source, receiver, blocks[2].transpose(-1, -2))
    h.index_add_(0, receiver.flatten(), (A_e.transpose(-1, -2) @ G_o[..., None]).flatten())
    h.index_add_(0, source.flatten(), -(B_e.transpose(-1, -2) @ G_o[..., None]).flatten())
    c = c + (E * R * log(2 * pi) - _logdet_cholesky(L_e).sum()
             + (o_e * G_o).sum()) / 2
    return GaussianAction(J, h, c)


@dataclass(frozen=True)
class GaussianParent:
    """Complete marginal and equilibrium reverse conditional on retained coordinates."""

    fine_action:       GaussianAction
    action:            GaussianAction
    retained:          torch.Tensor
    hidden:            torch.Tensor
    hidden_precision:  torch.Tensor
    hidden_gain:       torch.Tensor
    hidden_intercept:  torch.Tensor

    def hidden_covariance(self) -> torch.Tensor:
        r"""Return the reverse conditional covariance J_hh^-1."""
        identity = torch.eye(len(self.hidden), dtype=self.action.J.dtype, device=self.action.J.device)
        return torch.cholesky_solve(identity, torch.linalg.cholesky(self.hidden_precision))

    def lift_moments(
        self,
        mu_c:    torch.Tensor,
        Sigma_c: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        r"""Lift a retained Gaussian through the fine law's exact reverse kernel.

        mu_h=b+G mu_c and Sigma_hh=J_hh^-1+G Sigma_c G^T.
        This lift uses an equilibrium reverse kernel, not a hidden-history filter.
        """
        r = len(self.retained)
        if mu_c.shape != (r,) or Sigma_c.shape != (r, r):
            raise ValueError("retained moment dimensions differ")
        order = torch.cat((self.retained, self.hidden))
        mu_h = self.hidden_intercept + self.hidden_gain @ mu_c
        cross = self.hidden_gain @ Sigma_c
        Sigma_h = self.hidden_covariance() + cross @ self.hidden_gain.T
        mu = torch.cat((mu_c, mu_h))
        Sigma = torch.cat((torch.cat((Sigma_c, cross.T), dim=1),
                           torch.cat((cross, Sigma_h), dim=1)), dim=0)
        inverse_order = torch.argsort(order)
        return mu[inverse_order], Sigma[inverse_order][:, inverse_order]

    def markov_defect(self) -> torch.Tensor:
        r"""Return J_rh J_hh^-1 J_hr for held identity-mobility OU kinetics.

        It is the equilibrium conditional drift variance. A zero cross block
        gives autonomous retained OU dynamics in this declared coordinate model.
        """
        cross = self.fine_action.J[self.retained][:, self.hidden]
        return -cross @ self.hidden_gain

    def memory_kernel(self, t: float) -> torch.Tensor:
        r"""Return J_rh exp(-J_hh t) J_hr for the held quadratic OU.

        The full projected equation also carries the hidden initial residual
        and colored forcing. This kernel alone is not a stochastic simulator.
        """
        _time(t)
        cross = self.fine_action.J[self.retained][:, self.hidden]
        return cross @ torch.matrix_exp(-self.hidden_precision * t) @ cross.T

    def stationary_lag_covariance(self, t: float) -> torch.Tensor:
        r"""Return C exp(-J t) J^-1 C^T under stationary microscopic preparation.

        These covariances determine the stationary retained Gaussian path law;
        they generally do not define a Markov semigroup on retained states.
        """
        _time(t)
        J = self.fine_action.J
        columns = torch.eye(len(J), dtype=J.dtype, device=J.device)[:, self.retained]
        covariance_columns = torch.cholesky_solve(columns, torch.linalg.cholesky(J))
        return (torch.matrix_exp(-J * t) @ covariance_columns)[self.retained]


def marginalize(
    retained: torch.Tensor,
    action:   GaussianAction,
) -> GaussianParent:
    r"""Integrate hidden coordinates, retaining J,h,c and their reverse kernel.

    J_c=J_rr-J_rh J_hh^-1 J_hr; h_c=h_r-J_rh J_hh^-1 h_h.
    c_c=c+log(det J_hh)/2-d_h log(2 pi)/2-h_h^T J_hh^-1 h_h/2.
    """
    J, h = action.J, action.h
    if (retained.ndim != 1 or retained.dtype != torch.long or retained.device != J.device
            or not retained.numel() or retained.unique().numel() != retained.numel()):
        raise ValueError("retained must be distinct nonempty matching-device coordinate indices")
    if bool(((retained < 0) | (retained >= len(J))).any()):
        raise ValueError("retained coordinate lies outside the fine action")
    mask = torch.ones(len(J), dtype=torch.bool, device=J.device)
    mask[retained] = False
    hidden = torch.arange(len(J), device=J.device)[mask]
    J_rr = J[retained][:, retained]
    J_hh = J[hidden][:, hidden]
    J_rh = J[retained][:, hidden]
    h_h = h[hidden]
    L = torch.linalg.cholesky(J_hh)
    solved = torch.cholesky_solve(torch.cat((J_rh.T, h_h[:, None]), dim=1), L)
    gain, intercept = -solved[:, :-1], solved[:, -1]
    J_c = J_rr + J_rh @ gain
    # Exact Schur symmetry can differ by roundoff after the two solves.
    J_c = (J_c + J_c.T) / 2
    h_c = h[retained] - J_rh @ intercept
    c_c = action.c + (_logdet_cholesky(L) - len(hidden) * log(2 * pi) - h_h @ intercept) / 2
    parent_action = GaussianAction(J_c, h_c, c_c)
    return GaussianParent(action, parent_action, retained, hidden, J_hh, gain, intercept)
