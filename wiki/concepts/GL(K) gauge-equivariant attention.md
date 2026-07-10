---
type: concept
title: "GL(K) gauge-equivariant attention"
aliases:
  - "glkgaugeequivariantattention"
  - "GL(K) attention"
  - "Gauge-equivariant attention"
  - "Gauge-theoretic attention"
tags:
  - cluster/gauge-theory
  - cluster/attention
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-07-10
---

# GL(K) gauge-equivariant attention

**GL(K) gauge-equivariant attention** is the central construction of the program's
[[gl-k-attention|GL(K) attention manuscript]] (*"Attention as Gauge-Theoretic Variational
Inference"*). It constructs an attention rule as **variational inference over information
sources** and compares scoped limits of that rule with transformer attention: each token is a Gaussian "agent"
$q_i=\mathcal N(\mu_i,\Sigma_i)$ living on a statistical fiber bundle, and the attention weight
between tokens is *derived* by minimizing a multi-agent [[Variational free energy]]. The
mechanism is built so that those weights are **invariant** to a per-token change of feature
basis drawn from the general linear group $\mathrm{GL}(K)$ — the structure (gauge) group of the
construction (see [[GL(K) gauge group]]). This page states the construction precisely and
records what is proven versus conjectured. The analytic attention derivation is a belief-channel
reduction. The retained empirical sweep is instead a same-scale two-channel route with one model
refinement before one belief refinement. [[gl-k-attention-2026-07-09-review-revision]]

## Setup: tokens as Gaussian agents on a bundle

Fix a feature dimension $K$. Each token $i$ carries a belief $q_i=\mathcal N(\mu_i,\Sigma_i)$
with mean $\mu_i\in\mathbb R^K$ and covariance $\Sigma_i$ a **symmetric positive-definite (SPD)**
matrix. The covariance is the *belief geometry*: an agent that is confident along some directions
and uncertain along others is a non-isotropic $\Sigma_i$. These covariances live on the SPD cone
$\mathrm{SPD}(K)$, which is the symmetric space $\mathrm{GL}(K)/O(K)$
([[Symmetric spaces and the SPD cone]]); the affine-invariant Riemannian structure of that cone is
the geometry the program uses to move, average, and compare beliefs
([[SPD-manifold geometry and Riemannian optimization]]).

Over the token base sits a principal $G$-bundle whose fibers are statistical manifolds; the agents
are sections of it ([[Agents as fibre-bundle sections]]). Each token additionally carries a **gauge
frame** $U_i\in\mathrm{GL}(K)$ — a local, invertible change of basis for the $K$-dimensional
feature space. In the manuscript's real exponential chart the frames are generated from
$\phi_i\in\mathfrak{gl}(K)$ as $U_i=\exp(\phi_i)$. This chart reaches only
$\operatorname{image}(\exp)$, a proper subset of $\mathrm{GL}^+(K)$, even though the ambient
divergence theorem below applies to every invertible frame. The transport that carries token $j$'s
frame into token $i$'s frame is the composition

$$\Omega_{ij} \;=\; \exp(\phi_i)\,\exp(-\phi_j)\;=\;U_i U_j^{-1}\in\mathrm{GL}(K).$$

This $\Omega_{ij}$ is the bundle's discrete analogue of [[Parallel transport]]: it is the object
applied to a neighbor's belief before that belief is compared to one's own. The full-Gaussian
pushforward is exact under common $\mathrm{GL}(K)$ changes of frame. The live diagonal covariance
family is closed exactly only under monomial transports; a general congruence leaves that family and
therefore requires projection or approximation. [[gl-k-attention-2026-07-09-review-revision]]

## Definition: the congruence-transformed, GL(K)-invariant score

In ordinary dot-product attention the score is the inner product $Q_iK_j^\top$ of a query and a
key ([[vaswani-2017-attention]], [[Attention mechanisms — theory and positional structure]]).
Gauge-equivariant attention replaces this inner product with an **information divergence between
transported beliefs**. The generalized attention weight is

$$\beta_{ij} \;=\; \operatorname{softmax}_j\!\Big(-\,\tfrac1\tau\,
D_{\mathrm{KL}}\!\big[\,q_i \,\big\|\, \Omega_{ij}\,q_j\,\big]\Big),$$

where $\Omega_{ij}q_j$ denotes the pushforward of the neighbor's Gaussian under the transport map,
$\tau$ is a temperature, and the softmax normalizes over candidate sources $j$. This rule is not
posited — it is **derived** from the variational free energy of a mixture-of-sources generative
model in which agent $i$ infers which neighbor generated its state; the KL term arises exactly and
the softmax is the closed-form (KKT) solution of the constrained optimization over the categorical
source-selection posterior ([[gl-k-attention]]).

Two geometric facts make this well posed and frame-independent.

**Congruence on covariances.** A frame change $G\in\mathrm{GL}(K)$ acts on a covariance not by
similarity but by the **congruence (sandwich) action** $\Sigma\mapsto G\,\Sigma\,G^\top$. This is
the action under which the SPD cone is the orbit of the identity and $O(K)$ the stabilizer, i.e.
the very action that realizes $\mathrm{SPD}(K)=\mathrm{GL}(K)/O(K)$
([[Symmetric spaces and the SPD cone]], [[pennec-2006-affine-invariant-tensor]],
[[bhatia-2007-positive-definite-matrices]]). Transporting a neighbor's belief therefore sends
$\mu_j\mapsto\Omega_{ij}\mu_j$ and $\Sigma_j\mapsto\Omega_{ij}\Sigma_j\Omega_{ij}^\top$ — the
congruence keeps a covariance a covariance (Sylvester's law of inertia) and scales its determinant
by $(\det\Omega_{ij})^2$.

**Frame invariance of the score.** The query/key inner product, read through this geometry, becomes
the congruence-transformed quadratic form of the KL between two Gaussians. The key theorem of the
manuscript is that this score is invariant under a *common* gauge change:

> [!important] Theorem (GL(K) gauge invariance)
> For Gaussians $P,Q$ on $\mathbb R^K$ and any $\Omega\in\mathrm{GL}(K)$,
> $$D_{\mathrm{KL}}(\Omega_*P\,\|\,\Omega_*Q)=D_{\mathrm{KL}}(P\,\|\,Q),$$
> because the $(\det\Omega)^2$ Jacobian factors from the two Gaussian normalizations cancel
> identically. The result extends to **all $f$-divergences**, so the transport need only satisfy
> $\det\Omega_{ij}\neq0$ — the full $\mathrm{GL}(K)$ acts as a gauge symmetry of the attention
> scores ([[gl-k-attention]]).

This is the precise sense in which the attention is "gauge-equivariant": the per-token frames
$U_i\in\mathrm{GL}(K)$ are gauge degrees of freedom, and the scores — hence the attention pattern —
are unchanged when every frame is left-multiplied by a common $\mathrm{GL}(K)$ element. The
information-divergence form is what buys this invariance; a raw Euclidean dot product would not be
congruence-invariant. The invariance is the discrete-geometry counterpart of the classical
statement that divergences are coordinate-free on a [[Statistical manifold]]
([[cencov-1982-statistical-decision-rules]], [[amari-2016-information-geometry-applications]]),
specialized here to the linear-frame ($\mathrm{GL}(K)$) reparameterizations the bundle allows.

## Key results

- **Attention is derived, not assumed.** The full KL-plus-softmax rule above follows from a
  multi-agent VFE on a principal bundle with statistical-manifold fibers; the softmax is the KKT
  solution for the source-selection posterior and the KL is exact ([[gl-k-attention]],
  [[Variational free energy]]).

- **The shared-frame Regime-I reduction is narrower than standard attention.** The vertex cocycle
  makes loop transport flat but does not force pairwise identity. If one transport is constant on
  every attended edge including a self edge, or on all three edges of a transitive triple, then
  $\Omega_{ij}=I$. With isotropic covariance, the Gaussian KL then gives an identity-bilinear score
  plus a key-norm bias. An arbitrary learned $M=W_QW_K^\top$ is an additional structural map, not a
  transport factor recovered from this limit. [[gl-k-attention-2026-07-09-review-revision]]

- **Architectural choices can be compared with the geometry.** Approximately constant key norms can
  cancel the key-norm bias in the strict identity-transport reduction, but this is not a derivation of
  LayerNorm or of a general QK metric;
  [[Multi-head attention]] is a block-diagonal restriction of the gauge algebra
  $\bigoplus_a\mathfrak{gl}(d_{\mathrm{head}})$; RoPE positional encoding is reinterpreted as
  position-dependent gauge frames; and ALiBi/T5/causal biases are non-uniform attention priors
  $\pi_j$ entering the logits additively as $+\log\pi_j$ ([[gl-k-attention]],
  [[Attention mechanisms — theory and positional structure]]).
  [[gl-k-attention-2026-07-09-review-revision]]

- **Covariance fixed point and SPD dynamics.** Minimizing the free energy in $\Sigma_i$ yields the
  matrix precision fixed point
  $\Sigma_i^{-1}=\tfrac12\big[\Sigma_{p,i}^{-1}+\sum_j\beta_{ij}(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}\big]$:
  each agent's precision is a $\beta$-weighted blend of its prior precision and its neighbors'
  *transported* precisions — manifest [[Precision weighting]]. Updates to $\Sigma$ are taken as
  natural-gradient steps with an SPD-manifold retraction ([[SPD-manifold geometry and Riemannian optimization]],
  [[Natural gradient]], [[Fisher information metric]]).

- **Flat-bundle (vanishing holonomy) regime.** The gauge transformer's vertex-frame transport
  satisfies the cocycle identity $\Omega_{ij}\Omega_{jk}\Omega_{ki}=I$ as an *algebraic*
  identity, so its Regime-I [[Holonomy]] vanishes. A standard transformer has no transport
  variable or intrinsic holonomy; only the imposed identity-transport comparison point is flat.
  An edge-relaxed extension
  $\Omega_{ij}=\exp(\phi_i)\exp(\delta_{ij}G)\exp(-\phi_j)$ promotes the bundle to non-trivial
  holonomy (Regime II), reserved for the companion participatory program ([[participatory-it-from-bit]]).
  No nonzero Regime-I holonomy exponent exists. [[gl-k-attention-2026-07-09-review-revision]]

- **Forward-KL uniqueness is conditional.** For a fixed admissible witness, the density-ratio range
  must contain a nonempty open essential interval, or overlapping configurations must identify their
  integration constants. Under that richness condition, closure selects the positive ray
  $f_c(t)=c(t\log t-t+1)$ up to divergence-null affine terms. The convention $f''(1)=1$, or fixed
  exponents and coefficients, sets $c=1$. A diagonal family under general transport does not
  automatically supply the required witness. [[gl-k-attention-2026-07-09-review-revision]]

- **The nested attention envelope uses optimized costs, not a differentiated product.** For
  $F_i(\beta_i)=\min_{q_i}\{D_{\mathrm{KL}}(q_i\|p_i)+\sum_j\beta_{ij}C_{ij}(q_i)\}$,
  the envelope identity is $\partial F_i/\partial\beta_{ij}=C_{ij}(q_i^*(\beta_i))$.
  At fixed $q_i$, the attention-coordinate objective is linear in $\beta_i$ plus its entropy
  regularizer and gives the Gibbs row. After eliminating $q_i$, this becomes an implicit Gibbs
  fixed point. One must not differentiate $\sum_j\beta_{ij}C_{ij}(q_i^*(\beta_i))$ as though it
  were $F_i$. [[gl-k-attention-2026-07-09-review-revision]]

- **The retained sweep is two-channel and same-scale.** Every archived configuration activates
  `prior_source=model_channel` and `s_e_step=true`. One target-blind $s$ refinement toward a
  learned global, token-uniform $r$ and gamma-weighted model consensus supplies
  $q_i^{(0)}=p_i=s_i^{(1)}$, followed by one target-blind $q$ refinement. Outer cross-entropy
  differentiates through both paths; the inner hyper-prior and gamma terms are not scored again.
  The learned route includes the model tables, $r$, token and learned positional frames, output
  projection and bias, and the active mixer. This does not establish a slower model timescale or
  the full multiscale PIFB hierarchy. [[gl-k-attention-2026-07-09-review-revision]]

- **Coarse-grained mean dispersion is covariance broadening, not necessarily anisotropy.** The
  law-of-total-covariance contribution $\operatorname{Var}_A(\mu)$ is positive semidefinite and may
  be proportional to the identity. The historical sum of its norm and the block-averaged input
  deviation is only a triangle-inequality upper-bound proxy for the actual block deviation.
  [[gl-k-attention-2026-07-09-review-revision]]

- **The isotropic geometric bias measures scale and shape distortion.** The bias vanishes exactly
  for orthogonal transport, but $\Omega=cR$ with $R\in\mathrm{O}(K)$ preserves isotropic shape
  while changing covariance scale and gives nonzero bias unless $c=1$. A nonzero bias therefore
  does not by itself diagnose directional anisotropy. [[gl-k-attention-2026-07-09-review-revision]]

- **The vacuum/training language is interpretive and stabilizer-dependent.** An observation-free
  divergence sector may have gauge redundancy when its priors are transport-compatible. A fixed
  non-invariant likelihood generally reduces that redundancy to its stabilizer; it does not by
  itself force specialization, unequal Euclidean norms, or a phase transition. Those dynamical
  claims require a declared order parameter and evidence not supplied by the retained sweep.
  [[gl-k-attention-2026-07-09-review-revision]]

### Empirical anchor (audited development evidence)

The retained numerical record is the fixed-$\mathrm{GL}^+(10)$ WikiText-103 width sweep over
$K=10,20,\ldots,120$ with three development records per width and 491.52 million tokens per run.
Mean test perplexity decreases from $219.0\pm1.3$ to $74.1\pm0.3$. The sweep spans ten source
commits, activates the head mixer only from $K=20$ onward, and is neither iso-compute nor a matched
architecture comparison. All 36 provenance records mark dirty worktrees, and no dirty diff survives.
The archived configurations and committed code at their recorded SHAs reconstruct the same-scale
$s\to q$ route, but the SHAs do not identify the exact executed bytes. The trend is therefore
development-provenance evidence, not a frozen benchmark or transferable scaling law. Historical
matched-baseline and frozen-BERT numerical claims are not retained; only the shared-frame algebraic
score comparison survives. [[gl-k-attention-2026-07-09-review-revision]]

## KL vs Bures: which distortion measures belief distance?

The manuscript's load-bearing distortion is the **KL divergence** between transported Gaussians,
which is asymmetric and is the information-geometric ($\alpha$-connection) object whose invariance
under $\mathrm{GL}(K)$ is proved above. A natural sibling is the **Bures / Bures–Wasserstein
distance** on covariances — the classical shadow of the quantum Bures metric, which is the *smallest*
monotone (quantum-Fisher) metric and is generated by Uhlmann fidelity
([[Quantum information geometry]]). The two are not interchangeable: KL is the relative-entropy
distortion that yields the closed-form Gibbs/softmax update and the $f$-divergence invariance
theorem, whereas the Bures geometry is the transport-optimal (Wasserstein) one. The
affine-invariant SPD metric the program actually uses for $\Sigma$-updates,
$\langle A,B\rangle_\Sigma=\operatorname{tr}(\Sigma^{-1}A\Sigma^{-1}B)$, is a *third* choice,
congruence-invariant by construction ([[Symmetric spaces and the SPD cone]],
[[pennec-2006-affine-invariant-tensor]]).

> [!note] Editorial: The manuscript's invariance results are stated and proved for KL and the full
> $f$-divergence class; it does not derive the attention rule from a Bures distortion. Reading the
> belief geometry "via KL/Bures distortion" should therefore be understood as: KL supplies the
> derived attention scores and their $\mathrm{GL}(K)$ invariance, while Bures and the affine-invariant
> metric are the neighboring SPD geometries that make the covariance side of the construction
> well-posed. A Bures-distortion variant of the score is a plausible but currently *unproven*
> alternative, and the quantum-metric non-uniqueness ([[petz-1996-monotone-metrics]],
> [[Quantum information geometry]]) is exactly why one cannot assume KL and Bures coincide off the
> commuting case.

## Relation to prior gauge / equivariant / SPD-attention work

The construction sits downstream of the geometric-deep-learning program, which organizes neural
architectures by the symmetry groups they respect ([[bronstein-2021-geometric-deep-learning]],
[[Gauge equivariance and geometric deep learning]], [[Group equivariance]]). Gauge-equivariant CNNs
make convolutions covariant under local frame changes on a manifold ([[cohen-2019-gauge-cnn]],
[[Gauge equivariant CNN]]); GL(K) attention is the attention-mechanism analogue, with the divergence
replacing the steerable kernel. The closest attention-specific prior art is Riemannian self-attention
on the SPD manifold ([[wang-2023-riemannian-self-attention-spd]]), which the manuscript review flags
as the nearest neighbor. The "attention is variational inference" reading also connects to the
kernel/linear-attention lineage ([[tsai-2019-kernel-attention]]) and to the free-energy-principle
literature it operationalizes ([[Free-energy principle active inference]], [[parr-2022-active-inference]],
[[Variational free energy and predictive coding]]). The most direct conceptual precursor — that
approximate Bayesian inference *is itself* a gauge theory — is
[[sengupta2017gauge|sengupta-friston-2017-bayesian-gauge-theory]] (with [[sengupta-2016-neuronal-gauge|sengupta-2016-neuronal-gauge-theory]]);
the manuscript's bibliographic review identified these as the prior art it must position against.

## Relevance to this research

This is the attention-mechanism cornerstone of the gauge-theoretic VFE program. It is the page that
ties together the program's three pillars: the **gauge** scaffold (frames $U_i\in\mathrm{GL}(K)$,
transport $\Omega_{ij}$, [[Holonomy]], [[Gauge transformation]]); the **information geometry**
(KL distortion, [[Fisher information metric]], [[Natural gradient]],
[[Information geometry and natural gradient]]); and the **belief geometry** (SPD covariances on
$\mathrm{GL}(K)/O(K)$, [[Symmetric spaces and the SPD cone]]). It anchors the
[[VFE Transformer Program]] and feeds the [[Gauge-Theoretic Multi-Agent VFE Model]], where the same
transported-belief machinery drives meta-agent coarse-graining and the
[[Renormalization-group flow of beliefs]] / [[Meta-agents and hierarchical emergence]] thread.
The construction derives its own KL-softmax attention rule rather than positing it. Its strict
shared-frame, isotropic limit yields an identity-bilinear score plus a key-norm bias; a general
transformer compatibility $W_QW_K^\top$ and value map remain structural additions. It is therefore
the formal pivot for a scoped comparison with transformer attention, not a theorem that arbitrary
transformer attention is an exact special case. [[gl-k-attention-2026-07-09-review-revision]]

## Related

[[GL(K) gauge group]] · [[Symmetric spaces and the SPD cone]] ·
[[SPD-manifold geometry and Riemannian optimization]] ·
[[Attention mechanisms — theory and positional structure]] · [[Multi-head attention]] ·
[[Variational free energy]] · [[Free-energy principle active inference]] · [[Precision weighting]] ·
[[Fisher information metric]] · [[Natural gradient]] · [[Holonomy]] · [[Parallel transport]] ·
[[Gauge transformation]] · [[Agents as fibre-bundle sections]] · [[Group equivariance]] ·
[[Gauge equivariant CNN]] · [[Gauge equivariance and geometric deep learning]] ·
[[Quantum information geometry]] · [[Statistical manifold]]

## Sources

[[gl-k-attention]] · [[vaswani-2017-attention]] · [[bronstein-2021-geometric-deep-learning]] ·
[[cohen-2019-gauge-cnn]] · [[wang-2023-riemannian-self-attention-spd]] ·
[[tsai-2019-kernel-attention]] · [[pennec-2006-affine-invariant-tensor]] ·
[[bhatia-2007-positive-definite-matrices]] · [[amari-2016-information-geometry-applications]] ·
[[cencov-1982-statistical-decision-rules]] · [[petz-1996-monotone-metrics]] ·
[[parr-2022-active-inference]] · [[sengupta2017gauge|sengupta-friston-2017-bayesian-gauge-theory]] ·
[[sengupta-2016-neuronal-gauge|sengupta-2016-neuronal-gauge-theory]] · [[participatory-it-from-bit]]
