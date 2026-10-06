---
type: paper
title: "Energy Transformer"
aliases:
  - "Energy Transformer (Hoover 2023)"
  - "Hoover 2023 energy transformer"
  - "Hoover2023Energy"
authors:
  - Benjamin Hoover
  - Yuchen Liang
  - Bao Pham
  - Rameswar Panda
  - Hendrik Strobelt
  - Duen Horng Chau
  - Mohammed J. Zaki
  - Dmitry Krotov
year: 2023
arxiv: "2302.07253"
url: https://arxiv.org/abs/2302.07253
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/physics
created: 2026-10-06
---

# Energy Transformer

> [!info] Citation
> Hoover, B., Liang, Y., Pham, B., Panda, R., Strobelt, H., Chau, D. H., Zaki, M. J., and Krotov, D. (2023). *Energy Transformer.* Advances in Neural Information Processing Systems 36 (NeurIPS 2023). [arXiv:2302.07253](https://arxiv.org/abs/2302.07253) (v1, February 14, 2023; v2, November 1, 2023; cs.LG, cond-mat.dis-nn, cs.CV, q-bio.NC, stat.ML). Hoover, Liang and Pham contributed equally. The v2 PDF carries the NeurIPS 2023 footer. Code: [github.com/bhoov/energy-transformer-jax](https://github.com/bhoov/energy-transformer-jax).

## TL;DR

Energy Transformer (ET) replaces a stack of transformer blocks by one recurrent block whose update is gradient descent of an engineered global energy on layer-normalized tokens. The energy has an attention term, a log-sum-exp over keys of query-key alignments with no separate value matrix, and a "Hopfield Network" term that plays the role of the MLP with tied input and output weights. Because LayerNorm is the gradient of a Lagrangian with positive semidefinite Hessian, the continuous dynamics provably decrease the energy. The attention force has the conventional attention term with value matrix $(W^Q)^\top K$ plus a second term from differentiating through the keys, which the authors say is what makes recurrent descent valid. ET is trained by backpropagation through a fixed number of unrolled steps and evaluated on masked ImageNet patch completion (qualitative), graph anomaly detection and graph classification.

## Problem and setting

The authors take the transformer block as an empirically assembled combination of attention, MLP, residual connection and LayerNorm, and ask for a block whose operations, their order and their weight symmetries are dictated by one energy function, in the tradition of Dense Associative Memory (modern Hopfield) networks ([[krotov-2016-dense-associative-memory]], [[ramsauer2021hopfield]]). They contrast this with [[yang-2022-transformers-optimization-perspective]], which starts from the block and seeks an energy under constraints; ET starts from the energy and accepts whatever architecture results. Tokens $x_A\in\mathbb R^D$ (patches or graph nodes with positional embeddings) are treated as interacting particles.

## Method

Each token is layer-normalized, $g_i=\gamma(x_i-\bar x)/\sqrt{\tfrac1D\sum_j(x_j-\bar x)^2+\varepsilon}+\delta_i$, which is $g_i=\partial\mathcal L/\partial x_i$ for the Lagrangian $\mathcal L=D\gamma\sqrt{\tfrac1D\sum_j(x_j-\bar x)^2+\varepsilon}+\sum_j\delta_jx_j$ (eqs. 1 and 2). The energy is $E=E_{\mathrm{ATT}}+E_{\mathrm{HN}}$ with
$$E_{\mathrm{ATT}}=-\frac1\beta\sum_h\sum_C\log\sum_{B\ne C}\exp(\beta A_{hBC}),\qquad A_{hBC}=\sum_\alpha K_{\alpha hB}Q_{\alpha hC},$$
$K=W^Kg$, $Q=W^Qg$ (eqs. 3 and 4), and $E_{\mathrm{HN}}=-\sum_B\sum_\mu G(\xi_\mu\cdot g_B)$ with learned memories $\xi\in\mathbb R^{K\times D}$ and $G'=r$ an activation (ReLU for a classical continuous Hopfield network, a sharply peaked power or softmax for a modern one) (eq. 5). The dynamics are $\tau\,dx_{iA}/dt=-\partial E/\partial g_{iA}$ (eq. 6), and $dE/dt=-\tfrac1\tau\sum\partial_gE\,M\,\partial_gE\le0$ with $M=\partial^2\mathcal L/\partial x\partial x$ positive semidefinite (eqs. 7 and 8). Attention and the Hopfield module act in parallel on the same normalized tokens, not in sequence. For one head the attention force is
$$-\frac{\partial E_{\mathrm{ATT}}}{\partial g_{iA}}=\sum_{C\ne A}\sum_\alpha\Big[W^Q_{\alpha i}K_{\alpha C}\operatorname{softmax}_C(\beta K_C\!\cdot\!Q_A)+W^K_{\alpha i}Q_{\alpha C}\operatorname{softmax}_A(\beta K_A\!\cdot\!Q_C)\Big],$$
the first term being conventional attention with $V=(W^Q)^\top K$ and the second the new term. The Hopfield force $\sum_\mu\xi_{\mu i}G'(\xi_\mu\cdot g_A)$ (eq. 9) is token-wise, a tied-weight MLP. Unlike a modern Hopfield network, whose keys are fixed memories, ET's keys evolve with the queries.

In practice the ODE is discretized with step $\alpha=dt/\tau=0.1$ for $T=12$ steps in the image model (Table 4: token dimension 768, 12 heads of dimension 64, $\beta=1/8$, 3072 Hopfield memories, Adam with learning rate $5\times10^{-4}$ and gradient clipping, 100 epochs), the energy gradient is computed by JAX autodiff, and all parameters are trained by backpropagation through the unrolled steps on an MSE loss over masked patches. The graph-classification model stacks $S$ ET blocks, each with its own LayerNorm.

## Key results

On ImageNet-1K masked patch completion the paper shows qualitative reconstructions and decoder visualizations of the learned memories; the attention force dominates early and the Hopfield force sharpens patches late (Figure 4). In the image ablation (Table 14, validation MSE on masked tokens) the full model reaches 0.306, attention without the Hopfield module 0.343 to 0.403, and the Hopfield module without attention 0.825. On graph anomaly detection (Yelp, Amazon, T-Finance, T-Social at 1% and 40% training splits, Table 1) ET is best or near best in macro-F1 and AUC against GraphConsis, CAREGNN, PC-GNN, BWGNN, an MLP and a graph transformer; on graph classification over eight TUDataset sets (Table 2) it reports, for example, 90.3 on PROTEINS and 90.1 on NCI1 and trails EvoG on MUTAG (96.6 against 100.0). The ET block has about half the per-block parameters of a ViT-Base block (3.54M against 7.08M, Table 15); against a ViT reduced to 5.52M parameters, ET at 4.28M gives PSNR 21.51 against 22.11 on reconstruction (Table 16). No language-modeling result is reported.

## Relevance to this research

ET is the energy-first precedent for a transformer block: the authors choose an energy, and attention, the MLP analogue, LayerNorm and the residual structure follow as its descent dynamics, with a proof that the energy decreases. It derives three parts the GL(K) program still treats as neural, or partly so: LayerNorm (as the gradient of a Lagrangian), a tied-weight MLP (as a Hopfield energy over learned memories) and the residual update (as an Euler step). What it does not derive is the energy itself, which is "specifically engineered" for the task; the paper offers no probabilistic model of which $E$ is a negative log-density or free energy. Tokens are point vectors without covariance, there is no frame or gauge structure, and training is backpropagation through time over the unrolled dynamics. The GL(K) construction of [[dennis-2026-glk-attention-v2-rework-2026-10-05]] starts instead from Gaussian beliefs and exact inference: its routing is the source posterior of a stated model, its content is transported by group-valued links, and covariances propagate ([[GL(K) gauge-equivariant attention]]). Its MLP candidate, [[Template routing]] (`gaussian_template`), is the closest analogue to ET's Hopfield module, since with values tied to template means it reduces to modern-Hopfield retrieval against a bank of learned templates.

> [!note] Editorial: ET's second attention term, the force from differentiating the log-sum-exp through the keys of other tokens, is the sender-side part of a symmetric energy gradient. In the program's free energy the coupling $\sum_{ij}\beta_{ij}D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)$ likewise depends on the sender $q_j$, and a receiver update that holds the senders fixed does not include that force (the attention theme page records that a one-step belief update is a filter, not an argmin). ET is therefore a worked case in which keeping the sender-side force turns repeated application into guaranteed descent. This comparison is the vault's, not the paper's.

