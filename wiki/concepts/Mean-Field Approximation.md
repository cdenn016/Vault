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
updated: 2026-07-19
---

# Mean-Field Approximation

## Definition

The **mean-field approximation** is the workhorse simplification of variational inference: it
restricts the approximating family $\mathcal{Q}$ to **fully factorized** distributions over the
latent variables,
$$
q(z) = \prod_{i=1}^{m} q_i(z_i),
$$
so that every latent variable (or block of variables) is treated as *mutually independent* under
$q$. Variational inference recasts posterior computation as optimization — one posits a family
$\mathcal{Q}$ and finds the member $q^\*(z) = \arg\min_{q\in\mathcal{Q}} \mathrm{KL}\bigl(q(z)\|p(z\mid x)\bigr)$
closest to the intractable exact posterior $p(z\mid x)$ in reverse Kullback–Leibler (KL)
divergence, equivalently maximizing the [[Evidence lower bound (ELBO)|evidence lower bound]]
$\mathrm{ELBO}(q)=\mathbb{E}_q[\log p(z,x)]-\mathbb{E}_q[\log q(z)]$
([[blei-2017-variational-inference]]). The mean-field choice is what makes this optimization
tractable: by severing the dependence structure of $q$, the per-factor problem decouples into
something solvable in closed form for a large class of models. This is the same factorization
that statistical physics calls **mean-field theory** — replacing each particle's interaction with
its neighbors by an interaction with the *average* (mean) field — and the name is inherited
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
q_j^\*(z_j) \propto \exp\Bigl( \mathbb{E}_{-j}\bigl[\log p(z_j, z_{-j}, x)\bigr] \Bigr),
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
$q(x,\theta)=q(x)q(\theta)$ separates hidden states from parameters, the VBE step updates
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

A common pathology of reverse-KL mean-field VI is underestimated posterior
variance. Factorization and divergence orientation contribute in distinct ways
([[blei-2017-variational-inference]]).

1. **The factorization discards correlations.** By construction the variational covariance is
   block-diagonal: $q(z)=\prod_i q_i(z_i)$ can represent no posterior covariance *between* factors.
   Whatever dependence the true posterior carries — strong off-diagonal couplings, ridges,
   multimodal correlations — is projected away.

2. **Reverse KL is zero-forcing.** Minimizing $\mathrm{KL}(q\|p)$ penalizes
   probability that $q$ assigns where $p$ is small. In multimodal or strongly
   dependent targets this can favor an underdispersed approximation, but it is
   not a universal theorem that every optimum selects one mode. Order-Rényi
   divergences change density-ratio weighting; their consequences require a
   stated orientation and complete variational objective. Amari alpha-divergence
   geometry is a separate construction.

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
(log-partition) function $A(\theta)=\log\int\exp\langle\theta,\phi(x)\rangle d\nu(x)$ is convex,
and its convex conjugate is the negative entropy $A^\*(\mu)$ over the marginal polytope
$\mathcal{M}$ of realizable mean parameters, giving the exact representation
$$
A(\theta) = \sup_{\mu\in\mathcal{M}} \bigl\{\langle\theta,\mu\rangle - A^\*(\mu)\bigr\}.
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

## Link to opinion-dynamics and collective behavior

