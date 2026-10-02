"""Normalized source-label VFE and coupled metric descent at fixed c_*.

Recognition is product Gaussian with coordinate-optimal categorical labels.
Links are deterministic generative parameters with declared endpoint metrics.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import expm1, isfinite, log, pi as PI

import torch


@dataclass(frozen=True)
class CoupledModel:
    """Fixed priors, record metrics, source supports, and inverse-paired topology."""

    a:          torch.Tensor                 # (N,K), baseline means
    J_0:        torch.Tensor                 # (N,K,K), baseline precision
    H:          torch.Tensor                 # (N,K,K), record/endpoint metric
    sources:    torch.Tensor                 # (N,S), source node per candidate
    endpoints:  torch.Tensor                 # (E,2), stored map is source -> receiver
    link_index: torch.Tensor                 # (N,S), independent edge index
    reverse:    torch.Tensor                 # (N,S), use inverse stored map
    tau:        float

    def __post_init__(self) -> None:
        """Validate the declared nonself topology and positive fixed metrics once."""
        N, K = self.a.shape
        if not isfinite(self.tau) or self.tau <= 0:
            raise ValueError("temperature must be finite and positive")
        if self.J_0.shape != (N, K, K) or self.H.shape != (N, K, K):
            raise ValueError("node metric dimensions differ")
        if self.sources.ndim != 2 or self.sources.shape[0] != N or not self.sources.shape[1]:
            raise ValueError("each receiver needs a nonempty source row")
        if self.link_index.shape != self.sources.shape or self.reverse.shape != self.sources.shape:
            raise ValueError("candidate topology dimensions differ")
        if self.endpoints.ndim != 2 or self.endpoints.shape[1] != 2:
            raise ValueError("physical edges need two endpoints")
        for value in (self.sources, self.endpoints, self.link_index):
            if value.dtype != torch.long or value.device != self.a.device:
                raise ValueError("topology must use same-device long indices")
        if self.reverse.dtype != torch.bool or self.reverse.device != self.a.device:
            raise ValueError("reverse flags must be same-device booleans")
        for metric in (self.J_0, self.H):
            if not torch.allclose(metric, metric.mT):
                raise ValueError("metrics must be symmetric")
            torch.linalg.cholesky(metric)
        receiver = torch.arange(N, device=self.a.device)[:, None].expand_as(self.sources)
        if bool(((self.sources < 0) | (self.sources >= N) | (self.sources == receiver)).any()):
            raise ValueError("sources must be valid nonself nodes")
        if bool(((self.link_index < 0) | (self.link_index >= len(self.endpoints))).any()):
            raise ValueError("candidate references an unknown edge")
        edge = self.endpoints[self.link_index]
        target = torch.where(self.reverse, edge[..., 1], edge[..., 0])
        source = torch.where(self.reverse, edge[..., 0], edge[..., 1])
        if not torch.equal(target, receiver) or not torch.equal(source, self.sources):
            raise ValueError("physical edge orientation does not match source row")


@dataclass(frozen=True)
class CoupledState:
    """Recognition moments and moving generative parameters."""

    mu:    torch.Tensor                       # (N,K)
    Sigma: torch.Tensor                       # (N,K,K), positive definite
    pi:    torch.Tensor                       # (N,S), positive normalized rows
    Theta: torch.Tensor                       # (E,K,K), GL+ independent links


def comparison_maps(
    Theta: torch.Tensor,
    model: CoupledModel,
) -> torch.Tensor:
    r"""Return Theta_ij, deriving the reversed edge by matrix inversion."""
    direct = Theta[model.link_index]
    inverse = torch.linalg.inv(Theta)[model.link_index]
    return torch.where(model.reverse[..., None, None], inverse, direct)


def expected_costs(
    mu:    torch.Tensor,
    Sigma: torch.Tensor,
    Theta: torch.Tensor,
    model: CoupledModel,
) -> tuple[torch.Tensor, torch.Tensor]:
    r"""Compute E[D_ij] and mean cost for D_ij=||x_i-Theta_ij x_j||_H_i^2/2."""
    maps = comparison_maps(Theta, model)        # (N,S,K,K)
    residual = mu[:, None] - (maps @ mu[model.sources][..., None]).squeeze(-1)
    covariance = Sigma[:, None] + maps @ Sigma[model.sources] @ maps.mT
    mean_cost = .5 * torch.einsum("nsi,nij,nsj->ns", residual, model.H, residual)
    cost = mean_cost + .5 * torch.einsum("nij,nsji->ns", model.H, covariance)
    return cost, mean_cost


def _logdet_spd(matrix: torch.Tensor) -> torch.Tensor:
    r"""Return log det A=2 sum log diag(chol(A)) for an SPD matrix batch."""
    return 2 * torch.linalg.cholesky(matrix).diagonal(dim1=-2, dim2=-1).log().sum(-1)


def free_energy(
    state: CoupledState,
    model: CoupledModel,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    r"""Compute min_beta F=sum KL(q_i||p_i)-sum log sum pi exp(-E D/tau)+sum c_i.

    The record constant is c_i=K log(2 pi tau)/2-logdet(H_i)/2.
    Autograd differentiates the complete scalar, including sender/inverse terms.
    """
    cost, _ = expected_costs(state.mu, state.Sigma, state.Theta, model)
    difference = state.mu-model.a
    kl = .5 * (
        torch.einsum("nij,nji->n", model.J_0, state.Sigma)
        + torch.einsum("ni,nij,nj->n", difference, model.J_0, difference)
        - state.mu.shape[1] - _logdet_spd(model.J_0) - _logdet_spd(state.Sigma)
    )
    logits = state.pi.log()-cost/model.tau
    constant = .5 * (state.mu.shape[1]*log(2*PI*model.tau)-_logdet_spd(model.H))
    F = (kl+constant-torch.logsumexp(logits, dim=-1)).sum()
    return F, torch.softmax(logits, dim=-1), cost


def natural_step(
    state:       CoupledState,
    model:       CoupledModel,
    dt:          float,
    belief_rate: float = 1.,
    source_rate: float = .2,
    link_rate:   float = .05,
) -> tuple[CoupledState, dict[str, float | int]]:
    r"""Take an Armijo-accepted Fisher/endpoint-metric step on the reduced F.

    Gaussian directions are Sigma grad_mu F and 2 Sigma grad_Sigma F Sigma.
    Source velocity is beta-pi. Link gradient is H_i^-1 grad_Theta F H_j.
    Precision and source steps integrate their frozen-coefficient directions;
    Theta exp(-dt Theta^-1 V) is a first-order GL+ retraction.
    """
    if not isfinite(dt) or dt <= 0 or any(not isfinite(r) or r < 0 for r in (belief_rate, source_rate, link_rate)):
        raise ValueError("dt must be positive and rates nonnegative, all finite")
    mu, Sigma, Theta = [x.detach().requires_grad_() for x in (state.mu, state.Sigma, state.Theta)]
    F, beta, _ = free_energy(CoupledState(mu, Sigma, state.pi, Theta), model)
    g_mu, g_Sigma, g_Theta = torch.autograd.grad(F, (mu, Sigma, Theta))
    with torch.no_grad():
        beta = beta.detach()
        g_Sigma = .5*(g_Sigma+g_Sigma.mT)
        v_mu = (Sigma @ g_mu[..., None]).squeeze(-1)
        v_Sigma = 2*Sigma @ g_Sigma @ Sigma
        Lambda = torch.linalg.inv(Sigma)
        P = Lambda+2*g_Sigma
        H_i = model.H[model.endpoints[:, 0]]
        H_j = model.H[model.endpoints[:, 1]]
        v_Theta = torch.linalg.solve(H_i, g_Theta) @ H_j
        algebra = torch.linalg.solve(Theta, v_Theta)
        dissipation = (belief_rate*((g_mu*v_mu).sum()+(g_Sigma*v_Sigma).sum())
                       + source_rate*((beta-state.pi).square()/state.pi).sum()
                       + link_rate*(g_Theta*v_Theta).sum())
        before, slope = float(F), float(dissipation)
        if not isfinite(before) or not isfinite(slope) or slope < 0:
            raise FloatingPointError("nonfinite objective or invalid metric dissipation")
        for backtracks in range(24):
            step = dt * 2.**(-backtracks)
            a_b = -expm1(-step*belief_rate)
            a_p = -expm1(-step*source_rate)
            next_mu = mu-step*belief_rate*v_mu
            next_Sigma = torch.linalg.inv((1-a_b)*Lambda+a_b*P) if belief_rate else Sigma
            next_pi = (1-a_p)*state.pi+a_p*beta if source_rate else state.pi
            next_Theta = Theta @ torch.linalg.matrix_exp(-step*link_rate*algebra) if link_rate else Theta
            candidate = CoupledState(next_mu.detach(), next_Sigma.detach(), next_pi.detach(), next_Theta.detach())
            if not all(bool(torch.isfinite(x).all()) for x in (next_mu, next_Sigma, next_pi, next_Theta)):
                continue
            try:
                after = float(free_energy(candidate, model)[0])
            except torch.linalg.LinAlgError:
                continue
            if isfinite(after) and after <= before-1e-4*step*slope:
                return candidate, {"accepted_dt": step, "backtracks": backtracks,
                                   "before": before, "after": after, "dissipation": slope}
        raise RuntimeError("coupled VFE line search found no descending step")
