---
type: concept
title: Group equivariance
aliases:
  - Equivariance
  - Equivariant map
  - G-equivariance
  - Group-equivariant
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Group equivariance

## Definition

A map `f: X -> Y` is **equivariant** with respect to a group `G` when transforming the input by a group element produces a *correspondingly* transformed output, rather than leaving the output unchanged. Formally, suppose `G` acts on the input space through a representation `rho_X` and on the output space through a representation `rho_Y`. Then `f` is `G`-equivariant if

```
f(rho_X(g) . x) = rho_Y(g) . f(x)    for all g in G, x in X.
```

The two special cases worth naming explicitly are **invariance**, where `rho_Y(g)` is the identity for every `g` (the output does not move at all), and the **self-equivariant** case `rho_X = rho_Y` (input and output transform the same way). Invariance is thus equivariance into a trivial representation. The defining property is that symmetry *commutes* with the map: it does not matter whether one acts first and then applies `f`, or applies `f` first and then acts. A network built from equivariant layers inherits equivariance by composition, because the composition of equivariant maps is again equivariant.

A representation `rho` is a homomorphism from `G` into the invertible linear maps on a vector space, `rho(g h) = rho(g) rho(h)`; the choice of representation on each layer is what fixes *how* features transform. When that representation decomposes into [[Irreducible representation|irreducible representations]] (irreps), equivariance reduces to a set of independent per-irrep constraints — the organizing principle behind steerable architectures [[weiler-2019-e2-steerable]].

## Why it matters here

In the VFE Transformer, equivariance is the formal contract that justifies treating the model as *gauge-theoretic* rather than merely as a transformer with extra matrices. The architecture declares a symmetry group — the block general-linear group `GL(k)` (config `gauge_group: block_glk`) — and the design goal is that the network's belief-carrying computation respect that group's action. Equivariance is precisely the property a layer must have for "respecting a declared symmetry group" to be a precise statement rather than a slogan.

This matters for three concrete reasons.

First, the per-token Gaussian beliefs `(mu, Sigma)` central to the [[Variational free energy|variational free energy]] objective live in a space carrying a `GL(k)` action: a change of internal frame acts on `mu` by a linear map and on the covariance `Sigma` by the congruence (sandwich) action `Sigma -> G Sigma G^T`. If the inference and attention layers are equivariant, then a [[Gauge transformation|gauge transformation]] of the frame leaves the *physical* content of the beliefs unchanged while the coordinates transform predictably — the same logic that makes [[cohen-2019-gauge-cnn|gauge-equivariant CNNs]] well-defined on manifolds where no canonical frame exists.

Second, equivariance licenses [[Parallel transport|parallel transport]] of beliefs between tokens. Transporting a belief along a connection and *then* applying an equivariant layer agrees with applying the layer and then transporting; without equivariance, transport and computation would not commute and [[Holonomy|holonomy]] would be meaningless as a diagnostic.

Third, equivariance is the architectural counterpart of the *reparameterization invariance* the model already enjoys on the optimization side. The [[Natural gradient|natural gradient]] is invariant to smooth reparameterization of the model [[amari-1998-natural-gradient]]; group equivariance is invariance to a chosen *linear* symmetry acting on features. The two together give a model whose answers do not depend on arbitrary coordinate choices, whether of parameters or of frames [[ollivier-2015-riemannian-metrics-nn]].

## Details

**Group convolution as the canonical equivariant map.** The foundational result of geometric deep learning is that, for translations, ordinary convolution is exactly the operation that commutes with the group action — and generalizing the integral/sum from the translation group to a larger group `G` yields a *group convolution* that is `G`-equivariant by construction [[cohen-2016-gcnn]]. [[kondor-2018-compact-group-conv]] sharpened this into a converse: for any compact group, a *linear* layer is equivariant **if and only if** it is a group convolution. Group convolution is therefore not one option among many but the necessary and sufficient form of linear equivariance, which is why equivariant architectures are organized around it and around the irreps that diagonalize it.

**From global symmetry to local gauge.** Classical `G`-CNNs assume a single global symmetry acting the same way everywhere. On a curved domain there is no global frame, and the relevant notion weakens to a *local* gauge symmetry: each point chooses its own frame, and equivariance becomes a constraint relating layers under arbitrary, position-dependent frame changes [[cohen-2019-gauge-cnn]]. The kernel must satisfy a constraint, and features at different points are compared only after [[Parallel transport|parallel transport]] by the connection. The rigorous foundation for this picture is a fiber-bundle / induced-representation (Mackey-theory) account in which equivariant linear maps correspond one-to-one with convolutions by steerable kernels constrained per irrep, classifying `G`-CNNs by symmetry group, base space, and field type [[cohen-2019-general-theory-equivariant]] — the same triple (group, base, field) that grounds the program's per-token `GL(k)` frame-as-fibre and irrep-block decomposition. [[bronstein-2021-geometric-deep-learning]] frames this entire progression — grids, groups, graphs, geodesics, gauges — as one Erlangen-style "symmetry/equivariance blueprint," and it is the blueprint the VFE Transformer instantiates with `GL(k)` gauge frames and symmetry-respecting positional encodings.

