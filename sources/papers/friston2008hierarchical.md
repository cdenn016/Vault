---
type: paper
title: "Hierarchical Models in the Brain"
aliases:
  - "HDM DEM"
authors:
  - Friston, Karl
year: 2008
arxiv: null
url: https://doi.org/10.1371/journal.pcbi.1000211
tags:
  - cluster/vfe
  - project/multi-agent
  - field/neuroscience
  - field/statistics
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Hierarchical Models in the Brain

> [!info] Citation
> Friston, K. (2008). "Hierarchical Models in the Brain." *PLoS Computational Biology*, 4(11): e1000211. https://doi.org/10.1371/journal.pcbi.1000211

## TL;DR
This paper introduces hierarchical dynamic models (HDMs) formulated in generalised coordinates of motion and shows that a single variational inversion scheme — Dynamic Expectation Maximisation (DEM) — can invert the entire class. Special cases of the HDM subsume PCA, factor analysis, ICA, sparse coding, Kalman filtering, blind deconvolution, general linear models, and Gaussian process models, all unified under a free-energy framework. The paper further demonstrates that the resulting D/E/M-step gradient ascent on variational action can be implemented as a biologically plausible neural network with forward (prediction-error) and backward (prediction) message passing between cortical hierarchies.

## Problem & setting
Classical time-series methods (Kalman filtering, particle filtering) restrict noise to Markovian (uncorrelated) processes, discarding generalised motion and thus missing empirical priors encoded in temporal autocorrelations. Prior variational approaches handled hierarchical structure in static models or specialised dynamic models separately. The goal is a unified generative model flexible enough to cover both structural (cross-level) and dynamical (cross-time) empirical priors, invertible by one generic optimisation procedure.

## Method
HDMs are probabilistic state-space models arranged in levels, where the output of level $i+1$ provides input to level $i$:

$$y = g(x^{(1)}, v^{(1)}) + z^{(1)}, \quad \dot{x}^{(i)} = f(x^{(i)}, v^{(i)}) + w^{(i)}, \quad v^{(i-1)} = g(x^{(i)}, v^{(i)}) + z^{(i)}$$

States and causes are expressed in generalised coordinates of motion $\tilde{x} = [x, x', x'', \ldots]^T$, encoding the full local trajectory. Under Gaussian assumptions, the joint log-model is a quadratic in precision-weighted prediction errors $\tilde{\varepsilon}$:

$$\ln p(\tilde{y}, \tilde{x}, \tilde{v} \mid \theta, \lambda) = \tfrac{1}{2} \ln |\tilde{\Pi}| - \tfrac{1}{2} \tilde{\varepsilon}^T \tilde{\Pi} \tilde{\varepsilon}$$

Inversion proceeds via variational Bayes with a mean-field Laplace approximation $q(W) = q(u(t))q(\theta)q(\lambda)$. The resulting DEM algorithm alternates three steps: the D-step (states) integrates the ansatz $\dot{\tilde{m}} - D\tilde{m} = V_u^{(t)}$ to find conditional trajectories in a moving frame of reference; the E-step (parameters) runs a Gauss-Newton update on variational action accumulated over the full time-series; the M-step (hyperparameters) estimates precision parameters similarly. Conditional covariances come directly from the negative curvature of the internal action, avoiding explicit matrix inversions of the full state-space.

## Key results
DEM recovers hidden states, parameters, and hyperparameters jointly in a triple estimation problem, outperforming extended Kalman filtering and particle filtering on accuracy by exploiting generalised-coordinate empirical priors. The paper demonstrates exact recovery in a linear convolution model (two hidden states, four outputs) and shows that truncating generalised coordinates at order $n = 6$ (roughness $c = 4$) retains full numerical precision. Specialising HDM constraints yields exact correspondences to the GLM, ReML, PCA, factor analysis, ICA, sparse coding, Gaussian process models, and state-space/Kalman models. The neuronal implementation maps D-step updates to superficial pyramidal cells (forward, prediction-error connections) and E-step predictions to deep pyramidal cells (backward connections), consistent with known laminar anatomy of cortical hierarchies.

## Relevance to this research
This paper is a foundational reference for the VFE transformer program. The HDM free-energy functional $F = \langle \ln p(\tilde{y}, W) \rangle_q - \langle \ln q(W) \rangle_q$ is the ancestral form of the variational free energy minimised at each layer of the VFE transformer. The hierarchical prediction-error architecture — precision-weighted $\tilde{\Pi}\tilde{\varepsilon}$ signals flowing upward, generative predictions flowing downward — is structurally analogous to the belief-coupling terms $\beta_{ij} \mathrm{KL}(q_i \| \Omega_{ij} q_j)$ and the self-coupling $\alpha \mathrm{KL}(q_i \| p_i)$ in the VFE transformer's free-energy functional. The mean-field partition $q(u)q(\theta)q(\lambda)$ over states, parameters, and hyperparameters mirrors the VFE hierarchy $h \to s \to p \to q \to o$. The generalised-coordinates trick for handling smooth non-Markovian noise is directly relevant to designing temporally correlated belief updates in the transformer. In the multi-agent active-inference setting, the hierarchical empirical priors (higher levels constraining lower levels) map onto the hyper-prior term $\lambda_h \mathrm{KL}(s_i \| h)$ coupling individual models to a shared centroid.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Predictive Coding]], [[Active Inference]], [[Belief Propagation]]
- Related sources: [[friston-2003-learning-inference-brain|friston2003learning]], [[friston-2005-cortical-responses|friston2005theory]], [[friston-2010-free-energy-principle|friston2010free]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@article{friston2008hierarchical,
  author  = {Friston, Karl},
  title   = {Hierarchical Models in the Brain},
  journal = {PLoS Computational Biology},
  year    = {2008},
  volume  = {4},
  number  = {11},
  pages   = {e1000211},
  doi     = {10.1371/journal.pcbi.1000211},
}
```
