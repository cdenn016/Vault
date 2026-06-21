---
type: paper
title: "A Recurrent Latent Variable Model for Sequential Data"
aliases:
  - "Chung 2015"
  - "VRNN"
authors:
  - Chung, Junyoung
  - Kastner, Kyle
  - Dinh, Laurent
  - Goel, Kratarth
  - Courville, Aaron
  - Bengio, Yoshua
year: 2015
arxiv: "1506.02216"
url: https://arxiv.org/abs/1506.02216
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A Recurrent Latent Variable Model for Sequential Data

> [!info] Citation
> Chung, J., Kastner, K., Dinh, L., Goel, K., Courville, A., & Bengio, Y. (2015). "A Recurrent Latent Variable Model for Sequential Data." arXiv:1506.02216.

## TL;DR
The paper introduces the Variational Recurrent Neural Network (VRNN), which embeds a VAE at every timestep of an RNN so that the prior over latent variables is conditioned on the RNN hidden state rather than being a fixed Gaussian. This temporally-structured prior over latent variables allows the model to capture the high-level variability in structured sequential data — such as natural speech — more faithfully than standard RNNs or VAEs with independent priors. Empirically, VRNN outperforms baseline RNN-Gauss and RNN-GMM models on four speech datasets and a handwriting dataset in terms of log-likelihood.

## Problem & setting
Standard RNNs have entirely deterministic transition functions; all randomness is confined to the conditional output distribution. This is inadequate for highly structured, high-signal-to-noise sequential data (e.g., natural speech) where the underlying sources of variability are complex and temporally correlated. Prior work (STORN, DRAW) introduced latent random variables into RNNs but kept the prior independent across timesteps. The VRNN is designed to remedy this by introducing temporal dependencies in the latent prior.

## Method
The VRNN places a VAE at each timestep $t$, conditioned on the previous RNN hidden state $h_{t-1}$. The conditional prior is

$$z_t \sim \mathcal{N}(\mu_{0,t}, \mathrm{diag}(\sigma_{0,t}^2)), \quad [\mu_{0,t}, \sigma_{0,t}] = \phi^\mathrm{prior}_\tau(h_{t-1}),$$

the generating distribution is

$$x_t | z_t \sim \mathcal{N}(\mu_{x,t}, \mathrm{diag}(\sigma_{x,t}^2)), \quad [\mu_{x,t}, \sigma_{x,t}] = \phi^\mathrm{dec}_\tau(\phi^z_\tau(z_t), h_{t-1}),$$

and the approximate posterior is

$$z_t | x_t \sim \mathcal{N}(\mu_{z,t}, \mathrm{diag}(\sigma_{z,t}^2)), \quad [\mu_{z,t}, \sigma_{z,t}] = \phi^\mathrm{enc}_\tau(\phi^x_\tau(x_t), h_{t-1}).$$

The RNN hidden state is updated as $h_t = f_\theta(\phi^x_\tau(x_t), \phi^z_\tau(z_t), h_{t-1})$. Training maximises the timestep-wise variational lower bound

$$\mathbb{E}_{q(z_{\le T}|x_{\le T})}\left[\sum_{t=1}^T \left(-\mathrm{KL}(q(z_t|x_{\le t}, z_{<t}) \| p(z_t|x_{<t}, z_{<t})) + \log p(x_t|z_{\le t}, x_{<t})\right)\right],$$

with the reparameterisation trick enabling gradient flow through the stochastic nodes.

## Key results
On all four speech datasets (Blizzard, TIMIT, Onomatopoeia, Accent) the VRNN-Gauss and VRNN-GMM variants achieve substantially higher log-likelihood than RNN-Gauss and RNN-GMM baselines. The VRNN-I variant (independent prior, no temporal conditioning) lies consistently between the RNN baselines and the full VRNN, confirming that the temporally-structured prior is the key driver of improvement. On the handwriting task (IAM-OnDB), gains are smaller but still present. Qualitatively, VRNN-Gauss generates less noisy audio waveforms than RNN-GMM, and VRNN-GMM generates handwriting with more consistent style across a sample.

## Relevance to this research
The VRNN's per-timestep VAE with a recurrent, state-conditioned prior is a close structural precursor to the VFE transformer's iterative belief update over Gaussian tuples $(\mu, \Sigma, \phi)$. The ELBO objective in Eq. (11) — a sum of $-\mathrm{KL}(q \| p) + \log p(x|z)$ terms — is the per-step variational free energy minimised in the VFE framework; the self-coupling $\alpha \cdot \mathrm{KL}(q_i \| p_i)$ term in the VFE Lagrangian corresponds directly to the KL regulariser here. The temporally-structured prior (conditioning on $h_{t-1}$) parallels the way the VFE transformer's prior bank $p_i$ is updated via gauge-transported beliefs from neighboring tokens. The reparameterisation trick and joint generative/inference training are also foundational to understanding how backprop interacts with the variational objective in the VFE codebase.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Gaussian Beliefs]], [[Variational Autoencoder]]
- Related sources: [[kingma-2013-vae]], [[rezende-2014-stochastic-backprop]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{chung2015recurrent,
  author  = {Chung, Junyoung and Kastner, Kyle and Dinh, Laurent and Goel, Kratarth and Courville, Aaron and Bengio, Yoshua},
  title   = {A Recurrent Latent Variable Model for Sequential Data},
  journal = {arXiv preprint arXiv:1506.02216},
  year    = {2015},
}
```
