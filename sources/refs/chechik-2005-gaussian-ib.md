---
type: reference
title: "Information Bottleneck for Gaussian Variables"
aliases:
  - "Chechik et al. 2005"
  - "Gaussian Information Bottleneck"
authors:
  - Gal Chechik
  - Amir Globerson
  - Naftali Tishby
  - Yair Weiss
year: 2005
url: https://www.jmlr.org/papers/v6/chechik05a.html
tags:
  - cluster/info-geometry
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# Information Bottleneck for Gaussian Variables

> [!info] Citation
> Gal Chechik, Amir Globerson, Naftali Tishby, and Yair Weiss (2005). "Information Bottleneck for Gaussian Variables." *Journal of Machine Learning Research* 6: 165–188. <https://www.jmlr.org/papers/v6/chechik05a.html>

## TL;DR

This paper solves the [[Information bottleneck]] **in closed form** for jointly Gaussian variables. When $X$ and $Y$ are Gaussian, the optimal bottleneck representation $T$ is itself a noisy linear projection of $X$, and the optimal projection directions are **eigenvectors of the normalized regression matrix** $\Sigma_{x\mid y}\Sigma_x^{-1}$. As the trade-off parameter $\beta$ increases, eigen-directions switch on one at a time at critical values, so the Gaussian IB undergoes a sequence of structural phase transitions — a clean, analytic instance of compression-versus-relevance.

## What it establishes

- The Gaussian IB optimum is a noisy linear map; no need to search over general stochastic encoders.
- Optimal directions are eigenvectors of $\Sigma_{x\mid y}\Sigma_x^{-1}$, activated in order of relevance as $\beta$ grows (a spectral, phase-transition structure).
- A fully tractable model in which the abstract IB trade-off curve and its information plane can be computed exactly.

## Why the project cites it

Of the entire IB family this is the closest to PIFB ([[participatory-it-from-bit]]), because PIFB's representations are **Gaussian belief tuples** $(\mu, \Sigma, \phi)$ — exactly the regime Chechik et al. solve. Their result says that for Gaussian sources the optimal relevance-preserving compression is a covariance-eigenstructure operation, which is congenial to the project's treatment of belief covariances $\Sigma$ on the SPD manifold with affine-invariant geometry (see [[pennec-2006-affine-invariant-tensor]]). The closed-form Gaussian IB gives a tractable benchmark for the capacity-floor and complexity-versus-accuracy claims of the manuscript: PIFB's [[Variational free energy]] trade-off between the self-coupling KL and the observation likelihood should, restricted to Gaussian beliefs, reduce to a Gaussian-IB-like spectral problem in $\Sigma$. This anchors the [[Information bottleneck]] reading of PIFB in the one case where the trade-off is exactly solvable and matches the project's representation class, and links to the general IB principle ([[tishby-1999-information-bottleneck]]).

```bibtex
@article{chechik2005information,
  title   = {Information Bottleneck for Gaussian Variables},
  author  = {Chechik, Gal and Globerson, Amir and Tishby, Naftali and Weiss, Yair},
  journal = {Journal of Machine Learning Research},
  volume  = {6},
  pages   = {165--188},
  year    = {2005},
  url     = {https://www.jmlr.org/papers/v6/chechik05a.html}
}
```
