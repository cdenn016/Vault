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
updated: 2026-10-27
---

# Gauge equivariance and geometric deep learning

## Learned frames tested against capacity, October 26, 2026

The first registered test of whether the VFE transformer's per-token frames do work beyond their parameter count is [[vfe3-2026-10-26-paper-arms]]. Learned $GL(K)$ frames beat identity frames by 0.212 nats, random frozen frames by 0.207, and an equal-size additive per-type table by 0.154, so the frame fibre carries learned structure that neither random group elements nor additive capacity reproduce. Whether the group structure itself matters, as opposed to any learned per-type multiplicative map, is still open; see [[GL(K) gauge-equivariant attention]].

## Prior readings of attention as a sheaf, connection or gauge theory, October 6, 2026

Five sources bound what the GL(K) program can call new in reading attention geometrically. Graph networks with linear edge maps: [[barbero-2022-sheaf-attention-networks]] (abstract only) generalizes graph attention to cellular sheaves, and [[barbero-2022-sheaf-neural-networks-connection-laplacians]] with [[bodnar-2022-neural-sheaf-diffusion]] give sheaf diffusion with orthogonal restriction maps, a discrete $O(d)$-bundle whose Laplacian is the connection Laplacian; all are node-classification graph networks with no probabilistic fibers and no reading of a token transformer. Analogy for transformers: [[disipio-2025-curved-spacetime-transformers]] calls the operator $W_O\hat\alpha_{ij}W_V$ a discrete connection by analogy with general relativity and measures the turning angle of layerwise token trajectories as a curvature proxy, with no group, frame or holonomy. Gauge theory of inference: [[sengupta2017gauge]], already in the vault, is the closest conceptual precursor, a gauge theory of variational inference with parallel transport of sufficient statistics on a statistical manifold, but its attention is neuronal precision weighting, not transformer attention. In the opposite direction, [[favoni-2022-lattice-gauge-equivariant-cnns]] and [[nagai-2025-cask]] run networks on lattice gauge fields ([[Lattice gauge theory]]), and [[cassel-2025-bundle-scale-spaces]] and [[cassel-2025-yang-mills-data]] build locally gauge-equivariant graph architectures from discrete vector bundles. Of these, only [[disipio-2025-curved-spacetime-transformers]] addresses transformers directly, and only by analogy.

> [!note] Editorial: This is the vault's reading of the abstracts and the parts of each paper read (each note records its read status), from a brief search with no adversarial check. That none of them defines frames in a principal $\mathrm{GL}(K)$-bundle with Gaussian statistical fibers and group-valued links for token transformers is the reading of the October 5 rework ([[dennis-2026-glk-attention-v2-rework-2026-10-05]]), not a verified priority claim.

## Exponential links as charts of the content maps, October 4, 2026

[[dennis-2026-glk-lie-algebra-links-v2]] gives the static form of the frame-dressed links a concrete place in a trained architecture. For the shared low-rank generator built from the value and output maps, the exponential link splits exactly into the flat identification and a selective channel whose first-order part is the familiar multi-head value path, and the linear and exponential links are an exact change of coordinates on the principal-logarithm domain. The equivariance is the same in every chart: costs are invariant and messages covariant under passive frame changes, because every chart uses the content maps only through an effective receiving map. What the chart changes is the group domain and the optimization geometry, not the function class. Group-valued links also supply inverse edges, so causal attention graphs, which contain no directed cycles through distinct positions, acquire triangle holonomies ([[Holonomy]]).

## Dynamic link fields, October 3, 2026

The attention links of the program are frame-dressed, $\Theta_{ij}=U_ie^{X_{ij}}U_j^{-1}$, so the generator $X_{ij}$ is reference data and the passive gauge action never touches it. [[dennis-2026-dynamic-links]] uses this to make the links dynamic within a variational model rather than through an imposed equivariance constraint. The generators become latent variables with a normalized prior, and their evolution is inference. Two points matter for the geometric-deep-learning picture. First, curvature on a non-compact structure group cannot be measured by conjugation-invariant functions, which miss unipotent holonomy; the frames supply a reference metric under which the Frobenius defect of the holonomy is gauge invariant and separating. Second, the curvature energy is either a declared prior or, for undirected Gaussian matter, induced by integrating out the states, with Wilson's action at leading order ([[Lattice gauge theory]]).

