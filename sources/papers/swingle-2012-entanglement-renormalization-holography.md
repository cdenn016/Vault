---
type: paper
title: "Entanglement Renormalization and Holography"
aliases:
  - Swingle 2012
  - ER=MERA
  - swingle-2012-entanglement-renormalization
  - MERA = Holography
authors:
  - Swingle, Brian
year: 2012
arxiv: "0905.1317"
url: https://doi.org/10.1103/PhysRevD.86.065007
tags:
  - cluster/gauge-theory
  - cluster/participatory
  - cluster/participatory/quantum-foundations
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Entanglement Renormalization and Holography

> [!info] Citation
> Swingle, B. (2012). "Entanglement Renormalization and Holography." *Phys. Rev. D* 86(6): 065007. DOI: [10.1103/PhysRevD.86.065007](https://doi.org/10.1103/PhysRevD.86.065007). arXiv:0905.1317.

> [!note] Citation correction (2026-06-21): An earlier ingest recorded this as *Phys. Rev. B* 86, 045117 — that is **wrong**. The published venue is *Physical Review D* 86(6): 065007 (DOI 10.1103/PhysRevD.86.065007), confirmed by the refs/ note on merge.

## TL;DR
Swingle shows that the tensor network structure of entanglement renormalization (MERA) naturally gives rise to an emergent higher-dimensional holographic geometry, with the extra dimension corresponding to coarse-graining scale. At a quantum critical point the emergent geometry is a discrete version of anti-de Sitter (AdS) space, recovering the Ryu-Takayanagi minimal-surface formula for entanglement entropy as a consequence of the causal-cone structure of the network. This establishes a concrete, lattice-level bridge between real-space renormalization group methods and holographic gauge/gravity duality.

## Problem & setting
Quantum many-body ground states occupy an exponentially large Hilbert space yet appear to be relatively lightly entangled (area-law entropy). Traditional symmetry-breaking descriptions miss long-range entanglement characteristic of topological phases. Entanglement renormalization (MERA, Vidal 2007/2008) provides a multi-scale tensor-network description that iteratively removes local entanglement via disentanglers and coarse-graining isometries, producing a layered network with one layer per RG scale. Holographic gauge/gravity duality (Maldacena, Gubser-Klebanov-Polyakov, Witten 1998) maps strongly coupled quantum field theories to classical gravity in a curved higher-dimensional bulk. The question is whether these two ideas — developed independently — are secretly the same construction.

## Method
Swingle defines a bulk geometry directly from the entanglement structure of a quantum state encoded in a MERA network. Each tensor in the network is assigned a "cell" whose size is proportional to the local entanglement entropy $S_{\text{site}}$; the connectivity of cells mirrors the wiring of the quantum circuit. The entanglement entropy of a boundary block is bounded above by the length (in these cell units) of the minimal curve in the bulk — the boundary of the causal cone of the block. For the quantum Ising chain at criticality ($g=1$), scale invariance forces all layers to be equivalent, giving an infinite emergent geometry with the AdS$_2$ metric

$$ds^2 = R^2 \frac{dz^2 + dx^2}{z^2},$$

where $z \sim e^{\text{layer depth}}$ is the coarse-graining scale. Finite temperature introduces a "black-hole-like" scale where the coarse-grained density matrix becomes completely mixed, giving an extensive entropy contribution analogous to black-hole thermodynamics. Correlation functions of conformal primary operators go as $e^{-\Delta \ell}$, where $\ell$ is the geodesic length in AdS, recovering the standard holographic two-point function.

## Key results
The entanglement entropy of a block of sites in the ultraviolet lattice is bounded by the length of a minimal bulk curve, and at the quantum critical point this bound is saturated and equals $(c/3)\log L$ — consistent with CFT and the Ryu-Takayanagi formula. Gapped phases give a finite-depth geometry that terminates at a factorization scale, reproducing exponentially decaying correlations. Finite-temperature critical states give geometries containing a black-hole-like horizon at the hydrodynamic scale, producing an extensive entropy contribution on top of the boundary term. Redundant choices of renormalization group transformation are interpretable as bulk diffeomorphisms.

## Relevance to this research
The MERA/holography correspondence is directly relevant to the VFE transformer program in several ways. First, the construction shows that iterative variational minimization over a hierarchy of belief states (the VFE hierarchy $h \to s \to p \to q \to o$) is the information-theoretic analog of entanglement renormalization: each level of the hierarchy coarse-grains beliefs, and the "geometry" of the emergent representation is controlled by the KL divergences (free energies) at each scale. Second, the appearance of AdS geometry from a discrete, layer-wise tensor network suggests that the per-layer attention geometry in the GL(K)-equivariant transformer may have a natural holographic interpretation, with the depth of the network playing the role of the radial AdS coordinate. Third, the Ryu-Takayanagi formula — entropy = minimal surface area — is structurally parallel to the variational free-energy bound: both express an entropic quantity as an extremal geometric object. Fourth, gauge/gravity duality's role for bulk fields (renormalized couplings obeying RG equations) is analogous to how the VFE transformer's gauge connection encodes inter-layer transport in the belief hierarchy. This paper is foundational for understanding why deep hierarchical belief propagation with geometric structure might naturally give rise to AdS-like emergent spaces.

> [!note] Ouroboros-tower framing (from refs/ note): The MERA scale tower is the structural template for the program's **Ouroboros Tower**: both stack gauge-covariant coarse-grainings, one rung per scale, and in both the geometry of the tower *is* the [[Renormalization-group flow of beliefs]]. Swingle's "RG depth = bulk radial coordinate" is the precedent PIFB leans on when asking whether its own scale index can play the role of an emergent dimension; the minimal-cut/Ryu–Takayanagi correspondence is the entanglement-side mirror of belief-coupling cuts in the program's coupling graph. A HIGH-priority node bridging the [[Emergent spacetime and holography]] theme to the program's multi-scale machinery.

## Cross-links
- Concepts: [[Emergent spacetime and holography|Entanglement Renormalization]]
- Concepts: [[Emergent spacetime and holography|Holography]]
- Concepts: [[Emergent spacetime and holography|Anti-de Sitter Space]]
- Concepts: [[Renormalization-group flow of beliefs]], [[Ouroboros multi-scale dynamics]], [[Meta-agents and hierarchical emergence]], [[Emergent spacetime and holography]]
- Related sources: [[ryu-takayanagi-2006-holographic-entanglement-entropy|ryu-takayanagi-2006-holographic-derivation]], [[ryu-takayanagi-2006-holographic-entanglement-entropy]], [[vidal-2007-entanglement-renormalization]]
- Manuscript/Project: [[VFE Transformer Program]], [[participatory-it-from-bit]]

## BibTeX
```bibtex
@article{Swingle2012,
  author  = {Swingle, Brian},
  title   = {Entanglement Renormalization and Holography},
  journal = {Physical Review D},
  volume  = {86},
  number  = {6},
  pages   = {065007},
  year    = {2012},
  eprint  = {0905.1317},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th},
  doi     = {10.1103/PhysRevD.86.065007},
}
```
