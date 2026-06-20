---
type: reference
title: "Training Products of Experts by Minimizing Contrastive Divergence"
aliases:
  - "Hinton 2002"
  - "Hinton (2002) Products of Experts"
authors:
  - Geoffrey E. Hinton
year: 2002
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# Training Products of Experts by Minimizing Contrastive Divergence

> [!info] Citation
> Hinton, G. E. (2002). "Training Products of Experts by Minimizing Contrastive Divergence." *Neural Computation* **14**(8), 1771–1800. DOI: [10.1162/089976602760128018](https://doi.org/10.1162/089976602760128018).

## TL;DR

Introduces the **product of experts (PoE)** model — a distribution formed by multiplying together many individual expert distributions and renormalizing, $p(x) \propto \prod_i p_i(x)$ — and the **contrastive divergence** training algorithm that makes it tractable. A product (unlike a mixture/average) is sharp: each expert can independently veto a region by assigning it low probability, so the experts act as a conjunction of soft constraints. For Gaussians the product is itself Gaussian with precision equal to the *sum* of the experts' precisions. This is the machine-learning incarnation of logarithmic opinion pooling.

## What it establishes

A PoE combines experts multiplicatively rather than additively, yielding a distribution that is high only where *all* experts agree. The paper shows the normalization constant (partition function) makes exact maximum-likelihood training intractable, and that **contrastive divergence** — taking a few steps of Gibbs sampling from the data distribution rather than running the chain to equilibrium — gives a cheap, effective gradient. The key structural fact carried into the project's setting: multiplying Gaussian experts adds precisions, $\Sigma_\star^{-1} = \sum_i \Sigma_i^{-1}$, so a product is far more confident than any single expert and inherits the veto/zero-preserving behavior of geometric pooling.

## Why the project cites it

[[participatory-it-from-bit]] cites this (`HintonPoE2002`) as one of the four "anchor identifications" for its discounted-KL hyperprior: the additive-KL stack $\sum_k \lambda_k \mathrm{KL}(q_i \| p_k)$ corresponds to a **product-of-experts / log-linear pool** prior with components $p_k$ raised to powers $\lambda_k$, giving the Gaussian pooled precision $\Sigma_\star^{-1} = \sum_k \lambda_k \Sigma_k^{-1}$ — exactly Hinton's add-the-precisions rule. Equally, this is the pooling form the **meta-agent code explicitly rejects** for belief coarse-graining: [[Meta-agents and hierarchical emergence]] uses a gauge-covariant *sandwich average* (linear pool) of constituent covariances rather than a PoE, precisely to avoid the over-sharpening and veto pathology a product would impose when fusing constituent beliefs. So Hinton (2002) sits on both sides of the project's pooling story — adopted (as the log-pool identity) for the cross-scale hyperprior, and contrasted-against (as PoE) for the within-cluster barycenter. It is the ML-side companion to [[bordley-1982-multiplicative-pooling]] and [[genest-zidek-1986-pooling]].

```bibtex
@article{hinton2002training,
  author  = {Hinton, Geoffrey E.},
  title   = {Training Products of Experts by Minimizing Contrastive Divergence},
  journal = {Neural Computation},
  volume  = {14},
  number  = {8},
  pages   = {1771--1800},
  year    = {2002},
  doi     = {10.1162/089976602760128018},
  publisher = {MIT Press}
}
```
