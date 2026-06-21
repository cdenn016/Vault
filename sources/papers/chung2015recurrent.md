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
  - Courville, Aaron C.
  - Bengio, Yoshua
year: 2015
arxiv: 1506.02216
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
> Chung, J., Kastner, K., Dinh, L., Goel, K., Courville, A. C., & Bengio, Y. (2015). "A Recurrent Latent Variable Model for Sequential Data." *Advances in Neural Information Processing Systems 28* (NeurIPS 2015). arXiv:1506.02216.

## TL;DR

This paper introduces the Variational RNN (VRNN), a generative sequence model that incorporates stochastic latent variables at every time step into the hidden state of a recurrent neural network. The key insight is that the deterministic hidden state of standard RNNs is insufficient to capture the high variability observed in structured sequential data such as speech or handwriting; injecting a VAE-style latent variable at each step enriches the model's capacity to represent complex temporal distributions. The VRNN is trained end-to-end via a time-averaged variational lower bound (ELBO), yielding state-of-the-art performance on speech and handwriting generation benchmarks at the time of publication.

## Problem & setting

Standard RNNs maintain a deterministic hidden state that evolves according to a fixed transition function, which can underfit the rich variability inherent in high-dimensional sequential data such as speech waveforms or handwriting trajectories. The variational autoencoder (VAE) had recently demonstrated that injecting stochastic latent variables into the generative model of i.i.d. data dramatically improves representational capacity, but extending this idea to sequences in a principled way — where the prior and approximate posterior over the latent variable at each step are allowed to depend on the past — remained an open problem. Prior work (e.g., the Stochastic RNN of Bayer & Osendorfer 2014) placed latent variables only at transitions rather than within steps, or used simpler dynamics.

## Method

The VRNN couples a VAE with a recurrent network by conditioning both the prior and the approximate posterior on the RNN hidden state at each time step. Concretely, at step $t$:

- **Prior:** $p_\theta(\mathbf{z}_t \mid \mathbf{h}_{t-1}) = \mathcal{N}(\mu_{0,t},\, \mathrm{diag}(\sigma_{0,t}^2))$, where $\mu_{0,t}, \sigma_{0,t}$ are outputs of an MLP applied to $\mathbf{h}_{t-1}$.
- **Approximate posterior (encoder):** $q_\phi(\mathbf{z}_t \mid \mathbf{x}_{\le t}, \mathbf{z}_{<t}) = \mathcal{N}(\mu_t,\, \mathrm{diag}(\sigma_t^2))$, conditioned on both $\mathbf{x}_t$ and $\mathbf{h}_{t-1}$.
- **Generative model (decoder):** $p_\theta(\mathbf{x}_t \mid \mathbf{z}_{\le t}, \mathbf{x}_{<t})$ conditioned on $\mathbf{z}_t$ and $\mathbf{h}_{t-1}$.
- **Hidden state update:** $\mathbf{h}_t = f_\theta(\varphi^x(\mathbf{x}_t),\, \varphi^z(\mathbf{z}_t),\, \mathbf{h}_{t-1})$, where $\varphi^x$ and $\varphi^z$ are feature extraction networks and $f_\theta$ is a standard RNN (LSTM or GRU).

Training maximises the sequence-level ELBO:

$$\mathcal{L} = \sum_{t=1}^{T} \left[ \mathbb{E}_{q_\phi(\mathbf{z}_t|\cdot)}\bigl[\log p_\theta(\mathbf{x}_t \mid \mathbf{z}_{\le t}, \mathbf{x}_{<t})\bigr] - D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z}_t \mid \cdot) \,\|\, p_\theta(\mathbf{z}_t \mid \mathbf{h}_{t-1})\bigr) \right].$$

Crucially, the prior is not a fixed standard Gaussian but a learned, history-conditioned distribution — this is the central architectural departure from the standard VAE.

## Key results

The VRNN achieves state-of-the-art log-likelihood on four speech datasets (Blizzard, TIMIT, Onomatopoeia, and Accent) and on the IAM-OnDB handwriting dataset, outperforming deterministic RNNs and earlier stochastic sequence models (SRNN, STORN). Ablation experiments confirm that the history-conditioned prior (rather than a fixed Gaussian prior) is essential for strong performance: replacing it with a standard $\mathcal{N}(0, I)$ prior degrades results substantially, demonstrating that the recurrent structure of the prior is what allows the model to capture temporal coherence. Generated speech and handwriting samples show qualitatively natural variability.

## Relevance to this research

The VRNN is directly relevant to the VFE transformer program via several conceptual bridges. First, the per-step variational lower bound of the VRNN is structurally parallel to the free energy functional at the heart of the gauge-theoretic VFE model: the KL term $D_{\mathrm{KL}}(q \| p)$ is the self-coupling $\alpha \cdot \mathrm{KL}(q_i \| p_i)$ in the VFE, and the reconstruction term corresponds to the observation likelihood $-\mathbb{E}_q[\log p(o \mid x)]$. The VRNN's history-conditioned prior $p(\mathbf{z}_t \mid \mathbf{h}_{t-1})$ is an instance of the belief-to-prior coupling that the VFE transformer realises via the PriorBank: in both cases the prior is dynamic and context-dependent rather than fixed. Second, the reparameterization trick used to train the VRNN is the same gradient estimator underpinning all variational approaches in the VFE codebase. Third, the VRNN's latent tuple $(\mu_t, \sigma_t)$ — a mean and diagonal covariance propagated through time — is a Gaussian belief tuple of exactly the form $(mu, \Sigma, \phi)$ central to the VFE_3.0 design. The temporal recurrence in the VRNN's hidden state is analogous to how the VFE transformer's iterative minimisation propagates belief states across layers. The paper thus provides a well-studied precedent for treating sequential belief propagation as variational inference, and its per-step ELBO decomposition is useful background for the [[gl-k-attention|GL(K) attention manuscript]] where the attention step is derived as a stationary point of the free energy functional over belief couplings $\beta_{ij}$.

## Cross-links
- Concepts: [[Variational free energy]], [[Evidence lower bound (ELBO)]], [[Reparameterization trick]], [[Amortized inference]], [[Prediction error]]
- Related sources: [[kingma-2013-auto-encoding-variational-bayes]], [[marino-2018-iterative-amortized-inference]], [[sonderby-2016-ladder-vae]]
- Manuscript/Project: [[VFE Transformer Program]], [[gl-k-attention]]

## BibTeX
```bibtex
@inproceedings{chung2015recurrent,
  author    = {Chung, Junyoung and Kastner, Kyle and Dinh, Laurent and Goel, Kratarth and Courville, Aaron C. and Bengio, Yoshua},
  title     = {A Recurrent Latent Variable Model for Sequential Data},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {28},
  year      = {2015},
  url       = {https://arxiv.org/abs/1506.02216},
}
```
