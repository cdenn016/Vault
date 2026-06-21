---
type: paper
title: "Information Bottleneck for Gaussian Variables"
aliases:
  - Chechik 2005
  - Gaussian IB
  - GIB
  - chechik-2005-gaussian-ib
  - Chechik et al. 2005
  - Gaussian Information Bottleneck
authors:
  - Chechik, Gal
  - Globerson, Amir
  - Tishby, Naftali
  - Weiss, Yair
year: 2005
arxiv: null
url: https://jmlr.org/papers/v6/chechik05a.html
tags:
  - cluster/info-geometry
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Information Bottleneck for Gaussian Variables

> [!info] Citation
> Chechik, G., Globerson, A., Tishby, N., & Weiss, Y. (2005). "Information Bottleneck for Gaussian Variables." *Journal of Machine Learning Research*, 6, 165–188.

## TL;DR
This paper derives a closed-form analytic solution to the Information Bottleneck (IB) problem for jointly multivariate Gaussian variables. The optimal compressed representation is a noisy linear projection onto eigenvectors of the normalized regression matrix $\Sigma_{x|y}\Sigma_x^{-1}$, which are exactly the canonical correlation analysis (CCA) directions, but the compression tradeoff parameter $\beta$ uniquely determines both the effective dimension and the scale of each eigenvector via a cascade of structural phase transitions. The paper also provides a closed-form expression for the entire compression-relevance information curve in terms of the eigenvalue spectrum.

## Problem & setting
The Information Bottleneck method (Tishby et al., 1999) compresses a source variable $X$ while preserving information about a relevance variable $Y$, via the variational problem $\min_{p(t|x)} \mathcal{L} = I(X;T) - \beta I(T;Y)$. Prior work handled discrete clustering. This paper addresses the continuous case for jointly Gaussian $(X, Y)$, for which the general continuous IB problem is otherwise intractable. The key result is that Gaussianity forces the optimal mapping to be a noisy linear transformation $T = AX + \xi$, $\xi \sim \mathcal{N}(0, \Sigma_\xi)$, and this restriction makes the problem analytically solvable.

## Method
The optimal projection is characterized in Theorem 3.1: let $\{v_i\}$ be the left eigenvectors of $\Sigma_{x|y}\Sigma_x^{-1}$ sorted by ascending eigenvalues $\lambda_1 \leq \lambda_2 \leq \cdots$. For a given $\beta$, the optimal projection matrix is

$$A = \mathrm{diag}(\alpha_1, \ldots, \alpha_{n(\beta)}, 0, \ldots, 0) \cdot V,$$

where $V$ stacks the eigenvectors as rows, and the coefficients are

$$\alpha_i = \sqrt{\frac{\beta(1-\lambda_i)-1}{\lambda_i r_i}}, \quad r_i = v_i^T \Sigma_x v_i,$$

with $\alpha_i = 0$ (eigenvector dropped) whenever $\beta < \beta_i^c = (1-\lambda_i)^{-1}$. As $\beta$ increases through the cascade of critical values $\beta_i^c$, additional eigenvectors enter the representation and their norms grow continuously from zero — a series of structural phase transitions parameterizing a "continuous rank." The noise covariance is $\Sigma_\xi = I$ (WLOG, by a reparameterization lemma). A Blahut-Arimoto-style iterative algorithm is derived for the Gaussian case, updating $A_k$ and $\Sigma_{\xi_k}$ via explicit covariance recursions that converge to the eigenvector solution.

The closed-form information curve (compression-relevance tradeoff) is:

$$I(T;Y) = I(T;X) - \frac{n_I}{2} \log\!\left( \frac{n_I}{\prod_{i=1}^{n_I}(1-\lambda_i)^{1/n_I}} \cdot e^{2I(T;X)/n_I} \cdot \prod_{i=1}^{n_I} \lambda_i^{1/n_I} \right),$$

piecewise analytic in segments corresponding to successively larger $n_I = n_\beta(I(T;X))$.

## Key results
The optimal representation is always a subset of the CCA directions, weighted by $\beta$-dependent coefficients that differ from the CCA scaling $\sqrt{1-\lambda_i}$. The information curve is everywhere concave and smooth (derivative $= \beta^{-1}$), composed of analytic segments; concavity holds even for each individual segment, not just globally. The tangent slope at the origin is bounded by $1 - \lambda_1$, tighter than the data-processing bound. For $\beta \to \infty$ the curve saturates at $I(X;Y) = \frac{1}{2}\sum_i \log \lambda_i^{-1}$. The iterative Gaussian IB algorithm converges within approximately 20 steps to the correct eigenvector norms in experiments. An extension to the IB with side-information (IBSI) case is sketched, leading to a generalized eigenvalue problem in $A$.

## Relevance to this research
The Gaussian IB result is directly relevant to the VFE transformer's information-geometric foundations. The $\beta$-parametrized tradeoff between compression ($I(X;T)$) and relevance ($I(T;Y)$) is structurally analogous to the tradeoff in the VFE Lagrangian between KL self-coupling and belief-coupling terms. The critical phase transitions in GIB — where effective rank of the representation changes discontinuously as $\beta$ crosses $\beta_i^c = (1-\lambda_i)^{-1}$ — provide a concrete information-theoretic picture of how compression pressure controls representational dimensionality, directly connecting to questions of effective head dimension and feature selection in GL(K) attention. The regression-matrix eigenvectors $\Sigma_{x|y}\Sigma_x^{-1}$ and the noisy linear projection $T = AX + \xi$ bear comparison to the Gaussian belief update in the VFE E-step ($\mu_q \leftarrow \mu_p + \Sigma_p(\Sigma_p + \Sigma_\text{obs})^{-1}(\text{obs} - \mu_p)$). The iterative GIB algorithm's Blahut-Arimoto-like structure parallels the iterative VFE minimization (E/M-step alternation). For the information geometry of SPD belief spaces, GIB gives an exact instance of how geometry (eigenspectrum of $\Sigma$) shapes information flow and dimensionality selection.

## Cross-links
- Concepts: [[Information Bottleneck]], [[Canonical Correlation Analysis]], [[Information Geometry]], [[Variational Free Energy]], [[Gaussian Beliefs]]
- Related sources: [[tishby1999information]], [[globerson2004sufficient]], [[pennec-2006-affine-invariant-tensor]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention]], [[participatory-it-from-bit]]

> [!note] Why the project cites it (from manuscript-citation note)
> Of the entire IB family this is the closest to PIFB, because PIFB's representations are **Gaussian belief tuples** $(\mu, \Sigma, \phi)$ — exactly the regime Chechik et al. solve. Their result says the optimal relevance-preserving compression of a Gaussian source is a covariance-eigenstructure operation, congenial to the project's treatment of belief covariances $\Sigma$ on the SPD manifold with affine-invariant geometry (see [[pennec-2006-affine-invariant-tensor]]). It gives a tractable benchmark in the one case where the compression-relevance trade-off is exactly solvable and matches the project's representation class.

## BibTeX
```bibtex
@article{chechik2005information,
  author  = {Chechik, Gal and Globerson, Amir and Tishby, Naftali and Weiss, Yair},
  title   = {Information Bottleneck for {G}aussian Variables},
  journal = {Journal of Machine Learning Research},
  volume  = {6},
  pages   = {165--188},
  year    = {2005},
}
```
