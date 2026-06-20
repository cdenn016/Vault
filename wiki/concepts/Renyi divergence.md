---
type: concept
title: "Renyi divergence"
aliases: ["Renyi divergences", "Renyi alpha-divergence", "order-alpha divergence", "Renyi relative entropy"]
tags: [cluster/info-geometry, project/transformer, project/multi-agent]
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Renyi divergence

## Definition
The **Renyi divergence** of order $\alpha$ is a one-parameter family of statistical
"distances" between two probability distributions $P$ and $Q$. For an order
$\alpha \in (0,1) \cup (1,\infty)$ and densities $p, q$ with respect to a common
base measure, it is defined as

$$
D_\alpha(P \,\|\, Q) \;=\; \frac{1}{\alpha - 1}\,
\log \int p(x)^{\alpha}\, q(x)^{1-\alpha}\, dx .
$$

It is not symmetric ($D_\alpha(P\|Q) \neq D_\alpha(Q\|P)$ in general) and does not
satisfy a triangle inequality, so it is a *divergence* rather than a metric, but it
is non-negative and vanishes if and only if $P = Q$. The order $\alpha$ tunes how
strongly the divergence weights regions where the two distributions disagree:
small $\alpha$ is mass-covering (forgiving of $Q$ placing mass where $P$ has none),
large $\alpha$ is mode-seeking (penalizing such mismatches heavily). The crucial
fact is that the **Kullback-Leibler divergence is the limit** $\alpha \to 1$:
by L'Hopital's rule the ratio above tends to
$D_1(P\|Q) = \int p \log(p/q)\,dx = \mathrm{KL}(P\|Q)$. Thus Renyi divergence is a
strict generalization of KL, with KL recovered as the order-one member of the
family. This limiting relationship, together with the family's convexity,
monotonicity, and data-processing properties, is established definitively in
[[vanerven-2014-renyi-kl]].

## Why it matters here
The gauge-theoretic VFE transformer declares its `divergence_family` to be
`renyi`, meaning the discrepancy between the per-token approximate posterior (the
Gaussian belief $q(z) = \mathcal{N}(\mu, \Sigma)$) and the prior/target is measured
with $D_\alpha$ rather than with plain KL. Because KL is the $\alpha \to 1$ limit,
this is a *superset* of the standard variational objective: the model can recover
ordinary [[Variational free energy]] / [[Evidence lower bound (ELBO)]] training as a
special case, while the order $\alpha$ becomes a knob that reshapes the bound. The
practical payoff, following [[li-turner-2016-renyi-vi]], is that varying $\alpha$
smoothly interpolates between the (loose, mode-seeking) ELBO at $\alpha \to 1$ and
the (tight) log marginal likelihood as $\alpha \to 0$, and lets the trainer trade
off mass-covering versus mode-seeking behaviour of the learned beliefs. In a model
whose entire job is to maintain calibrated Gaussian beliefs and propagate
[[Precision weighting|precision-weighted]] [[Prediction error]], the choice of how
to penalize belief-vs-target mismatch is exactly the choice of $\alpha$.

## Details
**The variational Renyi bound.** Standard variational inference maximizes the ELBO,
a lower bound on the log evidence $\log p(x)$ built from the KL divergence between
$q$ and the posterior. [[li-turner-2016-renyi-vi]] replace KL with $D_\alpha$ to
obtain the **variational Renyi (VR) bound**

$$
\mathcal{L}_\alpha(q; x) \;=\; \frac{1}{1-\alpha}\,
\log\, \mathbb{E}_{q}\!\left[\left(\frac{p(x,z)}{q(z)}\right)^{1-\alpha}\right].
$$

At $\alpha = 1$ this reduces to the usual ELBO $\mathbb{E}_q[\log p(x,z) - \log q(z)]$;
as $\alpha \to 0$ it becomes $\log p(x)$ exactly. The bound is monotone in $\alpha$,
so the family is sandwiched between these endpoints and the single hyperparameter
$\alpha$ controls how tight the surrogate objective is.

