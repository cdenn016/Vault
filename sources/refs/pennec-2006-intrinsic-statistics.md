---
type: reference
title: "Intrinsic Statistics on Riemannian Manifolds: Basic Tools for Geometric Measurements"
aliases:
  - "Pennec 2006 (Intrinsic Statistics)"
  - "Pennec2009"
  - "Pennec (2006) Intrinsic Statistics"
authors:
  - Xavier Pennec
year: 2006
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# Intrinsic Statistics on Riemannian Manifolds: Basic Tools for Geometric Measurements

> [!info] Citation
> Xavier Pennec (2006). "Intrinsic Statistics on Riemannian Manifolds: Basic Tools for Geometric Measurements." *Journal of Mathematical Imaging and Vision* 25(1), 127–154. DOI: [10.1007/s10851-006-6228-4](https://doi.org/10.1007/s10851-006-6228-4).

> [!warning] Cite-key / year note
> The program cites this as **Pennec2009** with DOI `10.1007/s10851-006-6228-4`. That DOI resolves to the 2006 *JMIV* article recorded here (the journal date is 2006, vol. 25(1)). The "2009" key most likely refers instead to Pennec's 2009 book chapter "Statistical Computing on Manifolds: From Riemannian Geometry to Computational Anatomy" (in *Emerging Trends in Visual Computing*, Springer LNCS 5416, pp. 347–386, DOI 10.1007/978-3-642-00826-9_16), which surveys the same toolkit. Verify which work the manuscript intends; the DOI as written points to the 2006 JMIV paper below.

## What it establishes

- A coherent framework for **statistics on Riemannian manifolds**: the Riemannian (Fréchet/Karcher) mean as minimizer of expected squared geodesic distance, its existence/uniqueness via the exponential and logarithm maps, and a Newton-type gradient iteration to compute it.
- Intrinsic notions of dispersion: the covariance of a manifold-valued random variable defined in the tangent space at the mean, plus a Mahalanobis distance and a normal law on manifolds.
- The cut-locus/injectivity-radius caveats that bound where these constructions are well defined — the practical companion to the existence theory of [[karcher-1977-center-of-mass]].

## Why the project cites it

This is the statistics-on-manifolds toolkit the program leans on whenever it treats beliefs as random points on a curved fiber and asks for their mean and spread. The Riemannian mean and tangent-space covariance are exactly the constructs behind coherence-weighted coarse-graining and the meta-agent barycenters in [[Meta-agents and hierarchical emergence]]: pooling covariances and frames is computing a Fréchet mean and its dispersion on the SPD cone / $GL^+(K)$ Lie algebra. The Mahalanobis/normal-law-on-manifold machinery is the geometric analog of the Gaussian-belief KL terms the model minimizes. It sits beside [[pennec-2006-affine-invariant-tensor]] (the affine-invariant SPD metric) as Pennec's general-manifold statistical layer, supporting [[SPD-manifold geometry and Riemannian optimization]] and the hierarchical-emergence construction in [[participatory-it-from-bit]].

> [!note] Editorial: Provides the statistical-estimation tools (Karcher mean, intrinsic covariance) on top of the affine-invariant SPD geometry; cited as a methods reference, not for a project-specific result.

## BibTeX

```bibtex
@article{pennec2006intrinsic,
  title   = {Intrinsic Statistics on Riemannian Manifolds: Basic Tools for Geometric Measurements},
  author  = {Pennec, Xavier},
  journal = {Journal of Mathematical Imaging and Vision},
  volume  = {25},
  number  = {1},
  pages   = {127--154},
  year    = {2006},
  doi     = {10.1007/s10851-006-6228-4}
}
```
