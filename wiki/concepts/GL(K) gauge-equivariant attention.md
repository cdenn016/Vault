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
updated: 2026-06-21
---

# GL(K) gauge-equivariant attention

**GL(K) gauge-equivariant attention** is the central construction of the program's
[[gl-k-attention|GL(K) attention manuscript]] (*"Attention as Gauge-Theoretic Variational
Inference"*). It recasts transformer attention not as an architectural primitive but as
**variational inference over information sources**: each token is a Gaussian "agent"
$q_i=\mathcal N(\mu_i,\Sigma_i)$ living on a statistical fiber bundle, and the attention weight
between tokens is *derived* by minimizing a multi-agent [[Variational free energy]]. The
mechanism is built so that those weights are **invariant** to a per-token change of feature
basis drawn from the general linear group $\mathrm{GL}(K)$ — the structure (gauge) group of the
construction (see [[GL(K) gauge group]]). This page states the construction precisely and
records what is proven versus conjectured.

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
feature space. The frames are not arbitrary: in the manuscript they are generated from a Lie-algebra
field $\phi_i\in\mathfrak{gl}(K)$ via the matrix exponential, $U_i=\exp(\phi_i)$, which restricts to
the identity component $\mathrm{GL}^+(K)$ ($\det U_i>0$). The transport that carries token $j$'s
frame into token $i$'s frame is the composition

$$\Omega_{ij} \;=\; \exp(\phi_i)\,\exp(-\phi_j)\;=\;U_i U_j^{-1}\in\mathrm{GL}(K).$$

This $\Omega_{ij}$ is the bundle's discrete analogue of [[Parallel transport]]: it is the object
applied to a neighbor's belief before that belief is compared to one's own.

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

- **Standard attention is a degenerate limit.** Three ordered limits — flat connection, then
  vanishing gauge variation, then isotropic covariance — collapse gauge attention to the standard
  rule $\beta_{ij}\propto\operatorname{softmax}(Q_iK_j^\top/\sqrt{d_k})$. In that limit the invertible
  head-space factor of $W_QW_K^\top$ is identified as $\sigma^{-2}\Omega^{-\top}$, and the
  temperature $1/\sqrt{d_k}$ emerges from the dimensional concentration of the KL divergence rather
  than being a tuning convention ([[gl-k-attention]]).

- **Architectural choices fall out of the geometry.** Layer normalization is the key-norm
  cancellation condition ($\|\mu_j\|^2\approx C$) that makes inference frame-independent;
  [[Multi-head attention]] is a block-diagonal restriction of the gauge algebra
  $\bigoplus_a\mathfrak{gl}(d_{\mathrm{head}})$; RoPE positional encoding is reinterpreted as
  position-dependent gauge frames; and ALiBi/T5/causal biases are non-uniform attention priors
  $\pi_j$ entering the logits additively as $+\log\pi_j$ ([[gl-k-attention]],
  [[Attention mechanisms — theory and positional structure]]).

- **Covariance fixed point and SPD dynamics.** Minimizing the free energy in $\Sigma_i$ yields the
  matrix precision fixed point
  $\Sigma_i^{-1}=\tfrac12\big[\Sigma_{p,i}^{-1}+\sum_j\beta_{ij}(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}\big]$:
  each agent's precision is a $\beta$-weighted blend of its prior precision and its neighbors'
  *transported* precisions — manifest [[Precision weighting]]. Updates to $\Sigma$ are taken as
  natural-gradient steps with an SPD-manifold retraction ([[SPD-manifold geometry and Riemannian optimization]],
  [[Natural gradient]], [[Fisher information metric]]).

- **Flat-bundle (vanishing holonomy) regime.** The vertex-frame transport satisfies the cocycle
  identity $\Omega_{ij}\Omega_{jk}\Omega_{ki}=I$ as an *algebraic* identity, so both the gauge
  transformer and standard transformers operate with trivially vanishing reconstructed
  [[Holonomy]] (Regime I). An edge-relaxed extension
  $\Omega_{ij}=\exp(\phi_i)\exp(\delta_{ij}G)\exp(-\phi_j)$ promotes the bundle to non-trivial
  holonomy (Regime II), reserved for the companion participatory program ([[participatory-it-from-bit]]).

- **Forward KL is (conditionally) the right divergence.** Within the convex $f$-divergence class,
  the forward KL is the unique choice giving a closed-form Gibbs belief update with exponential-family
  closure *and* a consistent dual (envelope-theorem) reading of the attention weights; reverse KL,
  $\chi^2$, and Jensen–Shannon each break this log-linearity ([[gl-k-attention]] App. H). This is the
  attention-side echo of Chentsov/Petz uniqueness for invariant metrics
  ([[cencov-1982-statistical-decision-rules]], [[petz-1996-monotone-metrics]]).

- **Learning as symmetry breaking.** The untrained network is a gauge-symmetric "vacuum"; in the
  observation-free regime beliefs converge to a common gauge orbit, and observations break the
  symmetry. Training is read as explicit symmetry breaking ([[gl-k-attention]]).

### Empirical anchor (as reported)

On WikiText-103 a $\mathrm{GL}(15)$ gauge transformer ($K=90$, 81.4M params) reaches test
perplexity 71.6, beating a standard transformer at matched embedding dimension (PPL 118.6) by
$1.66\times$, though a parameter-matched standard transformer ($d_{\text{model}}=1{,}280$) still
wins at PPL 48.5. A frozen-BERT validation across 105 passages finds the flat-bundle KL attention
$\beta^{\text{flat}}_{ij}=\operatorname{softmax}(-\|Q_i-K_j\|^2/\tau)$ agreeing with dot-product
attention at grand mean correlation $\bar r=0.804$ — treated as a consistency check, since high $r$
partly follows from an algebraic identity ([[gl-k-attention]]).

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
Because it derives attention from first principles rather than positing it, it is the formal pivot on
which the program's claim — that transformer attention is a special case of gauge-theoretic
variational inference — rests.

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
