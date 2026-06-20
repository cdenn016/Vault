---
type: paper
title: Divergence Function, Duality, and Convex Analysis
aliases:
  - "Jun Zhang 2004"
  - "Divergence Function, Duality, and Convex Analysis"
authors:
  - Jun Zhang
year: 2004
arxiv: null
url: https://doi.org/10.1162/08997660460734047
tags:
  - cluster/info-geometry
  - cluster/methodology
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/statistics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Divergence Function, Duality, and Convex Analysis

> [!info] Citation
> Zhang, J. (2004). Divergence Function, Duality, and Convex Analysis. Neural Computation, 16(1), 159-195. DOI 10.1162/08997660460734047.

## TL;DR

Zhang shows that a single strictly convex potential function $\Phi$ generates not one divergence but an entire one-parameter family $D^{(\alpha)}_\Phi$ indexed by a real number $\alpha$, and that this family is the right object from which to read off information geometry. Every member of the family induces the *same* Riemannian (Fisher-type) metric, so the metric is $\alpha$-independent, while the parameter $\alpha$ controls a pair of torsion-free affine connections that are dual with respect to that metric. These connections are generally curved, and they flatten exactly at the two endpoints $\alpha = \pm 1$, where the divergence collapses to the Bregman divergence built from $\Phi$ and its convex conjugate $\Phi^*$ — the canonical divergence of a dually flat space, of which Kullback-Leibler is the prototypical case. The convex-analytic vantage point also lets Zhang separate two notions of duality that are usually conflated: a *referential* duality that swaps the two arguments / sends $\alpha \to -\alpha$, and a *representational* duality that swaps the potential for its Legendre conjugate $\Phi \to \Phi^*$. The paper is, in effect, a constructive recipe: hand it one convex function and it returns a whole dualistic information geometry.

## Problem & setting

Classical information geometry (Amari and Nagaoka) starts from a statistical manifold equipped with the Fisher metric and the family of $\alpha$-connections, and divergences such as Kullback-Leibler or the Amari $\alpha$-divergence appear as objects compatible with that structure. Zhang inverts the emphasis. He asks what geometric structure a *divergence function* alone determines, and how much of the standard apparatus can be recovered purely from convex analysis applied to a potential $\Phi: \mathbb{R}^n \to \mathbb{R}$ that is smooth and strictly convex, without first assuming a manifold of probability densities. The prior art he builds on is the Eguchi construction (a divergence induces a metric from its second derivatives and a pair of dual connections from its third derivatives), Amari's $\alpha$-geometry, and Bregman's convex-analytic divergence. The setting is therefore deliberately general: the points need not be probability distributions, only elements of a convex domain, which is why the framework later specializes cleanly to the probability-simplex case but is not restricted to it.

## Method

The construction starts from a strictly convex $\Phi$ and a real parameter $\alpha$, and forms a divergence by comparing $\Phi$ evaluated at a convex interpolation of the two points against the interpolation of the values of $\Phi$. Schematically, writing the two points as $x$ and $y$, the $\alpha$-divergence built from $\Phi$ has the form
$$
D^{(\alpha)}_\Phi(x, y) \;=\; \frac{4}{1-\alpha^2}\left[\frac{1-\alpha}{2}\,\Phi(x) + \frac{1+\alpha}{2}\,\Phi(y) - \Phi\!\left(\tfrac{1-\alpha}{2}\,x + \tfrac{1+\alpha}{2}\,y\right)\right],
$$
which is nonnegative precisely because $\Phi$ is convex (the bracket is the Jensen gap) and vanishes iff $x = y$. The prefactor $4/(1-\alpha^2)$ is the normalization that makes the limits $\alpha \to \pm 1$ finite. Applying the Eguchi machinery to this $D^{(\alpha)}_\Phi$ yields the geometry: its second-order Taylor expansion in the displacement gives the metric
$$
g_{ij}(x) \;=\; \partial_i \partial_j \Phi(x),
$$
the Hessian of the potential, which carries no $\alpha$ at all — hence the $\alpha$-independent metric. The third-order terms give a totally symmetric cubic tensor $T_{ijk} = \partial_i\partial_j\partial_k \Phi$ (the Amari-Chentsov tensor for this potential), and the pair of connections is
$$
\Gamma^{(\alpha)} \;=\; \Gamma^{(0)} - \tfrac{\alpha}{2}\,T, \qquad \Gamma^{(-\alpha)} \;=\; \Gamma^{(0)} + \tfrac{\alpha}{2}\,T,
$$
so $\nabla^{(\alpha)}$ and $\nabla^{(-\alpha)}$ are dual (conjugate) with respect to $g$: the $\alpha \to -\alpha$ reflection is exactly metric-duality of connections. In the limit $\alpha = \pm 1$ the interpolation degenerates to an endpoint and $D^{(\pm 1)}_\Phi$ becomes the Bregman divergence
$$
B_\Phi(x, y) \;=\; \Phi(x) - \Phi(y) - \langle \nabla\Phi(y),\, x - y\rangle,
$$
which, via the Legendre transform $\Phi^*(\xi) = \sup_x\{\langle \xi, x\rangle - \Phi(x)\}$ and the dual coordinates $\xi = \nabla\Phi(x)$, is representable symmetrically through $\Phi$ and $\Phi^*$. This is the canonical divergence of the dually flat space with potentials $(\Phi, \Phi^*)$, and the $\Phi \to \Phi^*$ swap is what Zhang names *representational* duality, logically independent of the $\alpha \to -\alpha$ *referential* duality. When the points are probability densities and $\Phi$ is chosen as the appropriate (negative) entropy potential, the family reproduces Amari's $\alpha$-divergence and, at the endpoints, KL.

