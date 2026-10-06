---
type: paper
title: "White-Box Transformers via Sparse Rate Reduction"
aliases:
  - "CRATE"
  - "Coding Rate Reduction Transformer"
  - "Yu 2023 white-box transformers"
  - "Yu2023WhiteBox"
authors:
  - Yaodong Yu
  - Sam Buchanan
  - Druv Pai
  - Tianzhe Chu
  - Ziyang Wu
  - Shengbang Tong
  - Benjamin D. Haeffele
  - Yi Ma
year: 2023
arxiv: "2306.01129"
url: https://arxiv.org/abs/2306.01129
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-10-06
---

# White-Box Transformers via Sparse Rate Reduction

> [!info] Citation
> Yu, Y., Buchanan, S., Pai, D., Chu, T., Wu, Z., Tong, S., Haeffele, B. D., and Ma, Y. (2023). *White-Box Transformers via Sparse Rate Reduction.* Advances in Neural Information Processing Systems 36 (NeurIPS 2023). [arXiv:2306.01129](https://arxiv.org/abs/2306.01129) (v1, June 1, 2023; cs.LG; 33 pages). Code: [github.com/Ma-Lab-Berkeley/CRATE](https://github.com/Ma-Lab-Berkeley/CRATE). The arXiv v1 abstract page and PDF do not name the venue; the NeurIPS 2023 placement is confirmed by the proceedings listing and the proceedings PDF footer found by web search. An extended journal version ("White-Box Transformers via Sparse Rate Reduction: Compression Is All There Is?", JMLR volume 25) also surfaced in that search and was not read.

## TL;DR

The paper posits that a representation should map each token to a mixture of low-dimensional zero-mean Gaussians supported on incoherent subspaces, measures this with the "sparse rate reduction" objective, and builds a transformer-like layer as one step of alternating minimization of that objective. The attention half (multi-head subspace self-attention, MSSA) is an approximate gradient step on a lossy coding rate of the tokens projected onto learned subspaces, with query, key and value all equal to the subspace basis $U_k^*$. The MLP half is replaced by one unrolled ISTA step for a nonnegative LASSO against a learned dictionary. The resulting CRATE networks are trained end to end by backpropagation on ImageNet-1K classification and trail ViT by 1.6 top-1 points at about 22M parameters (CRATE-B against ViT-S) and by 4.8 points at about 6M (CRATE-T against ViT-T), while layerwise measurements show the coding rate falling and sparsity rising with depth.

## Problem and setting

Tokens $Z=[z_1,\dots,z_N]\in\mathbb R^{d\times N}$ are to be transformed so that each token's marginal is a mixture of $K$ Gaussians $\mathcal N(0,\Sigma_k)$ supported on subspaces with orthonormal bases $U_k\in\mathbb R^{d\times p}$. The objective (eq. 1) is
$$\max_f\ \mathbb E_Z\big[R(Z)-R^c(Z;U_{[K]})-\lambda\|Z\|_0\big],\qquad Z=f(X),$$
with the lossy coding rate $R(Z)=\tfrac12\log\det(I+\tfrac{d}{N\epsilon^2}Z^*Z)$ (eq. 7) and the subspace-wise rate $R^c(Z;U_{[K]})=\sum_k\tfrac12\log\det(I+\tfrac{p}{N\epsilon^2}(U_k^*Z)^*(U_k^*Z))$ (eq. 8). The global map $f$ is realized as $L$ incremental layers $f^\ell$, each of which is supposed to improve the objective given a local model of the distribution of $Z^\ell$ (the layer's own $U^\ell_{[K]}$ and $D^\ell$). The authors separate forward "optimization" from backward "learning": the forward pass descends the objective for fixed layer parameters, and the parameters are learned by backpropagation with a downstream loss.

## Method

Section 2.2 gives an idealized motivation. For one token drawn from the subspace mixture and corrupted by Gaussian noise, Tweedie's formula gives the optimal denoiser $z^{\ell+1}=z^\ell+\sigma_\ell^2\nabla\log q^\ell(z^\ell)$, and under stated technical assumptions (small noise, equalized mixture normalizations) it is approximately a softmax over heads of $\|U_k^*z^\ell\|^2/2\sigma_\ell^2$ weighting the projections $U_k^*z^\ell$ (eq. 6).

Section 2.3 derives MSSA. The gradient of $R^c$ is $\nabla_ZR^c=\tfrac{p}{N\epsilon^2}\sum_kU_kU_k^*Z(I+\tfrac{p}{N\epsilon^2}(U_k^*Z)^*(U_k^*Z))^{-1}$ (eq. 9). Replacing the matrix inverse by an approximation and the token-similarity Gram matrix by a softmax membership "if we only use similar tokens to regress and denoise each other" (Approximation 4, Appendix A.2, which assumes unit-norm token columns, orthonormal incoherent $U_k$, and tokens lying near the union of subspaces) gives
$$Z^{\ell+1/2}\approx(1-\kappa\gamma)Z^\ell+\kappa\gamma\,\mathrm{MSSA}(Z^\ell\mid U_{[K]}),\quad \mathrm{SSA}(Z\mid U_k)=(U_k^*Z)\operatorname{softmax}((U_k^*Z)^*(U_k^*Z)),$$
with $\gamma=p/(N\epsilon^2)$ and the heads aggregated by $\gamma[U_1,\dots,U_K]$. This is softmax self-attention with $Q=K=V=U_k^*$ and a skip connection.

Section 2.4 replaces the MLP. Rather than differentiate the expansion term $R(Z)$, which needs a matrix inverse, the authors posit a complete incoherent or orthogonal dictionary $D\in\mathbb R^{d\times d}$ with $D^*D\approx I$, so that sparsifying with respect to $D$ approximately preserves $R$. The sparse-coding problem is relaxed to a nonnegative LASSO, $\min_{Z\ge0}\lambda\|Z\|_1+\|Z^{\ell+1/2}-DZ\|_F^2$, and one proximal-gradient (ISTA) step is unrolled: $Z^{\ell+1}=\mathrm{ReLU}(Z^{\ell+1/2}+\eta D^*(Z^{\ell+1/2}-DZ^{\ell+1/2})-\eta\lambda\mathbf 1)$ (eq. 17). Appendix A.3 calls this connection "high-level and heuristic" in the main text and gives a majorization-minimization derivation under further assumptions (normalized, mutually orthogonal token columns with $d\ge N$) that yields a slightly simplified ISTA block. The layer is $Z^{\ell+1/2}=Z^\ell+\mathrm{MSSA}(Z^\ell\mid U^\ell_{[K]})$, $Z^{\ell+1}=\mathrm{ISTA}(Z^{\ell+1/2}\mid D^\ell)$ (eq. 18), with layer-dependent parameters.

The implementation (Appendix B.1) departs from the derived layer in stated ways: the head aggregation $\tfrac{p}{N\epsilon^2}[U_1,\dots,U_K]$ is replaced by a free trainable $W\in\mathbb R^{d\times pK}$, LayerNorm is applied before both blocks, and the model is trained with the Lion optimizer (150 epochs, batch 2048) under a cross-entropy loss on a CLS token.

## Key results

Table 1 reports ImageNet-1K top-1 accuracy of 66.7, 69.2, 70.8 and 71.3 for CRATE-T, -S, -B and -L (6.09M, 13.12M, 22.80M and 77.64M parameters) against 71.5 for ViT-T (5.72M) and 72.4 for ViT-S (22.05M), trained under the same recipe; transfer by fine-tuning to CIFAR-10/100, Oxford Flowers-102 and Oxford-IIIT-Pets is close to ViT (for example 96.8 against 97.2 on CIFAR-10 for CRATE-B against ViT-S). The text gives CRATE-Base as 22.08 million parameters while Table 1 lists 22.80M; the discrepancy is in the source. Figures 3 and 4 show the measured $R^c(Z^{\ell+1/2})$ decreasing and the ISTA output sparsity improving over layers on training and validation data, and show that untrained networks do not do this, so the layerwise descent is learned rather than built in. The learned $U^\ell_{[K]}$ are approximately incoherent, increasingly so with depth. No language-modeling result is reported in this version.

## Relevance to this research

CRATE is the clearest precedent for deriving both halves of a transformer block, attention and MLP, from one stated objective, and the vault's GL(K) program has to be positioned against it. What CRATE derives is a forward pass that approximately descends a coding-rate objective: attention from a gradient step on $R^c$, the MLP from a sparse-coding proximal step, the skip connection from the step itself. Its approximations are explicit (Approximation 4; the orthogonal dictionary assumption; a heuristic LASSO link), and the implemented model relaxes the derived aggregation to a free matrix and keeps LayerNorm as an engineering choice. Tokens are point vectors; the Gaussians are a target distribution over tokens, not per-token beliefs; there is no propagated covariance, no divergence-based routing, no frame or gauge group, and training is ordinary backpropagation. The GL(K) construction of [[dennis-2026-glk-attention-v2-rework-2026-10-05]] differs on each of these counts: each token carries a Gaussian belief with covariance, routing is a Gaussian-KL softmax read as an exact source posterior, transport is group-valued and gauge-covariant ([[GL(K) gauge-equivariant attention]]), and [[dennis-2026-minimal-agent-model]] derives the receiving map and residual from Bayesian conditioning. In the other direction, CRATE has what the program lacks: a derived MLP replacement that has been trained at ImageNet scale, and measured layerwise evidence that the trained network descends the objective it was derived from. The program's MLP candidate, the mixture-responsibility [[Template routing]] (`gaussian_template`), has unit tests and no training result.

> [!note] Editorial: The ISTA block has a probabilistic reading the paper does not state. A nonnegative LASSO is MAP estimation of codes $Z$ under a Gaussian likelihood $Z^{\ell+1/2}\sim\mathcal N(DZ,\tfrac12 I)$ and an independent exponential prior with rate $\lambda$, so CRATE's MLP is one proximal step of MAP inference in a sparse linear-Gaussian generative model. That makes it a natural point of comparison for [[Template routing]], which is mixture-responsibility inference against Gaussian templates; the two differ in the prior (sparse factorial against one-of-$M$ mixture) and in whether uncertainty is carried. This is the vault's inference, not a claim of the paper.

> [!note] Editorial: The paper observes that rate reduction is invariant to arbitrary rotations of the representation and adds the sparsity term precisely to break that invariance toward the standard coordinate axes. The GL(K) program takes the opposite stance and keeps the frame freedom as a gauge symmetry, with transport between per-token frames. Whether a sparsity-like term would be gauge-compatible in that setting (it is not invariant under $\mathrm{GL}(K)$) is an open question the vault raises, not one the paper addresses.

Wiki pages: [[GL(K) gauge-equivariant attention]], [[Attention mechanisms — theory and positional structure]], [[Template routing]], [[Multi-head attention]].

## Cross-links

- Concepts: [[Multi-head attention]], [[Softmax]], [[Energy-Based Models]], [[Template routing]]
- Related sources: [[hoover-2023-energy-transformer]], [[yang-2022-transformers-optimization-perspective]], [[ramsauer2021hopfield]], [[movellan-2020-probabilistic-transformers]], [[vaswani-2017-attention]]

## Local full text

The arXiv v1 PDF is stored at `sources/pdfs/yu-2023-white-box-transformers-sparse-rate-reduction-arxiv-2306.01129.pdf` ([local PDF](../pdfs/yu-2023-white-box-transformers-sparse-rate-reduction-arxiv-2306.01129.pdf)), 33 pages, read by pypdf text extraction. Read: pages 1 to 10 in full (abstract, introduction, Sections 2 and 3, conclusion), the statement of Approximation 4 and the end of its derivation in Appendix A.2 (pp. 18 to 20), the opening and assumptions of Appendix A.3 (p. 20), and Appendix B.1 with the pseudocode (pp. 25 to 27). Not read: the references, Appendix A.1, the body of the A.2 and A.3 derivations, and Appendices B.2 to B.4. Source: [arXiv:2306.01129](https://arxiv.org/pdf/2306.01129). SHA-256: `2e7d840e50d57a1c2606e34f8c56fb5730349f8feaf19be8e66c283f76a970ca`.

## BibTeX

```bibtex
@inproceedings{Yu2023WhiteBox,
  author        = {Yu, Yaodong and Buchanan, Sam and Pai, Druv and Chu, Tianzhe and Wu, Ziyang and Tong, Shengbang and Haeffele, Benjamin D. and Ma, Yi},
  title         = {White-Box Transformers via Sparse Rate Reduction},
  booktitle     = {Advances in Neural Information Processing Systems},
  volume        = {36},
  year          = {2023},
  eprint        = {2306.01129},
  archivePrefix = {arXiv}
}
```