**Irreps and Clebsch-Gordan coupling.** When features are decomposed into [[Irreducible representation|irreps]], the equivariance constraint on a linear map factorizes into independent constraints per irrep, giving a reusable steerable basis [[weiler-2019-e2-steerable]]. *Nonlinear* equivariant mixing of features in different irreps is achieved by the tensor product, whose decomposition is governed by the [[Clebsch-Gordan coefficients|Clebsch-Gordan coefficients]]; [[thomas-2018-tensor-field-networks|Tensor Field Networks]] are the canonical template, coupling `SO(3)` irreps via spherical-harmonic filters and the Clebsch-Gordan product. This is the same bookkeeping the project invokes for its irrep-structured blocks and Clebsch-Gordan coupling.

**Lie groups and the algebra-first route.** For a continuous group like `GL(k)`, an efficient path to equivariance is to do all geometry in the **Lie algebra** (logarithmic coordinates) and map back to the group via the exponential. [[finzi-2020-lieconv|LieConv]] builds convolutions equivariant to any Lie group with a surjective exponential map by lifting points to algebra coordinates and recovering elements through `exp`. The VFE Transformer uses exactly this algebra-first parameterization: its gauge degrees of freedom are carried as a Lie-algebra element `phi`, retracted onto the group via a [[Baker-Campbell-Hausdorff formula|Baker-Campbell-Hausdorff]] (BCH) composition. The same algebra-first logic extends to *arbitrary* matrix groups, including the non-compact ones the project actually targets: [[finzi-2021-emlp-arbitrary-matrix-groups]] constructs equivariant layers for any matrix group — `GL(n)`, the Lorentz group `O(1,3)`, `Sp(n)` — by solving the constraint `rho(X) W = W rho(X)` at the Lie-algebra level through a nullspace computation, closing the non-compact-group gap left open by the compact-group results above for `GL(k)`-attention's commutant-restricted per-block maps.

> [!note] Editorial: In practice the model targets *approximate* or *soft* equivariance — `GL(k)` is non-compact and the retraction/optimization are inexact — so equivariance is better read as an inductive bias and a design target than as an exactly enforced identity at every layer.

## In this work

Group equivariance surfaces wherever the configuration commits to a symmetry group and then arranges computation to respect it:

- **`gauge_group: block_glk`.** The declared symmetry is the block general-linear group `GL(k)`; equivariance under it is the property the gauge machinery aims to enforce.
- **Lie-algebra `phi` + BCH retraction.** Gauge elements parameterized in the algebra and composed by BCH realize the [[finzi-2020-lieconv|LieConv]]-style algebra-first construction for a continuous group.
- **Belief transport and holonomy.** Equivariance is what makes [[Parallel transport|parallel transport]] of per-token `(mu, Sigma)` beliefs and the resulting [[Holonomy|holonomy]] coherent, following the gauge-CNN transport rule [[cohen-2019-gauge-cnn]].
- **Irreps and Clebsch-Gordan blocks.** Per-block features organized by [[Irreducible representation|irreps]] and coupled through [[Clebsch-Gordan coefficients|Clebsch-Gordan coefficients]] implement equivariant nonlinear mixing in the spirit of [[thomas-2018-tensor-field-networks]] and [[weiler-2019-e2-steerable]].
- **Symmetry-respecting positional encodings.** The learned positional `phi` composed via BCH is the positional analogue of an equivariant operator, designed so that position information enters without breaking the declared symmetry [[bronstein-2021-geometric-deep-learning]].

## Sources

- [[cohen-2016-gcnn]] — group-equivariant convolution; declaring a symmetry group structures the architecture.
- [[cohen-2019-gauge-cnn]] — generalization from global symmetry to local gauge equivariance, kernel constraint, parallel-transport rule.
- [[cohen-2019-general-theory-equivariant]] — fiber-bundle / induced-representation (Mackey-theory) foundation; equivariant maps as steerable convolutions classified by group, base space, and field type.
- [[weiler-2019-e2-steerable]] — reduction of equivariance constraints to per-irrep constraints; steerable basis.
- [[kondor-2018-compact-group-conv]] — group convolution is necessary and sufficient for linear equivariance under compact groups.
- [[bronstein-2021-geometric-deep-learning]] — Erlangen-style symmetry/equivariance blueprint unifying grids, groups, gauges.
- [[finzi-2020-lieconv]] — Lie-group equivariance via algebra (log) coordinates and `exp`.
- [[finzi-2021-emlp-arbitrary-matrix-groups]] — constructive equivariant layers for arbitrary (including non-compact `GL(n)`, `O(1,3)`, `Sp(n)`) matrix groups via Lie-algebra nullspace solve.
- [[thomas-2018-tensor-field-networks]] — irrep-valued features coupled by the Clebsch-Gordan tensor product.
- [[amari-1998-natural-gradient]], [[ollivier-2015-riemannian-metrics-nn]] — reparameterization-invariant optimization, the dual notion to feature equivariance.
- [[bleecker-1981-gauge-theory-variational-principles]] — canonical bundle-connection-and-variational-principle reference behind the gauge formalism.
- [[fulton-harris-1991-representation-theory]] — irrep classification and Clebsch-Gordan machinery behind `block_glk` gauge and the isotypic head mixers.
- [[cohen-2018-spherical-cnns]] — `SO(3)`-equivariant spherical convolution via irrep/Fourier analysis; geometric-DL sibling of gauge attention.

## See also

- [[Gauge transformation]]
- [[Parallel transport]]
- [[Holonomy]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Group equivariant CNN (G-CNN)]]
- [[Gauge equivariant CNN]]
- [[Steerable CNN]]
- [[LieConv]]
- [[Tensor Field Network]]
- [[Natural gradient]]
- [[Gauge equivariance and geometric deep learning]]
