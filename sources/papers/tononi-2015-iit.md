---
type: paper
title: "Consciousness: here, there and everywhere?"
aliases:
  - "Tononi 2015"
  - "IIT 3.0 review"
authors:
  - Tononi, Giulio
  - Koch, Christof
year: 2015
arxiv: null
url: https://doi.org/10.1098/rstb.2014.0167
tags:
  - cluster/participatory/consciousness
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/neuroscience
  - field/philosophy
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Consciousness: here, there and everywhere?

> [!info] Citation
> Tononi, G., & Koch, C. (2015). "Consciousness: here, there and everywhere?" *Philosophical Transactions of the Royal Society B*, 370: 20140167. https://doi.org/10.1098/rstb.2014.0167

## TL;DR
This review presents Integrated Information Theory (IIT), a formal and quantitative theory of consciousness that derives physical requirements for experience from five phenomenological axioms (intrinsic existence, composition, information, integration, exclusion). The central quantity is Phi (Φ), or integrated information, which measures the intrinsic irreducibility of a system's cause-effect structure; consciousness is identified with a maximally irreducible conceptual structure (a "quale") formed by a complex of mechanisms in a state. IIT explains why the cerebral cortex but not the cerebellum generates consciousness, predicts that feed-forward networks and digital simulations of brains are not conscious, and implies that consciousness is a graded, fundamental property of physical systems with sufficient causal integration.

## Problem & setting
Behavioural and neural correlates of consciousness (BCC, NCC) are insufficient to answer where consciousness is present — in brain-damaged patients, preterm infants, non-mammalian species, or machines. The "hard problem" resists purely neural explanations. IIT addresses this by reversing the standard strategy: rather than asking how the brain produces experience, it starts from consciousness itself, identifies its essential properties as axioms, and derives postulates about what physical substrates must satisfy.

## Method
IIT proceeds in three steps. First, five axioms characterize every possible experience: (1) intrinsic existence — experience is real from its own perspective; (2) composition — experience has structure built from elementary and higher-order distinctions; (3) information — experience is specific (it is one particular thing and not others); (4) integration — experience is unified and irreducible to independent parts; (5) exclusion — experience is definite in content and spatio-temporal grain. Second, corresponding postulates translate these into requirements on physical mechanisms: a system must have cause-effect power upon itself, be structured into compositions of mechanisms, specify a particular cause-effect structure, have that structure be intrinsically irreducible (Phi > 0 across its minimum information partition, MIP), and the maximally irreducible cause-effect structure (Phi_max) must exclude overlapping alternatives. Third, the central identity: an experience is identical to the maximally irreducible conceptual structure (quale) specified by a complex of mechanisms in a state. The quantity of consciousness is Phi_max; the quality is the shape of the conceptual structure in high-dimensional cause-effect space (qualia space), where each concept is a point whose size is its irreducibility phi_max and the constellation of all concepts defines the quale.

## Key results
IIT provides a principled, parsimonious account of several major empirical puzzles: the cerebral cortex (functionally specialized yet highly integrated) has high Phi_max, while the cerebellum (modular, near-independent processing) has low Phi_max. The perturbational complexity index (PCI), a scalar measure of EEG response compressibility after TMS inspired by IIT, reliably decreases in all conditions of loss of consciousness (deep sleep, anaesthesia, vegetative state) and remains high in conscious subjects and locked-in patients. A counterintuitive prediction: silent neurons still contribute to consciousness because they specify cause-effect repertoires just as active ones do. Feed-forward networks (including deep learning architectures) have Phi = 0 and are thus "zombies" — they can be behaviourally equivalent to feedback networks with Phi > 0 yet have no experience. Digital brain simulations similarly cannot be conscious because simulation is virtual (no real cause-effect power), just as a simulated star does not bend spacetime. The theory implies consciousness is graded (common across the animal kingdom), that aggregates of low-Phi systems do not combine into a higher-Phi whole (solving the panpsychist "combination problem"), and that multiple independent complexes can coexist in a single brain.

## Relevance to this research
IIT's framework carries several points of contact with the VFE/participatory research program. The identification of consciousness with a maximally irreducible cause-effect structure, characterized by Phi as a scalar measure of integration, resonates structurally with variational free energy (VFE) minimization: both frameworks define a scalar functional over belief or state distributions whose extrema characterize a system's "self-model." The distinction between the quantity of experience (Phi_max) and its quality (the shape of the conceptual structure in qualia space) parallels the VFE decomposition into a scalar free energy and the full belief geometry (mu, Sigma in SPD space). The exclusion postulate — only the maximally irreducible complex "exists" — is an instance of a Bayesian Occam's razor or model selection principle, analogous to complexity regularization in variational inference. The claim that feed-forward networks are not conscious because they lack intrinsic cause-effect power is directly relevant to the VFE transformer's design principle of iterative belief updating with recurrent coupling (beta_ij, gamma_ij attention) rather than a purely feed-forward pass; the recurrent Bayesian belief coupling is precisely the kind of integration IIT requires. The participatory-realism connection is explicit: IIT holds that consciousness is an observer-independent, intrinsic property, which parallels the "it from bit" and participatory approaches to ontology discussed in PIFB.tex. For the multi-agent model (MAgent_Model), IIT's treatment of aggregates (groups do not form super-complexes) constrains how collective consciousness should or should not emerge from multi-agent VFE interactions — the social coupling terms (gamma_ij) may raise group Phi without creating a superordinate complex.

## Cross-links
- Concepts: [[tononi-2004-integrated-information|Integrated Information Theory]], [[Consciousness]], [[Variational Free Energy]], [[fuchs-2017-participatory-realism|Participatory Realism]]
- Related sources: [[friston-2010-free-energy-principle|friston-2010-free-energy]], [[wheeler-1990-it-from-bit]]
- Manuscript/Project: [[VFE Transformer Program]], [[Participatory realism (it from bit)|PIFB]]

## BibTeX
```bibtex
@article{Tononi2015,
  author  = {Tononi, Giulio and Koch, Christof},
  title   = {Consciousness: here, there and everywhere?},
  journal = {Philosophical Transactions of the Royal Society B},
  year    = {2015},
  volume  = {370},
  pages   = {20140167},
  doi     = {10.1098/rstb.2014.0167},
}
```
