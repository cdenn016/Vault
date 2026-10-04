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
updated: 2026-10-04
---

# Holonomy

## Unipotent blind spot and the Frobenius defect, October 3, 2026

[[dennis-2026-dynamic-links]] proves that every continuous conjugation-invariant function on the non-compact $\mathrm{GL}(K)$, $K\ge2$, takes the same value at a unipotent element as at the identity: conjugating a Jordan block by $\operatorname{diag}(1,t^{-1},\dots)$ scales its superdiagonal by $t\to0$. Such functions depend only on eigenvalues, so every eigenvalue statistic of a holonomy, including the spectral curvature reported by the `vfe3` routing-holonomy diagnostic and the bounded density $\sum_k|\lambda_k(W)-1|$ of MAgent (corrected on [[Non-flat connection and the photon analogy]]), vanishes on a shear $W=I+E_{12}\ne I$. The note measures curvature by the Frobenius defect $\tfrac12\|W-I\|_F^2$ of the reference-coordinate holonomy instead. Because the generators are reference data, that matrix and not only its conjugacy class is invariant under the passive gauge action, the defect vanishes only at $W=I$, and on $O(K)$ it equals Wilson's density $K-\operatorname{tr}W$. The extra structure it uses is the reference metric, which reduces the measurement from $\mathrm{GL}(K)$ to $O(K)$; under the reparameterization that moves frames into links it is invariant exactly for nonzero multiples of orthogonal changes, and the scalar factor acts trivially on the holonomy. The October 3 version of the note said orthogonal changes only; it was corrected on October 4.

[[multiagentelbo-2026-10-04-lie-algebra-links]] states the same blindness in the multi-agent theory (`prop:link-class-function-blindness`, `cor:link-no-invariant-defect`): no continuous conjugation-invariant loop defect on $\mathrm{GL}(K)$ separates unipotent holonomy from the identity. Its loop defect $\mathfrak Q_p=\tfrac12\operatorname{Tr}\bigl(G^{-1}(I-\rho(\mathring\Theta_p))^\top G(I-\rho(\mathring\Theta_p))\bigr)$ uses the fiber metric $G$ and is invariant under reference changes by nonzero multiples of $G$-isometries. With latent links in $\mathrm{GL}^+(K)$, the determinant of the holonomy of a closed walk in a block that is not a forest is $\exp(\sum_a\operatorname{Tr}\mathring\omega_{e_a})$, which differs from one off a Lebesgue-null hyperplane. The fixed Gaussian parent family is then empty, so the holonomy-parent score is $+\infty$ almost surely under any absolutely continuous generator law (`cor:link-holonomy-parent-almost-sure`).

## Unified exponential-link construction, October 3, 2026

The author selected Option A exponential group-valued links as the primary future GL(K) integration direction in [[dennis-2026-attention-unified]]. Causal support forbids directed cycles through distinct positions, but invertible edges allow the inverse-edge triangle $\Theta_{ik}^{-1}\Theta_{ij}\Theta_{jk}$. Its conjugacy invariants can be nontrivial for a composite link field without an independent gauge action. A constant exponential link is nonflat unless its exponential is identity; "maximally curved" in the earlier note has no specified ordering and is removed in the consolidation.

The existing VFE_3.0 working tree now includes routing-triangle diagnostics, checked by five tiny CPU tests during consolidation. This is a diagnostic path, not a new learned exponential edge field or a trained performance result. The exact head-weight ratio requires the stated inverse-map assumptions; the general map-dependent diagnostic retains $TO$ rather than assuming identity. For jointly Gaussian reference states, zero regression composition defect on every strict triple is equivalent to first-order Markov conditional independence; group holonomy additionally needs invertible regression maps.

## Coboundary monitors and link spectra in vfe3 (design record, September 28)

The design record behind [[dennis-2026-phi-natgrad]] shows that the transformer's `holonomy_deviation` and `holonomy_wilson` metrics multiply only the coboundary $\Omega_{ij}=U_iU_j^{-1}$, which closes identically, so they measure floating-point error of the stored frame pair, not curvature; it recommends relabeling them as coboundary closure residuals. The gauge-invariant content of the communication links $L_{ij}^{(h)}=U_iM_hU_j^{-1}$ is instead the simultaneous similarity class of the $M_h$, and under a causal prior the only closed loops are self-loops, whose spectra are those of $rI+\sum_h\beta_{ii}^hM_h$. See the September 20 matrix-link section below for the scope of loop products.

## Edge twists, identity links and law coherence at one base point (review, September 23, tentative)

