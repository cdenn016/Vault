---
type: paper
title: "A general framework for updating belief distributions"
aliases:
  - Bissiri 2016
  - Gibbs posterior
  - loss-based Bayesian updating
  - Bissiri2016-generalized-bayes
  - BHW2016
  - Generalized Bayes
  - bissiri-holmes-walker-2016-general-bayes
  - Bissiri, Holmes & Walker 2016
  - Bissiri-Holmes-Walker (2016) General Bayes
authors:
  - Bissiri, P. G.
  - Holmes, C. C.
  - Walker, S. G.
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
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A general framework for updating belief distributions

> [!info] Citation
> Bissiri, P. G., Holmes, C. C., and Walker, S. G. (2016). "A general framework for updating belief distributions." *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, 78(5), 1103–1130. DOI: [10.1111/rssb.12158](https://doi.org/10.1111/rssb.12158). Preprint: [arXiv:1306.6430](https://arxiv.org/abs/1306.6430).

## TL;DR
This paper establishes that coherent Bayesian-style belief updating can be grounded in loss functions rather than likelihoods. Given a prior $\pi(\theta)$ and a loss $\ell(\theta, x)$, the unique coherent posterior is $\hat{\nu}(\theta) \propto \exp\{-\ell(\theta,x)\}\pi(\theta)$, which recovers standard Bayes when the loss is the negative log-likelihood. The KL divergence between posterior and prior emerges necessarily from a decision-theoretic coherence requirement, not by assumption. This provides principled inference in misspecified, M-open, and non-stochastic-data settings.

## Problem & setting
Classical Bayesian inference requires a complete, correctly-specified likelihood $f(x;\theta)$, which is often unavailable or too complex. The paper addresses settings where: (1) the parameter of interest does not directly index a density family (M-open case); (2) the data-generating mechanism is unknown but a proxy loss can be defined; (3) information is non-stochastic (expert declarations, partial observations). Prior work (Zhang 2006, Jiang & Tanner 2008) studied "Gibbs posteriors" empirically but lacked a coherence foundation or principled calibration of the loss scale.

## Method
The cumulative loss for a probability measure $\nu$ on $\theta$-space is

$$L(\nu; \pi, x) = \int \ell(\theta, x)\, \nu(d\theta) + d_{\mathrm{KL}}(\nu, \pi),$$

where $h_1(\nu, x) = \int \ell(\theta,x)\,\nu(d\theta)$ is the expected loss to data and $h_2(\nu, \pi) = d_{\mathrm{KL}}(\nu, \pi)$ is the loss to prior. The paper proves (Theorem 1 and online supplement) that the KL penalty is the *unique* choice satisfying a coherence condition: updating sequentially on $(x_1, x_2)$ must yield the same posterior as updating jointly. The minimizer of $L$ is

$$\hat{\nu}(\theta) = \frac{\exp\{-\ell(\theta,x)\}\pi(\theta)}{\int \exp\{-\ell(\theta,x)\}\pi(d\theta)}.$$

When $\ell(\theta,x) = -\log f(x;\theta)$ (self-information / log loss), this reduces to standard Bayes. The paper also develops calibration schemes for the relative weight $w$ of data loss to prior loss: annealing/temperature, unit-information loss (matching expected losses), hierarchical loss priors, operational frequentist calibration, and conjugate-loss priors.

## Key results
1. **Uniqueness theorem**: Under five natural assumptions (coherence, set-restriction consistency, monotonicity in loss, no-information invariance, translation invariance), the exponential-loss update (2) is the only valid posterior for all parameter spaces $|\Theta| \ge 3$.
2. **KL necessity**: For coherent sequential updates, the penalty between $\nu$ and $\pi$ must be the KL divergence — established algebraically from the coherence axiom.
3. **M-open unification**: The framework handles M-closed, M-open (proxy model), and pure loss settings identically; the analyst need not declare which regime holds.
4. **Non-stochastic information**: The update applies to non-stochastic expert information $I$ via an appropriate loss $\ell(\theta, I)$, providing an operational definition of conditional probability without a probability model for $I$.
5. **PAC-Bayes connection**: The Gibbs posterior $\hat{\nu}$ also minimizes an upper bound on generalization error (PAC-Bayes), but the authors emphasize that their derivation additionally guarantees coherent belief semantics and principled calibration.

## Relevance to this research
This paper is directly load-bearing for the VFE transformer's free-energy functional. The canonical VFE is

$$F = \alpha\, d_{\mathrm{KL}}(q_i \| p_i) + \lambda_h\, d_{\mathrm{KL}}(s_i \| h) + \sum_{ij}\bigl[\beta_{ij}\, d_{\mathrm{KL}}(q_i \| \Omega_{ij} q_j) + \tau\, \beta_{ij}\log(\beta_{ij}/\pi_{ij})\bigr] - \mathbb{E}_q[\log p(o|x)].$$

The KL terms between beliefs and priors/transported beliefs arise in this paper as the *unique coherent* penalty for updating belief distributions — exactly the $h_2(\nu,\pi)$ term. The Bissiri-Holmes-Walker result thus provides a decision-theoretic foundation for why VFE minimization (rather than likelihood maximization or some other objective) is the principled action for a rational agent updating Gaussian beliefs. The "self-coupling" term $\alpha\, d_{\mathrm{KL}}(q_i \| p_i)$ is precisely the $w$-weighted loss-to-prior in equation (7), with the KL emerging from coherence, not phenomenological choice. The attention entropy term $\tau\,\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ (required for softmax $\beta$ to be a stationary point of $F$) mirrors the calibration role of $w$ in Section 3: it sets the relative weight between belief-coupling loss and the prior over attention patterns. The framework's generalization to non-stochastic information (Section 4.1) also resonates with participatory realism / it-from-bit settings where "observations" may be non-stochastic constraints on beliefs.

## Cross-links
- Concepts: [[Variational Free Energy]] [[KL Divergence]] [[Belief Updating]] [[Information Geometry]] [[Gibbs Posterior]] [[Generalized Bayes]] [[Multi-agent variational free energy]]
- Related sources: [[friston-2023-path-integrals]] [[zellner-1988-optimal-information-processing]] [[knoblauch-2022-generalized-variational-inference]]
- Manuscript/Project: [[VFE Transformer Program]] [[GL(K) Attention]] [[PIFB]] [[participatory-it-from-bit]]

> [!note] Editorial: PIFB ([[participatory-it-from-bit]]) cites `BissiriHolmesWalker2016` to legitimize its **unrestricted, tempered coupling**: the default discounted-KL hyperprior with $\lambda_0, \rho > 0$ unconstrained "is a tempered free energy in the generalized-Bayesian sense of Bissiri, Holmes & Walker," letting the overall strength of ancestral coupling be scaled independently of the decay rate. More broadly, the project's whole VFE E-step (expected loss = negative log-evidence, plus a KL-to-prior penalty) is exactly the Bissiri-Holmes-Walker variational form, so per-token Gaussian belief inference is a coherent generalized-Bayesian update with precision/temperature playing the role of the learning rate $w$.

## BibTeX
```bibtex
@article{BissiriHolmesWalker2016,
  author  = {Bissiri, P. G. and Holmes, C. C. and Walker, S. G.},
  title   = {A general framework for updating belief distributions},
  journal = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
  year    = {2016},
  volume  = {78},
  number  = {5},
  pages   = {1103--1130},
  doi     = {10.1111/rssb.12158},
  eprint  = {1306.6430},
  archivePrefix = {arXiv},
  primaryClass  = {math.ST},
}
```
