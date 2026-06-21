---
type: concept
title: "Mean-Field Approximation"
aliases:
  - "Mean Field Approximation"
  - "Mean-field variational family"
  - "Factorized variational approximation"
  - "Mean Field Theory"
tags:
  - cluster/vfe
  - project/transformer
  - project/social-physics
status: draft
created: 2026-06-21
updated: 2026-06-21
---

# Mean-Field Approximation

## Definition

The **mean-field approximation** is the workhorse simplification of variational inference: it
restricts the approximating family $\mathcal{Q}$ to **fully factorized** distributions over the
latent variables,
$$
q(z) \;=\; \prod_{i=1}^{m} q_i(z_i),
$$
so that every latent variable (or block of variables) is treated as *mutually independent* under
$q$. Variational inference recasts posterior computation as optimization — one posits a family
$\mathcal{Q}$ and finds the member $q^\*(z) = \arg\min_{q\in\mathcal{Q}} \mathrm{KL}\!\bigl(q(z)\,\|\,p(z\mid x)\bigr)$
closest to the intractable exact posterior $p(z\mid x)$ in reverse Kullback–Leibler (KL)
divergence, equivalently maximizing the [[Evidence lower bound (ELBO)|evidence lower bound]]
$\mathrm{ELBO}(q)=\mathbb{E}_q[\log p(z,x)]-\mathbb{E}_q[\log q(z)]$
([[blei-2017-variational-inference]]). The mean-field choice is what makes this optimization
tractable: by severing the dependence structure of $q$, the per-factor problem decouples into
something solvable in closed form for a large class of models. This is the same factorization
that statistical physics calls **mean-field theory** — replacing each particle's interaction with
its neighbours by an interaction with the *average* (mean) field — and the name is inherited
directly from that lineage ([[wainwright-2008-graphical-models-variational]]).

It is essential to keep the factorization assumption separate from any assumption on the
*shape* of the factors. The mean-field family does not require the $q_i$ to be Gaussian or to
belong to any particular parametric family; the optimal factors fall out of the variational
problem itself. What it does require — and its defining commitment — is the **absence of
posterior dependence** across the factors.

## Coordinate-ascent (CAVI) updates

Because $q$ factorizes, the ELBO can be optimized one factor at a time while holding the others
fixed — a block-coordinate-ascent scheme known as **coordinate ascent variational inference
(CAVI)** ([[blei-2017-variational-inference]]). Isolating the dependence of the ELBO on a single
factor $q_j$ and setting the functional derivative to zero gives the celebrated coordinate-optimal
update
$$
q_j^\*(z_j) \;\propto\; \exp\!\Bigl(\, \mathbb{E}_{-j}\bigl[\log p(z_j, z_{-j}, x)\bigr] \Bigr),
$$
where $\mathbb{E}_{-j}[\cdot]$ denotes expectation over all *other* factors $\prod_{i\ne j} q_i$.
Equivalently, the optimal $q_j$ is proportional to the exponentiated expected log
**complete conditional** $\log p(z_j \mid z_{-j}, x)$. CAVI simply cycles these updates over
$j=1,\dots,m$ until the ELBO converges (Algorithm 1 of [[blei-2017-variational-inference]]).

For **conditionally conjugate** / conjugate-exponential models — where each complete conditional
lies in an [[Exponential family|exponential family]] and the priors are conjugate — the expectation
inside the exponential reduces to a closed-form update of the natural parameters from *expected
sufficient statistics*, so no integration or sampling is needed. This conjugate-exponential
structure is exactly what makes the mean-field updates analytic, and it is the backbone of
**[[Variational EM|variational Bayesian EM (VB-EM)]]**: there the factorization
$q(x,\theta)=q(x)\,q(\theta)$ separates hidden states from parameters, the VBE step updates
$q(x)$ from the expected sufficient statistics of $q(\theta)$, and the VBM step does the reverse,
both staying in the same conjugate family with closed-form updates that mirror ordinary EM
([[beal-2003-variational-bayesian]]).

Two convergence caveats matter in practice. First, the ELBO is in general **non-convex**, so CAVI
converges only to a *local* optimum and is sensitive to initialization — multiple random restarts
are standard ([[blei-2017-variational-inference]]). Second, the bound is only **tight when the true
posterior already factorizes** in the assumed way; the mean-field lower bound on the log-evidence
satisfies $\mathcal{F}\le\log p(x)$ with equality iff the variational family contains the exact
posterior ([[beal-2003-variational-bayesian]], [[wainwright-2008-graphical-models-variational]]).
Beal further shows that in the large-data limit the VB bound recovers the BIC, making mean-field VB
a consistent model-selection criterion ([[beal-2003-variational-bayesian]]).

