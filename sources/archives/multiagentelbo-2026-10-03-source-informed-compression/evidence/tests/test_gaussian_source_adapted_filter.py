"""Tiny joint-law checks for deterministic Gaussian source adaptation."""
from __future__ import annotations
import importlib
import torch
from tests.test_gaussian_joint_parent import _example
from multiagent_elbo.realizations.gaussian.switching_paths import sample_switching_history


def test_full_retention_matches_native_joint_density() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_adapted_filter")
    model,state,mobility = _example()
    dt=.03
    schedule=(state,)*3
    history=sample_switching_history(mobility,state,schedule,model,dt,4,92)
    R=history.paths.flatten(2)
    result=api.gaussian_joint_scores(R,history.assignments,mobility,state,schedule,model,dt,1)
    noise=torch.distributions.MultivariateNormal(torch.zeros(3,dtype=R.dtype),covariance_matrix=2*dt*torch.block_diag(*mobility))
    expected=history.log_source_kernel+noise.log_prob((history.paths[:,1:]-history.conditional_means).flatten(2))
    torch.testing.assert_close(result["log_joint"],expected,atol=2e-12,rtol=2e-12)
    torch.testing.assert_close(result["log_source"],history.log_source_kernel,atol=2e-12,rtol=2e-12)
    assert result["projection_max_error"] < 2e-14


def test_replay_and_prefix_are_deterministic_and_causal() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_adapted_filter")
    model,state,mobility = _example()
    schedule=(state,)*3
    history=sample_switching_history(mobility,state,schedule,model,.02,3,41)
    R=history.paths.mean(-2)
    args=(R,history.assignments,mobility,state,schedule,model,.02,3)
    result=api.gaussian_joint_scores(*args,shortcut_mass=.1)
    repeated=api.gaussian_joint_scores(*args,shortcut_mass=.1)
    prefix=api.gaussian_joint_scores(R[:,:2],history.assignments[:,:2],mobility,state,(state,),model,.02,3,shortcut_mass=.1)
    for key in ("log_joint","log_source","source_updates","shortcut"):
        torch.testing.assert_close(result[key],repeated[key],atol=0.,rtol=0.)
        torch.testing.assert_close(result[key][:,:1],prefix[key],atol=0.,rtol=0.)
    assert torch.isfinite(result["log_joint"]).all()
    assert result["projection_max_error"] < 2e-14
    assert result["covariance_projection_max_error"] < 2e-14


def test_unchanged_assignment_keeps_refresh_mass_and_hold_gaussian() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.source_adapted_filter")
    messages=importlib.import_module("multiagent_elbo.realizations.gaussian.gaussian_message")
    sources=importlib.import_module("multiagent_elbo.realizations.gaussian.source_gaussian")
    model,state,mobility = _example()
    dt=.02
    R=torch.tensor([[[.15],[.2]]],dtype=state.mu.dtype)
    J=torch.zeros((1,2,3),dtype=torch.long)
    initial=messages.observe_gaussian(state.mu[None],torch.block_diag(*state.Sigma)[None],R[:,0],3)
    source=sources.sequential_source_message(initial["mean"],initial["covariance"],J[:,0],J[:,1],state,model,3)
    mean,cov=messages.propagate_gaussian(initial["mean"],initial["covariance"],J[:,1],mobility,state,model,dt)
    conditional=messages.observe_gaussian(mean,cov,R[:,1],3)
    p=-torch.expm1(R.new_tensor(-dt))
    expected=torch.logaddexp(R.new_tensor(-dt),p.log()+source["log_refresh"])
    result=api.gaussian_joint_scores(R,J,mobility,state,(state,),model,dt,3)
    torch.testing.assert_close(result["log_source"][:,0],expected)
    torch.testing.assert_close(result["log_joint"][:,0],expected+conditional["log_density"])
    assert (result["log_source"][:,0]>-dt).all()