## Dressed frames, $\{e\}$-structures and sheaves, September 23, 2026

The v2 revision of the GL(K) attention manuscript separates two kinds of frame covariance. In gauge-equivariant CNNs ([[cohen-2019-gauge-cnn]], [[weiler-2021-coordinate-independent-cnns]]) the frame is geometric data defined only up to the structure group, and weight sharing forces the shared kernels to be intertwiners. In the attention construction the frames $U_i$ are learned. They fix an $\{e\}$-structure, a global frame field ([[weiler-2021-coordinate-independent-cnns]], Sections 2.1.1 and 3.1.3), and act as a local dressing field in the sense of [[fournel-2014-gauge-invariant-composite-fields]]. By criterion (C1) of [[francois-2019-artificial-gauge-symmetries]] the resulting covariance is artificial, the kind Kretschmann called physically vacuous ([[norton-1993-general-covariance]]), and it constrains none of the learned maps. [[Dressing field method]] records the construction.

For the matrix links, the comparison cospan $E_i\to H^{\mathrm{cmp}}\leftarrow E_j$ is a pair of restriction maps into an edge stalk, which is the data of a cellular sheaf ([[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]]). [[bodnar-2022-neural-sheaf-diffusion]] learns such restriction maps from node features and identifies sheaves with orthogonal restriction maps as discrete $O(d)$ bundles whose Laplacian is the connection Laplacian ([[Graph synchronization and connection Laplacians]]). The revision therefore treats sheaves, rather than [[Lattice gauge theory]], as the closer counterpart of its links.

## Gaussian agents and matrix communication links, September 20, 2026

[[dennis-2026-glk-matrix-links-2026-09-20]] connects full Gaussian site states to learned sending and receiving maps through $L_{ij}^{(h)}=U_iO_hT_hU_j^{-1}$. Covariance follows from transforming the endpoint maps as geometric data, rather than assuming a fixed rectangular numerical matrix intertwines arbitrary local actions. This gives a constrained matrix-link family even when individual heads lose rank. The flat vertex-frame transport and the communication operator are distinct objects.

[[wetterich-2014-linear-lattice-gauge-theory]] supplies the general-matrix-link precedent. The attention manuscript supplies its own GL(K) algebra and explicitly retains the action, global normalization, and dynamics as further obligations. [[GL(K) gauge-equivariant attention]], [[Lattice gauge theory]], and [[Holonomy]] record the construction and path restrictions. An MLP theory remains unresolved; no full-stack equivariance or common-free-energy descent follows.


## The big picture

Geometric deep learning is the program of designing neural architectures whose structure is dictated by the symmetries of the data domain. Rather than treating a network as an arbitrary function approximator and hoping the right invariances are learned, one *declares* a symmetry group and constrains every layer to respect it. The payoff is a sharp inductive bias: weight sharing, sample efficiency, and provable guarantees that the network's output transforms in a known way when its input is transformed. This theme collects the lineage of that idea — from global group symmetry, through compact-group harmonic analysis, to local gauge symmetry on manifolds — and traces how each layer of generality feeds the gauge-theoretic ambition of the [[VFE Transformer Program]], whose [[Gauge transformation|gauge transformations]] act through the block general-linear group GL(k).

The conceptual seed is [[cohen-2016-gcnn]], the [[Group equivariant CNN (G-CNN)]], which generalized the ordinary convolution from translations to larger discrete symmetry groups and proved that the resulting feature maps are *equivariant*: a symmetry acting on the input induces a predictable action on every feature map. This established the foundational slogan of the field — that a declared symmetry group should structure the architecture itself, not merely be hoped for. [[bronstein-2021-geometric-deep-learning]] later elevated this into an Erlangen-Program-style synthesis ("Grids, Groups, Graphs, Geodesics, and Gauges"), recasting CNNs, graph networks, and Transformers as instances of one symmetry/equivariance blueprint, and supplying the gauge, [[Parallel transport]], and [[Group equivariance|equivariance]] scaffolding that motivates the project's symmetry-respecting positional encodings.

