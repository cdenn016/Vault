---
type: paper
title: "Sequential Neural Models with Stochastic Layers"
aliases:
  - "Fraccaro 2016"
  - "SRNN"
authors:
  - Fraccaro, Marco
  - Sønderby, Søren Kaae
  - Paquet, Ulrich
  - Winther, Ole
year: 2016
arxiv: "1605.07571"
url: https://arxiv.org/abs/1605.07571
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Sequential Neural Models with Stochastic Layers

> [!info] Citation
> Fraccaro, M., Sønderby, S. K., Paquet, U., & Winther, O. (2016). "Sequential Neural Models with Stochastic Layers." arXiv:1605.07571.

## TL;DR
This paper introduces the Stochastic Recurrent Neural Network (SRNN), which combines a deterministic RNN with a nonlinear state space model (SSM) by keeping them as cleanly separated layers. The key insight is that this separation allows the posterior over latent states to retain a Markov structure, enabling a structured variational inference network (smoothing via a backward RNN) rather than a mean-field approximation. SRNN achieves state-of-the-art ELBO on Blizzard and TIMIT speech datasets by a large margin over the VRNN and related models.

## Problem & setting
Modeling complex sequential data (speech, music) with uncertainty in latent states. Prior work either used purely deterministic RNNs (no uncertainty propagation) or stochastic models like the VRNN where the stochastic and deterministic units are interleaved, creating conditional independence structures that preclude smoothing-style inference. SSMs support principled Bayesian filtering/smoothing but are traditionally restricted to exponential family transitions for tractability.

## Method
The SRNN defines a generative model by stacking a nonlinear SSM on top of a standard RNN. The joint factorization is:

$$p_\theta(x_{1:T}, z_{1:T}, d_{1:T} | u_{1:T}) = \prod_t p_{\theta_x}(x_t | z_t, d_t)\, p_{\theta_z}(z_t | z_{t-1}, d_t)\, p_{\theta_d}(d_t | d_{t-1}, u_t)$$

where $d_t$ is deterministic (GRU-computed) and $z_t$ is stochastic with a Gaussian prior whose mean and log-variance are parameterized by neural networks depending on $z_{t-1}$ and $d_t$. Because $d_{1:T}$ follows a delta distribution, it integrates out exactly, yielding an ELBO of the form

$$\mathcal{F}_i(\theta, \phi) = \mathbb{E}_{q_\phi}\!\left[\log p_\theta(x_{1:T} | z_{1:T}, \tilde{d}_{1:T})\right] - \mathrm{KL}\!\left(q_\phi(z_{1:T} | \tilde{d}_{1:T}, x_{1:T}, z_0) \,\|\, p_\theta(z_{1:T} | \tilde{d}_{1:T}, z_0)\right).$$

The variational approximation mirrors the true posterior structure $q_\phi(z_{1:T}) = \prod_t q_\phi(z_t | z_{t-1}, a_t)$, where $a_t = g_{\phi_a}(a_{t+1}, [d_t, x_t])$ is a backward-recurrent summary of future observations (smoothing). A "Resq" parameterization improves training stability by learning the residual between the variational mean and the predictive prior mean: $\mu^{(q)}_t = \hat{\mu}^{(p)}_t + \mathrm{NN}^{(q)}_1(z_{t-1}, a_t)$, so the inference network only needs to correct the prior's dynamics rather than learn them from scratch.

## Key results
On Blizzard speech (0.5s sequences), SRNN (smooth+Resq) achieves a log-likelihood lower bound of $\geq 11991$ versus $\geq 9107$ for VRNN-GMM — an improvement of roughly 31%. On TIMIT (avg. 3.1s sequences), SRNN achieves $\geq 60550$ versus $\geq 28982$ for VRNN-GMM — more than doubling the bound. On four polyphonic music benchmarks (Nottingham, JSB chorales, MuseData, Piano-midi.de), SRNN performs comparably to competing methods including NASMC and STORN, though not at the level of RNN-NADE (which uses a specialized output distribution). Smoothing consistently outperforms filtering, and the Resq parameterization improves results in 3 out of 4 speech configurations.

## Relevance to this research
SRNN is directly relevant to the VFE transformer program's treatment of beliefs as Gaussian tuples propagated through a generative hierarchy. The paper's ELBO decomposes as a sum of per-timestep KL divergences between variational posteriors and structured priors — exactly the belief-coupling and self-coupling terms in the VFE free energy functional. The Resq residual parameterization (learning corrections to the predictive prior mean rather than the full mean) mirrors the VFE perspective that inference updates should be understood as corrections to transported prior beliefs. The clean separation of deterministic and stochastic layers in SRNN also resonates with the VFE transformer's separation of gauge transport (deterministic, equivariant) from belief updates (stochastic, VFE-driven). The structured variational approximation that exploits d-separation and Markov structure of the posterior is analogous to how the VFE attention weights $\beta_{ij}$ are derived as stationary points of a well-defined free energy rather than ad hoc softmax outputs.

## Cross-links
- Concepts: [[Variational Free Energy]], [[ELBO]], [[State Space Models]], [[Gaussian Beliefs]]
- Related sources: [[chung2015recurrent]] (VRNN), [[krishnan2015deep]] (Deep Kalman Filter)
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{fraccaro2016sequential,
  author  = {Fraccaro, Marco and S{\o}nderby, S{\o}ren Kaae and Paquet, Ulrich and Winther, Ole},
  title   = {Sequential Neural Models with Stochastic Layers},
  journal = {arXiv preprint arXiv:1605.07571},
  year    = {2016},
}
```
