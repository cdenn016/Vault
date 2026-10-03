"""Fixed binary-source sensitivity coordinates for Gaussian compression.

The frozen probability weight makes this a heuristic, not expected Fisher
information or the linear-Gaussian exterior-interface optimum.
"""
from __future__ import annotations
import torch
from .coupled_learning import CoupledModel, CoupledState, comparison_maps
from .switching_paths import source_posterior


def source_sensitivity(
    mu:    torch.Tensor,                      # (d,), reference mean
    Sigma: torch.Tensor,                      # (d,d), reference covariance, possibly PSD
    state: CoupledState,
    model: CoupledModel,
) -> torch.Tensor:
    r"""Return G=sum_i w_i E[grad ell_i grad ell_i^T], with frozen w_i.

    ell_i=log(beta_i0/beta_i1) is quadratic, so its local gradient is C_i X.
    w_i=beta_i0(mu) beta_i1(mu); E[XX^T]=Sigma+mu mu^T. This does not
    replace w_i by its state-dependent value inside the expectation.
    """
    N,K=model.a.shape
    d=N*K
    if model.sources.shape!=(N,2):
        raise ValueError("source sensitivity requires binary receiver rows")
    if mu.shape!=(d,) or Sigma.shape!=(d,d):
        raise ValueError("reference moments must cover all fine coordinates")
    maps=comparison_maps(state.Theta,model)
    nodes=torch.cat((torch.arange(N,device=mu.device)[:,None],model.sources),dim=1)
    index=(nodes[:,:,None]*K+torch.arange(K,device=mu.device)).reshape(N,3*K)
    residual=mu.new_zeros((N,2,K,3*K))         # Local receiver and two sender slots.
    residual[:,:,:,:K]=torch.eye(K,dtype=mu.dtype,device=mu.device)
    residual[:,0,:,K:2*K]=-maps[:,0]
    residual[:,1,:,2*K:]=-maps[:,1]
    hessian=residual.mT@model.H[:,None]@residual
    C=(hessian[:,1]-hessian[:,0])/model.tau
    local_mu=mu[index]
    second=Sigma[index[:,:,None],index[:,None,:]]+local_mu[:,:,None]*local_mu[:,None,:]
    weights=source_posterior(mu.reshape(1,N,K),state,model)[0].prod(-1)
    local=weights[:,None,None]*(C@second@C.mT)
    # Scatter also covers repeated source nodes without dropping sender contributions.
    flat_index=(index[:,:,None]*d+index[:,None,:]).reshape(-1)
    G=mu.new_zeros(d*d).index_add(0,flat_index,local.reshape(-1)).reshape(d,d)
    return (G+G.T)/2


def source_informed_basis(
    mu:    torch.Tensor,                      # (d,), activation mean
    Sigma: torch.Tensor,                      # (d,d), positive-definite activation
    P:     torch.Tensor,                      # (m,d), full-row-rank retained map
    rank:  int,
    state: CoupledState,
    model: CoupledModel,
) -> tuple[torch.Tensor, torch.Tensor]:
    r"""Select W=V_r^T U^T L^{-1} from the conditional-reference sensitivity.

    Sigma=L L^T, U spans ker(P L), and B=L U. Evaluate G at N(mu,B B^T),
    then take leading eigenvectors of B^T G B. Thus W Sigma W^T=I and
    W Sigma P^T=0. Returned eigenvalues are raw, ordered and not clipped.
    Neither future observations nor later schedule entries enter this function.
    """
    d=mu.numel()
    if Sigma.shape!=(d,d) or P.ndim!=2 or P.shape[1]!=d or not 0<len(P)<d:
        raise ValueError("nontrivial retained rows and proper reference moments required")
    if not 0<=rank<=d-len(P):
        raise ValueError("message rank exceeds the hidden dimension")
    L=torch.linalg.cholesky(Sigma)
    torch.linalg.cholesky(P@Sigma@P.T)
    U=torch.linalg.qr(L.T@P.T,mode="complete").Q[:,len(P):]
    B=L@U
    G=source_sensitivity(mu,B@B.T,state,model)
    gram=B.T@G@B
    values,V=torch.linalg.eigh((gram+gram.T)/2)
    if not bool(torch.isfinite(values).all()):
        raise ArithmeticError("nonfinite sensitivity spectrum")
    tolerance=100*torch.finfo(values.dtype).eps*len(values)*max(1.,float(values.abs().max()))
    if float(values.min()) < -tolerance:
        raise ArithmeticError("sensitivity Gram has a materially negative eigenvalue")
    W=torch.linalg.solve_triangular(L.T,U@V.flip(1)[:,:rank],upper=True).T
    return W,values.flip(0)