The crucial generalization for this research program is the move from *global* to *local* symmetry. Where a global symmetry transforms the whole input coherently, a *gauge* symmetry permits an independent change of reference frame at every point — exactly the freedom one wants when each token carries its own learned coordinate frame. [[cohen-2019-gauge-cnn]] made this precise for CNNs on manifolds, deriving the kernel constraint and the parallel-transport rule that govern how features must be carried between neighboring frames. That parallel-transport rule is the geometric heart of why per-token beliefs in the VFE transformer must be *transported*, not merely compared, before they interact.

> [!note] Editorial: The defining design choice of this research program is to read the per-token belief frame as a fiber over the token, with GL(k) as the structure group. Under that reading, "attention between tokens" is literally the comparison of objects living in different fibers, which is ill-defined until a connection supplies parallel transport — exactly the apparatus geometric deep learning was built to provide.

There is one further step past Cohen and Weiler that this theme long left implicit: what happens when the fiber is not a vector space carrying a linear representation but a *space of probability distributions*. That is the bridge from the gauge-CNN literature above to [[Information geometry and natural gradient|information geometry]], and the Heidelberg group of Schnörr and collaborators has been building both ends of it — [[Sigma flow|sigma flows]] on the information-geometric side, [[Bundle scale space|bundle scale spaces]] and discrete Yang–Mills on the gauge side. The section *Statistical fibers meet local gauge* below records what can be imported from that work and where this program's construction genuinely differs.

## Key threads

**From global groups to compact-group harmonic analysis.** [[cohen-2016-gcnn]] handled discrete groups by enumeration. [[kondor-2018-compact-group-conv]] supplied the deep theorem: using representation theory and harmonic analysis, group convolution is *necessary and sufficient* for a linear layer to be equivariant under any compact group, and admissible operations are organized by [[Irreducible representation|irreducible representations]] (irreps). This licenses the project's irrep-structured, group-equivariant attention — the claim that equivariant linear maps are not a design choice but the only option, and that they decompose along irreps. [[cohen-2019-general-theory-equivariant]] gives this its most rigorous footing, placing the whole construction on a fiber-bundle and induced-representation (Mackey-theory) foundation in which equivariant linear maps correspond one-to-one with convolutions by steerable kernels constrained per irrep, classifying G-CNNs by symmetry group, base space, and field type — the bundle-theoretic grounding for the program's per-token GL(k) frame-as-fibre and irrep-block decomposition. [[weiler-2019-e2-steerable]] turned this into engineering: for the Euclidean group E(2), arbitrary representation-level kernel constraints reduce to *per-irrep* constraints, yielding a reusable irrep-indexed steerable basis. This is directly the bookkeeping the VFE transformer needs for its irreps and [[Clebsch-Gordan coefficients|Clebsch-Gordan]] block coupling.

**Irreps and Clebsch-Gordan coupling.** [[thomas-2018-tensor-field-networks]] is the canonical template here. Tensor Field Networks build SO(3)-equivariant layers whose features *live in irreps* and are coupled through spherical-harmonic filters and the Clebsch-Gordan tensor product — the rule that tells you how the product of two irreps decomposes back into irreps. The VFE transformer borrows this exact machinery for its irrep bookkeeping and Clebsch-Gordan coupling: when two gauge-structured features interact, their tensor product is re-expressed in the irrep basis, keeping the whole computation equivariant by construction.

**Lie-algebra-first parameterization.** LieConv's own result assumes a surjective exponential map. Real matrix exponentiation is not surjective onto $\mathrm{GL}^+(K)$, so the transformer's single real chart realizes only $\operatorname{image}(\exp)$. Finite BCH composition is local and approximate; exact ambient covariance of the score does not make this realized chart globally complete.

