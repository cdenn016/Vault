"""Tiny checks for a reference-conditioned compressed Gaussian message."""
from __future__ import annotations
import importlib
import numpy as np
import torch
from tests.test_gaussian_joint_parent import _example
from multiagent_elbo.realizations.gaussian.source_adapted_filter import gaussian_joint_scores
from multiagent_elbo.realizations.gaussian.switching_paths import sample_switching_history


def test_decoder_matches_independent_conditional_mixture() -> None:
    api=importlib.import_module("multiagent_elbo.realizations.gaussian.gaussian_compression")
    mu=torch.tensor([.2,-.1,.3,.7],dtype=torch.float64)
    B=torch.tensor([[1.,.2,0,0],[.1,1.2,.1,0],[0,.2,.9,.1],[.1,0,.2,1.1]],dtype=mu.dtype)
    Sigma=B@B.T
    P=mu.new_tensor([[.5,.5,0,0],[0,0,.5,.5]])
    W=mu.new_tensor([[1.,-1,0,0]])
    decoder=api.compile_compression(mu,Sigma,P,W)
    R=mu.new_tensor([[.4,-.2]]);m=mu.new_tensor([[.6]]);S=mu.new_tensor([[[.7]]])
    mean,cov=decoder.decode(R,m,S)
    H=np.concatenate([P.numpy(),W.numpy()]);sig=Sigma.numpy()
    gain=np.linalg.solve(H@sig@H.T,H@sig).T
    expected_mean=mu.numpy()+gain@(np.r_[R[0].numpy(),m[0].numpy()]-H@mu.numpy())
    expected_cov=sig-gain@H@sig+gain[:,2:]@S[0].numpy()@gain[:,2:].T
    np.testing.assert_allclose(mean[0],expected_mean,atol=2e-14)
    np.testing.assert_allclose(cov[0],expected_cov,atol=2e-14)
    torch.testing.assert_close(mean@P.T,R,atol=2e-14,rtol=0.)
    torch.testing.assert_close(cov@P.T,torch.zeros((1,4,2),dtype=mu.dtype),atol=2e-14,rtol=0.)
    encoded=decoder.encode(mean,cov)
    torch.testing.assert_close(encoded[0],m,atol=2e-14,rtol=0.)
    torch.testing.assert_close(encoded[1],S,atol=2e-14,rtol=0.)


def test_rank_zero_and_full_hidden_recover_existing_scorers() -> None:
    api=importlib.import_module("multiagent_elbo.realizations.gaussian.gaussian_compression")
    model,state,mobility=_example();dt=.03;schedule=(state,)*4
    history=sample_switching_history(mobility,state,schedule,model,dt,2,219,refresh_rate=25.)
    R=history.paths.mean(-2);P=state.mu.new_full((1,3),1/3)
    hidden=torch.linalg.qr(P.T,mode="complete").Q[:,1:].T
    args=(R,history.assignments,mobility,state,schedule,model,dt,3)
    for rows,reset in ((hidden,False),(hidden[:0],True)):
        decoder=api.compile_compression(state.mu.flatten(),torch.block_diag(*state.Sigma),P,rows)
        actual=gaussian_joint_scores(*args,refresh_rate=25.,compression=decoder)
        expected=gaussian_joint_scores(*args,refresh_rate=25.,reset_each_step=reset)
        for key in ("log_joint","log_source"):
            torch.testing.assert_close(actual[key],expected[key],atol=2e-11,rtol=2e-11)
        assert actual["message_scalars"]==len(rows)+len(rows)**2
        assert actual["projection_max_error"]<1e-12
        assert actual["covariance_projection_max_error"]<1e-12


def test_compressed_history_is_causal_and_uses_only_declared_coordinates() -> None:
    api=importlib.import_module("multiagent_elbo.realizations.gaussian.gaussian_compression")
    model,state,mobility=_example();dt=.03;schedule=(state,)*3
    history=sample_switching_history(mobility,state,schedule,model,dt,2,23,refresh_rate=25.)
    R=history.paths.mean(-2);P=state.mu.new_full((1,3),1/3);W=state.mu.new_tensor([[1.,-1.,0.]])
    decoder=api.compile_compression(state.mu.flatten(),torch.block_diag(*state.Sigma),P,W)
    result=gaussian_joint_scores(R,history.assignments,mobility,state,schedule,model,dt,3,refresh_rate=25.,compression=decoder)
    prefix=gaussian_joint_scores(R[:,:2],history.assignments[:,:2],mobility,state,schedule[:1],model,dt,3,refresh_rate=25.,compression=decoder)
    torch.testing.assert_close(result["log_joint"][:,:1],prefix["log_joint"],atol=0.,rtol=0.)
    assert result["message_scalars"]==2
    assert torch.isfinite(result["log_joint"]).all()
