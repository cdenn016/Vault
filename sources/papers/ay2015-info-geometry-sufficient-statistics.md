---
type: paper
title: "Information Geometry and Sufficient Statistics"
aliases:
  - "Ay 2015"
  - "Ay Jost Le Schwachhofer 2015"
authors:
  - Ay, Nihat
  - Jost, Jürgen
  - Lê, Hông Vân
  - Schwachhöfer, Lorenz
year: 2015
arxiv: "1207.6736"
url: https://arxiv.org/abs/1207.6736
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Information Geometry and Sufficient Statistics

> [!info] Citation
> Ay, N., Jost, J., Lê, H.V., & Schwachhöfer, L. (2015). "Information Geometry and Sufficient Statistics." arXiv:1207.6736. (Published 2015.)

## TL;DR
This paper establishes a rigorous foundation for information geometry on infinite-dimensional statistical models by introducing the notion of k-integrable parametrized measure models, which allow pullback of geometric structures from the universal measure space. The main result proves that the Fisher metric and the Amari-Chentsov tensor are the unique (up to a constant) invariant symmetric 2- and 3-tensor fields under sufficient statistics, extending Chentsov's classical finite-sample theorem to infinite sample spaces. Additionally, Markov morphisms between statistical models are decomposed in terms of sufficient statistics, yielding a geometric proof of the monotonicity theorem for Fisher information.

## Problem & setting
Classical information geometry (Chentsov, Amari) characterizes the Fisher metric and the Amari-Chentsov tensor as the unique geometric structures invariant under sufficient statistics, but only for finite sample spaces. Extending these uniqueness results to infinite sample spaces is non-trivial: the space of probability measures on an infinite space is infinite-dimensional, the standard differential-geometric constructions break down, and Pistone-Sempi's Banach manifold approach encounters topological obstructions (e.g., bounded random variables are not dense in the Orlicz-based topology). The central question is whether the same characterization theorems hold for parametrized families of measures on infinite or continuous sample spaces.

## Method
The authors introduce k-integrable parametrized measure models: a Banach manifold $M$ together with a smooth map $p: M \to M^+(\Omega, \mu)$ (into positive measures) whose log-density $\ln \bar{p}(x, \omega)$ is continuously Gateaux-differentiable and whose score function $\partial_V \ln \bar{p}(x, \omega)$ lies in $L^k(\Omega, p(x))$. This avoids the need to define tensor fields directly on the infinite-dimensional measure space $M(\Omega)$; instead, tensors are pulled back to $M$ via $p$.

The Fisher quadratic form and Amari-Chentsov 3-tensor are then defined on any 3-integrable parametrized measure model as:
$$g^F(V,W)_x = \int_\Omega \partial_V \ln\bar{p}(x,\omega)\,\partial_W \ln\bar{p}(x,\omega)\,dp(x),$$
$$T^{AC}(V,W,X)_x = \int_\Omega \partial_V \ln\bar{p}\cdot\partial_W \ln\bar{p}\cdot\partial_X \ln\bar{p}\,dp(x).$$
A sufficient statistic $\kappa: (\Omega_1, \mu_1) \to \Omega_2$ is characterized via the Fisher-Neyman factorization $\bar{p}_1(x, \omega_1) = s(x, \kappa(\omega_1))\,t(\omega_1)$, which implies $\partial_V \ln p_1(x, \omega_1) = \partial_V \ln \kappa_*(p_1(x))(\kappa(\omega_1))$ almost everywhere, and hence invariance of the Amari-Chentsov structure. Markov morphisms are maps between parametrized measure models that include smooth maps on parameter spaces, and the paper decomposes any Markov morphism as the composition of the inverse of a sufficient-statistic-induced morphism and an ordinary statistic.

## Key results
The Main Theorem (Theorem 2.10) establishes three uniqueness results for local, weakly continuous, sufficient-statistic-invariant tensor fields on statistical models:
1. The only invariant weakly continuous 1-form field is zero (on statistical models, where it must vanish by normalization).
2. The Fisher quadratic form is the unique (up to a constant) invariant weakly continuous quadratic form field.
3. The Amari-Chentsov tensor is the unique (up to a constant) invariant weakly continuous symmetric 3-tensor field.

Theorem 3.5 proves invariance of the Amari-Chentsov structure under sufficient statistics directly from the Fisher-Neyman characterization. Theorem 3.10 gives a geometric proof of the Fisher-Neyman factorization theorem under smoothness. The Monotonicity Theorem (Theorem 3.11) shows $\tilde{g}^F(V,V)_x \le g^F(V,V)_x$ for any statistic, with equality if and only if the statistic is sufficient, proving that sufficient statistics are the only information-preserving transformations.

## Relevance to this research
Information geometry provides the underlying geometric language for the VFE transformer's belief geometry and variational free energy minimization. The Fisher metric and the Amari-Chentsov tensor are the canonical geometric structures on the space of probability distributions used throughout the gauge-theoretic VFE framework — the SPD belief geometry for Gaussian beliefs $(mu, \Sigma, \phi)$ is precisely the information-geometric structure on Gaussian families. The uniqueness theorems here justify why the Fisher metric is the natural metric on the belief manifold (it is the only one invariant under sufficient statistics), directly underpinning the theoretical grounding of the KL divergence terms in the free energy functional. The monotonicity of Fisher information under statistics also connects to the information-processing inequality invoked in the VFE hierarchy ($h \to s \to p \to q \to$ observations), where each level compresses information. The Markov morphism framework resonates with the Markov blanket structure central to active inference and multi-agent VFE.

## Cross-links
- Concepts: [[Information Geometry]], [[Fisher information metric|Fisher Metric]], [[Amari-Chentsov Tensor]], [[Sufficient Statistics]], [[SPD-manifold geometry and Riemannian optimization|SPD Geometry]]
- Related sources: [[amari-1985-differential-geometric-methods|amari1985-differential-geometric-methods]], [[cencov-1982-statistical-decision-rules|chentsov1982-statistical-decision-rules]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@article{Ay2015,
  author  = {Ay, Nihat and Jost, J{\"u}rgen and L{\^e}, H{\^o}ng V{\^a}n and Schwachh{\"o}fer, Lorenz},
  title   = {Information Geometry and Sufficient Statistics},
  journal = {Probability Theory and Related Fields},
  year    = {2015},
  eprint  = {1207.6736},
  archivePrefix = {arXiv},
  primaryClass  = {math.ST},
}
```
