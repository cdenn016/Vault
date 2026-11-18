---
type: concept
title: Probabilistic opinion pooling
aliases: ["Opinion pooling", "Linear and logarithmic pooling", "Product of experts"]
tags:
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-11-18
---

# Probabilistic opinion pooling

## What it is

Probabilistic opinion pooling is the theory of how to combine several agents' probability distributions over a common space into a single collective distribution. Given $n$ agents, each supplying a probability function $p_i$ on the same algebra of events, a *pooling operator* $F(p_1,\dots,p_n)$ returns one collective probability function. Unlike the dynamical opinion models catalogued under [[Opinion dynamics]] — which iterate a local update rule over time — pooling is a *static aggregation*: it asks not how beliefs evolve but how, at a single instant, a set of beliefs should be merged into one. The canonical survey by [[genest-zidek-1986-pooling]] organizes the entire field around two principal families, and [[dietrich-list-2016-opinion-pooling]] sharpens this into theorem-level adjudication. The first family is the **linear (arithmetic) pool**, a weighted average $p = \sum_i w_i p_i$ with $\sum_i w_i = 1$. The second is the **logarithmic (geometric / multiplicative) pool**, a weighted normalized product $p \propto \prod_i p_i^{w_i}$ — the externally-Bayesian, evidence-combining alternative whose original Bayesian derivation is due to [[bordley-1982-multiplicative-pooling]].

## The axioms that force each operator

The central message of the literature is that *no single pooling rule is universally correct*: each is uniquely forced by a different, mutually incompatible set of axioms, so the choice of aggregator is a substantive modeling commitment whose consequences can be derived rather than asserted. [[dietrich-list-2016-opinion-pooling]] proves the two representation theorems sharply. **Eventwise independence** — that the pooled probability of an event depend only on the agents' probabilities for *that* event — together with **consensus (unanimity) preservation** forces linear pooling: $p = \sum_i w_i p_i$. By contrast, **external Bayesianity** — that pooling commute with Bayesian updating on shared evidence — together with a multiplicative independence condition forces geometric / log-linear pooling: $p \propto \prod_i p_i^{w_i}$. [[genest-zidek-1986-pooling]] frames the same dichotomy through the **marginalization property** (pooling commutes with computing marginals), which characterizes the linear pool, versus external Bayesianity, which characterizes the logarithmic pool. The two operators differ on the properties practitioners care about. Linear pooling is simple and consensus-respecting and preserves unanimous unconditional assignments, but it is *not* externally Bayesian and generally destroys probabilistic independence judgments. Geometric pooling is externally Bayesian and **zero-preserving**: because it is a product, any agent who assigns an event probability zero forces the collective to assign it zero — a "veto" on impossibility. The incompatibility is genuine: in nondegenerate cases one cannot have both eventwise independence and external Bayesianity, so the pooling choice is a forced trade-off, not a matter of taste.

## Product of experts

The logarithmic pool has a direct identification with the **product-of-experts** construction: a normalized product of component densities is exactly a product-of-experts model, and [[bordley-1982-multiplicative-pooling]] derives precisely this form by treating each expert's assessment as conditionally independent evidence and applying Bayesian revision, so the posterior is proportional to a product of expert-derived factors. For Gaussian beliefs $q_i = \mathcal{N}(\mu_i, \Sigma_i)$ the geometric pool is analytically transparent: the pooled precision is the weighted sum of component precisions, $\Sigma_\star^{-1} = \sum_i \lambda_i \Sigma_i^{-1}$, and the pooled mean is the corresponding precision-weighted average. The linear pool, by contrast, is a weighted arithmetic mixture that respects consensus but is not a product of experts.

## Dynamic density consensus and common-information risk

The weighted Kullback--Leibler average

$$
p_\star=\arg\min_p\sum_i w_i\,D_{\mathrm{KL}}(p\|p_i)
\propto\prod_i p_i^{w_i}
$$

is the geometric pool, but the variational characterization does not make it the centralized Bayesian posterior. [[battistelli-chisci-2014-kl-density-consensus]] implements this target through repeated graph-local Kullback--Leibler averaging. It establishes density consensus under its connectivity and weight assumptions; the agreed density is determined by the pool of initial densities, not automatically by the joint likelihood of all raw observations.

Dynamic filtering adds evidence lineage. [[bandyopadhyay-chung-2018-logop-filtering]] distinguishes pooling normalized likelihood information from pooling entire local posteriors and analyzes communication-aware variants. That distinction matters because recirculating a posterior can count historical evidence multiple times. When the cross-correlation is unknown, [[julier-uhlmann-1997-covariance-intersection]] supplies a conservative Gaussian baseline rather than pretending independence.

Four objects should therefore remain separate: an exact centralized Bayesian posterior, a one-shot static opinion pool, a distributed algorithm that converges to a chosen pool, and a conservative fusion rule for unknown common information. Agreement among agents is a protocol property; posterior correctness and calibration are additional statistical properties.

## Sources

- [[battistelli-chisci-2014-kl-density-consensus]] — distributed consensus on a Kullback--Leibler average of densities.
- [[bandyopadhyay-chung-2018-logop-filtering]] — logarithmic pooling for Bayesian filtering with explicit likelihood/posterior and communication distinctions.
- [[julier-uhlmann-1997-covariance-intersection]] — conservative Gaussian fusion under unknown cross-correlation.
- [[campbell-how-2014-decentralized-bayes]] — decentralized approximate posterior multiplication with shared-prior correction and symmetry alignment.

- [[genest-zidek-1986-pooling]] — the canonical survey and taxonomy of opinion pooling; linear vs logarithmic families and their characterizing axioms (marginalization vs external Bayesianity).
- [[bordley-1982-multiplicative-pooling]] — original Bayesian derivation of the multiplicative (log-linear) pool $p \propto \prod_i p_i^{w_i}$; the ancestor of product-of-experts and the zero-preserving veto property.
- [[dietrich-list-2016-opinion-pooling]] — theorem-level adjudication: eventwise independence + consensus forces linear pooling; external Bayesianity + multiplicative independence forces geometric pooling; the two are incompatible in nondegenerate cases.
