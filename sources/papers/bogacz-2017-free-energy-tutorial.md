---
type: paper
title: "A tutorial on the free-energy framework for modelling perception and learning"
aliases:
  - "Bogacz 2017"
  - "Bogacz 2017 — Free-Energy Tutorial"
authors:
  - Bogacz, Rafal
year: 2017
arxiv: null
url: https://doi.org/10.1016/j.jmp.2015.11.003
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/statistics
status: stable
created: 2026-06-18
updated: 2026-06-20
---

# A tutorial on the free-energy framework for modelling perception and learning

> [!info] Citation
> Bogacz, Rafal (2017). "A tutorial on the free-energy framework for modelling perception and learning." *Journal of Mathematical Psychology*, 76(B), 198–211. https://doi.org/10.1016/j.jmp.2015.11.003

## TL;DR

A pedagogical, fully worked derivation of the [[Variational free energy]] objective for Gaussian generative models, showing how minimizing free energy yields simple, biologically plausible update equations in which inference and learning are both gradient descent on the same scalar. The tutorial makes explicit the role of [[Precision weighting]] in scaling [[Prediction error]] and gives the closed-form E-step (belief updates) and M-step (parameter/precision updates) that the architecture's filtering-mode gradient dynamics directly mirror.

## Problem & setting

The paper starts from a minimal perception problem: an organism observes a noisy sensory value `u` and must infer a hidden cause `v` under a Gaussian generative model `p(v)` (prior, mean `v_p`, variance `Σ_p`) and `p(u|v)` (likelihood, mean `g(v)`, variance `Σ_u`). Exact Bayesian inversion of `p(v|u)` is generally intractable once the likelihood mean `g(v)` is nonlinear, so the tutorial introduces the variational approximation: replace the true posterior with a tractable approximate belief `q(v)` and minimize the [[Variational free energy]] `F`, an upper bound on negative log-evidence that equals negative log-evidence plus the KL divergence from `q` to the true posterior. Minimizing `F` therefore simultaneously sharpens the belief and (as a by-product) maximizes a bound on the marginal likelihood — the [[Evidence lower bound (ELBO)]] viewed from the energy side.

The pedagogical arc proceeds in stages: first a point estimate (Laplace/MAP) version where `q` is a delta at its mode `φ`, then a Gaussian `q` with its own variance, then learning of the generative parameters, and finally a circuit interpretation in which each quantity maps to the activity of a dedicated neuron or error unit.

## Method

The core object is the (Laplace-approximated) free energy for a single hidden variable, which after dropping constants reduces to a sum of squared, precision-weighted prediction errors:

`F = (1/2)[ ε_p² / Σ_p + ε_u² / Σ_u ] + (1/2) ln(Σ_p Σ_u)`,

with prior error `ε_p = φ − v_p` and sensory error `ε_u = u − g(φ)`. Two coupled dynamics follow by gradient descent / ascent on this single scalar:

- **E-step (inference / belief update).** The estimate `φ` relaxes by `φ̇ = −∂F/∂φ = ε_u g'(φ)/Σ_u − ε_p/Σ_p`. Defining precision-weighted prediction-error units `ξ_p = ε_p/Σ_p` and `ξ_u = ε_u/Σ_u`, the update becomes `φ̇ = g'(φ) ξ_u − ξ_p`: the belief moves to reduce top-down and bottom-up prediction error, each weighted by its inverse variance (precision). This is the filtering-style fixed-point relaxation: beliefs are updated online by integrating prediction-error currents rather than by a closed-form posterior solve.

- **M-step (learning).** Holding the relaxed beliefs fixed, the generative parameters descend the same `F`. Weights in `g(v)` update by a Hebbian rule proportional to the product of a presynaptic estimate and the postsynaptic precision-weighted error. The variances/precisions update by `Σ̇ ∝ (ε²/Σ² − 1/Σ)`, which drives each precision toward the inverse of the running mean-squared error — an explicit, local rule for learning the metric that scales every error term.

The tutorial then shows the error units themselves can be given relaxation dynamics, `ξ̇ = ε − Σ ξ`, so that the precision division is computed by a recurrent circuit rather than an explicit reciprocal. The whole scheme is presented as alternating coordinate descent — the [[Variational EM]] structure — on one free-energy functional, and it is shown to recover the predictive-coding network of [[rao-1999-predictive-coding]] as a special case.

## Key results

A single scalar (free energy) governs both perception and learning; no separate objectives are needed. All updates are local: each depends only on quantities available at the corresponding unit, making the scheme a candidate for neural implementation and a clean template for layerwise message passing. Precision appears everywhere as the gain on prediction error; learning precision is learning how much to trust each error channel. The Gaussian-belief, precision-weighted-error formulation connects directly to Friston's [[friston-2010-free-energy-principle|free-energy principle]] and to [[Variational EM]] (cf. [[neal-1998-variational-em]]), and reproduces classical [[rao-1999-predictive-coding|predictive coding]].

## Relevance to this research

This tutorial is the closest textbook analogue of the VFE-transformer's inner loop. The architecture maintains per-token Gaussian beliefs `(mu, Sigma)` from the `gaussian_diagonal` family and trains on a free-energy / ELBO objective with `gradient_mode = "filtering"` — exactly the online belief-relaxation E-step Bogacz derives (`φ̇ = g'(φ) ξ_u − ξ_p`) rather than a closed-form posterior solve. The explicit precision-weighted error units `ξ = ε/Σ` are the mathematical content of the model's `precision_weighted_attention`: attention logits are prediction errors scaled by belief precision, just as Bogacz scales each error by inverse variance. The M-step precision rule `Σ̇ ∝ (ε²/Σ² − 1/Σ)` is the elementary, diagonal counterpart of the model's M-step that updates `Sigma`; on the full architecture this lives on the SPD manifold, but the diagonal case here gives the ground-truth target the SPD machinery must reproduce. The `ln Σ` term in `F` is precisely the attention/belief-entropy contribution that regularizes precision away from collapse. In short, this paper supplies the explicit E-step/M-step update equations and precision terms that the filtering gradient mode mirrors, and grounds why the objective is a free energy rather than a plain likelihood.

> [!note] Editorial: Bogacz treats scalar/diagonal Gaussian beliefs with Euclidean gradient descent; the VFE-transformer generalizes the M-step on `Σ` to the SPD manifold and replaces the plain gradient with a natural/Riemannian one. These extensions are not in this paper — it is the flat, scalar baseline the geometry sits on top of.

## Cross-links

- Concepts: [[Variational free energy]], [[Evidence lower bound (ELBO)]], [[Prediction error]], [[Precision weighting]]
- Methods: [[Variational EM]], [[Predictive coding network]], [[Free-energy principle active inference]]
- Related sources: [[friston-2010-free-energy-principle]], [[rao-1999-predictive-coding]], [[neal-1998-variational-em]], [[millidge-2020-pc-approximates-backprop]], [[kingma-2013-auto-encoding-variational-bayes]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{bogacz2017tutorial,
  author  = {Bogacz, Rafal},
  title   = {A tutorial on the free-energy framework for modelling perception and learning},
  journal = {Journal of Mathematical Psychology},
  volume  = {76},
  number  = {B},
  pages   = {198--211},
  year    = {2017},
  doi     = {10.1016/j.jmp.2015.11.003},
  url     = {https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5341759/}
}
```