> [!note] Editorial: ET's energy is a Lyapunov function for its forward dynamics, but learning still uses backpropagation through the unrolled steps, so it is not a backprop-free model in the sense of [[dennis-2026-backprop-free-vfe-language-architecture]]. The paper does not attempt a local learning rule.

Wiki pages: [[GL(K) gauge-equivariant attention]], [[Attention mechanisms — theory and positional structure]], [[Energy-Based Models]], [[Associative Memory]], [[Template routing]].

## Cross-links

- Concepts: [[Energy-Based Models]], [[Associative Memory]], [[Softmax]], [[Multi-head attention]]
- Related sources: [[ramsauer2021hopfield]], [[krotov-2016-dense-associative-memory]], [[yang-2022-transformers-optimization-perspective]], [[yu-2023-white-box-transformers-sparse-rate-reduction]]

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/hoover-2023-energy-transformer-arxiv-2302.07253.pdf` ([local PDF](../pdfs/hoover-2023-energy-transformer-arxiv-2302.07253.pdf)), 28 pages, read by pypdf text extraction. Read: pages 1 to 10 in full (abstract through Discussion), Appendix B on ImageNet training with Table 4 (pp. 15 to 17), Appendix F on ablations (pp. 24 to 26), Appendix G on parameter counts (pp. 26 to 27) and the start of Appendix H (p. 28). Not read: the references (pp. 11 to 14), Appendix A (notation), and Appendices C to E (anomaly detection, graph classification and heterogeneous-graph details). Source: [arXiv:2302.07253](https://arxiv.org/pdf/2302.07253). SHA-256: `c90ed4990aef2a5cc8369e3536c32a4ce12105125d4ec8555ea70d808da62e8a`.

## BibTeX

```bibtex
@inproceedings{Hoover2023Energy,
  author        = {Hoover, Benjamin and Liang, Yuchen and Pham, Bao and Panda, Rameswar and Strobelt, Hendrik and Chau, Duen Horng and Zaki, Mohammed J. and Krotov, Dmitry},
  title         = {Energy Transformer},
  booktitle     = {Advances in Neural Information Processing Systems},
  volume        = {36},
  year          = {2023},
  eprint        = {2302.07253},
  archivePrefix = {arXiv}
}
```
