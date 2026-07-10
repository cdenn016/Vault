---
type: concept
title: "Gaussian Beliefs"
aliases:
  - "Gaussian belief"
  - "Gaussian belief state"
  - "Gaussian belief tuple"
  - "Belief tuple"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-07-09
---

# Gaussian Beliefs

## Definition

A **Gaussian belief** is the variational posterior an agent or token carries over a
latent state $c \in \mathbb{R}^K$,
$$
q(c) = \mathcal{N}(c \mid \mu, \Sigma), \qquad
\mu \in \mathbb{R}^K, \quad \Sigma \in \mathrm{SPD}(K),
$$
encoded by the **belief tuple** $(\mu, \Sigma)$: a mean vector and a symmetric
positive-definite (SPD) covariance. It is the workhorse representation of the
gauge-theoretic VFE program. In the [[GL(K) gauge-equivariant attention]] model every
token is exactly such a Gaussian "agent" $q_i = \mathcal{N}(\mu_i, \Sigma_i)$ living on a
statistical fiber bundle ([[gl-k-attention|GL(K) attention manuscript]],
[[Agents as fibre-bundle sections]]); in the multi-agent (MAgent) model each agent's belief
is the same tuple, and its inverse covariance $\Lambda = \Sigma^{-1}$ — the **precision** —
is read as inertial [[Mass as Fisher information|mass]] ([[belief-inertia]]).

The Gaussian is singled out for three structural reasons that this page develops:
it is an [[Exponential family]] member (so variational updates close in a finite parameter
set and stay conjugate); its covariance lives on the SPD cone, a Riemannian
[[Symmetric spaces and the SPD cone|symmetric space]] $GL(K)/O(K)$ on which the gauge group
acts by **congruence**; and the Kullback–Leibler divergence between two Gaussians has a
**closed form**, which makes the entropy-regularized KL-consensus coupling of attention and
the MAgent model tractable in closed form rather than by sampling.

## The belief as an exponential-family member

The Gaussian is the maximum-entropy distribution for fixed first and second moments, and it
is a member of the [[Exponential family]]: its density can be written
$q(c) = h(c)\,\exp\!\big(\langle \eta, T(c)\rangle - A(\eta)\big)$ with sufficient statistic
$T(c) = (c,\; c c^\top)$ ([[wainwright-2008-graphical-models-variational]],
[[amari-2016-information-geometry-applications]]). This gives two coordinate systems for the
*same* belief, related by a Legendre (convex) duality:

- **Natural (canonical) parameters** $\eta = \big(\Sigma^{-1}\mu,\; -\tfrac12 \Sigma^{-1}\big)
  = (h, -\tfrac12\Lambda)$ — the precision-weighted mean (the "information vector" $h$) and
  $-\tfrac12$ the precision matrix $\Lambda = \Sigma^{-1}$. Conjugate Bayesian updates are
  **linear** in these coordinates: combining a Gaussian prior with a Gaussian likelihood adds
  natural parameters, $\eta_{\text{post}} = \eta_{\text{prior}} + \eta_{\text{lik}}$
  ([[Conjugate-Exponential Family]], [[wainwright-2008-graphical-models-variational]]). This
  is exactly why the covariance fixed point of gauge attention is a sum of precisions —
  $\Sigma_i^{-1} = \tfrac12\big[\Sigma_{p,i}^{-1} + \sum_j \beta_{ij}
  (\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}\big]$ — and why the MAgent
  [[Mass as Fisher information|mass tensor]] is a sum of precision contributions
  ([[gl-k-attention|GL(K) attention manuscript]], [[belief-inertia]]).
- **Moment (expectation / dual) parameters** $\mathbb{E}_q[T] = (\mu,\; \Sigma + \mu\mu^\top)$
  — the mean and the (uncentered) second moment, equivalently $(\mu, \Sigma)$. The
  **log-partition function** $A(\eta)$ is convex; its gradient maps natural to moment
  parameters, $\nabla A(\eta) = \mathbb{E}_q[T]$, and its Hessian is the
  [[Fisher information metric]] $F(\eta) = \nabla^2 A(\eta)$
  ([[amari-2016-information-geometry-applications]]). Because the two coordinate systems are
  Legendre-dual, the Gaussian manifold is **dually flat** — carrying mutually dual $e$- and
  $m$-connections that are flat in the natural and moment coordinates respectively
  ([[Fisher information metric]], [[Statistical manifold]]).

