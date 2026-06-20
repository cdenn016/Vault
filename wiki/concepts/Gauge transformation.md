---
type: concept
title: "Gauge transformation"
aliases:
  - "Gauge transformations"
  - "Gauge symmetry"
  - "Frame change"
  - "Change of gauge"
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Gauge transformation

## Definition

A *gauge transformation* is a position-dependent change of reference frame applied to the internal degrees of freedom of a field, together with a compensating rule for how derivatives and couplings must change so that the underlying physics — or, here, the underlying computation — is left invariant. Formally, suppose every point (or token) $x$ carries a feature vector living in a vector space on which a group $G$ acts. A *global* symmetry applies a single group element $g \in G$ to every point at once. A *gauge* (or *local*) transformation instead applies a possibly different element $g(x) \in G$ at each point, sending a feature $f(x)$ to $\rho(g(x))\,f(x)$, where $\rho$ is the representation of $G$ on the feature space. The set of all such position-dependent assignments $x \mapsto g(x)$ forms the *gauge group*.

The crucial structural fact is that a gauge transformation is *not* a free relabeling: quantities that compare features at *different* points — derivatives, parallel transports, attention affinities — are frame-dependent and must transform consistently. A map is *gauge equivariant* when transforming the input by $g(x)$ and then applying the map yields the same result as applying the map first and then transforming the output by the (transported) action of $g(x)$. Gauge *invariance* is the special case where the output is unchanged. In the deep-learning reading codified by [[bronstein-2021-geometric-deep-learning]], a gauge is a local choice of frame for a feature field on a manifold, and a network layer is admissible precisely when it commutes with arbitrary local frame changes.

## Why it matters here

The VFE transformer is built so that its per-token Gaussian beliefs $(\mu, \Sigma)$ and their couplings are *expressed in a frame that the model is free to rotate at each token*. The chosen gauge group is the block general-linear group GL($k$) (`gauge_group: block_glk`): each token's latent space is partitioned into blocks, and an independent invertible linear map may act on each block. Because there is no canonical frame, the physics of the model — its free-energy objective and its predictions — must be invariant to which frame is picked at each token, exactly the requirement of a gauge transformation. This absence of a privileged frame is the same condition that motivates [[Quantum reference frames]], where physical content is read off only relative to a chosen frame and observables must be frame-invariant ([[bartlett-rudolph-spekkens-2007-reference-frames]]). This is the architectural commitment that turns a transformer into a *gauge-theoretic* one: rather than baking in a single global symmetry as the group-equivariant convolutions of [[cohen-2016-gcnn]] do, it follows the *local* gauge generalization of [[cohen-2019-gauge-cnn]], where features carry frames and any comparison across positions is mediated by [[Parallel transport]].

Gauge invariance is also what makes the optimization geometry well posed. A reparameterization-invariant objective demands a reparameterization-invariant update rule, which is precisely the [[Natural gradient]] preconditioned by the [[Fisher information metric]] (see [[amari-1998-natural-gradient]] and [[ollivier-2015-riemannian-metrics-nn]]). Gauge freedom on the latent frame is the geometric-deep-learning cousin of reparameterization invariance on the statistical manifold; both insist that the learning dynamics depend on the model, not on the arbitrary coordinates in which it is written.

## Details

**Group, algebra, and the "phi" parameterization.** For a Lie group such as GL($k$), gauge elements are most safely handled in the *Lie algebra*. The model parameterizes each gauge element as $g = \exp(\phi)$, where $\phi$ is a matrix (the `gauge_parameterization: phi` setting) living in the algebra $\mathfrak{gl}(k)$; the exponential map recovers the group element. This algebra-first treatment is the same device LieConv uses to remain equivariant to any Lie group with a surjective exponential map ([[finzi-2020-lieconv]]): doing all geometry in logarithmic coordinates and recovering group elements via $\exp$ keeps the parameterization unconstrained and differentiable.

**Composition by BCH.** Because two gauge elements compose as $\exp(\phi_1)\exp(\phi_2) = \exp\!\big(\phi_1 + \phi_2 + \tfrac12[\phi_1,\phi_2] + \cdots\big)$, composing transformations directly in the algebra requires the [[Baker-Campbell-Hausdorff formula|Baker–Campbell–Hausdorff]] (BCH) series, truncated to a finite order in practice. The model uses BCH both as the *retraction* that moves gauge parameters along an update (`phi_retract_mode: bch`) and as the *composition* rule for positional gauges (`pos_phi_compose: bch`, `bch_pe_order: 4`). Retractions are the cheap first-order surrogates for true geodesic exponentials analyzed in [[absil-2008-optimization-matrix-manifolds]]; using a Lie-group retraction keeps each update *on the group manifold* without leaving the gauge structure.

**Transport and holonomy.** Once features carry frames, comparing a belief at token $i$ with one at token $j$ requires carrying the frame along, i.e. [[Parallel transport]]. The path-dependence of that transport — the failure of a frame to return to itself around a loop — is [[Holonomy]]. The current configuration uses a flat connection (`transport_mode: flat`), the trivial-holonomy limit, while exposing a cocycle-relaxation knob (`cocycle_relaxation`) that controls how strictly the transport maps must satisfy the cocycle consistency condition required for a well-defined gauge structure. The textbook-grade statements of this transport rule and its cocycle/holonomy bookkeeping are derived from first principles in [[weiler-2021-coordinate-independent-cnns]], which shows that demanding coordinate-independence together with weight-sharing *forces* local-gauge equivariance, complete with the underlying $G$-structure and parallel-transport machinery.

