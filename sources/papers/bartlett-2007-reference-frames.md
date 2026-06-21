---
type: paper
title: "Reference frames, superselection rules, and quantum information"
aliases:
  - Bartlett 2007
  - BRS2007
  - bartlett-rudolph-spekkens-2007-reference-frames
  - Bartlett
  - Rudolph & Spekkens 2007
  - BRS 2007
  - Reference frames review
authors:
  - Bartlett, Stephen D.
  - Rudolph, Terry
  - Spekkens, Robert W.
year: 2007
arxiv: quant-ph/0610030
url: https://arxiv.org/abs/quant-ph/0610030
tags:
  - cluster/gauge-theory
  - cluster/participatory/quantum-foundations
  - project/transformer
  - project/multi-agent
  - field/physics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Reference frames, superselection rules, and quantum information

> [!info] Citation
> Bartlett, S. D., Rudolph, T., & Spekkens, R. W. (2007). "Reference frames, superselection rules, and quantum information." *Reviews of Modern Physics*, 79(2), 555–609. DOI: 10.1103/RevModPhys.79.555. arXiv:quant-ph/0610030.

## TL;DR
This review establishes a unified framework showing that lacking a reference frame for a symmetry group G is mathematically equivalent to a superselection rule associated with G. The key technical tool is G-twirling — averaging states or operations over the group's Haar measure — which decomposes Hilbert space into decoherence-full gauge subsystems and decoherence-free multiplicity subsystems. The paper surveys communication, cryptography, entanglement, and frame-alignment tasks under this restriction, demonstrating that quantum information processing can often be performed as efficiently without a shared reference frame as with one, via relational encodings into decoherence-free subsystems.

## Problem & setting
Classical and quantum information protocols implicitly assume parties share reference frames (Cartesian axes, clocks, phase references). When parties lack a shared reference frame, the relevant symmetry group G acts as collective noise. The paper asks: how does the absence of a shared RF constrain quantum information tasks, and can these constraints be circumvented? Prior work (Aharonov & Susskind 1967; Zanardi 2001; Knill et al. 2000) had addressed fragments; this review unifies them. The two running examples are U(1) phase references and SO(3)/SU(2) Cartesian frames.

## Method
The core formalism rests on the G-twirling superoperator
$$\mathcal{G}[\rho] = \int_G dg\, T(g)\rho T(g)^\dagger,$$
where $T$ is a unitary representation of the compact Lie group $G$ and $dg$ is the Haar measure. By Schur's lemmas the Hilbert space decomposes as
$$\mathcal{H} = \bigoplus_q \mathcal{H}_q, \quad \mathcal{H}_q = M_q \otimes N_q,$$
where $M_q$ carries irrep $q$ of $G$ (the gauge/decoherence-full subsystem) and $N_q$ carries the trivial representation (the multiplicity/decoherence-free subsystem). The theorem proved in Section II.C gives $\mathcal{G} = \sum_q (\mathcal{D}_{M_q} \otimes \mathcal{I}_{N_q}) \circ \mathcal{P}_q$, where $\mathcal{D}_{M_q}$ is the completely depolarizing map on $M_q$. States, operations, and POVMs that are G-invariant are then precisely those block-diagonal in the $\mathcal{H}_q$ sectors. Relational encodings into the $N_q$ (decoherence-free subsystems) allow communication, entanglement distribution, and cryptography without a shared RF. Frame alignment (Sec. V) uses covariant measurements, maximum-likelihood estimation, and figures of merit such as fidelity over the group.

## Key results
- Lacking a reference frame for group $G$ is operationally equivalent to a superselection rule for $G$: all accessible states, operations, and measurements are G-invariant (Sec. II.C theorem).
- For SU(2) collective noise on $N$ qubits: asymptotically one classical bit per qubit and one logical qubit per physical qubit can be transmitted without a shared Cartesian frame, matching the RF-assisted rate (Sec. III.A.2d).
- The two-mode single-photon state $(|01\rangle + |10\rangle)/\sqrt{2}$ is not operationally entangled under a local photon-number superselection rule, demonstrating that different notions of entanglement diverge under RF restrictions (Sec. III.C.1).
- Decoherence-free-subsystem based QKD without a shared polarization reference frame is provably unconditionally secure (Boileau et al. 2004/2005, Sec. III.B).
- Frame alignment of a direction or Cartesian frame using $N$ qubits achieves fidelity approaching 1 as $O(1/N^2)$ for phase references and $O(1/N)$ for SO(3) frames (Sec. V.D).
- Bounded reference frames become a quantifiable resource analogous to entanglement: interconversion, distillation, and degradation under use can all be analyzed (Sec. VI).

## Relevance to this research
The decomposition $\mathcal{H} = \bigoplus_q M_q \otimes N_q$ with decoherence-full gauge subsystems $M_q$ and decoherence-free multiplicity subsystems $N_q$ is structurally identical to the isotypic decomposition underlying the GL(K) gauge-equivariant attention mechanism: the $M_q$ correspond to the irrep carrier spaces on which the group acts (the gauge degrees of freedom that must be integrated out or transported equivariantly), and the $N_q$ correspond to the multiplicity spaces that carry the invariant (physical) information. The G-twirling map $\mathcal{G}$ is precisely the operation that projects onto G-invariant operators, mirroring how the VFE transport $\Omega_{ij}$ must preserve gauge invariance of the free energy. The paper's framework also clarifies why relational encodings (encoding information in relative degrees of freedom between subsystems) are the correct strategy when absolute frames are absent — directly motivating the KL divergence terms $\text{KL}(q_i \| \Omega_{ij} q_j)$ in the VFE free energy as relational comparisons of beliefs across positions. The superselection-rule/twirling duality provides a rigorous quantum-information-theoretic foundation for the participatory/gauge-frame perspective developed in PIFB.tex.

## Cross-links
- Concepts: [[Gauge Equivariance]], [[Superselection Rules]], [[Decoherence-Free Subsystems]], [[Irreducible Representations]], [[G-Twirling]], [[Reference Frames]], [[Quantum reference frames]], [[Gauge transformation]], [[Parallel transport]], [[Holonomy]], [[Participatory realism (it from bit)]], [[Agents as fibre-bundle sections]]
- Related sources: [[spekkens-2007-epistemic]], [[chiribella-2016-quantum-from-principles]], [[giacomini-2019-qrf-covariance]], [[vanrietvelde-2020-change-of-perspective]]
- Manuscript/Project: [[GL(K) Attention]], [[VFE Transformer Program]], [[PIFB]], [[participatory-it-from-bit]]

> [!note] Editorial: BRS's "speakable" (frame-invariant, communicable) vs "unspeakable" (frame-relative — a direction, a phase, a time) information split is the operational license to read the per-agent gauge frame $\phi_i$ as a *genuine physical reference frame* rather than a bookkeeping convenience: the project's [[Gauge transformation]] $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ is exactly a change of reference frame, [[Parallel transport]] of a belief from frame $i$ to $j$ is the inferential analogue of aligning two physical frames, and the unremovable residue when frames cannot be globally aligned is [[Holonomy]].

## BibTeX
```bibtex
@article{BartlettRudolphSpekkens2007,
  author  = {Bartlett, Stephen D. and Rudolph, Terry and Spekkens, Robert W.},
  title   = {Reference frames, superselection rules, and quantum information},
  journal = {Reviews of Modern Physics},
  volume  = {79},
  number  = {2},
  pages   = {555--609},
  year    = {2007},
  doi     = {10.1103/RevModPhys.79.555},
  eprint  = {quant-ph/0610030},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
}
```
