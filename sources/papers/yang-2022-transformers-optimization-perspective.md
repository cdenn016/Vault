---
type: paper
title: "Transformers from an Optimization Perspective"
aliases:
  - "Yang Huang Wipf 2022"
  - "Transformers from an optimization perspective (Yang 2022)"
  - "Yang2022Transformers"
authors:
  - Yongyi Yang
  - Zengfeng Huang
  - David Wipf
year: 2022
arxiv: "2205.13891"
url: https://arxiv.org/abs/2205.13891
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-10-06
---

# Transformers from an Optimization Perspective

> [!info] Citation
> Yang, Y., Huang, Z., and Wipf, D. (2022). *Transformers from an Optimization Perspective.* Advances in Neural Information Processing Systems 35 (NeurIPS 2022). [arXiv:2205.13891](https://arxiv.org/abs/2205.13891) (v1, May 27, 2022; v2, February 27, 2023; cs.LG). The arXiv comment and the v2 PDF footer state NeurIPS 2022. Code: [github.com/FFTYYY/Transformers-From-Optimization](https://github.com/FFTYYY/Transformers-From-Optimization).

## TL;DR

The paper asks whether there is an energy whose descent steps reproduce a transformer forward pass. It constructs a pairwise energy whose majorization-minimization step is softmax self-attention, proves that alternating separate gradient steps on two convex terms (attention and feed-forward) descends their sum outside a bounded region, and adds ReLU as a proximal step with a similar guarantee. The resulting layer, $\mathrm{ReLU}[\operatorname{softmax}_\beta(YW_a^sY^\top)\,Y\,W_f^s]$, matches a simplified transformer layer except that its weights are symmetric and shared across layers. The only experiment shows that this energy decreases layer by layer in random and trained 12-layer models on IMDB and SST-2; no task accuracy is reported in the main text.

## Problem and setting

Unfolded optimization reads a network as $Y^*(W,X)=\arg\min_YE(Y;W,X)$ with parameters trained through the unrolled iterations by a meta-loss, a bilevel problem (eqs. 1 and 2). The authors note that prior energies gave MLPs only with PSD effective weights, gave cross-attention rather than self-attention ([[ramsauer2021hopfield]]), or gave graph attention without the softmax. They target the simplified layer $Y^{(t+1)}=\mathrm{ReLU}[\operatorname{softmax}(Y^{(t)}W_aY^{(t)\top})Y^{(t)}W_f]$ (eq. 8, no LayerNorm or residual) and name four obstacles: token interactions, heterogeneous layer types, nonlinear activations and asymmetric weights. They address the first three, partly, and defer the fourth.

## Method

Self-attention (Section 3). For $E_1(Y)=\sum_{i,j}\rho(\tfrac12\|y_i-y_j\|^2)+R(Y)$ with concave nondecreasing $\rho$ and convex $R$, Theorem 3.1 takes $\rho(z)=-e^{-z}$, $R=\tfrac12\|Y\|_F^2$ and $\beta_j=\exp(-\tfrac12\|y_j\|^2)$ and shows that
$$y_i^{(t+1)}=\frac{\sum_j\beta_j\exp(y_i^{(t)\top}y_j^{(t)})\,y_j^{(t)}}{\sum_j\beta_j\exp(y_i^{(t)\top}y_j^{(t)})}$$
does not increase $E_1$, with equality only at stationary points; the step is a majorization-minimization update, a gradient step on a convex upper bound. If token norms are constant (enforceable by LayerNorm) the reweighted softmax is the ordinary one, and the reparametrization $Y=ZW_a$ gives $\operatorname{softmax}_\beta(ZW_a^sZ^\top)Z$ with symmetric $W_a^s=W_aW_a^\top$. Other choices of $\rho$ give other normalizations; $\rho(z)=\log(z+2)$ is worked as an example in the conclusion. Other step sizes produce residual connections, and a graph mask can restrict the sum.

Heterogeneous layers (Section 4). Alternating inexact minimization (AIM) takes $u=y-\alpha_1\nabla f(y)$, then $y^+=u-\alpha_2\nabla g(u)$, for Lipschitz-smooth strongly convex $f,g$. Theorem 4.1 shows $h=f+g$ decreases when $\alpha_1\le\alpha_2\le L_h^{-1}$ and a relative-noise ratio is bounded by an explicit constant; Lemma 4.3 identifies the guaranteed region as the outside of an Apollonian ball around the minimizer, so iterates descend until they enter a neighborhood of the optimum and then may oscillate. With $E_2(Y)=\tfrac12\operatorname{Tr}(YW_fY^\top)+\tfrac12\|Y\|_F^2$ the feed-forward step is $Y^+=UW_f^s$ with $W_f^s=(1-\alpha_2)I-\alpha_2(W_f+W_f^\top)/2$, and Corollary 4.5 gives descent of the convex upper bound outside a finite ball.

Nonlinearity (Section 5). ReLU is the proximal operator of the indicator of the nonnegative orthant, so appending it gives an inexact proximal-gradient step; Theorem 5.1 gives descent of $E_1+E_2+\varphi$ in the intersection of the Section 4 region with a further region $T(\kappa)$ that fills most of space for small steps. The final layer descends the total energy except on a region of finite measure, and differs from eq. 8 only by its symmetric weights. Appendix F argues that LayerNorm's translation and rescaling are gradient steps of added energy terms, that asymmetric weights are not covered (symmetric weights are cited as universal given enough width), and that unfolding forces the same weights at every layer, which finite-depth constructions from other work can relax.

## Key results

The results are theorems about descent under stated conditions. Section 6 checks the energy empirically on IMDB and SST-2 with GloVe embeddings: the energy averaged over 200 test samples decreases monotonically across 12 layers both at random initialization and after 2000 SGD steps (Figures 5 and 6), where for the trained model $\|Y\|_F^2$ in $E_1$ is replaced by $\|Y-X\|_F^2$, which the theory also covers and which yields an input residual. The authors note that the conditions of Lemma 4.3 and Theorem 5.1 are difficult to verify formally on real data. No classification accuracy, perplexity or comparison with a standard transformer appears in the main text.

## Relevance to this research

Of the three objective-to-transformer papers in the vault, this is the most explicitly mathematical about what "derived" means: an energy, a descent theorem for each part, and a stated list of what is not covered (asymmetric weights, layer-dependent weights). It derives softmax self-attention, a single linear feed-forward map, ReLU and, in the appendix, LayerNorm and residual connections, but the feed-forward part is one symmetric linear layer plus a proximal ReLU, not the two-layer MLP of a real transformer, and the weights are constrained to be symmetric and tied across depth. Training is backpropagation through the unrolled layers, and the evidence is energy descent only. Against the GL(K) program of [[dennis-2026-glk-attention-v2-rework-2026-10-05]], it shares the aim of a forward pass with a variational characterization but has point-vector tokens, no covariance, no probabilistic model behind the energy and no frame or gauge structure; the program's routing is an exact posterior and its transport is group-valued ([[GL(K) gauge-equivariant attention]]). The program, in turn, has no descent theorem across layers for its full block and no derivation of the MLP that has been trained; the AIM analysis is the kind of argument a combined attention-plus-[[Template routing]] free energy would need.

> [!note] Editorial: Theorem 3.1's reweighted softmax is the isotropic Gaussian-KL routing of the program. Since $y_i^\top y_j-\tfrac12\|y_j\|^2=-\tfrac12\|y_i-y_j\|^2+\tfrac12\|y_i\|^2$ and the last term cancels in the normalization, the weights $\beta_j\exp(y_i^\top y_j)/\sum_k\beta_k\exp(y_i^\top y_k)$ equal $\operatorname{softmax}_j(-\tfrac12\|y_i-y_j\|^2)$, which is $\operatorname{softmax}_j(-D_{\mathrm{KL}}(\mathcal N(y_i,I)\|\mathcal N(y_j,I)))$, the L2 attention of [[kim-2021-lipschitz-self-attention]] and the shared-frame isotropic limit recorded on [[GL(K) gauge-equivariant attention]] (identity-bilinear score plus a key-norm bias). Yang et al. reach it as an MM step on a pairwise energy; the program reaches it as a source posterior. The algebra is elementary; the identification is the vault's, and the paper does not mention divergences.

> [!note] Editorial: The symmetric-weight restriction has a counterpart in the program. A symmetric $W_a^s=W_aW_a^\top$ is the case in which query and key maps coincide, while the program's comparison link $U_iS_Q^{-1}S_KU_j^{-1}$ allows distinct query and key maps and still has a divergence reading when both are invertible. Whether that removes Yang et al.'s Challenge 4 for the attention score is the vault's question; the paper does not consider it.

Wiki pages: [[GL(K) gauge-equivariant attention]], [[Attention mechanisms — theory and positional structure]], [[Energy-Based Models]].

## Cross-links

- Concepts: [[Softmax]], [[Multi-head attention]], [[Energy-Based Models]], [[Activation Functions]]
- Related sources: [[ramsauer2021hopfield]], [[hoover-2023-energy-transformer]], [[yu-2023-white-box-transformers-sparse-rate-reduction]], [[kim-2021-lipschitz-self-attention]], [[vaswani-2017-attention]]

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/yang-2022-transformers-optimization-perspective-arxiv-2205.13891.pdf` ([local PDF](../pdfs/yang-2022-transformers-optimization-perspective-arxiv-2205.13891.pdf)), 21 pages, read by pypdf text extraction. Read: pages 1 to 11 (abstract through conclusion and the start of the references), the discussion in Appendix B.3, and Appendices E and F (pp. 20 to 21). Not read: the rest of the references and the proofs in Appendices A to D (pp. 14 to 20). Source: [arXiv:2205.13891](https://arxiv.org/pdf/2205.13891). SHA-256: `6ec12561f093b7bcbca0901b0d9b04fd382e114644fc526138d04017a5459ef1`.

## BibTeX

```bibtex
@inproceedings{Yang2022Transformers,
  author        = {Yang, Yongyi and Huang, Zengfeng and Wipf, David},
  title         = {Transformers from an Optimization Perspective},
  booktitle     = {Advances in Neural Information Processing Systems},
  volume        = {35},
  year          = {2022},
  eprint        = {2205.13891},
  archivePrefix = {arXiv}
}
```
