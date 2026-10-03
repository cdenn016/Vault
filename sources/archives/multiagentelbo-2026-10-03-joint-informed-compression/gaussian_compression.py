"""Reference-conditioned Gaussian lifts with a reduced persistent message.

Dense reference constants and temporary lifted moments are still used. This
reduces history-dependent message storage, not the current dense workspace.
"""
from __future__ import annotations
from dataclasses import dataclass
import torch


@dataclass(frozen=True)
class GaussianCompression:
    """Offline conditional X|(P X,W X); only W X moments persist online."""

    P:          torch.Tensor
    W:          torch.Tensor
    offset:     torch.Tensor
    gain:       torch.Tensor
    residual:   torch.Tensor

    def encode(
        self,
        mu:    torch.Tensor,                  # (B,d)
        Sigma: torch.Tensor,                  # (B,d,d)
    ) -> tuple[torch.Tensor, torch.Tensor]:
        r"""Push moments to W X: (W mu, W Sigma W^T)."""
        covariance=self.W@Sigma@self.W.T
        return mu@self.W.T,(covariance+covariance.mT)/2

    def decode(
        self,
        R:     torch.Tensor,                  # (B,m), actual retained value
        mu:    torch.Tensor,                  # (B,r), stored W X mean
        Sigma: torch.Tensor,                  # (B,r,r), stored covariance
    ) -> tuple[torch.Tensor, torch.Tensor]:
        r"""Mix the reference X|(R,z) over z~N(mu,Sigma)."""
        rank=len(self.P)
        mean=self.offset+torch.cat((R,mu),dim=-1)@self.gain.T
        B=self.gain[:,rank:]
        covariance=self.residual+B@Sigma@B.T
        return mean,(covariance+covariance.mT)/2


def compile_compression(
    mu:    torch.Tensor,                      # (d,), reference activation
    Sigma: torch.Tensor,                      # (d,d), positive definite
    P:     torch.Tensor,                      # (m,d), retained rows
    W:     torch.Tensor,                      # (r,d), extra independent rows
) -> GaussianCompression:
    r"""Compile N(mu,Sigma)(dx|[P;W]x), without a covariance subtraction.

    For H=[P;W], gain=Sigma H^T(H Sigma H^T)^(-1). The residual factor
    L U_perp spans the nullspace of H L, where Sigma=L L^T; its Gram matrix
    preserves the declared support without jitter or eigenvalue clipping.
    """
    d=mu.numel()
    if mu.shape!=(d,) or Sigma.shape!=(d,d) or P.ndim!=2 or W.ndim!=2:
        raise ValueError("activation vector/covariance and two row matrices required")
    if P.shape[1]!=d or W.shape[1]!=d or not 0<len(P)<=len(P)+len(W)<=d:
        raise ValueError("retained and message rows must fit the fine dimension")
    H=torch.cat((P,W))
    L=torch.linalg.cholesky(Sigma)
    cross=Sigma@H.T
    gain=torch.cholesky_solve(cross.T,torch.linalg.cholesky(H@cross)).T
    U=torch.linalg.qr(L.T@H.T,mode="complete").Q[:,len(H):]
    factor=L@U
    return GaussianCompression(P.clone(),W.clone(),mu-gain@(H@mu),gain,factor@factor.T)
