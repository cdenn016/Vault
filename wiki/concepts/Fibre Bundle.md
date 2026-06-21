---
type: concept
title: "Fibre Bundle"
aliases:
  - "fibrebundle"
  - "Fiber Bundle"
  - "fiber bundle"
  - "principal bundle"
  - "associated bundle"
tags:
  - cluster/gauge-theory
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-21
updated: 2026-06-21
---

# Fibre Bundle

## Definition

A **fibre bundle** is a space that, *locally*, looks like a product of two simpler spaces but, *globally*, may be twisted. The data of a (smooth) fibre bundle is a quadruple $(E, B, \pi, F)$ together with a **structure group** $G$:

- **Total space** $E$ — the space being described.
- **Base space** $B$ — a smooth manifold over which $E$ sits; in this program $B$ is the "context / index manifold" $\mathcal{C}$, explicitly *not* spacetime (see [[Agents as fibre-bundle sections]]).
- **Projection** $\pi : E \to B$ — a smooth surjection that collapses $E$ down onto $B$.
- **Fibre** $F$ — the model space attached over each point: $\pi^{-1}(b) \cong F$ for every $b \in B$.
- **Structure group** $G$ — a Lie group acting (effectively) on $F$, which controls how fibres over nearby points are glued.

The defining property is **local triviality**: every point of $B$ has an open neighbourhood $U$ with a diffeomorphism (a *local trivialization*) $\phi_U : \pi^{-1}(U) \xrightarrow{\ \sim\ } U \times F$ that respects the projection. On an overlap $U \cap V$ the two trivializations differ by a **transition function** $g_{UV} : U \cap V \to G$ acting on the fibre, and these must satisfy the **Čech cocycle condition**
$$
g_{UU} = e,\qquad g_{UV}\,g_{VU} = e,\qquad g_{UV}\,g_{VW} = g_{UW},
$$
which is exactly what allows the local pieces $U \times F$ to be patched into a single consistent global space $E$. A bundle is **trivial** when one global trivialization $E \cong B \times F$ exists; the cocycle is precisely the obstruction to global triviality. This bundle-theoretic language is the standard coordinate-free formalism of [[kobayashi-nomizu-1963-foundations]] and the physics-oriented treatments of [[nakahara-2003-geometry-topology-physics]] and [[bleecker-1981-gauge-theory-variational-principles]].

A **section** is a smooth right inverse $s : B \to E$ with $\pi \circ s = \mathrm{id}_B$ — a consistent choice of one point in each fibre. Sections are the natural notion of a "field": this is the precise sense in which the program treats agents/beliefs as fields, developed in [[Agents as fibre-bundle sections]] (each belief $q_i$ is a section of an associated statistical bundle). The smooth-manifold and section machinery underlying all of this is standard ([[lee-2012-smooth-manifolds]]).

## Principal vs. associated bundles

Two specializations carry the whole gauge-theoretic load.

A **principal $G$-bundle** $P(B, G)$ is a fibre bundle whose fibre *is* the structure group, $F = G$, equipped with a free, fibre-preserving right action of $G$ that acts simply transitively on each fibre ([[kobayashi-nomizu-1963-foundations]], [[nakahara-2003-geometry-topology-physics]]). Because the fibre is the group itself, a principal bundle carries the raw **gauge freedom** with no extra structure attached: a choice of point in a fibre is a choice of *frame*, and the group acts by changing frames. A principal bundle admits a global section **iff** it is trivial — so a nontrivial principal bundle has *no* global frame, which is the geometric origin of why one is forced to work in local patches and transport between them.

An **associated bundle** $E = P \times_\rho F$ attaches matter to the gauge frame. Given a representation $\rho : G \to \mathrm{Aut}(F)$ of the structure group on a model fibre $F$, the associated bundle is the quotient of $P \times F$ by the equivalence
$$
(p \cdot g,\ v) \ \sim\ (p,\ \rho(g)\,v),\qquad g \in G,
$$
i.e. moving the frame by $g$ and the fibre value by $\rho(g)$ leaves the physical point unchanged. **Matter fields are sections of associated bundles** carrying a representation of $G$ ([[bleecker-1981-gauge-theory-variational-principles]], [[kobayashi-nomizu-1963-foundations]]). The decomposition of $\rho$ into [[Irreducible representation]]s is the bookkeeping that organizes how distinct field types couple, and the demand that physics be independent of the frame is exactly [[Group equivariance]] under $G$.

