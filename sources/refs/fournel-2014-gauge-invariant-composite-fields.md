---
type: reference
title: "Gauge Invariant Composite Fields out of Connections, with Examples"
aliases:
  - "Fournel et al. 2014 dressing field method"
  - "Gauge invariant composite fields out of connections"
  - "Fournel2014Dressing"
authors:
  - Cédric Fournel
  - Jordan François
  - Serge Lazzarini
  - Thierry Masson
year: 2014
arxiv: "1212.6702"
doi: 10.1142/S0219887814500169
url: https://arxiv.org/abs/1212.6702
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/physics
  - field/mathematics
created: 2026-09-23
updated: 2026-09-23
---

# Gauge Invariant Composite Fields out of Connections, with Examples

> [!info] Citation
> Cédric Fournel, Jordan François, Serge Lazzarini, Thierry Masson (2014). "Gauge Invariant Composite Fields out of Connections, with Examples." *International Journal of Geometric Methods in Modern Physics* **11**, 1450016. DOI: [10.1142/S0219887814500169](https://doi.org/10.1142/S0219887814500169). Preprint: [arXiv:1212.6702](https://arxiv.org/abs/1212.6702) (v2 read).

## TL;DR

This is the founding paper of the dressing field method. When a gauge theory contains a group-valued field with a prescribed gauge transformation (a "dressing field"), one can form composite fields out of the connection and the matter fields that are gauge invariant. The procedure reduces the gauge symmetry by a change of field variables, which is distinct from gauge fixing, spontaneous symmetry breaking, and bundle reduction.

## What it establishes

The Main Lemma of Section 2 reads as follows. Let $\alpha$ be a connection of a gauge theory with structure group $H$, transforming as $\alpha^\gamma=\gamma^{-1}\alpha\gamma+\gamma^{-1}d\gamma$. If a field $u$ with values in a group $G\supseteq H$ transforms as $u^\gamma=\gamma^{-1}u$, then the composite field $\hat\alpha=u^{-1}\alpha u+u^{-1}du$, its curvature $u^{-1}\Omega u$, the dressed matter field $\hat\varphi=\rho(u^{-1})\varphi$, and its covariant derivative are $H$-gauge invariant whenever they are mathematically defined. The authors argue that this relation is not a gauge transformation: the dressing field need not belong to the gauge group, and the composite fields need not live in the original field spaces. Proposition 2.1 shows that a global dressing field valued in a subgroup $K$, acting geometrically, exists if and only if the principal bundle is trivial in the $K$ direction ($P\simeq P/K\times K$ as $K$-spaces).

Three examples follow. Section 3 extracts a dressing field from the scalar doublet of the electroweak sector, and the composite fields $W^\pm$, $Z^0$ and $A$ are exactly the Standard Model boson fields after symmetry breaking, which reinterprets the symmetry-breaking mechanism; for $SU(N)$ with $N>2$ the lemma gives only a reduction to $SU(N-1)$. Section 4 treats general relativity as a Cartan gauge theory: the dressing field extracted from the translational part of the Cartan connection plays the role of a vielbein, and the composite fields behave as Christoffel symbols. Section 5 starts from a gauge theory on Atiyah Lie algebroids and obtains composite fields describing massive vector fields.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript (`manuscripts/Attention/GL(K)_attention_v2.tex`) cites this paper as the origin of the dressing field method. In that reading, the reference moments $\xi_i=U_i^{-1}\mu_i$ (and $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$) are dressed gauge-invariant composite fields, and the learned frame $U_i$ plays the role of the dressing field. [[francois-2019-artificial-gauge-symmetries]] supplies the criterion that classifies the resulting covariance as artificial. See [[Dressing field method]] and [[GL(K) gauge-equivariant attention]].

> [!note] Editorial: The match to the Main Lemma is exact up to convention. Under the manuscript's passive change $\mu_i\mapsto g_i\mu_i$, $U_i\mapsto g_iU_i$, set $\gamma=g_i^{-1}$. Then $\mu_i^\gamma=\rho(\gamma^{-1})\mu_i$ and $U_i^\gamma=\gamma^{-1}U_i$, so $U_i$ is a dressing field and $\hat\varphi=\rho(U_i^{-1})\mu_i=\xi_i$.

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/Fournel2014Dressing.pdf` ([local PDF](../pdfs/Fournel2014Dressing.pdf)). Source: [arXiv:1212.6702](https://arxiv.org/pdf/1212.6702). SHA-256: `bda146f1ac84b5bcbca62b852f4efe5f621e881c5f3644e415befc75ef9b6cb8`.

## BibTeX

```bibtex
@article{Fournel2014Dressing,
  author = {Fournel, C{\'e}dric and Fran{\c{c}}ois, Jordan and Lazzarini, Serge and Masson, Thierry},
  title = {Gauge Invariant Composite Fields out of Connections, with Examples},
  journal = {International Journal of Geometric Methods in Modern Physics},
  volume = {11},
  pages = {1450016},
  year = {2014},
  doi = {10.1142/S0219887814500169},
  eprint = {1212.6702},
  archivePrefix = {arXiv}
}
```