**Local gauge symmetry and transport.** [[cohen-2019-gauge-cnn]] is the load-bearing source for the program's central metaphor. Once features carry a local frame, comparing features at different locations requires a connection, and the connection furnishes [[Parallel transport]] and, around closed loops, [[Holonomy]]. The VFE transformer reuses this to transport per-token Gaussian beliefs between tokens before they are compared in attention, so that the comparison is frame-independent. [[weiler-2021-coordinate-independent-cnns]] derives this same apparatus from first principles in monograph form, showing that requiring coordinate-independence together with weight-sharing *forces* local-gauge equivariance, and supplying the full G-structure, parallel-transport, and holonomy bookkeeping — the textbook-grade statements of the transport rule and the cocycle/holonomy conditions the program leans on. [[bronstein-2021-geometric-deep-learning]] frames the whole apparatus — frames, transport, holonomy — as a unifying vocabulary across architectures, which is why it serves as the conceptual anchor connecting this theme to attention and positional structure.

## How it lands in this work

The MAgent exact-ELBO construction now types continuum bundle fields and finite realizations separately. Sampling a supplied section on a finite design is not the same operation as marginalizing a correlated finite recognition law, although an explicit compatibility hypothesis can identify their outputs at the design points. Finite site variables alone are not a lattice gauge theory: a genuine lattice construction also declares an interaction complex, group-valued links on oriented edges, and two-cells or plaquettes. No continuum reconstruction or continuum-limit theorem follows merely from the finite ELBO.

The architecture uses block-$\mathrm{GL}(K)$ frames to transport Gaussian beliefs. The full-Gaussian divergence is exactly invariant under common invertible pushforwards, but the live diagonal family is closed only under monomial congruences and otherwise requires projection. Regime-I vertex transport has exact trivial holonomy.

For an identity-initialized post-belief head remap under the live untied product action $\mathrm{GL}(10)^H$, an off-diagonal $H\times H$ remap does not commute with independent per-head gauges and is therefore not gauge-equivariant. It becomes a Schur-commutant intertwiner only under a gauge tied across equivalent head copies. In the one-layer linear-decode path the map is absorbable into the output projection as a function-class statement, but no matched mixer-off control isolates its optimization effect.

Full-SPD covariance geometry and Gaussian belief natural gradients remain valid. The frame conditioner is separate: the positive Frobenius/Cartan form is not full-$\mathrm{GL}(K)$ adjoint-invariant or Fisher, and its exponential-coordinate pullback is extrinsic and only locally positive definite where $D\exp$ has full rank.

## Open questions / gaps

The active MAgent frame optimizer does not yet support the manuscript's full common-right $\mathrm{GL}^+(K)$ trajectory claim. Scalar Gaussian-KL invariance under a common pushforward remains valid, but the reached Frobenius body-covector update transforms under a different law from the one required by right-orbit equivariance for generic nonorthogonal gauge changes. The open design choice is whether to restrict the admitted symmetry, state a gauge fixing, or replace the update with a proved right-equivariant rule.

Hierarchical closure creates a second domain problem. Legal bounded products of exponential frame increments can reach well-conditioned elements of $\mathrm{GL}^+(K)$ for which no real logarithm exists, while the current coarse-frame construction requires `matrix_log_principal`. A group-level construction that avoids a global logarithm, or an invariant restriction to a log-safe domain, is required before the formal frame group and executable hierarchy have the same domain.

The main realized-family gap is exact: a single real exponential chart misses part of $\mathrm{GL}^+(K)$. Stored group elements (`omega_direct`) or multiple-chart constructions can cover transformations that the phi chart cannot. This is separate from LieConv's valid theorem under its own surjectivity premise.

Holonomy is closed in strict Regime I: $\Omega_{ij}=U_iU_j^{-1}$ telescopes around every loop. The open holonomy question belongs to independent-edge or otherwise nonflat transport, not stacked vertex-cocycle attention.

## Synchronization and variational gauge boundaries (2026-08-10)

[[ahn-2017-gauging-variational-inference]] uses factor reparameterizations to improve a
graphical-model variational approximation. That is a useful algorithmic analogy, but it is not automatically
the passive principal-bundle gauge of the MultiAgentELBO theory. [[gao-2021-synchronization-geometry]]
connects synchronization, flat bundles, and holonomy; [[singer-2012-vector-diffusion-maps]] and
[[bandeira-2013-connection-cheeger]] supply spectral connection-Laplacian diagnostics under their
orthogonal or compact hypotheses.

