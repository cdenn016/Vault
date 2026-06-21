---
type: paper
title: "The holographic principle"
aliases:
  - "Bousso 2002"
  - "holographic principle review"
authors:
  - Bousso, Raphael
year: 2002
arxiv: hep-th/0203101
url: https://arxiv.org/abs/hep-th/0203101
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The holographic principle

> [!info] Citation
> Bousso, R. (2002). "The holographic principle." *Reviews of Modern Physics* 74, 825. arXiv:hep-th/0203101.

## TL;DR
This is the canonical review article on the holographic principle, establishing that the area of any surface bounds the information content of adjacent spacetime regions at approximately 1.4 × 10^69 bits per square meter. The covariant entropy bound — that entropy on any light-sheet of a surface B does not exceed the area of B divided by 4 — is presented as the most general and correct formulation. The holographic principle asserts this bound reflects a fundamental reduction in the degrees of freedom of nature from the volume-scaling expected by local quantum field theory to an area-scaling dictated by quantum gravity.

## Problem & setting
Local quantum field theory predicts that the number of degrees of freedom in a spatial region scales with its volume V, even after a Planck-scale UV cutoff: N ~ V. Black hole thermodynamics, however, implies that the maximal entropy in any region bounded by area A is S_BH = A/4 (in Planck units), which grows as area rather than volume. This discrepancy — by a factor of order R in Planck units, typically enormous — is the central puzzle. Prior formulations (the spherical entropy bound of 't Hooft 1993 and Susskind 1995, derived from the generalized second law via the Susskind and Geroch processes) were limited to weakly gravitating, spherically symmetric systems in asymptotically flat space and failed in cosmological and strongly gravitating settings.

## Method
The paper proceeds from black hole thermodynamics — Bekenstein entropy S_BH = A/4, Hawking temperature T = κ/(2π), the generalized second law dS_total ≥ 0 — through the Bekenstein bound S ≤ 2πER (for weakly gravitating systems) and the spherical entropy bound S ≤ A/4, then identifies four explicit counterexamples to the naive "spacelike entropy bound" (closed cosmologies, the expanding universe, collapsing stars, and weakly gravitating systems in certain slicings). The covariant entropy bound is constructed via light-sheets: given any surface B, choose null hypersurfaces orthogonal to B along which the expansion θ ≤ 0 (non-expanding light rays); the entropy on any such light-sheet satisfies S ≤ A(B)/4. Raychaudhuri's equation governs the focusing of the null generators, and the Flanagan-Marolf-Wald (FMW) theorems establish sufficient conditions on entropy density for the bound to hold. The bound is then verified across a comprehensive set of examples: FRW cosmologies, collapsing stars and shells, nearly null boundaries, and de Sitter space.

Key equations:
- Bekenstein-Hawking entropy: S_BH = A/4 (Planck units), equivalently S_BH = kAc³/(4Gℏ)
- Bekenstein bound: S ≤ 2πER
- Spherical entropy bound: S ≤ A/4
- Covariant entropy bound: S(light-sheet of B) ≤ A(B)/4
- Degrees of freedom: N = A/4 (not V)
- Raychaudhuri: governs focusing of null generators, dθ/dλ = -(1/(D-2))θ² - σ²_ab - R_ab k^a k^b

## Key results
The covariant entropy bound holds in every tested case, including all settings where the spherical and spacelike bounds fail. The number of fundamental degrees of freedom in any region is N = A/4 rather than N ~ V, implying that local quantum field theory overcounts by a factor of order R (the radius in Planck units). Black holes saturate the bound and are the most entropic objects within a given area. The AdS/CFT correspondence is identified as an explicit realization of the holographic principle in asymptotically anti-de Sitter spacetimes, where the boundary CFT lives at one bit per Planck area. Holographic screens can be constructed for arbitrary spacetimes, supporting the claim that "the world is a hologram" in the sense that all information can be encoded on preferred 2D surfaces. The principle challenges the very notion of locality and assigns a preferred role to null hypersurfaces in the classical limit of quantum gravity.

## Relevance to this research
The holographic principle is the foundational backdrop for the participatory "it from bit" program: the claim that physical reality is constituted by information, that geometry encodes information content, and that the degrees of freedom of spacetime are area-scaling rather than volume-scaling. This maps directly onto the cluster/participatory/quantum-foundations themes in this research program. The covariant entropy bound's reliance on light-sheets and null geometry resonates with the information-geometric structures underlying the VFE transformer's belief geometry: both replace naive local (volume) counting with a global geometric (area/boundary) constraint. The role of unitarity and black hole complementarity — that no single observer can access both copies of information — echoes the perspectival, observer-relative framing of participatory realism (Wheeler's "it from bit") explored in the PIFB manuscript. The area-information duality (A/4 degrees of freedom) is a concrete instantiation of the general claim that geometry and information are unified, which the VFE/GL(K) framework pursues in the context of Riemannian/SPD belief geometry and gauge-equivariant attention.

## Cross-links
- Concepts: [[Holographic Principle]], [[Covariant Entropy Bound]], [[Black Hole Thermodynamics]], [[Information Geometry]], [[Participatory Realism]]
- Related sources: [[wheeler-1990-it-from-bit]], [[bekenstein-1973-black-holes]], [[maldacena-1998-adscft]]
- Manuscript/Project: [[PIFB]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Bousso2002,
  author  = {Bousso, Raphael},
  title   = {The holographic principle},
  journal = {Reviews of Modern Physics},
  volume  = {74},
  pages   = {825},
  year    = {2002},
  eprint  = {hep-th/0203101},
  archivePrefix = {arXiv},
}
```
