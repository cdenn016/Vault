---
type: theme
title: Gauge equivariance and geometric deep learning
aliases:
  - Geometric deep learning
  - Gauge-equivariant networks
  - GDL
  - Equivariant neural networks
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-19
---

# Gauge equivariance and geometric deep learning

## The big picture

Geometric deep learning is the program of designing neural architectures whose structure is dictated by the symmetries of the data domain. Rather than treating a network as an arbitrary function approximator and hoping the right invariances are learned, one *declares* a symmetry group and constrains every layer to respect it. The payoff is a sharp inductive bias: weight sharing, sample efficiency, and provable guarantees that the network's output transforms in a known way when its input is transformed. This theme collects the lineage of that idea — from global group symmetry, through compact-group harmonic analysis, to local gauge symmetry on manifolds — and traces how each layer of generality feeds the gauge-theoretic ambition of the [[VFE Transformer Program]], whose [[Gauge transformation|gauge transformations]] act through the block general-linear group GL(k).

The conceptual seed is [[cohen-2016-gcnn]], the [[Group equivariant CNN (G-CNN)]], which generalized the ordinary convolution from translations to larger discrete symmetry groups and proved that the resulting feature maps are *equivariant*: a symmetry acting on the input induces a predictable action on every feature map. This established the foundational slogan of the field — that a declared symmetry group should structure the architecture itself, not merely be hoped for. [[bronstein-2021-geometric-deep-learning]] later elevated this into an Erlangen-Program-style synthesis ("Grids, Groups, Graphs, Geodesics, and Gauges"), recasting CNNs, graph networks, and Transformers as instances of one symmetry/equivariance blueprint, and supplying the gauge, [[Parallel transport]], and [[Group equivariance|equivariance]] scaffolding that motivates the project's symmetry-respecting positional encodings.

The crucial generalization for this research program is the move from *global* to *local* symmetry. Where a global symmetry transforms the whole input coherently, a *gauge* symmetry permits an independent change of reference frame at every point — exactly the freedom one wants when each token carries its own learned coordinate frame. [[cohen-2019-gauge-cnn]] made this precise for CNNs on manifolds, deriving the kernel constraint and the parallel-transport rule that govern how features must be carried between neighboring frames. That parallel-transport rule is the geometric heart of why per-token beliefs in the VFE transformer must be *transported*, not merely compared, before they interact.

> [!note] Editorial: The defining design choice of this research program is to read the per-token belief frame as a fiber over the token, with GL(k) as the structure group. Under that reading, "attention between tokens" is literally the comparison of objects living in different fibers, which is ill-defined until a connection supplies parallel transport — exactly the apparatus geometric deep learning was built to provide.

## Key threads

**From global groups to compact-group harmonic analysis.** [[cohen-2016-gcnn]] handled discrete groups by enumeration. [[kondor-2018-compact-group-conv]] supplied the deep theorem: using representation theory and harmonic analysis, group convolution is *necessary and sufficient* for a linear layer to be equivariant under any compact group, and admissible operations are organized by [[Irreducible representation|irreducible representations]] (irreps). This licenses the project's irrep-structured, group-equivariant attention — the claim that equivariant linear maps are not a design choice but the only option, and that they decompose along irreps. [[cohen-2019-general-theory-equivariant]] gives this its most rigorous footing, placing the whole construction on a fiber-bundle and induced-representation (Mackey-theory) foundation in which equivariant linear maps correspond one-to-one with convolutions by steerable kernels constrained per irrep, classifying G-CNNs by symmetry group, base space, and field type — the bundle-theoretic grounding for the program's per-token GL(k) frame-as-fibre and irrep-block decomposition. [[weiler-2019-e2-steerable]] turned this into engineering: for the Euclidean group E(2), arbitrary representation-level kernel constraints reduce to *per-irrep* constraints, yielding a reusable irrep-indexed steerable basis. This is directly the bookkeeping the VFE transformer needs for its irreps and [[Clebsch-Gordan coefficients|Clebsch-Gordan]] block coupling.

**Irreps and Clebsch-Gordan coupling.** [[thomas-2018-tensor-field-networks]] is the canonical template here. Tensor Field Networks build SO(3)-equivariant layers whose features *live in irreps* and are coupled through spherical-harmonic filters and the Clebsch-Gordan tensor product — the rule that tells you how the product of two irreps decomposes back into irreps. The VFE transformer borrows this exact machinery for its irrep bookkeeping and Clebsch-Gordan coupling: when two gauge-structured features interact, their tensor product is re-expressed in the irrep basis, keeping the whole computation equivariant by construction.

