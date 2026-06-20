---
type: concept
title: Irreducible representation
aliases:
  - Irrep
  - Irreps
  - Irreducible representations
tags:
  - cluster/gauge-theory
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Irreducible representation

## Definition

A *representation* of a group $G$ on a vector space $V$ is a homomorphism $\rho : G \to GL(V)$, assigning to each group element $g$ an invertible linear map $\rho(g)$ that respects the group law, $\rho(g)\rho(h) = \rho(gh)$. A subspace $W \subseteq V$ is *invariant* (a *subrepresentation*) if $\rho(g)\,W \subseteq W$ for every $g$. A representation is **irreducible** — an *irrep* — when its only invariant subspaces are the trivial ones, $\{0\}$ and $V$ itself. Equivalently, an irrep cannot be written as a direct sum of smaller representations; it is an atom out of which all other representations of $G$ are built.

For the compact and reductive groups that appear in geometric deep learning, two structural theorems make irreps the natural coordinate system. *Maschke's / complete-reducibility theorem* says every finite-dimensional representation decomposes as a direct sum of irreps, $V \cong \bigoplus_i m_i\, V_i$, where the $V_i$ are distinct irreps and $m_i$ are multiplicities. *Schur's lemma* says any linear map that commutes with a group action (an *intertwiner*) is, between two irreps, either zero (if they are inequivalent) or a scalar multiple of the identity (if they are the same). Together these mean that any equivariant linear operation is forced to act *block-diagonally and scalar-wise within each irrep type* — which is exactly why irreps function as the bookkeeping device for symmetry-respecting architectures.

## Why it matters here

The VFE transformer declares a symmetry group — the block general-linear group $GL(k)$, tag `gauge_group block_glk` — and asks its representations and beliefs to transform consistently under it. Whenever a network commits to a symmetry group, representation theory dictates the *only* admissible linear maps: by Schur's lemma the design space of equivariant layers collapses to a choice of how irreps are mixed and coupled. Irreps are therefore the alphabet in which the model's [[Group equivariance]] is spelled out. They label the feature "types" that may legally interact, and the [[Clebsch-Gordan coefficients]] are the multiplication table telling which products of irrep features land in which output irrep.

This matters concretely for the model's gauge machinery. Per-token beliefs and gauge frames are transported between positions ([[Parallel transport]]) and accumulate twists around loops ([[Holonomy]]); for these operations to be well defined and equivariant, the objects being transported must carry definite representation labels. The Clebsch-Gordan coupling and irrep structure cited in the config are the means by which block features of different types are combined without breaking $GL(k)$ covariance. In short, irreps convert an abstract symmetry declaration into a finite, enforceable set of allowed couplings.

## Details

**Decomposition and the canonical form.** Writing a representation in *isotypic* form, $V \cong \bigoplus_i \mathbb{C}^{m_i} \otimes V_i$, separates the multiplicity space $\mathbb{C}^{m_i}$ (which an equivariant layer may mix freely) from the irrep space $V_i$ (on which the group acts irreducibly and which an equivariant map can only scale, per Schur). This split is the structural reason equivariant networks parameterize a *learnable mixing of multiplicities* but a *fixed action within each irrep*.

**Tensor products and Clebsch-Gordan.** The tensor product of two irreps is generally reducible and decomposes again into irreps, $V_a \otimes V_b \cong \bigoplus_c N_{ab}^{c}\, V_c$. The change-of-basis matrices realizing this decomposition are the Clebsch-Gordan coefficients. They are the canonical mechanism for building nonlinear, multiplicative interactions between typed features while staying equivariant — used to couple $SO(3)$ irreps via the Clebsch-Gordan tensor product in [[thomas-2018-tensor-field-networks]] and generalized to a per-irrep kernel basis in [[weiler-2019-e2-steerable]]. See [[Clebsch-Gordan coefficients]].

**Kernel constraints reduce to irreps.** The deep payoff for architecture design is that the constraint "this convolution / linear map must be equivariant" can be solved *one irrep at a time*. [[weiler-2019-e2-steerable]] shows that for $E(2)$ the general group-representation kernel constraint factors into independent per-irrep constraints, yielding a reusable, irrep-indexed steerable basis. [[kondor-2018-compact-group-conv]] proves, via representation theory and harmonic analysis, that group convolution is *necessary and sufficient* for linear equivariance under any compact group, and organizes the admissible operations by irrep. This is the rigorous backbone behind the slogan that a declared symmetry group structures the whole network, first made operational for discrete groups by [[cohen-2016-gcnn]]. [[cohen-2019-general-theory-equivariant]] lifts this to a fiber-bundle / induced-representation (Mackey-theory) footing, proving that equivariant linear maps correspond one-to-one with convolutions by steerable kernels constrained per irrep and thereby classifying G-CNNs by symmetry group, base space, and field type — the abstract counterpart of the project's per-token $GL(k)$ frame-as-fibre and irrep-block decomposition.

**Steerability.** A feature field is *steerable* when transforming the input by $g$ acts on the field by the corresponding irrep matrices $\rho_i(g)$; steerable CNNs ([[weiler-2019-e2-steerable]]) and the gauge/manifold setting of [[cohen-2019-gauge-cnn]] organize feature maps as stacks of irrep-typed fields whose transport respects the local frame. [[bronstein-2021-geometric-deep-learning]] places this irrep-and-equivariance scaffolding inside a single "Grids, Groups, Graphs, Geodesics, Gauges" blueprint.

