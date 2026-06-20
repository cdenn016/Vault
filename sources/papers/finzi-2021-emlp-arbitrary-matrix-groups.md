---
type: paper
title: A Practical Method for Constructing Equivariant Multilayer Perceptrons for Arbitrary Matrix Groups
aliases:
  - "Finzi, Welling, Wilson 2021 — EMLP"
  - "Equivariant MLPs for Arbitrary Matrix Groups"
authors:
  - Marc Finzi
  - Max Welling
  - Andrew Gordon Wilson
year: 2021
arxiv: 2104.09459
url: https://arxiv.org/abs/2104.09459
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

# A Practical Method for Constructing Equivariant Multilayer Perceptrons for Arbitrary Matrix Groups

> [!info] Citation
> Finzi, M., Welling, M., & Wilson, A. G. (2021). A Practical Method for Constructing Equivariant Multilayer Perceptrons for Arbitrary Matrix Groups. Proceedings of the 38th International Conference on Machine Learning (ICML 2021), PMLR 139:3318-3328. arXiv:2104.09459.

## TL;DR

Equivariant networks before this work were built group by group, each new symmetry demanding a bespoke derivation of which linear maps respect it. Finzi, Welling, and Wilson replace that artisanal pipeline with a single mechanical procedure: given any matrix group specified by a finite set of generators (and, for the continuous part, its Lie-algebra generators), the equivariance condition on a layer's weight matrix becomes a homogeneous linear system, and the space of admissible equivariant layers is exactly the nullspace of that system. Solving the nullspace numerically yields an orthonormal basis of equivariant maps, which is then parameterized by free coefficients and trained. Because the construction only needs the generators acting in some representation, it works uniformly for compact groups (permutations, $O(5)$), non-compact groups (the Lorentz group $O(1,3)$, the general linear group $GL(n)$), symplectic groups $Sp(n)$, and even finite groups like the Rubik's cube group — settings where no closed-form convolutional kernel exists. The resulting architecture, EMLP, is a multilayer perceptron whose every linear layer is provably equivariant and whose nonlinearities are supplied by group-equivariant gated and bilinear layers, and it is released as an open-source library that takes a group and a representation and returns the trainable layer.

## Problem & setting

Equivariance — the requirement that transforming the input by a group element produces a correspondingly transformed output — is the structural prior behind convolutional networks (translation), graph and set networks (permutation), and steerable/spherical CNNs (rotation). Each of these was derived analytically for its specific group, typically by exploiting that the group is compact and that its representations decompose into known [[Irreducible representation|irreducibles]] with tabulated intertwiners. That strategy does not transfer to groups outside the small catalogue of translation, rotation, and permutation, and it stalls entirely for non-compact groups such as the Lorentz group of special relativity or the general linear group $GL(n)$, whose representation theory lacks the clean orthogonality and finite decomposition that the compact case provides. The paper's setting is the general one: an arbitrary matrix group $G$, presented by a (possibly mixed continuous-and-discrete) generating set, acting through a chosen representation $\rho$ on the feature spaces between layers. The aim is a constructive, numerical, group-agnostic recipe for the equivariant linear layers, building on the steerable-CNN and group-convolution lineage of Cohen and Welling but discarding the assumption that closed-form solutions or compactness are available.

## Method

