"""Deterministic Gaussian joint prediction on the observed block-mean fiber."""
from __future__ import annotations
from collections.abc import Sequence
import torch
from typing import Optional
from .gaussian_compression import GaussianCompression
from .coupled_learning import CoupledModel, CoupledState
from .gaussian_message import observe_gaussian, propagate_gaussian
from .source_gaussian import sequential_source_message


def gaussian_joint_scores(
    R:               torch.Tensor,           # (B,H+1,C*K), actual retained history
    assignments:     torch.Tensor,           # (B,H+1,N), complete source labels
    mobility:        torch.Tensor,           # (N,K,K)
    initial:         CoupledState,
    schedule:        Sequence[CoupledState],
    model:           CoupledModel,
    dt:              float,
    block_size:      int,
    refresh_rate:    float = 1.,
    shortcut_mass:   float = 0.,
    reset_each_step: bool = False,
    compression:     Optional[GaussianCompression] = None,
) -> dict[str, torch.Tensor | float | int]:
    r"""Score normalized k_hat(J_next|history) g_hat(R_next|history,J_next).

    Carry a dense Gaussian on each observed fiber. Ascending source cubature
    supplies a normalized refresh law and an adapted Gaussian. If the complete
    assignment is unchanged, use the original hold Gaussian for propagation,
    retaining both hold and same-assignment refresh in the source probability.
    This economical convention is an approximation to the full two-branch
    posterior. Changed assignments use the adapted refresh Gaussian.

    The reset control discards past messages at each step. Neither arm is an
    exact native filter or an admitted continuous-time O1 closure. Optional
    compression stores only W X moments between steps and lifts them through
    a fixed activation conditional. Dense temporary moments remain necessary.
    """
    if dt <= 0 or refresh_rate < 0 or not schedule:
        raise ValueError("positive time step, nonnegative refresh, and schedule required")
    B,H = len(R),len(schedule)
    N,K = initial.mu.shape
    if block_size < 1 or N % block_size:
        raise ValueError("block size must divide the agent count")
    if R.shape != (B,H+1,N//block_size*K) or assignments.shape != (B,H+1,N):
        raise ValueError("retained histories must cover the declared microsteps")
    if compression is not None:
        P = R.new_zeros((N//block_size*K,N*K))
        for i in range(N):
            for k in range(K):
                P[(i//block_size)*K+k,i*K+k] = 1/block_size
        if compression.P.shape != P.shape or not torch.equal(compression.P,P):
            raise ValueError("compression must retain the scorer's exact block means")
    log_hold = R.new_tensor(-refresh_rate*dt)
    log_refresh_coin = torch.log(-torch.expm1(log_hold))
    activation_cov = torch.block_diag(*initial.Sigma).expand(B,-1,-1)
    activation_mean = initial.mu.expand(B,N,K)
    result = {name:R.new_empty((B,H)) for name in ("log_joint","log_source")}
    result["source_updates"] = torch.empty((B,H),dtype=torch.long,device=R.device)
    result["shortcut"] = torch.empty((B,H),dtype=torch.bool,device=R.device)
    max_mean_error,max_cov_error = 0.,0.
    message = None
    for t,state in enumerate(schedule):
        if t == 0 or reset_each_step:
            message = observe_gaussian(activation_mean,activation_cov,R[:,t],block_size)
            if compression is not None:
                message = compression.encode(message["mean"].flatten(1),message["covariance"])
        if compression is None:
            mu,cov = message["mean"],message["covariance"]
        else:
            mu,cov = compression.decode(R[:,t],*message)
            mu = mu.reshape(B,N,K)
            observed = mu.reshape(B,N//block_size,block_size,K).mean(2).flatten(1)
            max_mean_error = max(max_mean_error,float((observed-R[:,t]).abs().max()))
            max_cov_error = max(max_cov_error,float((cov@compression.P.T).abs().max()))
        source = sequential_source_message(mu,cov,assignments[:,t],assignments[:,t+1],
                                            state,model,block_size,shortcut_mass)
        same = (assignments[:,t+1] == assignments[:,t]).all(-1)
        held = torch.where(same,log_hold,-torch.inf)
        log_source = torch.logaddexp(held,log_refresh_coin+source["log_refresh"])
        adapted_mu = torch.where(same[:,None,None],mu,source["mean"])
        adapted_cov = torch.where(same[:,None,None],cov,source["covariance"])
        mean,covariance = propagate_gaussian(adapted_mu,adapted_cov,assignments[:,t+1],
                                             mobility,state,model,dt)
        message = observe_gaussian(mean,covariance,R[:,t+1],block_size)
        result["log_source"][:,t] = log_source
        result["log_joint"][:,t] = log_source+message["log_density"]
        result["source_updates"][:,t] = source["updates"]
        result["shortcut"][:,t] = source["shortcut"]
        observed_mean = message["mean"].reshape(B,N//block_size,block_size,K).mean(2).flatten(1)
        cov_Pt = message["covariance"].reshape(B,N*K,N//block_size,block_size,K).mean(3)
        max_mean_error = max(max_mean_error,float((observed_mean-R[:,t+1]).abs().max()))
        max_cov_error = max(max_cov_error,float(cov_Pt.abs().max()))
        if compression is not None:
            message = compression.encode(message["mean"].flatten(1),message["covariance"])
        # Fine moments are workspace for this step, not compressed history state.
        del mu,cov,source,adapted_mu,adapted_cov,mean,covariance,cov_Pt,observed_mean
    rank = N*K if compression is None else len(compression.W)
    return {**result,"projection_max_error":max_mean_error,
            "covariance_projection_max_error":max_cov_error,
            "message_scalars":rank+rank*rank}
