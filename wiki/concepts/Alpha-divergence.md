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
updated: 2026-06-18
---

# Alpha-divergence

## Definition

An **alpha-divergence** is a one-parameter family of dissimilarity measures
$D_\alpha(p \,\|\, q)$ between two probability distributions, indexed by a real
parameter $\alpha$, that quantifies how far $q$ is from $p$ while smoothly
interpolating between several classical divergences. Two closely related
conventions appear in this research program, and it is worth stating both
precisely.

The first is **Amari's alpha-divergence** from information geometry, which for
$\alpha \neq \pm 1$ is

$$
D_\alpha(p \,\|\, q) \;=\; \frac{4}{1-\alpha^2}\left(1 - \int p(x)^{\frac{1+\alpha}{2}}\, q(x)^{\frac{1-\alpha}{2}}\, dx\right).
$$

In the limits $\alpha \to 1$ and $\alpha \to -1$ this recovers the two
Kullback–Leibler divergences $\mathrm{KL}(p\,\|\,q)$ and $\mathrm{KL}(q\,\|\,p)$,
and at $\alpha = 0$ it reduces (up to a constant) to the squared Hellinger
distance, which is symmetric. This is the family that sits inside [[amari-2000-methods-information-geometry|Methods of Information Geometry]] alongside the dual **alpha-connections** on a statistical manifold.

The second convention is the **Rényi alpha-divergence** of order
$\alpha > 0,\ \alpha \neq 1$,

$$
D^{R}_\alpha(p \,\|\, q) \;=\; \frac{1}{\alpha - 1}\, \log \int p(x)^{\alpha}\, q(x)^{1-\alpha}\, dx ,
$$

whose $\alpha \to 1$ limit is exactly $\mathrm{KL}(p\,\|\,q)$. The two families
are monotone reparameterizations of the same underlying quantity (the
$\alpha$-power integral, or *Chernoff $\alpha$-coefficient*), so a result about
one transfers to the other up to a change of variable; see [[Renyi divergence]]
for the order-based account and [[vanerven-2014-renyi-kl|van Erven & Harremoës]]
for the definitive treatment. Throughout, $\alpha$ is the *order* that selects
which member of the family is in force; the [[Fisher information metric]]
emerges as the common second-order (small-perturbation) limit of every member,
which is why all of them induce the *same* local geometry.

> [!note] Editorial: The literature is split on the symbol $\alpha$ — Amari's
> $\alpha$ and Rényi's $\alpha$ differ by an affine change of variable
> ($\alpha_{\text{Amari}} = 2\alpha_{\text{Rényi}} - 1$ in one common
> convention). This page uses $\alpha$ for the order generically and names the
> convention whenever the exact formula matters.

## Why it matters here

The VFE transformer declares `divergence_family: "renyi"`, which means its
training objective is built not on the plain KL term of the standard evidence
lower bound but on an $\alpha$-indexed generalization of it. Concretely, the
[[Variational free energy]] / [[Evidence lower bound (ELBO)]] objective is
replaced by a **variational Rényi bound**: a one-parameter family of bounds on
the log marginal likelihood whose tightness and mass-covering behavior are
tuned by $\alpha$ (see [[li-turner-2016-renyi-vi|Li & Turner]]). Because
$\mathrm{KL}$ is the $\alpha \to 1$ limit, the alpha-divergence is the lever
that lets the model dial *continuously* between the conventional ELBO
($\alpha \to 1$), tighter zero-avoiding objectives ($\alpha < 1$), and
mass-covering or even log-likelihood-recovering regimes ($\alpha \to 0$ gives
the exact log marginal likelihood in the Rényi convention). For per-token
diagonal-Gaussian beliefs $(\mu, \Sigma)$, this choice controls *how* the
approximate posterior is fit to the implicit true posterior — whether it hugs a
single mode or spreads to cover mass — without changing the rest of the
inference machinery.

The alpha-divergence also matters geometrically. The same $\alpha$ that indexes
the divergence indexes a dual pair of **affine connections** on the manifold of
Gaussian beliefs ([[amari-2000-methods-information-geometry|Amari & Nagaoka]]),
which is precisely the dually-flat exponential-family geometry the model's
[[Natural gradient]] M-step exploits. So the divergence family and the
optimizer's metric are two faces of one information-geometric object.

## Details

**Special cases and limits.** Writing the Rényi form, the value of $\alpha$
selects qualitatively different behaviors:

- $\alpha \to 1$: the divergence as written reduces to $D^{R}_\alpha \to \mathrm{KL}(p\,\|\,q)$.
  Mind the orientation: the *variational* Rényi bound at $\alpha\to1$ becomes the ordinary
  [[Evidence lower bound (ELBO)|ELBO]], which minimizes the reciprocal $\mathrm{KL}(q\,\|\,p)$ — the
  *exclusive*, **mode-seeking** divergence (belief $q$ first), **not** a mass-covering one. Whether
  inference is mass-covering or mode-seeking is set by $\alpha$ itself ($\alpha<1$ inclusive /
  mass-covering, $\alpha>1$ mode-seeking); see the orientation note on [[Renyi divergence]].