A linear layer $W$ mapping a representation $\rho_{\text{in}}$ to a representation $\rho_{\text{out}}$ is equivariant if and only if it intertwines the two representations,
$$ \rho_{\text{out}}(g)\, W = W\, \rho_{\text{in}}(g) \qquad \text{for all } g \in G. $$
For a continuous group this infinite family of constraints reduces, by differentiating at the identity, to a finite set of linear conditions indexed by the Lie-algebra generators $X_k$ of $\mathfrak{g}$,
$$ \rho_{\text{out}}(X_k)\, W - W\, \rho_{\text{in}}(X_k) = 0, $$
supplemented by one discrete constraint $\rho_{\text{out}}(h)\,W - W\,\rho_{\text{in}}(h) = 0$ for each generator $h$ of any disconnected component. Vectorizing $W$ turns each constraint into a sparse matrix acting on $\mathrm{vec}(W)$, so the full equivariance condition is a single large homogeneous system $C\,\mathrm{vec}(W) = 0$. The set of equivariant layers is precisely $\ker C$, and the authors compute an orthonormal basis of this nullspace numerically — using an iterative scheme that avoids forming the dense constraint matrix, so the method scales to high-dimensional representations where a direct singular value decomposition would be infeasible. The free parameters of the layer are then the coordinates of $W$ in this basis. Representations for the hidden layers are assembled compositionally from a small set of base representations through the standard tensor algebra — direct sums $\rho \oplus \rho'$, tensor products $\rho \otimes \rho'$, and duals $\rho^{*}$ — so the user specifies feature types as algebraic expressions and the solver handles the rest. Because pointwise nonlinearities generally break equivariance for nontrivial representations, EMLP obtains its nonlinearity from equivariant gated activations and from bilinear layers that contract pairs of features through the equivariant tensor structure, preserving the symmetry while supplying the expressivity an MLP needs.

## Key results

The central result is the algorithm itself: a single procedure that, given generators of any matrix group and a representation, returns a basis for the equivariant linear maps without case-by-case mathematics. The authors demonstrate it across a deliberately diverse zoo of groups spanning the compact, non-compact, symplectic, and finite cases — including $O(5)$, the Lorentz group $O(1,3)$, $SO(n)$, $Sp(n)$, $GL(n)$-type and permutation symmetries, and the Rubik's cube group — recovering known equivariant bases where they exist and producing new ones where none had been derived. On applied tasks the equivariant EMLP improves over non-equivariant baselines, with the headline demonstrations drawn from particle physics (a Lorentz-equivariant regression) and from modeling dynamical systems, including Hamiltonian dynamics where the relevant symmetry is symplectic. The evidence is strong on generality and correctness of the construction (the equivariance is exact by design, not learned), and supportive though more modest in scale on the downstream benchmarks, which serve to illustrate rather than exhaustively stress-test the approach. The accompanying open-source library is itself a load-bearing contribution, making the method reproducible and reusable.

## Relevance to this research

This paper closes a gap flagged in [[Gauge equivariance and geometric deep learning]]: most geometric-deep-learning machinery presumes compact structure groups with tabulated irreducible intertwiners, whereas the VFE transformer's gauge group is $GL(K)$ — non-compact, and exactly the regime where the older analytic recipes fail. Finzi et al. supply a constructive answer by solving the intertwiner constraint $\rho(X)W = W\rho(X)$ at the Lie-algebra level and reading off the equivariant maps as a numerical nullspace, which is precisely the object the program needs when it restricts per-block head maps to the commutant of a representation (the Schur-commutant head mixer of `use_head_mixer` and its irrep-tower siblings are commutants of exactly this kind). The construction therefore validates, from the equivariant-ML side, the program's claim that admissible gauge-equivariant linear maps form the block-diagonal commutant $GL(K_1)\oplus\cdots\oplus GL(K_H)$ over the [[Irreducible representation|irreducible]] decomposition — and it generalizes the recipe to any matrix group the program might later adopt (Lorentz-type or symplectic [[Group equivariance|structure groups]]), at the cost of trading closed forms for a numerical solve. It is the practical bridge between the gauge-theoretic insistence on exact equivariance and an implementable layer.

## Cross-links

- Concepts / Themes: [[Gauge equivariance and geometric deep learning]], [[Group equivariance]], [[Irreducible representation]]

## BibTeX

```bibtex
@inproceedings{finzi2021emlparbit,
  author    = {Finzi, Marc and Welling, Max and Wilson, Andrew Gordon},
  title     = {A Practical Method for Constructing Equivariant Multilayer Perceptrons for Arbitrary Matrix Groups},
  booktitle = {Proceedings of the 38th International Conference on Machine Learning (ICML 2021)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {139},
  pages     = {3318--3328},
  year      = {2021},
  publisher = {PMLR},
  eprint    = {2104.09459},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/2104.09459}
}
```