**Representations, irreps, and coupling.** A gauge group acts on features through representations. Decomposing features into [[Irreducible representation|irreducible representations]] (irreps) and coupling them through the [[Clebsch-Gordan coefficients|Clebsch–Gordan]] tensor product is the standard bookkeeping for building gauge-equivariant layers, established for steerable and tensor-field networks in [[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], and [[thomas-2018-tensor-field-networks]]. The VFE transformer carries the corresponding switches (`irrep_spec`, `use_cg_coupling`, `cross_couplings`), so its block-GL($k$) gauge group can in principle structure attention by irrep rather than by raw coordinates.

**Preconditioning the gauge update.** Updates to $\phi$ are preconditioned per block by the Killing form of the Lie algebra (`phi_precond_mode: killing_per_block`). The Killing form is the natural, gauge-covariant inner product on a Lie algebra; preconditioning with it is the gauge-theoretic analogue of the block-Kronecker Fisher preconditioning K-FAC introduced for natural-gradient training ([[martens-2015-kfac]], [[martens-2020-natural-gradient-insights]]). In both cases the point is to make the update *invariant to the frame*, so learning respects the gauge symmetry rather than fighting it.

> [!note] Editorial: The config sets `transport_mode: flat`, `cocycle_relaxation: 1.0`, `use_cg_coupling: false`, and `irrep_spec: null` in the inspected run, so the gauge machinery is present and parameterizable but operating in its simplest (flat, uncoupled) regime for this particular training run rather than at full curvature.

## In this work

The gauge transformation is the organizing symmetry of the whole architecture, surfacing across the config as:

- `gauge_group: block_glk` — the gauge group is block GL($k$), one invertible linear map per latent block per token.
- `gauge_parameterization: phi` with `phi_scale` — gauge elements are generated from algebra-valued $\phi$ via the exponential map.
- `phi_retract_mode: bch` and `phi_precond_mode: killing_per_block` — gauge parameters are retracted with a truncated BCH map and preconditioned by the per-block Killing form during the M-step.
- `transport_mode: flat`, `cocycle_relaxation` — the connection used to transport beliefs between tokens, and the consistency relaxation governing it.
- `pos_phi: learned`, `pos_phi_compose: bch`, `bch_pe_order`, `pos_phi_scale` — positional encodings are themselves learned gauge elements composed via BCH, the gauge-native counterpart to the RoPE / ALiBi / T5 position priors that ride alongside them.
- `irrep_spec`, `use_cg_coupling`, `cross_couplings` — the irrep decomposition and Clebsch–Gordan coupling through which the gauge group can structure attention (disabled in the inspected run).

Because the beliefs $(\mu, \Sigma)$ that the gauge frames act upon are SPD-manifold objects (see [[pennec-2006-affine-invariant-tensor]]), the gauge action on a covariance is a congruence (sandwich) action $\Sigma \mapsto g\,\Sigma\,g^{\top}$, which preserves positive-definiteness; the matching `spd_affine` retraction then moves $\Sigma$ on its own manifold. The gauge layer and the SPD layer thus share the same Riemannian, frame-invariant design philosophy.

## Sources

- [[cohen-2019-gauge-cnn]] — local gauge transformations on manifolds; kernel constraint and parallel-transport rule.
- [[weiler-2021-coordinate-independent-cnns]] — definitive monograph deriving gauge equivariance from coordinate-independence plus weight-sharing, with full $G$-structure, transport, and cocycle/holonomy statements.
- [[bronstein-2021-geometric-deep-learning]] — gauges and equivariance as a unifying blueprint for deep nets.
- [[cohen-2016-gcnn]] — global group equivariance, the precursor to local gauge equivariance.
- [[finzi-2020-lieconv]] — Lie-algebra (log) parameterization with $\exp$ recovery.
- [[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]] — irreps and Clebsch–Gordan coupling for gauge-equivariant layers.
- [[absil-2008-optimization-matrix-manifolds]] — retractions as surrogates for the geodesic exponential.
- [[martens-2015-kfac]], [[martens-2020-natural-gradient-insights]] — block Fisher / curvature preconditioning, the analogue of [[Killing form|Killing-form]] preconditioning.
- [[amari-1998-natural-gradient]], [[ollivier-2015-riemannian-metrics-nn]] — reparameterization-invariant updates, the statistical counterpart of gauge invariance.
- [[pennec-2006-affine-invariant-tensor]] — affine-invariant SPD geometry on which the gauge congruence acts.
- [[horn-johnson-2013-matrix-analysis]] — matrix-analysis reference for the GL($k$) congruence action and exponential map.
- [[bartlett-rudolph-spekkens-2007-reference-frames]] — quantum reference frames and the frame-invariance of physical content.
- [[bleecker-1981-gauge-theory-variational-principles]] — canonical bundle-connection-and-variational-principle reference behind the gauge formalism.

## See also

- [[Parallel transport]]
- [[Holonomy]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Group equivariance]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Gauge equivariant CNN]]
- [[Steerable CNN]]
- [[LieConv]]
- [[Tensor Field Network]]
- [[Structural realism]]
- [[Quantum reference frames]]