- $\alpha \to 0$: collapses toward $-\log \int_{\{p>0\}} q$, related to the
  *inclusive* mass-covering behavior; in the variational-bound construction of
  [[li-turner-2016-renyi-vi|Li & Turner]] the bound at $\alpha = 0$ recovers the
  exact log marginal likelihood.
- $\alpha = \tfrac12$ (Rényi) / $\alpha = 0$ (Amari): the *symmetric* member,
  proportional to the squared Hellinger distance.
- $\alpha \to \infty$: the *worst-case* / min-max member, dominated by the point
  of largest density ratio.

**Properties.** Across the whole family, $D_\alpha(p\,\|\,q) \ge 0$ with
equality iff $p = q$ almost everywhere; $D_\alpha$ is jointly convex in
$(p, q)$ over the appropriate range of $\alpha$, is monotone non-decreasing in
the order $\alpha$ (for the Rényi convention), and satisfies a **data-processing
inequality** — pushing both arguments through the same channel cannot increase
the divergence. It also obeys a **Pythagorean / projection** relation on
exponential families, the property that makes information-geometric projections
(and the dual e-/m-projections) well behaved. These facts are catalogued in
[[vanerven-2014-renyi-kl|van Erven & Harremoës]].

**Local geometry.** Expanding $D_\alpha(p \,\|\, p + \delta p)$ to second order
in a perturbation $\delta p$ yields the *same* quadratic form for every
$\alpha$: the [[Fisher information metric]]. This is the precise sense in which
all alpha-divergences agree infinitesimally and differ only in their global,
finite-displacement curvature. The mismatch between members shows up as the
$\alpha$-dependent dual connections, not in the metric itself.

**Estimation in the Gaussian case.** When $p$ and $q$ are diagonal Gaussians —
the family the architecture uses for token beliefs — the alpha-power integral
$\int p^{\alpha} q^{1-\alpha}$ has a closed form, so both the Rényi and Amari
divergences between two Gaussian beliefs are available analytically. This makes
the alpha-divergence objective differentiable through the belief parameters
$(\mu, \Sigma)$ and compatible with the [[Reparameterization trick]]
([[kingma-2013-auto-encoding-variational-bayes|Kingma & Welling]]) used to push
gradients into the recognition pathway.

## In this work

The alpha-divergence surfaces in several wired-in places in the VFE
transformer:

- **Training objective.** `divergence_family: "renyi"` makes the per-token
  free-energy / [[Evidence lower bound (ELBO)]] term an $\alpha$-order Rényi
  bound rather than a pure KL, following
  [[li-turner-2016-renyi-vi|Li & Turner]]; the KL-based ELBO of
  [[friston-2010-free-energy-principle|the free-energy principle]] and the
  Neal–Hinton negative-free-energy functional
  ([[neal-1998-variational-em|Neal & Hinton]]) are recovered as the
  $\alpha \to 1$ special case, so the existing [[Variational EM]] E-step/M-step
  loop is unchanged in form.
- **Belief fitting.** The order $\alpha$ controls the mass-covering vs.
  mode-seeking trade-off when the diagonal-Gaussian beliefs $(\mu, \Sigma)$ are
  relaxed in the E-step (cf. the precision-weighted Gaussian updates of
  [[bogacz-2017-free-energy-tutorial|Bogacz]] and the predictive-coding error
  dynamics of [[rao-1999-predictive-coding|Rao & Ballard]]).
- **Geometry of the M-step.** The alpha-connections that come bundled with the
  alpha-divergence ([[amari-2000-methods-information-geometry|Amari & Nagaoka]])
  are the dual-flat structure underlying the model's Fisher-preconditioned
  [[Natural gradient]] parameter updates
  ([[amari-1998-natural-gradient|Amari]]). The convex-analytic account of
  [[zhang-2004-divergence-duality-convex|Zhang]] makes the bundling explicit:
  one convex potential generates the entire parametric alpha-divergence family,
  each member inducing the *same* Fisher-type metric together with a dual pair
  of alpha-connections, so the program's Rényi/alpha objective and its
  natural-gradient geometry are two readings of a single dually-flat structure
  whose canonical (Bregman/KL) divergence is recovered at $\alpha = \pm 1$.

> [!note] Editorial: The config exposes the *family* name `"renyi"`; the
> specific operative value of $\alpha$ is a tunable hyperparameter of the run
> rather than a fixed architectural constant, and at $\alpha = 1$ the objective
> is bit-for-bit the standard ELBO.

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
- [[amari-1998-natural-gradient]] — the Fisher metric as the common local limit
  and the natural-gradient direction it induces.
- [[nielsen-2020-elementary-introduction-information-geometry]] — pedagogical IG
  survey grounding the model's KL divergences and natural-gradient M-step.
- [[kingma-2013-auto-encoding-variational-bayes]] — reparameterized,
  amortized Gaussian variational inference, the substrate the divergence acts
  on.
- [[friston-2010-free-energy-principle]], [[neal-1998-variational-em]],
  [[bogacz-2017-free-energy-tutorial]] — the KL-based ELBO / free-energy
  objective recovered at $\alpha \to 1$.

## See also

- [[Renyi divergence]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Reparameterization trick]]
- [[Amortized inference]]
- [[Precision weighting]]
