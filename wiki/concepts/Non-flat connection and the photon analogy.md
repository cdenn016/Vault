---
type: concept
title: "Non-flat connection and the photon analogy"
aliases:
  - "Regime I"
  - "Regime II"
  - "Non-flat connection"
  - "Non-flat gauge connection"
  - "Photon analogy"
  - "Minimal coupling"
  - "Edge-relaxed cocycle"
tags:
  - cluster/gauge-theory
  - cluster/multi-agent
  - project/transformer
status: draft
created: 2026-06-18
updated: 2026-11-18
---

# Non-flat connection and the photon analogy

## Dynamic links: the Maxwell half for vfe3, October 3, 2026

[[dennis-2026-dynamic-links]] makes the transformer's exponential link generators $X_{ij}$ latent variables on a depth-by-token lattice, with a normalized prior inside the variational free energy, so that link dynamics are inference. The prior has an anchor (mass) term and a curvature term on the elementary loops, measured by the Frobenius defect $\tfrac12\|W-I\|_F^2$ of the reference-coordinate holonomy, which equals Wilson's density $K-\operatorname{tr}W$ on $O(K)$ and, unlike every eigenvalue statistic, does not vanish on unipotent holonomy. The time-like loops of the lattice supply the kinetic term $\|\partial_\ell X-\cdots\|^2$ as the electric part of the same curvature energy, and the linearized link field equation is a screened, massive Euclidean Maxwell equation sourced by the delta-rule current (prediction error times source state). In the causal model the curvature energy is a declared prior; for undirected Gaussian matter, integrating out the states induces $\tfrac12\log\det J(X)$, whose hopping expansion begins with Wilson's triangle action. This is a derivation, not an implementation: `vfe3` still runs only the static shared-generator chart, which is the note's zero-temperature limit.

Two statements of the dynamic-links note were corrected on October 4. The Frobenius defect is invariant under nonzero multiples of orthogonal reparameterizations, not orthogonal ones only. Without the link prior, stationary generators can exist at critical points of the exponential map, and the chart infimum is approached at the singular rank-one transport only when $\xi_j^\top C_j^{-1}\xi'\ge0$; otherwise it lies strictly above it.

## Definition

In the gauge-VFE transformer the inter-token transport is the cocycle $\Omega_{ij} = \Omega_i\,\Omega_j^{-1}$ (equivalently $\exp(\phi_i)\exp(-\phi_j)$), a **flat** connection: every closed-loop [[Holonomy]] is the identity and the connection is pure gauge. This is **Regime I**, the vacuum — the connection does no frame-independent work and can be rotated away. **Regime II** promotes the connection to a genuinely **non-flat** one by inserting an edge factor $\Omega_{ij} = \Omega_i\,V_{ij}\,\Omega_j^{-1}$ (or $\exp(\phi_i)\exp(\delta_{ij})\exp(-\phi_j)$) whose closed-loop holonomy is nontrivial: transport around a loop returns a belief transformed by a real group element, the integrated [[Holonomy|curvature]].

The **photon analogy** reads this connection as the gauge field that mediates interaction between belief "matter" fields, exactly as the electromagnetic potential $A_\mu$ mediates interaction between electrons in QED. The dictionary is direct: the belief $q_i(c) = \mathcal N(\mu,\Sigma)$ plays the electron field $\psi$, the induced connection plays the photon $A_\mu$, the gauge-covariant transport plays minimal coupling $D_\mu\psi = (\partial_\mu + A_\mu)\psi$, and the Yang–Mills action plays the Maxwell action. The analogy has **two halves**:

1. **The Maxwell / Yang–Mills kinetic term** — a kinetic action $\int \operatorname{tr}(F_{\mu\nu}F^{\mu\nu})$ for the connection itself, making it a propagating degree of freedom whose curvature $F$ measures the failure to be pure gauge ([[yang-mills-1954]]).
2. **Minimal coupling** — the connection must do real work *on the matter*: a covariant-derivative vertex by which the connection mediates belief interactions across the base, with the Gaussian covariance carried by the sandwich product $\Sigma\mapsto M\Sigma M^\top$.

