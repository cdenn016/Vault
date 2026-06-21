---
type: concept
title: Clebsch-Gordan coefficients
aliases:
  - Clebsch-Gordan coupling
  - CG coefficients
  - Clebsch-Gordan tensor product
  - CG tensor product
  - "Tensor Product"
tags:
  - cluster/gauge-theory
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Clebsch-Gordan coefficients

## Definition

The **Clebsch-Gordan (CG) coefficients** are the fixed numerical constants that decompose the tensor product of two [[Irreducible representation|irreducible representations]] of a group into a direct sum of irreducibles. Given a group $G$ and two irreps acting on spaces $V_{\ell_1}$ and $V_{\ell_2}$, the tensor-product representation on $V_{\ell_1} \otimes V_{\ell_2}$ is generally *reducible*: it splits into a sum of irreps,
$$
V_{\ell_1} \otimes V_{\ell_2} \;\cong\; \bigoplus_{\ell} \, m_{\ell}\, V_{\ell},
$$
where $m_\ell$ are integer multiplicities. The CG coefficients are the entries of the orthogonal (unitary) change-of-basis matrix $C$ that realizes this isomorphism explicitly. Writing basis vectors with magnetic indices, a coupled vector in the $\ell$ block is obtained from the product basis by
$$
v^{(\ell)}_{m} \;=\; \sum_{m_1,\,m_2} C^{\,\ell\, m}_{\ell_1 m_1,\; \ell_2 m_2}\; u^{(\ell_1)}_{m_1}\, w^{(\ell_2)}_{m_2}.
$$
The defining property is *equivariance*: for any group element $g$, applying $g$ to the two factors and then coupling gives the same result as coupling and then applying $g$ in the coupled irreps. Equivalently, $C$ intertwines $\rho_{\ell_1}(g)\otimes\rho_{\ell_2}(g)$ with $\bigoplus_\ell \rho_\ell(g)$ for all $g$. The classical case is $G=\mathrm{SO}(3)$ (or its cover $\mathrm{SU}(2)$), where the coefficients couple angular momenta $\ell_1$ and $\ell_2$ into total angular momentum $\ell$ ranging over $|\ell_1-\ell_2|,\dots,\ell_1+\ell_2$; but the construction is general to any compact (and, with care, reductive) group.

The map $(u, w) \mapsto v^{(\ell)}$ built from CG coefficients is the **Clebsch-Gordan tensor product** (or "CG coupling"): a bilinear, group-equivariant way to combine two feature vectors that themselves transform under irreps, producing an output that again transforms cleanly under the group.

## Why it matters here