## Underestimation of posterior variance

The signature pathology of mean-field VI is that it **systematically underestimates posterior
variance**, and it does so for two compounding reasons ([[blei-2017-variational-inference]]).

1. **The factorization discards correlations.** By construction the variational covariance is
   block-diagonal: $q(z)=\prod_i q_i(z_i)$ can represent no posterior covariance *between* factors.
   Whatever dependence the true posterior carries — strong off-diagonal couplings, ridges,
   multimodal correlations — is projected away.

2. **Reverse KL is mode-seeking / zero-forcing.** Minimizing $\mathrm{KL}(q\,\|\,p)$ (rather than
   the "forward" $\mathrm{KL}(p\,\|\,q)$) penalizes placing $q$-mass where $p$ is small, but *not*
   the reverse. The optimizer is therefore driven to a *single* mode and to a $q$ that is
   **narrower** than $p$ — it would rather be too confident than spread mass into low-density
   regions. This direction-of-KL asymmetry is the same lever the [[Alpha-divergence|alpha- and
   Rényi divergence]] families interpolate: $\alpha\to 1$ recovers the mode-seeking reverse-KL
   ELBO, while larger $\alpha$ relaxes the zero-forcing toward more mass-covering (variance-
   preserving) behaviour.

The net effect is a posterior approximation whose *point* estimates can be excellent while its
*uncertainty* is too tight — a serious problem whenever calibrated uncertainty matters. Whether
mean-field VI's uncertainties can be corrected in general, and what its statistical (consistency,
calibration) properties are, were flagged as largely open questions
([[blei-2017-variational-inference]]).

## Statistical-physics origin and the variational principle

The term "mean field" predates machine learning: it is borrowed from the statistical mechanics of
interacting systems, where a many-body problem is made tractable by replacing the fluctuating field
each particle feels with its ensemble average. [[wainwright-2008-graphical-models-variational]]
make this lineage exact by deriving *all* the major inference algorithms — sum-product / belief
propagation, mean field, expectation propagation, max-product, and LP/conic relaxations — from a
**single variational principle** rooted in exponential-family conjugate duality. The cumulant
(log-partition) function $A(\theta)=\log\int\exp\langle\theta,\phi(x)\rangle\,d\nu(x)$ is convex,
and its convex conjugate is the negative entropy $A^\*(\mu)$ over the marginal polytope
$\mathcal{M}$ of realizable mean parameters, giving the exact representation
$$
A(\theta) \;=\; \sup_{\mu\in\mathcal{M}} \bigl\{\langle\theta,\mu\rangle - A^\*(\mu)\bigr\}.
$$
Approximate algorithms arise from relaxing this principle in two ways: outer-bounding the marginal
polytope $\mathcal{M}$, or substituting a tractable surrogate entropy for $A^\*$. **Naive mean
field** is the relaxation that replaces $A^\*$ by the entropy of a fully factored
$q=\prod_s q_s$ and optimizes the resulting *lower* bound on the log-likelihood; the closely
related **Bethe** approximation (single-node entropies minus pairwise mutual-information terms)
yields belief propagation as its stationary-point equations
([[wainwright-2008-graphical-models-variational]]). A practical consequence of this physics
heritage: unlike the convex tree-reweighted bounds, the mean-field objective is **non-convex**, so
mean-field fixed points may be multiple and only locally optimal — the variational-optimization
mirror of the multiple-minima landscape of a frustrated mean-field energy.

## Link to opinion-dynamics and collective behaviour

The same factorization travels into the modelling of *populations of interacting agents*. In
sociophysics and [[Opinion dynamics|opinion dynamics]], a **mean-field** treatment replaces each
agent's coupling to its specific neighbours by a coupling to the population's mean (or to the
distribution of opinions), exactly as in physics — this is the device that makes voter-type,
bounded-confidence, and kinetic opinion models analytically tractable in the large-population limit
(see [[Sociophysics]] and the survey in
[[Statistical physics of social systems and collective behavior]]). There are thus **two distinct
mean-field ideas** that share a name and a heritage but operate at different levels:

- a *variational* mean field, which factorizes the **approximate posterior** $q(z)=\prod_i q_i(z_i)$
  of one inference problem (the subject of this page); and
- a *thermodynamic / kinetic* mean field, which factorizes the **interaction** among many agents by
  routing it through an aggregate, and is the foundation of the
  [[Mean-field games and continuum limits|continuum limit]] of agent populations.