The decisive subtlety — the place implementations go wrong — is that **a non-identity edge factor is not curvature**. A single twist $V\neq I$ can be gauge-removable on a tree, can belong to a globally flat connection, or can sit inside trivial plaquette holonomy; and the induced form $A_\mu = U^{-1}\partial_\mu U$ is *pure gauge* (the Maurer–Cartan identity gives $F\equiv 0$), curvature-free no matter how nonzero $A$ looks ([[nakahara-2003-geometry-topology-physics]], [[baez-muniain-1994-gauge-fields]]). Genuine Regime II requires nontrivial **closed-loop holonomy** — a plaquette/Wilson-loop or triangle product that deviates from the identity *and survives a gauge transformation* — the gauge-invariant loop observable that the lattice gauge program builds its dynamics on ([[wilson-1974-confinement-quarks]], [[kogut-susskind-1975-hamiltonian-lattice-gauge]], [[creutz-1983-quarks-gluons-lattices]]). Equivalently, the curvature certificate must be a conjugation-invariant of the loop (its eigenvalue spectrum, or $\operatorname{Re}\operatorname{tr}$), not the frame-dependent $\lVert W - I\rVert_F$.

## Why it matters here

A flat connection can only express consensus: the inter-token coupling $\beta_{ij}\,\mathrm{KL}(q_i \| \Omega_{ij}[q_j])$ pulls beliefs toward a single gauge-fixed agreement, with no room for path-dependent, curvature-selected structure. A non-flat connection is what lets the model carry frame-independent relational content that cannot be averaged away — the gauge-theoretic substrate for emergent organization. The gauge principle also *forces the form* of any term that differentiates beliefs along the base: the covariant derivative $D_\mu$ is the unique lowest-order operator that keeps $q_i$ in its own representation, so a base-kinetic belief term, if added, must use $D_\mu$ on pain of breaking gauge covariance. This form-forcing is exact (the same logic that fixes minimal coupling in QED); the *existence* of such a term is a modeling choice, not a consequence forced by the existing free energy. The same form-forcing is derived from first principles in the geometric-deep-learning setting by [[weiler-2021-coordinate-independent-cnns]], where requiring coordinate-independence plus weight-sharing *forces* local-gauge equivariance, supplying textbook-grade statements of the parallel-transport rule and the cocycle/holonomy conditions this program leans on.

This concept is core theory of the [[VFE Transformer Program]] (`vfe3`).

## Details

**The `vfe3` implementation.** A 2026-06-18 audit compared the transformer against the full photon standard. Regime II is the edge-relaxed cocycle $\Omega_{ij} = \exp(\phi_i\!\cdot\!G)\,\exp(\delta_{ij}\!\cdot\!G)\,\exp(-\phi_j\!\cdot\!G)$ with a learned **bilinear** edge factor $\delta_{ij}^a = \mu_i^\top W^a \mu_j$ (`vfe3/geometry/transport.py:_build_regime_ii`; the connection $W$ is a sanctioned, default-off neural-network exception, selected by `transport_mode='regime_ii'`). A nonzero $W$ does produce genuine triangle holonomy. But the raw-mean bilinear is **gauge-invariant only at $W=0$**: under a gauge action $\mu_i\mapsto g\mu_i$ the edge factor is not equivariant, so $\Omega_{ij}$ ceases to transform as $g_i\Omega_{ij}g_j^{-1}$ and the deviation grows with $\lVert W\rVert$ (the codebase documents this in `test_regime_ii_edge_factor_breaks_gauge_invariance_for_nonzero_W`). The gauge-*invariant* alternative — building $\delta$ from the Mahalanobis/trace/log-det features of the belief KL, which are congruence-invariant (`gauge_invariant_edge_features`, "Route B") — is now **wired** as the registered builder `transport_mode='regime_ii_covariant'` (`_build_regime_ii_covariant`, a sanctioned default-off NN exception with a learned `connection_M` of shape `(n_gen, 3)`; added 2026-06-18, threaded end-to-end through the E-step and trainable, with gauge-equivariance pinned by `tests/test_regime_ii_covariant.py`). The covariance $\Omega_{ij}\mapsto g_i\Omega_{ij}g_j^{-1}$ holds under the *coherent* gauge action — the frame co-transforms, $\exp(\phi_i)\mapsto g_i\exp(\phi_i)$, so the transported key $\Omega^0_{ij}\mu_j$ and the query $\mu_i$ both land in vertex $i$'s frame and the KL edge features see a *common* push-forward — not from transforming the raw beliefs alone with $\phi$ held fixed (a 2026-06-18 audit clarified this mechanism; the end-to-end $\Omega$ transformation law, beyond the edge-feature invariance, is now pinned by `test_regime_ii_covariant_omega_transforms_covariantly`). The invariance is fp32-fragile: the transported-key congruence $\Omega^0\Sigma\Omega^{0\top}$ squares $\operatorname{cond}(\Omega^0)\sim\exp(2\lVert\phi\rVert)$ on the non-compact `block_glk` frame (>100% relative error at $K{=}70$), so the feature congruence and its Cholesky now run in a **float64 island** with a `safe_cholesky` non-PD fallback (audit fix 2026-06-18), mirroring `transport_covariance`'s sandwich upcast. And `vfe3` carries **no Maxwell/Yang–Mills kinetic term** in its free energy. So the bilinear `regime_ii` buys curvature by sacrificing the gauge principle, while the covariant `regime_ii_covariant` (Route B) keeps **both** the gauge principle and the belief coupling — leaving the missing Yang–Mills kinetic term as `vfe3`'s sole remaining gap versus the full photon standard.

