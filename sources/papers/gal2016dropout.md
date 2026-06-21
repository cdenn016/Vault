---
type: paper
title: "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning"
aliases:
  - "Gal 2016"
  - "MC Dropout"
authors:
  - Gal, Yarin
  - Ghahramani, Zoubin
year: 2016
arxiv: "1506.02142"
url: https://arxiv.org/abs/1506.02142
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning

> [!info] Citation
> Gal, Yarin and Ghahramani, Zoubin (2016). "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning." Proceedings of the 33rd International Conference on Machine Learning (ICML), JMLR: W&CP volume 48. arXiv:1506.02142.

## TL;DR

This paper establishes a theoretical equivalence between dropout training in deep neural networks and approximate Bayesian inference in deep Gaussian processes. The central result is that minimizing the standard dropout objective is equivalent to minimizing the KL divergence between a Bernoulli variational distribution over network weights and the posterior of a deep GP. This equivalence allows uncertainty estimates to be extracted from any existing dropout-trained network by collecting the variance of stochastic forward passes at test time (Monte Carlo dropout), without modifying the model or incurring additional training cost.

## Problem & setting

Standard deep learning tools for regression and classification do not capture model uncertainty: softmax outputs are frequently misread as model confidence, yet a network can assign high-confidence predictions to inputs far from the training distribution. Bayesian neural networks address this gap but impose prohibitive inference costs (doubled parameter counts, slow convergence). The paper asks whether the already-ubiquitous dropout regularizer can be reinterpreted to yield principled, cheap uncertainty estimates.

## Method

The authors show that a neural network with arbitrary depth and nonlinearities, with Bernoulli dropout applied before every weight layer, approximates a deep Gaussian process whose covariance function is determined by the choice of nonlinearity and weight regularization. Concretely, they define a variational distribution $q(\omega)$ over weight matrices whose columns are randomly zeroed:

$$W_i = M_i \cdot \mathrm{diag}([z_{i,j}]_{j=1}^{K_i}), \quad z_{i,j} \sim \mathrm{Bernoulli}(p_i),$$

and show that minimizing the dropout training objective $\mathcal{L}_{\mathrm{dropout}}$ is equivalent to minimizing the KL objective

$$-\int q(\omega)\log p(Y|X,\omega)\,d\omega + \mathrm{KL}(q(\omega)\|p(\omega)).$$

At test time, the predictive mean and variance are estimated via $T$ stochastic forward passes (MC dropout):

$$\mathbb{E}_{q}[y^*] \approx \frac{1}{T}\sum_{t=1}^T \hat{y}^*(x^*, W_1^t,\ldots,W_L^t), \quad \mathrm{Var}_q[y^*] \approx \tau^{-1}I + \frac{1}{T}\sum_t \hat{y}^{*T}\hat{y}^* - \mathbb{E}_q[y^*]^T\mathbb{E}_q[y^*],$$

where $\tau = p\,l^2/(2N\lambda)$ links model precision to weight decay $\lambda$, prior length-scale $l$, dropout probability $p$, and dataset size $N$.

## Key results

Across ten UCI regression benchmarks, MC dropout matches or outperforms Probabilistic Backpropagation (PBP) and Graves (2011) variational inference in both RMSE and predictive log-likelihood on all datasets except Yacht Hydrodynamics (where PBP edges ahead in RMSE). On MNIST classification, stochastic forward-pass scatter plots reveal that softmax uncertainty envelopes capture genuine model ignorance for ambiguous rotated-digit inputs that standard softmax confidence misses. In a 2D reinforcement learning task, Thompson sampling driven by dropout uncertainty achieves rewards above 1 within 25 batches from burn-in, whereas epsilon-greedy requires 175 batches to reach the same level. Deeper networks and more training epochs consistently improve both RMSE and log-likelihood over the baseline one-hidden-layer result (Table 2 in the paper).

## Relevance to this research

The VFE transformer maintains explicit Gaussian belief tuples $(μ, Σ, φ)$ and minimizes a variational free energy that subsumes KL divergences between beliefs and priors. The Gal–Ghahramani result is directly germane in two ways. First, it provides a reference anchor for what "approximate Bayesian inference via KL minimization" means in a computationally tractable setting, grounding the VFE hierarchy's free-energy functional in a concrete finite-network analog. Second, the MC dropout predictive variance formula — expressing epistemic uncertainty as the sample variance of stochastic forward passes — is structurally analogous to how the VFE transformer propagates $\Sigma$ through attention layers: both track second-moment information that standard (deterministic, point-estimate) architectures discard. The connection is particularly relevant to the $\alpha_i$ self-coupling term $\alpha \cdot \mathrm{KL}(q_i \| p_i)$, which penalizes beliefs that deviate from priors and plays the same regularization role as dropout's weight-decay-through-$\tau$. The paper also illustrates why uncertainty representation is indispensable for active inference and reinforcement learning — a motivation the VFE program shares. It does not address gauge equivariance, SPD geometry, or GL(K) transport, so its relevance is at the level of the variational inference substrate rather than the geometric superstructure.

## Cross-links
- Concepts: [[Variational Free Energy]] [[Gaussian Process]] [[KL Divergence]] [[Approximate Bayesian Inference]]
- Related sources: [[kingma2013vae]] [[blundell2015weight]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{gal2016dropout,
  author    = {Gal, Yarin and Ghahramani, Zoubin},
  title     = {Dropout as a {B}ayesian Approximation: Representing Model Uncertainty in Deep Learning},
  booktitle = {Proceedings of the 33rd International Conference on Machine Learning},
  series    = {JMLR: W\&CP},
  volume    = {48},
  year      = {2016},
  note      = {arXiv:1506.02142},
}
```