Investigators X01 and E1 of the 2026-09-23 Theory review ([[multiagentelbo-2026-09-23-theory-streamlining-review]]) find that loop holonomy is not the only gauge-invariant link content at $c_*$. All agent frames there are points of one torsor, and with passive changes $U_i\mapsto a_i^{-1}U_i$, $\Theta_e\mapsto a_i^{-1}\Theta_ea_j$ the edge twist $H_e=U_i^{-1}\Theta_eU_j$ is invariant under the independent vertex group and changes only by one simultaneous conjugation under a change of reference point. Each single edge therefore carries a gauge-invariant conjugacy class. On a path graph, where every closed walk is a backtrack, the recomputed edge invariants $(\mathrm{tr},\det)$ were $(1.62,2.33)$ and $(-0.96,0.19)$ against $(2,1)$ for the identity. The gauge-invariant link content at one base point is the family $\{H_e\}$ modulo one simultaneous conjugation. X01 names the falsifier: if agents at $c_*$ carried separate fiber copies with no canonical identification, only loops would carry invariants.

The same review separates identity links from flat links. The manuscript's "flat links" hypothesis $\Theta_e=T_{ij}$ is the identity-link specialization (Regime I) and is strictly stronger than trivial holonomy, which only requires a coboundary $\Theta_e=V_iV_j^{-1}$. On a triangle with coboundary links and the same beliefs, the summed transported KL is 29.56 against 298.99 for $\Theta=T$, so flat and identity links are different energies.

Full-law coherence is a third agreement notion beside frame agreement ($H_\gamma=I$) and mean agreement. All transported KLs vanish exactly when the root law is stabilized by the network holonomy. In the C1 witness, three agents with law $\mathcal N(0,\Sigma)$, $\Sigma=\begin{pmatrix}4&1\\1&1\end{pmatrix}$, link $\Theta_{12}=\Sigma^{1/2}R(0.7)\Sigma^{-1/2}$ and identity links elsewhere have zero transported KL on every edge, while the loop holonomy is non-orthogonal, lies at Frobenius distance 1.655 from $I$, and fixes no nonzero vector. This agrees with the September 11 record experiment and the September 12 circle-law witness below. The new point is that coalescence driven by vanishing transported KL needs law coherence up to holonomy stabilizers, quantified over every closed walk, rather than frame agreement.

> [!note] Editorial
> The edge-twist invariant concerns what is gauge invariant in the link datum at one base point. It does not contradict the 2026-08-18 section below on detection by embedded agents, which is about what a depth-limited agent can measure.

> [!warning] Tentative: investigator recomputation, same model family, not adjudicated
> Recomputations by investigators of one model family (Claude Opus 5.5); the invariance residuals were at or below $2\times10^{-15}$.

### Incorporation in the restructured manuscript (September 24)

All three results are now statements of Chapter 2 of the main manuscript at `623e4fe` ([[multiagentelbo-2026-09-24-theory-restructure]]), the propositions tagged ESTABLISHED with their proofs in the chapter, alongside the definitions they use. In the manuscript's convention $u_i=\sigma\cdot U_i^{-1}$, `prop:geo-edge-twist-invariance` defines the per-edge twist $\mathring\Theta^x_e=U_i^{-1}\Theta^x_eU_j$ of an edge copy $e:j\to i$ and proves that it is unchanged by arbitrary passive re-expressions, that a change of reference point or an active automorphism conjugates every twist by one common element, and that two link data sets on the same multigraph are related by one active automorphism exactly when their twist tuples are related by one simultaneous conjugation. `def:geo-graph-flat-links` separates graph-flat links (trivial holonomy on every closed walk) from frame-aligned links $\Theta^x_e=T_{ij}=U_iU_j^{-1}$, and `rem:geo-flatness-strictness` shows that frame alignment implies graph flatness but not conversely: on two vertices joined by one edge copy every closed walk is a backtrack, so every link is graph flat while its edge class can differ from the identity.

`def:geo-law-coherence` and `prop:geo-three-agreements` make law coherence the third agreement. Laws on a connected internal multigraph are law coherent exactly when $q_{i_0}$ is fixed by $\widehat\rho_x(\mathrm{Hol}^x(p))$ for every closed internal walk $p$ at $i_0$ and the other laws are its transports. Law coherence implies agreement of every equivariant statistic, and the converse fails for the mean; frame agreement neither implies nor is implied by law coherence or mean agreement; and with several independent cycles a condition on one loop is necessary but not sufficient. The C1 witness above is part of the proposition. The review's numerical instances (the path-graph invariants and the energies 29.56 and 298.99) are not in the manuscript. Chapter 10 cites the proposition for the law coherence of its holonomy-conditioned reconstruction (`thm:cg-holonomy-kl-marginal`) and adds a single-point operational record sensitive to network-loop holonomy (`thm:cg-loop-operational-holonomy`).

