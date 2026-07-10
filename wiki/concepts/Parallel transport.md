---
type: concept
title: Parallel transport
aliases:
  - Vector transport
  - Connection transport
  - "Gauge transport"
  - "gauge-covariant transport"
  - "Transport Operator"
tags:
  - cluster/gauge-theory
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-09
---

# Parallel transport

## Definition

**Parallel transport** is the rule that moves a tangent vector (or, more generally, an element of a fibre over a manifold) from one point to another *along a chosen path* while keeping it "as constant as possible" with respect to a [[Gauge transformation|connection]]. On a curved manifold there is no canonical way to compare vectors living in tangent spaces at two different points; a connection supplies the missing comparison by prescribing, infinitesimally, how a vector must rotate and stretch to stay parallel as its base point moves. Formally, given a connection with coefficients (a covariant derivative ∇), a vector field V is *parallel-transported* along a curve γ(t) when its covariant derivative along the curve vanishes, ∇_{γ̇} V = 0. Solving this linear ordinary differential equation along γ produces a linear isomorphism between the fibres at the endpoints, the **transport map** P_γ.

The defining property is **path dependence**: transporting a vector around a closed loop generally does not return it unchanged, and the resulting fibre automorphism is the loop's [[Holonomy|holonomy]]. The failure of transport to be path-independent is precisely the curvature of the connection. When the manifold is flat (zero curvature) transport is path-independent and reduces to ordinary translation; when it is curved, transport encodes the geometry.

In the *gauge-theoretic* reading, a manifold is covered by local frames (gauges), each fibre is acted on by a structure group, and parallel transport is the operation that relates feature vectors expressed in one frame to the same features expressed in a neighbouring frame. Changing the local frame is a [[Gauge transformation|gauge transformation]]; transport is the connection-compatible way to carry data between frames so that downstream computations do not depend on the arbitrary local choice. The program's term **gauge transport** names exactly this dynamical use: moving belief/representation vectors between token frames along the connection so that comparisons (attention scores) are made in a common frame and remain covariant under local gauge transformations. It is worth distinguishing from a passive gauge transformation (relabeling the frame): transport carries data *along a path*, accumulating [[Holonomy|holonomy]] when the connection is non-flat, so in gauge-theoretic attention a query-key comparison implicitly transports one token's frame to another's before the inner product. The linear map that effects this — a **transport operator** that intertwines the group action so features transform consistently — generalizes parallel transport; in equivariant deep learning (e.g. the SE(3)-Transformer) it is built from steerable kernels and Wigner-D matrices acting on irreducible-representation features ([[fuchs-2020-se3-transformer]]), the discrete attention-mechanism analogue of gauge parallel transport.

## Why it matters here

The VFE transformer attaches geometric structure to each token: a per-token Gaussian belief with mean μ and a symmetric-positive-definite (SPD) covariance Σ, organised under a block general-linear gauge group GL(k) with a Lie-algebra "phi" parameterization. These per-token objects live in *different local frames*, so to combine them — in precision-weighted attention, in Clebsch–Gordan block coupling, or when composing positional encodings — their representations must be brought into a common frame. Parallel transport is the operation that does this consistently with the declared symmetry, and it is the conceptual bridge connecting three of the project's pillars:

- **Gauge equivariance.** [[Gauge equivariant CNN|Gauge-equivariant networks]] make local-frame choices unobservable by transporting features along the manifold; [[cohen-2019-gauge-cnn]] derives exactly the kernel constraint plus parallel-transport rule that lets a network process data on a manifold without a global frame. The VFE transformer inherits this: its GL(k) gauge frames and the transport of per-token beliefs are the same idea applied to token features rather than pixels on a sphere.
- **SPD-manifold geometry.** Because Σ lives on the curved SPD cone, "moving" a covariance or its tangent update from one belief to another is a transport problem. The affine-invariant metric of [[pennec-2006-affine-invariant-tensor]] and the monograph geometry of [[bhatia-2007-positive-definite-matrices]] give the SPD manifold its connection and hence its transport rule, while [[absil-2008-optimization-matrix-manifolds]] supplies *vector transport* as the cheap, retraction-compatible surrogate the model actually uses.
- **Riemannian optimization.** This applies to belief-side manifold updates. The audited frame update has no proven invariant/Fisher metric. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial: The architecture's holonomy/transport vocabulary is best read as the geometric enforcement of frame-independence: any quantity that two tokens must share has to be transported, not naively copied, or the model would silently depend on arbitrary local gauges.

