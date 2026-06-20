---
type: paper
title: Coordinate Independent Convolutional Networks — Isometry and Gauge Equivariant Convolutions on Riemannian Manifolds
aliases:
  - "Weiler, Forré, Verlinde, Welling 2021"
  - "Coordinate Independent CNNs"
authors:
  - Maurice Weiler
  - Patrick Forré
  - Erik Verlinde
  - Max Welling
year: 2021
arxiv: 2106.06020
url: https://arxiv.org/abs/2106.06020
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/mathematics
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Coordinate Independent Convolutional Networks — Isometry and Gauge Equivariant Convolutions on Riemannian Manifolds

> [!info] Citation
> Weiler, M., Forré, P., Verlinde, E., & Welling, M. (2021). Coordinate Independent Convolutional Networks — Isometry and Gauge Equivariant Convolutions on Riemannian Manifolds. arXiv:2106.06020.

## TL;DR

This monograph derives convolutional neural networks on Riemannian manifolds from a single physical principle: a network's inference must not depend on the arbitrary local coordinates (reference frames) chosen to express its feature fields. The central theorem is that demanding *coordinate independence together with weight sharing* is not merely compatible with, but logically *forces*, equivariance under local gauge transformations — changes of the local frame at each point. Feature maps are recast as sections of associated fiber bundles transforming in chosen representations of a structure group $G$, convolution kernels become equivariant maps constrained by that representation, and the comparison of features at distinct points requires parallel transport along a connection. The framework subsumes group-equivariant CNNs, gauge CNNs, and spherical CNNs as special cases distinguished by the manifold's $G$-structure, and it cleanly separates the *local* (gauge) symmetry that every coordinate-independent network must respect from the *global* (isometry) symmetries it inherits when the metric has them. It is, in effect, a textbook-grade unification of geometric deep learning written in the language of principal and associated bundles.

## Problem & setting

Ordinary convolution relies on translating one shared kernel across a flat domain, which presupposes a global system of coordinates and a canonical way to compare a kernel placed at one location with the same kernel placed at another. On a curved manifold neither presupposition survives: there is no global chart, tangent spaces at different points are distinct vector spaces, and any local frame one picks to write down a feature vector is arbitrary. Prior work — group-equivariant CNNs (Cohen & Welling 2016), spherical CNNs (Cohen et al. 2018), and the earlier gauge-equivariant CNN on the icosahedron (Cohen et al. 2019) — had shown case by case how to build convolutions respecting particular symmetries, but each construction was tailored to its domain. Weiler, Forré, Verlinde, and Welling ask the prior-agnostic question: what must *any* convolution look like if it is to give the same answer regardless of the reference frames used to coordinatize its inputs and outputs? Their setting is a smooth Riemannian manifold $M$ equipped with a $G$-structure — a reduction of the frame bundle to a structure group $G \le \mathrm{GL}(d)$ — and feature fields modeled as sections of associated bundles. The assumptions are differential-geometric rather than statistical: a metric, a compatible connection, and a chosen field type (representation) for every feature space.

## Method

A feature field of type $\rho$ is a section of the associated bundle $A = P \times_\rho V$, where $P$ is the principal $G$-bundle of reference frames and $\rho: G \to \mathrm{GL}(V)$ is the representation carried by that feature. Concretely, the numerical coefficients $f(x)$ of a feature depend on the chosen frame, and a local gauge transformation $g(x) \in G$ — a change of frame at $x$ — acts on them by

$$ f(x) \;\longmapsto\; \rho\big(g(x)\big)\, f(x). $$

Coordinate independence is the statement that the network's output transforms by the *output* representation whenever its input is regauged this way; this is local gauge equivariance, and the paper's foundational result is that weight sharing makes it mandatory rather than optional. To convolve, a kernel must aggregate feature vectors sampled at neighboring points, but those neighbors live in different fibers expressed in different frames. The kernel therefore acts on features *parallel-transported* into a common frame along the connection of the $G$-structure, and the requirement that the whole operation commute with regauging imposes the kernel constraint

$$ K\big(\rho_{\mathrm{in}}(g)\, v\big) \;=\; \rho_{\mathrm{out}}(g)\, K(v), \qquad g \in G, $$