> [!warning] Status
> Manuscript statements with proofs, written and checked by Claude Opus 5.5 agents with their own scripts; no cross-model check (the author's choice) and not adjudicated.

## Matrix-link loop observables, September 20, 2026

[[dennis-2026-glk-matrix-links-2026-09-20]] distinguishes the flat vertex-frame connection $\Omega_{ij}=U_iU_j^{-1}$ from communication links $L_{ij}^{(h)}=U_iO_hT_hU_j^{-1}$. Any declared closed product of matrices obeying $B_{ij}'=g_iB_{ij}g_j^{-1}$ transforms by conjugation at its base site, and its trace is invariant without requiring inverse links. Such a product may record gain or rank loss; nonidentity does not establish curvature of $\Omega$ or holonomy of an invertible connection.

For a shared unweighted head, a path with $r$ edges is $U_{i_0}(OT)^rU_{i_r}^{-1}$, so paths with the same endpoints and length coincide. Causal attention has no directed cycles through distinct token positions. These limits must accompany any proposed loop diagnostic. See [[Lattice gauge theory]] for the matrix-link construction and its distinction from group-valued parallel transport.


## Triangle defect of attention routing, October 2, 2026

[[dennis-2026-link-origin]] shows that the multi-head operator $\mathcal C_{ij}=U_iOB_{ij}TU_j^{-1}$ is generically a $\mathrm{GL}(K)$ link, so loops with one reversed edge exist. For $TO=I$ the loop is $U_iO(\bigoplus_h\beta_{ij}\beta_{jk}/\beta_{ik}\,I_d)O^{-1}U_i^{-1}$, and for routing $\beta=\pi e^{-D/\kappa}/Z$ the log-holonomy of each head is
$$-\frac{D_{ij}+D_{jk}-D_{ik}}{\kappa}+\log\frac{\pi_{ij}\pi_{jk}}{\pi_{ik}}-\log Z_j,$$
the triangle defect of the routing costs offset by the intermediate normalizer. Because the KL has no triangle inequality, and here compares query with key laws under different maps, the defect has no definite sign. For the exponential link with commuting generators the loop is $U_iO\exp(B_{ij}+B_{jk}-B_{ik})O^{-1}U_i^{-1}$, and in general it follows the [[Baker-Campbell-Hausdorff formula]] series. The note computes the defect only from formulas, checked in float64 at $K=6$; it has not been measured in a trained model, and reading attention weights as an abelian connection is an interpretation. See [[Lattice gauge theory]].

## Nonlinear adaptive cyclic formation, September 13

[[multiagentelbo-2026-09-13-nonlinear-adaptive-attention-rg]] constructs, for every fixed finite L>=2, nonlinear cyclic coalescence with exact marked parents and actual-law model learning. A model-posterior source row changes by TV greater than 0.37, and physical and optimizing hidden conditionals change by KL greater than 1/200 on the same 2/epsilon horizon. Conditional KL is O_L(epsilon^2), with separate complete-score and retained-path bounds. Every parent starts from the full actual retained joint law.

Source assignments are retained discrete coordinates with zero mobility. Their recognition masses stay fixed; changing model-posterior attention is distinguished from the actual recognition conditional that weights the marginal force. This admission repairs the collapsed proposal's marked-activation gap. Supplied contrasts, internal-neighbor support, calibration, small fixed standardized nonlinearity, and a shrinking amplitude/temperature regime remain explicit. All loops survive and base transport remains deferred. Earlier dated sections retain their original scopes.

> [!note] Current scope, September 11, 2026
> The current [[multiagentelbo-2026-09-11-formation|finite relational-record theorem]] exhibits nontrivial cycle holonomy with exactly matching singleton marginals and zero transported marginal KL. Record equivalence agrees with gauge equivalence only for the stated noisy relational experiment and its admitted preparations. Transition cocycles and independently specified connection links must not be conflated. Also, a flat connection can have nontrivial holonomy around a noncontractible loop: the older statement below identifying every nontrivial holonomy with curvature needs this topological qualification. [[multiagentelbo-2026-09-11-continuum]] keeps discrete loops and continuum curvature claims separate.


## Retained loops in adaptive coalescence, September 12

[[multiagentelbo-2026-09-12-adaptive-cyclic-rg]] proves cyclic Gaussian formation while retaining every original triangle circulation through each parent. No independent Wilson or curvature penalty is imposed. The translation-law witness has trivial stabilizers, so small mismatch entails small fluctuating frustrated holonomies; this is a representation-specific property, not a general flatness condition. Its separate circle-law calculation permits exact coherent nonidentity stabilizer holonomy. Full correlated cut-mark kernels survive reduction rather than being replaced by conditional means. The construction concerns interaction loops above one fixed base point, not transport across the contextual base.

## Definition

Holonomy measures the failure of a connection to be path-independent. Given a manifold equipped with a connection (a rule for [[Parallel transport]] — moving a vector, frame, or belief along a curve while keeping it "as constant as the geometry allows"), transporting an object around a **closed loop** generally does not return it unchanged: it comes back rotated, scaled, or otherwise transformed by some group element. That net transformation is the **holonomy** of the loop. The set of all such transformations, taken over all loops based at a point, forms a group — the **holonomy group** — which is a subgroup of the connection's structure (gauge) group.

Concretely, if a connection is specified by a Lie-algebra-valued one-form (a "gauge potential") `A`, the holonomy of a loop `γ` is the path-ordered exponential

```
Hol(γ) = P exp( -∮_γ A )  ∈ G,
```

an element of the structure group `G`. The connection is **flat** (curvature zero) exactly when the holonomy of every contractible loop is the identity; then transport is path-independent and the geometry is said to be **holonomic**. Nontrivial holonomy is equivalently the integrated effect of **curvature**: by the non-abelian Stokes / Ambrose–Singer theorem, the holonomy around an infinitesimal loop is the curvature two-form evaluated on the loop's area. Holonomy is therefore the global, observable shadow of local curvature.

## Why it matters here

Generic non-abelian connections and curved SPD manifolds can have nontrivial holonomy. The realized transformer Regime-I connection is more restrictive: $\Omega_{ij}=U_iU_j^{-1}$ telescopes on every closed loop, so $H=I$ exactly despite the noncommutativity of $\mathrm{GL}(K)$. Nontrivial model holonomy requires an independent-edge or otherwise nonflat Regime-II connection.

## Detection by embedded agents (2026-08-18)

Holonomy lives on loops, so an agent whose visibility is its Markov blanket cannot measure it
directly: depth-1 sight closes no loop, and even depth-2 sight only suffices given
*provenance* — comparing two routes from an identified common source ($\Omega_{ij}\Omega_{jk}$
against $\Omega_{ik}$ requires knowing both messages originate at $k$). What an embedded agent
does have access to are gauge-invariant *signatures*, each confounded with dynamics:

- **Irreducible frustration.** On a loop with nontrivial holonomy no belief assignment zeroes
  all pairwise transported divergences simultaneously — the agent experiences an unresolvable
  residual free energy no local move removes. This is source-backed in the finite lab: a block
  with nontrivial holonomy has an empty orbit-family fixed sector, so frustration *is* the
  local shadow of loop curvature.
- **Loop non-closure among identified peers** — A agrees with B, B with C, C disagrees with A —
  the smallest observable Wilson-loop signature, available at depth 2 with provenance.
- **Self-return distortion**: one's own past state coming back transformed around a loop (the
  telephone game is a holonomy experiment run on the social connection), available at depth 1
  with memory and self-recognition.

