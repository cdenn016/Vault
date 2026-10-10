---
type: concept
title: Fisher information metric
aliases:
  - Fisher information
  - Fisher information matrix
  - FIM
  - Fisher-Rao metric
  - "Fisher Metric"
  - "Fisher metric"
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-10-10
---

# Fisher information metric

> [!note] Current scope, September 11, 2026
> The new results distinguish information contraction, full statistical sufficiency and regular geometric descent. Fisher preservation alone need not imply sufficiency, and a weak Fisher metric does not automatically supply a strong Hilbert norm or invertible natural-gradient mobility. [[multiagentelbo-2026-09-11-conditional-geometry]] records the quotient and projectability hypotheses; [[multiagentelbo-2026-09-11-thermodynamic-fisher]] records the thermodynamic and joint-depth limit conditions. Geometry feedback also has explicit obstruction cases in [[multiagentelbo-2026-09-11-geometry-feedback]].


## Definition

The **Fisher information metric** is the Riemannian metric that the space of probability distributions carries when each distribution is regarded as a point on a smooth manifold. Consider a parametric family of densities $p(x \mid \theta)$ indexed by a parameter vector $\theta \in \mathbb{R}^n$. The **Fisher information matrix** at $\theta$ is

$$
F(\theta)_{ij} = \mathbb{E}_{p(x\mid\theta)}\left[ \partial_i \log p(x\mid\theta)\partial_j \log p(x\mid\theta) \right]
= -\mathbb{E}_{p(x\mid\theta)}\left[ \partial_i\partial_j \log p(x\mid\theta) \right],
$$

where $\partial_i = \partial/\partial\theta_i$ and the score is $\partial_i \log p$. The two expressions agree under mild regularity conditions. $F(\theta)$ is symmetric and positive semi-definite, and where it is positive definite it defines an inner product on each tangent space, $\langle u, v\rangle_\theta = u^\top F(\theta) v$. This collection of inner products is the Fisher information metric, also called the **Fisher-Rao metric**.

Its defining virtue is that it is *intrinsic*: the metric measures distances between distributions, not between coordinate values, so it is invariant under smooth reparameterizations of $\theta$. Infinitesimally it is the second-order term of the Kullback-Leibler divergence — $\mathrm{KL}\big(p_\theta \| p_{\theta+d\theta}\big) = \tfrac{1}{2}d\theta^\top F(\theta) d\theta + o(\|d\theta\|^2)$ — which is why the Fisher metric is the unique (up to scale) metric compatible with the statistical structure of the manifold. This grounding in information geometry is developed canonically by [[amari-2000-methods-information-geometry]].

## Why it matters here

The exact Fisher-geometric claim in the VFE transformer concerns its Gaussian
belief family. Gauge frames and decoder parameters are separate parameter
spaces and do not acquire a Fisher metric merely because they participate in
the same training schedule.

First, **belief optimization**. The online Gaussian belief update uses the belief-family Fisher metric. The frame M-step is separate and is not an identified Fisher natural gradient.

Second, **the divergence family**. A smooth divergence induces a local quadratic
form proportional to Fisher information, but the proportionality can depend on
the convention and order. In the standard order-Rényi convention, the local
Hessian carries an order-dependent positive factor. Nonlinear monotone
transforms preserve value ordering, not gradients, Hessians, affine connections,
or global geometry. Amari's [[Alpha-divergence]] and order-[[Renyi divergence]]
must therefore remain distinct.

> [!note] Editorial (2026-07-10): the frame conditioner is not the Fisher metric,
> and its positive Frobenius form is not full-$\mathrm{GL}(K)$
> adjoint-invariant. Belief Fisher geometry and frame conditioning must remain
> separate.

## Details

**Exponential families and dual flatness.** For an exponential family written in
natural parameters, the Fisher information equals the Hessian of the
log-partition function. The Gaussian belief family is exponential, and its full
joint mean-covariance Fisher–Rao geometry is treated by
[[skovgaard-1984-riemannian-geometry-normal-model]]. Amari's alpha-connections
and alpha-divergences describe a dualistic structure on statistical manifolds.
The configured order-Rényi discrepancy is related at the level of a power
integral but does not inherit those connections through a nonlinear monotone
change of divergence value.

