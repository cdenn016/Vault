---
type: paper
title: "3D Steerable CNNs: Learning Rotationally Equivariant Features in Volumetric Data"
aliases:
  - "Weiler 2018"
  - "3D Steerable CNNs"
authors:
  - Weiler, Maurice
  - Geiger, Mario
  - Welling, Max
  - Boomsma, Wouter
  - Cohen, Taco S.
year: 2018
arxiv: "1807.02547"
url: https://arxiv.org/abs/1807.02547
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# 3D Steerable CNNs: Learning Rotationally Equivariant Features in Volumetric Data

> [!info] Citation
> Weiler, Maurice, Mario Geiger, Max Welling, Wouter Boomsma, and Taco S. Cohen (2018). "3D Steerable CNNs: Learning Rotationally Equivariant Features in Volumetric Data." *Advances in Neural Information Processing Systems (NeurIPS)* 31. arXiv:1807.02547. <https://arxiv.org/abs/1807.02547>

## TL;DR

This paper develops convolutional neural networks for volumetric (3D) data that are equivariant to the full rotation group SO(3) by constructing steerable feature fields whose transformation properties are specified by irreducible representations of SO(3). The key technical contribution is an explicit, analytic parameterization of all SO(3)-equivariant convolution kernels between arbitrary feature field types, expressed in terms of spherical harmonics and Clebsch-Gordan coupling. This gives a complete, constructive basis for 3D steerable convolutions and achieves state-of-the-art results on 3D medical image segmentation benchmarks with substantially fewer parameters than non-equivariant baselines.

## Problem & setting

Standard 3D CNNs treat volumetric data with no built-in rotational symmetry: rotating the input by an arbitrary SO(3) element does not produce a predictably rotated output unless the network has seen all rotations in training. For tasks such as molecular property prediction, protein structure analysis, and 3D medical imaging, the underlying physics is rotationally invariant, so networks should reflect this. The steerable CNN framework (Cohen and Welling 2016; Weiler and Cesa 2019) extends equivariance from discrete groups to continuous Lie groups by assigning each feature map a representation of the symmetry group and requiring convolution kernels to intertwine those representations. In 3D the natural group is SO(3), whose irreps are the integer-spin spherical harmonic representations of dimension $2\ell+1$ for $\ell = 0, 1, 2, \ldots$.

## Method

The central object is a feature field $f : \mathbb{R}^3 \to \mathbb{R}^C$ that transforms as a direct sum of SO(3) irreps: $[T_g f](x) = \rho(g) f(g^{-1} x)$ where $\rho = \bigoplus_i \rho_{\ell_i}$ collects the spin-$\ell_i$ Wigner D-matrices of each channel group. SO(3)-equivariance of a convolution $f_{out} = \kappa \star f_{in}$ requires the kernel to satisfy the intertwiner condition
$$\kappa(g x) = \rho_{out}(g)\,\kappa(x)\,\rho_{in}(g)^{-1} \quad \forall\, g \in SO(3).$$
The authors solve this constraint by decomposing the kernel in a spherical harmonic / Clebsch-Gordan basis. For a pair of irreps $(\ell_{in}, \ell_{out})$, the radially-weighted kernel is an intertwiner between $\rho_{\ell_{in}}$ and $\rho_{\ell_{out}}$, which by Schur's lemma for SO(3) is spanned by the Clebsch-Gordan recoupling tensors for each allowed coupling spin $J \in \{|\ell_{out}-\ell_{in}|, \ldots, \ell_{out}+\ell_{in}\}$. Thus the full kernel space for any feature type pair has an explicit analytic basis parameterized by a radial profile per allowed coupling, and all learnable degrees of freedom are these radial functions (sampled discretely). This replaces unconstrained $3\times3\times3$ filter banks with a sparse, structured set of radial basis functions weighted by fixed spherical harmonic coupling tensors.

## Key results

The method is validated on 3D biomedical image segmentation (medical CT volumes) and molecular property prediction (QM9 dataset). On the medical segmentation tasks the equivariant models match or exceed standard U-Net-type baselines while using an order-of-magnitude fewer parameters, because the constraint removes all rotationally redundant filter degrees of freedom. On QM9 molecular property regression the 3D steerable approach achieves competitive results with methods that rely on hand-crafted molecular features, operating directly on volumetric electron-density grids. The analytic kernel basis is the principal theoretical result: it provides a complete characterization of the SO(3)-equivariant linear maps between any two feature field types, which subsumes earlier ad hoc 3D equivariant constructions and directly generalizes the 2D steerable CNN theory to the non-compact (relative to SO(2)) but still compact SO(3) case.

## Relevance to this research

The VFE transformer organizes its gauge sector around GL(K) block representations with Lie-algebra generators $\phi$ and Clebsch-Gordan coupling of irrep-indexed feature blocks. This paper is the most direct 3D precursor to the irrep-indexed kernel construction used throughout the steerable and gauge-equivariant CNN lineage that the project draws on. Three specific connections matter.

First, the Clebsch-Gordan kernel basis is structurally identical to the coupling used in [[Tensor Field Network|Tensor Field Networks]] (Thomas et al. 2018, same year) and provides an independent derivation of the same idea from the steerable-kernel perspective. In the VFE transformer context, the [[Clebsch-Gordan coefficients]] appear as the natural way to couple gauge-algebra blocks of different irrep type; this paper makes the constructive basis explicit and shows it is complete (no admissible kernels are missed).

Second, the radial-angular factorization of equivariant kernels (radial learnable, angular fixed by irrep coupling) is a template for the VFE project's separation of learnable scalar parameters from fixed group-theoretic structure. The principle — that gauge equivariance constrains the angular/group-theoretic shape of an interaction while leaving radial/scalar degrees of freedom free — recurs in every gauge-equivariant layer.

Third, the empirical demonstration that equivariant parameterization dramatically reduces parameter count while maintaining or improving accuracy directly motivates the VFE transformer's gauge-equivariant attention design: the GL(K) gauge structure is not merely theoretically principled but should provide similar sample-efficiency benefits.

> [!note] Editorial: Weiler et al. work with the compact group SO(3); the VFE transformer's gauge group is the non-compact block GL(K). The irrep-reduction and Clebsch-Gordan machinery transfers structurally, but the specific spherical harmonic bases and Wigner D-matrix formulas are SO(3)-specific and do not carry over directly. GL(K) representation theory requires separate treatment (in the manuscript [[gl-k-attention]]).

## Cross-links

- Concepts: [[Irreducible representation]], [[Clebsch-Gordan coefficients]], [[Group equivariance]], [[Gauge transformation]], [[Parallel transport]]
- Methods: [[Steerable CNN]], [[Gauge equivariant CNN]], [[Tensor Field Network]], [[Group equivariant CNN (G-CNN)]]
- Related sources: [[weiler-2019-e2-steerable]], [[thomas-2018-tensor-field-networks]], [[cohen-2019-gauge-cnn]], [[cohen-2016-gcnn]], [[finzi-2020-lieconv]]
- Theme: [[Gauge equivariance and geometric deep learning]]
- Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{weiler20183d,
  author    = {Weiler, Maurice and Geiger, Mario and Welling, Max and Boomsma, Wouter and Cohen, Taco S.},
  title     = {{3D} Steerable {CNNs}: Learning Rotationally Equivariant Features in Volumetric Data},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {31},
  year      = {2018},
  eprint    = {1807.02547},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1807.02547}
}
```
