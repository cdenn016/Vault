---
type: paper
title: "A Multiplicative Formula for Aggregating Probability Assessments"
aliases:
  - "Bordley 1982"
  - "Bordley (1982) Multiplicative Pooling"
authors:
  - Robert F. Bordley
year: 1982
arxiv: null
url: https://doi.org/10.1287/mnsc.28.10.1137
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - project/multi-agent
  - project/social-physics
  - field/statistics
  - field/economics
  - cluster/social-physics/opinion-dynamics
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# A Multiplicative Formula for Aggregating Probability Assessments

> [!info] Citation
> Bordley, R. F. (1982). "A Multiplicative Formula for Aggregating Probability Assessments." *Management Science* **28**(10), 1137–1148. DOI: [10.1287/mnsc.28.10.1137](https://doi.org/10.1287/mnsc.28.10.1137).

## TL;DR

The original derivation of the **multiplicative (log-linear) opinion-pooling** formula, in which a decision-maker aggregates several experts' probability assessments by taking a weighted, normalized *product* of their distributions rather than a weighted average. Bordley derives the formula from a small set of axioms about how a Bayesian decision-maker should revise a prior in light of multiple experts' opinions, treating each expert's assessment as evidence. The result is the direct ancestor of the product-of-experts construction and of geometric opinion pooling.

## Problem & setting

A single decision-maker holds a prior over events and consults $n$ experts, each of whom reports a probability assessment. How should the decision-maker combine them into a single revised distribution? Bordley models each expert report as a likelihood-bearing observation and applies Bayesian updating, asking what aggregation rule results under independence-style assumptions on the experts' informativeness.

## Method

Treating expert assessments as conditionally independent evidence about the true state, Bayesian revision of the decision-maker's prior produces a posterior proportional to the prior times a product of expert-derived factors. With suitable normalization and weighting (reflecting relative expert reliability), this yields the multiplicative pooling formula $p \propto \prod_i p_i^{w_i}$ — a weighted geometric mean. Bordley characterizes the conditions under which this multiplicative form, rather than a linear average, is the coherent Bayesian aggregate.

## Key results

- Derives the weighted-product (log-linear / geometric) pooling rule from Bayesian first principles, with weights encoding expert reliability.
- Establishes multiplicative pooling as the externally-Bayesian, evidence-combining alternative to linear (arithmetic) pooling.
- Exhibits the "veto" / zero-preserving property inherent to products: an event any expert assigns probability zero is assigned zero by the aggregate.

## Relevance to this research

Bordley (1982) is the historical root of the pooling rule the project's meta-agent code *deliberately rejects*. The coarse-graining step in [[Meta-agents and hierarchical emergence]] pools constituent beliefs by a gauge-covariant arithmetic (sandwich) average of $(\mu,\Sigma)$, not by the multiplicative product Bordley derives, precisely to avoid the product's veto pathology and to remain consensus-preserving. This reference therefore documents the alternative the project measures itself against: it is the precursor to the product-of-experts of [[hinton-2002-poe]] and the geometric-pool branch of the [[genest-zidek-1986-pooling]] and [[dietrich-list-2016-opinion-pooling]] taxonomies. Where PIFB (see [[participatory-it-from-bit]]) *does* invoke a log-linear pool — in the discounted-KL multi-generation hyperprior, where the weighted-product Gaussian precision $\Sigma_\star^{-1} = \sum_k \lambda_k \Sigma_k^{-1}$ is exactly Bordley's multiplicative aggregate — this note marks the genealogy of that form. Citing Bordley fixes which pooling tradition the project is and is not adopting at each point in the model.

## Cross-links

- Concepts: [[Meta-agents and hierarchical emergence]], [[Multi-agent variational free energy]]
- Related sources: [[hinton-2002-poe]], [[genest-zidek-1986-pooling]], [[dietrich-list-2016-opinion-pooling]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@article{bordley1982multiplicative,
  author  = {Bordley, Robert F.},
  title   = {A Multiplicative Formula for Aggregating Probability Assessments},
  journal = {Management Science},
  volume  = {28},
  number  = {10},
  pages   = {1137--1148},
  year    = {1982},
  doi     = {10.1287/mnsc.28.10.1137},
  publisher = {INFORMS}
}
```
