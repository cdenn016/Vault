---
type: concept
title: "Exponential family"
aliases:
  - "Exponential families"
  - "Exponential Families"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-06-21
---

# Exponential family

An **exponential family** is a parametric class of probability distributions whose
densities share a common functional skeleton: an inner product between a parameter vector
and a fixed set of *sufficient statistics*, wrapped in an exponential and normalized. This
single algebraic form is what makes the family the natural habitat of variational inference
and [[Information geometry and natural gradient|information geometry]]: it carries a pair of
dual coordinate systems, a convex potential that generates all moments, a Fisher metric that
is literally a Hessian, and conjugate-prior structure that keeps Bayesian updates in closed
form. The Gaussian belief tuples $(\mu, \Sigma)$ used throughout the gauge-theoretic VFE
program are members of this family, so the abstract structure below is the working geometry
of the model, not a side note.

## Definition — canonical form

A family $\{p(x \mid \eta)\}$ is an exponential family in **canonical (natural) form** when
its density with respect to a base measure can be written

$$
p(x \mid \eta) \;=\; h(x)\,\exp\!\big(\langle \eta,\, T(x)\rangle - A(\eta)\big),
$$

where

- $T(x)$ is the **sufficient statistic** — a vector-valued function of the data that captures
  everything the data say about the parameter (see [[Sufficient statistics]]). The
  Fisher–Neyman factorization that defines sufficiency is exactly the $h(x)\exp(\langle\eta,T(x)\rangle)$
  shape here, and exponential families are precisely the regular models admitting a
  *finite-dimensional* sufficient statistic that does not grow with sample size
  [[wainwright-2008-graphical-models-variational]].
- $\eta$ is the **natural** (or **canonical**) **parameter**, living in the convex set
  $\Theta = \{\eta : A(\eta) < \infty\}$;
- $h(x) \ge 0$ is the **base measure** (carrier), independent of $\eta$;
- $A(\eta)$ is the **log-partition** (or **cumulant**) **function**,
  $$
  A(\eta) \;=\; \log \int h(x)\,\exp\!\big(\langle \eta, T(x)\rangle\big)\,d\nu(x),
  $$
  the normalizer that makes the density integrate to one.

The family is *minimal* when the components of $T$ are affinely independent (no linear
combination is constant a.s.), so that $\eta$ is identifiable; it is *regular* when $\Theta$
is open. These regularity conditions are what license the derivative identities below
[[nielsen-2020-elementary-introduction-information-geometry]].

> [!note] Editorial: The prompt's compact "$\eta \cdot T(x)$" is the inner product
> $\langle \eta, T(x)\rangle$ written above; the dot and the angle brackets denote the same
> pairing of the natural parameter against the sufficient statistic.

## Log-partition as a cumulant generator

Because $A(\eta)$ is the log of a moment-generating-style integral, differentiating it in
$\eta$ pulls down cumulants of the sufficient statistic. The first two derivatives give

$$
\nabla A(\eta) \;=\; \mathbb{E}_{\eta}[\,T(x)\,] \;=:\; \mu,
\qquad
\nabla^2 A(\eta) \;=\; \operatorname{Cov}_{\eta}[\,T(x)\,].
$$

The gradient is the **mean of the sufficient statistic**; the Hessian is its **covariance**.
Higher derivatives yield higher cumulants — hence the name *cumulant function*. Two structural
facts follow immediately:

1. **Convexity.** Since $\nabla^2 A = \operatorname{Cov}_\eta[T] \succeq 0$, $A$ is convex
   (strictly convex on a minimal family, where the covariance is positive definite). Convexity
   of the log-partition is the analytic backbone of the whole variational picture
   [[wainwright-2008-graphical-models-variational]].
2. **Moments are coordinates.** The map $\eta \mapsto \mu = \nabla A(\eta)$ is a smooth,
   invertible change of coordinates on a minimal regular family.

## Natural ↔ mean: the dual parameters

The second fact above means an exponential family carries **two** equally natural coordinate
systems related by a [[Bregman divergence|Legendre]] transform:

- the **natural parameters** $\eta$, and
- the **mean (expectation) parameters** $\mu = \nabla A(\eta) = \mathbb{E}_\eta[T(x)]$.

Define the convex conjugate of the log-partition function,

$$
A^{*}(\mu) \;=\; \sup_{\eta}\,\big\{\langle \eta, \mu\rangle - A(\eta)\big\}.
$$

For exponential families $A^{*}$ is the **negative entropy** of the distribution as a function
of its mean parameters [[wainwright-2008-graphical-models-variational]]. The two potentials
$(A, A^{*})$ form a Legendre dual pair, and the coordinate maps are mutual inverses:

$$
\mu = \nabla A(\eta), \qquad \eta = \nabla A^{*}(\mu).
$$

