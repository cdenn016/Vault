---
type: concept
title: "GL(K) gauge group"
aliases:
  - "glkgaugegroup"
  - "GL(K) group"
  - "General linear gauge group"
  - "GL(K,R)"
  - "GL+(K)"
tags:
  - cluster/gauge-theory
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-07-09
---

# GL(K) gauge group

## Definition

The **general linear group** $\mathrm{GL}(K,\mathbb{R})$ is the group of invertible $K\times K$ real matrices under multiplication. In the gauge-theoretic variational-free-energy program it is the **structure (gauge) group** of the belief bundle: each token carries an internal $K$-dimensional feature frame, and $\mathrm{GL}(K)$ is the group of admissible *change-of-frame* maps acting on that frame. Because the model never commits to a canonical frame, a frame may be chosen independently at each token — a *position-dependent* (local) group element $g(x)\in\mathrm{GL}(K)$ — which is exactly the defining move of a [[Gauge transformation]]. The set of all such assignments $x\mapsto g(x)$ is the gauge group; demanding that the free-energy objective and predictions be invariant under it is what makes the architecture *gauge-theoretic* ([[gl-k-attention|GL(K) attention manuscript]], [[bronstein-2021-geometric-deep-learning]]).

The program works with the **identity component** $\mathrm{GL}^+(K)=\{g:\det g>0\}$, the orientation-preserving invertible maps. This is forced by the frame parameterization: gauge elements are generated as $g=\exp(\phi)$ from a matrix $\phi$ in the Lie algebra, and the matrix exponential always lands in the identity component ($\det\exp(\phi)=e^{\operatorname{tr}\phi}>0$). The gauge invariance of the divergence terms, however, is broader: the manuscript's $\mathrm{GL}(K)$ invariance theorem (below) holds for *any* $\det\Omega\neq0$, so the full $\mathrm{GL}(K)$ — both orientation components — acts as a symmetry of the inference, while the $\exp(\phi)$ parameterization realizes only $\mathrm{GL}^+(K)$ ([[gl-k-attention|GL(K) attention manuscript]]).

### The Lie algebra gl(k)

The **Lie algebra** $\mathfrak{gl}(K)$ is the tangent space to $\mathrm{GL}(K)$ at the identity: *all* $K\times K$ real matrices (no invertibility constraint), equipped with the matrix commutator $[\phi_1,\phi_2]=\phi_1\phi_2-\phi_2\phi_1$ as its Lie bracket. The exponential map supplies unconstrained differentiable coordinates, but over the reals $\operatorname{image}(\exp)$ is a proper subset of $\mathrm{GL}^+(K)$ rather than the whole identity component. [[gl-k-attention-2026-07-09-review-revision]]

Because two gauge elements compose as
$$
\exp(\phi_1)\exp(\phi_2)=\exp\!\Big(\phi_1+\phi_2+\tfrac12[\phi_1,\phi_2]+\cdots\Big),
$$
composing transformations directly in the algebra requires the [[Baker-Campbell-Hausdorff formula|Baker–Campbell–Hausdorff]] series; finite truncation is a local approximation. The configured regularized Cartan/Killing object is a frame preconditioner, not a full-$\mathrm{GL}(K)$-invariant Fisher natural gradient. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial: $\mathfrak{gl}(K)$ is the *full* matrix algebra precisely because $\mathrm{GL}^+(K)$ is open in $\mathbb{R}^{K\times K}$ — its tangent space at $I$ is the whole ambient space. This is what distinguishes $\mathfrak{gl}(K)$ from the constrained algebras (skew-symmetric $\mathfrak{so}(K)$, traceless $\mathfrak{sl}(K)$) of the compact/special subgroups, and is why the unconstrained $\phi$ parameterization is available without projection.

## The quotient GL(K)/O(K) and the SPD cone

The single most load-bearing fact connecting the gauge group to the rest of the program is the homogeneous-space identification
$$
\mathrm{SPD}(K)\;\cong\;\mathrm{GL}(K,\mathbb{R})/O(K)\;\cong\;\mathrm{GL}^+(K)/SO(K),
$$
where $\mathrm{SPD}(K)$ is the cone of symmetric positive-definite $K\times K$ matrices — the space the program's belief **covariances** $\Sigma$ live in. This realizes the SPD cone as a **Riemannian symmetric space of noncompact type**: $\mathrm{GL}(K)$ acts transitively on the cone by the **congruence (sandwich) action** $\Sigma\mapsto M\,\Sigma\,M^{\top}$, the orbit of the identity $I$ is the whole cone, and the *stabilizer* of $I$ is the orthogonal group $O(K)$ (since $M\,I\,M^{\top}=I\iff M\in O(K)$). Quotienting the group by that stabilizer therefore gives the cone ([[Symmetric spaces and the SPD cone]], [[helgason-1978-symmetric-spaces]], [[pennec-2006-affine-invariant-tensor]]).

