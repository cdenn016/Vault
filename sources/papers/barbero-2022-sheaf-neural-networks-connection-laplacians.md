---
type: paper
title: "Sheaf Neural Networks with Connection Laplacians"
aliases:
  - "Conn-NSD"
  - "Barbero 2022 connection Laplacians"
  - "Barbero2022Connection"
authors:
  - Federico Barbero
  - Cristian Bodnar
  - Haitz Sáez de Ocáriz Borde
  - Michael Bronstein
  - Petar Veličković
  - Pietro Liò
year: 2022
arxiv: "2206.08702"
url: https://arxiv.org/abs/2206.08702
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-10-06
---

# Sheaf Neural Networks with Connection Laplacians

> [!info] Citation
> Barbero, F., Bodnar, C., Sáez de Ocáriz Borde, H., Bronstein, M., Veličković, P., and Liò, P. (2022). *Sheaf Neural Networks with Connection Laplacians.* Presented at the ICML 2022 Workshop on Topology, Algebra, and Geometry in Machine Learning. [arXiv:2206.08702](https://arxiv.org/abs/2206.08702) (v1, June 17, 2022; cs.LG, math.AT, math.DG).

## TL;DR

A sheaf neural network operates on a cellular sheaf of a graph: a vector space (stalk) at every node and edge and a linear restriction map for every incident node-edge pair. [[bodnar-2022-neural-sheaf-diffusion]] learns the restriction maps by gradient descent from node features; this workshop paper instead precomputes them. At each node a local PCA of the one-hop neighborhood gives a $d$-dimensional orthonormal basis $O_i$, and the transport along an edge is the orthogonal alignment $O_{ij}=UV^\top$ obtained from the SVD $O_i^\top O_j=U\Sigma V^\top$. With orthogonal restriction maps the sheaf is a discrete $O(d)$-bundle, and its Laplacian is the connection Laplacian of [[singer-2012-vector-diffusion-maps]]. The resulting model, Conn-NSD, is competitive with learned-sheaf diffusion on most of nine node-classification benchmarks and cheaper per epoch.

## Problem and setting

Sheaf diffusion mitigates over-smoothing and heterophily in graph neural networks, but the sheaf has to come from somewhere. Earlier work either built it by hand from domain knowledge ([[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]]) or learned a parametric map $\mathcal F_{v\trianglelefteq e}=\Phi(x_v,x_u)$ end to end, which the authors say can overfit and costs computation. The paper takes the manifold assumption: node features are samples of a $d$-dimensional manifold in $\mathbb R^p$, tangent spaces at neighboring points are aligned by orthogonal maps, and the alignment approximates parallel transport. The construction is the one of Singer and Wu, adapted from point clouds to graphs.

## Method

Definitions 2.1 to 2.5 give the cellular sheaf, the coboundary $\delta(x)_e=\mathcal F_{v\trianglelefteq e}x_v-\mathcal F_{u\trianglelefteq e}x_u$, the sheaf Laplacian $L_{\mathcal F}=\delta^\top\delta$ and its normalization; a trivial sheaf with one-dimensional stalks and identity maps recovers the graph Laplacian. Diffusion is $\dot X=-\Delta_{\mathcal F}X$, and the trained model of Bodnar et al. is $\dot X=-\sigma(\Delta_{\mathcal F(t)}(I_n\otimes W_1)XW_2)$. Algorithm 1 replaces $\mathcal F(t)$ by a fixed sheaf. For each node, the centered one-hop neighbor matrix $\hat X_i$ is decomposed by SVD and the first $d$ left singular vectors form $O_i$ (the weighting matrix of Singer and Wu is taken as the identity; nodes with fewer than $d$ neighbors are padded with the Euclidean-nearest nodes, and $d$ is a hyperparameter). The transport for each edge is the polar factor of $O_i^\top O_j$. The sheaf is computed once before training.

## Key results

Nine datasets ordered by homophily (Texas, Wisconsin, Film, Squirrel, Chameleon, Cornell, Citeseer, Pubmed, Cora), ten fixed splits, with RandEdge-NSD (a Haar-random orthogonal matrix per edge) and RandNode-NSD (a random matrix per node, transports derived from them) as controls. Conn-NSD has a higher mean accuracy than both random controls on all nine datasets, but the gap is large relative to the reported standard deviations only on Squirrel and Chameleon and against RandEdge on Cora and Pubmed; on Texas, Wisconsin, Film and Cornell it is inside one standard deviation. It reports 86.16 on Texas and 37.91 on Film against 85.67 to 85.95 and 37.79 to 37.81 for Diag-, O(d)- and Gen-NSD, differences inside the stated standard deviations, and is clearly behind on Squirrel (45.19 against 53.17 to 56.34) and Chameleon (65.21 against 67.93 to 68.68). Mean seconds per epoch on a TITAN X are lower than for O(d)-NSD on every dataset (0.310 against 0.572 on Squirrel, the stated 45.8 percent speedup). The authors read the result as the sheaf acting as a regularizer, most useful on small graphs.

## Relevance to this research

This is the closest machine-learning precedent for orthogonal group-valued edge transports on a graph read as a discrete bundle with a connection Laplacian, and it fixes what the GL(K) program cannot claim as new about that half. The differences are specific. The transports here lie in $O(d)$ with $d$ a small stalk dimension, are computed from data by local PCA, and drive a diffusion equation; in [[dennis-2026-glk-attention-v2-rework-2026-10-05]] the frames are learned per token and per position in $\mathrm{GL}^+(K)$, the links are $\Theta_{ij}=U_ie^{L_{ij}}U_j^{-1}$ with a shared Lie-algebra generator, the fibers are Gaussian statistical manifolds, and routing is a divergence-based softmax, not a Laplacian. Nothing in the paper is about attention, probabilistic fibers, or non-compact groups.

> [!note] Editorial: The alignment $O_{ij}=UV^\top$ is the polar factor of $O_i^\top O_j$, which is not the product of the polar factors of the node frames. If that reading is right, the transports are not exactly flat in general, whereas the flat link $\Omega_{ij}=U_iU_j^{-1}$ of the GL(K) manuscripts is flat by construction. The paper does not discuss holonomy; this comparison is the vault's inference from Section 3.1.

Wiki pages: [[Graph synchronization and connection Laplacians]], [[Gauge equivariance and geometric deep learning]], [[GL(K) gauge-equivariant attention]], [[Holonomy]], [[Parallel transport]].

## Cross-links

- Concepts: [[Graph synchronization and connection Laplacians]], [[Parallel transport]], [[Holonomy]]
- Related sources: [[bodnar-2022-neural-sheaf-diffusion]], [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]], [[singer-2012-vector-diffusion-maps]], [[barbero-2022-sheaf-attention-networks]]

## Local full text

The arXiv v1 PDF is stored at `sources/pdfs/Barbero2022Connection.pdf` ([local PDF](../pdfs/Barbero2022Connection.pdf)), 8 pages, read in full. Source: [arXiv:2206.08702](https://arxiv.org/pdf/2206.08702). SHA-256: `52203cabcdf0b73dbe9e7693615972e538dc347f349486dda1d8d14a13adec92`.

## BibTeX

```bibtex
@misc{Barbero2022SheafConnection,
  author        = {Barbero, Federico and Bodnar, Cristian and S{\'a}ez de Oc{\'a}riz Borde, Haitz and Bronstein, Michael and Veli{\v{c}}kovi{\'c}, Petar and Li{\`o}, Pietro},
  title         = {Sheaf Neural Networks with Connection {L}aplacians},
  year          = {2022},
  eprint        = {2206.08702},
  archivePrefix = {arXiv},
  note          = {ICML 2022 Workshop on Topology, Algebra, and Geometry in Machine Learning}
}
```