Those spectral guarantees do not transfer directly to noncompact `GL^+(2)` links. A project
application first needs a declared fiber metric and proofs of self-adjointness,
positive-semidefiniteness, and the relevant comparison inequality. Link synchronizability also
remains distinct from operational belief agreement. [[gerdes-2025-trivializing-flows-lattice-gauge]]
is a future equivariant sampling comparator for compact lattice groups, not a ready-made sampler for
the project's noncompact group.

## Statistical fibers meet local gauge — the Heidelberg programme (2026-08-12)

The gauge-CNN lineage above ends at vector-space fibers: features transform under a linear
representation, and the whole theory of steerable kernels is a theory of intertwiners between
representations. The program pursued here takes a different fiber — a
[[Statistical manifold|statistical manifold]] of Gaussian laws — and asks for the same local-frame
apparatus on top of it. Until now this theme had no external comparator for that combination. It
now has one, and it is close.

**What the four papers contain.** [[cassel-2024-sigma-flows]] introduces the
[[Sigma flow|sigma flow]]: the Riemannian gradient flow of a generalized harmonic energy, whose
stationary points are [[Harmonic map|harmonic maps]] from a closed Riemannian domain manifold into
the open probability simplex carrying the Fisher–Rao metric. Its distinctive ingredient is that the
*domain* metric depends on the evolving state and is realized by a compact, time-variant
parametrization learned from data; geometric integration of the flow produces a network, and the
paper draws explicit structural comparisons to transformer architectures. Its discrete precursor is
the [[Assignment flow|assignment flow]], extended in
[[gonzalez-alvarado-2025-patch-assignment]] to patch dictionaries with an action-functional
characterization. On the other side, [[cassel-2025-bundle-scale-spaces]] models node features as
sections of associated vector bundles, equivariant under *local* actions of a general group $G$, and
defines a diffusion whose non-trivial fixed points are harmonic sections of the bundle — in explicit
contrast to Gaussian scale space, whose only fixed points are constants. [[cassel-2025-yang-mills-data]]
supplies the full finite-graph apparatus underneath: discrete vector bundles, graph voltages as
discretized gauge fields, gauged Laplacians and their heat kernels (closely related to, but
distinguished from, graph connection Laplacians), an axiomatic characterization of those kernels
among all gauge-invariant node-feature transformations, a spanning-tree nullspace theorem, and a
**discrete Yang–Mills energy** whose holonomy-based curvature certifies synchronizability.

**What is importable rather than re-derivable.** Four things. (i) The smooth-to-discrete appendix of
[[cassel-2025-yang-mills-data]] — graph voltages obtained from parallel transport, discrete
Laplacians obtained from covariant derivatives — is exactly the bridge this theme's *How it lands in
this work* section says a finite construction owes before it can call itself a lattice gauge theory.
(ii) The axiomatic characterization is a uniqueness argument for the gauge-covariant diffusion
vertex, i.e. a principled answer to "why *this* covariant Dirichlet term". (iii) The
Yang–Mills-energy-as-synchronizability-certificate result is a ready-made diagnostic for the
curvature regularizers described in [[Non-flat connection and the photon analogy]], and connects
directly to the material already recorded on
[[Graph synchronization and connection Laplacians]]. (iv) The harmonic-section fixed-point statement
tells you what a gauge-covariant smoothing term actually converges to, which is not obvious and is
not "the constant field".

**Where this program genuinely differs.** The sigma flow has a statistical-manifold target but **no
principal bundle, no gauge group, no connection, and no curvature term**; the map is a plain map,
not a section, and there is no local frame freedom to transport. The bundle papers have a genuine
local gauge structure but **vector-space fibers**, not statistical ones, and their gauge field is a
voltage to be analysed or parametrized rather than a dynamical connection co-optimized inside an
inference objective. Neither side has a variational free energy: there is no likelihood, no
accuracy/complexity decomposition, no population of agents with overlapping supports, and no
local/global free-energy split. Finally, the concrete machinery is developed for $\mathrm{SO}(d)$,
a compact group — the caveat already recorded on
[[Graph synchronization and connection Laplacians]] about noncompact $\mathrm{GL}^{+}$ links applies
unchanged.

