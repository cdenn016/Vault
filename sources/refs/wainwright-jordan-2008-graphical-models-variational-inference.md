---
type: reference
title: "Graphical Models, Exponential Families, and Variational Inference"
aliases:
  - "Wainwright & Jordan 2008 — Graphical Models, Exponential Families, and Variational Inference"
  - "Wainwright-Jordan 2008"
authors:
  - "Martin J. Wainwright"
  - "Michael I. Jordan"
year: 2008
url: https://www.nowpublishers.com/article/Details/MAL-001
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
  - field/mathematics
created: 2026-06-20
updated: 2026-06-20
---

# Graphical Models, Exponential Families, and Variational Inference

> [!info] Citation
> Wainwright, M. J., & Jordan, M. I. (2008). "Graphical Models, Exponential Families, and Variational Inference." *Foundations and Trends in Machine Learning* **1**(1–2), 1–305. DOI: [10.1561/2200000001](https://doi.org/10.1561/2200000001).

## TL;DR

The canonical monograph recasting **inference in graphical models as a convex-analytic problem on exponential families**. Its organizing idea: for any exponential-family distribution $p_\theta(x) = \exp\{\langle \theta, \phi(x)\rangle - A(\theta)\}$, the log-partition function $A(\theta)$ and its **conjugate dual** $A^*(\mu)$ — the negative entropy expressed in **mean parameters** $\mu = \mathbb{E}_\theta[\phi(x)]$ — generate a **variational representation** of inference. Exact inference is a maximization over the **marginal polytope** $\mathcal{M}$ of realizable mean parameters; every standard approximate algorithm (mean-field, sum-product/belief propagation, expectation propagation, tree-reweighted and convex bounds) is then read off as a *relaxation* of that same variational problem — approximating either the constraint set $\mathcal{M}$ or the dual entropy $A^*$. This is the reference that frames mean-field variational inference as conjugate-duality optimization rather than as an ad hoc bound.

## What it establishes

For an exponential family with natural parameter $\theta$, sufficient statistic $\phi$, and log-partition function $A(\theta)$, the gradient map $\nabla A(\theta) = \mathbb{E}_\theta[\phi(x)] = \mu$ carries natural (canonical) coordinates to **mean coordinates**, and the Legendre–Fenchel conjugate

$$ A^*(\mu) = \sup_{\theta} \big\{ \langle \theta, \mu \rangle - A(\theta) \big\} $$

equals the negative entropy of the distribution with mean parameter $\mu$ (for $\mu$ in the interior of the marginal polytope $\mathcal{M}$). Dual to this, the log-partition function admits the variational form

$$ A(\theta) = \sup_{\mu \in \mathcal{M}} \big\{ \langle \theta, \mu \rangle - A^*(\mu) \big\}, $$

whose maximizer recovers the true mean parameters — that is, *computes the marginals*. The monograph's contribution is to organize the whole zoo of inference algorithms as principled approximations to this single program:

- **Mean-field methods** restrict $\mu$ to a tractable inner subset $\mathcal{M}_F \subseteq \mathcal{M}$ (the mean parameters realizable by a factorized/structured sub-family), turning the variational problem into a **nonconvex** maximization whose stationary conditions are the coordinate-ascent mean-field updates. This is exactly the lower-bound (ELBO) view of variational inference, derived here from convex duality rather than from Jensen's inequality.
- **Sum-product / belief propagation** is recovered as optimizing the **Bethe** approximation — an outer relaxation of $\mathcal{M}$ to the locally consistent polytope $\mathbb{L}$, with the entropy $A^*$ replaced by the (non-convex) Bethe entropy.
- **Tree-reweighted and other convex surrogates** replace the Bethe entropy with a provably convex upper bound, yielding *upper* bounds on $A(\theta)$ and outer bounds on the marginals.
- The **marginal polytope $\mathcal{M}$** itself — the convex hull of the sufficient statistics over all configurations — is identified as the geometric object that exact inference optimizes over, with its facet complexity explaining why exact inference is hard.

> [!note] Editorial: The monograph is also published verbatim as a standalone book (Now Publishers, 2008); the *Foundations and Trends* article and the book share pagination (1–305). It is descriptive of the convex-duality program, not the originator of every algorithm it unifies (belief propagation, mean-field EM, EP predate it); its lasting contribution is the unifying variational/marginal-polytope picture.

## Why the project cites it

This reference supplies the **convex-duality scaffolding** beneath the project's free-energy objective, and it is the most direct justification for treating the VFE transformer's per-token belief update as exponential-family variational inference rather than as a heuristic.

- **Mean parameters and the Gaussian belief tuple.** The model's beliefs are Gaussians carried as $(\mu, \Sigma, \phi)$. For the Gaussian exponential family the natural-to-mean map $\nabla A$ is precisely the passage from natural parameters $(\Sigma^{-1}\mu, -\tfrac12\Sigma^{-1})$ to mean parameters $(\mu, \Sigma + \mu\mu^\top)$ — the Legendre duality this monograph builds the whole theory on. The E-step's coordinate-ascent over $(\mu, \Sigma)$ is mean-field VI in exactly Wainwright–Jordan's sense, optimizing over an inner relaxation $\mathcal{M}_F$ of the marginal polytope.
- **Mean-field free energy as conjugate duality.** The canonical $F$ the model minimizes — the [[Variational free energy]], i.e. the negative [[Evidence lower bound (ELBO)]] — is the mean-field instantiation of $\langle \theta, \mu \rangle - A^*(\mu)$ with the entropy term $A^*$ supplying the belief- and attention-distribution entropies. This frames the additive KL self-coupling, hyper-prior, and coupling terms as a single convex-dual objective over mean parameters, the reading the gauge-theory and variational audit lenses asked the wiki to anchor.
- **Tractable factorization for the multi-agent model.** The mean-field inner-bound view ($\mathcal{M}_F \subseteq \mathcal{M}$) is what makes the per-agent / per-token factorization of the [[Gauge-Theoretic Multi-Agent VFE Model]] tractable: each agent's belief is a marginal in a structured sub-family, and message passing between agents is the graphical-model coupling this monograph formalizes.
- **Why the surrogate is a relaxation, not the truth.** Because the monograph cleanly separates the *exact* variational problem (over $\mathcal{M}$, with true entropy $A^*$) from its *relaxations* (inner mean-field bounds; outer Bethe/convex bounds), it gives the project the precise language for stating that its mean-field, entropy-suppressed, and attention-as-belief-propagation steps are approximations with known directional error — the honesty the program demands of its own objective.

See also the variational-inference survey [[blei-2017-variational-inference]], the EM origin [[dempster-1977-em]], the information-geometry monograph [[amari-2000-methods-information-geometry]] (whose dually-flat / Legendre picture is the geometric face of the same exponential-family duality), and the free-energy-principle reading [[friston-2010-free-energy-principle]]. Theme: [[Variational free energy and predictive coding]].

## BibTeX

```bibtex
@article{wainwright2008graphical,
  author    = {Wainwright, Martin J. and Jordan, Michael I.},
  title     = {Graphical Models, Exponential Families, and Variational Inference},
  journal   = {Foundations and Trends in Machine Learning},
  volume    = {1},
  number    = {1--2},
  pages     = {1--305},
  year      = {2008},
  publisher = {Now Publishers},
  doi       = {10.1561/2200000001},
  issn      = {1935-8237}
}
```
