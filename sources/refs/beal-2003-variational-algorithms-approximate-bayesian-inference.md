---
type: reference
title: "Variational Algorithms for Approximate Bayesian Inference"
aliases: ["Beal 2003 — Variational Bayesian EM", "VBEM"]
authors: ["Matthew J. Beal"]
year: 2003
url: https://cse.buffalo.edu/faculty/mbeal/thesis/
tags: [cluster/vfe, project/transformer, project/multi-agent, field/statistics, field/cs-ml]
created: 2026-06-20
updated: 2026-06-20
---

# Variational Algorithms for Approximate Bayesian Inference

> [!info] Citation
> Matthew J. Beal (2003). *Variational Algorithms for Approximate Bayesian Inference.* Ph.D. thesis, Gatsby Computational Neuroscience Unit, University College London.

## TL;DR

Beal's thesis develops the **variational Bayesian (VB)** treatment of latent-variable models, in which a single free-energy lower bound on the log marginal likelihood is maximized jointly over an approximate posterior on the hidden variables and an approximate posterior on the parameters. Its central contribution is the **Variational Bayesian Expectation–Maximization (VBEM)** algorithm: a mean-field generalization of EM that, for conjugate-exponential-family models, alternates a VBE-step over hidden-variable posteriors with a VBM-step over parameter posteriors, each in closed form, while monotonically increasing one common bound $\mathcal{F}$. The thesis applies this machinery to hidden Markov models, mixtures, factor analysers, state-space models, and — through the bound itself — to Bayesian model selection.

## What it establishes

The object maximized throughout is a free-energy functional. For observed data $y$, hidden variables $x$, and parameters $\theta$, with a factorized variational posterior $q(x,\theta) = q_x(x)\,q_\theta(\theta)$, the bound is

$$
\log p(y) \ \ge\ \mathcal{F}[q_x, q_\theta] \ =\ \int q_x(x)\,q_\theta(\theta)\,\log \frac{p(y, x, \theta)}{q_x(x)\,q_\theta(\theta)}\, dx\, d\theta,
$$

so that $\log p(y) - \mathcal{F} = \mathrm{KL}\!\left(q_x q_\theta \,\|\, p(x,\theta \mid y)\right) \ge 0$. The gap is exactly the Kullback–Leibler divergence from the factorized variational posterior to the true joint posterior, and tightening the bound is the same as minimizing that divergence. This is the [[Evidence lower bound (ELBO)]] / negative [[Variational free energy]] applied not only over hidden states (as in ordinary variational EM) but over the **parameters** as well — the step that makes the treatment Bayesian rather than point-estimate maximum-likelihood.

From this Beal derives the VBEM fixed-point updates. Under a conjugate-exponential family, the optimal coordinate updates have the mean-field form

$$
q_x(x) \ \propto\ \exp\!\big\langle \log p(y, x \mid \theta) \big\rangle_{q_\theta},
\qquad
q_\theta(\theta) \ \propto\ p(\theta)\,\exp\!\big\langle \log p(y, x \mid \theta) \big\rangle_{q_x},
$$

where each expectation is taken under the *other* factor's current variational posterior. The VBE-step computes expected sufficient statistics using the *expected natural parameters* $\bar\theta = \langle \theta \rangle_{q_\theta}$ rather than a single point estimate, so the resulting algorithm is "EM with the parameters integrated out under $q_\theta$," reducing to ordinary EM only when $q_\theta$ collapses to a point mass. The thesis proves the bound is non-decreasing across these alternating updates and uses its converged value as an approximation to the log model evidence for **automatic model-order selection** (number of mixture components, hidden states, or latent factors), a practical alternative to BIC and to bridge-sampling estimates of the marginal likelihood.

## Why the project cites it

This thesis is the most direct statistical antecedent of the project's iterative-VFE scheme, and it is cited by the variational lens of the audit and debate panels for precisely that reason. The VFE transformer carries all of its representational capacity in iterated minimization of a free-energy functional over Gaussian belief tuples $(\mu, \Sigma, \phi)$, with no backprop-trained feature stack; Beal's VBEM is the canonical worked example of running a model entirely as coordinate ascent on $\mathcal{F}$, which is what the project generalizes.

- **Free energy as the single objective.** The project's per-token belief update and parameter update are the two coordinate moves on one bound, exactly the VBE / VBM split. Beal's $\log p(y) - \mathcal{F} = \mathrm{KL}(q\|p)$ identity is the entry point for the model's [[Amortized inference]] reading of the belief solve and for replacing KL with tunable $\alpha$- / Rényi divergences in the belief-fitting step.
- **Posterior over parameters, not just states.** Where ordinary variational EM (Neal–Hinton) keeps a point parameter and a distribution over latents, Beal keeps distributions over *both*. The project's hierarchy $h \to s \to p \to q$ — hyper-prior over models, priors over beliefs, beliefs over data — mirrors this layering of distributions-over-distributions, and the meta-entropy / model-coupling terms in the free energy are the project's analogue of carrying a $q_\theta$ rather than a single $\theta$.
- **Conjugate-exponential mean-field structure.** Beal's closed-form updates rest on conjugacy in the exponential family; the project's Gaussian-belief family and natural-parameter ($\bar\theta$-style) M-step inherit that structure, which is what lets the alternation run as cheap fixed-point iterations rather than an inner optimization, and what links the updates to the [[Fisher information metric]] natural-gradient geometry used elsewhere in the program.
- **Bound as model evidence.** The converged $\mathcal{F}$ as an evidence surrogate is the template for the project's use of free-energy values to compare regimes and toggle configurations rather than only to drive a single fit.

> [!note] Editorial: Beal's monotonicity and closed-form VBEM updates are established for KL-based mean-field bounds in conjugate-exponential families. The VFE transformer departs on two axes — it can replace KL with a Rényi / $\alpha$-divergence in the belief step, and it uses structured Gaussian beliefs with gauge transport rather than a generic conjugate posterior — so the project realizes the *spirit* of VBEM (coordinate ascent on a free-energy bound with distributions over both states and parameters) as a principled generalization, not a literal instance of the 2003 algorithm.

## Cross-links

- Concepts: [[Variational free energy]], [[Evidence lower bound (ELBO)]], [[Amortized inference]]
- Theme: [[Variational free energy and predictive coding]]
- Related sources: [[dempster-1977-em]], [[neal-1998-variational-em]], [[blei-2017-variational-inference]], [[kingma-2013-auto-encoding-variational-bayes]]
- Projects: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@phdthesis{beal2003variational,
  author = {Beal, Matthew J.},
  title  = {Variational Algorithms for Approximate {B}ayesian Inference},
  school = {Gatsby Computational Neuroscience Unit, University College London},
  year   = {2003},
  url    = {https://cse.buffalo.edu/faculty/mbeal/thesis/}
}
```