**And what is honestly missing on their side too.** [[cassel-2024-sigma-flows]] states in §1.3 that
its setting violates the standing assumptions of the harmonic-map literature — the target is open,
has positive sectional curvature, and carries a non-metric affine connection — and therefore leaves
existence and global convergence of the gradient flow to future work, proving only a Lyapunov
decrease. This is a real gap, not a technicality, and it should not be cited as well-posedness.

> [!note] Editorial: The framing "this group holds the statistical-fiber half and the local-gauge
> half in separate papers, and has not yet combined them" is the vault's own reading across the four
> sources. The papers cite one another and
> [[gonzalez-alvarado-2025-patch-assignment]] points forward to bundle scale spaces as the next
> step, but none of them states the combination as an achieved result, and none mentions variational
> free energy.

## Sources synthesized

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
- [[cassel-2025-bundle-scale-spaces]] — Bundle Scale Spaces: node features as sections of associated vector bundles, locally $G$-equivariant architectures by construction, generalized-Laplacian diffusion with harmonic sections as non-trivial fixed points.
- [[cassel-2025-yang-mills-data]] — Yang-Mills Meets Data: discrete vector bundles, graph voltages, gauged Laplacians / heat kernels with an axiomatic characterization, and a discrete Yang–Mills energy certifying synchronizability (for $\mathrm{SO}(d)$).
- [[cassel-2024-sigma-flows]] — Sigma Flows: Riemannian gradient flow of a generalized harmonic energy giving harmonic maps into the Fisher–Rao simplex, with a learnable state-dependent domain metric; existence and global convergence explicitly left open.
- [[gonzalez-alvarado-2025-patch-assignment]] — Riemannian Patch Assignment Gradient Flows: the discrete assignment-flow precursor, with label-interaction dictionaries and a Lagrangian action-functional characterization.
- [[fournel-2014-gauge-invariant-composite-fields]] — Gauge Invariant Composite Fields out of Connections: the Main Lemma of the dressing field method.
- [[francois-2019-artificial-gauge-symmetries]] — Artificial versus Substantial Gauge Symmetries: a local dressing field signals an artificial symmetry (criterion C1).
- [[norton-1993-general-covariance]] — the Kretschmann objection and eight decades of dispute over general covariance.
- [[bodnar-2022-neural-sheaf-diffusion]] — Neural Sheaf Diffusion: learned restriction maps of cellular sheaves on graphs.
- [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]] — spectral theory of cellular sheaf Laplacians.
- [[barbero-2022-sheaf-neural-networks-connection-laplacians]] — precomputed orthogonal sheaf from local PCA and SVD alignment (Conn-NSD).
- [[barbero-2022-sheaf-attention-networks]] — Sheaf Attention Networks: attention-based graph networks on cellular sheaves (abstract only).
- [[disipio-2025-curved-spacetime-transformers]] — attention as a discrete connection by analogy with general relativity; turning-angle curvature of token trajectories.
- [[favoni-2022-lattice-gauge-equivariant-cnns]] — lattice gauge equivariant CNNs: link-transported convolution and bilinear layers that generate Wilson loops.

### Related sources

- [[Gauge VFE ELBO curriculum]]
- [[bleecker-1981-gauge-theory-variational-principles]] — Canonical bundle-connection-and-variational-principle reference behind the gauge formalism.
- [[fulton-harris-1991-representation-theory]] — Irrep classification and Clebsch-Gordan machinery behind `block_glk` gauge and isotypic head mixers.
- [[steinberg-2012-representation-theory-finite-groups]] — Finite-group irrep/character theory behind the model's isotypic head mixers and CG coupling.
- [[cohen-2018-spherical-cnns]] — SO(3)-equivariant spherical convolution via irrep/Fourier analysis; geometric-DL sibling of gauge attention.

Cross-cluster anchors: [[SPD-manifold geometry and Riemannian optimization]] ([[absil-2008-optimization-matrix-manifolds]]), [[Information geometry and natural gradient]] ([[ollivier-2015-riemannian-metrics-nn]], [[Natural gradient]]), and [[Attention mechanisms — theory and positional structure]] ([[vaswani-2017-attention]]).