## Key results

The paper establishes, as theorems rather than empirical claims, that the $\alpha$-divergence family $D^{(\alpha)}_\Phi$ is a genuine divergence for every $\alpha$ (nonnegative, zero only on the diagonal) whenever $\Phi$ is strictly convex; that the induced metric is $\alpha$-independent and equals the Hessian of $\Phi$; that the family carries a pair of dual $\alpha$-connections which are in general nonflat and become flat exactly at $\alpha = \pm 1$; and that at those endpoints the divergence reduces to the Bregman / canonical divergence of a dually flat manifold, representable through $\Phi$ and $\Phi^*$. The structural payoff is the clean separation of referential duality ($\alpha \to -\alpha$, argument swap) from representational duality ($\Phi \to \Phi^*$, Legendre conjugation), and the observation that for divergences between probability densities the resulting connections are "bidual," embodying both symmetries at once. Because the results are analytic identities derived from convexity and the Legendre transform, the evidence is mathematical proof; the paper contains no numerical benchmarks, and its strength lies in the generality and exactness of the correspondence rather than in any measured quantity.

## Relevance to this research

This paper is the convex-analytic foundation that licenses the VFE program to treat its Rényi / $\alpha$-divergence loss terms and its Kullback-Leibler terms as members of *one* family living in *one* dually flat geometry rather than as ad hoc alternatives. Zhang's central result — that a single convex potential $\Phi$ generates an $\alpha$-parameterized divergence family carrying one common Fisher-type metric ($\partial_i\partial_j\Phi$) plus a dual pair of $\alpha$-connections, with the Bregman/canonical KL divergence recovered exactly at $\alpha = \pm 1$ — is the precise statement of why the free-energy functional's $\mathrm{KL}(q_i \| p_i)$ self-coupling and any $\alpha$- or Rényi-generalized divergence terms share a metric structure and differ only by their connection (the flat KL endpoints versus curved interior $\alpha$). For the Gaussian belief tuples $(\mu, \Sigma)$ this means the program's divergences are all read off the same exponential-family potential, so switching the divergence registry's $\alpha$ is a controlled move along Zhang's family rather than a change of geometry; see [[Information geometry and natural gradient]], [[Alpha-divergence]], [[Renyi divergence]], and [[Fisher information metric]]. The referential/representational duality distinction further clarifies that the natural-gradient preconditioning (which uses the $\alpha$-independent metric) is invariant across the family even where the connection-dependent transport is not.

## Cross-links

- Concepts / Themes: [[Information geometry and natural gradient]], [[Alpha-divergence]], [[Renyi divergence]], [[Fisher information metric]]
- Related sources: [[amari-2000-methods-information-geometry]], [[nielsen-2020-elementary-introduction-information-geometry]], [[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]], [[amari-1998-natural-gradient]]

## BibTeX

```bibtex
@article{zhang2004divergence,
  author  = {Zhang, Jun},
  title   = {Divergence Function, Duality, and Convex Analysis},
  journal = {Neural Computation},
  volume  = {16},
  number  = {1},
  pages   = {159--195},
  year    = {2004},
  publisher = {MIT Press},
  doi     = {10.1162/08997660460734047}
}
```