The same factorization travels into the modeling of *populations of interacting agents*. In
sociophysics and [[Opinion dynamics|opinion dynamics]], a **mean-field** treatment replaces each
agent's coupling to its specific neighbors by a coupling to the population's mean (or to the
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

> [!note] Editorial (2026-07-10): Variational and population mean fields are
> analogous but not identical. Aggregate interaction does not prove posterior
> independence. A product posterior over agent latents remains an explicit
> variational-family assumption, and pairwise or aggregate coupling does not
> restore cross-agent correlations within that product family.
> [[gl-k-attention-2026-07-09-review-revision]]

## Beyond mean field

The principled extension is a hierarchy of variational families and effective theories, not a
single replacement slogan. A normalized structured posterior, such as a sparse block-Gaussian
joint over agent or token states, retains the ordinary ELBO and restores selected cross-variable
covariances. Region beliefs and counting numbers provide a cheaper intermediate construction:
Bethe and generalized region-graph free energies retain local correlations and correct overlapping
entropy contributions, with their message-passing stationary points derived by
[[yedidia-freeman-weiss-2005-region-free-energy]]. Exactness applies to the appropriate acyclic
region structures; generic loopy pseudomarginals do not automatically define a global posterior or
an evidence lower bound.

State-posterior correlation and configuration-level fluctuation theory answer different questions.
The former improves $Q(z\mid x)$ inside a fixed generative model. The latter places a probability law
over slow belief and gauge configurations, then studies connected structural fluctuations and their
coarse-grained effective action. The [[Meta-entropy]] Gibbs lift and the proposed 2PI completion in
[[participatory-it-from-bit]] occupy this second tier. They are warranted when configuration
thermodynamics, phase structure, or scale dependence is part of the scientific target; they are not
required merely to relax a product posterior.

## Relevance to this research

The VFE transformer stores one diagonal-Gaussian marginal belief per token, a
representation reminiscent of a mean-field family. The deployed target-blind
belief step is not a CAVI coordinate optimum, and its separate decode
cross-entropy means the alternating schedule is not one VB-EM/ELBO loop. A
Gaussian family alone also does not imply conjugacy or a closed-form CAVI
update. [[gl-k-attention-2026-07-09-review-revision]]

The program's distinctive moves are best read as *responses to the two known limitations of
mean field*:

- **Coupling marginals without restoring joint covariance.** Gauge transport and
  pairwise discrepancies let one token's marginal update depend on transported
  neighboring marginals. They do not change a product-form $q=\prod_i q_i$ into
  a joint distribution with nonzero cross-token covariance. Recovering posterior
  correlations would require an explicitly coupled variational family or other
  joint representation. The entropy-regularized softmax weights govern pairwise
  interactions, not the covariance structure of $q$.

- **Changing pairwise divergence sensitivity.** The belief step can replace KL
  with an order-[[Renyi divergence|Rényi divergence]], changing sensitivity to
  density-ratio tails in each oriented pairwise term. This does not by itself
  guarantee calibrated posterior variance or repair correlations removed by a
  product family. [[Alpha-divergence|Amari alpha-divergence]] is distinct.

For the **multi-agent** reading, one may explicitly choose a product posterior
over agent latents and separately define aggregate interactions. That modeling
choice links the transformer analogy to [[Opinion dynamics]] and
[[Mean-field games and continuum limits]], but aggregate coupling alone does not
derive the product factorization.

The exact-ELBO manuscript distinguishes agent-block factors, state/model channel-block factors, and a finer site-factorized comparison family. Agent-block and channel-block factors can retain dependence across all finite design points inside a factor. The moving-peer obstruction applies only to the fine family $Q=\bigotimes_{\ell,b}q_{\ell,b}$ and uses a separate site-local path for each design point. It does not cover the coarser cross-design families or restricted families lacking the required tangents. Its continuum corollary is conditional on the exact centered tangent, a common admissible rectangle, domination, and positive integrated variance; it does not construct a section-space probability law. [[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]]

## Related

[[Variational free energy]] · [[Evidence lower bound (ELBO)]] · [[Variational EM]] ·
[[Exponential family]] · [[Alpha-divergence]] · [[Natural gradient]] ·
[[Multi-agent variational free energy]] · [[GL(K) gauge-equivariant attention]] ·
[[Mean-field games and continuum limits]] · [[Opinion dynamics]] · [[Sociophysics]] ·
[[Statistical physics of social systems and collective behavior]]

## Sources

- [[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]] — typed block/site factorizations and the corrected fine-family moving-peer obstruction.
- [[blei-2017-variational-inference]] — VI as optimization; the mean-field family, CAVI updates,
  the closed-form $q_j^\*\propto\exp\mathbb{E}_{-j}[\log p(z_j,z_{-j},x)]$, non-convexity / local
  optima, and the systematic underestimation of posterior variance under reverse KL.
- [[wainwright-2008-graphical-models-variational]] — the exponential-family conjugate-duality
  variational principle from which naive mean field (and Bethe / belief propagation) descend; the
  statistical-physics origin and the non-convex mean-field objective.
- [[beal-2003-variational-bayesian]] — variational Bayesian EM; the factored posterior
  $q(x)q(\theta)$, closed-form conjugate-exponential updates, tightness of the mean-field bound iff
  the factorization is exact, and BIC recovery in the large-data limit.
- [[yedidia-freeman-weiss-2005-region-free-energy]] — Bethe and region-graph free energies,
  generalized belief propagation, and the exact-versus-loopy boundary for correlation corrections.
