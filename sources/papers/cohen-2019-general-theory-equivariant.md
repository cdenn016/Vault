---
type: paper
title: A General Theory of Equivariant CNNs on Homogeneous Spaces
aliases:
  - "Cohen, Geiger, Weiler 2019"
  - "General Theory of Equivariant CNNs on Homogeneous Spaces"
authors:
  - Taco S. Cohen
  - Mario Geiger
  - Maurice Weiler
year: 2019
arxiv: 1811.02017
url: https://arxiv.org/abs/1811.02017
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A General Theory of Equivariant CNNs on Homogeneous Spaces

> [!info] Citation
> Cohen, T. S., Geiger, M., & Weiler, M. (2019). A General Theory of Equivariant CNNs on Homogeneous Spaces. Advances in Neural Information Processing Systems 32 (NeurIPS 2019), 9145-9156. arXiv:1811.02017.

## TL;DR

This paper supplies the rigorous mathematical foundation for group-equivariant convolutional networks by recasting their feature maps as *fields* — sections of vector bundles — over a homogeneous base space, and their layers as equivariant linear maps between spaces of such fields. The central theorem, an application of Mackey theory and the theory of induced representations, is that every equivariant linear map between two field spaces is exactly a convolution with a kernel obeying a fixed linear constraint, and that the space of admissible kernels is finite-dimensional and computable irrep-by-irrep. With this in hand the authors classify *all* G-CNNs (the regular, steerable, spherical, and scalar-field variants that had been proposed separately) by three invariants: the symmetry group $G$, the homogeneous base space $G/H$ on which the fields live, and the *field type* — the representation of the stabilizer subgroup $H$ that dictates how each feature vector transforms. The work converts a zoo of ad hoc constructions into instances of a single induced-representation template.

## Problem & setting

By 2018 group-equivariant CNNs existed in many incompatible flavors: Cohen and Welling's group convolutions on discrete groups, steerable CNNs with irrep-valued features, spherical CNNs convolving over $\mathrm{SO}(3)$, and harmonic/scalar networks. Each was derived by hand for its own group and its own notion of "feature," and it was not clear which choices were forced and which were arbitrary. The paper asks the structural question: given a symmetry group $G$ acting transitively on a base space $X = G/H$ (so $X$ is a *homogeneous space* with stabilizer $H$), what is the full space of equivariant linear layers between feature fields, and what data must one fix to pin a network down? The prior art it consolidates includes Cohen and Welling's group-equivariant convolutions (ICML 2016), the steerable-CNN formalism (Cohen and Welling 2017; Weiler et al. 2018), and the spherical CNNs of Cohen et al. (ICLR 2018); the mathematical tools are Mackey's theory of induced representations and the classical correspondence between intertwiners and convolution operators.

## Method

A feature map is not a bare function $X \to \mathbb{R}^c$ but a *field*: a section of a vector bundle associated to the principal $H$-bundle $G \to G/H$ through a chosen representation $\rho$ of the stabilizer $H$ on a fiber $\mathbb{R}^c$. The group $G$ acts on the space of such sections by an *induced representation* $\mathrm{Ind}_H^G \rho$, and the "field type" of a layer is precisely the pair (fiber representation $\rho$, base point geometry). The key result is a one-to-one correspondence: every $G$-equivariant linear map between an input field of type $\rho_{\mathrm{in}}$ and an output field of type $\rho_{\mathrm{out}}$ is a convolution
$$
(\kappa \star f)(x) = \int_X \kappa(x, y)\, f(y)\, dy ,
$$
with a *steerable kernel* $\kappa$ that is forced to satisfy a two-sided equivariance constraint
$$
\kappa(h\,x) = \rho_{\mathrm{out}}(h)\,\kappa(x)\,\rho_{\mathrm{in}}(h)^{-1}, \qquad h \in H .
$$
This constraint is the heart of the theory. Decomposing $\rho_{\mathrm{in}}$ and $\rho_{\mathrm{out}}$ into [[Irreducible representation|irreducible representations]] of $H$ and invoking Schur's lemma turns the kernel constraint into independent linear conditions on each irrep block: between an input irrep and an output irrep the admissible kernel space is a fixed, finite-dimensional solution space (often spanned by harmonic basis functions), and it vanishes unless the irreps are compatible. Solving the constraint per irrep block therefore yields a complete, computable basis of equivariant kernels, and any equivariant layer is a learnable linear combination of that basis. Convolution itself is understood as integration over the group (or over $G/H$ with the induced action), recovering Cohen and Welling's group convolution as the special case where $\rho$ is the regular representation of $H$ and field type is "scalar over the full group."