**Lie-algebra-first parameterization.** LieConv's own result assumes a surjective exponential map. Real matrix exponentiation is not surjective onto $\mathrm{GL}^+(K)$, so the transformer's single real chart realizes only $\operatorname{image}(\exp)$. Finite BCH composition is local and approximate; exact ambient covariance of the score does not make this realized chart globally complete. [[gl-k-attention-2026-07-09-review-revision]]

**Local gauge symmetry and transport.** [[cohen-2019-gauge-cnn]] is the load-bearing source for the program's central metaphor. Once features carry a local frame, comparing features at different locations requires a connection, and the connection furnishes [[Parallel transport]] and, around closed loops, [[Holonomy]]. The VFE transformer reuses this to transport per-token Gaussian beliefs between tokens before they are compared in attention, so that the comparison is frame-independent. [[weiler-2021-coordinate-independent-cnns]] derives this same apparatus from first principles in monograph form, showing that requiring coordinate-independence together with weight-sharing *forces* local-gauge equivariance, and supplying the full G-structure, parallel-transport, and holonomy bookkeeping — the textbook-grade statements of the transport rule and the cocycle/holonomy conditions the program leans on. [[bronstein-2021-geometric-deep-learning]] frames the whole apparatus — frames, transport, holonomy — as a unifying vocabulary across architectures, which is why it serves as the conceptual anchor connecting this theme to attention and positional structure.

## How it lands in this work

The MAgent exact-ELBO construction now types continuum bundle fields and finite realizations separately. Sampling a supplied section on a finite design is not the same operation as marginalizing a correlated finite recognition law, although an explicit compatibility hypothesis can identify their outputs at the design points. Finite site variables alone are not a lattice gauge theory: a genuine lattice construction also declares an interaction complex, group-valued links on oriented edges, and two-cells or plaquettes. No continuum reconstruction or continuum-limit theorem follows merely from the finite ELBO. [[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]]

The architecture uses block-$\mathrm{GL}(K)$ frames to transport Gaussian beliefs. The full-Gaussian divergence is exactly invariant under common invertible pushforwards, but the live diagonal family is closed only under monomial congruences and otherwise requires projection. Regime-I vertex transport has exact trivial holonomy. [[gl-k-attention-2026-07-09-review-revision]]

The audited width sweep also uses an identity-initialized post-belief head remap at every $K\geq20$; $K=10$ has no mixer. For the live untied product action $\mathrm{GL}(10)^H$, an off-diagonal $H\times H$ remap does not commute with independent per-head gauges and is therefore not gauge-equivariant. It becomes a Schur-commutant intertwiner only under a gauge tied across equivalent head copies. In the one-layer linear-decode path the map is absorbable into the output projection as a function-class statement, but no matched mixer-off control isolates its optimization effect. [[gl-k-attention-2026-07-09-review-revision]]

Full-SPD covariance geometry and Gaussian belief natural gradients remain valid. The frame conditioner is separate: the positive Frobenius/Cartan form is not full-$\mathrm{GL}(K)$ adjoint-invariant or Fisher, and its exponential-coordinate pullback is extrinsic and only locally positive definite where $D\exp$ has full rank. [[gl-k-attention-2026-07-09-review-revision]]

## Open questions / gaps

The active MAgent frame optimizer does not yet support the manuscript's full common-right $\mathrm{GL}^+(K)$ trajectory claim. Scalar Gaussian-KL invariance under a common pushforward remains valid, but the reached Frobenius body-covector update transforms under a different law from the one required by right-orbit equivariance for generic nonorthogonal gauge changes. The open design choice is whether to restrict the admitted symmetry, state a gauge fixing, or replace the update with a proved right-equivariant rule. [[participatory-it-from-bit-2026-07-11-code-concordance-review]]

Hierarchical closure creates a second domain problem. Legal bounded products of exponential frame increments can reach well-conditioned elements of $\mathrm{GL}^+(K)$ for which no real logarithm exists, while the current coarse-frame construction requires `matrix_log_principal`. A group-level construction that avoids a global logarithm, or an invariant restriction to a log-safe domain, is required before the formal frame group and executable hierarchy have the same domain. [[participatory-it-from-bit-2026-07-11-code-concordance-review]]

