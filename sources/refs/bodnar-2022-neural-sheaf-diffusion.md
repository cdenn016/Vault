---
type: reference
title: "Neural Sheaf Diffusion: A Topological Perspective on Heterophily and Oversmoothing in GNNs"
aliases:
  - "Bodnar et al. 2022 neural sheaf diffusion"
  - "Bodnar2022NeuralSheaf"
authors:
  - Cristian Bodnar
  - Francesco Di Giovanni
  - Benjamin Paul Chamberlain
  - Pietro Liò
  - Michael M. Bronstein
year: 2022
arxiv: "2202.04579"
url: https://arxiv.org/abs/2202.04579
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-09-23
updated: 2026-09-23
---

# Neural Sheaf Diffusion: A Topological Perspective on Heterophily and Oversmoothing in GNNs

> [!info] Citation
> Cristian Bodnar, Francesco Di Giovanni, Benjamin Paul Chamberlain, Pietro Liò, Michael M. Bronstein (2022). "Neural Sheaf Diffusion: A Topological Perspective on Heterophily and Oversmoothing in GNNs." *Advances in Neural Information Processing Systems* **35** (NeurIPS 2022). Preprint: [arXiv:2202.04579](https://arxiv.org/abs/2202.04579) (v4 read).

## TL;DR

A cellular sheaf on a graph assigns vector spaces (stalks) to nodes and edges and linear restriction maps from node stalks into edge stalks. Ordinary graph neural networks correspond to the trivial sheaf. Diffusion with the sheaf Laplacian of a richer sheaf avoids oversmoothing and handles heterophilic graphs, and the restriction maps can be learned from node features (Neural Sheaf Diffusion).

## What it establishes

Definition 1 introduces a cellular sheaf $(G,\mathcal F)$: stalks $\mathcal F(v)$, $\mathcal F(e)$ and restriction maps $\mathcal F_{v\trianglelefteq e}:\mathcal F(v)\to\mathcal F(e)$. Following Hansen and Ghrist, the node stalk is read as a private opinion and the edge stalk as a public discourse space, and global sections are the configurations on which all neighbors agree in every edge stalk. Definition 2 gives the sheaf Laplacian $L_{\mathcal F}(x)_v=\sum_{v,u\trianglelefteq e}\mathcal F_{v\trianglelefteq e}^\top(\mathcal F_{v\trianglelefteq e}x_v-\mathcal F_{u\trianglelefteq e}x_u)$, whose kernel is isomorphic to the space of global sections. Sheaves with orthogonal restriction maps are discrete $O(d)$ bundles, and their Laplacian is the connection Laplacian. Section 3 relates the spectral gap to the path dependence of the induced transport (Propositions 3–5, a Cheeger-type inequality) and characterizes the harmonic space (Lemma 6), then ranks sheaf classes (trivial, diagonal invertible, orthogonal, general) by their power to linearly separate classes in the diffusion limit. The authors note that the results extend to $GL(d)$ restriction maps when the maps are bounded below in norm. Section 4 analyzes the discrete, parametric, non-linear diffusion, and Section 5 learns each restriction map as a function $\Phi(x_v,x_u)$ of the incident node features (diagonal, orthogonal, and general variants), with competitive results on heterophilic benchmarks.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript uses this paper, with [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]], to position its matrix links. The comparison cospan $E_i\to H^{\mathrm{cmp}}\leftarrow E_j$ is a pair of restriction maps into an edge stalk, so cellular sheaves are a closer counterpart of the construction than lattice gauge theory. See [[Lattice gauge theory]], [[Graph synchronization and connection Laplacians]], [[GL(K) gauge-equivariant attention]], and [[dennis-2026-glk-matrix-links-2026-09-20]].

## Local full text

The arXiv v4 PDF is stored at `sources/pdfs/Bodnar2022NeuralSheaf.pdf` ([local PDF](../pdfs/Bodnar2022NeuralSheaf.pdf)). Source: [arXiv:2202.04579](https://arxiv.org/pdf/2202.04579). SHA-256: `6358eb67686856112ae798d99958b5f84344be7c8d9f28f7073bd9efd81d5044`.

## BibTeX

```bibtex
@inproceedings{Bodnar2022NeuralSheaf,
  author = {Bodnar, Cristian and Di Giovanni, Francesco and Chamberlain, Benjamin Paul and Li{\`o}, Pietro and Bronstein, Michael M.},
  title = {Neural Sheaf Diffusion: A Topological Perspective on Heterophily and Oversmoothing in {GNN}s},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {35},
  year = {2022},
  eprint = {2202.04579},
  archivePrefix = {arXiv}
}
```
