"""Joint source/configuration sensitivity for a fixed Gaussian message basis.

The activation and probability freezing make this a basis-selection proxy,
not the Fisher matrix of the observed switching history or a path optimum.
"""
from __future__ import annotations
from math import expm1
import torch
from .coupled_learning import CoupledModel, CoupledState, comparison_maps
from .source_informed_compression import source_sensitivity
from .switching_paths import source_posterior


def configuration_sensitivity(
    P:        torch.Tensor,                   # (m,d), retained rows
    mobility: torch.Tensor,                   # (N,K,K), positive-definite mobility
    beta:     torch.Tensor,                   # (N,2), independent assignment rows
    dt:       float,
    state:    CoupledState,
    model:    CoupledModel,
) -> torch.Tensor:
    r"""Return E_J[A_J^T Q^{-1} A_J] under a product binary assignment law.

    A_J=P(I-dt M H_J), Q=2dt P M P^T. The second moment is the mean
    Jacobian's Gram plus dt^2 sum_i beta_i0 beta_i1 times the Gram of each
    projected Hessian difference. Both receiver and sender blocks are kept.
    """
    N,K=model.a.shape
    d=N*K
    if dt<=0 or model.sources.shape!=(N,2) or beta.shape!=(N,2):
        raise ValueError("positive time step and binary receiver probabilities required")
    if bool((beta<0).any()) or not torch.allclose(beta.sum(-1),torch.ones_like(beta[:,0])):
        raise ValueError("assignment rows must be normalized and nonnegative")
    M=torch.block_diag(*mobility)
    PM=P@M
    Q_chol=torch.linalg.cholesky(2*dt*PM@P.T)
    maps=comparison_maps(state.Theta,model)
    nodes=torch.cat((torch.arange(N,device=P.device)[:,None],model.sources),dim=1)
    index=(nodes[:,:,None]*K+torch.arange(K,device=P.device)).reshape(N,3*K)
    residual=P.new_zeros((N,2,K,3*K))          # Local receiver / two sender slots.
    residual[:,:,:,:K]=torch.eye(K,dtype=P.dtype,device=P.device)
    residual[:,0,:,K:2*K]=-maps[:,0]
    residual[:,1,:,2*K:]=-maps[:,1]
    local_hessian=(residual.mT@model.H[:,None]@residual)/model.tau
    local_mean=(beta[:,:,None,None]*local_hessian).sum(1)
    flat_index=(index[:,:,None]*d+index[:,None,:]).reshape(-1)
    H_bar=torch.block_diag(*model.J_0).reshape(-1).index_add(0,flat_index,local_mean.reshape(-1)).reshape(d,d)
    A_bar=P-dt*PM@H_bar
    mean_white=torch.linalg.solve_triangular(Q_chol,A_bar,upper=False)
    # Each Hessian difference has only 3K input coordinates. Keep its local Gram.
    projected=PM[:,index].permute(1,0,2)       # (N,m,3K).
    white=torch.linalg.solve_triangular(Q_chol,projected,upper=False)
    delta=local_hessian[:,0]-local_hessian[:,1]
    local_variance=dt**2*beta.prod(-1)[:,None,None]*(delta.mT@(white.mT@white)@delta)
    variance=P.new_zeros(d*d).index_add(0,flat_index,local_variance.reshape(-1)).reshape(d,d)
    G=mean_white.T@mean_white+variance
    return (G+G.T)/2


def joint_informed_basis(
    mu:           torch.Tensor,              # (d,), activation mean
    Sigma:        torch.Tensor,              # (d,d), positive-definite activation
    P:            torch.Tensor,              # (m,d), retained rows
    mobility:     torch.Tensor,              # (N,K,K)
    held_beta:    torch.Tensor,              # (N,2), native initial label rows
    dt:           float,
    refresh_rate: float,
    rank:         int,
    state:        CoupledState,              # First structural state only.
    model:        CoupledModel,
) -> tuple[torch.Tensor, torch.Tensor, dict[str, float]]:
    r"""Diagonalize B^T[c G_source+(1-c)G_hold+c G_redraw]B.

    B=L U with Sigma=L L^T and U spanning ker(P L); c=1-exp(-rate dt).
    The global coin mixes complete product-law second moments, preserving
    its label correlations. Source sensitivity still freezes beta at mu and
    treats the proposal coin as augmented information rather than observing it.
    """
    d=mu.numel()
    if dt<=0 or refresh_rate<0 or Sigma.shape!=(d,d) or P.ndim!=2 or P.shape[1]!=d or not 0<len(P)<d:
        raise ValueError("proper reference, nontrivial retained rows and valid clock required")
    if not 0<=rank<=d-len(P):
        raise ValueError("message rank exceeds the hidden dimension")
    L=torch.linalg.cholesky(Sigma)
    torch.linalg.cholesky(P@Sigma@P.T)
    U=torch.linalg.qr(L.T@P.T,mode="complete").Q[:,len(P):]
    B=L@U
    c=-expm1(-refresh_rate*dt)
    source=c*source_sensitivity(mu,B@B.T,state,model)
    beta=source_posterior(mu.reshape(1,*model.a.shape),state,model)[0]
    config=(1-c)*configuration_sensitivity(P,mobility,held_beta,dt,state,model)
    config=config+c*configuration_sensitivity(P,mobility,beta,dt,state,model)
    source_gram=B.T@source@B
    config_gram=B.T@config@B
    gram=source_gram+config_gram
    values,V=torch.linalg.eigh((gram+gram.T)/2)
    if not bool(torch.isfinite(values).all()):
        raise ArithmeticError("nonfinite joint sensitivity spectrum")
    tolerance=100*torch.finfo(values.dtype).eps*len(values)*max(1.,float(values.abs().max()))
    if float(values.min()) < -tolerance:
        raise ArithmeticError("joint sensitivity Gram has a materially negative eigenvalue")
    W=torch.linalg.solve_triangular(L.T,U@V.flip(1)[:,:rank],upper=True).T
    return W,values.flip(0),{"refresh_probability":c,
        "source_hidden_trace":float(source_gram.trace()),"configuration_hidden_trace":float(config_gram.trace())}
