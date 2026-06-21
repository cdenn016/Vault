---
type: paper
title: "Estimating the Dimension of a Model"
aliases:
  - Schwarz 1978
  - Schwarz (1978) BIC
authors:
  - Schwarz, Gideon
year: 1978
arxiv: null
url: http://www.jstor.org/stable/2958889
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Estimating the Dimension of a Model

> [!info] Citation
> Schwarz, G. (1978). "Estimating the Dimension of a Model." *The Annals of Statistics*, 6(2), 461–464. DOI: [10.1214/aos/1176344136](https://doi.org/10.1214/aos/1176344136). http://www.jstor.org/stable/2958889

## TL;DR
Schwarz derives a Bayesian criterion for selecting among statistical models of differing complexity. By approximating the marginal likelihood of each model via Laplace's method, he arrives at the Bayesian Information Criterion (BIC): maximize the log-likelihood penalized by (d/2) log n, where d is the number of free parameters and n is the sample size. The criterion is consistent — it selects the true model dimension with probability one as n → ∞.

## Problem & setting
Given observations from an exponential-family distribution, one wants to select among a finite collection of nested parametric models of increasing dimension without overfitting. The classical Akaike Information Criterion (AIC) penalizes complexity by d but is not consistent. Schwarz seeks a Bayesian, large-sample justification for a stronger penalty that ensures asymptotic consistency.

## Method
Under a prior that assigns positive probability to each model dimension, the posterior probability of model M_d given data X^n is proportional to the marginal likelihood p(X^n | M_d). Schwarz expands log p(X^n | M_d) around the MLE using a Laplace approximation:

$$\log p(X^n \mid M_d) \approx \log p(X^n \mid \hat{\theta}_d) - \frac{d}{2}\log n + O(1)$$

where the O(1) term is independent of n and asymptotically negligible relative to the penalty. The BIC score for model M_d is therefore:

$$\mathrm{BIC}(d) = \log p(X^n \mid \hat{\theta}_d) - \frac{d}{2}\log n$$

Selection is by maximizing BIC over d. The derivation assumes the observations are i.i.d. from an exponential family and the true model lies in the candidate set.

## Key results
The main result is that maximizing BIC yields a consistent model-dimension estimator: if the true dimension is d*, then the dimension selected by BIC converges to d* almost surely as n → ∞. This contrasts with AIC (penalty d), which over-selects larger models with positive asymptotic probability. The (d/2) log n penalty arises directly from the log-determinant of the Fisher information matrix in the Laplace approximation to the marginal likelihood.

## Relevance to this research
BIC is directly connected to the variational free energy (VFE) framework at the model-selection level. The free energy F = −ELBO = KL(q ∥ p) − log p(o) is a variational upper bound on the negative log marginal likelihood; Schwarz's Laplace approximation gives the leading asymptotic term of that same quantity. In the VFE transformer, the hyper-prior KL term λ_h KL(s_i ∥ h) plays an analogous complexity-penalization role at the level of model beliefs s_i — preferring simpler (lower-dimensional, centroid-hugging) model representations. The BIC derivation also underpins the interpretation of the Fisher information geometry (SPD matrices) as the natural curvature of the Laplace approximation, linking directly to the SPD belief geometry (Σ matrices) used throughout the GL(K) attention layers.

## Cross-links
- Concepts: [[Variational Free Energy]], [[MDL and BIC model selection|Model Selection]], [[Laplace Approximation]], [[Fisher information metric|Fisher Information]], [[SPD-manifold geometry and Riemannian optimization|SPD Geometry]], [[MDL and BIC model selection]]
- Themes: [[Meta-agents and hierarchical emergence]]
- Related sources: [[akaike-1974-aic]], [[rissanen-1978-mdl]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]], [[participatory-it-from-bit]]

> [!note] Editorial: For the multi-agent thread, BIC is one of the two retention criteria used when forming [[Meta-agents and hierarchical emergence|meta-agents]] by coarse-graining clusters of agents: a candidate coarse parent (adding $k$ parameters) is kept only if the gain in fit outweighs the $\tfrac{1}{2}k\log n$ complexity penalty, giving the hierarchy-growth rule a principled Bayesian footing. As the asymptotic Bayesian counterpart of MDL ([[rissanen-1978-mdl]]), it anchors the [[MDL and BIC model selection]] page.

## BibTeX
```bibtex
@article{Schwarz1978,
  author  = {Schwarz, Gideon},
  title   = {Estimating the Dimension of a Model},
  journal = {The Annals of Statistics},
  year    = {1978},
  volume  = {6},
  number  = {2},
  pages   = {461--464},
  doi     = {10.1214/aos/1176344136},
  publisher = {Institute of Mathematical Statistics},
  url     = {http://www.jstor.org/stable/2958889},
}
```