**Fisher as curvature, and as Gauss–Newton.**
[[martens-2020-natural-gradient-insights]] relates Fisher and Generalized
Gauss–Newton matrices under specified output-distribution and loss conditions.
This motivates damping in those settings, but the identity is not automatic for
an arbitrary objective and has not been established for the frame M-step.

**Tractable approximations.** K-FAC and related Fisher approximations remain valid general methods. No audited derivation identifies the transformer's frame conditioner with a K-FAC block or a frame Fisher matrix.

**Relation to Riemannian optimization.** On a statistical manifold the Fisher
metric defines geodesics, while retractions and vector transports provide local
surrogates as formalized by [[absil-2008-optimization-matrix-manifolds]]. The
convergence result of [[bonnabel-2013-riemannian-sgd]] applies under its stated
assumptions and does not transfer automatically to every configured update. The
SPD-covariance side uses an affine-invariant metric on positive-definite
matrices.

**Quantum extension and a physical reading.** The classical Fisher metric has a quantum counterpart — the [[Quantum information geometry|quantum Fisher information]] — whose statistical-distance origin traces to [[wootters-1981-statistical-distance]], whose canonical form for pure-state estimation is the Bures/SLD metric of [[braunstein-caves-1994-quantum-fisher]], and which sits within the monotone-metric classification of [[petz-1996-monotone-metrics]] over the [[uhlmann-1976-transition-probability]] fidelity. A complementary strand, [[Physics from Fisher information]], runs the implication the other way: [[frieden-1998-physics-fisher]] and [[reginatto-1998-fisher-quantum]] derive dynamical laws (including the Schrodinger equation) from extremizing Fisher information, the same variational template that recurs when [[parr-2020-markov-blankets-thermodynamics]] casts free-energy minimization in thermodynamic terms.

> [!note] Editorial (2026-07-10): For zero-mean Gaussians, the covariance Fisher
> metric is one-half the conventional affine-invariant SPD metric,
> $g_\Sigma(U,V)=\tfrac12\operatorname{tr}(\Sigma^{-1}U\Sigma^{-1}V)$. The
> constant factor preserves geodesic paths but changes gradient scale. This
> covariance-only identity does not identify the full mean-covariance geometry
> or the gauge-frame optimizer with AIRM.

## Covariant pullback and information duration

For a section $s:\mathcal C\to\mathcal E_x$ of a statistical associated bundle, the ordinary
differential $Ts$ contains a base component forced by $\varpi_x\circ s=\operatorname{id}$. A chosen
connection removes that tautological component and defines the covariant vertical first jet

$$
D^\omega s=\operatorname{ver}^\omega\circ Ts.
$$

The rigorous agent-perceived tensor on the fixed base is therefore

$$
h_s^\omega(X,Y)=g^F(D^\omega sX,D^\omega sY).
$$

Under the stated equivariance hypotheses this tensor is global and passive-gauge invariant, but it is
connection-relative. It is generally a semimetric: when the fiber Fisher metric is positive definite,
$\operatorname{rad}h_s^\omega=\ker D^\omega s$. Constant rank gives a metric quotient of tangent
vector bundles; descent to a quotient manifold additionally requires integrability, a regular leaf
space, and tensor basicness.

A realized fixed-base law history $Q(\lambda)$ has Fisher length

$$
L_F[Q]=\int\sqrt{G^F_Q(\dot Q,\dot Q)}\,d\lambda,
$$

which is invariant under orientation-preserving reparameterization. Its endpoints determine only the
Fisher--Rao distance, the infimum of lengths over admissible connecting curves; they do not determine
the realized path, orientation, or duration. After VFE natural-gradient descent selects an oriented
unparameterized orbit, Fisher arclength supplies an agent-relative **information duration**. This is
not physical time, and natural-gradient orbits are not generally Fisher geodesics.

## Orbit Fisher form at one base point (review, September 23, tentative)

