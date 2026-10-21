---
type: concept
title: Holonomy
aliases:
  - Holonomy group
  - Anholonomy
  - Gauge holonomy
tags:
  - cluster/gauge-theory
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-10-20
---

# Holonomy

## Edge-dependent links: curved mode and pure-gauge control, October 6, 2026

[[dennis-2026-edge-latent-links]] gives the first implemented link field with more than one holonomy class per layer: with $G_{ij}=e^{L}\exp(A_iB_j^\top)$ the triangle trace changes at first order in $B$, while the pure-gauge control $G_{ij}=g_ie^{L}g_j^{-1}$ has every triangle holonomy conjugate to $e^{L}$. In the depth loops $(G_{ik}^{\ell+1}G_{kk}^\ell)^{-1}G_{ij}^{\ell+1}G_{jk}^\ell$ the upper shared generator cancels, so the shared-generator model is loop-flat there although its triangles are not.

## Triangle spectra of the implemented charts, October 4, 2026

[[dennis-2026-glk-lie-algebra-links-v2]] places the inverse-edge triangle holonomy in the main GL(K) manuscript and computes it for the routed links that VFE_3.0 actually forms. With tiled heads, an invertible $T$, an invertible effective receiving map $\widetilde O$ and positive weights on the three edges, the triangle holonomy of $\mathcal M_{ab}=U_a\widetilde O\boldsymbol\beta_{ab}TU_b^{-1}$ is similar to $\boldsymbol\rho_{ijk}T\widetilde O$, where $\boldsymbol\rho_{ijk}$ is the head-diagonal routing ratio $\beta_{ij}^{(h)}\beta_{jk}^{(h)}/\beta_{ik}^{(h)}$. The head transfer is $TO$ in the affine chart, $I+TO$ in the first-order chart and $e^{TO}$ in the exponential chart, so a vanishing routing defect still leaves a holonomy similar to the transfer, which in the exponential chart is generally not the identity. For softmax routing the receiver normalizer cancels and the intermediate normalizer $Z_j$ remains in $\log\rho_{ijk}$. To second order the exponential-link holonomy is $\log(e^{-Z}e^Ae^B)=(A+B-Z)+\tfrac12([A,B]-[Z,A]-[Z,B])+O(3)$, so an additive coboundary of generators does not make the links flat when its values fail to commute. The statements are checked numerically in float64 at small sizes; none of them is a measurement on trained links.

## Unipotent blind spot and the Frobenius defect, October 3, 2026

[[dennis-2026-dynamic-links]] proves that every continuous conjugation-invariant function on the non-compact $\mathrm{GL}(K)$, $K\ge2$, takes the same value at a unipotent element as at the identity: conjugating a Jordan block by $\operatorname{diag}(1,t^{-1},\dots)$ scales its superdiagonal by $t\to0$. Such functions depend only on eigenvalues, so every eigenvalue statistic of a holonomy, including the spectral curvature reported by the `vfe3` routing-holonomy diagnostic and the bounded density $\sum_k|\lambda_k(W)-1|$ of MAgent (corrected on [[Non-flat connection and the photon analogy]]), vanishes on a shear $W=I+E_{12}\ne I$. The note measures curvature by the Frobenius defect $\tfrac12\|W-I\|_F^2$ of the reference-coordinate holonomy instead. Because the generators are reference data, that matrix and not only its conjugacy class is invariant under the passive gauge action, the defect vanishes only at $W=I$, and on $O(K)$ it equals Wilson's density $K-\operatorname{tr}W$. The extra structure it uses is the reference metric, which reduces the measurement from $\mathrm{GL}(K)$ to $O(K)$; under the reparameterization that moves frames into links it is invariant exactly for nonzero multiples of orthogonal changes, and the scalar factor acts trivially on the holonomy. The October 3 version of the note said orthogonal changes only; it was corrected on October 4.

## Unified exponential-link construction, October 3, 2026

The author selected Option A exponential group-valued links as the primary future GL(K) integration direction in [[dennis-2026-attention-unified]]. Causal support forbids directed cycles through distinct positions, but invertible edges allow the inverse-edge triangle $\Theta_{ik}^{-1}\Theta_{ij}\Theta_{jk}$. Its conjugacy invariants can be nontrivial for a composite link field without an independent gauge action. A constant exponential link is nonflat unless its exponential is identity; "maximally curved" in the earlier note has no specified ordering and is removed in the consolidation.

