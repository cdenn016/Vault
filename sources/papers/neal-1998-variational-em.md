---
type: paper
title: A View of the EM Algorithm that Justifies Incremental, Sparse, and Other Variants
aliases:
  - Neal & Hinton 1998 — Variational EM
  - "neal-hinton-1998-em-variational"
authors:
  - Radford M. Neal
  - Geoffrey E. Hinton
year: 1998
arxiv: ""
url: https://link.springer.com/chapter/10.1007/978-94-011-5014-9_12
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-18
updated: 2026-06-18
---

# A View of the EM Algorithm that Justifies Incremental, Sparse, and Other Variants

> [!info] Citation
> Radford M. Neal & Geoffrey E. Hinton (1998). *A View of the EM Algorithm that Justifies Incremental, Sparse, and Other Variants.* In M. I. Jordan (ed.), *Learning in Graphical Models*, pp. 355–368. Kluwer/Springer. [Publisher link](https://link.springer.com/chapter/10.1007/978-94-011-5014-9_12).

## TL;DR

Neal and Hinton recast the classical Expectation–Maximization (EM) algorithm as the joint optimization of a single objective: a function that equals the **negative variational free energy** of the model. They show that EM does not merely "increase the likelihood" but rather performs coordinate ascent on this free-energy functional, alternating between a distribution `q` over the unobserved variables (the E-step) and the model parameters `θ` (the M-step). Because both steps optimize the *same* quantity, one is free to take *partial* or *incremental* steps — updating only some latent variables, or only approximating the optimal `q` — and still guarantee monotone improvement. This justifies online/incremental EM, sparse EM, and a broad family of approximate variants.

## Problem & setting

Standard EM maximizes the log marginal likelihood `log p(x | θ)` of observed data `x` under a model with latent variables `z`, by iterating an E-step (compute the posterior `p(z | x, θ)`) and an M-step (re-estimate `θ` given expected sufficient statistics). The classical justification is indirect: each full iteration provably does not decrease the likelihood, but the argument treats the two steps as distinct operations and offers no principled license for *approximate* E-steps. Neal and Hinton ask: is there a single function that both steps optimize, so that partial progress on either step is provably safe?

## Method

The paper introduces the functional (in their notation, a quantity `F`) over a freely chosen distribution `q(z)` and parameters `θ`:

```
F(q, θ) = E_q[ log p(x, z | θ) ] + H[q]
        = log p(x | θ) − KL( q(z) || p(z | x, θ) ).
```

The first line writes `F` as the expected complete-data log-likelihood plus the entropy of `q`; this is exactly the **evidence lower bound** (ELBO), i.e. the negative variational free energy. The second line is the key decomposition: `F` equals the true log-likelihood minus the Kullback–Leibler divergence from `q` to the exact posterior. Two consequences follow immediately:

- **E-step = maximize `F` over `q`.** Since `log p(x | θ)` does not depend on `q`, maximizing `F` over `q` minimizes the KL term, which is zero exactly when `q(z) = p(z | x, θ)`. So the optimal E-step recovers the true posterior, and `F` then equals the log-likelihood — the bound is tight.
- **M-step = maximize `F` over `θ`.** Holding `q` fixed, only the expected complete-data log-likelihood depends on `θ`, recovering the ordinary M-step.

Because both steps ascend the *same* `F`, the authors observe that neither step needs to be carried to its optimum. A **partial E-step** that merely increases `F` (e.g. updating `q` for a single data point, or settling on a tractable approximate `q`) still yields monotone improvement. From this they derive: an **incremental EM** that recomputes `q` for one latent variable per E-step (empirically faster convergence on a Gaussian-mixture problem); a **sparse EM** that, when a latent can take many values but few carry non-negligible probability, freezes the small-probability components and updates only the plausible set; and a wider family of approximate and "winner-take-all" variants, all unified as coordinate ascent on free energy.

## Key results

- A single negative-free-energy / ELBO functional `F(q, θ)` whose two coordinate-ascent steps **are** the E-step and M-step of EM; full EM is the special case where the E-step is exact.
- A rigorous license for **approximate and partial E-steps**: any update that does not decrease `F` preserves the convergence guarantee, which is the foundation later used by variational EM and predictive-coding inference.
- Concrete incremental and sparse variants, with empirical evidence that incremental updates converge faster than batch EM on mixture estimation.

## Relevance to this research

This paper is the formal backbone of the VFE transformer's **two-timescale optimization** and is the reason its training loop is coherent rather than ad hoc.

- **E-step / M-step decomposition.** The transformer maintains per-token Gaussian beliefs `(mu, Sigma)` (the `q` distribution, family `gaussian_diagonal`) and a set of network parameters. Its **E-step** updates the beliefs and its **M-step** updates the parameters — exactly the two coordinate-ascent moves on `F` that Neal and Hinton identify. The model's ELBO / free-energy training objective *is* their `F`, so belief updates and parameter updates are guaranteed to push on the same quantity. See [[Variational EM]] and [[Evidence lower bound (ELBO)]].
- **Filtering / incremental updates.** The config's `gradient_mode "filtering"` and the per-token, causal processing of a transformer mean beliefs are refined incrementally rather than via a single global posterior solve. This paper's central contribution — that **partial E-steps still increase `F`** — is precisely what makes such incremental/filtering belief updates theoretically sound. See [[Inference machinery — variational EM and filtering]].
- **KL as the tightness gap.** Their `F = log p(x|θ) − KL(q || posterior)` identity is the entry point for the model's information-geometry machinery: the VFE transformer generalizes this gap to [[Renyi divergence|Renyi]] / [[Alpha-divergence|alpha]] divergences (`divergence_family "renyi"`, with KL as the `alpha → 1` limit), so the belief-fitting step minimizes a tunable divergence rather than only KL.
- **Amortization and free energy.** The decomposition underlies modern [[Variational free energy]] and [[Amortized inference]]: where Neal and Hinton optimize `q` directly, later work (and this transformer) *amortize* the E-step with a learned network, while inheriting the same guarantee that improving `F` improves the model.

> [!note] Editorial: The VFE transformer departs from the 1998 setting by replacing the exact-posterior E-step with a structured Gaussian belief and a Renyi/alpha divergence rather than KL; Neal & Hinton's monotonicity guarantee holds strictly only for KL with an exact-or-improving E-step, so the transformer's variant is a principled relaxation, not a literal instance.

## Cross-links

- Methods: [[Variational EM]], [[Iterative amortized inference]], [[Predictive coding network]], [[Free-energy principle active inference]]
- Concepts: [[Variational free energy]], [[Evidence lower bound (ELBO)]], [[Amortized inference]], [[Prediction error]], [[Precision weighting]]
- Divergences / geometry: [[Renyi divergence]], [[Alpha-divergence]]
- Themes: [[Variational free energy and predictive coding]], [[Inference machinery — variational EM and filtering]]
- Related sources: [[friston-2010-free-energy-principle]], [[bogacz-2017-free-energy-tutorial]], [[kingma-2013-auto-encoding-variational-bayes]], [[marino-2018-iterative-amortized-inference]], [[rao-1999-predictive-coding]], [[li-turner-2016-renyi-vi]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@incollection{neal1998view,
  author    = {Neal, Radford M. and Hinton, Geoffrey E.},
  title     = {A View of the {EM} Algorithm that Justifies Incremental, Sparse, and Other Variants},
  booktitle = {Learning in Graphical Models},
  editor    = {Jordan, Michael I.},
  series    = {NATO ASI Series},
  publisher = {Kluwer Academic Publishers},
  address   = {Dordrecht},
  pages     = {355--368},
  year      = {1998},
  doi       = {10.1007/978-94-011-5014-9_12},
  url       = {https://link.springer.com/chapter/10.1007/978-94-011-5014-9_12}
}
```
