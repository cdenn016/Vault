---
type: concept
title: "Renyi divergence"
aliases: ["Renyi divergences", "Renyi alpha-divergence", "order-alpha divergence", "Renyi relative entropy"]
tags: [cluster/info-geometry, project/transformer, project/multi-agent]
status: draft
created: 2026-06-18
updated: 2026-07-10
---

# Renyi divergence

## Definition
The **Renyi divergence** of order $\alpha$ is a one-parameter family of statistical
"distances" between two probability distributions $P$ and $Q$. For an order
$\alpha \in (0,1) \cup (1,\infty)$ and densities $p, q$ with respect to a common
base measure, it is defined as

$$
D_\alpha(P \| Q) = \frac{1}{\alpha - 1}
\log \int p(x)^{\alpha} q(x)^{1-\alpha} dx .
$$

It is not symmetric ($D_\alpha(P\|Q) \neq D_\alpha(Q\|P)$ in general) and does not
satisfy a triangle inequality, so it is a *divergence* rather than a metric, but it
is non-negative and vanishes if and only if $P = Q$. The order $\alpha$ changes
the weighting of density-ratio regions. Any claim about posterior coverage or
mode selection additionally requires the argument orientation and the complete
variational objective. The **Kullback-Leibler divergence is the limit**
$\alpha \to 1$:
by L'Hopital's rule the ratio above tends to
$D_1(P\|Q) = \int p \log(p/q)dx = \mathrm{KL}(P\|Q)$. Thus Renyi divergence is a
strict generalization of KL, with KL recovered as the order-one member of the
family. This limiting relationship, together with the family's convexity,
monotonicity, and data-processing properties, is established definitively in
[[vanerven-2014-renyi-kl]].

## Why it matters here
The gauge-theoretic VFE transformer uses an order-$\alpha$ Rényi divergence as
one pairwise discrepancy between Gaussian beliefs. The configured term is not
the variational Rényi bound of [[li-turner-2016-renyi-vi|Li & Turner]], does not
bound log evidence, and does not make the separate belief and decode objectives
one [[Evidence lower bound (ELBO)|ELBO]]. Its order controls density-ratio
sensitivity within that oriented pairwise term. [[gl-k-attention-2026-07-09-review-revision]]

## Details
**The variational Renyi bound.** Standard variational inference maximizes the ELBO,
a lower bound on the log evidence $\log p(x)$ built from the KL divergence between
$q$ and the posterior. [[li-turner-2016-renyi-vi]] replace KL with $D_\alpha$ to
obtain the **variational Renyi (VR) bound**

$$
\mathcal{L}_\alpha(q; x) = \frac{1}{1-\alpha}
\log \mathbb{E}_{q}\left[\left(\frac{p(x,z)}{q(z)}\right)^{1-\alpha}\right].
$$

At $\alpha = 1$ this reduces to the usual ELBO
$\mathbb{E}_q[\log p(x,z)-\log q(z)]$; as $\alpha \to 0$ it becomes
$\log p(x)$ exactly. For $0\leq\alpha\leq1$, monotonicity places the bound
between those endpoints. Orders above one lie beyond the ELBO side of this
ordering and are not sandwiched between the order-zero and order-one values.

**Order and orientation.** The implemented term is
`DiagonalGaussian.renyi_closed_form`, oriented as $D_\alpha(q\|p)$ with the
belief first. At order one it tends to $\mathrm{KL}(q\|p)$. Reversing the
arguments tends instead to $\mathrm{KL}(p\|q)$; the two orientations do not
coincide. Order alone therefore does not determine a universal inference
regime. The Li–Turner bound above has its own target-over-belief construction
and must be analyzed separately from this pairwise divergence.

**Relation to alpha-divergences and information geometry.** After matching
parameters, Rényi and Amari divergences are nonlinear monotone transforms of a
common power integral. This preserves ordering and the equality set, but not
gradients, Hessians, Bregman structure, dual connections, or global geometry.
A smooth order-Rényi divergence induces the [[Fisher information metric]] only
up to an order-dependent positive scale in its local quadratic term. Amari's
alpha-connections arise from the Amari divergence family and cannot be assigned
to Rényi orders by parameter relabeling. See [[Alpha-divergence]],
[[amari-2000-methods-information-geometry]], and
[[zhang-2004-divergence-duality-convex]].

**Gaussian closed forms.** For two Gaussians the integral $\int p^\alpha q^{1-\alpha}$
is tractable, so $D_\alpha$ between diagonal-Gaussian beliefs has a closed form in
terms of $\mu$ and $\Sigma$ — convenient given the architecture's per-token
$\mathcal{N}(\mu,\Sigma)$ representation.

## In this work
- **`divergence_family: renyi`** — the config sets the belief/prior discrepancy
  measure to the order-$\alpha$ Renyi family, with KL recovered at $\alpha \to 1$
  as documented in [[vanerven-2014-renyi-kl]].
- **Belief objective** — the belief-side discrepancy can use the Rényi family,
  with KL recovered at order one. The decoder still minimizes separate cross-entropy,
  so the complete loop is not one variational Rényi bound.
- **Coupling to the optimizer** — joint Gaussian beliefs retain their Fisher
  geometry; the covariance block is one-half conventional AIRM. This does not
  make the frame or decode M-step a Fisher natural gradient;
  the audited frame table uses plain AdamW, with the configured pullback/heavy-ball path inactive. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial: The config exposes `divergence_family` as a categorical
> choice; the specific scheduled or learned value of the order $\alpha$ is a
> training detail not fixed by the family declaration itself, so its precise
> setting per run should be read from the run config rather than inferred here.

## Sources
- [[li-turner-2016-renyi-vi]] — the variational Renyi bound; one-parameter family interpolating ELBO to log evidence.
- [[vanerven-2014-renyi-kl]] — definitive survey of order-$\alpha$ Renyi divergence; KL as the $\alpha \to 1$ limit.
- [[amari-2000-methods-information-geometry]] — alpha-divergences, alpha-connections, and dually-flat exponential-family geometry.
- [[zhang-2004-divergence-duality-convex]] — convex-analytic construction of the parametric alpha-divergence family from one convex potential, with dual alpha-connections and KL recovered at $\alpha = \pm 1$.
- [[amari-1998-natural-gradient]] — Fisher-metric natural gradient that pairs with the divergence on the same manifold.
- [[cover-thomas-2006-elements-information-theory]] — defines entropy, KL / relative entropy, and mutual information, the order-one ($\alpha \to 1$) limit of Renyi divergence and the foundation of the free-energy KL and attention-entropy terms.

## See also
- [[Alpha-divergence]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Precision weighting]]
- [[Variational EM]]
