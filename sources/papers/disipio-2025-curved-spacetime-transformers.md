---
type: paper
title: "The Curved Spacetime of Transformer Architectures"
aliases:
  - "Di Sipio 2025"
  - "Curved Spacetime of Transformers"
  - "DiSipio2025Curved"
authors:
  - Riccardo Di Sipio
  - Jairo Diaz-Rodriguez
  - Luis Serrano
year: 2025
arxiv: "2511.03060"
url: https://arxiv.org/abs/2511.03060
tags:
  - cluster/attention
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/physics
  - field/mathematics
created: 2026-10-06
---

# The Curved Spacetime of Transformer Architectures

> [!info] Citation
> Di Sipio, R., Diaz-Rodriguez, J., and Serrano, L. (2025). *The Curved Spacetime of Transformer Architectures.* [arXiv:2511.03060](https://arxiv.org/abs/2511.03060) (v1, November 4, 2025; cs.LG, cs.CL, math.DG). Code: [github.com/rdisipio/llm-curvature](https://github.com/rdisipio/llm-curvature).

## TL;DR

The paper maps a transformer onto general relativity by analogy and tests one prediction of the map. Queries and keys induce an effective metric $g_{ij}=x_i^\top W_Q^\top W_Kx_j$, the attention operator $\hat\alpha_{ij}W_V$ plays the role of a discrete connection that transports value vectors between tokens, layers are discrete time slices, and backpropagation is read as a least-action principle on parameter space. If the analogy holds, token embeddings should follow bent paths through the layers, and the authors measure that bending in pretrained encoders.

## Problem and setting

Prior work on curved representation spaces (hyperbolic embeddings, mixed-curvature transformers, a Riemannian parallel-transport framework for attention) examined curvature empirically, architecturally or mathematically, and the paper's stated gap is an explicit link to general relativity, with curvature arising dynamically from the training loss.

## Method

Section 3 defines the effective metric (the authors note it is generally non-symmetric and not positive definite, so it is not Riemannian in the strict sense) and reads the layer update $x_i^{(\ell+1)}=x_i^{(\ell)}+W_O^{(\ell)}\sum_j\hat\alpha_{ij}^{(\ell)}W_V^{(\ell)}x_j^{(\ell)}$ as a discrete velocity $\dot x_i=\sum_j\Gamma_{ij}^{(\ell)}x_j$ with connection coefficients $\Gamma_{ij}^{(\ell)}=W_O^{(\ell)}\hat\alpha_{ij}^{(\ell)}W_V^{(\ell)}$ (Eqs. 10 to 12). A midpoint approximation gives a layer-discretized geodesic equation (Eq. 14), and a semantic action $S_{\mathrm{LM}}=\sum_\ell(g_{ij}^{(\ell)}\dot x^i\dot x^j-\mathcal L_{\mathrm{train}})$ is introduced, with the caveat that activations are functions of the weights, so the action is over parameter-induced trajectories. Multi-head attention is read as an atlas of charts with $W_O$ as the transition map. Curvature is measured by proxies on the layerwise trajectory of one token: the turning angle $\theta_i$ between successive displacements $\Delta_i=x_i-x_{i-1}$ and the length-to-chord ratio $R=\sum_i\|\Delta_i\|/\|x_N-x_0\|$.

## Key results

On BERT (12 layers, 768 dimensions) a 69-word paragraph yields a curvature landscape over tokens and layers. Across 100 random sentences and twelve pretrained encoders (DistilBERT, DistilRoBERTa, MiniLM, BERT, RoBERTa, DeBERTa, ALBERT in small, base and large sizes), trajectories show more flat ($<80^\circ$) and sharp ($>100^\circ$) angles and larger $R$ than a null model that keeps each trajectory's step lengths and draws random directions (1000 samples per word); for example BERT-large gives $R=10.07$ against 4.72 under the null. A "lensing" experiment compares trajectories of an ambiguous token with and without a disambiguating context word and against a control edit, and reports, for BERT, larger divergence when the disambiguating word is present or removed than for the control edit on all four metrics it defines (final-layer separation, layerwise separation, curvature divergence, turning-angle gap). The authors state limitations: transformer inference uses a static geometry (the trained $W_Q$, $W_K$ do not respond to the sequence, unlike back-reaction in general relativity), and the observed curvature is inferred locally along probed paths.

## Relevance to this research

This is the closest published use of the words "attention as a connection" for transformers, so it bounds what the GL(K) program can call novel in that phrase. The content differs sharply from the group-valued reading. Here the connection coefficient is the mixing operator $W_O\hat\alpha_{ij}W_V$, not a group element; no gauge group, principal bundle, frame, or loop is defined, so there is no holonomy; and "curvature" is the turning angle of a depth trajectory, a statistic of one token's path, not the curvature of the connection. The paper also treats geometry as fixed at inference and names adaptive geometry as future work, which is the setting of the latent-link supplement of [[dennis-2026-glk-attention-v2-rework-2026-10-05]].

> [!note] Editorial: Equations 10 to 12 identify the per-head edge operator $W_O\hat\alpha_{ij}W_V$ with the affine-chart edge map $\beta_{ij}O_hT_h$ of the GL(K) manuscripts (the residual then supplies the identity term). The vault's inference is that the paper's discrete geodesic reading and the first-order chart $I+L$ of the routed-transport theorem describe the same update, one by physical analogy and one by an exact group-theoretic statement. The paper itself does not make this connection. Appendices A to F (the Christoffel-symbol derivations, the Einstein-Hilbert action, the statistical tests, and the model list) were not read.

Wiki pages: [[GL(K) gauge-equivariant attention]], [[Gauge equivariance and geometric deep learning]], [[Holonomy]], [[Multi-head attention]], [[Attention Mechanism]].

## Cross-links

- Concepts: [[Attention Mechanism]], [[Multi-head attention]], [[Parallel transport]], [[Holonomy]]
- Related sources: [[vaswani-2017-attention]], [[elhage-2021-transformer-circuits-framework]], [[sengupta2017gauge]], [[wang-2023-riemannian-self-attention-spd]]

## Local full text

The arXiv v1 PDF is stored at `sources/pdfs/DiSipio2025Curved.pdf` ([local PDF](../pdfs/DiSipio2025Curved.pdf)), 26 pages; the main text (pages 1 to 14) was read, the appendices were not. Source: [arXiv:2511.03060](https://arxiv.org/pdf/2511.03060). SHA-256: `9b76270c2463906673841ade36fe26bf4758b0efefae71c887ef713de6122b04`.

## BibTeX

```bibtex
@misc{DiSipio2025Curved,
  author        = {Di Sipio, Riccardo and Diaz-Rodriguez, Jairo and Serrano, Luis},
  title         = {The Curved Spacetime of Transformer Architectures},
  year          = {2025},
  eprint        = {2511.03060},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG}
}
```