## Details

**Connections and the transport ODE.** A connection ∇ is specified locally by Christoffel-like coefficients Γ. Along a curve γ(t) with velocity γ̇, the parallel-transport equation is the linear system

  d/dt V(t) + Γ(γ(t))(γ̇(t), V(t)) = 0,  V(0) given.

Its solution defines P_{γ, 0→t}, a linear (and, for metric connections, isometric) map between fibres. Two structural facts matter for this project:

1. **Curvature ⇔ holonomy.** The commutator of covariant derivatives is the curvature tensor; integrating it around an infinitesimal loop gives the leading-order [[Holonomy|holonomy]]. Nonzero curvature is the obstruction to a global flat frame.
2. **Metric compatibility.** When the connection preserves a metric, transport preserves inner products, so transported beliefs keep their lengths and angles — essential when transported covariances must remain SPD and transported precisions must remain meaningful.

The monograph of [[weiler-2021-coordinate-independent-cnns]] derives this whole apparatus from first principles, showing that requiring coordinate-independence together with weight-sharing *forces* local-gauge equivariance and yields textbook-grade statements of the transport rule and the cocycle/holonomy conditions the project leans on.

**Lie-group and gauge picture.** When the structure group is a Lie group G (here the block general-linear group GL(k)), transport along a path is an element of G obtained by integrating a Lie-algebra-valued connection. The model parameterizes group elements in the algebra via "phi" and maps them to the group with the exponential — the same algebra-first strategy [[finzi-2020-lieconv]] uses for general Lie groups and [[thomas-2018-tensor-field-networks]] uses for SO(3). A truncated [[Baker-Campbell-Hausdorff formula|Baker–Campbell-Hausdorff]] (BCH) composition appears in specific algebra-coordinate composition routines. The `retract_phi` dispatcher belongs only to optional in-E-step frame revision; neither outer optimizer calls it, and both outer routes take additive coordinate steps. The Erlangen-Program synthesis of [[bronstein-2021-geometric-deep-learning]] frames grids, groups, and gauges under exactly this transport-and-equivariance blueprint, and [[cohen-2016-gcnn]] is its discrete-group ancestor. The fiber-bundle / induced-representation (Mackey-theory) foundation of [[cohen-2019-general-theory-equivariant]] makes the bookkeeping rigorous, putting equivariant linear maps in one-to-one correspondence with convolutions by steerable kernels constrained per irrep and classifying G-CNNs by symmetry group, base space, and field type — the same frame-as-fiber and irrep-block decomposition the project's per-token GL(k) construction uses. [[gl-k-attention-2026-07-09-review-revision]]

**Exact transport vs. vector transport.** Genuine parallel transport requires solving the ODE along a geodesic, which is expensive. [[absil-2008-optimization-matrix-manifolds]] introduces **vector transport**: any smooth map that approximates parallel transport to first order and is compatible with a chosen **retraction** (a cheap surrogate for the exponential map). The VFE transformer's `spd_affine` covariance retraction belongs to this manifold-optimization vocabulary. The optional frame `retract_phi` routine is a separate in-E-step coordinate-composition route; it is not used by either outer frame optimizer and should not be inferred from the existence of BCH elsewhere in the model. [[gl-k-attention-2026-07-09-review-revision]]

**SPD transport variants.** On the SPD cone there are two practical regimes:
- The **affine-invariant** connection of [[pennec-2006-affine-invariant-tensor]] / [[bhatia-2007-positive-definite-matrices]] gives curved, congruence-equivariant geodesics and a transport implemented by a congruence (sandwich) action; this is the geometry behind `spd_affine`.
- The **Log-Euclidean** metric of [[arsigny-2006-log-euclidean]] pushes SPD matrices through the matrix logarithm into a flat vector space where transport is trivial (ordinary translation), trading curvature-faithfulness for speed and commutativity. SPDNet-style layers ([[huang-2017-spdnet]]) and SPD self-attention ([[wang-2023-riemannian-self-attention-spd]]) build on these same SPD geometries.

