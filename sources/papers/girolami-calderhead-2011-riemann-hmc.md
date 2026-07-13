---
type: paper
title: "Riemann Manifold Langevin and Hamiltonian Monte Carlo Methods"
aliases:
  - "Riemann-manifold HMC (Girolami and Calderhead 2011)"
authors:
  - Mark Girolami
  - Ben Calderhead
year: 2011
doi: 10.1111/j.1467-9868.2010.00765.x
url: https://doi.org/10.1111/j.1467-9868.2010.00765.x
tags:
  - cluster/info-geometry
  - project/multi-agent
  - field/statistics
  - field/mathematics
created: 2026-07-12
---

# Riemann Manifold Langevin and Hamiltonian Monte Carlo Methods

> [!info] Citation
> Mark Girolami and Ben Calderhead (2011). “Riemann manifold Langevin and Hamiltonian Monte Carlo methods.” *Journal of the Royal Statistical Society: Series B (Statistical Methodology)* 73(2), 123–214. DOI: [10.1111/j.1467-9868.2010.00765.x](https://doi.org/10.1111/j.1467-9868.2010.00765.x).
>
> Provenance: arXiv:0907.1100 is not used as this note's canonical identifier. Its current withdrawn v3 has a different title and includes Siu A. Chin as a third author, so it no longer matches the published two-author journal article identified by the DOI.

## TL;DR

Girolami and Calderhead define Langevin and Hamiltonian Monte Carlo methods on a position-dependent Riemannian geometry, using a metric such as the Fisher information to adapt proposals to local statistical structure. The paper is an important example of Fisher/Riemannian geometry entering the kinetic term of a Hamiltonian algorithm, while also showing why metric choice must be kept conceptually separate from the curvature of the objective or loss.

## Problem & setting

Standard random-walk, Langevin, and Hamiltonian samplers can mix poorly for high-dimensional or strongly correlated target distributions because a single Euclidean scale cannot represent changing local geometry. The paper addresses Bayesian posterior sampling on statistical parameter manifolds, with demonstrations on logistic regression, log-Gaussian Cox processes, stochastic volatility, and nonlinear dynamical-system inference.

## Method

The authors replace a constant mass matrix with a position-dependent metric tensor $G(q)$ derived from the statistical model's local Riemannian structure. In Hamiltonian form, the momentum distribution depends on $G(q)$, producing a nonseparable Hamiltonian with kinetic contribution $\tfrac12 p^{\mathsf T}G(q)^{-1}p$ and the associated log-determinant term. Generalized integration and Metropolis correction preserve the target distribution; the Langevin construction uses the same local geometry to scale drift and noise.

## Key results

Across the reported inference problems, the Riemann-manifold methods adapt automatically to local scales and correlations and deliver substantial gains in time-normalized effective sample size relative to comparison samplers. The result is algorithmic rather than ontological: the Fisher or related metric is a chosen geometric preconditioner for sampling, not evidence that the posterior loss Hessian, the intrinsic statistical metric, and a physical mass tensor are identical objects.

## Relevance to this research

This paper supplies a precise precedent for using the [[Fisher information metric]] as kinetic geometry. It therefore supports the plausibility of [[Mass as Fisher information]] but also enforces a notation and claim boundary: the intrinsic Fisher metric, the free-energy loss Hessian, and the separately chosen kinetic metric must remain distinct. For [[Hamiltonian belief dynamics]], adopting Fisher geometry in the kinetic term is a defensible modeling choice, not a theorem that follows from scalar damping or from the curvature of variational free energy.

## Cross-links

The primary conceptual links are [[Fisher information metric]], [[Natural gradient]], [[Mass as Fisher information]], [[Hamiltonian belief dynamics]], and [[Belief inertia]]. The paper also complements [[neal-2011-mcmc-hamiltonian]], which provides the standard Euclidean HMC baseline against which the position-dependent geometry is understood.

## BibTeX

```bibtex
@article{GirolamiCalderhead2011,
  author  = {Girolami, Mark and Calderhead, Ben},
  title   = {Riemann Manifold Langevin and Hamiltonian Monte Carlo Methods},
  journal = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
  volume  = {73},
  number  = {2},
  pages   = {123--214},
  year    = {2011},
  doi     = {10.1111/j.1467-9868.2010.00765.x}
}
```
