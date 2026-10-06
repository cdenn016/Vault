---
type: paper
title: "Lattice gauge equivariant convolutional neural networks"
aliases:
  - "L-CNN"
  - "L-CNNs"
  - "LGE CNN"
  - "Favoni 2022"
  - "Favoni2022LatticeGauge"
authors:
  - Matteo Favoni
  - Andreas Ipp
  - David I. Müller
  - Daniel Schuh
year: 2022
arxiv: "2012.12901"
url: https://arxiv.org/abs/2012.12901
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/physics
  - field/cs-ml
created: 2026-10-06
---

# Lattice gauge equivariant convolutional neural networks

> [!info] Citation
> Favoni, M., Ipp, A., Müller, D. I., and Schuh, D. (2022). *Lattice gauge equivariant convolutional neural networks.* Physical Review Letters **128**, 032003. DOI: [10.1103/PhysRevLett.128.032003](https://doi.org/10.1103/PhysRevLett.128.032003). [arXiv:2012.12901](https://arxiv.org/abs/2012.12901) (v2, November 22, 2021; hep-lat, cs.LG).

## TL;DR

L-CNNs are convolutional networks whose layers preserve lattice gauge equivariance exactly. The input is a set of link variables $U_{x,\mu}$ of a lattice gauge theory (here $\mathrm{SU}(N_c)$) together with matrix-valued channels $W_{x,i}$ that transform locally, $W\to\Omega_xW\Omega_x^\dagger$. A gauge-covariant convolution parallel-transports $W$ from neighboring sites using the links, and a bilinear layer multiplies locally transforming matrices; alternating the two grows arbitrarily shaped Wilson loops from local operations. With a trace layer for gauge-invariant output and Polyakov loops for non-contractible topology, the authors argue the network can approximate any gauge-covariant function on the lattice.

## Problem and setting

Gauge-invariant observables on the lattice are traced Wilson loops (holonomies), and the number of loop shapes grows exponentially with path length. Earlier machine-learning work either picked loops by hand, used discrete Abelian groups, or fed plaquettes to flow-based samplers; a systematic construction for continuous non-Abelian groups was missing. Link variables transform as $T_\Omega U_{x,\mu}=\Omega_xU_{x,\mu}\Omega_{x+\mu}^\dagger$, and the plaquette $U_{x,\mu\nu}=U_{x,\mu}U_{x+\mu,\nu}U_{x+\nu,\mu}^\dagger U_{x,\nu}^\dagger$ is the elementary $1\times1$ Wilson loop of the Wilson action.

## Method

The layers (Eqs. 5 to 11) are: L-Conv, $W_{x,i}\to\sum_{j,\mu,k}\omega_{i,j,\mu,k}U_{x,k\cdot\mu}W_{x+k\cdot\mu,j}U_{x,k\cdot\mu}^\dagger$, with kernels connecting sites only along coordinate axes because the shortest lattice path is not unique; L-Bilin, $W_{x,i}\to\sum_{j,k}\alpha_{i,j,k}W_{x,j}W'_{x,k}$; L-Act, multiplication by a gauge-invariant scalar function such as $\mathrm{ReLU}(\mathrm{Re}\,\mathrm{Tr}\,W)$; L-Exp, the link update $U_{x,\mu}\to E_{x,\mu}U_{x,\mu}$ with $E_{x,\mu}=\exp(i\sum_i\beta_{\mu,i}[W_{x,i}]_{\mathrm{ah}})$, the exponential of the anti-Hermitian traceless part of $W$; and Trace, Plaquette and Polyakov layers. Figure 2 sketches an induction that L-Conv and L-Bilin generate every contractible Wilson loop.

## Key results

The letter's experiments are regression tasks for Wilson loops of different sizes and shapes in pure $\mathrm{SU}(2)$ gauge theory; the authors report that L-CNNs outperform conventional CNNs by far, with the gap growing with loop size, and that they generalize gauge-invariant quantities that ordinary CNNs fail to find. Numerical tables and the supplementary material (pages 7 to 20) were not read.

## Relevance to this research

L-CNNs are the clean contrast case for the lattice-gauge language of the GL(K) manuscripts: the gauge field is the input, the group is compact, the gauge symmetry is real and constrains every layer, and the network learns functions of holonomies. In [[dennis-2026-glk-attention-v2-rework-2026-10-05]] the frames $U_i$ are learned parameters, the covariance is artificial in the sense of [[francois-2019-artificial-gauge-symmetries]], the group is $\mathrm{GL}(K)$, and there is no loop observable in the evaluated model. The L-Conv update, parallel transport of locally adjoint-transforming data along links, is the same shape as the transported message $\sum_j\Theta_{ij}\mu_j$ of attention. [[nagai-2025-cask]] is the attention-based sibling for lattice QCD. Neither reads a transformer on tokens as a lattice gauge theory.

> [!note] Editorial: The nearest structural parallel to the exponential link $\Theta_{ij}=U_ie^{L_{ij}}U_j^{-1}$ is L-Exp, which also exponentiates a locally transforming Lie-algebra element and multiplies it onto a given group element. The parallel is formal: L-Exp acts on a given $\mathrm{SU}(N_c)$ gauge field, whereas the GL(K) generator is a learned map into $\mathrm{GL}^+(K)$.

Wiki pages: [[Lattice gauge theory]], [[Gauge equivariant CNN]], [[Gauge equivariance and geometric deep learning]], [[Holonomy]], [[Parallel transport]].

## Cross-links

- Concepts: [[Lattice gauge theory]], [[Gauge equivariant CNN]], [[Holonomy]], [[Parallel transport]]
- Related sources: [[nagai-2025-cask]], [[wilson-1974-confinement-quarks]], [[cohen-2019-gauge-cnn]], [[weiler-2021-coordinate-independent-cnns]], [[francois-2019-artificial-gauge-symmetries]]

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/Favoni2022LatticeGauge.pdf` ([local PDF](../pdfs/Favoni2022LatticeGauge.pdf)), 20 pages (6-page letter and 14-page supplement); the letter's first three pages were read in detail. Source: [arXiv:2012.12901](https://arxiv.org/pdf/2012.12901). SHA-256: `bea559aff5fb55e44e02f8e9776a4f71b83ebd2e1ddc965804db0e390f5e7843`.

## BibTeX

```bibtex
@article{Favoni2022LGECNN,
  author  = {Favoni, Matteo and Ipp, Andreas and M{\"u}ller, David I. and Schuh, Daniel},
  title   = {Lattice gauge equivariant convolutional neural networks},
  journal = {Physical Review Letters},
  volume  = {128},
  number  = {3},
  pages   = {032003},
  year    = {2022},
  doi     = {10.1103/PhysRevLett.128.032003},
  eprint  = {2012.12901},
  archivePrefix = {arXiv}
}
```
