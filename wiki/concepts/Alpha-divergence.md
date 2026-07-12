---
type: concept
title: Alpha-divergence
aliases:
  - Alpha divergence
  - α-divergence
  - Amari alpha-divergence
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-18
updated: 2026-07-10
---

# Alpha-divergence

## Definition

An **alpha-divergence** is a one-parameter family of dissimilarity measures
$D_\alpha(p \| q)$ between two probability distributions, indexed by a real
parameter $\alpha$, that quantifies how far $q$ is from $p$ while smoothly
interpolating between several classical divergences. Two closely related
conventions appear in this research program, and it is worth stating both
precisely.

The first is **Amari's alpha-divergence** from information geometry, which for
$\alpha \neq \pm 1$ is

$$
D_\alpha(p \| q) = \frac{4}{1-\alpha^2}\left(1 - \int p(x)^{\frac{1+\alpha}{2}} q(x)^{\frac{1-\alpha}{2}} dx\right).
$$

In the limits $\alpha \to 1$ and $\alpha \to -1$ this recovers the two
Kullback–Leibler divergences $\mathrm{KL}(p\|q)$ and $\mathrm{KL}(q\|p)$,
and at $\alpha = 0$ it reduces (up to a constant) to the squared Hellinger
distance, which is symmetric. This is the family that sits inside [[amari-2000-methods-information-geometry|Methods of Information Geometry]] alongside the dual **alpha-connections** on a statistical manifold.

The second convention is the **Rényi alpha-divergence** of order
$\alpha > 0,\ \alpha \neq 1$,

$$
D^{R}_\alpha(p \| q) = \frac{1}{\alpha - 1} \log \int p(x)^{\alpha} q(x)^{1-\alpha} dx ,
$$

whose $\alpha \to 1$ limit is exactly $\mathrm{KL}(p\|q)$. For a fixed power
integral, Rényi and Amari divergences are related by a nonlinear monotone
transform after matching their parameters. That relation preserves ordering
and equality at zero, but it does not preserve gradients, Hessians, Bregman or
dual structure, or global geometry. Smooth members recover Fisher geometry
locally only up to an order-dependent positive scale; see [[Renyi divergence]]
and [[vanerven-2014-renyi-kl|van Erven & Harremoës]].

> [!note] Editorial: The literature is split on the symbol $\alpha$ — Amari's
> $\alpha$ and Rényi's $\alpha$ differ by an affine change of variable
> ($\alpha_{\text{Amari}} = 2\alpha_{\text{Rényi}} - 1$ in one common
> convention). This page uses $\alpha$ for the order generically and names the
> convention whenever the exact formula matters.

## Why it matters here

The VFE transformer configures an order-$\alpha$ Rényi divergence for pairwise
belief discrepancies. This is not the variational Rényi bound of
[[li-turner-2016-renyi-vi|Li & Turner]], does not bound log evidence, and does
not replace the separate decode cross-entropy with an ELBO. The order changes
which density-ratio regions receive greater weight, but any language about
posterior mass or modes requires a specified orientation and variational
objective. Amari's alpha-divergences and alpha-connections are a distinct
information-geometric construction; they cannot be identified with the
configured Rényi order by a symbol match. The joint Gaussian belief update uses
Fisher geometry, whose covariance block is one-half conventional AIRM, whereas
the audited frame table uses plain AdamW and leaves the configured geometric/heavy-ball path inactive.
[[gl-k-attention-2026-07-09-review-revision]]

## Details

**Special cases and limits.** Writing the Rényi form, the value of $\alpha$
selects qualitatively different behaviors:

- $\alpha \to 1$: the divergence as written reduces to
  $D^{R}_\alpha \to \mathrm{KL}(p\|q)$. Reversing the arguments instead gives
  $\mathrm{KL}(q\|p)$; orientation therefore remains part of the definition.
- $\alpha \to 0$: the order-Rényi divergence has its support-sensitive limit.
  Separately, the Li–Turner variational bound recovers log marginal likelihood
  at its order-zero endpoint; this is a property of that bound, not of the
  configured pairwise discrepancy.
- $\alpha = \tfrac12$ (Rényi): $D^{R}_{1/2}=-2\log BC$, where $BC$ is the
  Bhattacharyya coefficient. Amari's symmetric member is a constant multiple
  of squared Hellinger distance. These quantities are monotone functions of
  one another, not globally proportional.
- $\alpha \to \infty$: the *worst-case* / min-max member, dominated by the point
  of largest density ratio.