> [!note] Editorial: In this program the structure group is $G = \mathrm{GL}(K,\mathbb{R})$ (compact restriction $\mathrm{SO}(3)$ in the proof-of-concept runs), the model fibres are statistical manifolds of Gaussians, and $\rho$ acts on a Gaussian belief by transport of the mean and **congruence** of the covariance, $\rho(g)\cdot\mathcal{N}(\mu,\Sigma) = \mathcal{N}(g\mu,\,g\Sigma g^{\top})$. This is the associated-bundle attachment of probability to gauge developed in [[Agents as fibre-bundle sections]] and the [[Gauge-Theoretic Multi-Agent VFE Model]]; it is a project-specific choice, not part of the textbook definition.

## Connection → parallel transport → curvature → holonomy

A bare bundle has no way to compare fibres over different base points. A **connection** supplies exactly that comparison, and from it flows the whole gauge-field apparatus in a single chain.

**Connection.** A connection is an intrinsic splitting of each tangent space $T_pP$ into a **vertical** part (along the fibre) and a **horizontal** part (an Ehresmann horizontal distribution), equivalently a $\mathfrak{g}$-valued **connection one-form** $\omega$, where $\mathfrak{g} = \mathrm{Lie}(G)$ ([[kobayashi-nomizu-1963-foundations]], [[nakahara-2003-geometry-topology-physics]]). In a local trivialization the connection appears as the **gauge potential** $A$, a $\mathfrak{g}$-valued one-form on $B$ — this is precisely the gauge field of physics.

**Parallel transport.** Horizontal lifts of curves in $B$ define [[Parallel transport]]: a path-dependent fibre isomorphism $P_\gamma$ that carries a section's value from one point to another "as constantly as the geometry allows," i.e. with vanishing covariant derivative along the curve ([[kobayashi-nomizu-1963-foundations]]). Transport is how one agent's belief is carried into another's frame to be compared — comparison requires *transport, not subtraction* (see [[Agents as fibre-bundle sections]], [[Multi-agent variational free energy]]).

**Curvature.** The **curvature two-form**
$$
F \;=\; \Omega \;=\; d\omega + \tfrac{1}{2}[\omega,\omega]
\qquad\bigl(\text{locally } F = dA + \tfrac{1}{2}[A,A]\bigr)
$$
is the structure equation; it measures the infinitesimal failure of parallel transport to commute ([[kobayashi-nomizu-1963-foundations]], [[bleecker-1981-gauge-theory-variational-principles]]). Curvature is the **field strength**, and it satisfies the Bianchi identity $DF = 0$. A connection with $F = 0$ is **flat**.

**Holonomy.** Transporting around a *closed loop* $\gamma$ generally returns a section transformed by a group element — the loop's [[Holonomy]],
$$
\mathrm{Hol}(\gamma) \;=\; \mathcal{P}\exp\!\Big(\!-\!\oint_\gamma A\Big) \;\in\; G,
$$
a path-ordered exponential. The set of all such elements is the **holonomy group**, a subgroup of $G$. The **Ambrose–Singer theorem** identifies the holonomy Lie algebra with the span of curvature values, so *curvature is infinitesimal holonomy* and holonomy is the integrated, gauge-invariant, observable shadow of local curvature ([[kobayashi-nomizu-1963-foundations]], [[nakahara-2003-geometry-topology-physics]]). The connection is flat **iff** every contractible loop has trivial holonomy. Because the program's gauge group is non-abelian ($\mathrm{GL}(K)$/$\mathrm{SO}(3)$), loop order matters and holonomy is generically nontrivial — the regime where it is informative rather than vacuous (see [[Holonomy]], [[Non-flat connection and the photon analogy]]).

A **[[Gauge transformation]]** is a vertical automorphism of $P$ (equivalently a $G$-valued function), acting on the potential by $A \mapsto gAg^{-1} - (dg)g^{-1}$ and on the curvature by the adjoint action $F \mapsto gFg^{-1}$ — the source of gauge *covariance* of the field strength ([[bleecker-1981-gauge-theory-variational-principles]]). The full chain — connection, transport, curvature, holonomy, gauge covariance — is the substrate every gauge construction in the program reuses.

## Topological invariants

Local curvature data integrates to **global** topological invariants. The **[[Characteristic Classes]]** (Chern, Pontryagin, Euler classes) are cohomology classes built from curvature that are independent of the chosen connection and detect the bundle's twisting; index theorems tie this local curvature to global topology ([[nakahara-2003-geometry-topology-physics]], [[milnor1976-characteristic-classes-spherical-fibre]]). Isomorphism classes of principal $G$-bundles over $B$ are classified by homotopy classes of maps from $B$ into a [[Classifying Space]] $BG$ — the universal home of all $G$-bundles. These invariants are how one knows, frame-independently, whether a bundle is genuinely twisted.

## Relevance to this research

Fibre bundles are the geometric backbone of the entire gauge-theoretic VFE program; nearly every distinctive construction is a specialization of the chain above.