## Key results

The paper's contributions are structural rather than empirical. First, it proves the intertwiner-equals-convolution correspondence for fields on homogeneous spaces, generalizing the classical Euclidean statement to arbitrary $G/H$. Second, it reduces the design of an equivariant layer to solving the kernel constraint per irrep, giving a constructive recipe for a complete kernel basis and a finite count of free parameters. Third, and most cited, it produces a *taxonomy*: any G-CNN in the literature is specified by its symmetry group $G$, its homogeneous base space $G/H$, and the field types (stabilizer representations) of its layers — and conversely every consistent choice of those three yields a valid equivariant architecture. Regular G-CNNs, steerable CNNs, spherical CNNs, and scalar-field networks fall out as particular field-type choices. The evidence is mathematical proof plus worked instantiations rather than benchmark tables; the paper's strength is that it shows the design space is exhausted by the three invariants and that nothing outside the steerable-kernel family can be equivariant and linear.

## Relevance to this research

This paper is the bundle-theoretic charter for treating equivariance as a constraint *forced* by a chosen field type rather than something coaxed out by training, and it directly grounds the VFE transformer's per-token frame-as-fibre picture. In the GL(K) attention construction each token carries a local gauge frame (a fibre over the token), the head dimension splits into stabilizer-style irrep blocks, and covariance transport $\Omega \Sigma \Omega^{\top}$ is the associated-bundle action on a field — exactly the induced-representation setup Cohen, Geiger and Weiler axiomatize. Their central lemma, that equivariant linear maps are convolutions by kernels obeying $\kappa(h x) = \rho_{\mathrm{out}}(h)\kappa(x)\rho_{\mathrm{in}}(h)^{-1}$ and that this constraint decomposes irrep-by-irrep via Schur's lemma, is the precise warrant for the program's block-diagonal $\mathrm{GL}(K_1)\oplus\cdots\oplus\mathrm{GL}(K_H)$ head structure and for the per-irrep-block mixers being the *only* equivariant maps available — the head mixer is allowed exactly to the extent it lives in the Schur commutant of the field type. It also clarifies a load-bearing distinction for the program: global $G$-equivariance over a homogeneous space (this paper) versus the local *gauge* equivariance of Cohen et al.'s later gauge-CNN work, which is the regime the transformer's untied per-block gauge actually inhabits. See [[Gauge equivariance and geometric deep learning]], [[Irreducible representation]], [[Group equivariance]], and [[Parallel transport]] for the connecting machinery.

## Cross-links

- Concepts / Themes: [[Gauge equivariance and geometric deep learning]], [[Irreducible representation]], [[Group equivariance]], [[Parallel transport]]
- Related sources: [[amari-1998-natural-gradient]]

## BibTeX

```bibtex
@inproceedings{cohen2019generalth,
  author    = {Cohen, Taco S. and Geiger, Mario and Weiler, Maurice},
  title     = {A General Theory of Equivariant {CNN}s on Homogeneous Spaces},
  booktitle = {Advances in Neural Information Processing Systems 32 (NeurIPS 2019)},
  pages     = {9145--9156},
  year      = {2019},
  eprint    = {1811.02017},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1811.02017}
}
```
