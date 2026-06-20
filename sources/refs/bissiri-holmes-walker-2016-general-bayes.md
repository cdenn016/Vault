---
type: reference
title: "A General Framework for Updating Belief Distributions"
aliases:
  - "Bissiri, Holmes & Walker 2016"
  - "Bissiri-Holmes-Walker (2016) General Bayes"
authors:
  - Pier Giovanni Bissiri
  - Chris C. Holmes
  - Stephen G. Walker
year: 2016
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# A General Framework for Updating Belief Distributions

> [!info] Citation
> Bissiri, P. G., Holmes, C. C., & Walker, S. G. (2016). "A General Framework for Updating Belief Distributions." *Journal of the Royal Statistical Society: Series B (Statistical Methodology)* **78**(5), 1103–1130. DOI: [10.1111/rssb.12158](https://doi.org/10.1111/rssb.12158). Preprint: [arXiv:1306.6430](https://arxiv.org/abs/1306.6430).

## TL;DR

Establishes that a coherent belief update need not arise from a likelihood and Bayes' theorem: given any **loss function** connecting a parameter to data, the rational update of a prior is the distribution minimizing expected loss plus a KL divergence to the prior. The solution is the **Gibbs posterior** $\pi(\theta) \propto \pi_0(\theta)\exp(-w\,\ell(\theta, \text{data}))$, and ordinary Bayesian updating is the special case where the loss is the negative log-likelihood. This **generalized / Gibbs-posterior Bayes** (also "tempered Bayes," with $w$ a learning rate) legitimizes loss-based belief updates as coherent, not ad hoc.

## What it establishes

The authors show, from a decision-theoretic coherence argument, that the unique update preserving rationality under a general loss $\ell$ is the variational problem
$$
\pi^\star = \arg\min_{\nu}\Big\{ w\,\mathbb{E}_{\nu}[\ell(\theta,x)] + \mathrm{KL}(\nu \| \pi_0) \Big\},
$$
whose minimizer is the Gibbs posterior above. The temperature / learning rate $w$ scales the influence of the data relative to the prior; $w=1$ with $\ell = -\log p(x\mid\theta)$ reproduces exact Bayes, while other $w$ give principled "cold" or "tempered" posteriors. This places exponentiated-loss updates — common in machine learning — on a coherent inferential footing and provides the formal meaning of a *tempered* free energy.

## Why the project cites it

[[participatory-it-from-bit]] cites this (`BissiriHolmesWalker2016`) to legitimize its **unrestricted, tempered coupling**: the manuscript notes that the default discounted-KL hyperprior with $\lambda_0, \rho > 0$ unconstrained "is a tempered free energy in the generalized-Bayesian sense of Bissiri, Holmes & Walker," letting the overall strength of ancestral coupling be scaled independently of the decay rate. More broadly, this reference is the justification that the project's whole **VFE E-step is a valid belief update**: the E-step minimizes free energy = expected loss (negative log-evidence) plus a KL-to-prior penalty, which is exactly the Bissiri-Holmes-Walker variational form. So the project's per-token Gaussian belief inference is not a heuristic energy descent but a coherent generalized-Bayesian update, with the precision/temperature playing the role of the learning rate $w$. This anchors the [[Variational free energy]] objective and the [[Multi-agent variational free energy]] coupling as legitimate inference rather than mere regularization.

```bibtex
@article{bissiri2016general,
  author  = {Bissiri, Pier Giovanni and Holmes, Chris C. and Walker, Stephen G.},
  title   = {A General Framework for Updating Belief Distributions},
  journal = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
  volume  = {78},
  number  = {5},
  pages   = {1103--1130},
  year    = {2016},
  doi     = {10.1111/rssb.12158},
  eprint  = {1306.6430},
  archivePrefix = {arXiv},
  primaryClass  = {math.ST}
}
```