**Properties.** Order-Rényi divergence is nonnegative, monotone
non-decreasing in its order, and satisfies data processing for positive orders.
Joint convexity holds in the standard range $0<\alpha<1$, not uniformly for
all orders. Specialized Rényi projection and Pythagorean results require their
stated order, existence, and alpha-convexity assumptions. The dual e-/m-
projection theorem belongs to KL/Amari dualistic geometry and does not transfer
through the nonlinear monotone relation. See
[[vanerven-2014-renyi-kl|van Erven & Harremoës]].

**Local geometry.** Expanding a smooth divergence around equality yields the
[[Fisher information metric]] up to a convention- and order-dependent positive
scale. A nonlinear monotone transform changes that scale and higher derivatives,
so it does not transfer the induced affine connections or global geometry.
Amari's alpha-connections belong to the Amari divergence family, not to Rényi
orders merely because both use the symbol $\alpha$.

**Estimation in the Gaussian case.** When $p$ and $q$ are diagonal Gaussians —
the family the architecture uses for token beliefs — the alpha-power integral
$\int p^{\alpha} q^{1-\alpha}$ has a closed form, so both the Rényi and Amari
divergences between two Gaussian beliefs are available analytically. The
implemented pairwise order-Rényi term is therefore differentiable directly in
the belief parameters $(\mu, \Sigma)$ and does not require a recognition
network or a sampled variational bound.

## In this work

The alpha-divergence surfaces in several wired-in places in the VFE
transformer:

- **Belief divergence.** `divergence_family: "renyi"` selects an order-$\alpha$
  pairwise Rényi divergence in the belief objective, with KL recovered as
  $\alpha\to1$. This configured divergence is not thereby the variational
  Rényi bound of [[li-turner-2016-renyi-vi|Li & Turner]], and it does not turn
  the separate belief and decode objectives into one [[Variational EM]] loop.
- **Belief fitting.** The order $\alpha$ changes sensitivity to density-ratio
  tails in the oriented pairwise discrepancy. It does not, without a specified
  posterior approximation objective, establish a universal coverage-versus-mode
  interpretation for the belief filter.
- **Scoped geometry.** Amari's alpha-divergences and alpha-connections form an
  information-geometric family distinct from order-$\alpha$ Rényi divergence.
  A smooth Rényi divergence induces Fisher geometry locally only up to an
  order-dependent positive scale; for the standard convention its mean-parameter
  Hessian carries a factor $\alpha$. The joint Gaussian belief update has Fisher
  geometry, with a covariance block equal to one-half conventional AIRM, while
  the audited frame table uses plain AdamW. No one dually-flat
  construction identifies all three objects. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-07-10): The config exposes the pairwise divergence
> family and order. At $\alpha=1$ that divergence is KL; this does not make the
> complete two-objective schedule a standard ELBO.

## Sources

- [[li-turner-2016-renyi-vi]] — the variational Rényi bound; the
  $\alpha$-family of variational objectives interpolating ELBO ↔ log marginal
  likelihood.
- [[vanerven-2014-renyi-kl]] — definitive survey of the order-$\alpha$ Rényi
  divergence: convexity, monotonicity, data processing, Pythagorean geometry,
  and KL as the $\alpha \to 1$ limit.
- [[amari-2000-methods-information-geometry]] — Amari's alpha-divergence,
  alpha-connections, and the dually-flat exponential-family geometry.
- [[zhang-2004-divergence-duality-convex]] — convex-analytic construction of the
  parametric alpha-divergence family from one convex potential, with its common
  Fisher-type metric and dual alpha-connections, recovering the Bregman/canonical
  KL divergence of a dually-flat space at $\alpha = \pm 1$.
- [[amari-1998-natural-gradient]] — Fisher natural-gradient geometry for the
  Gaussian belief family; local divergence metrics may differ by scale.
- [[nielsen-2020-elementary-introduction-information-geometry]] — pedagogical
  information-geometry background for belief-side divergence and Fisher geometry.
- [[kingma-2013-auto-encoding-variational-bayes]] — reparameterized,
  amortized Gaussian variational inference, the substrate the divergence acts
  on.
- [[friston-2010-free-energy-principle]], [[neal-1998-variational-em]],
  [[bogacz-2017-free-energy-tutorial]] — KL-based ELBO/free-energy comparison
  material; order one recovers the pairwise KL term, not the deployed complete
  objective.

## See also

- [[Renyi divergence]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Reparameterization trick]]
- [[Amortized inference]]
- [[Precision weighting]]
