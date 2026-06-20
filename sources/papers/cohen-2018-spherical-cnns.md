---
type: paper
title: Spherical CNNs
aliases:
  - "Cohen et al. 2018 — Spherical CNNs"
authors:
  - Taco S. Cohen
  - Mario Geiger
  - Jonas Köhler
  - Max Welling
year: 2018
arxiv: "1801.10130"
url: https://arxiv.org/abs/1801.10130
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-06-20
updated: 2026-06-20
---

# Spherical CNNs

> [!info] Citation
> Taco S. Cohen, Mario Geiger, Jonas Köhler, and Max Welling (2018). *Spherical CNNs*. ICLR 2018. arXiv:[1801.10130](https://arxiv.org/abs/1801.10130).

## TL;DR

Cohen, Geiger, Köhler and Welling construct a convolutional network for signals on the sphere $S^2$ that is **equivariant to the full rotation group $SO(3)$**, not merely to in-plane translations. Their central move is to define spherical cross-correlation as an integral over rotations rather than translations, so a filter is matched against every *rotated* copy of the input; the output is therefore naturally a function on the group $SO(3)$. This correlation obeys a **generalized (non-commutative) Fourier theorem** — it diagonalizes in the basis of $SO(3)$ [[Irreducible representation]]s (Wigner D-matrices) — which lets the layer be computed efficiently with a generalized FFT. The paper is the spherical, harmonic-analytic member of the geometric-deep-learning family: it shows how to make a network's representations transform predictably under a *continuous, non-commutative* symmetry group by working in the irrep (Fourier) domain.

## Problem & setting

Planar CNNs are equivariant to translations, but many signals live on the sphere — omnidirectional camera images, global climate and weather fields, molecular electron densities sampled on a surrounding sphere — where the natural symmetry is the rotation group $SO(3)$, not the plane's translation group. Naively projecting a spherical signal onto a flat grid and running an ordinary CNN destroys this symmetry: the unavoidable map distortion means a rotation of the underlying signal is *not* a translation of the projected image, so a planar CNN must relearn the same pattern at every orientation, wasting capacity and sample budget. The paper asks for a principled building block whose feature maps transform consistently when the input sphere is rotated, so that rotational symmetry is guaranteed by construction. Formally, signals are functions $f : S^2 \to \mathbb{R}^K$ and filters are likewise spherical functions; the first layer's output lives on $SO(3)$ because a point on the sphere fixes only two of the three rotational degrees of freedom, leaving a residual circle of orientations.

## Method

The construction replaces planar cross-correlation by its rotational analogue. For a spherical signal $f$ and filter $\psi$, the **spherical correlation** evaluates, for every rotation $R \in SO(3)$, the inner product of $f$ with the rotated filter $L_R \psi$:
$$
(\psi \star f)(R) = \int_{S^2} \psi(R^{-1} x)\, f(x)\, dx ,
$$
so the result is a function on $SO(3)$. Deeper layers then correlate functions on $SO(3)$ with filters on $SO(3)$ by the same group-integral recipe. This operator is **equivariant** by construction: rotating the input, $f \mapsto L_Q f$, rotates the output, $(\psi \star L_Q f)(R) = (L_Q(\psi \star f))(R)$, so a transformation of the input induces a known transformation of the features rather than scrambling them — the defining property of [[Group equivariance]].

The computational engine is harmonic analysis on the sphere and the group. By the **generalized Fourier theorem**, correlation becomes pointwise multiplication in the spectral domain: expand $f$ and $\psi$ in spherical harmonics / Wigner D-functions (the matrix entries of the $SO(3)$ [[Irreducible representation]]s), multiply the resulting blockwise coefficients, and invert. The forward and inverse transforms are computed with a generalized non-commutative FFT, making the equivariant layer practical. Pointwise nonlinearities are applied in the spatial domain and are equivariant because the group acts by rotating sample points; the network alternates between the spatial domain (for nonlinearities) and the spectral domain (for correlation).

## Key results

- **Exact $SO(3)$ equivariance, empirically verified.** The error between rotating-then-correlating and correlating-then-rotating stays at the level of numerical/discretization noise across network depth, confirming the construction is equivariant rather than merely approximately so.
- **Rotated-MNIST-on-the-sphere and shape recognition.** A spherical CNN substantially outperforms planar baselines when test orientations are not seen at training time, demonstrating that built-in rotational equivariance buys generalization across poses without orientation augmentation.
- **3D shape (SHREC'17) and molecular regression (QM7).** The model is competitive with task-specific architectures while being generic, showing the spherical/irrep approach transfers to real scientific signals (atomization-energy regression from a spherical encoding of molecular geometry).
- **Efficiency.** Diagonalizing correlation in the irrep basis and using a generalized FFT keeps the cost tractable, in contrast to evaluating the rotational integral directly.

## Relevance to this research

This paper is a geometric-deep-learning **sibling** of the VFE transformer's gauge-equivariant attention, valued for the *machinery by which a continuous symmetry group constrains representations through its irreps* rather than for a literal architecture import (see [[VFE Transformer Program]]). The connections are specific:

- **Working in the irrep / Fourier domain.** Spherical CNNs realize equivariance by diagonalizing the group action into [[Irreducible representation]] blocks and operating blockwise — exactly the algebraic discipline behind the program's irrep-tower head mixers and its isotypic / Clebsch-Gordan coupling, where quantities are organized by how they transform under the gauge group and combined block-by-block. This paper is the cleanest demonstration that an irrep decomposition turns an awkward group-integral into cheap blockwise multiplication.
- **Equivariance to a non-commutative, continuous group.** Where the earlier G-CNN ([[cohen-2016-gcnn]]) handles *discrete* image symmetries, this paper handles the *continuous, non-commutative* $SO(3)$ — a closer rehearsal for the program's continuous block general-linear gauge group, in the sense that one must reason about [[Group equivariance]] for a Lie group rather than a finite one.
- **A point of contrast that sharpens the program's claim.** Spherical CNNs achieve *global* $SO(3)$ equivariance via a global harmonic transform; the gauge-equivariant lineage ([[cohen-2019-gauge-cnn]]) replaces this with *local* frame changes and [[parallel transport]]. The VFE transformer sits on the local-gauge side, so this paper marks the global-symmetry baseline against which the per-token, per-block local-gauge design is the generalization.

> [!note] Editorial: The mapping is by analogy, not identity. Spherical CNNs are equivariant to the compact group $SO(3)$ and exploit its unitary, finite-dimensional irreps and a clean Peter–Weyl/Fourier theory; the program's $GL(k)$ gauge group is non-compact, so its finite-dimensional representations are not unitary and there is no directly analogous $L^2$ harmonic transform. What carries over is the *principle* — decompose into irreps and act blockwise to keep equivariance manifest — not the spherical-harmonic toolchain itself. The paper also treats deterministic feature fields, whereas the transformer transports full Gaussian beliefs (mu, Sigma); that probabilistic/SPD extension is supplied elsewhere in the program.

## Cross-links

- Concepts: [[Group equivariance]], [[Irreducible representation]], [[Clebsch-Gordan coefficients]], [[Parallel transport]]
- Theme: [[Gauge equivariance and geometric deep learning]]
- Related sources: [[cohen-2016-gcnn]], [[cohen-2019-gauge-cnn]], [[kondor-2018-compact-group-conv]], [[bronstein-2021-geometric-deep-learning]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{cohen2018spherical,
  title     = {Spherical {CNN}s},
  author    = {Cohen, Taco S. and Geiger, Mario and K{\"o}hler, Jonas and Welling, Max},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2018},
  eprint    = {1801.10130},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1801.10130}
}
```
