---
type: reference
title: "Maximum Likelihood from Incomplete Data via the EM Algorithm"
aliases: ["Dempster 1977", "Dempster, Laird & Rubin 1977", "EM algorithm"]
authors: ["A. P. Dempster", "N. M. Laird", "D. B. Rubin"]
year: 1977
tags: [cluster/vfe, project/transformer, project/multi-agent, field/statistics]
created: 2026-06-18
updated: 2026-06-18
---

# Maximum Likelihood from Incomplete Data via the EM Algorithm

> [!info] Citation
> A. P. Dempster, N. M. Laird, and D. B. Rubin (1977). "Maximum Likelihood from Incomplete Data via the EM Algorithm (with Discussion)." *Journal of the Royal Statistical Society, Series B*, **39**(1), 1–38.

## TL;DR

Dempster, Laird, and Rubin unify a broad family of iterative maximum-likelihood procedures under a single schema, the **Expectation–Maximization (EM) algorithm**, for fitting models to *incomplete data* — data with missing values, latent variables, or otherwise unobserved structure. Each iteration alternates an E-step, which forms the expected complete-data log-likelihood given the observed data and the current parameter estimate, with an M-step, which maximizes that expectation; the paper proves that the observed-data likelihood is non-decreasing across iterations.

## What it establishes

The paper formalizes the notion of incomplete data through a many-to-one mapping from a complete-data sample space to the observed sample space, so that the observed likelihood is an integral (or sum) of a complete-data likelihood over the unobserved configurations. Within this framework it defines the two-step iteration:

- **E-step:** compute $Q(\theta \mid \theta^{(t)}) = \mathbb{E}\!\left[\log p(x \mid \theta) \,\middle|\, y, \theta^{(t)}\right]$, the conditional expectation of the complete-data log-likelihood given the observed data $y$ and the current estimate $\theta^{(t)}$.
- **M-step:** set $\theta^{(t+1)} = \arg\max_\theta Q(\theta \mid \theta^{(t)})$.

Its central theoretical result is a **monotonicity guarantee**: each EM iteration does not decrease the observed-data likelihood, $L(\theta^{(t+1)}) \ge L(\theta^{(t)})$. The authors show this is a consequence of Jensen's inequality applied to the gap between the complete- and observed-data likelihoods, and they characterize the fixed points and convergence behavior of the iteration. The paper subsumes many previously separate methods (Baum–Welch for hidden Markov models, Gaussian-mixture fitting, factor analysis, variance-component estimation) as instances of the same algorithm, giving them a common derivation and convergence argument.

## Why the project cites it

EM is the algorithmic ancestor of the variational machinery the project builds on. The modern reading recasts the E- and M-steps as alternating maximization of a single functional — the negative [[Variational free energy]] (equivalently, the [[Evidence lower bound (ELBO)]]) — with respect to an approximate posterior and the parameters, respectively. This *free-energy view of EM* is exactly the bridge the project leans on:

- **Variational EM as inference machinery.** The project's inference scaffolding uses [[Variational EM]] and, more generally, [[Free-energy principle active inference]]: the E-step is belief updating (inference over latent states), the M-step is parameter/learning. Recognizing both as ascent on one free-energy functional is what licenses treating perception and learning as a single optimization, and connects the discrete EM iteration to the continuous-time belief dynamics the project studies.
- **Bound-based inference.** When the exact E-step posterior is intractable, EM generalizes to variational EM, where the E-step optimizes an approximate posterior against the [[Evidence lower bound (ELBO)]]. This is the same bound underlying the [[Variational autoencoder (VAE)]] and [[Amortized inference]] / [[Iterative amortized inference]] used elsewhere in the program.
- **Geometry of the updates.** Because EM ascends a likelihood/free-energy surface, its trajectory and convergence are naturally described in the [[Fisher information metric]], linking the classical algorithm to the [[Natural gradient]] and information-geometric structure the project uses to give beliefs inertia and mass (see [[Mass as Fisher information]]).

In short, the note anchors the project's variational and active-inference layer to its statistical origin: EM is where the alternation between inferring hidden state and updating parameters first received a clean derivation and a monotone-improvement proof, and the project's free-energy formulation is a direct geometric generalization of it.

> [!note] Editorial: The free-energy / ELBO reinterpretation of EM is later work (e.g. Neal & Hinton; see [[neal-1998-variational-em]]); the 1977 paper itself states the algorithm and proves likelihood monotonicity, and does not use free-energy language.

## BibTeX

```bibtex
@article{dempster1977em,
  author  = {Dempster, A. P. and Laird, N. M. and Rubin, D. B.},
  title   = {Maximum Likelihood from Incomplete Data via the {EM} Algorithm},
  journal = {Journal of the Royal Statistical Society, Series B},
  year    = {1977},
  volume  = {39},
  number  = {1},
  pages   = {1--38},
  doi     = {10.1111/j.2517-6161.1977.tb01600.x},
  note    = {With discussion}
}
```
