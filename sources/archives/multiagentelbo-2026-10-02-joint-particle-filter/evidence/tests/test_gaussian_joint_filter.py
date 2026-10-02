"""Tiny exact-identity and mixture checks for assignment-aware particle prediction."""
from __future__ import annotations
from dataclasses import replace
import importlib
import torch
from tests.test_gaussian_joint_parent import _example


def test_mixture_joint_density_normalizes_and_retains_source_observation_coupling() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.joint_filter")
    log_weights = torch.tensor([[.25,.75]],dtype=torch.float64).log()
    source = torch.tensor([[.2,.8]],dtype=torch.float64).log()
    observation = torch.tensor([[.3,.9]],dtype=torch.float64).log()
    log_joint,log_source,ess_source,ess_joint,weights = api.condition_particle_weights(log_weights,source,observation)
    expected_terms = torch.tensor([[.25*.2*.3,.75*.8*.9]],dtype=torch.float64)
    torch.testing.assert_close(log_joint,expected_terms.sum(-1).log())
    torch.testing.assert_close(log_source,torch.tensor([.65],dtype=torch.float64).log())
    torch.testing.assert_close(weights,expected_terms/expected_terms.sum(-1,keepdim=True))
    torch.testing.assert_close(ess_joint,1/weights.square().sum(-1))
    ws = (log_weights+source-log_source[:,None]).exp()
    torch.testing.assert_close(ess_source,1/ws.square().sum(-1))


def test_full_retention_filter_log_density_is_the_native_joint_law() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.joint_filter")
    from multiagent_elbo.realizations.gaussian.switching_paths import sample_switching_history
    model,state,mobility = _example()
    dt=.03
    schedule=(state,replace(state,pi=state.pi.flip(-1)),state)
    history=sample_switching_history(mobility,state,schedule,model,dt,4,92)
    R=history.paths.flatten(2)
    result=api.particle_joint_scores(R,history.assignments,mobility,state,schedule,model,dt,1,5,130)
    noise=torch.distributions.MultivariateNormal(torch.zeros(3,dtype=R.dtype),
                                                covariance_matrix=2*dt*torch.block_diag(*mobility))
    expected=history.log_source_kernel+noise.log_prob((history.paths[:,1:]-history.conditional_means).flatten(2))
    torch.testing.assert_close(result["log_joint"],expected,atol=2e-12,rtol=2e-12)
    torch.testing.assert_close(result["source_ess"],torch.full((4,3),5.,dtype=R.dtype))
    torch.testing.assert_close(result["joint_ess"],torch.full((4,3),5.,dtype=R.dtype))
    assert result["projection_max_error"] < 2e-14


def test_particle_filter_replays_tape_and_prefix_without_future_input() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.joint_filter")
    from multiagent_elbo.realizations.gaussian.switching_paths import sample_switching_history
    model,state,mobility = _example()
    history=sample_switching_history(mobility,state,(state,)*3,model,.02,3,41)
    R=history.paths.mean(-2)
    args=(R,history.assignments,mobility,state,(state,)*3,model,.02,3,7,57)
    result=api.particle_joint_scores(*args)
    repeated=api.particle_joint_scores(*args)
    prefix=api.particle_joint_scores(R[:,:2],history.assignments[:,:2],mobility,state,(state,),model,.02,3,7,57)
    for key in ("log_joint","log_source","source_ess","joint_ess"):
        torch.testing.assert_close(result[key],repeated[key],atol=0.,rtol=0.)
        torch.testing.assert_close(result[key][:,:1],prefix[key],atol=0.,rtol=0.)
        assert torch.isfinite(result[key]).all()
    assert (result["joint_ess"]>=1-1e-12).all() and (result["joint_ess"]<=7+1e-12).all()
    assert result["projection_max_error"] < 2e-14


def test_baseline_scores_actual_joint_observations_with_gaussian_normalizers() -> None:
    api = importlib.import_module("multiagent_elbo.realizations.gaussian.joint_filter")
    from multiagent_elbo.realizations.gaussian.switching_paths import (
        sample_switching_history,source_posterior,sheet_force)
    from multiagent_elbo.realizations.gaussian.coupled_learning import free_energy
    model,state,mobility = _example()
    dt=.02
    history=sample_switching_history(mobility,state,(state,)*2,model,dt,3,21)
    R=history.paths.mean(-2)
    actual=api.lifted_baseline_log_scores(R,history.assignments,mobility,state,(state,)*2,model,dt,3)
    Sigma=torch.block_diag(*state.Sigma)
    P=torch.full((1,3),1/3,dtype=R.dtype)
    gain=torch.linalg.solve(P@Sigma@P.T,P@Sigma).T
    C=2*dt*P@torch.block_diag(*mobility)@P.T
    probability=-torch.expm1(torch.tensor(-dt,dtype=R.dtype))
    expected=[]
    for t in range(2):
        X=(state.mu.flatten()+(R[:,t]-state.mu.flatten()@P.T)@gain.T).reshape(3,3,1)
        new,old=history.assignments[:,t+1],history.assignments[:,t]
        beta=source_posterior(X,state,model)
        redraw=beta.gather(-1,new[...,None]).squeeze(-1).prod(-1)
        log_source=((1-probability)*(new==old).all(-1)+probability*redraw).log()
        force=sheet_force(X,free_energy(state,model)[1],state.Theta,model)
        mean=(X-dt*torch.einsum("nij,bnj->bni",mobility,force)).flatten(1)@P.T
        density=torch.distributions.MultivariateNormal(mean,covariance_matrix=C)
        expected.append(log_source+density.log_prob(R[:,t+1]))
    torch.testing.assert_close(actual,torch.stack(expected,1),atol=2e-12,rtol=2e-12)
