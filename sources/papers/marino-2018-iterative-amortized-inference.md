---
type: paper
title: Iterative Amortized Inference
aliases:
  - "Marino 2018 — Iterative Amortized Inference"
authors:
  - Joseph Marino
  - Yisong Yue
  - Stephan Mandt
year: 2018
arxiv: "1807.09356"
url: https://arxiv.org/abs/1807.09356
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-18
updated: 2026-06-18
---

# Iterative Amortized Inference

> [!info] Citation
> Joseph Marino, Yisong Yue, and Stephan Mandt (2018). *Iterative Amortized Inference*. arXiv:1807.09356. [https://arxiv.org/abs/1807.09356](https://arxiv.org/abs/1807.09356)

## TL;DR

Standard variational autoencoders use an *amortized* inference network that maps each data point directly to the parameters of its approximate posterior in a single forward pass. This shortcut is fast but leaves an *amortization gap*: the network's one-shot guess is generically worse than the optimum a per-datapoint optimizer would reach. Marino, Yue, and Mandt propose **iterative amortized inference**: instead of emitting posterior parameters directly, the inference model learns to *refine* them by repeatedly encoding the gradients of the variational objective. The result is a learned optimizer that closes much of the amortization gap while keeping inference fast, and it subsumes ordinary single-pass and top-down inference as special cases.

## Problem & setting

In amortized variational inference (see [[Amortized inference]] and the [[Variational autoencoder (VAE)]]), a recognition network $f_\phi(x)$ predicts the parameters of the approximate posterior $q(z\mid x)$ — for a Gaussian belief, its mean and (co)variance — so that inference reduces to one feed-forward evaluation shared across all data. The training signal is the [[Evidence lower bound (ELBO)]], equivalently the negative [[Variational free energy]]. The weakness is structural: because $f_\phi$ must serve every input through a fixed map, its output for any particular $x$ rarely coincides with the true ELBO-maximizing $q$. The shortfall in ELBO between the amortized prediction and the per-datapoint optimum is the *amortization gap*, and it is distinct from the *approximation gap* set by the variational family.

## Method

The central idea is to treat inference as *optimization that is itself learned*. Rather than predicting $q$'s parameters outright, an iterative inference model takes the current belief together with the gradient of the variational objective with respect to that belief, and outputs an update:

$$\lambda_{t+1} = \lambda_t + f_\phi\big(\lambda_t,\ \nabla_{\lambda_t}\mathcal{L}\big),$$

where $\lambda_t$ are the current posterior parameters (e.g. the Gaussian mean and variance) and $\mathcal{L}$ is the ELBO / free energy. Iterating this map for a few steps progressively tightens the bound, so the network learns an *update rule* — a data-driven counterpart to gradient ascent on the belief — instead of a direct encoder. The authors show that the conventional single-pass VAE encoder is the one-step, gradient-agnostic special case, and that several empirically successful "top-down" inference architectures fall out naturally as instances of encoding errors/gradients at each level. This places amortized and iterative inference on a common footing with the gradient-based belief updates of [[Iterative amortized inference]] used in predictive-coding-style schemes.

## Key results

- Iterative inference models **outperform standard single-pass inference models** on benchmark image and text datasets, achieving higher ELBO / lower negative log-likelihood by narrowing the amortization gap.
- The framework **unifies** direct, iterative, and top-down inference, explaining why top-down architectures help: they amount to encoding hierarchical prediction errors and gradients.
- Only a **small number of refinement steps** is needed, so the accuracy gain comes at modest extra compute, preserving the practical appeal of amortization.

## Relevance to this research

This paper is the conceptual template for the **E-step** of the VFE-transformer. In that model each token carries a Gaussian belief $(\mu, \Sigma)$ over its latent, and `gradient_mode: filtering` updates those beliefs by following free-energy gradients rather than re-deriving them from scratch — exactly the "learn to perform inference optimization through repeatedly encoding gradients" recipe formalized here. Concretely:

- The per-token mean $\mu$ and covariance $\Sigma$ play the role of Marino et al.'s posterior parameters $\lambda$; the filtering E-step is their iterative update $\lambda_{t+1} = \lambda_t + f_\phi(\lambda_t, \nabla \mathcal{L})$ applied along the sequence.
- The objective whose gradient is encoded is the model's ELBO / [[Variational free energy]], so the [[Prediction error]] signals that drive each refinement are the same quantities this paper feeds into its inference network.
- Framing the E-step as a learned optimizer (rather than a closed-form coordinate-ascent step) is precisely the amortization-gap-closing move motivated here, and it dovetails with the predictive-coding reading of belief updates and with [[Precision weighting]] of those errors in the attention block.

> [!note] Editorial: The VFE-transformer's covariance $\Sigma$ lives on the SPD manifold, so a faithful filtering E-step must take the iterative update of this paper into the Riemannian setting (affine-invariant retraction on $(\mu,\Sigma)$) rather than the Euclidean parameter space Marino et al. assume. The iterative-amortization principle is what carries over; the geometry of the step does not.

## Cross-links

- [[Amortized inference]]
- [[Iterative amortized inference]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Prediction error]]
- [[Precision weighting]]
- [[Variational autoencoder (VAE)]]
- [[Variational EM]]
- [[Predictive coding network]]
- Related sources: [[kingma-2013-auto-encoding-variational-bayes]], [[marino-2018-iterative-amortized-inference]], [[neal-1998-variational-em]], [[rao-1999-predictive-coding]], [[millidge-2020-pc-approximates-backprop]]

## BibTeX

```bibtex
@inproceedings{marino2018iterative,
  title     = {Iterative Amortized Inference},
  author    = {Marino, Joseph and Yue, Yisong and Mandt, Stephan},
  booktitle = {Proceedings of the 35th International Conference on Machine Learning (ICML)},
  year      = {2018},
  eprint    = {1807.09356},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1807.09356}
}
```