The covariant pullback above measures transport along base curves. At a single base point the attention network instead compares a belief with a belief moved by an independent link, $\mathrm{KL}(q_i\Vert\hat\rho(\Omega_{ij})q_j)$. Investigator X03 of the 2026-09-23 Theory review ([[multiagentelbo-2026-09-23-theory-streamlining-review]]) records the corresponding second-order law along the orbit $t\mapsto\hat\rho(e^{t\xi})q$:
$$
\mathcal D\bigl(q,\hat\rho(e^{t\xi})q\bigr)=\frac{t^2}{2}\mathfrak k_q(\xi,\xi)+O(t^3),\qquad \mathfrak k_q(\xi,\eta)=g^F(\zeta_\xi q,\zeta_\eta q),
$$
where $\zeta_\xi q$ is the fundamental vector field of the fiber action. When $g^F$ is positive definite the radical of $\mathfrak k_q$ is the isotropy algebra $\mathfrak g_q$, so directions that fix the belief cost nothing at second order. This orbit form governs link-transport, holonomy and plaquette energies near the identity at $c_*$; the Theory manuscript states it only at the end of a base-direction theorem. For Gaussians under the $\mathrm{GL}(K)$ congruence action ($K=2,3,4$, 200 draws) the normalized $O(t)$ remainder stayed below 1.24, and a skew isotropy generator $\xi=W\Sigma^{-1}$ annihilated a zero-mean Gaussian to $1.7\times10^{-15}$. X03 also derived the third-order coefficient of the transported-divergence expansion, $\tfrac12g(v,\nabla^*_vv)+\tfrac16T_{\mathcal D}(v,v,v)$, with $\nabla^*$ the dual connection (the exponential connection for KL).

> [!warning] Tentative: investigator recomputation, same model family, not adjudicated
> A corollary of an existing divergence-jet proposition, with numerical and SymPy checks by one investigator (Claude Opus 5.5).

### Incorporation in the restructured manuscript (September 24)

The orbit form is now `cor:pb-orbit-fisher-form` in Chapter 7 of the main manuscript at `623e4fe` ([[multiagentelbo-2026-09-24-theory-restructure]]), tagged ESTABLISHED, with its proof in Appendix B.2 (Deferred Proofs). Under the chapter's regularity hypothesis it defines $\mathfrak k_q(\xi,\eta)=g^F_q(\xi_{\mathcal B}(q),\eta_{\mathcal B}(q))$ and the isotropy algebra $\mathfrak g_q=\{\xi:\xi_{\mathcal B}(q)=0\}$. It states that $\mathfrak k_q$ is positive semidefinite with radical exactly $\mathfrak g_q$, the Lie algebra of the stabilizer of $q$, that $\mathrm{KL}(q\Vert\widehat\rho(\exp t\xi)q)=\tfrac{t^2}{2}\mathfrak k_q(\xi,\xi)+O(t^3)$, that the left side vanishes for every $t$ when $\xi\in\mathfrak g_q$, and that the same expansion holds for every regular invariant contrast with its metric jet in place of $g^F$. It follows `prop:pb-kl-divergence-jets`, which identifies the metric jet of KL with $g^F$ and its cubic jet with the Amari–Chentsov tensor. X03's third-order coefficient $\tfrac12g(v,\nabla^*_vv)+\tfrac16T_{\mathcal D}(v,v,v)$ is `prop:pb-divergence-cubic-coefficient` in Supplement B, Chapter B2, stated for one-sided contrast expansions along curves, with $\nabla^*$ the exponential connection for regular KL. The review's Gaussian draws are not reproduced in the manuscript.

The same chapter's `prop:ig-fisher-characterizations`, tagged STANDARD, states Cencov's uniqueness theorem (on the open simplex of positive laws on a finite set, the Fisher metric is, up to a positive factor, the unique Riemannian metric invariant under congruent Markov embeddings) and since October 10, 2026 cites it as Theorem 11.1 and Lemma 11.3 of [[cencov-1982-statistical-decision-rules]], with no page number. Campbell (1986, Proc. AMS 98:135) names the result as "Theorem 11.1 or Lemma 11.3" of the monograph; secondary sources disagree on the page (156, 159 and 161 all appear), and the AMS volume itself was not read, so the restructure's earlier "Lemma 11.3, p. 161" locator (itself corrected from p. 156) was replaced by the two statement numbers. The source note on the monograph records no page-level locator of its own.

