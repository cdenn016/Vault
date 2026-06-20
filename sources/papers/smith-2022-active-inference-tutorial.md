---
type: paper
title: A step-by-step tutorial on active inference and its application to empirical data
aliases:
  - "Smith, Friston, Whyte 2022"
  - "Active Inference Tutorial"
authors:
  - Ryan Smith
  - Karl J. Friston
  - Christopher J. Whyte
year: 2022
arxiv: null
url: https://doi.org/10.1016/j.jmp.2021.102632
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/psychology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A step-by-step tutorial on active inference and its application to empirical data

> [!info] Citation
> Smith, R., Friston, K. J., & Whyte, C. J. (2022). A step-by-step tutorial on active inference and its application to empirical data. Journal of Mathematical Psychology, 107, 102632. DOI 10.1016/j.jmp.2021.102632.

## TL;DR

This is the standard operational primer on discrete-state active inference: it teaches a reader with minimal programming and mathematics background how to build a partially observable Markov decision process (POMDP) generative model, solve it by minimizing variational and expected free energy, simulate the resulting behaviour and neuronal responses, and fit the model to empirical choice data. Where most active-inference papers state the update equations and move on, this tutorial walks through every term explicitly, names each component of the generative model ($\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$, $\mathbf{E}$), and supplies runnable MATLAB scripts built on the SPM/`spm_MDP_VB` routines that a reader can customize. Its lasting value to anyone outside the field is that it gives the equation-level, worked-example template for the discrete active-inference inference loop — the variational free energy for state inference, the expected free energy for policy selection, and the softmax that ties them together — at a level of detail one rarely finds in the primary Friston papers.

## Problem & setting

Active inference casts perception, learning, and action as a single problem of approximate Bayesian inference under a generative model, with all updates driven by the minimization of free energy. The framework is highly general but notoriously hard to enter: introductions presuppose fluency in variational calculus, message passing, and the SPM codebase, which has limited its adoption in experimental psychology and computational psychiatry. The paper's stated aim is pedagogical — to remove that barrier — and it is organized in three parts: a non-technical and then technical introduction to the underlying quantities (Bayes' theorem, surprisal, variational free energy, expected free energy); a formal account of POMDP structure and how it is solved; and a fully worked construction of a behavioral-task model with simulations and a recipe for fitting it to data. It builds directly on the discrete-time active-inference POMDP formulation of Friston and colleagues (Friston et al., 2016, 2017; Da Costa et al., 2020) and the accompanying neural process theory, and is best read as the operational companion to Parr, Pezzulo & Friston's *Active Inference* (MIT Press, 2022).

## Method

The generative model is a factorized joint over outcomes, hidden states, and policies, $p(o_{1:T}, s_{1:T}, \pi)$. Its components are the likelihood matrix $\mathbf{A}$ mapping hidden states to outcomes, $p(o_\tau \mid s_\tau)$; the transition matrices $\mathbf{B}(\pi)$ giving policy-conditioned state dynamics $p(s_\tau \mid s_{\tau-1}, \pi)$ and encoding the Markov property; the preference vector $\mathbf{C}$ defining $p(o \mid C)$ over preferred outcomes; the prior $\mathbf{D}$ over initial states $p(s_1)$; and the prior $\mathbf{E}$ over policies (the "habit"). State inference proceeds by positing an approximate posterior $q(s)$ and minimizing the **variational free energy** (VFE), written in the tutorial as the expected log-ratio between model and approximate posterior,
$$ F = \mathbb{E}_{q(s,\pi)}\!\left[\ln q(s,\pi) - \ln p(o, s, \pi)\right], $$
which is an upper bound on surprisal $-\ln p(o)$; minimizing $F$ therefore drives $q(s)$ toward the true posterior $p(s\mid o)$ while maximizing a bound on model evidence. The mean-field factorization assumed for the approximate posterior treats hidden states, policies, and (Dirichlet) parameters as independent factors, and per-policy state estimates are obtained by gradient descent on $F$, realized as a marginal-message-passing update over the factor graph. Action is selected by minimizing **expected free energy** (EFE), evaluated over outcomes that have not yet occurred and therefore treated as random variables. The tutorial gives the now-standard decomposition into risk and ambiguity,
$$ G(\pi) = \underbrace{D_{\mathrm{KL}}\!\left[q(o\mid\pi)\,\|\,p(o\mid C)\right]}_{\text{risk}} + \underbrace{\mathbb{E}_{q(s\mid\pi)}\!\left[H[p(o\mid s)]\right]}_{\text{ambiguity}}, $$
equivalently a split into pragmatic (reward-seeking) and epistemic (information-seeking) value, which is what gives active inference its built-in resolution of the explore–exploit dilemma. The posterior over policies is then a softmax of the relevant scores: before observation $\pi_0 = \sigma(\ln \mathbf{E} - \gamma G)$ and after observation $\pi = \sigma(\ln \mathbf{E} - F - \gamma G)$, with $\gamma$ an expected-free-energy precision that is itself updated from a (Gamma/Dirichlet-hyperparameter) prior. Parameter learning (e.g. of $\mathbf{A}$) is handled by Dirichlet conjugate updates, supplying the slow M-step that complements the fast E-step over states and policies.