In information-geometric language $(\eta, \mu)$ are the two global affine coordinate systems of
a **dually flat** [[Statistical manifold]]: $\eta$ is flat for the *exponential* ($e$-)
connection, $\mu$ is flat for the *mixture* ($m$-) connection, and the two are tied together
by the Legendre transform of $A$
[[amari-2000-methods-information-geometry]][[nielsen-2020-elementary-introduction-information-geometry]].
This dual-coordinate structure is exactly what the VFE architecture exploits when it moves a
belief between its natural representation (e.g. precision $\Sigma^{-1}\mu$, $-\tfrac12\Sigma^{-1}$)
and its moment representation $(\mu, \Sigma)$.

The canonical divergence between two points of a dually flat manifold is the **Bregman
divergence** of $A$ (equivalently of $A^{*}$), which for exponential families *equals the
Kullback–Leibler divergence*:

$$
\mathrm{KL}\big(p_{\eta_1} \,\|\, p_{\eta_2}\big)
\;=\; A(\eta_2) - A(\eta_1) - \langle \nabla A(\eta_1),\, \eta_2 - \eta_1\rangle
\;=\; D_{A}(\eta_2 \,\|\, \eta_1),
$$

so KL between two members of the family is just the gap between $A$ and its first-order Taylor
expansion — a [[Bregman divergence]]
[[amari-2000-methods-information-geometry]][[nielsen-2020-elementary-introduction-information-geometry]].
The continuous $\alpha$-deformation of this divergence is the [[Alpha-divergence]] family
(KL is the $\alpha\to\pm1$ limit).

## Hessian = Fisher information

Differentiating the score $\nabla_\eta \log p(x\mid\eta) = T(x) - \nabla A(\eta)$ shows that the
[[Fisher information metric]] of an exponential family in natural coordinates is *exactly* the
Hessian of the log-partition function:

$$
g(\eta) \;=\; \mathbb{E}_\eta\!\big[\nabla_\eta \log p \,\nabla_\eta \log p^{\top}\big]
\;=\; -\,\mathbb{E}_\eta\!\big[\nabla^2_\eta \log p\big]
\;=\; \nabla^2 A(\eta) \;=\; \operatorname{Cov}_\eta[T(x)].
$$

So the three objects — the Fisher information, the negative expected log-likelihood Hessian,
and the covariance of the sufficient statistic — coincide
[[nielsen-2020-elementary-introduction-information-geometry]][[amari-2000-methods-information-geometry]].
In the dual mean coordinates the Fisher metric is the Hessian of the conjugate potential,
$g^{*}(\mu) = \nabla^2 A^{*}(\mu) = g(\eta)^{-1}$, so the natural and mean charts carry mutually
inverse Fisher metrics — the precise sense in which they are *dual*. This identity is what makes
the [[Natural gradient]] cheap to reason about on these families: preconditioning by $g^{-1}$ is
preconditioning by the curvature of $A$, and on a dually flat manifold the natural-gradient step
in one coordinate system is an ordinary gradient step in the other
[[amari-1998-natural-gradient]].

> [!note] Editorial: This chain — *Hessian of $A$ = covariance of $T$ = Fisher metric =
> inverse-metric of the dual chart* — is why the project can treat "use the Fisher metric" and
> "use the curvature of the log-partition" as the same instruction for Gaussian beliefs, and why
> the M-step's Fisher/Killing preconditioning is geometrically the invariant-metric choice rather
> than an arbitrary curvature estimate (cf. [[amari-2000-methods-information-geometry]]).

## Gaussian beliefs as the working instance

The multivariate Gaussian $\mathcal{N}(m, \Sigma)$ is the exponential family the VFE program runs
on (see [[Gaussian Beliefs]]). Writing the density in canonical form gives

$$
T(x) = \big(x,\; x x^{\top}\big),
\qquad
\eta = \big(\Sigma^{-1} m,\; -\tfrac12 \Sigma^{-1}\big),
\qquad
\mu = \big(m,\; \Sigma + m m^{\top}\big),
$$

with log-partition $A(\eta) = \tfrac12 m^{\top}\Sigma^{-1} m + \tfrac12\log\det(2\pi\Sigma)$. The
natural parameters are the **information form** $(\Sigma^{-1}m,\ -\tfrac12\Sigma^{-1})$ used in
Gaussian belief propagation; the mean parameters are the **moment form**. The natural-to-mean map
$\nabla A$ is precisely the passage between these two representations
[[wainwright-2008-graphical-models-variational]]. Three consequences matter for the model:

- **Closed-form KL.** Because the Gaussian is an exponential family, $\mathrm{KL}(\mathcal N_1\|\mathcal N_2)$
  is the Bregman divergence of $A$ and has a closed form, which is what makes the entropy-regularized
  KL-consensus coupling and the divergence terms of the [[Variational free energy]] tractable
  [[Gaussian Beliefs]].
