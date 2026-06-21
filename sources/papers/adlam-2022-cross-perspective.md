---
type: paper
title: "Information is Physical: Cross-Perspective Links in Relational Quantum Mechanics"
aliases:
  - Adlam Rovelli 2022
  - cross-perspective links RQM
  - adlam-rovelli-2022-cross-perspective
  - Adlam & Rovelli 2022
  - Cross-perspective links
  - RQM cross-perspective
authors:
  - Adlam, Emily
  - Rovelli, Carlo
year: 2022
arxiv: "2203.13342"
url: https://arxiv.org/abs/2203.13342
tags:
  - cluster/participatory/quantum-foundations
  - cluster/participatory/philosophy-of-mind
  - cluster/gauge-theory
  - project/multi-agent
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Information is Physical: Cross-Perspective Links in Relational Quantum Mechanics

> [!info] Citation
> Adlam, Emily and Rovelli, Carlo (2022). "Information is Physical: Cross-Perspective Links in Relational Quantum Mechanics." *Philosophy of Physics* (2023). Preprint: arXiv:2203.13342 [quant-ph]. https://arxiv.org/abs/2203.13342

## TL;DR
Relational quantum mechanics (RQM) holds that quantum states are always relative to an observer, but this creates a tension with the principle that information is physical: an observer's subjective measurement outcome appears inaccessible to others, verging on solipsism. Adlam and Rovelli resolve this by introducing a new postulate — cross-perspective links — which guarantees that information an observer acquires about a variable is stored in their physical variables and is therefore accessible by measurement to any other observer, underwriting intersubjective agreement and empirical confirmability within RQM. The paper also proposes a refined ontology in which quantum states remain relational while quantum events themselves are observer-independent, absolute facts.

## Problem & setting
Standard formulations of RQM postulate (i) that quantum states are purely relational (relative to an observer) and (ii) that it is meaningless to compare accounts from different perspectives except relative to a third observer. A consequence is that when Alice obtains a measurement outcome it is stored only in her subjective perspective, not in any physical variable accessible to Bob — violating the naturalistic principle "information is physical." This makes empirical confirmation appear impossible and exposes RQM to a solipsism objection. Prior work by Van Fraassen proposed related constraints but still relativized them to an additional observer, leaving the fundamental problem unresolved.

## Method
The authors replace the old postulate of "relativity of comparisons" with the postulate of **cross-perspective links**: if Alice measures variable $V$ of system $S$, and the information about $V$ is not subsequently destroyed in Alice's physical variables, then any observer Bob who measures the physical variable representing Alice's record of $V$ will obtain a result matching Alice's. Information destruction is quantified via the Heisenberg disturbance relation $\delta A_V \delta A_Q \propto \hbar$: measuring a conjugate variable $A_Q$ with precision $\delta A_Q$ disturbs $A_V$ by an inversely proportional amount. The postulate is time-symmetric and can be restated as: consecutive interactions involving the same variable must produce matching definite values, with no causal priority between them. The ontology is refined to a sparse-flash picture in which quantum events (flashes) are absolute, observer-independent facts, whereas quantum states remain relational descriptions of the joint history of an observer and a system.

## Key results
The cross-perspective links postulate, combined with the existing "internally consistent descriptions" postulate, entails that $M^S_B = M^A_B = M_A$ — Bob's direct measurement of $S$, his readout of Alice's record, and Alice's own outcome all agree. This produces a stable set of intersubjective facts from a substratum of relational ones. Decoherence ensures that these stable facts emerge rapidly for macroscopic observers. The postulate dissolves the solipsism objection (observers can align perspectives via measurement and communication), resolves the systems-and-subsystems puzzle (brain particles rapidly share information through decoherence, yielding a coherent subjective perspective), addresses the preferred-basis problem, and clarifies the Frauchiger-Renner scenario. The epistemic/ontic distinction for the quantum state dissolves: because knowledge is itself physical, a relational quantum state is simultaneously an epistemic description of history and an ontic feature of reality. The resulting ontology is nonlocal but not in any signalling-violating or frame-preferring sense; the laws of nature apply atemporally to the entire distribution of quantum events.

## Relevance to this research
This paper is a core reference for the **participatory realism** philosophical backbone of the VFE/GL(K) research program. The key connections are:

**Participatory ontology and "it from bit."** The cross-perspective links paper is the technical companion to Wheeler's "it from bit" thesis: physical reality is constituted by observer-system interactions (quantum events), and what makes those events real is precisely that the information is stored in physical variables accessible to all observers. This is the quantum-foundations underpinning of participatory realism as developed in the companion manuscript PIFB.tex.

**Relational beliefs and VFE beliefs.** RQM's quantum state is a relational description of the joint history of an observer and a system — formally analogous to how beliefs $q_i$ in the VFE framework describe the relation between an agent $i$ and the environment, not an absolute property of either. The cross-perspective links mechanism (information stored in physical variables, accessible via measurement) parallels the mechanism by which VFE belief updates propagate across agents through the $\beta_{ij} \cdot \text{KL}(q_i \| \Omega_{ij} q_j)$ coupling terms.

**Intersubjective agreement and multi-agent consensus.** The paper's core result — that observers can achieve intersubjective agreement about quantum events through appropriate measurements — is structurally analogous to the multi-agent VFE model's convergence to shared beliefs at free-energy minima. The gauge transport operators $\Omega_{ij}$ play the role of the physical measurement channel Bob uses to read Alice's record.

**Observer-independence of events vs. relativity of states.** The distinction between absolute quantum events and relational quantum states maps onto the distinction between the (observer-independent) free energy functional $F$ and the (agent-relative, gauge-transformed) belief distributions $q_i$. The invariant quantity in both cases is the event/value, not the state/representation.

**Information is physical.** The principle that knowledge is stored in physical variables connects directly to the information-geometric perspective underlying VFE: beliefs are not abstract probability distributions but are encoded in physical (neural/computational) substrate, and their geometry (SPD matrices, Fisher metric) reflects the physical constraints of that substrate.

## Cross-links
- Concepts: [[fuchs-2017-participatory-realism|Participatory Realism]] · [[Relational Quantum Mechanics]] · [[Information is Physical]] · [[Parallel transport]] · [[Holonomy]] · [[Gauge transformation]] · [[Agents as fibre-bundle sections]]
- Related sources: [[wheeler-1990-it-from-bit|wheeler-1989-it-from-bit]] · [[rovelli-1996-relational-qm]] · [[friston-2019-particular-physics|friston-2019-free-energy]] · [[brukner-2018-no-go-observer-facts]] · [[frauchiger-renner-2018-no-self-description]]
- Manuscript/Project: [[Participatory realism (it from bit)|PIFB]] · [[participatory-it-from-bit]] · [[VFE Transformer Program]] · [[GL(K) gauge-equivariant attention|GL(K) Attention]]

> [!note] Editorial: Adlam-Rovelli's "cross-perspective links" are the closest existing-physics analogue of the project's inter-agent transport map $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ — a fact in one frame is physically readable in another, consistently — which the project *constructs* as [[Parallel transport]] of beliefs along a connection, with the residual disagreement quantified by [[Holonomy]].

## BibTeX
```bibtex
@article{AdlamRovelli2022,
  author  = {Adlam, Emily and Rovelli, Carlo},
  title   = {Information is Physical: Cross-Perspective Links in Relational Quantum Mechanics},
  journal = {Philosophy of Physics},
  year    = {2023},
  eprint  = {2203.13342},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
  url     = {https://arxiv.org/abs/2203.13342},
  note    = {Preprint arXiv:2203.13342 (2022); published in Philosophy of Physics (2023)},
}
```
