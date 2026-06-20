---
type: paper
title: General E(2)-Equivariant Steerable CNNs
aliases:
  - "Weiler & Cesa 2019 — E(2)-Steerable CNNs"
authors:
  - Maurice Weiler
  - Gabriele Cesa
year: 2019
arxiv: "1911.08251"
url: https://arxiv.org/abs/1911.08251
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# General E(2)-Equivariant Steerable CNNs

> [!info] Citation
> Maurice Weiler and Gabriele Cesa. *General E(2)-Equivariant Steerable CNNs.* NeurIPS 2019. arXiv:1911.08251. <https://arxiv.org/abs/1911.08251>

## TL;DR

The paper gives a unified, constructive theory of convolutions on the plane that are equivariant to the Euclidean group E(2) — translations together with rotations and reflections. Feature fields transform according to chosen group representations, and equivariance imposes a linear constraint on the convolution kernels. The central technical move is to show that the kernel constraint for an *arbitrary* representation decomposes into independent constraints, one per pair of [[Irreducible representation|irreducible representations]], so that solving the irrep-level constraint once yields a complete steerable basis for any feature type. This turns equivariant network design into a bookkeeping exercise over irreps and their couplings.

## Problem & setting

A standard CNN is equivariant only to translations. To additionally guarantee that rotating or reflecting the input produces a correspondingly transformed output, one must restrict which kernels are admissible. Following the Steerable CNN program, each feature space is a *feature field* assigned a representation $\rho$ of the structure group (a subgroup of O(2)), specifying how its channels mix under a group element. Equivariance of a convolution between an input field of type $\rho_{in}$ and an output field of type $\rho_{out}$ is then equivalent to a kernel constraint
$$\kappa(g\,x) = \rho_{out}(g)\,\kappa(x)\,\rho_{in}(g)^{-1},$$
a linear PDE-like condition the kernel $\kappa$ must satisfy pointwise. The difficulty is that $\rho_{in}$ and $\rho_{out}$ may be high-dimensional reducible representations, making the constraint unwieldy to solve directly.

## Method

The authors reduce the general constraint to its irreducible pieces. Any orthogonal representation decomposes into a direct sum of irreps via a change of basis; under that decomposition the kernel constraint block-diagonalizes into independent constraints between pairs of irreps $(\psi_i, \psi_j)$. They solve each irrep-to-irrep constraint in closed form for O(2), SO(2), the cyclic and dihedral groups, and the reflection group, obtaining an analytic angular basis (built from circular harmonics) for the admissible kernels in every case. A general steerable kernel is then assembled by stacking these elementary solutions according to the irrep multiplicities of the chosen field types — equivalently, by intertwining irreps through fixed projection/embedding maps. Because the framework treats the representation type as a free design choice, it subsumes prior equivariant architectures (group-convolutional, harmonic, and steerable variants) as special cases and exposes the full design space. The companion `e2cnn` library implements the basis generation and field algebra.

## Key results

A systematic empirical study sweeps over subgroups of E(2) and over field-type choices, substituting equivariant layers into standard backbones. The equivariant models improve accuracy on CIFAR-10, CIFAR-100, and STL-10 over non-equivariant baselines, with the best symmetry group depending on the dataset's intrinsic invariances. The paper's lasting contribution is less the benchmark numbers than the unifying recipe: a complete, reusable irrep-indexed basis for planar equivariant kernels.

## Relevance to this research

The VFE-transformer's gauge sector is organized around irreps and [[Clebsch-Gordan coefficients|Clebsch-Gordan]] coupling of block general-linear (GL(k)) feature blocks, and this paper supplies the canonical machinery for exactly that pattern. Three connections are concrete:

- **Irrep-level constraint reduction.** The project parameterizes gauge action in a Lie-algebra ("phi") basis and couples blocks via Clebsch-Gordan tensors. Weiler and Cesa's reduction — *solve the constraint once per irrep pair, then assemble by multiplicity* — is the template for building GL(k)-block-equivariant maps without re-deriving constraints for every reducible block type. See [[Irreducible representation]] and [[Clebsch-Gordan coefficients]].
- **Steerable bases as equivariant linear maps.** Their kernel constraint $\kappa(gx)=\rho_{out}(g)\kappa(x)\rho_{in}(g)^{-1}$ is the intertwiner condition; the project's requirement that gauge transformations act consistently across coupled blocks is the same algebraic demand, here solved constructively. This grounds [[Group equivariance]] and the use of [[Tensor Field Network|Tensor Field Networks]]-style irrep tensor products in the attention/positional pathway.
- **Design-space map for symmetry choice.** The paper's sweep over E(2) subgroups and field types is methodologically the same decision the VFE-transformer faces in choosing how gauge structure couples to attention; it argues that the right symmetry and field type are dataset-dependent and should be searched, not assumed.

> [!note] Editorial: Weiler and Cesa work with compact planar groups O(2)/SO(2), whereas the project's gauge group is the non-compact block general-linear group GL(k); the irrep-reduction and intertwiner machinery transfers structurally, but the analytic circular-harmonic bases do not carry over directly, since GL(k) representation theory differs from that of compact O(2).

## Cross-links

- Concepts: [[Irreducible representation]], [[Clebsch-Gordan coefficients]], [[Group equivariance]], [[Gauge transformation]]
- Methods: [[Steerable CNN]], [[Gauge equivariant CNN]], [[Group equivariant CNN (G-CNN)]], [[Tensor Field Network]]
- Related sources: [[cohen-2019-gauge-cnn]], [[cohen-2016-gcnn]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]], [[bronstein-2021-geometric-deep-learning]]
- Theme: [[Gauge equivariance and geometric deep learning]]
- Project: [[VFE Transformer Program]]

```bibtex
@inproceedings{weiler2019e2steerable,
  title     = {General {E(2)}-Equivariant Steerable {CNNs}},
  author    = {Weiler, Maurice and Cesa, Gabriele},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2019},
  eprint    = {1911.08251},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1911.08251}
}
```
