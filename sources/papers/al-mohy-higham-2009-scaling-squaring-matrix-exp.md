---
type: paper
title: A New Scaling and Squaring Algorithm for the Matrix Exponential
aliases:
  - "Al-Mohy, Higham 2009"
  - "Scaling and Squaring Matrix Exponential"
authors:
  - Awad H. Al-Mohy
  - Nicholas J. Higham
year: 2009
arxiv: null
url: https://doi.org/10.1137/09074721X
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

# A New Scaling and Squaring Algorithm for the Matrix Exponential

> [!info] Citation
> Al-Mohy, A. H., & Higham, N. J. (2009). A New Scaling and Squaring Algorithm for the Matrix Exponential. SIAM Journal on Matrix Analysis and Applications, 31(3), 970-989. DOI 10.1137/09074721X.

## TL;DR

This paper gives the scaling-and-squaring algorithm that, with minor refinements, is the default matrix-exponential routine in modern numerical libraries (it underlies `scipy.linalg.expm` and is the algorithmic ancestor of `torch.matrix_exp`). The method approximates $e^A$ by $\big(r_m(2^{-s}A)\big)^{2^s}$, where $r_m$ is the $[m/m]$ diagonal Padé approximant to $e^x$; the scaling integer $s$ shrinks $\|2^{-s}A\|$ into the region where the Padé approximant is accurate, and $s$ repeated squarings undo the scaling. The contribution over Higham's 2005 algorithm is a sharper backward-error analysis that chooses $s$ from the sequence $\{\|A^k\|^{1/k}\}$ rather than from $\|A\|$ alone, together with a fix to how diagonal entries are handled in the squaring phase for (quasi-)triangular matrices. Both changes attack *overscaling*: the failure mode in which a needlessly large $s$ is selected, so that many squarings amplify rounding error and corrupt accuracy. The new algorithm is never worse than its predecessor at equal cost and is often substantially better, in accuracy, cost, or both, on non-normal and triangular matrices.

## Problem & setting

Computing $e^A$ for a dense matrix $A \in \mathbb{C}^{n\times n}$ is a workhorse operation, and scaling-and-squaring is the most widely used dense method because it pairs a cheap, rationally-evaluated Padé core with a self-correcting halving/squaring wrapper. The accuracy of $r_m(2^{-s}A) \approx e^{2^{-s}A}$ is controlled by a backward-error bound: one shows that $r_m(2^{-s}A) = e^{2^{-s}A + E}$ for some perturbation $E$, and chooses the smallest $s$ (and a Padé degree $m$, in practice up to $m=13$) so that the relative backward error $\|E\|/\|2^{-s}A\|$ falls below the unit roundoff $u \approx 1.1\times10^{-16}$ in double precision. Higham's 2005 SIAM Review algorithm formalized this with parameters $\theta_m$ — the largest argument norm tolerable at each degree, with $\theta_{13}\approx 5.37$ for the degree-13 default — and made scaling-and-squaring the textbook standard (Higham, *Functions of Matrices*, 2008, Ch. 10). The defect the present paper isolates is that bounding the perturbation through $\|2^{-s}A\|$ is pessimistic for non-normal matrices, because $\|A^k\|$ can be far smaller than $\|A\|^k$. When the bound is loose, the algorithm scales more aggressively than the true error demands, and each of the $s$ squarings of a near-singular or non-normal iterate can magnify rounding error — the overscaling phenomenon flagged by several earlier authors.

## Method