> [!note] Editorial: These two senses coincide structurally when the agents in question are
> themselves Bayesian. If a population of [[Multi-agent variational free energy|VFE agents]] each
> carries an independent belief and is coupled only through population-level aggregates, then the
> product belief $\prod_i q_i$ *is* a mean-field variational posterior over the joint latent state,
> and the agent-level mean-field interaction *is* the variational mean-field factorization viewed
> at the population scale. The wiki keeps the two pages distinct because the supporting literature
> is distinct ([[blei-2017-variational-inference]] / [[beal-2003-variational-bayesian]] for the
> inferential sense; the kinetic / mean-field-games corpus for the population sense), but the
> identification is the bridge the SocialPhysics program leans on.

## Relevance to this research

The mean-field approximation is the structural prior behind the **per-token, per-layer belief
factorization** of the VFE transformer. Each token carries an *independent* Gaussian belief tuple
$(\mu,\Sigma,\phi)$, which is precisely a mean-field factorization $q(z)=\prod_i q_i(z_i)$ over the
token latents; the VFE free-energy functional $F$ minimized at each layer is an
[[Evidence lower bound (ELBO)|ELBO]] (up to sign and coupling terms), and the layerwise
belief-update / parameter-update loop is the [[Variational EM|VB-EM]] E-step / M-step alternation
specialized to that Gaussian family ([[blei-2017-variational-inference]],
[[beal-2003-variational-bayesian]]). The choice of Gaussian belief tuples is not incidental:
Gaussians lie in the conjugate-exponential family, so the mean-field / CAVI updates are
closed-form, exactly as Beal's framework requires ([[beal-2003-variational-bayesian]]).

The program's distinctive moves are best read as *responses to the two known limitations of
mean field*:

- **Recovering lost correlations via gauge transport.** The mean-field factorization's inability
  to represent posterior dependence across tokens
  ([[blei-2017-variational-inference]]) is exactly what the gauge-equivariant transport terms
  $\Omega_{ij}$ are designed to repair: the inter-token coupling
  $\mathrm{KL}\!\bigl(q_i \,\|\, \Omega_{ij}\,q_j\bigr)$ reintroduces structured dependence that a
  naive product posterior cannot carry. The softmax attention weights $\beta_{ij}$ themselves arise
  as the stationary point of an entropy-regularized coupling objective — the same variational /
  conjugate-duality machinery [[wainwright-2008-graphical-models-variational]] use to derive
  belief-propagation fixed points (see [[GL(K) gauge-equivariant attention]]).

- **Tuning the variance pathology via the divergence.** The reverse-KL variance underestimation
  ([[blei-2017-variational-inference]]) is a live design concern for the decode path (the
  KL-to-prior decode versus the PriorBank pathway). The program retains the freedom to replace the
  plain KL in the belief step with an [[Alpha-divergence|alpha- / Rényi divergence]], trading the
  mode-seeking zero-forcing of reverse KL for more mass-covering behaviour when calibrated
  uncertainty is needed.

Finally, the same factorization underwrites the **multi-agent** reading: a population of
independent VFE agents coupled through aggregates is a mean-field posterior at the population scale
(see the Editorial above and [[Multi-agent variational free energy]]), which is the formal hinge
connecting the transformer's token beliefs to the SocialPhysics program's
[[Opinion dynamics|opinion-dynamics]] and [[Mean-field games and continuum limits|continuum]]
limits.

## Related

[[Variational free energy]] · [[Evidence lower bound (ELBO)]] · [[Variational EM]] ·
[[Exponential family]] · [[Alpha-divergence]] · [[Natural gradient]] ·
[[Multi-agent variational free energy]] · [[GL(K) gauge-equivariant attention]] ·
[[Mean-field games and continuum limits]] · [[Opinion dynamics]] · [[Sociophysics]] ·
[[Statistical physics of social systems and collective behavior]]

## Sources

- [[blei-2017-variational-inference]] — VI as optimization; the mean-field family, CAVI updates,
  the closed-form $q_j^\*\propto\exp\mathbb{E}_{-j}[\log p(z_j,z_{-j},x)]$, non-convexity / local
  optima, and the systematic underestimation of posterior variance under reverse KL.
- [[wainwright-2008-graphical-models-variational]] — the exponential-family conjugate-duality
  variational principle from which naive mean field (and Bethe / belief propagation) descend; the
  statistical-physics origin and the non-convex mean-field objective.
- [[beal-2003-variational-bayesian]] — variational Bayesian EM; the factored posterior
  $q(x)q(\theta)$, closed-form conjugate-exponential updates, tightness of the mean-field bound iff
  the factorization is exact, and BIC recovery in the large-data limit.