- **Agents are sections, not vectors.** The foundational ontological move of the [[Gauge-Theoretic Multi-Agent VFE Model]] is that an agent's belief $q_i$ and generative model $s_i$ are **smooth sections of associated bundles** over a base of contexts $\mathcal{C}$, with structure group $G = \mathrm{GL}(K,\mathbb{R})$ ([[Agents as fibre-bundle sections]]). Spatial extension, overlap of agent supports, and intersubjectivity all follow from beliefs being *fields* over a base rather than single distributions. When the base collapses to a point ($\dim\mathcal{C}=0$) the sections reduce to one distribution per agent and standard attention is recovered — the transformer is the zero-dimensional shadow of the bundle picture (developed in [[gl-k-attention]], [[participatory-it-from-bit]]).

- **Comparison is transport; disagreement is holonomy.** Because sections live in different gauge frames, the consensus/alignment energy is a *transported* KL, $\mathrm{KL}(q_i\,\|\,\Omega_{ij}[q_j])$, with $\Omega_{ij}=U_iU_j^{-1}$ the discrete parallel transport between frames ([[Agents as fibre-bundle sections]], [[Multi-agent variational free energy]]). Propagating beliefs around a social/computational loop can fail to return them unchanged — that path-dependence is [[Holonomy]], and nonzero curvature is the obstruction to consistent transport. This grounds [[Belief inertia]] and the connection's role in the dynamics.

- **Statistical fibres and information geometry.** When the associated fibre is a statistical manifold of Gaussians, the connection interacts with the [[Fisher information metric]] (see [[Information geometry and natural gradient]], [[Mass as Fisher information]]); the bundle/connection texts supply the connection-theoretic side that information geometry specializes to probability. The covariance fibres sit on the curved SPD cone, whose transport is genuinely curved (see [[Symmetric spaces and the SPD cone]]).

- **Equivariant transformer.** The same principal-bundle connection theory underlies gauge-equivariant deep learning ([[Group equivariance]], [[Irreducible representation]], the theme [[Gauge equivariance and geometric deep learning]]). The [[VFE Transformer Program]]'s per-block GL(K) gauge, irrep-tower head mixers, and Clebsch–Gordan coupling realize the connection-and-representation machinery on belief tuples $(\mu,\Sigma,\phi)$; a learned, structure-group-respecting transport *is* a discrete connection.

- **Variational principle.** Bleecker's framing — physical dynamics as the stationary points of a gauge-invariant action — is the structural analogue of the program's central move, that belief and attention dynamics are stationary points of the variational free energy ([[bleecker-1981-gauge-theory-variational-principles]]). The correspondence is at the level of variational structure, an analogy rather than a literal Yang–Mills reproduction.

> [!note] Editorial: In the present single-tree constructions the reconstructed bundle is canonically *trivializable* — each frame $U_i$ is defined on its whole patch, so the Čech data is a coboundary and nontrivial bundle topology is out of scope (see [[Agents as fibre-bundle sections]]). The bundle language is organizational and load-bearing for the *connection / transport / holonomy* content, not (yet) for nontrivial [[Characteristic Classes]].

## Related

[[Agents as fibre-bundle sections]], [[Gauge transformation]], [[Parallel transport]], [[Holonomy]], [[Characteristic Classes]], [[Classifying Space]], [[Group equivariance]], [[Irreducible representation]], [[Non-flat connection and the photon analogy]], [[Fisher information metric]], [[Symmetric spaces and the SPD cone]], [[Killing form]]

## Sources

- [[kobayashi-nomizu-1963-foundations]] — canonical rigorous treatment of principal/associated bundles, connections, parallel transport, curvature, holonomy, Ambrose–Singer.
- [[nakahara-2003-geometry-topology-physics]] — physics-oriented development of fibre bundles, connection/curvature, holonomy, and characteristic classes.
- [[bleecker-1981-gauge-theory-variational-principles]] — bundles and connections via the gauge-invariant variational (Yang–Mills) principle; gauge transformation and curvature transformation laws.
- [[lee-2012-smooth-manifolds]] — smooth manifolds, sections, local trivializations underlying the construction.
- [[milnor1976-characteristic-classes-spherical-fibre]] — characteristic classes of (sphere) fibre bundles.
- [[participatory-it-from-bit]], [[gl-k-attention]] — the program's principal/associated-bundle and agents-as-sections constructions (primary project sources).

## See also

- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[VFE Transformer Program]]
- [[Gauge equivariance and geometric deep learning]]
- [[Multi-agent variational free energy]]
- [[Meta-agents and hierarchical emergence]]
- [[Participatory realism and quantum foundations]]
