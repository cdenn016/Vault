---
type: paper
title: "What is the Unity of Consciousness?"
aliases:
  - "Bayne Chalmers 2005"
  - "Unity of Consciousness Bayne"
  - "Unity of Consciousness"
authors:
  - Bayne, Tim
  - Chalmers, David J.
year: 2005
arxiv: null
url: null
tags:
  - cluster/participatory/consciousness
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/philosophy
  - field/neuroscience
  - field/psychology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# What is the Unity of Consciousness?

> [!info] Citation
> Bayne, Tim and Chalmers, David J. (2005). "What is the Unity of Consciousness?" In A. Cleeremans (ed.), *The Unity of Consciousness: Binding, Integration, Dissociation*. Oxford University Press, 2003.

## TL;DR
Bayne and Chalmers taxonomize the varieties of conscious unity and argue that phenomenal unity — the thesis that any set of phenomenal states of a subject at a time is subsumed by a single encompassing phenomenal state — is both the most substantive and most defensible form of the unity thesis. They distinguish phenomenal unity from access unity, show that access unity demonstrably fails (via Sperling's partial-report experiments), and argue that phenomenal unity places non-trivial constraints on theories of consciousness. The paper defends the Phenomenal Unity Thesis as a plausible, non-trivial claim while remaining agnostic about its ultimate truth.

## Problem & setting
Conscious experience presents a multiplicity of simultaneous states — visual, auditory, bodily, emotional, cognitive — yet these states seem to belong together as aspects of a single encompassing consciousness. The paper asks: (1) what precisely is the unity of consciousness? (2) is it necessarily true? and (3) how might it be explained? Prior work (Descartes, Kant) held unity to be an essential feature of mind; others (Nagel 1971, Dennett 1992) denied it or treated it as illusory, especially in light of split-brain cases. The paper treats the Unity Thesis — "Necessarily, any set of conscious states of a subject at a time is unified" — as the target, seeking a reading under which it is substantive rather than trivial or obviously false.

## Method
The authors proceed by conceptual analysis and taxonomy. They distinguish four varieties of unity:

- **Objectual unity**: two states directed at the same object (tied to the binding problem in cognitive neuroscience; the corresponding unity thesis is likely false, since most states are not co-directed).
- **Spatial unity**: states that represent objects as part of the same phenomenal space (fails for non-spatial states such as emotions and abstract thoughts).
- **Subject unity**: states had by the same subject at the same time (trivially true by definition; uninformative).
- **Subsumptive unity**: states both subsumed by a single encompassing state of consciousness — the "total phenomenal state."

They then cross-classify with Block's (1995) access/phenomenal distinction to obtain the two central notions. **Access unity**: two states are access-unified when the conjunction of their contents is jointly accessible for report, reasoning, and behavioral control. **Phenomenal unity**: two states are phenomenally unified when there is something it is like to be in both simultaneously — a conjoint phenomenology that subsumes the individual phenomenologies.

The **Phenomenal Unity Thesis (PUT)** is formulated as: Necessarily, any set of phenomenal states of a subject at a time is phenomenally unified (equivalently: the subject always has a total phenomenal state). The **Access Unity Thesis (AUT)** is the parallel claim for access-conscious states.

## Key results
The Access Unity Thesis is shown to be straightforwardly false. Sperling's (1960) partial-report experiment demonstrates that subjects have access to each of three rows of a 3×4 letter matrix individually (reporting ~3.3/4 letters per row when cued) but not to the conjunction of all rows (reporting only ~4.5/12 when required to report all). This access bottleneck shows that two access-conscious states can fail to be access-unified. The authors conclude that access unity, even in its pairwise form, fails empirically.

The Phenomenal Unity Thesis is defended as non-trivial: some philosophers (e.g., Hurley 1998) explicitly entertain its denial, and certain popular theories of consciousness (identified in sections not reproduced in the extracted text) are argued to be incompatible with it, showing it has substantive theoretical force. The total and original (full-set) versions of the PUT are shown to be equivalent under transitivity of subsumption; the pairwise PUT entails the full PUT for finite sets. The authors do not claim to prove the PUT, but argue it is plausible, captures a deep intuition, and faces no knockdown objection.

## Relevance to this research
The paper is directly relevant to the participatory-realism and consciousness threads of this research program, particularly the PIFB manuscript (Participatory It-From-Bit), which situates phenomenal unity within an information-theoretic and participatory ontology. Several connections are notable.

The distinction between access unity (which breaks down at information-processing bottlenecks) and phenomenal unity (the global "total phenomenal state") maps naturally onto the distinction between local belief-propagation messages and the global VFE minimum in the transformer model: the free-energy landscape itself enforces a kind of global coherence that need not correspond to pairwise accessibility. The Sperling bottleneck is structurally analogous to bounded attention in the GL(K) attention mechanism, where softmax weights distribute finite capacity across tokens, yet the joint VFE is globally well-defined. The "total phenomenal state" idea — a single encompassing phenomenal state that subsumes all others — resonates with the hyper-prior level of the VFE hierarchy (h → s → p → q → observations), where the hyper-prior plays the role of the unifying "conscious field" across agents or layers. The paper's insistence that phenomenal unity is non-trivial (not merely the conjunction of states, but requiring that conjunction itself to be a phenomenal state) parallels the requirement in VFE theory that the joint belief distribution be a well-defined Gaussian, not merely a product of marginals — a covariance structure that can fail in degenerate cases.

## Cross-links
- Concepts: [[Unity of Consciousness]] · [[Phenomenal Consciousness]] · [[Access Consciousness]] · [[Binding Problem]]
- Related sources: [[Cleeremans-unity-consciousness]] · [[Block-access-phenomenal]] · [[Hurley1998]]
- Manuscript/Project: [[PIFB]] · [[VFE Transformer Program]] · [[GL(K) Attention Manuscript]]

## BibTeX
```bibtex
@incollection{Bayne2005,
  author    = {Bayne, Tim and Chalmers, David J.},
  title     = {What is the Unity of Consciousness?},
  booktitle = {The Unity of Consciousness: Binding, Integration, Dissociation},
  editor    = {Cleeremans, Axel},
  publisher = {Oxford University Press},
  year      = {2003},
}
```