The existing VFE_3.0 working tree now includes routing-triangle diagnostics, checked by five tiny CPU tests during consolidation. This is a diagnostic path, not a new learned exponential edge field or a trained performance result. The exact head-weight ratio requires the stated inverse-map assumptions; the general map-dependent diagnostic retains $TO$ rather than assuming identity. For jointly Gaussian reference states, zero regression composition defect on every strict triple is equivalent to first-order Markov conditional independence; group holonomy additionally needs invertible regression maps.

## Coboundary monitors and link spectra in vfe3 (design record, September 28)

The design record behind [[dennis-2026-phi-natgrad]] shows that the transformer's `holonomy_deviation` and `holonomy_wilson` metrics multiply only the coboundary $\Omega_{ij}=U_iU_j^{-1}$, which closes identically, so they measure floating-point error of the stored frame pair, not curvature; it recommends relabeling them as coboundary closure residuals. The gauge-invariant content of the communication links $L_{ij}^{(h)}=U_iM_hU_j^{-1}$ is instead the simultaneous similarity class of the $M_h$, and under a causal prior the only closed loops are self-loops, whose spectra are those of $rI+\sum_h\beta_{ii}^hM_h$. See the September 20 matrix-link section below for the scope of loop products.

## Matrix-link loop observables, September 20, 2026

[[dennis-2026-glk-matrix-links-2026-09-20]] distinguishes the flat vertex-frame connection $\Omega_{ij}=U_iU_j^{-1}$ from communication links $L_{ij}^{(h)}=U_iO_hT_hU_j^{-1}$. Any declared closed product of matrices obeying $B_{ij}'=g_iB_{ij}g_j^{-1}$ transforms by conjugation at its base site, and its trace is invariant without requiring inverse links. Such a product may record gain or rank loss; nonidentity does not establish curvature of $\Omega$ or holonomy of an invertible connection.

For a shared unweighted head, a path with $r$ edges is $U_{i_0}(OT)^rU_{i_r}^{-1}$, so paths with the same endpoints and length coincide. Causal attention has no directed cycles through distinct token positions. These limits must accompany any proposed loop diagnostic. See [[Lattice gauge theory]] for the matrix-link construction and its distinction from group-valued parallel transport.

## Triangle defect of attention routing, October 2, 2026

[[dennis-2026-link-origin]] shows that the multi-head operator $\mathcal C_{ij}=U_iOB_{ij}TU_j^{-1}$ is generically a $\mathrm{GL}(K)$ link, so loops with one reversed edge exist. For $TO=I$ the loop is $U_iO(\bigoplus_h\beta_{ij}\beta_{jk}/\beta_{ik}\,I_d)O^{-1}U_i^{-1}$, and for routing $\beta=\pi e^{-D/\kappa}/Z$ the log-holonomy of each head is
$$-\frac{D_{ij}+D_{jk}-D_{ik}}{\kappa}+\log\frac{\pi_{ij}\pi_{jk}}{\pi_{ik}}-\log Z_j,$$
the triangle defect of the routing costs offset by the intermediate normalizer. Because the KL has no triangle inequality, and here compares query with key laws under different maps, the defect has no definite sign. For the exponential link with commuting generators the loop is $U_iO\exp(B_{ij}+B_{jk}-B_{ik})O^{-1}U_i^{-1}$, and in general it follows the [[Baker-Campbell-Hausdorff formula]] series. The note computes the defect only from formulas, checked in float64 at $K=6$; it has not been measured in a trained model, and reading attention weights as an abelian connection is an interpretation. See [[Lattice gauge theory]].

## Definition

Holonomy measures the failure of a connection to be path-independent. Given a manifold equipped with a connection (a rule for [[Parallel transport]] — moving a vector, frame, or belief along a curve while keeping it "as constant as the geometry allows"), transporting an object around a **closed loop** generally does not return it unchanged: it comes back rotated, scaled, or otherwise transformed by some group element. That net transformation is the **holonomy** of the loop. The set of all such transformations, taken over all loops based at a point, forms a group — the **holonomy group** — which is a subgroup of the connection's structure (gauge) group.

Concretely, if a connection is specified by a Lie-algebra-valued one-form (a "gauge potential") `A`, the holonomy of a loop `γ` is the path-ordered exponential

```
Hol(γ) = P exp( -∮_γ A )  ∈ G,
```