The confound is the geometric-versus-dynamical-phase problem: an embedded agent cannot freeze
the other agents' updates, so it cannot cleanly factor observed loop distortion into connection
curvature and source dynamics. In the theory the clean measurement belongs to the level above:
the mark-carrying parent retains its block's interior holonomy groups as declared data, and C2
conserves the Wilson charge under blocking, so the coarse level literally carries as *local*
marks what no constituent could see — hierarchy is the theory's holonomy-measurement
instrument, one more face of "a level-$\ell$ parent with depth-1 sight commands depth-$r^\ell$
in the fine graph" ([[Meta-agents and hierarchical emergence]]).

> [!note] Editorial: the frustration/empty-fixed-sector fact and mark-retention/C2 are
> implemented, tested lab constructions — but single-implementation and not independently
> verified, so tentative like the rest of the 2026-08-17/18 lab chain; the human-scale
> readings (intransitivity detection, the telephone game as a Wilson loop) are interpretive
> glosses, not measurements.

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
- [[multiagentelbo-2026-10-04-lie-algebra-links]] — class-function blindness and the metric loop defect in the multi-agent theory; latent noncompact links make the holonomy-parent score infinite almost surely.

## See also

- [[Parallel transport]]
- [[Gauge transformation]]
- [[Lattice gauge theory]] — Wilson loops are lattice holonomy (the trace of transport around a plaquette)
- [[Group equivariance]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Gauge equivariant CNN]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Gauge equivariance and geometric deep learning]]