The VFE transformer declares a structural symmetry group — the block general-linear group $\mathrm{GL}(k)$ (the config's `gauge_group block_glk`) — and organizes its internal features by **irreps** of that group. The moment features carry irrep labels, any operation that *multiplies* or *couples* two such features must be made equivariant, or the declared symmetry is broken. CG coefficients are precisely the bookkeeping that keeps bilinear interactions inside the equivariant category: they are the only group-respecting way to take a tensor product of two irrep-typed quantities and read off the result back in irrep coordinates. In the config this surfaces as **Clebsch-Gordan coupling** between irrep blocks.

This matters for the same reason [[Group equivariance]] matters throughout the model: a gauge-theoretic transformer wants its predictions to be independent of the arbitrary local frame chosen at each token (see [[Gauge transformation]]). Linear, irrep-preserving maps are already constrained by representation theory, but the interesting nonlinear couplings — where information from one irrep block influences another — require the CG tensor product to stay equivariant. Without it, mixing blocks would silently entangle the gauge frame into the computation.

> [!note] Editorial: The source digest names Clebsch-Gordan coupling between irrep blocks as an architectural ingredient but does not specify the exact bilinear sites in the layer stack; the mechanics below are imported from the canonical equivariant-network literature ([[thomas-2018-tensor-field-networks]], [[weiler-2019-e2-steerable]]) that the project draws on.

## Details

**The intertwiner / Schur picture.** By Schur's lemma, an equivariant linear map between irreps is zero unless the irreps match, in which case it is a scalar (up to multiplicity). The CG decomposition extends this to *bilinear* maps: the space of equivariant bilinear maps $V_{\ell_1}\otimes V_{\ell_2}\to V_\ell$ is spanned exactly by the CG coupling onto the $\ell$ block, with dimension equal to the multiplicity $m_\ell$. So CG coefficients enumerate *all* allowed equivariant quadratic interactions — a representation-theoretic basis, just as harmonic analysis gives a basis for equivariant linear layers in [[kondor-2018-compact-group-conv]].

**Selection rules.** The decomposition is sparse: most products $(\ell_1,\ell_2,\ell)$ are forbidden (their multiplicity is zero), which both constrains and cheapens the computation. For $\mathrm{SO}(3)$ this is the triangle inequality $|\ell_1-\ell_2|\le \ell \le \ell_1+\ell_2$; for general groups it is the multiplicity pattern of the tensor product. These selection rules are exactly what make irrep bookkeeping tractable.

**The canonical template.** [[thomas-2018-tensor-field-networks|Tensor Field Networks]] make this concrete for neural layers: features live in $\mathrm{SO}(3)$ irreps, spatial filters are built from spherical harmonics, and the filter output is coupled to the feature via the Clebsch-Gordan tensor product — yielding rotation- and translation-equivariant layers for 3D point clouds. This is the direct ancestor of "irrep bookkeeping + CG coupling" as a network design pattern. [[weiler-2019-e2-steerable|General E(2)-equivariant steerable CNNs]] reach the same place from the kernel-constraint side: they reduce an arbitrary representation kernel constraint to *per-irrep* constraints, producing a reusable irrep-indexed steerable basis — the linear-layer counterpart to CG coupling's bilinear one.

**Variants and relatives.** The CG tensor product is the bilinear member of a family. Its linear cousins are the steerable / irrep-block-diagonal linear maps licensed by Schur's lemma; its filter-side cousin in the gauge setting is the kernel constraint of [[cohen-2019-gauge-cnn|gauge equivariant CNNs]], which additionally couples features through [[Parallel transport]] across a manifold. Computationally, CG coupling can be cast as a tensor contraction against a sparse coefficient tensor, and for large irreps it is often the dominant cost of equivariant layers, motivating cached or factorized CG tensors.

## In this work

Within the VFE transformer's config, Clebsch-Gordan coupling is the equivariant mechanism for letting the $\mathrm{GL}(k)$ irrep blocks interact. The model parameterizes its gauge degrees of freedom in the Lie algebra (the "phi" parameterization) and retracts via [[Baker-Campbell-Hausdorff formula|Baker-Campbell-Hausdorff]], following the algebra-first style of [[finzi-2020-lieconv|LieConv]]; the irreps it carries are organized so that block-to-block mixing can be expressed as CG tensor products rather than arbitrary (symmetry-breaking) linear mixes. This sits alongside the model's other geometric machinery — [[Parallel transport]] and [[Holonomy]] for moving beliefs between token frames, and the broader [[Group equivariance]] discipline articulated in [[bronstein-2021-geometric-deep-learning|geometric deep learning]] — as the piece that keeps *quadratic* feature interactions inside the equivariant category.

## Sources

- [[thomas-2018-tensor-field-networks]] — features in $\mathrm{SO}(3)$ irreps coupled by the Clebsch-Gordan tensor product; the canonical template for irrep bookkeeping and CG coupling.
- [[weiler-2019-e2-steerable]] — reduces representation kernel constraints to per-irrep constraints, giving a reusable irrep-indexed steerable basis directly applicable to CG block coupling.
- [[kondor-2018-compact-group-conv]] — representation-theoretic / harmonic-analysis account organizing admissible equivariant operations by irreps for compact groups.
- [[cohen-2019-gauge-cnn]] — gauge-equivariant kernel constraint and parallel-transport rule, the local-gauge counterpart in which irrep features are coupled.
- [[cohen-2016-gcnn]] — the foundational statement that a declared symmetry group structures the network's operations.
- [[bronstein-2021-geometric-deep-learning]] — Erlangen-Program synthesis supplying the gauge/equivariance scaffolding around irrep coupling.
- [[finzi-2020-lieconv]] — Lie-algebra-first parameterization matching the model's $\mathrm{GL}(k)$ gauge handling.
- [[fulton-harris-1991-representation-theory]] — irrep classification and Clebsch-Gordan machinery behind the `block_glk` gauge and the isotypic head mixers.
- [[steinberg-2012-representation-theory-finite-groups]] — finite-group irrep and character theory behind the model's isotypic head mixers and CG coupling.

## See also

- [[Irreducible representation]]
- [[Group equivariance]]
- [[Gauge transformation]]
- [[Parallel transport]]
- [[Holonomy]]
- [[Gauge equivariant CNN]]
- [[Steerable CNN]]
- [[Tensor Field Network]]
- [[Group equivariant CNN (G-CNN)]]