This is the source of three structural facts the program uses for free, rather than imposing by hand:

- **The covariance geometry falls out of group structure.** The invariant Riemannian metric on the quotient $\mathrm{GL}(K)/O(K)$ is exactly the **affine-invariant metric** $\langle A,B\rangle_\Sigma=\operatorname{tr}(\Sigma^{-1}A\,\Sigma^{-1}B)$ on the cone, with matrix-exp/log geodesics through the $\Sigma^{1/2}$-sandwich and nonpositive curvature ([[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]). Congruence invariance and nonpositive curvature are consequences of the quotient, not accidents of a metric choice ([[Symmetric spaces and the SPD cone]]).
- **Frames and covariances are acted on by the *same* group.** A gauge frame $\phi$ lives in $\mathfrak{gl}(K)$ and a covariance $\Sigma$ lives on the cone; the very group whose left action realizes a frame change acts on covariances by congruence. The gauge action on a belief's covariance is therefore the sandwich $\Sigma\mapsto g\,\Sigma\,g^{\top}$, which preserves positive-definiteness ([[Gauge transformation]], [[Symmetric spaces and the SPD cone]]).
- **The Cartan decomposition separates rotation from scale.** The algebra splits as $\mathfrak{gl}(K)=\mathfrak{o}(K)\oplus\mathrm{Sym}(K)$ — antisymmetric matrices (the compact $\mathfrak{k}$, which fix $\Sigma=I$) plus symmetric matrices (the directions $\mathfrak{p}$ that move along the cone). Geodesics on the cone are one-parameter subgroups exponentiated through $\mathfrak{p}$ ([[Symmetric spaces and the SPD cone]], [[Killing form]]).

## Reaching the other orientation: the det<0 component

The $\exp(\phi)$ parameterization realizes only $\mathrm{GL}^+(K)$ (Definition above), so the orientation-reversing component $\{\det g<0\}$ — which the invariance theorem *admits* as a symmetry — is **unreachable** by the continuous frame parameterization. The program closes this gap **two ways** — by storing the frame as a group element, or (more cheaply) by prepending a reflection to $\exp(\phi)$ — each paired with a discrete learnable move ([[2026-07-08-omega-direct-detsign-buildout]], [[2026-07-08-phi-reflection-buildout]]):

- **`omega_direct` — store the group element, not the algebra.** Rather than $g=\exp(\phi)$, `gauge_parameterization="omega_direct"` stores each token's frame as a $\mathrm{GL}(K)$ element $U_i$ directly and transports by the stored cocycle $\Omega_{ij}=U_iU_j^{-1}$. Because $U$ is stored rather than exponentiated it can hold *either* orientation, and a group-manifold retraction keeps M-step updates on $\mathrm{GL}^+(K)$ within whichever sheet $U$ occupies.
- **The two sheets are separated by a free-energy barrier, not just topology.** As $\det U\to 0$ the congruence $\Sigma\mapsto U\Sigma U^\top$ collapses a covariance direction, so every $\Sigma^{-1}$ / $\log\det\Sigma$ term diverges (clamped, flat gradient). Continuous VFE descent therefore cannot cross $\det=0$; a token stays in whichever sheet it starts in. The frame factors as $U=R\,U^0$ with $U^0\in\mathrm{GL}^+(K)$ continuous and $R$ a discrete reflection ($\det R=-1$), which must be handled combinatorially.
- **Learnable orientation (`omega_reflection="metropolis"`).** The discrete reflection is *learned* by a $\Delta F$-gated Metropolis move — a coordinate-descent split where gradient descent owns $\mathrm{GL}^+(K)$ and an accept/reject sweep owns the discrete $\pi_0(\mathrm{GL}(K))=\mathbb{Z}/2$ det-sign, both minimizing the *same* free energy. Because $R$ is an orthogonal involution the proposal is symmetric (plain Metropolis $\min(1,e^{-\Delta F/T})$, no Hastings ratio). Under a **diagonal** covariance family the move is near-inert — $R=\operatorname{diag}(-1,1,\dots)$ leaves the (squared) diagonal congruence exactly invariant, so $\Delta F\approx 0$ — so it carries information only with a full / off-diagonal covariance or a low temperature ([[2026-07-08-omega-direct-detsign-buildout]]).
- **The cheaper route: $R\exp(\phi)$ on the phi path (`phi_reflection="metropolis"`).** Rather than switch parameterization, keep $\exp(\phi)$ for the continuous part and prepend a per-token reflection: $g_i=R_i\exp(\phi_i)$, so $\det g_i=\det(R_i)\,e^{\operatorname{tr}\phi_i}=-e^{\operatorname{tr}\phi_i}<0$. ($\det\exp(\phi)=e^{\operatorname{tr}\phi}>0$ is *always* positive — that is exactly why $\exp(\phi)$ alone is confined to $\mathrm{GL}^+(K)$; the sign flip is entirely the prefactor.) This realizes the coset decomposition $\mathrm{GL}(K)=\{I,R\}\cdot\mathrm{GL}^+(K)$ and reaches the $\det<0$ sheet with a single sign **bit** per token — a non-differentiable buffer flipped by the *same* Metropolis move — rather than a stored $K\times K$ element. Transport folds as $\Omega_{ij}\to R_i\Omega_{ij}R_j$ and stays flat. Its reach is $R\cdot\mathrm{image}(\exp)$ (the two sheets' exp-images), so unlike `omega_direct` it misses the non-exp interior of $\mathrm{GL}^+(K)$; in exchange it reuses the full $\exp(\phi)$ / [[Baker-Campbell-Hausdorff formula|BCH]] / [[Killing form|Killing]] machinery ([[2026-07-08-phi-reflection-buildout]]).

## Key results

**The congruence action is well-posed.** Two elementary matrix-analysis lemmas make $\Sigma\mapsto M\Sigma M^{\top}$ usable: by **Sylvester's law of inertia**, congruence preserves positive-definiteness, so a transported covariance is still a valid covariance; and congruence scales the determinant by $(\det M)^2$ ([[horn-johnson-2013-matrix-analysis]]). The latter is the identity invoked whenever a Gaussian normalization transforms under a gauge change.

**$\mathrm{GL}(K)$ gauge invariance of the divergence.** The manuscript proves that for Gaussians $P,Q$ on $\mathbb{R}^K$ and any $\Omega\in\mathrm{GL}(K)$,
$$
D_{\mathrm{KL}}\!\left(\Omega_*P\,\|\,\Omega_*Q\right)=D_{\mathrm{KL}}\!\left(P\,\|\,Q\right),
$$
because the $(\det\Omega)^2$ Jacobian factors cancel identically; the result extends to all $f$-divergences, so a transport map need only satisfy $\det\Omega\neq0$ for the full $\mathrm{GL}(K)$ to act as a gauge symmetry of the inference ([[gl-k-attention|GL(K) attention manuscript]]). This is the formal guarantee that attention scores — built from KL divergences between transported beliefs — are invariant to local frame choice, the property that earns the name "gauge."

**Vertex-frame transport has trivially vanishing holonomy.** The program's standard transport between tokens $i$ and $j$ factorizes through the gauge frames as $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$, which satisfies the cocycle identity $\Omega_{ij}\Omega_{jk}\Omega_{ki}=I$ as an algebraic identity. The resulting gauge-transformer connection is therefore **flat**: its reconstructed [[Holonomy]] around any loop vanishes. A standard transformer has no transport variable or intrinsic holonomy; flatness applies only to the imposed identity-transport comparison point. A relaxed extension $\Omega_{ij}=\exp(\phi_i)\exp(\delta_{ij}G)\exp(-\phi_j)$ promotes the gauge model to nontrivial holonomy, reserved for the companion work ([[gl-k-attention|GL(K) attention manuscript]], [[Parallel transport]], [[Holonomy]]). [[gl-k-attention-2026-07-09-review-revision]]

**No bi-invariant metric on the frame group.** Unlike the covariance side, where the cone inherits a canonical invariant metric from the quotient, the *frame* group $\mathrm{GL}^+(K)$ is noncompact and non-abelian and so — by Milnor's theorem — admits **no bi-invariant metric** ([[milnor-1976-left-invariant-metrics]]). The clean symmetric-space structure on the covariance side has no automatic counterpart on the frame side, which is why the choice of inner product on $\mathfrak{gl}(K)$ (e.g. the Killing-form preconditioner) is a genuine modeling decision rather than a foregone conclusion.

## Relevance to this research

$\mathrm{GL}(K)$ organizes transported-Gaussian attention. The Regime-I vertex cocycle makes loop transport flat but does not force pairwise identity. Identity follows in the shared-frame reduction, or when one edge-independent constant occurs on every attended edge including a self edge or on all three edges of a transitive triple. The resulting isotropic score is identity-bilinear with a key-norm bias. A general learned $W_QW_K^\top$ is structural rather than transport-derived. [[gl-k-attention-2026-07-09-review-revision]]

The quotient $\mathrm{GL}(K)/O(K)\cong\mathrm{SPD}(K)$ supports the affine-invariant geometry of full covariances and their Fisher/AIRM natural gradients. It does not identify the configured frame conditioner with that Fisher metric. The live diagonal family is closed under congruence only for monomial transports, so a general frame action is projected or approximate. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[gl-k-attention|GL(K) attention manuscript]] — the canonical source: $\mathrm{GL}(K)$ as structure group of the belief bundle, the $\mathrm{GL}(K)$ invariance theorem for KL/$f$-divergences, the $\exp(\phi)$ frame parameterization restricting to $\mathrm{GL}^+(K)$, and the vertex-frame transport / vanishing-holonomy lemma.
- [[2026-07-08-omega-direct-detsign-buildout]] — the `omega_direct` element-store parameterization and the learnable ($\Delta F$-gated Metropolis) det-sign that reach the $\det<0$ component the $\exp(\phi)$ parameterization cannot; the free-energy barrier separating the sheets; and the diagonal-family / gauge-covariance-vs-frame-use findings.
- [[2026-07-08-phi-reflection-buildout]] — the cheaper $R\exp(\phi)$ route: a learnable per-token reflection *bit* prepended to $\exp(\phi)$ that reaches $R\cdot\mathrm{image}(\exp)$ on the default phi path (one bit vs a stored $K\times K$ element; misses the non-exp interior `omega_direct` reaches). Same Metropolis move; the coset decomposition $\mathrm{GL}(K)=\{I,R\}\cdot\mathrm{GL}^+(K)$.
- [[Symmetric spaces and the SPD cone]] — the quotient $\mathrm{GL}(K)/O(K)\cong\mathrm{SPD}(K)$, the congruence action with $O(K)$ stabilizer, the Cartan decomposition, and the affine-invariant metric.
- [[helgason-1978-symmetric-spaces]] — canonical reference for symmetric spaces $G/K$ and the identification of the SPD cone with the noncompact $\mathrm{GL}(K)/O(K)$.
- [[pennec-2006-affine-invariant-tensor]] — the affine-invariant metric as the invariant Riemannian structure of the cone, on which the gauge congruence acts.
- [[bhatia-2007-positive-definite-matrices]] — SPD geometry: geodesics, geodesic distance, geometric mean.
- [[horn-johnson-2013-matrix-analysis]] — Sylvester's law of inertia (congruence preserves definiteness) and the $(\det M)^2$ determinant-under-sandwich identity.
- [[hall-2015-lie-groups]] — matrix Lie groups, the $\mathfrak{gl}(K)$ Lie algebra, the exponential map, and the Lie-algebra correspondence.
- [[milnor-1976-left-invariant-metrics]] — no bi-invariant metric on the noncompact non-abelian frame group $\mathrm{GL}^+(K)$.
- [[bronstein-2021-geometric-deep-learning]] — gauges and local frame equivariance as a unifying blueprint for deep nets.
- [[sengupta2017gauge]], [[sengupta-2016-neuronal-gauge]] — neuronal-gauge-theory precedent: approximate Bayesian inference as a gauge theory.
- [[wang-2023-riemannian-self-attention-spd]] — nearest SPD-valued self-attention prior art.

## See also

- [[Gauge transformation]]
- [[Gauge Theory]]
- [[GL(K) gauge-equivariant attention]]
- [[Symmetric spaces and the SPD cone]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Killing form]]
- [[Baker-Campbell-Hausdorff formula]]
- [[Holonomy]]
- [[Parallel transport]]
- [[Group equivariance]]
- [[Irreducible representation]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[VFE Transformer Program]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
