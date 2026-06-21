---
type: paper
title: "On the Existence and Uniqueness of the Real Logarithm of a Matrix"
aliases:
  - "Culver 1966"
  - "Culver 1966 real logarithm"
authors:
  - Culver, W.
year: 1966
arxiv: null
url: https://doi.org/10.2307/2035390
tags:
  - cluster/spd-geometry
  - project/transformer
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# On the Existence and Uniqueness of the Real Logarithm of a Matrix

> [!info] Citation
> Culver, W. (1966). "On the Existence and Uniqueness of the Real Logarithm of a Matrix." *Proceedings of the American Mathematical Society*, 17(5), 1146–1151. doi:10.2307/2035390. URL: https://www.ams.org/journals/proc/1966-017-05/S0002-9939-1966-0202740-6/

## TL;DR

This paper establishes the necessary and sufficient conditions under which a real nonsingular matrix possesses a real logarithm — that is, a real matrix $B$ such that $e^B = A$. The central result is that a real nonsingular matrix $A$ has a real logarithm if and only if every elementary divisor (Jordan block) corresponding to a negative real eigenvalue occurs an even number of times. The paper also characterizes when such a logarithm is unique among real matrices.

## Problem & setting

Given a real nonsingular square matrix $A$, one asks whether there exists a real matrix $B$ satisfying $e^B = A$. Over $\mathbb{C}$ any nonsingular matrix has a logarithm (via the Jordan form and the complex branch of $\log$), but complex logarithms come in conjugate pairs and the question of which matrices admit a *real* logarithm is nontrivial. Prior work (e.g. Rinehart 1955) had treated special cases; Culver's 1966 paper is the first complete characterization via Jordan structure.

## Method

The proof works through the real Jordan canonical form. A real nonsingular matrix $A$ is brought to its real Jordan form, which consists of blocks corresponding to (i) positive real eigenvalues, (ii) negative real eigenvalues (occurring in even-multiplicity pairs for a real log to exist), and (iii) complex conjugate pairs. Each block type admits a real logarithm independently. The even-multiplicity condition on negative-eigenvalue blocks is necessary because a single real Jordan block with negative eigenvalue $-\lambda$ ($\lambda > 0$) does not have a real logarithm — its only logarithms are complex ($\log \lambda + i(2k+1)\pi$ on the diagonal, forcing off-diagonal terms to be complex). When negative eigenvalue blocks come in pairs, a $2\times 2$ rotation-block representation restores a real form.

Uniqueness requires additionally that the matrix has no eigenvalues on $(-\infty, 0]$ and that the imaginary parts of all eigenvalues of $B$ lie in $(-\pi, \pi)$; under these conditions the principal logarithm is the unique real logarithm.

## Key results

- **Existence theorem.** A real nonsingular matrix $A$ has a real logarithm if and only if each Jordan block corresponding to a negative real eigenvalue occurs an even number of times in the Jordan form of $A$.
- **Uniqueness theorem.** The real logarithm is unique (among real matrices) when $A$ has no negative real eigenvalues and the imaginary parts of all complex eigenvalues lie strictly in $(-\pi, \pi)$.
- The paper gives explicit constructions of the logarithm in each case, establishing existence by construction rather than abstract argument.

## Relevance to this research

The matrix logarithm is the foundational operation behind two geometric structures used in the VFE transformer. First, the **Log-Euclidean metric** on SPD matrices (see [[arsigny-2006-log-euclidean]]) maps covariances $\Sigma \mapsto \log \Sigma$ into the flat symmetric-matrix vector space; all subsequent calculus (means, geodesics, interpolation) is performed there and mapped back with the matrix exponential. The well-posedness of this map — that a real SPD matrix always has a unique real symmetric logarithm — follows directly from Culver's theorem: SPD matrices have strictly positive eigenvalues, so no negative-eigenvalue Jordan blocks arise and the real logarithm exists and is unique. Second, the **Baker-Campbell-Hausdorff retraction** used for the `block_glk` gauge group and the Lie-algebra transport of beliefs involves exponential and logarithmic maps on $GL(K)$; the existence of real group-valued logarithms (needed to invert the exponential map locally) likewise rests on the conditions Culver establishes. This paper is therefore the foundational existence-and-uniqueness reference underpinning the matrix-log and matrix-exp operations used throughout the SPD-geometry and gauge-transport components of the codebase.

## Cross-links

- Concepts: [[Symmetric spaces and the SPD cone]], [[Parallel transport]], [[Baker-Campbell-Hausdorff formula]]
- Related sources: [[arsigny-2006-log-euclidean]], [[bhatia-2007-positive-definite-matrices]], [[pennec-2006-affine-invariant-tensor]], [[absil-2008-optimization-matrix-manifolds]]
- Manuscript/Project: [[VFE Transformer Program]], [[gl-k-attention|Attention as Gauge-Theoretic Variational Inference]]

## BibTeX

```bibtex
@article{culver1966existence,
  author  = {Culver, W.},
  title   = {On the Existence and Uniqueness of the Real Logarithm of a Matrix},
  journal = {Proceedings of the American Mathematical Society},
  volume  = {17},
  number  = {5},
  pages   = {1146--1151},
  year    = {1966},
  doi     = {10.2307/2035390},
  url     = {https://www.ams.org/journals/proc/1966-017-05/S0002-9939-1966-0202740-6/}
}
```
