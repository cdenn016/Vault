---
type: paper
title: "Probabilistic Opinion Pooling"
aliases:
  - "Dietrich & List 2016"
  - "Dietrich-List (2016) Opinion Pooling"
authors:
  - Dietrich, Franz
  - List, Christian
year: 2016
arxiv: null
url: https://doi.org/10.1093/oxfordhb/9780199607617.013.37
tags:
  - cluster/social-physics/opinion-dynamics
  - cluster/multi-agent
  - project/multi-agent
  - project/social-physics
  - field/philosophy
  - field/statistics
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# Probabilistic Opinion Pooling

> [!info] Citation
> Dietrich, F., & List, C. (2016). "Probabilistic Opinion Pooling." In A. Hájek & C. Hitchcock (Eds.), *The Oxford Handbook of Probability and Philosophy*. Oxford University Press. DOI: [10.1093/oxfordhb/9780199607617.013.37](https://doi.org/10.1093/oxfordhb/9780199607617.013.37).

## TL;DR

A theorem-level survey of how to aggregate several agents' probability assignments over a common event space into a single collective probability function. It organizes the field around three canonical pooling operators — **linear** (a weighted arithmetic average of the individual probabilities), **geometric / multiplicative** (a weighted normalized product, i.e. log-linear pooling), and **multiplicative** variants — and characterizes each by the axioms it uniquely satisfies. The central message is that no single pooling rule is universally "correct": each is forced by a different, mutually incompatible set of desiderata, so the choice of aggregator is a substantive modeling commitment with consequences that can be derived rather than asserted.

## Problem & setting

Given $n$ agents, each supplying a probability function $p_i$ on the same algebra of events, find a pooling function $F(p_1,\dots,p_n)$ returning a collective probability function. The paper asks which axioms — unanimity preservation, eventwise independence (the pooled probability of an event depends only on the agents' probabilities for that event), external Bayesianity (commuting with Bayesian updating on shared evidence), and unanimity on independence — pin down which operator.

## Method

The work proceeds axiomatically. It states representation theorems: **eventwise independence plus consensus preservation forces linear pooling** (the pooled probability is $\sum_i w_i p_i$); whereas **external Bayesianity together with a multiplicative independence condition forces geometric/log-linear pooling** ($p \propto \prod_i p_i^{w_i}$). It then contrasts the two on properties practitioners care about: linear pooling preserves agreement on unconditional probabilities but generally fails to preserve probabilistic independence judgments and is not externally Bayesian; geometric pooling is externally Bayesian and zero-preserving (a "veto" on impossibility) but violates eventwise independence on the original event algebra.

## Key results

- **Linear pooling** is the unique aggregator satisfying eventwise independence with unanimity preservation. It is simple and consensus-respecting but is *not* externally Bayesian and destroys independence structure.
- **Geometric (log-linear) pooling** is the unique externally-Bayesian, zero-preserving aggregator. For Gaussians it yields a product-of-experts whose precision is the weighted sum of component precisions — but it gives any agent a "veto" (an event one agent rules out is ruled out collectively).
- The axiomatic incompatibilities are sharp: one cannot have both eventwise independence and external Bayesianity in nondegenerate cases. The pooling choice is therefore a forced trade-off, not a matter of taste.

## Relevance to this research

This paper is the cleanest theorem-level adjudication of the **barycenter / pooling choice** at the heart of the [[Gauge-Theoretic Multi-Agent VFE Model]]. The meta-agent coarse-graining step (see [[Meta-agents and hierarchical emergence]]) pools constituent beliefs by a *gauge-covariant linear (sandwich) average* — transport each constituent into the meta frame, then take a coherence-weighted arithmetic mean of $(\mu, \Sigma)$ — explicitly rather than by a product-of-experts. Dietrich & List supply the principled reason this is defensible: linear pooling is the operator forced by eventwise independence and consensus preservation, and it avoids the veto pathology of geometric pooling that would let a single overconfident constituent annihilate the collective belief. Their result also clarifies the cost: the sandwich average is not externally Bayesian, which is exactly why [[participatory-it-from-bit]] keeps the log-linear / tempered-Bayes pooling as a *separate* identification for the multi-generation hyperprior term (the discounted-KL stack), where external Bayesianity and the geometric-discount structure are wanted. The two pooling regimes thus live in different parts of the model, and this reference is the axiomatic map that tells the project which is appropriate where.

## Cross-links
- Concepts: [[Meta-agents and hierarchical emergence]], [[Multi-agent variational free energy]]
- Related sources: [[genest-zidek-1986-pooling]], [[hinton-2002-poe]], [[bordley-1982-multiplicative-pooling]], [[bissiri-holmes-walker-2016-general-bayes]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX
```bibtex
@incollection{dietrich2016probabilistic,
  author    = {Dietrich, Franz and List, Christian},
  title     = {Probabilistic Opinion Pooling},
  booktitle = {The Oxford Handbook of Probability and Philosophy},
  editor    = {H{\'a}jek, Alan and Hitchcock, Christopher},
  publisher = {Oxford University Press},
  year      = {2016},
  doi       = {10.1093/oxfordhb/9780199607617.013.37}
}
```