**Mass-covering versus mode-seeking.** For $\alpha < 1$ the objective behaves like
the mass-covering "inclusive" KL$(p\|q)$ regime, encouraging the Gaussian belief to
spread over all of the target's support; for $\alpha > 1$ it sharpens toward
mode-seeking behaviour. Negative $\alpha$ values are also admissible in the VR
framework and give still more mass-covering objectives, useful when underestimating
uncertainty is costly.

> [!note] Editorial (orientation, verified against code 2026-06-18): These regime
> labels follow the VR-bound orientation $p(x,z)/q(z)$ (target-over-belief). The
> implemented family member is the *reciprocal* — `DiagonalGaussian.renyi_closed_form`
> computes $D_\alpha(q\|p)$ with the belief $q$ as the first argument (`mu_q=self`),
> and `free_energy.pairwise_energy` always passes the belief first
> (`functional(q_b, key)`). So in code-orientation terms the $\alpha<1$ /
> $\alpha>1$ mass-covering / mode-seeking reading is stated relative to $D_\alpha(q\|p)$,
> the argument order opposite to the $p\|q$ phrasing above. At the live `renyi_order = 1.0`
> both orientations coincide (KL), so the distinction only bites for a swept $\alpha \neq 1$.

**Relation to alpha-divergences and information geometry.** Renyi divergence is
monotonically related to the *alpha*-divergence family of Amari (the two are
reparameterizations of the same underlying $f$-divergence quantity built from the
integral $\int p^\alpha q^{1-\alpha}$). The alpha-divergences and their associated
**alpha-connections** are the backbone of the dually-flat exponential-family
geometry developed in [[amari-2000-methods-information-geometry]]; see
[[Alpha-divergence]]. Because the model's beliefs are exponential-family
(diagonal-Gaussian) objects, this geometric structure is not incidental: the same
manifold whose metric is the [[Fisher information metric]] (used for the
[[Natural gradient]]) carries the alpha/Renyi divergences as its canonical
contrast functions, so the divergence choice and the optimizer geometry are two
faces of one information-geometric picture.

**Gaussian closed forms.** For two Gaussians the integral $\int p^\alpha q^{1-\alpha}$
is tractable, so $D_\alpha$ between diagonal-Gaussian beliefs has a closed form in
terms of $\mu$ and $\Sigma$ — convenient given the architecture's per-token
$\mathcal{N}(\mu,\Sigma)$ representation.

## In this work
- **`divergence_family: renyi`** — the config sets the belief/prior discrepancy
  measure to the order-$\alpha$ Renyi family, with KL recovered at $\alpha \to 1$
  as documented in [[vanerven-2014-renyi-kl]].
- **Training objective** — the free-energy / ELBO loss of the
  [[Variational EM]] loop is replaced by (or generalized to) the variational Renyi
  bound of [[li-turner-2016-renyi-vi]]; the E-step that relaxes beliefs and the
  M-step that updates parameters then descend this Renyi free energy rather than the
  pure KL one.
- **Coupling to the optimizer** — because the beliefs live on a statistical
  manifold, the Renyi/alpha contrast pairs naturally with the Fisher-preconditioned
  [[Natural gradient]] M-step (see [[amari-1998-natural-gradient]]), keeping the
  objective and the update geometry consistent.

> [!note] Editorial: The config exposes `divergence_family` as a categorical
> choice; the specific scheduled or learned value of the order $\alpha$ is a
> training detail not fixed by the family declaration itself, so its precise
> setting per run should be read from the run config rather than inferred here.

## Sources
- [[li-turner-2016-renyi-vi]] — the variational Renyi bound; one-parameter family interpolating ELBO to log evidence.
- [[vanerven-2014-renyi-kl]] — definitive survey of order-$\alpha$ Renyi divergence; KL as the $\alpha \to 1$ limit.
- [[amari-2000-methods-information-geometry]] — alpha-divergences, alpha-connections, and dually-flat exponential-family geometry.
- [[amari-1998-natural-gradient]] — Fisher-metric natural gradient that pairs with the divergence on the same manifold.

## See also
- [[Alpha-divergence]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Precision weighting]]
- [[Variational EM]]
