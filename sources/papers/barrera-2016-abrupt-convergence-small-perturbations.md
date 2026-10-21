---
type: paper
title: "Abrupt convergence for stochastic small perturbations of one dimensional dynamical systems"
aliases:
  - "Barrera and Jara 2016"
  - "One-dimensional small-noise cutoff"
authors:
  - Barrera G.
  - Jara M.
year: 2016
arxiv: "1511.00003"
doi: "10.1007/s10955-016-1468-1"
url: "https://arxiv.org/abs/1511.00003"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
  - field/physics
created: 2026-09-28
updated: 2026-09-28
---

# Abrupt convergence for stochastic small perturbations of one dimensional dynamical systems

> [!info] Citation
> G. Barrera and M. Jara (2016). "Abrupt convergence for stochastic small perturbations of one dimensional dynamical systems." *Journal of Statistical Physics* **163**(1), 113–138. doi:10.1007/s10955-016-1468-1. arXiv:1511.00003.

## Verification record

Metadata verified on 2026-09-28 against the arXiv abstract page and the Crossref record; full text read from arXiv. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED). The verifier noted one nuance adopted here: Section 5 is presented as an argument built on Theorem 2.1, not as a numbered theorem.

## Verified content

Definitions 1.1, 1.2 and 1.3 introduce cut-off, window cut-off and profile cut-off. Theorem 2.1 treats $dx=-V'(x)\,dt+\sqrt\epsilon\,dW$ in one dimension, with $V\in C^3$, $V'(x)=0$ only at $x=0$, $V''\ge\delta>0$, and $x_0\neq0$. It proves profile cut-off in total variation with profile $G(b)=\|\mathcal N(ce^{-b},1)-\mathcal N(0,1)\|_{\mathrm{TV}}$, cut-off time

$$t_\epsilon=\frac{1}{2V''(0)}\Big[\ln\frac1\epsilon+\ln\big(2V''(0)\big)\Big],$$

and window $w_\epsilon=1/V''(0)+\epsilon^\beta$. Theorem 3.2 is the linearized case; its remark with $V(x)=\lambda x^2/2$ shows that the Ornstein–Uhlenbeck process has profile cut-off. Section 5 treats a double-well potential: the local distance $\|x_t-\mathcal N(0,\epsilon/(2V''(x^*)))\|_{\mathrm{TV}}$ has a local cut-off at $\frac{1}{2V''(x^*)}\ln\frac1\epsilon$, and Remark 5.1 extends this to multi-well potentials. The introduction recalls, citing [[freidlin-2012-random-perturbations-dynamical-systems]], that mean exit times from a well are exponentially large in the inverse noise and that normalized exit times are exponentially distributed and memoryless.

## Cross-links

- Concepts: [[Meta-agents and hierarchical emergence]], [[Geometric singular perturbation theory]]
- Related sources: [[barrera-2020-thermalisation-small-random-perturbations]], [[freidlin-2012-random-perturbations-dynamical-systems]], [[bovier-2015-metastability-potential-theoretic-approach]], [[bovier-2004-metastability-diffusions]]

## BibTeX

```bibtex
@article{barrera2016abrupt,
  author        = {Barrera, G. and Jara, M.},
  title         = {Abrupt convergence for stochastic small perturbations of one dimensional dynamical systems},
  journal       = {Journal of Statistical Physics},
  volume        = {163},
  number        = {1},
  pages         = {113--138},
  year          = {2016},
  doi           = {10.1007/s10955-016-1468-1},
  eprint        = {1511.00003},
  archivePrefix = {arXiv}
}
```