The backward error of the $[m/m]$ Padé approximant is an analytic function $h_{2m+1}$ of the scaled matrix, expressible as a power series $\sum_{k\ge 2m+1} c_k X^k$ in $X = 2^{-s}A$. Higham 2005 bounded $\|h_{2m+1}(X)\| \le \tilde h(\|X\|)$ using only $\|X\| = 2^{-s}\|A\|$. Al-Mohy and Higham instead bound each term using the sharper quantities
$$ \alpha_p(A) \;=\; \max\!\big(\,\|A^p\|^{1/p},\ \|A^{p+1}\|^{1/(p+1)}\,\big), $$
which exploit that for a power series the relevant growth rate is $\|A^k\|^{1/k}$, not $\|A\|$. Because $\|A^k\|^{1/k}$ converges down to the spectral radius and can sit well below $\|A\|$ for non-normal $A$, the resulting bound on the backward error is tighter, so a smaller $s$ suffices and overscaling is avoided. The $\alpha_p$ are not formed by computing matrix powers explicitly; they are estimated cheaply via a 1-norm power-iteration estimator (the Higham-Tisseur block estimator) applied to $A^p$ through repeated matrix-vector products, keeping the extra cost low relative to the Padé evaluation. The second ingredient addresses the squaring recurrence $X_{j+1} = X_j^2$: for a triangular (or, after a Schur reduction, quasi-triangular) matrix the exact diagonal of $e^{2^{-s}A}$ is known in closed form, $\exp$ of the diagonal entries, and likewise the exact superdiagonal blocks satisfy a known formula. Substituting these exact values during squaring, rather than propagating the Padé approximation's diagonal, removes a source of error that the repeated squarings would otherwise compound.

## Key results

The paper proves backward-error bounds in terms of the $\alpha_p$ sequence and uses them to drive the selection of $(s,m)$, retaining the same set of admissible Padé degrees ($m \in \{3,5,7,9,13\}$ with degree 13 as the high-accuracy default) and the same $\theta_m$ thresholds, but evaluated against the sharper norm proxies. The headline empirical claim, verified by their numerical experiments, is that the new algorithm delivers accuracy at least as good as Higham 2005 at no greater cost on general matrices, and on matrices that are triangular or that trigger overscaling it yields significant gains in accuracy, in operation count, or in both simultaneously. The evidence is the standard package for a numerical-linear-algebra method of this era: rigorous backward-error theorems plus a test battery of matrices (including deliberately non-normal and triangular cases) comparing forward errors against high-precision reference solutions. I have not independently re-verified the specific error figures from the paper's tables, so those should be read qualitatively rather than quoted as exact constants.

## Relevance to this research

This is the algorithm whose floating-point behavior governs the fidelity of every matrix exponential in the gauge-theoretic VFE transformer. Each gauge transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ and every Baker-Campbell-Hausdorff retraction is a `torch.matrix_exp` call whose backward error, scaling choice, and overscaling risk are exactly what this paper analyzes; in fp32 the unit roundoff is $u\approx 6\times10^{-8}$ rather than the $10^{-16}$ the $\theta_m$ thresholds were tuned for, so the margin against accumulated squaring error is far thinner and the overscaling diagnosis here is directly load-bearing. The $\alpha_p$ analysis is the lever that distinguishes the well-behaved compact-rotation sector of the gauge algebra from the non-compact symmetric-$\phi$ sector: for skew-symmetric generators $\|A^k\|^{1/k}=\|A\|$ and scaling is tight, whereas for the symmetric (SPD-cone-tangent) directions the spectral radius and $\|A\|$ diverge, so $\|2^{-s}A\|$ overestimates the error, $s$ is inflated, and the squaring phase amplifies roundoff precisely where the transport leaves the bounded-rotation regime. This is the concrete numerical mechanism behind clamp choices and any observed holonomy-NaN fraction in the non-compact sector, and it ties the manuscript's [[Baker-Campbell-Hausdorff formula]] retraction to a verifiable error model. See [[SPD-manifold geometry and Riemannian optimization]] for the affine-invariant geometry these exponentials parameterize.

## Cross-links

- Concepts / Themes: [[SPD-manifold geometry and Riemannian optimization]], [[Baker-Campbell-Hausdorff formula]]
- Related sources: [[pennec-2006-affine-invariant-tensor]], [[bonnabel-2013-riemannian-sgd]]

## BibTeX

```bibtex
@article{almohyhigham2009scaling,
  author  = {Al-Mohy, Awad H. and Higham, Nicholas J.},
  title   = {A New Scaling and Squaring Algorithm for the Matrix Exponential},
  journal = {SIAM Journal on Matrix Analysis and Applications},
  volume  = {31},
  number  = {3},
  pages   = {970--989},
  year    = {2009},
  publisher = {Society for Industrial and Applied Mathematics},
  doi     = {10.1137/09074721X},
  url     = {https://doi.org/10.1137/09074721X}
}
```