> [!note] Editorial: The program exploits this duality directly. Belief E-steps that look
> like ordinary gradient descent on $(\mu,\Sigma)$ become [[Natural gradient]] steps once one
> reads them in natural-parameter coordinates, where the Fisher metric is the
> log-partition Hessian; this is the abstract content of the Bayesian-learning-rule
> reading cited on [[Fisher information metric]].

## SPD covariance geometry

The covariance factor $\Sigma$ is not a free $K\times K$ matrix: it must stay symmetric
positive-definite, so it lives on the **SPD cone** $\mathrm{SPD}(K)$, a curved manifold rather
than a flat Euclidean parameter block ([[Symmetric spaces and the SPD cone]],
[[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]). The
natural Riemannian structure there is the **affine-invariant metric**
$\langle A, B\rangle_\Sigma = \operatorname{tr}(\Sigma^{-1} A\, \Sigma^{-1} B)$, under which the
cone has nonpositive curvature and the geodesic between two covariances is the matrix
"sandwich" $A \#_t B = A^{1/2}(A^{-1/2} B A^{-1/2})^t A^{1/2}$
([[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]). For the
zero-mean Gaussian family this affine-invariant metric **is** the Fisher–Rao metric on
covariances ([[Fisher information metric]]); the full $(\mu,\Sigma)$ Fisher–Rao geometry,
with the mean and covariance coupled, is worked out for exactly this normal model by
[[skovgaard-1984-riemannian-geometry-normal-model]].

Two consequences matter operationally. First, optimizing $\Sigma$ is a problem in
[[SPD-manifold geometry and Riemannian optimization|Riemannian optimization]]: belief and
M-step updates use an SPD retraction (the `spd_affine` step) that moves *along* the
symmetric-space geodesics instead of taking a Euclidean step that could leave the cone
([[gl-k-attention|GL(K) attention manuscript]], [[pennec-2006-affine-invariant-tensor]]).
Second, many covariance objectives ($\log\det\Sigma$, $\operatorname{tr}(A\Sigma^{-1})$,
geodesic-distance terms) are **geodesically convex** under this metric, so Riemannian descent
on $\Sigma$ reaches global optima ([[Symmetric spaces and the SPD cone]]). The numerically
stable matrix $\exp$, $\log$, and $\sqrt{\cdot}$ primitives the geometry needs are standard
([[Symmetric spaces and the SPD cone]], [[petersen2012matrix|Matrix Cookbook]] for the
Gaussian derivative identities).

## Congruence (gauge) action on the covariance

The defining structural move of the program is that the **gauge group acts on a Gaussian
belief**, and on the covariance specifically by **congruence** (the two-sided "sandwich"). If
a frame change / transport is a matrix $\Omega \in GL(K)$, pushing the belief forward gives
$$
\mu \longmapsto \Omega\,\mu, \qquad
\Sigma \longmapsto \Omega\,\Sigma\,\Omega^{\top},
$$
i.e. $\Omega_* \mathcal{N}(\mu,\Sigma) = \mathcal{N}(\Omega\mu,\, \Omega\Sigma\Omega^\top)$. This
is precisely the action that realizes the SPD cone as the orbit
$\mathrm{SPD}(K) \cong GL(K)/O(K)$ of the identity under congruence, with $O(K)$ the stabilizer
of $I$ ([[Symmetric spaces and the SPD cone]], [[pennec-2006-affine-invariant-tensor]]). Two
elementary matrix facts make the action well posed and are the ones the program leans on
([[horn-johnson-2013-matrix-analysis]], cf. [[Symmetric spaces and the SPD cone]]):

- **Congruence preserves positive-definiteness** (Sylvester's law of inertia): a transported
  covariance $\Omega\Sigma\Omega^\top$ is still SPD, so it is still a valid covariance.
- **Congruence scales the determinant by $(\det\Omega)^2$**:
  $\det(\Omega\Sigma\Omega^\top) = (\det\Omega)^2 \det\Sigma$. This is the identity that governs
  how the Gaussian normalization $(2\pi)^{-K/2}(\det\Sigma)^{-1/2}$ transforms under a gauge
  change, and it is the factor that **cancels** in the KL divergence (next section).

In gauge attention the transport between token $i$ and token $j$ is
$\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j) \in GL^+(K)$, built from per-token frame fields
$\phi$ in the Lie algebra of $GL^+(K)$; transporting neighbor $j$'s belief into $i$'s frame
sends $\Sigma_j \mapsto \Omega_{ij}\Sigma_j\Omega_{ij}^\top$
([[gl-k-attention|GL(K) attention manuscript]], [[GL(K) gauge group]],
[[Gauge transformation]], [[Parallel transport]]). The same congruence appears in the MAgent
mass tensor, where the incoming-social precision is the transported neighbor precision
$(\Omega_{ik}\Sigma_k\Omega_{ik}^\top)^{-1}$ ([[Mass as Fisher information]], [[belief-inertia]]).

> [!note] Editorial: The earlier stub for this page sourced the congruence-transport claims to
> variational-autoencoder / information-bottleneck papers. That is a mis-sourcing: the
> congruence action $\Sigma \mapsto \Omega\Sigma\Omega^\top$, its determinant law, and the
> $GL(K)/O(K)$ orbit structure are properties of SPD-matrix geometry and the program's own
> gauge construction, and are sourced here to
> [[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]],
> [[horn-johnson-2013-matrix-analysis]] (via [[Symmetric spaces and the SPD cone]]) and the
> [[gl-k-attention|GL(K) attention manuscript]], not to the VAE/IB literature.

## Closed-form KL between Gaussians

Because Gaussians are an exponential family, the Kullback–Leibler divergence
([[kullback-1951-kl-divergence|Kullback–Leibler 1951]]) between two of them is available in
**closed form**. For $q_0 = \mathcal{N}(\mu_0,\Sigma_0)$ and $q_1 = \mathcal{N}(\mu_1,\Sigma_1)$
on $\mathbb{R}^K$,
$$
D_{\mathrm{KL}}(q_0 \,\|\, q_1) = \tfrac12\Big[
\operatorname{tr}(\Sigma_1^{-1}\Sigma_0)
+ (\mu_1-\mu_0)^\top \Sigma_1^{-1}(\mu_1-\mu_0)
- K + \ln\tfrac{\det\Sigma_1}{\det\Sigma_0}
\Big]
$$
([[petersen2012matrix|Matrix Cookbook]],
[[wainwright-2008-graphical-models-variational]]). The quadratic Mahalanobis term is a
precision-weighted prediction error — the same object [[Precision weighting]] names — and the
log-determinant term scores the relative volume/uncertainty of the two beliefs. This closed
form is what makes the program's couplings analytic: the gauge-attention weight is
$\beta_{ij} = \operatorname{softmax}_j(-D_{\mathrm{KL}}[q_i \| \Omega_{ij} q_j]/\tau)$, derived
(not posited) as the source-selection posterior of a mixture generative model
([[gl-k-attention|GL(K) attention manuscript]], [[GL(K) gauge-equivariant attention]],
[[Belief coupling]]).

The KL divergence is **gauge-invariant** under the congruence action, and this is a theorem of
the program, not an assumption: for any $\Omega \in GL(K)$,
$$
D_{\mathrm{KL}}(\Omega_* q_0 \,\|\, \Omega_* q_1) = D_{\mathrm{KL}}(q_0 \,\|\, q_1),
$$
because the $(\det\Omega)^2$ factors in the two log-determinants cancel exactly and the
sandwiched precision/quadratic terms are similarity-invariant under the trace. The result holds
for *all* $f$-divergences and needs only $\det\Omega \neq 0$, so the full $GL(K)$ acts as a
gauge symmetry of the divergence ([[gl-k-attention|GL(K) attention manuscript]], Theorem
"$GL(K)$ Gauge Invariance"). Infinitesimally the KL reduces to the
[[Fisher information metric|Fisher–Rao]] quadratic form,
$D_{\mathrm{KL}}(q_\theta \| q_{\theta+d\theta}) = \tfrac12\, d\theta^\top F(\theta)\, d\theta
+ o(\|d\theta\|^2)$, tying the global KL coupling back to the local Gaussian geometry
([[Fisher information metric]], [[Bregman divergence]] — KL is the Bregman divergence generated
by the Gaussian log-partition function).

## Relevance to this research

Gaussian beliefs are a **core program concept**, the shared substrate of both flagship projects:

- **VFE transformer / gauge attention.** Each token is a Gaussian agent; attention is KL
  consensus between transported Gaussians; and the covariance fixed point is a precision sum.
  In the shared-frame Regime-I specialization, the isotropic limit is identity-bilinear plus a key-norm bias; a general
  $W_QW_K^\top$ is structural, not transport. Full-Gaussian congruence remains exact, while the
  live diagonal family is exact only under monomial transport and otherwise uses projection.
  [[gl-k-attention-2026-07-09-review-revision]]
- **Multi-agent / MAgent model.** Each agent carries $(\mu,\Sigma)$; precision $\Sigma^{-1}$
  is inertial [[Mass as Fisher information|mass]], which gives the model [[Belief inertia]] and
  a [[Hamiltonian belief dynamics|Hamiltonian]] second-order belief dynamics
  ([[belief-inertia]]).

The three facets above are not independent conveniences but three faces of one fact: the
Gaussian family is the dually flat exponential family whose covariance manifold is the SPD
symmetric space the gauge group acts on. Exponential-family closure gives tractable conjugate
(precision-additive) updates; the SPD/affine-invariant geometry gives the right Riemannian
optimization for $\Sigma$; and the closed-form, gauge-invariant KL gives an analytic,
frame-independent coupling between beliefs. Where the model needs to leave the diagonal-Gaussian
regime it does so by enriching $\Sigma$ (full SPD covariance, congruence transport), never by
abandoning the tuple — which is what keeps the whole pipeline closed-form and differentiable
([[gl-k-attention|GL(K) attention manuscript]]).

## Related

- [[Exponential family]] · [[Conjugate-Exponential Family]] · [[Statistical manifold]]
- [[Fisher information metric]] · [[Natural gradient]] · [[Information geometry and natural gradient]]
- [[Symmetric spaces and the SPD cone]] · [[SPD-manifold geometry and Riemannian optimization]]
- [[GL(K) gauge group]] · [[Gauge transformation]] · [[Parallel transport]]
- [[GL(K) gauge-equivariant attention]] · [[Belief coupling]] · [[Precision weighting]]
- [[Mass as Fisher information]] · [[Belief inertia]] · [[Hamiltonian belief dynamics]]
- [[Variational free energy]] · [[Bregman divergence]] · [[Reparameterization trick]]

## Sources

- [[gl-k-attention|GL(K) attention manuscript]] — Gaussian-agent tokens, the congruence
  transport $\Omega_{ij}\Sigma_j\Omega_{ij}^\top$, the closed-form KL attention weight, the
  $GL(K)$ KL-invariance theorem, and the covariance precision fixed point. **Primary program
  source for the congruence-transport claims** (replaces the stub's VAE/IB mis-citation).
- [[pennec-2006-affine-invariant-tensor]] — the affine-invariant Riemannian metric on the SPD
  cone and the congruence action; the covariance geometry underneath $\Sigma$.
- [[bhatia-2007-positive-definite-matrices]] — SPD geometry: geodesics, geodesic distance, and
  the matrix sandwich/congruence structure of the cone.
- [[horn-johnson-2013-matrix-analysis]] — Sylvester's law of inertia (congruence preserves
  positive-definiteness) and the $(\det\Omega)^2$ determinant-under-congruence identity.
- [[skovgaard-1984-riemannian-geometry-normal-model]] — Fisher–Rao geometry of the full
  $(\mu,\Sigma)$ normal model (mean and covariance jointly).
- [[wainwright-2008-graphical-models-variational]] — exponential-family form of the Gaussian,
  natural/moment (mean) parameters, log-partition duality, and conjugate updates.
- [[amari-2016-information-geometry-applications]] — dually flat exponential-family geometry,
  Legendre duality of natural and moment parameters, log-partition Hessian as Fisher metric.
- [[kullback-1951-kl-divergence]] — the Kullback–Leibler divergence the closed form computes.
- [[petersen2012matrix]] — matrix calculus identities (Gaussian KL closed form, log-det and
  trace derivatives) used for the covariance updates.

## See also

- [[Gaussian Belief Propagation]] — message passing with Gaussian beliefs in
  information (natural-parameter) form.
- [[Gaussian State Space Model]] — Gaussian beliefs propagated through linear-Gaussian dynamics.
- [[Conjugate-Exponential Family]] — why the conjugate updates close in natural parameters.