> [!note] Editorial: For the *general*-linear group $GL(k)$ used here — non-compact and not semisimple — the clean finite-dimensional unitary irrep theory of compact groups does not transfer verbatim; $GL(k)$ representations need not be completely reducible. In practice the project works in Lie-algebra ("phi") coordinates (cf. the algebra-first parameterization of [[finzi-2020-lieconv]]), so "irrep" should be read as the type-labeling and block-coupling discipline inherited from the compact-group theory above, applied per block, rather than a literal unitary irrep classification of $GL(k)$. The constructive route for exactly this non-compact regime is [[finzi-2021-emlp-arbitrary-matrix-groups]], which builds layers equivariant to arbitrary matrix groups (including the non-compact $GL(n)$, $O(1,3)$, $Sp(n)$) by solving the commutant constraint $\rho(X)W = W\rho(X)$ at the Lie-algebra level via nullspace computation — closing the non-compact-group gap for the project's commutant-restricted per-block maps.

## In this work

Irreps surface wherever the config's gauge-theoretic vocabulary touches typed, coupled features:

- **Gauge group `block_glk`.** The block $GL(k)$ structure partitions features into blocks that transform under group actions; representation labels are what make a "block" a well-defined transforming object rather than an arbitrary slice. This block structure also dovetails with the per-block [[Killing form|Killing-form]] preconditioning and the [[Fisher information metric]]-style, Kronecker-factored M-step (cf. [[martens-2015-kfac]], [[ollivier-2015-riemannian-metrics-nn]]).
- **Clebsch-Gordan coupling and irreps (config terms).** Explicitly listed in the architecture; these are the operations that combine block features of different types, following the template of [[thomas-2018-tensor-field-networks]] and the per-irrep machinery of [[weiler-2019-e2-steerable]] and [[kondor-2018-compact-group-conv]].
- **Parallel transport / holonomy of beliefs.** Transporting per-token Gaussian beliefs and gauge frames ([[Parallel transport]], [[Holonomy]]) presupposes those objects carry representation types, the local-gauge setting formalized by [[cohen-2019-gauge-cnn]].
- **Positional encodings via learned phi.** The Lie-algebra `phi` parameterization composed through [[Baker-Campbell-Hausdorff formula|BCH]] retraction is the algebra-coordinate analogue of [[finzi-2020-lieconv]]; irrep structure governs how such transforming features may legally interact.

## Sources

- [[cohen-2016-gcnn]] — group-equivariant convolution; a declared symmetry group structures the architecture.
- [[cohen-2019-gauge-cnn]] — local gauge equivariance, kernel constraints, parallel transport on manifolds.
- [[weiler-2019-e2-steerable]] — reduction of the kernel constraint to per-irrep constraints; irrep-indexed steerable basis.
- [[kondor-2018-compact-group-conv]] — representation theory / harmonic analysis: convolution is necessary and sufficient for compact-group equivariance, organized by irreps.
- [[cohen-2019-general-theory-equivariant]] — fiber-bundle / Mackey-theory foundation: equivariant maps as steerable convolutions constrained per irrep, classifying G-CNNs by group, base space, and field type.
- [[finzi-2021-emlp-arbitrary-matrix-groups]] — constructive equivariant layers for arbitrary (including non-compact) matrix groups by Lie-algebra-level nullspace solution of the commutant constraint.
- [[thomas-2018-tensor-field-networks]] — features living in irreps coupled by the Clebsch-Gordan tensor product.
- [[finzi-2020-lieconv]] — Lie-algebra (log) coordinates for equivariance, the algebra-first parameterization mirrored by the project's `phi`.
- [[bronstein-2021-geometric-deep-learning]] — Erlangen-program synthesis placing irreps and equivariance in one blueprint.

## See also

- [[Group equivariance]]
- [[Clebsch-Gordan coefficients]]
- [[Gauge transformation]]
- [[Parallel transport]]
- [[Holonomy]]
- [[Steerable CNN]]
- [[Gauge equivariant CNN]]
- [[Group equivariant CNN (G-CNN)]]
- [[Tensor Field Network]]
- [[LieConv]]

## Related sources (ingested 2026-06-20)

- [[bleecker-1981-gauge-theory-variational-principles]] — Foundational treatment of gauge fields as connections on principal bundles and the variational (Yang-Mills) principle;
- [[fulton-harris-1991-representation-theory]] — Standard reference for Lie-group/Lie-algebra irreps and isotypic decomposition - the rep-theory backbone of the block_glk gauge and irrep-tower head mixers.
- [[steinberg-2012-representation-theory-finite-groups]] — Concrete character-theoretic development of finite-group representation theory;
- [[cohen-2018-spherical-cnns]] — SO(3)-equivariant convolution via generalized Fourier analysis on the sphere;
- [[georgi-1999-lie-algebras-particle-physics]] — computational representation theory: roots/weights, Young tableaux, and explicit tensor-product (Clebsch–Gordan) decomposition into irreducibles.
- [[woit-2017-quantum-theory-groups-representations]] — Lie-group/representation theory through quantum mechanics; the $SU(2)$/$SO(3)$ irrep prototype and the momentum map from a group action.
- [[hall-2013-quantum-theory-mathematicians]] — rigorous operator-theoretic QM with $SU(2)$ angular momentum, the Wigner–Eckart theorem, and geometric quantization (companion to Hall's Lie-groups text).
