---
type: paper
title: "DEM: A variational treatment of dynamic systems"
aliases:
  - "Friston 2008"
  - "DEM"
  - "Dynamic Expectation Maximisation"
authors:
  - Friston, Karl J.
  - Trujillo-Barreto, Nelson
  - Daunizeau, Jean
year: 2008
arxiv: null
url: https://doi.org/10.1016/j.neuroimage.2008.02.054
tags:
  - cluster/vfe
  - project/multi-agent
  - field/neuroscience
  - field/statistics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# DEM: A variational treatment of dynamic systems

> [!info] Citation
> Friston, K.J., Trujillo-Barreto, N., & Daunizeau, J. (2008). "DEM: A variational treatment of dynamic systems." NeuroImage, 41, 849–885. https://doi.org/10.1016/j.neuroimage.2008.02.054

## TL;DR
This paper introduces Dynamic Expectation Maximisation (DEM), a variational scheme for inverting nonlinear dynamic causal models formulated as differential equations. The method maximises a variational action (path-integral of free-energy) with respect to conditional densities on trajectories of states and time-invariant densities on parameters and hyperparameters, under a Laplace (Gaussian) fixed-form approximation. By working in generalised coordinates of motion, DEM supports online Bayesian inversion and is shown to outperform Kalman and particle filtering while simultaneously supporting dual and triple inference on states, parameters, and hyperparameters.

## Problem & setting
Classical Bayesian filtering approaches (extended Kalman, particle filters) infer hidden states of dynamical systems but require known parameters and covariances, and assume Wiener (uncorrelated) process noise. DEM addresses the harder triple-inference problem — simultaneous estimation of states, parameters governing deterministic dynamics, and hyperparameters governing random fluctuations — without requiring conjugate priors or closed-form update rules. Prior variational approaches (Valpola & Karhunen 2002; Honkela et al. 2006) used multilayer perceptrons or restricted model classes; DEM applies to any analytic nonlinear model specified only by its likelihood and priors.

## Method
DEM formulates inference as maximisation of a variational action — the path-integral of free-energy, $\bar{F} = \int F(t)\,dt$ — over conditional densities $q(u,t)$ (states) and $q(\vartheta)$ (parameters, hyperparameters), where $F = \langle \ln p(y,\vartheta)\rangle_q + H[q]$ is the standard free-energy lower bound on log-evidence. Under the mean-field factorisation $q(\vartheta) = \prod_i q(\vartheta_i)$ and a Laplace (Gaussian) approximation, the conditional covariance equals the negative curvature of the internal action at the mode, so optimisation reduces to tracking the path of the conditional mode.

The key technical innovation is the use of generalised coordinates of motion $\tilde{u} = (u, u', u'', \ldots)$ — a representation of instantaneous trajectories rather than single states. Ensemble dynamics in this augmented space admit a stationary density in a frame moving with the mode, enabling a fast analytic integration. DEM then iterates three steps:

- **D-step** (dynamics): integrate the conditional mode trajectory $\tilde{\mu}(t)$ via local linearisation using the Jacobian $\mathcal{I} = \nabla^2 V(\tilde{\mu}, t) + D$, where $D$ is the derivative operator shifting generalised coordinates.
- **E-step** (parameters): Gauss-Newton update $\Delta\mu_\theta = -[\nabla^2 \bar{V}(\theta)]^{-1} \nabla \bar{V}(\theta)$ after accumulating the time-integrated variational action.
- **M-step** (hyperparameters): identical form, conditioning on state and parameter uncertainty through mean-field terms $W^{(u)}_\lambda$.

The generative model is a hierarchical nonlinear state-space system $y = g(x,v) + z$, $\dot{x} = f(x,v) + w$ with Gaussian innovations whose precision is linear in hyperparameters, enabling exact M-step updates. Temporal correlations are encoded via a smoothness hyperparameter $\gamma$ controlling the Gaussian autocorrelation of innovations, so DEM is not limited to Wiener processes.

## Key results
DEM (with embedding order $n=6$) accurately recovers the conditional trajectory of causal and hidden states in linear and nonlinear dynamic causal models, outperforming extended Kalman and particle filtering in accuracy of state estimation. For system identification (dual estimation of states and parameters), DEM matches or exceeds EM-based approaches. Triple estimation — simultaneous inference on states, parameters, and hyperparameters — is demonstrated on a linear convolution model and on the nonlinear hemodynamic (Balloon) model used to deconvolve BOLD signals in fMRI, yielding sensible posteriors on neuronal efficacy and hemodynamic parameters. The free-action serves as a principled lower bound on log-evidence, enabling model comparison. The scheme is implemented as a single routine (spm_DEM.m) requiring only the functions $f$ and $g$ without bespoke derivations.

## Relevance to this research
DEM is the foundational algorithmic realisation of the free-energy principle for dynamical systems and is directly ancestral to the VFE transformer. Key connections: (1) the free-energy $F = \langle U \rangle_q + H[q]$ is the same functional minimised in the VFE transformer's E-step, with the Laplace approximation giving Gaussian belief tuples $(\mu, \Sigma)$; (2) the hierarchical structure $h \to s \to p \to q \to o$ of the VFE transformer mirrors DEM's HDM with empirical priors at each level; (3) the D-step's prediction-error-driven update in generalised coordinates is the continuous-time counterpart of the transformer's attention-weighted belief propagation; (4) the mean-field partition of parameters into states/parameters/hyperparameters anticipates the VFE model's $(\mu, \Sigma, \phi)$ tuple with hyper-prior $h$ and model-level $s$; (5) the variational action path-integral framework connects to the active inference / FEP literature directly relevant to the multi-agent model.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Generalised Coordinates]], [[Active Inference]], [[Laplace Approximation]], [[Expectation Maximisation]]
- Related sources: [[friston-2005-fep]], [[friston-2010-fep-unified]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]]

## BibTeX
```bibtex
@article{Friston2008DEM,
  author  = {Friston, Karl J. and Trujillo-Barreto, Nelson and Daunizeau, Jean},
  title   = {{DEM}: A variational treatment of dynamic systems},
  journal = {NeuroImage},
  volume  = {41},
  pages   = {849--885},
  year    = {2008},
  doi     = {10.1016/j.neuroimage.2008.02.054},
}
```
