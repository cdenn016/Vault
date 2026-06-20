---
type: reference
title: Nineteen Dubious Ways to Compute the Exponential of a Matrix, Twenty-Five Years Later
aliases:
  - "Moler, Van Loan 2003"
  - "Nineteen Dubious Ways to Compute the Exponential of a Matrix"
authors:
  - Cleve Moler
  - Charles Van Loan
year: 2003
arxiv: null
url: https://doi.org/10.1137/S00361445024180
tags:
  - cluster/spd-geometry
  - cluster/methodology
  - project/transformer
  - project/multi-agent
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Nineteen Dubious Ways to Compute the Exponential of a Matrix, Twenty-Five Years Later

> [!info] Citation
> Moler, C., & Van Loan, C. (2003). Nineteen Dubious Ways to Compute the Exponential of a Matrix, Twenty-Five Years Later. SIAM Review, 45(1), 3-49. DOI 10.1137/S00361445024180.

## TL;DR

This is the canonical survey of how one actually computes $e^A$ for a square matrix $A$, and a sober census of why nearly every obvious method is, in some regime, numerically untrustworthy. The authors catalogue roughly nineteen candidate algorithms grouped into five families — truncated series, ordinary-differential-equation integrators, polynomial (Cayley–Hamilton, Lagrange/Newton interpolation) methods, matrix-decomposition (eigenvalue and Schur) methods, and operator-splitting methods — and assess each on stability, efficiency, and the range of matrices it survives. The 2003 reprise adds twenty-five years of analysis on top of the 1978 original and concludes that no single method is uniformly reliable, but that **scaling and squaring combined with a Padé approximant** is the method of choice in practice, while the seductively simple **eigenvalue/eigenvector method fails precisely for non-normal, defective, and near-defective matrices** because it must invert an ill-conditioned eigenvector matrix. The paper is also where the field's intuition about the *conditioning* of the exponential map itself — quantified through the Fréchet derivative and a matrix-exponential condition number that grows with $\|A\|$ and with the departure from normality — is laid out for numerical-analysis readers.

## Problem & setting

The task is to evaluate $e^A = \sum_{k=0}^\infty A^k/k!$ for a given $n\times n$ real or complex matrix $A$, the closed-form solution operator of the linear system $\dot{x}=Ax$, $x(0)=x_0 \mapsto x(t)=e^{tA}x_0$. The series converges for every $A$, so the difficulty is never existence but *numerical* computation in finite precision: cancellation, overflow, and the amplification of rounding error. Moler and Van Loan build on the long-standing observation that the spectral / Jordan-form solution $e^A = V e^\Lambda V^{-1}$ is mathematically exact yet practically fragile, and that the smoothness of the closed form hides the genuine ill-conditioning carried by $V$ and by the spectral spread of $A$. The 1978 paper had already established the five-family taxonomy and the "dubious" verdict; the 2003 update revisits each family in light of subsequent work (notably backward-error analysis of scaling-and-squaring, the Schur–Parlett recurrence for general matrix functions, and Krylov-subspace methods for the action $e^A b$ on large sparse $A$), and re-states which conclusions held up.

## Method

The survey's organizing instrument is a side-by-side stability/efficiency assessment of each algorithm. The series family includes the truncated Taylor sum and its rational cousins; a truncated Taylor series suffers catastrophic cancellation when $A$ has eigenvalues of large negative real part (the celebrated example where $e^A$ has tiny entries but the partial sums have enormous ones). The decomposition family reduces $A$ to diagonal or triangular form, $A = V\Lambda V^{-1}$, and applies $\exp$ to the spectrum; its error is governed by the eigenvector-conditioning $\kappa(V) = \|V\|\,\|V^{-1}\|$, which blows up as $A$ approaches a defective matrix with coalescing eigenvalues and parallel eigenvectors. The Schur-form variant ($A = QTQ^{*}$ with $Q$ unitary) trades the ill-conditioned $V$ for an orthogonal $Q$ but pushes the difficulty into evaluating $\exp$ of the triangular factor, handled by the Parlett recurrence which itself degrades when eigenvalues cluster.