The main realized-family gap is exact: a single real exponential chart misses part of $\mathrm{GL}^+(K)$. Stored group elements (`omega_direct`) or multiple-chart constructions can cover transformations that the phi chart cannot. This is separate from LieConv's valid theorem under its own surjectivity premise. [[gl-k-attention-2026-07-09-review-revision]]

Holonomy is closed in strict Regime I: $\Omega_{ij}=U_iU_j^{-1}$ telescopes around every loop. The open holonomy question belongs to independent-edge or otherwise nonflat transport, not stacked vertex-cocycle attention. [[gl-k-attention-2026-07-09-review-revision]]

## Sources synthesized

- [[participatory-it-from-bit-2026-07-11-code-concordance-review]] — MAgent/PIFB2 code-concordance review of optimizer equivariance and the frame-log domain of hierarchical pooling.

- [[cohen-2016-gcnn]] — Group Equivariant Convolutional Networks: the founding statement that a declared symmetry group structures the architecture and yields provable [[Group equivariance]].
- [[cohen-2019-gauge-cnn]] — Gauge Equivariant CNNs and the Icosahedral CNN: the move from global to local symmetry, with the kernel constraint and [[Parallel transport]] rule underpinning the project's gauge frames.
- [[weiler-2019-e2-steerable]] — General E(2)-Equivariant Steerable CNNs: reduction of kernel constraints to per-[[Irreducible representation|irrep]] constraints, giving a reusable steerable basis.
- [[kondor-2018-compact-group-conv]] — Equivariance and Convolution for Compact Groups: proof that group convolution is necessary and sufficient for linear equivariance, organized by irreps.
- [[bronstein-2021-geometric-deep-learning]] — Geometric Deep Learning (Grids, Groups, Graphs, Geodesics, Gauges): the Erlangen-Program synthesis unifying CNNs, GNNs, and Transformers under one equivariance blueprint.
- [[finzi-2020-lieconv]] — LieConv: Lie-algebra-first, exponential-map parameterization of equivariance to arbitrary Lie groups, the template for the GL(k) phi.
- [[thomas-2018-tensor-field-networks]] — Tensor Field Networks: irrep-valued features coupled by the [[Clebsch-Gordan coefficients|Clebsch-Gordan]] tensor product, the canonical template for the project's irrep bookkeeping.
- [[cohen-2019-general-theory-equivariant]] — A General Theory of Equivariant CNNs on Homogeneous Spaces: fiber-bundle / induced-representation (Mackey-theory) foundation classifying G-CNNs by group, base space, and field type, grounding the frame-as-fibre and irrep-block decomposition.
- [[finzi-2021-emlp-arbitrary-matrix-groups]] — A Practical Method for Constructing Equivariant MLPs for Arbitrary Matrix Groups: Lie-algebra nullspace construction of layers equivariant to arbitrary (including non-compact) matrix groups, addressing the GL(k) non-compactness gap.
- [[weiler-2021-coordinate-independent-cnns]] — Coordinate Independent Convolutional Networks: monograph deriving gauge equivariance from coordinate-independence plus weight-sharing, with the transport and cocycle/holonomy bookkeeping the program leans on.

### Related sources

- [[bleecker-1981-gauge-theory-variational-principles]] — Canonical bundle-connection-and-variational-principle reference behind the gauge formalism.
- [[fulton-harris-1991-representation-theory]] — Irrep classification and Clebsch-Gordan machinery behind `block_glk` gauge and isotypic head mixers.
- [[steinberg-2012-representation-theory-finite-groups]] — Finite-group irrep/character theory behind the model's isotypic head mixers and CG coupling.
- [[cohen-2018-spherical-cnns]] — SO(3)-equivariant spherical convolution via irrep/Fourier analysis; geometric-DL sibling of gauge attention.

Cross-cluster anchors: [[SPD-manifold geometry and Riemannian optimization]] ([[absil-2008-optimization-matrix-manifolds]]), [[Information geometry and natural gradient]] ([[ollivier-2015-riemannian-metrics-nn]], [[Natural gradient]]), and [[Attention mechanisms — theory and positional structure]] ([[vaswani-2017-attention]]).