## Key results

This is a tutorial, not an empirical study, so its "results" are demonstrations rather than theorems or benchmark numbers. It establishes a complete, reproducible pipeline: a worked generative model of an explore–exploit task — a two-armed-bandit variant in which an agent can guess for a large reward or pay an information cost to request a hint for a smaller but more certain reward — together with simulations showing how varying preference precision and policy precision shifts the agent between information-seeking and reward-seeking behaviour. It then shows how to invert the same model on empirical choice data, fitting subject-specific parameters by maximizing model evidence (variational Bayes / Bayesian model comparison over participants), which is the route by which active inference enters computational psychiatry. The strength of the evidence is pedagogical and constructive: every equation is derived and tied to a line of MATLAB, and the appendices give the full derivation of the EFE decompositions and the message-passing updates. No quantitative benchmark or model-comparison statistic is claimed as a headline finding, and none should be attributed to this paper.

## Relevance to this research

This is the standard operational reference for the discrete (POMDP) active-inference generative model, and it gives the equation-level E-step/M-step template that the gauge-theoretic VFE transformer's inference loop can be benchmarked against. Its explicit variational free energy (for state inference) and expected free energy (for policy selection), together with the worked mean-field factorization over hidden states, policies, and Dirichlet parameters, are the canonical discrete analogue of the program's iterative belief updates over Gaussian tuples $(\mu, \Sigma, \phi)$: the tutorial's fast gradient descent on $F$ over $q(s)$ is the E-step, and its slow Dirichlet conjugate updates of $\mathbf{A}$/$\mathbf{B}$ are the M-step, so it is the cleanest external check on whether the transformer's filtering loop respects the standard EM blindness separation. The risk-plus-ambiguity (epistemic + pragmatic) decomposition of EFE is also the reference form the program's attention-entropy and meta-entropy couplings should be read against — the softmax over policies $\sigma(\ln\mathbf{E} - F - \gamma G)$ is structurally the discrete cousin of the softmax-$\beta$ attention weights that fall out of the free-energy functional. See [[Inference machinery — variational EM and filtering]] and [[Variational free energy and predictive coding]] for where this template plugs into the program.

## Cross-links

- Concepts / Themes: [[Inference machinery — variational EM and filtering]], [[Variational free energy and predictive coding]]

## BibTeX

```bibtex
@article{smith2022activeinf,
  author  = {Smith, Ryan and Friston, Karl J. and Whyte, Christopher J.},
  title   = {A step-by-step tutorial on active inference and its application to empirical data},
  journal = {Journal of Mathematical Psychology},
  volume  = {107},
  pages   = {102632},
  year    = {2022},
  doi     = {10.1016/j.jmp.2021.102632},
  url     = {https://doi.org/10.1016/j.jmp.2021.102632}
}
```