The recommended algorithm is **scaling and squaring with Padé**: choose an integer $s$ so that $\|A/2^{s}\|$ is small, evaluate a diagonal Padé approximant $r_{m}(A/2^{s}) \approx e^{A/2^{s}}$ (a rational function chosen because Padé is far more accurate than Taylor for a given cost when the argument is small), and recover $e^{A} = \big(r_{m}(A/2^{s})\big)^{2^{s}}$ by repeated squaring. The Padé error is controlled by making the scaled argument small; the squaring reassembles the full exponential. The sensitivity of the *problem* — independent of any algorithm — is captured by the Fréchet derivative $L(A,E) = \frac{d}{dt}e^{A+tE}\big|_{t=0} = \int_{0}^{1} e^{(1-\tau)A} E\, e^{\tau A}\, d\tau$, whose norm defines a matrix-exponential condition number
$$ \kappa_{\exp}(A) = \frac{\|L(A)\|\,\|A\|}{\|e^{A}\|}, $$
which is large when $A$ is far from normal and grows with the spectral spread; this condition number lower-bounds the relative error any backward-stable method can deliver.

## Key results

The survey's enduring verdict is qualitative rather than a single theorem: of the nineteen methods, none is unconditionally satisfactory, several are actively dangerous, and scaling-and-squaring-with-Padé is the best general-purpose default — the conclusion later hardened by Higham's backward-error-optimal parameter selection. The eigenvalue/eigenvector method is singled out as unreliable precisely because its accuracy is tied to $\kappa(V)$, so it degrades smoothly toward useless as $A$ becomes non-normal and breaks down entirely at defective matrices where $V$ is singular; the paper's point is that this failure is invisible in exact arithmetic and only appears in floating point. Truncated Taylor series is shown to be unreliable for matrices with widely separated or large-magnitude eigenvalues owing to cancellation. The ODE-integrator family can work but is generically less efficient than the tailored Padé route. The 2003 additions report that for the *action* $e^{A}b$ on large sparse matrices, Krylov-subspace methods change the cost calculus, and that the Schur–Parlett framework generalizes the triangular approach to arbitrary matrix functions. Throughout, the strength of evidence is analytic (error bounds, conditioning arguments) backed by illustrative numerical examples rather than large benchmark suites; the claims about *which* methods fail are rigorous, while "best in practice" is an engineering judgment the authors are explicit about.

## Relevance to this research

This survey pins exactly the numerical regime the gauge-theoretic VFE transformer operates in whenever it forms $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ or any retraction through the matrix exponential on the [[SPD-manifold geometry and Riemannian optimization]] cone. Two distinctions from the paper are load-bearing here. First, the conditioning of $\exp$ depends sharply on departure from normality: when the generators $\phi$ are *skew* (a compact gauge group, $e^{\phi}$ orthogonal) the eigenvector matrix is unitary and $\kappa(V)=1$, so even the naive spectral method is well behaved; but when $\phi$ is *symmetric* — the SPD / non-compact $GL(K)$ directions — $A$ is non-normal under the group action, $\kappa_{\exp}$ grows with $\|\phi\|$, and the eigenvalue method's breakdown for near-defective matrices becomes a live failure mode rather than a textbook curiosity. Second, the paper is the reason the implementation should prefer scaling-and-squaring-with-Padé (and not a bare eigendecomposition) for $\exp(\phi)$, and the reason clamping $\|\phi\|$ before exponentiation is a genuine conditioning control and not mere cosmetics: the squaring count $s$ and the Padé accuracy are both functions of $\|A/2^{s}\|$, so bounding the generator norm directly bounds the attainable forward error and the NaN/Inf risk in fp32. The same conditioning lens informs how far one can truncate the [[Baker-Campbell-Hausdorff formula]] when composing $e^{\phi_i}e^{-\phi_j}$ and how reliably the resulting transport feeds the curvature / [[Holonomy]] diagnostics.

## Cross-links
- Concepts / Themes: [[SPD-manifold geometry and Riemannian optimization]], [[Holonomy]], [[Baker-Campbell-Hausdorff formula]]
- Related sources: [[amari-1998-natural-gradient]]

## BibTeX
```bibtex
@article{molervanloan2003nineteen,
  author  = {Moler, Cleve and Van Loan, Charles},
  title   = {Nineteen Dubious Ways to Compute the Exponential of a Matrix, Twenty-Five Years Later},
  journal = {SIAM Review},
  volume  = {45},
  number  = {1},
  pages   = {3--49},
  year    = {2003},
  publisher = {Society for Industrial and Applied Mathematics},
  doi     = {10.1137/S00361445024180},
  url     = {https://doi.org/10.1137/S00361445024180}
}
```