an element of the structure group `G`. The connection is **flat** (curvature zero) exactly when the holonomy of every contractible loop is the identity; then transport is path-independent and the geometry is said to be **holonomic**. Nontrivial holonomy is equivalently the integrated effect of **curvature**: by the non-abelian Stokes / Ambrose–Singer theorem, the holonomy around an infinitesimal loop is the curvature two-form evaluated on the loop's area. Holonomy is therefore the global, observable shadow of local curvature.

## Why it matters here

Generic non-abelian connections and curved SPD manifolds can have nontrivial holonomy. The realized transformer Regime-I connection is more restrictive: $\Omega_{ij}=U_iU_j^{-1}$ telescopes on every closed loop, so $H=I$ exactly despite the noncommutativity of $\mathrm{GL}(K)$. Nontrivial model holonomy requires an independent-edge or otherwise nonflat Regime-II connection.

## Details

**Holonomy and curvature.** For a connection with curvature `F`, the holonomy of a small loop bounding an oriented area element `Σ` is

```
Hol ≈ exp( -∮ F )  ≈  I - F(Σ) + ...,
```

so curvature is the *density* of holonomy and holonomy is its *integral*. A connection is flat iff `F = 0` iff all contractible-loop holonomies vanish. This is the geometric content behind a **cocycle condition**: a consistent assignment of frame-to-frame transport maps (transition functions / cocycles) is one whose loop compositions are trivial; relaxing it allows controlled nontrivial holonomy. The textbook-grade statement of this transport rule and of the cocycle/holonomy conditions — derived from first principles by demanding coordinate-independence plus weight-sharing, which together *force* local-gauge equivariance with full G-structure and parallel-transport bookkeeping — is [[weiler-2021-coordinate-independent-cnns]].

