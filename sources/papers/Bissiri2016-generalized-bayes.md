---
type: paper
title: "A General Framework for Updating Belief Distributions"
aliases:
  - "Bissiri 2016"
  - "BHW2016"
  - "Generalized Bayes"
authors:
  - Bissiri, Pier Giovanni
  - Holmes, Chris C.
  - Walker, Stephen G.
year: 2016
arxiv: null
url: https://doi.org/10.1111/rssb.12158
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A General Framework for Updating Belief Distributions

> [!info] Citation
> Bissiri, P. G., Holmes, C. C., & Walker, S. G. (2016). "A general framework for updating belief distributions." *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, 78(5), 1103–1130. https://doi.org/10.1111/rssb.12158

## TL;DR

Bissiri, Holmes, and Walker derive an axiomatic characterization of rational belief updating via a general loss function rather than a likelihood. They show that the unique coherent update of a prior $\pi$ given a loss $\ell(x, \theta)$ and data $x$ is the Gibbs posterior $\pi^*(\theta) \propto \pi(\theta) \exp(-w \ell(x, \theta))$, where $w > 0$ is a learning-rate or "temperature" parameter. This generalizes Bayes' theorem — standard Bayes emerges when $\ell = -\log p(x|\theta)$ — and connects Bayesian inference to variational free-energy minimization: the posterior is the minimizer of $\mathbb{E}_\pi[\ell] + \frac{1}{w} \mathrm{KL}(\pi \| \pi_0)$.

## Problem & setting

Standard Bayesian updating requires a fully specified generative model (likelihood $p(x|\theta)$). In misspecified, semi-parametric, or otherwise intractable settings this is unavailable or misleading. The paper asks: what is the rational belief update when only a loss function $\ell : \mathcal{X} \times \Theta \to \mathbb{R}$ is available, measuring how well parameter $\theta$ "fits" data $x$? Prior work (PAC-Bayes, Gibbs posteriors) had used such updates pragmatically; this paper provides an axiomatic justification via coherence conditions (self-consistency, continuity, marginalization).

## Method

The main result is a representation theorem. Given a prior $\pi_0$ on $\Theta$ and a loss $\ell(x, \theta)$, any belief update $\pi_0 \mapsto \pi^*$ satisfying the coherence axioms (invariance under sufficiency, continuity, and a "learning sequence" composition property) must take the form

$$\pi^*(\theta \mid x) \propto \pi_0(\theta) \exp\!\bigl(-w\,\ell(x,\theta)\bigr), \quad w > 0.$$

This Gibbs/exponential-tilt update is equivalently the solution to the variational problem

$$\pi^* = \arg\min_\pi \Bigl[\mathbb{E}_\pi[\ell(x,\theta)] + \tfrac{1}{w}\,\mathrm{KL}(\pi \,\|\, \pi_0)\Bigr],$$

making the connection to variational inference and ELBO optimization explicit. The KL term acts as a regularizer penalizing departure from the prior, and $w$ controls the trade-off (analogous to an inverse temperature or step-size). When $\ell = -\log p(x|\theta)$ and $w = 1$, the standard Bayes posterior is recovered.

## Key results

- Axiomatic derivation: under mild coherence axioms, the Gibbs posterior is the unique rational belief update based on a loss function.
- The update is characterized as the minimizer of free energy $F[\pi] = \mathbb{E}_\pi[\ell] + \frac{1}{w}\mathrm{KL}(\pi\|\pi_0)$, giving a direct variational interpretation.
- The learning-rate parameter $w$ enters naturally and can be chosen or estimated (e.g., via cross-validation or PAC-Bayes bounds); this "tempered" or "powered" likelihood perspective subsumes many existing robust Bayesian methods.
- The framework accommodates arbitrary loss functions (not just negative log-likelihoods), enabling principled inference in misspecified, semi-parametric, and non-likelihood settings.

## Relevance to this research

This paper is directly foundational to the VFE transformer's variational free-energy objective. The variational free energy

$$F = \alpha\,\mathrm{KL}(q_i \| p_i) + \sum_{ij}\beta_{ij}\,\mathrm{KL}(q_i \| \Omega_{ij} q_j) + \cdots$$

has exactly the Bissiri–Holmes–Walker structure: each term is an expected loss (the KL divergence acting as a transport cost / belief-coupling loss) regularized by a KL back to a prior. The gauge-transported coupling $\mathrm{KL}(q_i \| \Omega_{ij} q_j)$ is the "loss" for token $i$ relative to gauge-transported belief $j$, and the attention weights $\beta_{ij}$ are the minimizers of the full free energy — a direct generalization of the Gibbs posterior to a many-body, gauge-equivariant setting.

The Bissiri et al. result also provides justification for the softmax attention derivation: attention weights $\beta_{ij} \propto \exp(-\mathrm{KL}/\tau)$ are exactly Gibbs posteriors over "which neighbor to couple to," with $\tau = \kappa\sqrt{d}$ playing the role of $1/w$. This is directly relevant to the GL(K) attention manuscript (see `Manuscripts-Theory/GL(K)_attention.tex`) and the PIFB theory (`Manuscripts-Theory/PIFB.tex`), where the softmax derivation is the stationarity condition of $F$ over the attention distribution.

For the multi-agent model (`MAgent_Model`), the Bissiri framework supports treating meta-agent belief updates as Gibbs posteriors over model distributions, with the loss being the expected KL divergence under the meta-level free energy.

## Cross-links
- Concepts: [[Variational Free Energy]], [[KL Divergence]], [[Gibbs Posterior]], [[Generalized Bayes]], [[Attention as Inference]]
- Related sources: [[Knoblauch2022-generalized-variational-inference]], [[Zellner1988-optimal-information-processing]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention Manuscript]], [[PIFB Manuscript]]

## BibTeX
```bibtex
@article{BissiriHolmesWalker2016,
  author  = {Bissiri, Pier Giovanni and Holmes, Chris C. and Walker, Stephen G.},
  title   = {A General Framework for Updating Belief Distributions},
  journal = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
  year    = {2016},
  volume  = {78},
  number  = {5},
  pages   = {1103--1130},
  doi     = {10.1111/rssb.12158},
  url     = {https://doi.org/10.1111/rssb.12158},
}
```