> [!note] Editorial: The implementation-status claims here (which builder is wired, the gauge-covariance break at $W\neq0$) are grounded in direct reads of the `vfe3` code and the in-repo derivation memos `derivations/photon_minimal_coupling_analysis_2026-06-02.md` and `..._review_response_2026-06-03.md`, plus the 2026-06-18 audit and the same-day fixes, rather than in any curated vault source. The photon-mediation *form* is proven; the claim that the minimal-coupling term *must exist* is conjectural and so marked in the memos.

**Eigenvalue curvature densities and unipotent holonomy.** The non-negative eigenvalue density $\sum_k|\lambda_k(W)-1|$ of a plaquette holonomy is $\geq 0$ and $0$ exactly when every eigenvalue of $W$ equals one. That does not imply $W=I$ for non-diagonalizable $W$: for the unipotent shear $W=I+E_{12}$ ($K\ge2$) both eigenvalues equal one, so the density is $0$ although $W\neq I$. More generally, no continuous class function on the non-compact $GL(K)$ separates a unipotent element from the identity, because conjugation by $\operatorname{diag}(t,1,\dots,1)$ sends $I+E_{12}$ to $I+tE_{12}\to I$ as $t\to0$. Such a density is therefore blind to unipotent holonomy; separating curvature measures are discussed in [[dennis-2026-dynamic-links]].

## In this work

In `vfe3`, `transport_mode='regime_ii'` selects the bilinear edge-relaxed cocycle (`connection_W`, `cocycle_relaxation` homotopy $\alpha\in[0,1]$; flat at $\alpha=0$ or $W=0$), gauge-covariant only at $W=0$. `transport_mode='regime_ii_covariant'` selects the covariant Route B (`_build_regime_ii_covariant`, learned `connection_M` over the congruence-invariant `gauge_invariant_edge_features`; flat at $M=0$): non-flat **and** gauge-covariant for any $M$, default-off, end-to-end trainable (the config auto-enables `oracle_unroll_grad` for both non-flat regimes). Still no Yang–Mills kinetic term; `TODO(Route A)` in the builder targets a commutant-restricted connection on a compact subgroup for exact equivariance plus a bounded Wilson action. (Status October 3, 2026: these regimes have since been removed from `vfe3`; `transport_mode` is a retired field pinned to `"flat"`, and the current projected routes carry only the static shared-generator exponential chart selected by `content_link_chart`. [[dennis-2026-dynamic-links]] derives, but does not implement, a curvature and kinetic term for latent link generators on that chart.)

## Sources

- [[yang-mills-1954]] — the non-abelian gauge field and its $\operatorname{tr}(F^2)$ action; the Maxwell half of the analogy.
- [[nakahara-2003-geometry-topology-physics]], [[baez-muniain-1994-gauge-fields]] — pure-gauge/Maurer–Cartan ($F\equiv0$), holonomy, and lattice plaquettes as the discrete curvature carrier.
- [[frankel-2011-geometry-of-physics]] — minimal coupling and the covariant derivative as the unique form-forced base-kinetic operator.
- [[weiler-2021-coordinate-independent-cnns]] — monograph deriving gauge equivariance from coordinate-independence plus weight-sharing, with full G-structure, parallel-transport, and cocycle/holonomy bookkeeping.
- [[wilson-1974-confinement-quarks]] — the Wilson loop as the gauge-invariant order parameter and the lattice plaquette action.
- [[kogut-susskind-1975-hamiltonian-lattice-gauge]] — Hamiltonian lattice gauge theory; link variables and electric/magnetic terms on the lattice.
- [[creutz-1983-quarks-gluons-lattices]] — textbook treatment of lattice gauge theory, plaquettes, and Wilson-loop computation.
- [[dennis-2026-dynamic-links]] — latent link generators in the free energy: Frobenius-defect curvature prior, kinetic term from time-like loops, delta-rule field equation, induced Wilson action of undirected Gaussian matter; also the unipotent blind spot of eigenvalue curvature measures.

## See also

- [[Holonomy]]
- [[Parallel transport]]
- [[Gauge transformation]]
- [[VFE Transformer Program]]