**Anholonomy and the geometric (Berry-type) phase.** Holonomy is sometimes called *anholonomy* to stress that the closed-loop transport fails to close on itself in the fiber. The classic intuition is parallel-transporting a vector around a spherical triangle: it returns rotated by an angle equal to the enclosed solid angle (the sphere's curvature times area). Abelian holonomy reduces to such a phase/scale factor; the non-abelian GL(k) case generalizes this to a full matrix.

**Relation to Lie-algebra coordinates.** BCH commutators describe generic non-abelian group commutators, but they do not create holonomy in the realized vertex cocycle: the exact group products $U_iU_j^{-1}$ still telescope. Finite BCH truncation is only a local approximation, and any truncation residue is numerical/chart error rather than a Regime-I curvature observable.

**Holonomy group as a representation-theoretic object.** The holonomy group sits inside the structure group and acts on features that are organized into [[Irreducible representation]]s. Equivariant architectures route information through irreps and couple them with [[Clebsch-Gordan coefficients]] ([[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]]); the holonomy is the concrete group element that acts on each irrep block as a belief is transported, so its effect decomposes block-by-block across the model's irrep bookkeeping.

> [!note] Editorial (2026-07-09): generic holonomy definitions on this page remain valid. In this architecture, measurable nontrivial loop transport belongs only to an edge-relaxed/nonflat path; strict Regime I is exactly flat.

## In this work

Holonomy surfaces wherever the config commits to a connection or to non-commuting transport:

- **Regime-I vertex transport.** The cocycle gives $H=I$ exactly; noncommutativity alone does not change this.
- **Parallel transport / holonomy of beliefs.** Closed-loop transport is a valid consistency diagnostic only for a connection that the architecture actually realizes. The Regime-I frame connection closes exactly; an edge-relaxed connection can be tested for nontrivial loop transport ([[cohen-2019-gauge-cnn]], [[bronstein-2021-geometric-deep-learning]]).
- **Generic SPD holonomy.** Levi-Civita parallel transport of tangent vectors around a closed path on the curved affine-invariant SPD manifold can have nontrivial holonomy ([[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]). The deployed `spd_affine` covariance retraction updates covariance points; it does not by itself implement that closed-loop tangent-vector transport or establish SPD-side model holonomy.
- **Edge-relaxed transport.** Independent edge variables can produce nontrivial holonomy and are the appropriate target for loop diagnostics.
- **Frame conditioning.** The configured Cartan/Killing object is an optimizer preconditioner, not a full-$\mathrm{GL}(K)$ Fisher metric and not a certificate that holonomy is reparameterization invariant.

## Triangle holonomy on causal support, October 2, 2026

[[dennis-2026-link-curvature]] defines the triangle holonomy of an invertible causal link field as $F_{ijk}=\Theta_{ik}^{-1}\Theta_{ij}\Theta_{jk}$ for $k<j<i$, the loop $k\to j\to i\to k$ whose last step uses the inverse of the long edge. It transforms as $F_{ijk}\mapsto g_kF_{ijk}g_k^{-1}$, and in reference coordinates it equals $U_k(G_{ik}^{-1}G_{ij}G_{jk})U_k^{-1}$, so the frames drop out of its conjugacy class: no choice of frames flattens or creates the curvature, which is a property of the reference field $G$. The field is flat exactly when each link is the ordered product of adjacent links, and for invertible links exactly when it is pure gauge $g_ig_j^{-1}$ (singular counterexample: the shared projector). The KL triangle defect above is the head-sum row of a table of candidates: positional and rotary links are flat, the constant exponential link has $F=U_ke^{X}U_k^{-1}$, the routed exponent has the additive defect $B_{ij}+B_{jk}-B_{ik}$ in the exponent, and the head sum has the multiplicative defect. Normalized head-sum routing is flat on strict triangles iff $\beta_{ij}=c_i/c_j$; uniform causal attention has a nonzero defect (largest cocycle violation $1/6$ on five tokens). The note suggests the flat pattern and the uniform pattern as baselines for the defect computed from logged routing weights; no such measurement has been made. For regression links of a joint Gaussian the curvature is the partial cross-covariance $\Sigma_{ik|j}$. See [[Lattice gauge theory]].

## Sources

- [[dennis-2026-glk-lie-algebra-links-v2]] — inverse-edge triangle holonomy in the main manuscript; triangle spectrum of the tiled routed links similar to $\boldsymbol\rho_{ijk}T\widetilde O$ in each content-link chart; second-order BCH holonomy (revision drafted by Claude Opus 5.5, float64 checks).
- [[dennis-2026-dynamic-links]] — class functions on non-compact $\mathrm{GL}(K)$ are blind to unipotent holonomy; the Frobenius defect of the reference-coordinate holonomy separates, and equals Wilson's density on $O(K)$; loops of the depth-by-token link lattice.
- [[dennis-2026-link-origin]] — triangle defect of routing logits as the loop of the head-sum link; exponential-link loops via BCH (agent-drafted, small-dimension checks).
- [[dennis-2026-link-curvature]] — triangle holonomy on causal support, frame independence of its conjugacy class, flat = recurrent, holonomy table of candidate links (agent-drafted, float64 checks at K=4).
- [[cohen-2019-gauge-cnn]] — gauge equivariance on manifolds: the kernel constraint and the parallel-transport rule whose closed-loop composition is holonomy.
- [[bronstein-2021-geometric-deep-learning]] — Erlangen-Program synthesis providing the gauge / connection / parallel-transport scaffolding.
- [[finzi-2020-lieconv]] — Lie-algebra (log-coordinate) parameterization with exp recovery, the BCH-style composition underlying non-abelian holonomy.
- [[weiler-2021-coordinate-independent-cnns]] — monograph deriving gauge equivariance from coordinate-independence plus weight-sharing, with textbook-grade transport rule and cocycle/holonomy conditions.
- [[moler-vanloan-2003-nineteen-dubious-ways]] — conditioning of the matrix exponential and the eigenvalue-method breakdown for non-normal or defective matrices; symmetric `phi` is normal and nondefective.
- [[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]] — irrep-structured features and Clebsch–Gordan coupling on which the holonomy group acts block-by-block.
- [[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]] — the curved affine-invariant SPD geometry whose transport is non-flat.
- [[absil-2008-optimization-matrix-manifolds]] — retractions and vector transports as first-order surrogates for geodesic transport.
- [[ollivier-2015-riemannian-metrics-nn]], [[amari-1998-natural-gradient]] — metric/Fisher preconditioning that makes transport reparameterization-invariant.
- [[bleecker-1981-gauge-theory-variational-principles]] — canonical bundle-connection-and-variational-principle reference behind the gauge formalism (connections, curvature, and holonomy on principal bundles).

## See also

- [[Parallel transport]]
- [[Gauge transformation]]
- [[Cellular sheaves and sheaf Laplacians]] — $H^0$ of an invertible-link sheaf is the holonomy-fixed subspace; curved links are sheaves on the 1-skeleton only.
- [[Lattice gauge theory]] — Wilson loops are lattice holonomy (the trace of transport around a plaquette)
- [[Group equivariance]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Gauge equivariant CNN]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Gauge equivariance and geometric deep learning]]
