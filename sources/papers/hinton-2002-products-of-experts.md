---
type: paper
title: "Training Products of Experts by Minimizing Contrastive Divergence"
aliases:
  - Hinton 2002
  - PoE
  - Products of Experts
  - hinton-2002-poe
  - Hinton (2002) Products of Experts
authors:
  - Hinton, Geoffrey E.
year: 2002
arxiv: null
url: https://doi.org/10.1162/089976602760128018
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Training Products of Experts by Minimizing Contrastive Divergence

> [!info] Citation
> Hinton, Geoffrey E. (2002). "Training Products of Experts by Minimizing Contrastive Divergence." *Neural Computation* 14(8): 1771–1800. DOI: [10.1162/089976602760128018](https://doi.org/10.1162/089976602760128018).

## TL;DR

Introduces the Product of Experts (PoE) model — a probability distribution formed as the (normalised) product of several simpler expert distributions — and the Contrastive Divergence (CD) learning algorithm that makes PoE tractable. CD approximates the intractable gradient of the log-likelihood by running a short Markov chain rather than reaching equilibrium, enabling efficient training.

## Problem & setting

Mixture of Experts models combine experts via a gating network that selects one expert per data point; the result is a mixture (sum). A Product of Experts instead multiplies expert probabilities pointwise before renormalisation, which can represent sharp, high-dimensional constraints more naturally than a mixture. The challenge is that the normalising partition function of the product is typically intractable, blocking maximum-likelihood learning.

## Method

The PoE distribution is $p(\mathbf{x}) \propto \prod_m p_m(\mathbf{x})$ over individual expert distributions $p_m$. Hinton proposes Contrastive Divergence: instead of computing the exact gradient $\langle \partial \log p_m / \partial \theta \rangle_\text{data} - \langle \partial \log p_m / \partial \theta \rangle_\text{model}$, the second expectation is approximated by running only $k$ (typically 1) steps of Gibbs sampling starting from the data, yielding a fast, biased but practically effective gradient estimate.

## Key results

CD-1 (one step of contrastive divergence) trains PoE models effectively on density estimation benchmarks. The product structure allows PoE to represent distributions concentrated on complex manifolds that mixtures struggle with. The paper demonstrates the approach on simple visual data and shows faster convergence than fully equilibrated MCMC.

## Relevance to this research

The PoE factorisation is directly relevant to the VFE transformer's belief-coupling structure: combining beliefs from multiple agents/heads as a product of Gaussians is a PoE, and the normalisation/partition-function problem it solves mirrors the softmax normalisation in attention. CD is also a precursor to score-matching and diffusion-model training, and connects to the E-step/M-step separation in the VFE framework. The "product of priors" structure appears in Friston's free-energy principle when multiple generative models are combined.

For Gaussian experts the product is itself Gaussian with precision equal to the *sum* of the experts' precisions, $\Sigma_\star^{-1} = \sum_i \Sigma_i^{-1}$ (the ML incarnation of logarithmic opinion pooling). PIFB invokes this add-the-precisions identity as one of its anchor identifications for the discounted-KL hyperprior, where the additive-KL stack $\sum_k \lambda_k\,\mathrm{KL}(q_i\|p_k)$ corresponds to a product-of-experts / log-linear pool with weighted precision $\Sigma_\star^{-1} = \sum_k \lambda_k \Sigma_k^{-1}$. Conversely, this is exactly the pooling form the meta-agent coarse-graining *rejects* ([[Meta-agents and hierarchical emergence]]): it uses a gauge-covariant *sandwich average* (linear pool) of constituent covariances rather than a PoE, to avoid the over-sharpening/veto pathology a product imposes when fusing constituent beliefs.

## Cross-links

- Concepts: [[Variational free energy]], [[Belief coupling]], [[Multi-agent variational free energy]], [[Meta-agents and hierarchical emergence]]
- Related sources: [[friston-2010-free-energy-principle]], [[kingma-2013-auto-encoding-variational-bayes]], [[bordley-1982-multiplicative-pooling]], [[genest-zidek-1986-pooling]]
- Project: [[VFE Transformer Program]], [[participatory-it-from-bit]]

## BibTeX

```bibtex
@article{HintonPoE2002,
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