so admissible kernels are exactly the $G$-equivariant (intertwiner) maps between input and output representations. Because transport is path-dependent on a curved manifold, comparing features moved around a closed loop returns them rotated by the *holonomy* of the connection — the group element $\mathrm{Hol}(\gamma) \in G$ accumulated around loop $\gamma$ — and the connection is flat (trivial holonomy) only when its curvature vanishes. Transition functions between overlapping frames satisfy the bundle *cocycle* condition $g_{ik} = g_{ij}\,g_{jk}$, which is precisely the consistency the gauge formulation must respect. Layered on top of this purely local structure, the paper shows that when the metric admits isometries that are symmetries of the $G$-structure, the resulting convolution is additionally equivariant under those *global* isometries, recovering group-equivariant CNNs as the homogeneous-space special case. The construction is demonstrated on a Möbius strip, whose nontrivial topology makes the orientation gauge unavoidable, with public code.

## Key results

The principal result is a *necessity* theorem rather than a benchmark: under coordinate independence and weight sharing, local gauge equivariance is forced, and the degree of equivariance required is dictated by the structure group $G$ of the manifold's $G$-structure — a larger $G$ (less reduction) demands equivariance under a larger gauge group and so admits fewer kernels. The framework classifies admissible convolution kernels as intertwiners between the input and output field representations, giving a constructive basis for steerable kernels on manifolds. It establishes that coordinate-independent convolutions are automatically equivariant with respect to the isometries that preserve the $G$-structure, unifying isometry equivariance and gauge equivariance under one bundle-theoretic roof and exhibiting group-equivariant CNNs, spherical CNNs, and gauge CNNs as instances selected by the choice of $M$, $G$, and field types. The Möbius-strip implementation is a proof of concept demonstrating orientation-independent inference on a topologically nontrivial domain rather than a large-scale empirical study; the contribution is the theory and its internal coherence, which is strong and self-contained, not a state-of-the-art accuracy claim.

## Relevance to this research

This is the definitive monograph deriving gauge equivariance from first principles, and it supplies the textbook-grade statements the VFE transformer program leans on rather than asserts. Its central theorem — that coordinate independence plus weight sharing *forces* local-gauge equivariance, with the feature transport rule $f \mapsto \rho(g)\,f$ and the intertwiner kernel constraint as consequences — is the rigorous justification for the program's insistence that belief and covariance transport obey the gauge-covariant sandwich $\Omega\,\Sigma\,\Omega^\top$ and that per-head operations respect the $\mathrm{GL}(K)$ structure group rather than break it (see [[Gauge equivariance and geometric deep learning]], [[Gauge transformation]]). Its full parallel-transport-and-holonomy bookkeeping directly informs the program's connection design: the cocycle condition $g_{ik}=g_{ij}g_{jk}$ is the consistency the transports $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$ must satisfy, and the curvature/holonomy distinction is exactly the Regime-I (flat, trivial holonomy) versus Regime-II (learned non-flat connection) split the codebase toggles between (see [[Parallel transport]], [[Holonomy]], [[Non-flat connection and the photon analogy]]). Finally, its separation of mandatory local gauge symmetry from inherited global isometry symmetry clarifies what the program can and cannot claim: gauge equivariance is structural, whereas any global equivariance is contingent on the relevant isometries actually being $G$-structure symmetries.

## Cross-links

- Concepts / Themes: [[Gauge equivariance and geometric deep learning]], [[Holonomy]], [[Parallel transport]], [[Gauge transformation]], [[Non-flat connection and the photon analogy]]
- Related sources: [[amari-1998-natural-gradient]], [[pennec-2006-affine-invariant-tensor]]

## BibTeX

```bibtex
@article{weiler2021coordina,
  author  = {Weiler, Maurice and Forr{\'e}, Patrick and Verlinde, Erik and Welling, Max},
  title   = {Coordinate Independent Convolutional Networks -- Isometry and Gauge Equivariant Convolutions on Riemannian Manifolds},
  journal = {arXiv preprint arXiv:2106.06020},
  year    = {2021},
  eprint  = {2106.06020},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url     = {https://arxiv.org/abs/2106.06020}
}
```
