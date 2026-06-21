---
type: paper
title: "Adam: A Method for Stochastic Optimization"
aliases:
  - "Kingma 2015"
  - "Adam optimizer"
authors:
  - Kingma, Diederik P.
  - Ba, Jimmy Lei
year: 2015
arxiv: "1412.6980"
url: https://arxiv.org/abs/1412.6980
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Adam: A Method for Stochastic Optimization

> [!info] Citation
> Kingma, Diederik P. and Ba, Jimmy Lei (2015). "Adam: A Method for Stochastic Optimization." Published as a conference paper at ICLR 2015. arXiv:1412.6980.

## TL;DR

Adam (Adaptive Moment Estimation) is a first-order stochastic optimization algorithm that computes per-parameter adaptive learning rates from exponential moving averages of the gradient (first moment) and its elementwise square (second raw moment). Bias-correction terms counteract the zero-initialization of the moment accumulators. The method combines AdaGrad's ability to handle sparse gradients with RMSProp's suitability for non-stationary objectives, and achieves an O(sqrt(T)) regret bound in the online convex setting.

## Problem & setting

Stochastic gradient-based optimization of high-dimensional, possibly non-stationary objective functions. Prior adaptive methods either lack bias correction (RMSProp) or accumulate gradient history monotonically causing step-size collapse (AdaGrad). The goal is a method that works across sparse and dense gradient regimes, is invariant to diagonal rescaling of gradients, requires little memory, and is easy to tune.

## Method

At each timestep t, Adam maintains two exponential moving averages of the gradient g_t:

- First moment (mean): m_t = beta_1 * m_{t-1} + (1 - beta_1) * g_t
- Second raw moment (uncentered variance): v_t = beta_2 * v_{t-1} + (1 - beta_2) * g_t^2

Both are initialized to zero, inducing bias toward zero early in training. Bias-corrected estimates are formed as:

- m_hat_t = m_t / (1 - beta_1^t)
- v_hat_t = v_t / (1 - beta_2^t)

The parameter update is then:

theta_t = theta_{t-1} - alpha * m_hat_t / (sqrt(v_hat_t) + epsilon)

Default hyperparameters: alpha = 0.001, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-8.

The effective stepsize |Delta_t| <= alpha, establishing a trust region. The ratio m_hat / sqrt(v_hat) is interpreted as a signal-to-noise ratio: when it is small (high uncertainty), the effective step shrinks, providing automatic annealing. The update is invariant to gradient rescaling since scaling g by c scales m_hat by c and v_hat by c^2, which cancel.

AdaMax, a variant based on the L-infinity norm, replaces v_hat_t with u_t = max(beta_2 * u_{t-1}, |g_t|), yielding a simpler bound |Delta_t| <= alpha without bias correction.

The connection to information geometry: v_hat_t approximates the diagonal of the Fisher information matrix (Pascanu & Bengio, 2013), making Adam a diagonal natural gradient preconditioner, though more conservative than vanilla NGD.

## Key results

Theorem 4.1 establishes an O(sqrt(T)) regret bound for Adam with decaying learning rate alpha_t = alpha / sqrt(t) and exponentially decaying beta_{1,t}: the regret R(T) is bounded by a sum involving sqrt(T * v_hat_{T,i}) (geometry-adaptive term) and the L2 norms of the gradient histories. For sparse gradients this bound improves to O(log(d) * sqrt(T)) versus O(sqrt(dT)) for non-adaptive SGD.

Corollary 4.2: R(T)/T = O(1/sqrt(T)) -> 0, so average regret converges.

Empirically: Adam matches or outperforms SGD with Nesterov momentum and AdaGrad on logistic regression (MNIST, IMDB sparse BoW), multilayer neural networks with dropout, and convolutional networks (CIFAR-10). Bias correction is shown to be critical for stability when beta_2 is close to 1 (the case for sparse gradients): without it, RMSProp-style updates diverge in early training.

## Relevance to this research

Adam is the standard first-order optimizer used in training the VFE transformer's learnable parameters (connection_W, head_mixer weights, learnable lambda/alpha/r scalars, T5 bias tables, prior bank). Understanding its diagonal Fisher preconditioner interpretation is directly relevant to the M-step design: the VFE framework's natural alternative is a Killing-metric or exact Fisher M-step on the SPD belief manifold, against which Adam's diagonal approximation is contrasted. The bias-correction argument is a clean example of correcting for initialization bias in exponential averages, a pattern that appears in the exponential moving average of beta_ij attention weights and in the model-coupling gamma_ij updates.

## Cross-links

- Concepts: [[Natural gradient]], [[Fisher information matrix]], [[Variational free energy]]
- Related sources: [[amari-1998-natural-gradient]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{kingma2015adam,
  author    = {Kingma, Diederik P. and Ba, Jimmy Lei},
  title     = {Adam: {A} Method for Stochastic Optimization},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2015},
  note      = {arXiv:1412.6980}
}
```