> [!warning] Status
> Manuscript statements (ESTABLISHED with proofs, or STANDARD with a checked citation), written and checked by Claude Opus 5.5 agents with their own scripts; no cross-model check (the author's choice) and not adjudicated.

## In this work

The Fisher information metric surfaces wherever the configuration declares an information-geometric or natural-gradient operation:

- **Frame updates.** These use a separate optimizer/optional conditioner and carry no Fisher or K-FAC identification.
- **Belief (E-step) updates.** The per-token Gaussian beliefs are refined by natural-gradient / [[Natural gradient]] steps, whose metric is the Fisher information of the diagonal-Gaussian belief family.
- **Rényi objective.** The `divergence_family "renyi"` term is an order-Rényi
  pairwise discrepancy with KL at order one. Its local quadratic form is
  proportional to Fisher; it does not supply Amari alpha-connections or the
  Li–Turner variational bound.
- **SPD covariance geometry.** The `spd_affine` retraction operates under AIRM.
  On the zero-mean Gaussian covariance factor, Fisher is one-half conventional
  AIRM.

Blockwise frame conditioning should not be called Fisher preconditioning. The established Fisher metric is the one on the Gaussian belief family; optional gauge-frame conditioners are separate optimizer preconditioners. The audited frame table uses plain AdamW, with those conditioners and the heavy-ball field inactive.

## The Fisher metric as a renormalization scale

[[berman-2023-bayesian-renormalization]] promotes the metric from a preconditioner to a *scale*. Since $D_{KL}(\theta\Vert\theta') = \tfrac12\mathcal I_{ij}\delta\theta^i\delta\theta^j + O(\delta\theta^3)$, the metric converts parameter displacement into statistical distinguishability, and a distinguishability scale is a correlation length. Setting $\tau = 1/T$ with $T$ the observation count, the posterior flow $\pi_T = \mathcal N(\mu_T, T^{-1}\mathcal I^{-1})$ becomes a Fokker–Planck equation with the pushforward Fisher metric as diffusion kernel, structurally identical to the Polchinski exact-RG equation: **inference and renormalization are the same equation with the flow reversed.** Large Fisher eigenvalues are stiff directions (relevant); small ones are sloppy (irrelevant), and the operational scheme integrates out everything below a cutoff.

Two consequences for this program. First, the multi-agent model's matrix-weighted interaction Laplacian *is* this metric in the belief-mean sector — for $Y\sim\mathcal N(\mu,\Lambda^{-1})$ the Fisher information in $\mu$ is exactly $\Lambda$ — so [[Coarse Graining|coarse-graining costs]], natural-gradient preconditioning, and the RG cutoff are all statements about one spectrum. Second, an exactly unidentifiable direction has *zero* Fisher eigenvalue, hence is maximally sloppy: the $K^2$-dimensional coarse-frame orbit the exact-ELBO white paper proves unidentifiable is not merely undetermined but the first thing any Bayesian renormalization discards. That is a stronger statement than "declare a convention," and it explains why no geometric criterion could ever have selected a canonical frame.

> [!warning] Do not use the diagonal. [[berman-2023-bayesian-renormalization|BKS]] argue spectrally but implement with diagonal entries $\mathcal I_{ii}$, a discrepancy they never address; a set of individually sloppy but jointly stiff directions is then misclassified. For a coupled family the criterion must be a subspace determinant, not an entrywise threshold. Their construction also requires an invertible metric, so a degenerate sector must be quotiented before the machinery is imported.

## Bény–Osborne metric and monotonicity boundary

[[beny-osborne-2015-info-geometric-rg]] uses the **Kubo–Mori** relative-entropy Hessian on faithful quantum states; its commuting restriction is Fisher–Rao. Equations (3)–(6) give the observable metric and channel contraction,
$$
g_{N(\rho)}(Nx,Nx) \le g_\rho(x,x).
$$
Here $N$ is a quantum channel and $x$ a state tangent. Their scalar construction requires a tangent field transported by the flow, Eqs. (9)–(10); the generator supplies squared speed. The infinite-lattice density argument assumes translation-compatible local dynamics without active rescaling, while Section IV discusses the rescaling obstruction. [Primary text, Sections I–IV](https://arxiv.org/pdf/1206.7004v3).

> [!warning] Source-note correction (2026-09-05)
> The immutable [[beny-osborne-2015-info-geometric-rg]] note calls this Fisher–Bures. Equation (4) explicitly identifies Kubo–Mori. Use this correction when citing the paper; the original source note remains unchanged.

> [!note] Editorial: RG v2 application
> Use this metric for distinguishability on a declared tangent space. Treat the proposed coupling-response calculation as a finite diagnostic; identifying a common-space beta function, relevance exponents, or a continuum limit remains a separate construction. See [[Staged hierarchy formation and RG composability]].

## Sources

- [[amari-1998-natural-gradient]] — establishes the Fisher metric as the preconditioner of the natural (steepest-descent) gradient on a statistical manifold.
- [[amari-2000-methods-information-geometry]] — canonical treatment of the Fisher metric, dual connections, $\alpha$-connections, and dually flat exponential-family geometry.
- [[nielsen-2020-elementary-introduction-information-geometry]] — pedagogical grounding for KL geometry and Gaussian belief natural gradients.
- [[cover-thomas-2006-elements-information-theory]] — defines entropy, KL/relative entropy, and mutual information underpinning the free-energy KL and attention-entropy terms.
- [[khan-rue-2023-bayesian-learning-rule]] — natural-gradient descent on exponential-family natural parameters as one learning rule unifying Adam, Newton, VI, and online learning; the Fisher-preconditioned Gaussian belief update.
- [[martens-2020-natural-gradient-insights]] — Fisher/Generalized Gauss–Newton relation under specified output-distribution and loss conditions; natural gradient as a curvature method.
- [[martens-2015-kfac]] — block-Kronecker approximation of neural-network Fisher matrices; no frame-Fisher or frame-K-FAC identification is asserted here.
- [[ollivier-2015-riemannian-metrics-nn]] — family of Fisher-based, reparameterization-invariant training metrics for neural networks.
- [[zhang-2004-divergence-duality-convex]] — an $\alpha$-divergence family built from one convex potential, each inducing a common Fisher-type metric plus dual $\alpha$-connections, recovering Bregman/KL at $\alpha=\pm1$.
- [[skovgaard-1984-riemannian-geometry-normal-model]] — Fisher-Rao Riemannian geometry of the full Gaussian model (mean and covariance jointly), with geodesic ODEs and Rao distance for the $(\mu,\Sigma)$ manifold.
- [[vanerven-2014-renyi-kl]], [[li-turner-2016-renyi-vi]] — respectively order-Rényi divergence and the variational Rényi bound; neither is Amari's alpha-connection construction.
- [[pennec-2006-affine-invariant-tensor]] — affine-invariant SPD metric; the zero-mean Gaussian covariance Fisher metric is one-half this conventional AIRM.
- [[absil-2008-optimization-matrix-manifolds]], [[bonnabel-2013-riemannian-sgd]] — retractions and Riemannian SGD for moving under a manifold metric.
- [[wootters-1981-statistical-distance]] — statistical distance between quantum states, the origin of the quantum Fisher metric.
- [[braunstein-caves-1994-quantum-fisher]] — symmetric-logarithmic-derivative / Bures quantum Fisher information as the bound on quantum parameter estimation.
- [[petz-1996-monotone-metrics]] — classification of monotone (contractive) Riemannian metrics on quantum states, the quantum analogue of the Fisher uniqueness theorem.
- [[uhlmann-1976-transition-probability]] — transition probability / fidelity underlying the Bures geometry of quantum states.
- [[frieden-1998-physics-fisher]] — derivation of physical laws by extremizing Fisher information (extreme physical information).
- [[reginatto-1998-fisher-quantum]] — the Schrodinger equation obtained from a Fisher-information variational principle.
- [[parr-2020-markov-blankets-thermodynamics]] — free-energy minimization read thermodynamically, the same extremal-information template applied to self-organizing systems.

- [[berman-2023-bayesian-renormalization]] — the Fisher metric as an emergent RG scale; stiff/sloppy as relevant/irrelevant; the information-shell scheme.
- [[gabrielli-2025-network-renormalization]] — §6.4 names Fisher information and information geometry as the route to parameter relevance on networks, without deriving it.

## See also

- [[Natural gradient]]
- [[Renyi divergence]]
- [[Alpha-divergence]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Information geometry and natural gradient]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Quantum information geometry]]
- [[Physics from Fisher information]]
