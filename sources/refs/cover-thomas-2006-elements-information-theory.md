---
type: reference
title: "Elements of Information Theory (2nd ed.)"
aliases:
  - "Cover & Thomas 2006 — Elements of Information Theory"
  - "Cover-Thomas"
  - "cover2006elements"
  - "Cover and Thomas 2006"
  - "Elements of Information Theory"
authors:
  - "Cover T. M."
  - "Thomas J. A."
year: 2006
url: https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/statistics
  - field/cs-ml
created: 2026-06-20
updated: 2026-06-20
---

# Elements of Information Theory (2nd ed.)

> [!info] Citation
> Cover, T. M. and Thomas, J. A. (2006). *Elements of Information Theory*, 2nd edition. Wiley-Interscience, Hoboken, NJ. ISBN 978-0-471-24195-9. DOI: 10.1002/047174882X.

## TL;DR

The standard graduate textbook on Shannon information theory. It builds the core functionals — entropy $H$, relative entropy (Kullback-Leibler divergence) $D$, and mutual information $I$ — and develops their operational meaning through the source-coding, channel-coding, and rate-distortion theorems. For this project it is the canonical reference for the information-theoretic quantities that appear inside the variational free-energy functional: the KL/relative-entropy couplings and the attention-distribution entropy.

## What it establishes

The book defines the entropy of a discrete random variable and the relative entropy between two distributions,

$$ H(X) = -\sum_x p(x)\log p(x), \qquad D(p\,\|\,q) = \sum_x p(x)\log\frac{p(x)}{q(x)}, $$

and the mutual information $I(X;Y) = D\big(p(x,y)\,\|\,p(x)p(y)\big) = H(X) - H(X\mid Y)$, then derives their structural properties and operational theorems.

- **Relative entropy as the master quantity.** $D(p\,\|\,q) \ge 0$ with equality iff $p=q$ (Gibbs' inequality / information inequality), and $D$ is jointly convex in $(p,q)$. Mutual information, channel capacity, and the rate-distortion function are all expressed through $D$, making relative entropy the organizing object the project's KL couplings inherit.
- **Chain rules and the data-processing inequality.** Entropy and mutual information factor through chain rules; the data-processing inequality $I(X;Y)\ge I(X;Z)$ for a Markov chain $X\to Y\to Z$ bounds how much information survives post-processing — the bound that underlies the [[Information bottleneck]] trade-off.
- **Operational coding theorems.** The asymptotic equipartition property, the source-coding theorem ($H$ as the compression limit), the channel-coding theorem ($I$ as capacity), and rate-distortion theory give each functional an operational meaning rather than a purely formal one.
- **The link to maximum likelihood and statistics.** The text develops relative entropy as the exponent in large-deviation / hypothesis-testing rates (Stein's lemma, Sanov's theorem) and connects $D$ to maximum-likelihood estimation, the bridge from Shannon information to the statistical-manifold view of the [[Fisher information metric]] (the local quadratic form of $D$). It also presents the Rényi entropies/divergences as the one-parameter generalization of $H$ and $D$, the discrete counterpart of the [[Renyi divergence]] and [[Alpha-divergence]] families used elsewhere in the program.

> [!note] Editorial: This note summarizes the scope of the standard second edition (Wiley-Interscience, 2006); specific theorem or page numbers are not reproduced here. The local-quadratic relation $D(p\,\|\,p+d\theta)\approx \tfrac12 d\theta^\top g\, d\theta$ between relative entropy and the Fisher metric is standard information geometry (see [[amari-2016-information-geometry-applications]]) rather than a headline result of this text.

## Why the project cites it

This reference supplies the information-theoretic vocabulary in which the project's free-energy objective is written, and the inequalities that justify treating its terms as well-posed costs.

- **KL/relative entropy as the coupling cost.** Every coupling in the free-energy functional — the self-coupling $\alpha\,\mathrm{KL}(q_i\,\|\,p_i)$ of beliefs to priors, the hyper-prior term $\lambda_h\,\mathrm{KL}(s_i\,\|\,h)$, and the belief/model couplings $\beta_{ij}\,\mathrm{KL}(q_i\,\|\,\Omega_{ij}q_j)$ — is a relative entropy in exactly Cover & Thomas's sense. Non-negativity and convexity of $D$ (Gibbs' inequality) are what make these terms genuine costs minimized at agreement, central to the [[Variational free energy]] construction and the [[Information geometry and natural gradient]] theme.
- **Attention entropy.** The $\tau\,\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ term that makes softmax attention a stationary point of $F$ is the entropy of the attention distribution relative to a uniform prior — the discrete relative entropy this text defines. The temperature $\tau = \kappa\sqrt{\dim_h}$ scales that entropic regularizer.
- **Information bottleneck.** The project's rate-distortion / compression intuitions for what attention and the belief hierarchy retain are framed through mutual information and the data-processing inequality developed here; see [[tishby-1999-information-bottleneck]] and the Gaussian case in [[chechik-2005-gaussian-ib]].
- **Bridge to information geometry.** Relative entropy is the global object whose local second-order form is the [[Fisher information metric]]; this text is the information-theoretic half of the foundation that [[amari-2016-information-geometry-applications]] and [[cencov-1982-statistical-decision-rules]] complete on the geometric side, grounding the natural-gradient M-step.

## Cross-links

Concepts and theme: [[Fisher information metric]], [[Information bottleneck]], [[Renyi divergence]], [[Information geometry and natural gradient]].
Projects: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]].
Related sources: [[amari-2016-information-geometry-applications]], [[cencov-1982-statistical-decision-rules]], [[tishby-1999-information-bottleneck]], [[chechik-2005-gaussian-ib]].

## BibTeX

```bibtex
@book{cover2006elements,
  title     = {Elements of Information Theory},
  author    = {Cover, Thomas M. and Thomas, Joy A.},
  year      = {2006},
  edition   = {2nd},
  publisher = {Wiley-Interscience},
  address   = {Hoboken, NJ},
  isbn      = {978-0-471-24195-9},
  doi       = {10.1002/047174882X}
}
```