> [!note] Editorial: The choice between affine-invariant and Log-Euclidean transport is the recurring efficiency/fidelity trade-off in the model's covariance machinery; the `spd_affine` setting commits to the curved, congruence-equivariant variant.

## In this work

Parallel transport surfaces wherever per-token beliefs or gauge-frame quantities must be compared across frames or across optimization steps:

- **Gauge frames and belief transport.** The `gauge_group block_glk` (block GL(k)) declaration means each token's features sit in a local frame; transport carries beliefs between frames so attention and coupling are frame-independent, exactly the construction of [[cohen-2019-gauge-cnn]] and the gauge pillar of [[bronstein-2021-geometric-deep-learning]].
- **Phi coordinates and optional BCH composition.** The Lie-algebra "phi" parameterization realizes group-valued transport after exponentiation. The optional in-E-step frame-revision route composes an algebra step with truncated BCH; the custom outer optimizer and AdamW instead update phi additively. This mirrors the log-coordinate approach of [[finzi-2020-lieconv]] and the irrep/Clebsch–Gordan bookkeeping of [[thomas-2018-tensor-field-networks]] (see [[Clebsch-Gordan coefficients]], [[Irreducible representation]]). [[gl-k-attention-2026-07-09-review-revision]]
- **SPD covariance updates.** The `spd_affine` retraction places Σ on the affine-invariant SPD manifold of [[pennec-2006-affine-invariant-tensor]] and [[bhatia-2007-positive-definite-matrices]]; updating and aggregating covariances (as in [[wang-2023-riemannian-self-attention-spd]]) requires transporting tangent vectors between SPD points.
- **Belief-side transport.** Vector transport can relocate belief-manifold tangent data; no corresponding frame-natural-gradient claim is established. [[gl-k-attention-2026-07-09-review-revision]]
- **Holonomy and cocycles.** Strict Regime-I transport telescopes to $H=I$; path dependence belongs to an edge-relaxed/nonflat connection. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[cohen-2019-gauge-cnn]] — derives the kernel constraint and parallel-transport rule for gauge-equivariant networks on manifolds.
- [[bronstein-2021-geometric-deep-learning]] — situates parallel transport, gauges, and equivariance in a single geometric-deep-learning blueprint.
- [[cohen-2016-gcnn]] — discrete-group ancestor establishing symmetry-structured architectures.
- [[cohen-2019-general-theory-equivariant]] — fiber-bundle / induced-representation foundation classifying G-CNNs by group, base space, and field type, grounding the per-token GL(k) frame-as-fibre and irrep-block decomposition.
- [[weiler-2021-coordinate-independent-cnns]] — monograph deriving gauge equivariance from coordinate-independence plus weight-sharing, with textbook-grade transport-rule and cocycle/holonomy statements.
- [[finzi-2020-lieconv]] — Lie-algebra (log-coordinate) parameterization of group actions, the template for "phi" plus BCH transport.
- [[thomas-2018-tensor-field-networks]] — irrep-valued features transported and coupled via Clebsch–Gordan products.
- [[absil-2008-optimization-matrix-manifolds]] — retractions and vector transport as first-order surrogates for the exponential map and parallel transport.
- [[pennec-2006-affine-invariant-tensor]] — affine-invariant SPD connection underpinning `spd_affine` transport.
- [[bhatia-2007-positive-definite-matrices]] — geodesics, geometric mean, and transport geometry of the SPD cone.
- [[arsigny-2006-log-euclidean]] — flat Log-Euclidean alternative where transport is trivial.
- [[bonnabel-2013-riemannian-sgd]] — Riemannian SGD whose iterate-to-iterate updates rely on transport.
- [[huang-2017-spdnet]] — deep SPD-matrix network grounding tangent-space and transport operations.
- [[wang-2023-riemannian-self-attention-spd]] — SPD-manifold self-attention aggregating transported covariances.
- [[fuchs-2020-se3-transformer]] — SE(3)-equivariant transport operator built from steerable kernels and Wigner-D matrices; the attention-mechanism analogue of gauge parallel transport.

## See also

- [[Gauge transformation]]
- [[Holonomy]]
- [[Group equivariance]]
- [[Gauge equivariant CNN]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Gauge equivariance and geometric deep learning]]