- **SPD covariance geometry.** The covariance block $\Sigma$ is symmetric positive definite; the
  Fisher geometry of the Gaussian family restricted to $\Sigma$ is the affine-invariant SPD metric the
  model uses for retraction, tying belief geometry to the same invariant metric
  [[amari-2000-methods-information-geometry]].
- **Dual charts in the code.** Moving between the Lie-algebra `phi` coordinate, the SPD covariance,
  and the moment representation is moving between $\eta$ and $\mu$ on the same dually flat manifold
  [[nielsen-2020-elementary-introduction-information-geometry]].

## Conjugacy

A prior over the natural parameters is **conjugate** to an exponential-family likelihood when it
has the matching exponential-family shape

$$
\pi(\eta \mid \chi, \nu) \;\propto\; \exp\!\big(\langle \eta, \chi\rangle - \nu\, A(\eta)\big),
$$

with hyperparameters $(\chi, \nu)$ playing the role of pseudo-observations. The hallmark of
conjugacy is that the posterior stays in the *same* family with **additively updated** natural
parameters: observing data with sufficient statistic $\sum_i T(x_i)$ sends
$(\chi,\nu) \mapsto (\chi + \sum_i T(x_i),\ \nu + n)$. Bayesian updating is therefore linear in the
natural parameters — a sum of sufficient statistics — which is the source of every closed-form
update in the program. This **conjugate-exponential** structure (see [[Conjugate-Exponential Family]])
is exactly the condition under which variational Bayesian EM yields closed-form coordinate-ascent
updates whose posteriors remain in the family
[[wainwright-2008-graphical-models-variational]], and it is why the Gaussian belief state can be
refined by the [[Variational EM]] E-step without leaving the Gaussian family.

## Relevance to this research

Exponential families are the connective tissue of the gauge-theoretic VFE program; nearly every
other piece of its machinery is a property of this one structure.

- **Beliefs are exponential-family members.** Per-token / per-agent Gaussian beliefs $(\mu,\Sigma)$
  are exponential-family distributions, so they automatically inherit dually flat geometry, closed-form
  KL, and a Fisher metric equal to the log-partition Hessian [[Gaussian Beliefs]].
- **Variational free energy is conjugate duality.** The VFE objective $F = \mathrm{KL}(q\|p)$ is an
  instance of the conjugate-dual variational principle: $A(\eta) = \sup_{\mu\in\mathcal M}\{\langle\eta,\mu\rangle - A^{*}(\mu)\}$,
  and the [[Evidence lower bound (ELBO)]] is its rearrangement
  [[wainwright-2008-graphical-models-variational]]. The Bethe/mean-field free energies that the
  monograph derives are the statistical-physics predecessors of the model's free-energy functional.
- **E/M steps are dual projections.** The [[Variational EM]] split — E-step refines beliefs, M-step
  moves parameters — is the pair of *dual projections* (m-projection / e-projection) on the dually flat
  exponential-family manifold, with the [[Natural gradient]] M-step preconditioned by the inverse Fisher
  metric, i.e. the Hessian of $A^{*}$ [[amari-2000-methods-information-geometry]][[amari-1998-natural-gradient]].
- **Attention as an entropy-regularized coupling.** The softmax attention weights arise as the
  stationary point of an entropy-regularized variational problem — the same conjugate-duality template
  that gives belief-propagation fixed points in [[wainwright-2008-graphical-models-variational]].
- **Maximum-entropy lineage.** Exponential families are the maximum-entropy distributions subject to
  expectation constraints on $T(x)$, the Jaynes derivation that licenses reading the natural parameters
  as Lagrange multipliers and connects the formalism to statistical mechanics
  [[jaynes-1957-information-statistical-mechanics]].

For a worked review aimed at practitioners, [[blei-2017-variational-inference]] develops coordinate-ascent
variational inference directly on conditionally-conjugate exponential families; the dually flat geometry is
laid out pedagogically in [[nielsen-2020-elementary-introduction-information-geometry]] and at research depth
in [[amari-2000-methods-information-geometry]].

## Related

[[Statistical manifold]], [[Fisher information metric]], [[Variational free energy]],
[[Natural gradient]], [[Information geometry and natural gradient]], [[Bregman divergence]],
[[Alpha-divergence]], [[Sufficient statistics]], [[Conjugate-Exponential Family]],
[[Gaussian Beliefs]], [[Variational EM]], [[Evidence lower bound (ELBO)]],
[[Amari-Chentsov tensor]]

## Sources

[[wainwright-2008-graphical-models-variational]], [[amari-2000-methods-information-geometry]],
[[nielsen-2020-elementary-introduction-information-geometry]], [[amari-1998-natural-gradient]],
[[jaynes-1957-information-statistical-mechanics]], [[blei-2017-variational-inference]]
